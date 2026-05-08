#!/usr/bin/env python3
"""Phase 2.3 — Extensionless internal-link sweep.

Finds markdown links of the form `[text](slug)` or `[text](slug#anchor)` where
`slug` does not contain `://`, does not end in `.md`, and resolves to an existing
`.md` file in `docs/`. Appends `.md` so Jekyll's `jekyll-relative-links` plugin
can rewrite to `.html` at build time.

Skips:
  * Absolute URLs (http://, https://, mailto:, tel:)
  * Anchor-only links (#section)
  * Already has an extension (.html, .pdf, .png, etc.)
  * Slug doesn't resolve to an existing .md (true broken — surfaces in lychee)

Plan reference: §2.3 (link repair, mechanical bulk).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# `[text](target)`  where target is the URL/path. Capture link with group 1, target with 2.
LINK_RE = re.compile(r"(\[(?:[^\[\]]|\[[^\]]*\])*\])\(([^)]+)\)")
ABSOLUTE_RE = re.compile(r"^(?:[a-z][a-z0-9+\-.]*://|mailto:|tel:|#)", re.IGNORECASE)
HAS_EXT_RE = re.compile(r"\.[a-z0-9]{1,5}(?:#.*)?$", re.IGNORECASE)
ANCHOR_SPLIT_RE = re.compile(r"^([^#?]+)([#?].*)?$")


def repair_text(
    text: str, source_path: Path, docs_root: Path
) -> tuple[str, list[str]]:
    """Return (new_text, list_of_repairs)."""
    repairs: list[str] = []

    def _repair(m: re.Match[str]) -> str:
        link_text = m.group(1)
        target = m.group(2).strip()

        # Skip absolute URLs and pure-anchor links
        if ABSOLUTE_RE.match(target):
            return m.group(0)

        # Skip Jekyll {% link %} tags (these appear inside the text, but link tags
        # are produced by liquid before markdown link syntax — pass through).
        if target.startswith("{%") or target.startswith("{{"):
            return m.group(0)

        # Already has an extension
        if HAS_EXT_RE.search(target):
            return m.group(0)

        # Skip targets containing null bytes or control characters (defensive)
        if any(ord(c) < 32 for c in target):
            return m.group(0)

        # Split slug + anchor/query
        am = ANCHOR_SPLIT_RE.match(target)
        if not am:
            return m.group(0)
        slug = am.group(1)
        anchor = am.group(2) or ""

        # Skip slugs containing slashes that look like absolute URLs we missed
        if slug.startswith("/") or "://" in slug:
            return m.group(0)

        # Resolve relative to source file's directory
        try:
            candidate = (source_path.parent / (slug + ".md")).resolve()
            candidate2 = (docs_root / (slug + ".md")).resolve()
        except (OSError, ValueError):
            return m.group(0)

        target_md: Path | None = None
        if candidate.exists() and str(candidate).startswith(str(docs_root.resolve())):
            target_md = candidate
        elif candidate2.exists():
            target_md = candidate2

        if target_md is None:
            return m.group(0)  # truly broken — leave for lychee to flag

        new_target = slug + ".md" + anchor
        repairs.append(f"  {target!r} → {new_target!r}")
        return f"{link_text}({new_target})"

    new_text = LINK_RE.sub(_repair, text)
    return new_text, repairs


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--docs-root", default="docs", type=Path)
    p.add_argument("--dry-run", action="store_true")
    p.add_argument(
        "--out",
        default="scripts/review/reports/link-repair.log",
        type=Path,
    )
    args = p.parse_args(argv)

    docs_root = args.docs_root.resolve()
    files = sorted(docs_root.rglob("*.md"))
    total_repairs = 0
    fixed_files = 0
    log_lines: list[str] = []
    for md in files:
        text = md.read_text(encoding="utf-8")
        new_text, repairs = repair_text(text, md, docs_root)
        if not repairs:
            continue
        rel = md.relative_to(docs_root)
        log_lines.append(f"{rel} ({len(repairs)} repairs)")
        log_lines.extend(repairs)
        total_repairs += len(repairs)
        if not args.dry_run:
            md.write_text(new_text, encoding="utf-8")
            fixed_files += 1

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(log_lines) + "\n", encoding="utf-8")
    mode = "DRY-RUN" if args.dry_run else "applied"
    print(
        f"link-repair ({mode}): {total_repairs} repairs across {fixed_files} files → {args.out}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
