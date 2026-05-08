#!/usr/bin/env python3
"""Phase 4.3 — Post-build HTML accessibility fix.

Walks `_site/**/*.html` and applies safe in-place transformations that
make rendered pages WCAG 2.1 AA compliant for issues that originate in
markdown / Jekyll defaults rather than in the source content:

1. **Disabled task-list checkboxes (kramdown output).**
   `<input type="checkbox" class="task-list-item-checkbox" disabled />`
   produced by kramdown for `- [ ] item` syntax has no accessible name.
   Fails: `WCAG2AA.Principle4.Guideline4_1.4_1_2.H91.InputCheckbox.Name`
   and `WCAG2AA.Principle1.Guideline1_3.1_3_1.F68`.

   Fix: add `aria-hidden="true"` and `tabindex="-1"`. The visible text
   immediately following the input continues to convey the meaning to
   AT (read by the surrounding `<li class="task-list-item">`).

This runs after `bundle exec jekyll build` and is idempotent.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Match `<input ... class="..task-list-item-checkbox.." ... disabled ... />`
# in any attribute order, inserting aria-hidden=\"true\" and tabindex=\"-1\"
# if not already present.
INPUT_RE = re.compile(
    r"""
    (<input\b)               # 1: opening
    (
      (?=[^>]*\btask-list-item-checkbox\b)
      (?=[^>]*\bdisabled\b)
      (?:(?!aria-hidden=)[^>])*?  # avoid double-applying
    )
    (\s*/?>)                 # 3: closing of self-closing or open
    """,
    re.VERBOSE,
)


def fix_html(text: str) -> tuple[str, int]:
    """Return (new_text, num_fixes)."""
    count = 0

    def repl(m: re.Match[str]) -> str:
        nonlocal count
        count += 1
        attrs = m.group(2).rstrip()
        return (
            f'{m.group(1)}{attrs} aria-hidden="true" tabindex="-1"'
            f'{m.group(3)}'
        )

    return INPUT_RE.sub(repl, text), count


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--site-root", default="_site", type=Path)
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(argv)

    if not args.site_root.exists():
        print(f"site root not found: {args.site_root}", file=sys.stderr)
        return 2

    total_fixes = 0
    files_modified = 0
    for html in args.site_root.rglob("*.html"):
        text = html.read_text(encoding="utf-8")
        new_text, n = fix_html(text)
        if n and new_text != text:
            total_fixes += n
            files_modified += 1
            if not args.dry_run:
                html.write_text(new_text, encoding="utf-8")

    mode = "DRY-RUN" if args.dry_run else "applied"
    print(
        f"a11y-postbuild ({mode}): {total_fixes} task-list checkbox fixes "
        f"across {files_modified} HTML files"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
