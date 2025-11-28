#!/usr/bin/env python3
"""
Fix Level 200 knowledge check files to wrap answers in collapsible details elements.

The Level 200 format has:
---
**Correct Answer: X**
**Explanation:**
... detailed explanation with Why A/B/C/D sections ...

This script wraps these in <details markdown="1"> tags.
"""

import re
from pathlib import Path


def fix_level200_file(filepath: Path) -> tuple[bool, int]:
    """
    Fix a Level 200 knowledge check file.
    Returns (was_modified, question_count)
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has details tags
    if '<details' in content:
        return False, 0

    # Pattern to match answer blocks:
    # ---\n\n**Correct Answer: X** or **Correct Answer:** X
    # ... everything until the next question (## Question) or end of file

    # The pattern looks for:
    # 1. A line with just --- followed by blank lines
    # 2. **Correct Answer followed by the letter
    # 3. Everything until the next ## Question heading

    # Multiple patterns to handle different Level 200 formats:

    # Pattern 1: --- separator before answer (arc-advanced style)
    pattern1 = r'(\n\n---\n\n)(\*\*Correct Answer:?\*?\*?:?\s*[A-D].*?)(?=\n\n---\n\n## Question|\Z)'

    # Pattern 2: No separator, answer follows directly after options
    # Matches: "\n\n**Correct Answer: X**\n\n**Explanation:**..." until next ### Question or ---
    pattern2 = r'(\n\n)(\*\*Correct Answer:?\*?\*?:?\s*[A-D]\*?\*?\s*\n+\*\*Explanation:\*?\*?.*?)(?=\n---\n|\n### Question|\Z)'

    def wrap_answer(match):
        separator = match.group(1)
        answer_content = match.group(2).strip()
        return f'''{separator}<details markdown="1">
<summary>Click to reveal answer</summary>

{answer_content}

</details>

'''

    # Try pattern 1 first
    new_content, count = re.subn(pattern1, wrap_answer, content, flags=re.DOTALL)

    # If no matches, try pattern 2
    if count == 0:
        new_content, count = re.subn(pattern2, wrap_answer, content, flags=re.DOTALL)

    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True, count

    return False, 0


def main():
    level200_path = Path("/workspaces/sov-cloud-brain-trek/docs/level-200")

    knowledge_files = list(level200_path.glob("*knowledge-check*.md"))

    print(f"Processing {len(knowledge_files)} Level 200 knowledge check files\n")
    print("-" * 60)

    total_fixed = 0
    total_questions = 0

    for filepath in sorted(knowledge_files):
        modified, count = fix_level200_file(filepath)
        if modified:
            print(f"✅ FIXED: {filepath.name} ({count} questions wrapped)")
            total_fixed += 1
            total_questions += count
        else:
            print(f"⏭️  SKIP: {filepath.name} (already has details or no matches)")

    print("-" * 60)
    print(f"\nSummary: {total_fixed} files fixed, {total_questions} answer sections wrapped")


if __name__ == "__main__":
    main()
