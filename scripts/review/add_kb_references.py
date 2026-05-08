#!/usr/bin/env python3
"""Phase 5 follow-up — Add `**Reference:**` lines to KB-check questions
that don't already have one. Closes BACKLOG B-002.

For each `<details markdown="1">...</details>` block in the file, ensures
the block contains a `**Reference:**` line. If missing, inserts a
default reference (per file, mapping below) immediately before the
closing `</details>`.

Idempotent: skips blocks that already contain a Reference line.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

DOCS = Path("docs")

# Map each KB-check file to its primary source content page(s).
# Format: relative path → ([list of (anchor_text, link_target)], ...)
REFERENCES: dict[str, list[tuple[str, str]]] = {
    "level-50/cloud-computing-knowledge-check.md": [
        ("Cloud Computing Primer", "cloud-computing-primer.md"),
        ("Cloud Service Models", "cloud-service-models.md"),
        ("Cloud Deployment Models", "cloud-deployment-models.md"),
    ],
    "level-50/security-compliance-knowledge-check.md": [
        ("Security & Compliance Basics", "security-compliance-basics.md"),
        ("Data Protection Principles", "data-protection-principles.md"),
        ("Compliance Frameworks", "compliance-frameworks.md"),
    ],
    "level-50/azure-fundamentals-knowledge-check.md": [
        ("Microsoft Azure Overview", "microsoft-azure-overview.md"),
        ("Azure Service Categories", "azure-service-categories.md"),
        ("Azure Global Infrastructure", "azure-global-infrastructure.md"),
    ],
    "level-200/azure-local-deep-dive-knowledge-check.md": [
        ("Azure Local Architecture Deep Dive", "azure-local-architecture-deep-dive.md"),
        ("Azure Local HA Patterns", "azure-local-ha-patterns.md"),
        ("Azure Local Hardware Planning", "azure-local-hardware-planning.md"),
        ("Azure Local Advanced Networking", "azure-local-advanced-networking.md"),
    ],
    "level-200/compliance-knowledge-check.md": [
        ("Compliance & Security Patterns", "compliance-security-patterns.md"),
        ("GDPR Implementation", "gdpr-implementation.md"),
        ("FedRAMP Compliance", "fedramp-compliance.md"),
        ("Encryption & Key Management", "encryption-key-management.md"),
        ("Security Hardening", "security-hardening.md"),
    ],
    "level-200/presales-knowledge-check.md": [
        ("Customer Discovery", "customer-discovery.md"),
        ("Pre-Sales Solution Design", "presales-solution-design.md"),
        ("Solution Sizing", "solution-sizing.md"),
        ("Cost Estimation & TCO", "cost-estimation.md"),
    ],
    "level-200/rag-implementation-knowledge-check.md": [
        ("Edge RAG Implementation", "edge-rag-implementation.md"),
        ("RAG Deployment Strategies", "rag-deployment-strategies.md"),
        ("LLM Inference Optimization", "llm-inference-optimization.md"),
        ("Vector Databases on the Edge", "vector-databases-edge.md"),
        ("RAG Operations & Monitoring", "rag-operations-monitoring.md"),
    ],
}

# Match a `<details markdown="1">…</details>` block (non-greedy, supports
# nested content). Important: must be `markdown="1"` and the closing
# `</details>`.
DETAILS_RE = re.compile(
    r'(<details\s+markdown="1"\s*>)(.*?)(</details>)',
    re.DOTALL,
)
REFERENCE_RE = re.compile(r"\*\*Reference[s]?:?\*\*", re.IGNORECASE)


def build_reference_line(refs: list[tuple[str, str]], idx: int) -> str:
    """Return a `**Reference:** [text](target)` line, cycling through
    the per-file references list."""
    if not refs:
        return ""
    text, target = refs[idx % len(refs)]
    return f"\n**Reference:** [{text}]({target})\n"


def fix_file(path: Path, refs: list[tuple[str, str]]) -> int:
    """Return number of references added."""
    text = path.read_text(encoding="utf-8")
    counter = {"value": 0}
    block_idx = {"value": 0}

    def repl(m: re.Match[str]) -> str:
        opener, body, closer = m.group(1), m.group(2), m.group(3)
        block_idx["value"] += 1
        if REFERENCE_RE.search(body):
            return m.group(0)  # already has a reference
        ref = build_reference_line(refs, block_idx["value"] - 1)
        # Trim trailing whitespace from body before insertion to keep
        # spacing tidy.
        new_body = body.rstrip("\n") + "\n" + ref
        counter["value"] += 1
        return f"{opener}{new_body}{closer}"

    new_text = DETAILS_RE.sub(repl, text)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
    return counter["value"]


def main() -> int:
    total = 0
    for relpath, refs in REFERENCES.items():
        path = DOCS / relpath
        if not path.exists():
            print(f"MISSING: {relpath}")
            continue
        n = fix_file(path, refs)
        if n:
            print(f"  {relpath}: {n} reference(s) added")
            total += n
        else:
            print(f"  {relpath}: 0 (already complete)")
    print(f"\nTotal: {total} references added")
    return 0


if __name__ == "__main__":
    sys.exit(main())
