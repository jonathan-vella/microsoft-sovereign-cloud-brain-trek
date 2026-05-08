#!/usr/bin/env python3
"""Knowledge-check structural validator (Phase 2.4).

Plan reference: §A bucket policy. CHECK-ONLY. Fixes live in
`scripts/fix_knowledge_checks.py` and `scripts/fix_level200_knowledge_checks.py`.

Severity buckets:
  P0  missing answer or reference; <details> without markdown="1"
  P1  fewer than 10 questions
  P2  inconsistent question numbering, missing reference link
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

QUESTION_RE = re.compile(r"^###\s+Question\s+\d+", re.MULTILINE)
DETAILS_OPEN_RE = re.compile(r"<details(?:\s[^>]*)?>")
DETAILS_MD_RE = re.compile(r'<details[^>]*\bmarkdown\s*=\s*"1"[^>]*>')
# Match: **Correct Answer: B**, **Correct Answer:** B, **Correct Answer**: B, **Answer: B**
ANSWER_RE = re.compile(
    r"\*\*(?:Correct\s+)?Answer\b[^*\n]*\*\*", re.IGNORECASE
)
REFERENCE_RE = re.compile(r"\*\*Reference[s]?:?\*\*", re.IGNORECASE)


def lint(path: Path, text: str) -> list[tuple[str, str]]:
    if "knowledge-check" not in path.name and "knowledge_check" not in path.name:
        return []
    findings: list[tuple[str, str]] = []
    qcount = len(QUESTION_RE.findall(text))
    if qcount == 0:
        findings.append(("P1", f"no question headings found"))
        return findings
    if qcount < 10:
        findings.append(("P1", f"only {qcount} questions (minimum 10)"))

    open_count = len(DETAILS_OPEN_RE.findall(text))
    md_count = len(DETAILS_MD_RE.findall(text))
    if open_count == 0:
        findings.append(("P0", "no <details> answer blocks"))
    if open_count > md_count:
        findings.append(
            ("P0", f"{open_count - md_count} <details> blocks missing markdown=\"1\"")
        )
    answers = len(ANSWER_RE.findall(text))
    if answers < qcount:
        findings.append(
            ("P0", f"answers ({answers}) < questions ({qcount})")
        )
    refs = len(REFERENCE_RE.findall(text))
    if refs < qcount:
        findings.append(
            ("P2", f"references ({refs}) < questions ({qcount})")
        )
    return findings


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--docs-root", default="docs", type=Path)
    p.add_argument(
        "--out",
        default="scripts/review/reports/knowledge-checks.txt",
        type=Path,
    )
    args = p.parse_args(argv)

    files = sorted(args.docs_root.rglob("*.md"))
    findings: list[str] = []
    examined = 0
    for md in files:
        text = md.read_text(encoding="utf-8")
        rel = md.relative_to(args.docs_root)
        results = lint(md, text)
        if results:
            examined += 1
        for sev, msg in results:
            findings.append(f"{sev} KC {rel}: {msg}")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(findings) + "\n", encoding="utf-8")
    p0 = sum(1 for f in findings if f.startswith("P0 "))
    p1 = sum(1 for f in findings if f.startswith("P1 "))
    p2 = sum(1 for f in findings if f.startswith("P2 "))
    print(
        f"kb-checks: {examined} files with findings | P0={p0} P1={p1} P2={p2} → {args.out}")
    return 1 if p0 else 0


if __name__ == "__main__":
    sys.exit(main())
