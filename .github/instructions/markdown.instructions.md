---
applyTo: "**/*.md"
---

# Markdown Authoring Instructions

These instructions ensure all Markdown files comply with linting rules and project conventions.

## File Structure

### YAML Front Matter (Required)

Every Markdown file must start with YAML front matter:

```yaml
---
layout: default
title: Page Title
nav_order: 1
parent: Parent Section Name    # For child pages
has_children: true             # For parent pages
description: "Brief SEO description"
---
```

### Page Title

- Use a single H1 (`#`) immediately after front matter
- Add `{: .no_toc }` after the title to exclude from TOC
- Never use multiple H1 headings in a single file

```markdown
# Page Title
{: .no_toc }
```

### Table of Contents (for multi-section pages)

```markdown
## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}
```

---

## Heading Rules

### Hierarchy (MD001)

- Never skip heading levels (H1 → H2 → H3, not H1 → H3)
- Use H2 (`##`) for main sections
- Use H3 (`###`) for subsections
- Use H4 (`####`) sparingly for detailed breakdowns

### Style (MD003)

- Use ATX-style headings with `#` symbols
- Include a space after `#`
- Leave one blank line before and after headings

```markdown
## Correct Heading

Content here...

### Subsection

More content...
```

### No Duplicate Headings (MD024)

- Sibling headings at the same level must be unique
- Different sections can have the same subheading names

---

## Lists

### Unordered Lists (MD004, MD007)

- Use dashes (`-`) for bullet points
- Indent nested items with 2 spaces
- Leave blank lines before and after lists

```markdown
Content before list.

- First item
- Second item
  - Nested item
  - Another nested item
- Third item

Content after list.
```

### Ordered Lists (MD029, MD030)

- Use sequential numbers (`1.`, `2.`, `3.`)
- Maintain consistent spacing after numbers

```markdown
1. First step
2. Second step
3. Third step
```

### Checkboxes

- Use `- [ ]` for incomplete items
- Use `- [x]` for completed items
- Use `✅` emoji for learning objectives

```markdown
## Prerequisites

- [ ] Azure subscription
- [ ] Basic cloud knowledge

## Learning Objectives

- ✅ Understand sovereignty concepts
- ✅ Explain Azure Local modes
```

---

## Code Blocks

### Fenced Code Blocks (MD040, MD046, MD048)

- Always use triple backticks (not indentation)
- Always specify the language for syntax highlighting
- Use lowercase language identifiers

````markdown
```powershell
Get-AzResourceGroup -Name "sovereign-rg"
```

```yaml
apiVersion: v1
kind: ConfigMap
```

```bash
az login --use-device-code
```

```json
{
  "name": "example",
  "value": 123
}
```
````

### Inline Code (MD038)

- Use single backticks for inline code
- No spaces inside backticks

```markdown
Run the `Get-AzVM` cmdlet to list VMs.
```

---

## Links

### Internal Links

- Use relative paths from the current file
- Include `.md` extension

```markdown
[Digital Sovereignty](../level-100/digital-sovereignty.md)
[Next Module](./module-02-cloud-models.md)
```

### External Links

- Use full URLs
- Add descriptive link text (not "click here")

```markdown
[Microsoft Learn](https://learn.microsoft.com/)
[Azure Local Documentation](https://learn.microsoft.com/azure/azure-local/)
```

### Section Anchors

- Use lowercase with hyphens
- Match the heading text exactly

```markdown
[See Prerequisites](#prerequisites)
[Learning Objectives](#learning-objectives)
```

### Reference Links (MD052, MD053)

- Define reference links at the bottom of the file
- Ensure all references are used

```markdown
Read the [official documentation][ms-learn] for more details.

[ms-learn]: https://learn.microsoft.com/
```

---

## Images

### Alt Text Required (MD045)

- Every image must have descriptive alt text
- Alt text should describe the image content

```markdown
![Azure Local architecture diagram showing connected mode](../../assets/images/level-100/azure-local-architecture.svg)
```

### Image Captions

- Add italicized caption below images

```markdown
![Diagram description](path/to/image.svg)
*Figure 1: Caption describing the visual*
```

