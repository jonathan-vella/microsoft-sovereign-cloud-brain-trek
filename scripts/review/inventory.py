#!/usr/bin/env python3
"""Build inventory.csv for the docs review pipeline (Phase 0.3).

Plan reference: §0.3 — columns are tied to specific audit dimensions:
    path, level, kind, word_count, nav_excluded,
    has_frontmatter_description, outbound_internal_links, image_refs

Usage:
    python3 scripts/review/inventory.py [--docs-root docs] [--out scripts/review/reports/inventory.csv]
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

# Front-matter parser: kept dependency-free intentionally.
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
KEY_RE = re.compile(r"^([A-Za-z_][\w-]*)\s*:\s*(.*?)\s*$")
INTERNAL_LINK_RE = re.compile(
    r"\]\((?!https?://|mailto:|tel:|#)([^)]+?\.md(?:#[^)]*)?)\)"
)
JEKYLL_LINK_RE = re.compile(r"\{%\s*link\s+([^%]+?)\s*%\}")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")


def parse_frontmatter(text: str) -> dict[str, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    out: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if not line or line.startswith("#"):
            continue
        km = KEY_RE.match(line)
        if km:
            out[km.group(1)] = km.group(2).strip().strip('"').strip("'")
    return out


def classify_kind(path: Path) -> str:
    name = path.name.lower()
    if name == "readme.md":
        return "readme"
    if name.startswith("module-"):
        return "overview"
    if "knowledge-check" in name:
        return "kb-check"
    if name.startswith("lab-") or name.endswith("-lab.md"):
        return "lab"
    if name.startswith("visual_specifications") or name == "visual_specifications.md":
        return "spec"
    if name == "404.md":
        return "asset-doc"
    if path.parent.name == "resources":
        return "asset-doc"
    if path.parent.name == "docs":
        return "overview"
    return "topic"


def derive_level(rel_path: Path) -> str:
    parts = rel_path.parts
    if not parts:
        return "top"
    if parts[0].startswith("level-"):
        return parts[0].replace("level-", "L")
    if parts[0] == "resources":
        return "resources"
    return "top"


def word_count(text: str) -> int:
    body = FRONTMATTER_RE.sub("", text, count=1)
    body = re.sub(r"```.*?```", " ", body, flags=re.DOTALL)
    body = re.sub(r"`[^`]+`", " ", body)
    body = re.sub(r"<[^>]+>", " ", body)
    return len(re.findall(r"\b\w[\w'-]*\b", body))


def collect(docs_root: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for md in sorted(docs_root.rglob("*.md")):
        rel = md.relative_to(docs_root)
        try:
            text = md.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = md.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(text)
        nav_excluded = fm.get("nav_exclude", "").lower() in ("true", "yes")
        has_desc = bool(fm.get("description"))
        internal_links = len(INTERNAL_LINK_RE.findall(text)) + len(
            JEKYLL_LINK_RE.findall(text)
        )
        images = len(IMAGE_RE.findall(text))
        rows.append(
            {
                "path": str(rel).replace("\\", "/"),
                "level": derive_level(rel),
                "kind": classify_kind(rel),
                "word_count": word_count(text),
                "nav_excluded": "true" if nav_excluded else "false",
                "has_frontmatter_description": "true" if has_desc else "false",
                "outbound_internal_links": internal_links,
                "image_refs": images,
            }
        )
    return rows


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--docs-root", default="docs", type=Path)
    p.add_argument(
        "--out",
        default="scripts/review/reports/inventory.csv",
        type=Path,
    )
    args = p.parse_args(argv)

    if not args.docs_root.exists():
        print(f"docs root not found: {args.docs_root}", file=sys.stderr)
        return 2

    rows = collect(args.docs_root)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "path",
                "level",
                "kind",
                "word_count",
                "nav_excluded",
                "has_frontmatter_description",
                "outbound_internal_links",
                "image_refs",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)
    print(f"inventory: {len(rows)} files → {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
