# Contributing to Microsoft Sovereign Cloud Brain Trek

Thank you for your interest in contributing to the Microsoft Sovereign Cloud Brain Trek training platform! This document provides guidelines for contributing to this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Content Guidelines](#content-guidelines)
- [Pull Request Process](#pull-request-process)
- [Style Guide](#style-guide)

---

## Code of Conduct

This project adheres to the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

---

## Getting Started

### Prerequisites

- Git
- Ruby 3.x with Bundler
- Node.js (for markdownlint)
- VS Code (recommended)

### Local Development Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/jonathan-vella/microsoft-sovereign-cloud-brain-trek.git
   cd microsoft-sovereign-cloud-brain-trek
   ```

2. **Install dependencies:**

   ```bash
   bundle install
   npm install -g markdownlint-cli2
   ```

3. **Run the site locally:**

   ```bash
   bundle exec jekyll serve
   ```

4. **Open in browser:** Navigate to `http://localhost:4000`

### Using the Dev Container (Recommended)

This project includes a dev container configuration for VS Code:

1. Open the project in VS Code
2. When prompted, click "Reopen in Container"
3. All dependencies will be automatically installed

---

## How to Contribute

### Reporting Issues

- Use the [GitHub Issues](https://github.com/jonathan-vella/microsoft-sovereign-cloud-brain-trek/issues) page
- Check existing issues before creating a new one
- Use the provided issue templates when available
- Include clear descriptions and reproduction steps

### Suggesting Enhancements

- Open an issue with the "enhancement" label
- Describe the improvement and its benefits
- Include examples or mockups if applicable

### Contributing Content

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Run linting: `markdownlint-cli2 "**/*.md"`
5. Test locally with Jekyll
6. Commit your changes
7. Push to your fork
8. Open a Pull Request

---

## Content Guidelines

### File Structure

```text
docs/
├── level-50/      # Prerequisites (1-2 weeks)
├── level-100/     # Foundational (2-4 weeks)
├── level-200/     # Intermediate (4-6 weeks)
├── level-300/     # Advanced (8-12 weeks)
└── resources/     # External references
```

### File Naming

- Use lowercase with hyphens: `topic-name.md`
- Module overviews: `module-0N-topic.md`
- Knowledge checks: `topic-knowledge-check.md`
- Labs: `lab-0N-name.md`

### Required Front Matter

All content pages must include YAML front matter:

```yaml
---
layout: default
title: Page Title
nav_order: 1
parent: Parent Section Name
description: "Brief description for SEO"
---
```

### Writing Style

- Use clear, concise technical language
- Define acronyms on first use
- Use active voice
- Include practical examples
- Reference official Microsoft Learn documentation

---

## Pull Request Process

1. **Before submitting:**
   - Run `markdownlint-cli2 "**/*.md"` and fix any errors
   - Test the Jekyll build locally
   - Ensure all links are valid
   - Update related documentation if needed

2. **PR requirements:**
   - Clear, descriptive title
   - Description of changes and motivation
   - Reference related issues (if any)
   - Screenshots for visual changes

3. **Review process:**
   - PRs require at least one approving review
   - Address reviewer feedback promptly
   - Keep PRs focused and reasonably sized

---

## Style Guide

### Markdown Standards

This project uses markdownlint with custom configuration. Key rules:

- ATX-style headings (`#`, `##`, `###`)
- Dash (`-`) for unordered lists
- Blank lines around headings and lists
- Fenced code blocks with language specifiers
- No trailing punctuation in headings (except `?`)

### Code Blocks

Always specify the language:

````markdown
```powershell
Get-AzResourceGroup -Name "sovereign-rg"
```

```yaml
apiVersion: v1
kind: ConfigMap
```
````

### Links

- **Internal links:** Use relative paths (`../level-100/topic.md`)
- **External links:** Use full URLs with descriptive text
- **Microsoft Learn:** Include as references where applicable

### Callouts

Use Jekyll callout syntax:

```markdown
{: .note }
> **Note:** Additional helpful information.

{: .warning }
> **Warning:** Important caution for the reader.
```

---

## Questions?

If you have questions about contributing, please:

1. Check the [documentation](docs/README.md)
2. Search existing [issues](https://github.com/jonathan-vella/microsoft-sovereign-cloud-brain-trek/issues)
3. Open a new issue with your question

Thank you for contributing to this project!
