#!/usr/bin/env python3
"""Phase 5 — Bulk-replace 'e.g.,' with 'for example,' outside code blocks.

Microsoft style guide rejects 'e.g.,' (Microsoft.Foreign rule).
This sweep is mechanical and safe: it only modifies prose outside code
blocks, inline code, and link URLs.

Idempotent.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

CODEBLOCK_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`]+`")
LINK_URL_RE = re.compile(r"\]\([^)]+\)")
EG_RE = re.compile(r"\be\.g\.,?", re.IGNORECASE)


def fix(text: str) -> tuple[str, int]:
    placeholders: list[str] = []

    def _mask(m: re.Match[str]) -> str:
        placeholders.append(m.group(0))
        return f"\x00P{len(placeholders) - 1}\x00"

    masked = CODEBLOCK_RE.sub(_mask, text)
    masked = INLINE_CODE_RE.sub(_mask, masked)
    masked = LINK_URL_RE.sub(_mask, masked)

    count = 0

    def _repl(m: re.Match[str]) -> str:
        nonlocal count
        count += 1
        # Preserve original case roughly: "E.g.," → "For example," at sentence start
        original = m.group(0)
        if original[0].isupper():
            return "For example,"
        return "for example,"

    masked = EG_RE.sub(_repl, masked)

    # Unmask in reverse order
    for idx in range(len(placeholders) - 1, -1, -1):
        masked = masked.replace(f"\x00P{idx}\x00", placeholders[idx])
    return masked, count


def main() -> int:
    docs = Path("docs")
    total = 0
    files = 0
    for md in docs.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        new_text, n = fix(text)
        if n and new_text != text:
            md.write_text(new_text, encoding="utf-8")
            total += n
            files += 1
            print(f"  {md.relative_to(docs)}: {n} fix(es)")
    print(f"\nTotal: {total} replacements across {files} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
