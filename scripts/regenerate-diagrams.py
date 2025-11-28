#!/usr/bin/env python3
"""
Regenerate all SVG diagrams from Python sources.

Usage:
    python scripts/regenerate-diagrams.py           # Regenerate all diagrams
    python scripts/regenerate-diagrams.py --level 50   # Regenerate only Level 50
    python scripts/regenerate-diagrams.py --level 100  # Regenerate only Level 100
    python scripts/regenerate-diagrams.py --dry-run    # Show what would be generated
"""

import argparse
import subprocess
import sys
from pathlib import Path

# Base directory for diagram sources
DIAGRAMS_BASE = Path(__file__).parent.parent / "docs" / "assets" / "diagrams" / "src"

DIAGRAM_DIRS = {
    50: DIAGRAMS_BASE / "level-50",
    100: DIAGRAMS_BASE / "level-100",
    200: DIAGRAMS_BASE / "level-200",
    300: DIAGRAMS_BASE / "level-300",
}


def get_python_scripts(level: int = None) -> list[Path]:
    """Get all Python diagram scripts, optionally filtered by level."""
    scripts = []

    if level:
        if level in DIAGRAM_DIRS:
            dir_path = DIAGRAM_DIRS[level]
            if dir_path.exists():
                scripts.extend(sorted(dir_path.glob("*.py")))
    else:
        for dir_path in DIAGRAM_DIRS.values():
            if dir_path.exists():
                scripts.extend(sorted(dir_path.glob("*.py")))

    return scripts


def regenerate_diagram(script_path: Path, dry_run: bool = False) -> bool:
    """Regenerate a single diagram from its Python source."""
    if dry_run:
        print(f"  [DRY RUN] Would generate: {script_path.name}")
        return True

    print(f"  Generating: {script_path.name}...", end=" ", flush=True)

    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            timeout=60,
            cwd=script_path.parent,
        )

        if result.returncode == 0:
            print("✓")
            return True
        else:
            print("✗")
            print(f"    Error: {result.stderr[:200]}")
            return False

    except subprocess.TimeoutExpired:
        print("✗ (timeout)")
        return False
    except Exception as e:
        print(f"✗ ({e})")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Regenerate SVG diagrams from Python sources"
    )
    parser.add_argument(
        "--level",
        type=int,
        choices=[50, 100, 200, 300],
        help="Only regenerate diagrams for a specific level",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be generated without actually running",
    )

    args = parser.parse_args()

    print("=" * 60)
    print("Sovereign Cloud Brain Trek - Diagram Regeneration")
    print("=" * 60)

    scripts = get_python_scripts(args.level)

    if not scripts:
        print(f"\nNo Python scripts found" + (f" for Level {args.level}" if args.level else ""))
        return 1

    print(f"\nFound {len(scripts)} diagram script(s)" + (f" for Level {args.level}" if args.level else ""))
    print()

    success_count = 0
    fail_count = 0

    # Group by level
    current_level = None
    for script in scripts:
        # Determine level from path
        for level, dir_path in DIAGRAM_DIRS.items():
            if script.parent == dir_path:
                if current_level != level:
                    current_level = level
                    print(f"\n📂 Level {level}:")
                break

        if regenerate_diagram(script, args.dry_run):
            success_count += 1
        else:
            fail_count += 1

    print()
    print("=" * 60)
    print(f"Results: {success_count} succeeded, {fail_count} failed")
    print("=" * 60)

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
