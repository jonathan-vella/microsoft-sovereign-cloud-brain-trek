#!/usr/bin/env python3
"""
Fix knowledge check files to ensure consistent formatting and proper rendering.

Issues addressed:
1. Add markdown="1" to <details> tags for kramdown markdown parsing
2. Convert inline **Answer: X** format to collapsible <details> format
3. Ensure proper blank lines for HTML/markdown rendering
"""

import os
import re
from pathlib import Path


def fix_details_markdown_attr(content: str) -> str:
    """Add markdown='1' to details tags if missing."""
    # Replace <details> with <details markdown="1">
    content = re.sub(
        r'<details(?!\s+markdown)>',
        '<details markdown="1">',
        content
    )
    return content


def fix_inline_answers_level50(content: str) -> str:
    """
    Convert Level 50 style inline answers to collapsible format.
    Pattern: **Answer: X** - explanation
    """
    # Pattern for inline answers: **Answer: X** - explanation
    pattern = r'\*\*Answer:\s*([A-D])\*\*\s*-\s*(.+?)(?=\n\n###|\n\n---|\n\n##|\Z)'

    def replace_inline_answer(match):
        letter = match.group(1)
        explanation = match.group(2).strip()
        return f'''<details markdown="1">
<summary>Click to reveal answer</summary>

**Correct Answer: {letter}**

**Explanation:** {explanation}

</details>'''

    content = re.sub(pattern, replace_inline_answer, content, flags=re.DOTALL)
    return content


def fix_level200_answers(content: str) -> str:
    """
    Convert Level 200 style visible answers to collapsible format.
    Pattern: ---\n\n**Correct Answer: X**\n\n**Explanation:**...
    """
    # Pattern for Level 200 answers that come after ---
    # Match from --- through the explanation section
    pattern = r'(---\s*\n+)\*\*Correct Answer:?\*\*:?\s*([A-D])\s*\n+\*\*Explanation:\*\*\s*\n*(.*?)(?=\n---\n|\n## |\Z)'

    def replace_visible_answer(match):
        separator = match.group(1)
        letter = match.group(2)
        explanation = match.group(3).strip()
        return f'''{separator}<details markdown="1">
<summary>Click to reveal answer</summary>

**Correct Answer: {letter}**

**Explanation:**

{explanation}

</details>'''

    content = re.sub(pattern, replace_visible_answer, content, flags=re.DOTALL)
    return content


def process_file(filepath: Path) -> tuple[bool, str]:
    """Process a single knowledge check file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    modified = original

    # Check what type of file this is
    has_details = '<details' in modified
    has_inline_answer = re.search(r'\*\*Answer:\s*[A-D]\*\*\s*-', modified)
    has_visible_correct = re.search(r'^---\s*\n+\*\*Correct Answer', modified, re.MULTILINE)

    changes = []

    # Fix 1: Add markdown="1" to existing details tags
    if has_details:
        new_content = fix_details_markdown_attr(modified)
        if new_content != modified:
            modified = new_content
            changes.append("Added markdown='1' to details tags")

    # Fix 2: Convert inline answers (Level 50 style)
    if has_inline_answer:
        new_content = fix_inline_answers_level50(modified)
        if new_content != modified:
            modified = new_content
            changes.append("Converted inline answers to collapsible format")

    # Fix 3: Convert visible answers (Level 200 style)
    # Note: This is more complex due to varied formats, skip for now
    # if has_visible_correct:
    #     new_content = fix_level200_answers(modified)
    #     if new_content != modified:
    #         modified = new_content
    #         changes.append("Wrapped visible answers in details tags")

    if modified != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(modified)
        return True, ", ".join(changes)

    return False, "No changes needed"


def main():
    docs_path = Path("/workspaces/sov-cloud-brain-trek/docs")

    # Find all knowledge check files
    knowledge_files = list(docs_path.rglob("*knowledge-check*.md")) + \
                      list(docs_path.rglob("*knowledge_check*.md"))

    print(f"Found {len(knowledge_files)} knowledge check files\n")
    print("-" * 60)

    modified_count = 0
    for filepath in sorted(knowledge_files):
        rel_path = filepath.relative_to(docs_path)
        modified, message = process_file(filepath)
        status = "✅ FIXED" if modified else "⏭️  OK"
        print(f"{status}: {rel_path}")
        if modified:
            print(f"         └─ {message}")
            modified_count += 1

    print("-" * 60)
    print(f"\nSummary: {modified_count} files modified, {len(knowledge_files) - modified_count} unchanged")


if __name__ == "__main__":
    main()
