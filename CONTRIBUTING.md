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

## Working on the Astro site (`site/`)

The repo is **mid-migration** from Jekyll (`docs/`) to Astro Starlight (`site/`).
Both trees are live; the Jekyll site is the production deployment until the
Phase 6 cutover.

### When to edit which tree

| Editing                                | Tree                                | Why                                                                                  |
| -------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------ |
| Existing content (typo / clarification) | `docs/` AND `site/src/content/docs/`| Until cutover, **both trees must stay in sync**. Re-run `npm run migrate` after editing `docs/`. |
| Brand-new content                      | `site/src/content/docs/`            | New content authored directly in Starlight format; no kramdown round-trip needed.    |
| Workflow / tooling                     | repo root                           | `.github/workflows/*`, `package.json`, lint configs.                                 |

### Astro authoring conventions

- **Knowledge checks** use the `<KnowledgeCheck answer="B">…</KnowledgeCheck>` component (see `site/src/components/KnowledgeCheck.astro`).
- **Mermaid diagrams** wrapped for collapse use `<DiagramContainer title="…">` (see `site/src/components/DiagramContainer.astro`).
- **Callouts** use Starlight asides: `:::note`, `:::tip`, `:::caution`, `:::danger`.
- A file becomes `.mdx` only if it uses one of the components above; otherwise it stays `.md`.

### Astro Docs MCP server (Copilot)

The workspace ships a Model Context Protocol config at `.vscode/mcp.json` that
points GitHub Copilot at the official [Astro Docs MCP](https://docs.astro.build/en/guides/build-with-ai/)
server. When you ask Copilot a question about Astro or Starlight, it will
search official docs first.

For the **Copilot Coding Agent** (server-side runs that don't read
`.vscode/mcp.json`), add the equivalent server in repo settings under
_Settings → Copilot → Coding agent → MCP servers_:

```json
{
  "mcpServers": {
    "astro-docs": {
      "type": "http",
      "url": "https://mcp.docs.astro.build/mcp",
      "tools": ["search_astro_docs"]
    }
  }
}
```

---

## Rollback runbook (Phase 6 cutover)

If the post-cutover Astro deploy is broken in production, follow this sequence
to restore the Jekyll site. **Practice this once in a staging fork before
cutover** so the timing is known.

1. **Revert the cutover merge commit** on `main`:

   ```bash
   git revert <astro-cutover-merge-commit>
   git push origin main
   ```

2. **Re-enable the Jekyll workflow**:

   ```bash
   git mv .github/workflows/jekyll-deploy.yml.disabled .github/workflows/jekyll-deploy.yml
   ```

3. **Disable the Astro workflow** (so it doesn't race with the Jekyll one):

   ```bash
   git mv .github/workflows/astro-deploy.yml .github/workflows/astro-deploy.yml.disabled
   ```

4. **Commit and push** the workflow renames:

   ```bash
   git commit -m "rollback: re-enable jekyll-deploy, disable astro-deploy"
   git push origin main
   ```

5. **Trigger the Jekyll workflow manually** via the Actions tab
   (`Run workflow` on _Deploy Jekyll Site to GitHub Pages_).
   If the Pages cache is stale, force a redeploy by pushing a no-op edit to any
   file under `docs/`.
6. **Verify production**: hit `https://jonathan-vella.github.io/microsoft-sovereign-cloud-brain-trek/`
   and spot-check three deep URLs. Check `_site/` rendered correctly via the
   Pages deployment log.
7. **Open a tracking issue** with the failure mode so the next cutover attempt
   addresses the root cause before retrying.

---

## Questions?

If you have questions about contributing, please:

1. Check the [documentation](docs/README.md)
2. Search existing [issues](https://github.com/jonathan-vella/microsoft-sovereign-cloud-brain-trek/issues)
3. Open a new issue with your question

Thank you for contributing to this project!
