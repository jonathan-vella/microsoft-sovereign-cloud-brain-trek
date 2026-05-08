#!/usr/bin/env python3
"""Terminology linter (Phase 2.1, 2.7).

Plan reference: copilot-instructions.md glossary, §D, §G.

Severity buckets:
  P0  contradicts authoritative glossary in a published page
  P2  stylistic preference

--fix mode performs only context-free substitutions; ambiguous matches
are reported but never auto-replaced.

Migration narratives (lines containing "(legacy)", "previously known as",
"formerly", or "Stack HCI" inside the same paragraph as "Azure Local")
are skipped — they intentionally name old products.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

FRONTMATTER_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)


@dataclass(frozen=True)
class Rule:
    pattern: str
    replacement: str
    severity: str
    code: str
    description: str
    safe_fix: bool
    case_sensitive: bool = False


# Order matters: longer / more specific patterns first.
RULES: list[Rule] = [
    Rule(
        pattern=r"\bAzure\s+Active\s+Directory\b(?!\s*\(legacy\))",
        replacement="Microsoft Entra ID",
        severity="P0",
        code="TERM-AAD",
        description="Azure Active Directory → Microsoft Entra ID",
        safe_fix=True,
    ),
    Rule(
        pattern=r"\bAAD\b",
        replacement="Microsoft Entra ID",
        severity="P0",
        code="TERM-AAD-ABBR",
        description="AAD → Microsoft Entra ID",
        safe_fix=False,  # ambiguous in code/scripts; flag only
        case_sensitive=True,
    ),
    Rule(
        # Bad forms only, case-sensitive: EdgeRAG, edgerag, edge_rag, edge-rag (when not in URL slug)
        # Correct form "Edge RAG" is intentionally NOT matched.
        pattern=r"\b(?:EdgeRAG|edgeRAG|edgerag|edge_rag)\b",
        replacement="Edge RAG",
        severity="P0",
        code="TERM-EDGERAG",
        description="EdgeRAG/edgerag/edge_rag → Edge RAG",
        safe_fix=True,
        case_sensitive=True,
    ),
    Rule(
        # "edge-rag" in prose only — not in URL slugs (these are legitimate Microsoft Learn paths).
        # The URL filter happens in lint_and_fix() by skipping matches inside ](...) or after :// .
        pattern=r"\bedge-rag\b",
        replacement="Edge RAG",
        severity="P0",
        code="TERM-EDGERAG-HYPH",
        description="edge-rag (prose) → Edge RAG",
        safe_fix=False,  # context-sensitive (URLs); flag only, manual review
        case_sensitive=True,
    ),
    Rule(
        # Avoid migration narratives explicitly: skip when paragraph mentions "legacy"/"formerly"
        pattern=r"\bAzure\s+Stack\s+HCI\b(?!\s*\(legacy\))",
        replacement="Azure Local",
        severity="P0",
        code="TERM-HCI",
        description="Azure Stack HCI → Azure Local (outside migration narratives)",
        safe_fix=False,  # context-sensitive; report only, sweep manually
    ),
    Rule(
        # Detect lowercase form only — "Sovereign Landing Zone" is the canonical form.
        pattern=r"\bsovereign\s+landing\s+zone\b",
        replacement="Sovereign Landing Zone",
        severity="P2",
        code="TERM-SLZ-CASE",
        description="lowercase 'sovereign landing zone' → 'Sovereign Landing Zone'",
        safe_fix=True,
        case_sensitive=True,
    ),
    Rule(
        pattern=r"\bcustomer\s+lockbox\b",
        replacement="Customer Lockbox",
        severity="P2",
        code="TERM-LOCKBOX",
        description="customer lockbox → Customer Lockbox",
        safe_fix=True,
        case_sensitive=True,
    ),
    Rule(
        pattern=r"\bair[\s_]gapped\b|\bairgapped\b",
        replacement="air-gapped",
        severity="P2",
        code="TERM-AIRGAPPED",
        description="air gapped/airgapped → air-gapped",
        safe_fix=True,
    ),
]

CODEBLOCK_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`]+`")
# Markdown link URL: `](http...)` or `](path/to/page)` — the URL portion only.
LINK_URL_RE = re.compile(r"\]\(([^)]+)\)")
# Bare URL
BARE_URL_RE = re.compile(r"https?://\S+")
# Filename / file-path tokens (e.g., edge-rag-architecture.svg, docs/level-200/foo.md).
# Common doc-asset and source extensions only — keeps prose rules from flagging file names.
FILENAME_RE = re.compile(
    r"\b[\w./\\-]+\.(?:svg|png|jpg|jpeg|gif|webp|md|html?|css|js|ts|json|ya?ml|sh|ps1|py|tf|bicep|drawio|toml|ini|csv|log|txt)\b",
    re.IGNORECASE,
)
PARAGRAPH_RE = re.compile(r"\n\s*\n")


def _mask_code(text: str) -> tuple[str, list[tuple[int, str]]]:
    """Replace fenced + inline code AND link URLs and bare URLs with placeholders.

    Link URL slugs (e.g., `azure-arc/edge-rag/`) and code samples are not prose,
    and rules should never alter or flag them.
    """
    placeholders: list[tuple[int, str]] = []

    def _sub_full(m: re.Match[str]) -> str:
        placeholders.append((len(placeholders), m.group(0)))
        return f"\x00P{len(placeholders) - 1}\x00"

    def _sub_url(m: re.Match[str]) -> str:
        # Preserve the `](...)` shell so link text remains scannable;
        # only the URL inside parens is masked.
        placeholders.append((len(placeholders), m.group(1)))
        return f"](\x00P{len(placeholders) - 1}\x00)"

    masked = CODEBLOCK_RE.sub(_sub_full, text)
    masked = INLINE_CODE_RE.sub(_sub_full, masked)
    masked = LINK_URL_RE.sub(_sub_url, masked)
    masked = BARE_URL_RE.sub(_sub_full, masked)
    masked = FILENAME_RE.sub(_sub_full, masked)
    return masked, placeholders


def _unmask(text: str, placeholders: list[tuple[int, str]]) -> str:
    # Iterate in reverse-creation order so nested placeholders unwind
    # correctly. (A later placeholder may contain the literal pattern of
    # an earlier placeholder if regexes overlapped, e.g. when a markdown
    # link's text portion is itself a URL: `[https://x](https://x)`.)
    for idx, original in reversed(placeholders):
        text = text.replace(f"\x00P{idx}\x00", original)
    return text


def _is_migration_paragraph(paragraph: str) -> bool:
    """Heuristic: returns True if paragraph is intentionally describing the
    Azure Stack HCI → Azure Local rename / history.
    """
    low = paragraph.lower()
    keywords = (
        "legacy",
        "formerly",
        "previously known",
        "previously called",
        "rebrand",
        "rebranded",
        "renamed",
        "history",
        "evolution",
        "era",
        "from azure stack hci",
        "stack hci to azure local",
    )
    if any(k in low for k in keywords):
        return True
    # Heading paragraphs like "### From X to Y" — short heading that mentions both names
    if "stack hci" in low and "azure local" in low and len(paragraph) < 200:
        return True
    return False


def lint_and_fix(text: str, do_fix: bool) -> tuple[str, list[tuple[str, str, str, int]]]:
    findings: list[tuple[str, str, str, int]] = []
    # Don't touch front-matter
    fm_m = FRONTMATTER_RE.match(text)
    fm = fm_m.group(0) if fm_m else ""
    body = text[len(fm):]

    masked, placeholders = _mask_code(body)
    paragraphs = PARAGRAPH_RE.split(masked)
    rebuilt: list[str] = []

    for para in paragraphs:
        new_para = para
        for rule in RULES:
            flags = 0 if rule.case_sensitive else re.IGNORECASE
            for m in re.finditer(rule.pattern, para, flags=flags):
                # Skip migration narratives for product-rename rules.
                # _is_migration_paragraph() detects "formerly", "previously known",
                # "renamed", etc.; both Azure Stack HCI → Azure Local and
                # Azure Active Directory → Microsoft Entra ID are documented
                # legacy product references.
                if rule.code in {"TERM-HCI", "TERM-AAD"} and _is_migration_paragraph(para):
                    continue
                line_no = para[: m.start()].count("\n")
                findings.append(
                    (rule.severity, rule.code, rule.description, line_no)
                )
                if do_fix and rule.safe_fix:
                    new_para = re.sub(
                        rule.pattern,
                        rule.replacement,
                        new_para,
                        flags=flags,
                    )
                    break  # one rule pass per paragraph; re-run audit if needed
        rebuilt.append(new_para)

    new_body = "\n\n".join(rebuilt)
    new_body = _unmask(new_body, placeholders)
    return fm + new_body, findings


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--docs-root", default="docs", type=Path)
    p.add_argument("--fix", action="store_true")
    p.add_argument(
        "--out",
        default="scripts/review/reports/terminology.txt",
        type=Path,
    )
    args = p.parse_args(argv)

    files = sorted(args.docs_root.rglob("*.md"))
    out_lines: list[str] = []
    fixed_files = 0
    for md in files:
        text = md.read_text(encoding="utf-8")
        new_text, findings = lint_and_fix(text, args.fix)
        rel = md.relative_to(args.docs_root)
        for sev, code, desc, line in findings:
            out_lines.append(f"{sev} {code} {rel}: line~{line + 1} — {desc}")
        if args.fix and new_text != text:
            md.write_text(new_text, encoding="utf-8")
            fixed_files += 1

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(out_lines) + "\n", encoding="utf-8")
    p0 = sum(1 for line in out_lines if line.startswith("P0 "))
    p2 = sum(1 for line in out_lines if line.startswith("P2 "))
    print(
        f"terminology: {len(files)} files | findings P0={p0} P2={p2}"
        + (f" | fixed {fixed_files}" if args.fix else "")
        + f" → {args.out}"
    )
    return 1 if p0 else 0


if __name__ == "__main__":
    sys.exit(main())
