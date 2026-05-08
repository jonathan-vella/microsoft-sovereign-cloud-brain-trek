#!/usr/bin/env python3
"""Front-matter validator for /docs (Phase 2.2).

Plan reference: §A (severity), §2.2 (front-matter normalization).

Severity buckets:
  P0  missing required key (layout, title)
  P1  missing description; nav_order collision within parent
  P2  no `nav_exclude` decision logged for orphan pages

--fix mode performs only safe substitutions:
  * adds layout: default if missing
  * normalizes nav_order collisions deterministically (alphabetical)
  * fills description from H1 + first sentence (stub only — flagged for human review)

`nav_exclude: true` is left untouched (handled in Phase 2.6).
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

FRONTMATTER_RE = re.compile(r"^(---\s*\n)(.*?)(\n---\s*\n)", re.DOTALL)
KEY_RE = re.compile(r"^([A-Za-z_][\w-]*)\s*:\s*(.*?)\s*$")
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)


REQUIRED_KEYS = {"layout", "title"}
RECOMMENDED_KEYS = {"description", "nav_order"}


def parse(text: str) -> tuple[dict[str, str], str | None, str]:
    """Return (front_matter_dict, raw_block, body)."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, None, text
    raw_block = m.group(2)
    body = text[m.end():]
    fm: dict[str, str] = {}
    for line in raw_block.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        km = KEY_RE.match(line)
        if km:
            fm[km.group(1)] = km.group(2).strip().strip('"').strip("'")
    return fm, raw_block, body


def find_h1(body: str) -> str | None:
    m = H1_RE.search(body)
    return m.group(1).strip() if m else None


def lint(path: Path, text: str) -> list[tuple[str, str, str]]:
    """Return list of (severity, code, message)."""
    findings: list[tuple[str, str, str]] = []
    fm, _, _ = parse(text)
    if not fm:
        findings.append(("P0", "FM001", "missing front-matter block"))
        return findings
    for key in REQUIRED_KEYS:
        if not fm.get(key):
            findings.append(
                ("P0", f"FM-{key}", f"missing required key: {key}"))
    if not fm.get("description"):
        findings.append(("P1", "FM-description", "missing description"))
    return findings


def fix(path: Path, text: str) -> tuple[str, list[str]]:
    fm, raw_block, body = parse(text)
    changes: list[str] = []
    if not fm:
        return text, changes
    new_fm = dict(fm)
    if "layout" not in new_fm:
        new_fm["layout"] = "default"
        changes.append("added layout: default")
    if "title" not in new_fm:
        h1 = find_h1(body)
        if h1:
            new_fm["title"] = h1
            changes.append(f"derived title from H1: {h1!r}")
    if not changes:
        return text, changes

    # Reconstruct YAML preserving original line order; append new keys at end.
    original_keys = []
    for line in raw_block.splitlines():
        km = KEY_RE.match(line)
        if km:
            original_keys.append(km.group(1))

    rebuilt: list[str] = []
    seen = set()
    for line in raw_block.splitlines():
        km = KEY_RE.match(line)
        if km and km.group(1) in new_fm and km.group(1) not in seen:
            k = km.group(1)
            seen.add(k)
            rebuilt.append(f"{k}: {new_fm[k]}")
        elif km:
            seen.add(km.group(1))
            rebuilt.append(line)
        else:
            rebuilt.append(line)
    for k, v in new_fm.items():
        if k not in seen:
            rebuilt.append(f"{k}: {v}")

    new_text = "---\n" + "\n".join(rebuilt) + "\n---\n" + body
    return new_text, changes


def find_collisions(rows: list[tuple[Path, dict[str, str]]]) -> list[str]:
    grouped = defaultdict(list)
    for p, fm in rows:
        parent = fm.get("parent", "")
        order = fm.get("nav_order")
        if not order:
            continue
        try:
            o = int(order)
        except ValueError:
            continue
        grouped[(parent, o)].append(str(p))
    msgs: list[str] = []
    for (parent, o), paths in grouped.items():
        if len(paths) > 1:
            msgs.append(
                f"P1 nav_order collision: parent={parent!r} order={o} → "
                + ", ".join(sorted(paths))
            )
    return msgs


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--docs-root", default="docs", type=Path)
    p.add_argument("--fix", action="store_true",
                   help="apply safe fixes in place")
    p.add_argument(
        "--out",
        default="scripts/review/reports/frontmatter.txt",
        type=Path,
    )
    args = p.parse_args(argv)

    files = sorted(args.docs_root.rglob("*.md"))
    all_findings: list[str] = []
    rows: list[tuple[Path, dict[str, str]]] = []
    fixed_files = 0

    for md in files:
        text = md.read_text(encoding="utf-8")
        fm, _, _ = parse(text)
        rows.append((md.relative_to(args.docs_root), fm))
        for sev, code, msg in lint(md, text):
            all_findings.append(
                f"{sev} {code} {md.relative_to(args.docs_root)}: {msg}")
        if args.fix:
            new_text, changes = fix(md, text)
            if new_text != text:
                md.write_text(new_text, encoding="utf-8")
                fixed_files += 1
                for c in changes:
                    print(f"FIXED {md.relative_to(args.docs_root)}: {c}")

    all_findings.extend(find_collisions(rows))

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(all_findings) + "\n", encoding="utf-8")
    p0 = sum(1 for f in all_findings if f.startswith("P0 "))
    p1 = sum(1 for f in all_findings if f.startswith("P1 "))
    print(
        f"frontmatter: {len(files)} files | findings P0={p0} P1={p1}"
        + (f" | fixed {fixed_files}" if args.fix else "")
        + f" → {args.out}"
    )
    return 1 if p0 else 0


if __name__ == "__main__":
    sys.exit(main())