### Placeholder Format

When images are pending:

```markdown
> **📊 Visual Asset Placeholder**
> *Asset Name: [Asset N: Asset Title]*
> Description of what the diagram will show...
> **Source:** Adapted from Microsoft Learn documentation
```

---

## HTML Usage (MD033)

### Allowed HTML Elements

The following HTML elements are permitted:

- `<details>`, `<summary>` — Expandable sections
- `<div>`, `<span>`, `<p>` — Styling containers
- `<table>`, `<thead>`, `<tbody>`, `<tr>`, `<th>`, `<td>` — Complex tables
- `<br>` — Line breaks
- `<a>`, `<img>` — Links and images with special attributes

### Expandable Content Pattern

```markdown
<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

Explanation content here...

</details>
```

### Markdown Inside HTML Blocks (Critical)

When including Markdown syntax (images, links, emphasis) inside HTML elements, you **must** add the `markdown="1"` attribute. Without this, Kramdown will not process Markdown inside raw HTML.

```markdown
<!-- ❌ WRONG: Markdown won't be processed -->
<div class="diagram-content">
![Architecture diagram](path/to/image.svg)
</div>

<!-- ✅ CORRECT: Markdown is processed -->
<div class="diagram-content" markdown="1">
![Architecture diagram](path/to/image.svg)
</div>
```

Common patterns requiring `markdown="1"`:

```markdown
<div class="custom-container" markdown="1">

**Bold text**, _italic_, and [links](url.md) work here.

- List items work
- As do code blocks

</div>
```

---

## Just the Docs Syntax

### Callouts

```markdown
{: .warning }
> **⚠️ Warning Title**
> Warning content here.

{: .note }
> **💡 Note:** Additional information.

{: .important }
> **Important:** Critical information.
```

### Excluding from TOC

```markdown
# Page Title
{: .no_toc }

## Section Not in TOC
{: .no_toc }
```

### Text Styling Classes

```markdown
Large heading text
{: .fs-9 }

Subtitle text
{: .fs-6 .fw-300 }
```

### Buttons

```markdown
[Get Started](path.md){: .btn .btn-primary }
[View on GitHub](url){: .btn .btn-outline }
```

---

## Horizontal Rules (MD035)

- Use exactly three dashes
- Leave blank lines before and after

```markdown
Content above.

---

Content below.
```

---

## Emphasis (MD049, MD050)

- Use `_underscores_` for _italics_
- Use `**asterisks**` for **bold**
- Use `***both***` for _**bold italic**_

```markdown
This is _emphasized_ text.
This is **strong** text.
This is ***strong and emphasized*** text.
```

---

## Tables (MD055, MD056)

- Include leading and trailing pipes
- Align separator row properly
- Use consistent column widths when possible

```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data 1   | Data 2   | Data 3   |
| Data 4   | Data 5   | Data 6   |
```

---

## Whitespace Rules

### Trailing Spaces (MD009)

- No trailing whitespace except for line breaks
- Use two spaces at end of line for `<br>` equivalent

### Blank Lines (MD012, MD022, MD031, MD032)

- Maximum 2 consecutive blank lines
- One blank line before and after headings
- One blank line before and after code blocks
- One blank line before and after lists

### Final Newline (MD047)

- Files must end with a single newline character

---

## Knowledge Check Format

```markdown
### Question N: Topic Name

Question text here?

A) Option A  
B) Option B  
C) Option C  
D) Option D

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Detailed explanation here.

**Reference:** [Topic Documentation](link.md)

</details>
```

---

## Quick Checklist

Before committing Markdown files:

- [ ] YAML front matter with `layout`, `title`, `nav_order`
- [ ] Single H1 with `{: .no_toc }`
- [ ] Sequential heading hierarchy (no skipped levels)
- [ ] All code blocks have language specified
- [ ] All images have alt text
- [ ] Internal links use relative paths with `.md`
- [ ] External links use full URLs
- [ ] Lists have blank lines before/after
- [ ] No trailing whitespace (except line break spaces)
- [ ] File ends with newline
- [ ] Pre-commit hook passes: `pre-commit run --all-files`
