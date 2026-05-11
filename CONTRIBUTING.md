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
   cd site
   npm ci
   ```

3. **Run the site locally:**

   ```bash
   npm run dev
   ```

4. **Open in browser:** Navigate to `http://localhost:4321/microsoft-sovereign-cloud-brain-trek/`

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
3. Make your changes under `site/src/content/docs/**`
4. Run linting: `npx markdownlint-cli2` (from repo root) and `npm run check` (from `site/`)
5. Run a full build to catch broken links / schema issues: `cd site && npm run build`
6. Commit your changes
7. Push to your fork
8. Open a Pull Request

---

## Content Guidelines

### File Structure

```text
site/src/content/docs/
├── level-50/      # Prerequisites (1-2 weeks)
├── level-100/     # Foundational (2-4 weeks)
├── level-200/     # Intermediate (4-6 weeks)
├── level-300/     # Advanced (8-12 weeks)
└── resources/     # External references
site/public/images/  # Static images served at /images/...
```

### File Naming

- Use lowercase with hyphens: `topic-name.md`
- Module overviews: `module-0N-topic.md`
- Knowledge checks: `topic-knowledge-check.md`
- Labs: `lab-0N-name.md`

### Required Front Matter

All content pages must include YAML front matter. The Zod content-collection
schema validates this at build time (see `site/src/content.config.ts`):

```yaml
---
title: Page Title
description: "Brief description for SEO (required, 20-220 chars)"
sidebar:
  order: 1                # Optional: position in the sidebar
  hidden: false           # Optional: hide from the sidebar
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
   - Run `npx markdownlint-cli2` from the repo root and fix any errors
   - Run `cd site && npm run check && npm run build` and confirm both pass
   - Update related documentation (CONTRIBUTING.md, README.md) if needed

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

- **Internal links:** Use Starlight slugs (no `.md` extension, trailing slash) — e.g. `[Foo](../module-01-topic/foo/)`.
- **External links:** Use full URLs with descriptive text.
- **Microsoft Learn:** Include as references where applicable.
- The site's **base path** is `/microsoft-sovereign-cloud-brain-trek/`. Use root-relative paths (`/level-XX/...`) or relative paths; never hard-code the base path.

### Callouts

Use Starlight aside syntax:

```markdown
:::note[Optional title]
Additional helpful information.
:::

:::caution[Optional title]
Important caution for the reader.
:::

:::tip[Optional title]
Useful tip or "good to know".
:::
```

---

## Authoring conventions for `site/`

### Components

- **Knowledge checks** use the `<KnowledgeCheck answer="B" reference="...">…</KnowledgeCheck>` component (see `site/src/components/KnowledgeCheck.astro`). Children are rich MDX containing the question, options, and explanation.
- **Mermaid diagrams** wrapped for collapse use `<DiagramContainer title="…" defaultOpen>` (see `site/src/components/DiagramContainer.astro`).
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

## Rollback runbook (post-cutover safety net)

If a regression on `main` breaks the Astro deploy in production, restore the
previous Jekyll site using the `legacy/jekyll-last` tag (the last commit before
the Phase 6 cutover).

1. **Revert the cutover merge commit** on `main`:

   ```bash
   git revert <astro-cutover-merge-commit>
   git push origin main
   ```

2. **Restore the Jekyll workflow and source tree** from the tag:

   ```bash
   git checkout legacy/jekyll-last -- docs/ _config.yml Gemfile .github/workflows/jekyll-deploy.yml.disabled
   git mv .github/workflows/jekyll-deploy.yml.disabled .github/workflows/jekyll-deploy.yml
   ```

3. **Disable the Astro workflow** (so it doesn't race with the Jekyll one):

   ```bash
   git mv .github/workflows/astro-deploy.yml .github/workflows/astro-deploy.yml.disabled
   ```

4. **Commit and push**:

   ```bash
   git commit -m "rollback: restore jekyll-deploy from legacy/jekyll-last"
   git push origin main
   ```

5. **Trigger the Jekyll workflow manually** via the Actions tab
   (_Run workflow_ on _Deploy Jekyll Site to GitHub Pages_). If the Pages
   cache is stale, force a redeploy by pushing a no-op edit to any file
   under `docs/`.
6. **Verify production**: hit
   `https://jonathan-vella.github.io/microsoft-sovereign-cloud-brain-trek/`
   and spot-check three deep URLs.
7. **Open a tracking issue** with the failure mode so the next cutover
   attempt addresses the root cause before retrying.

---

## Questions?

If you have questions about contributing, please:

1. Check the [content tree](site/src/content/docs/)
2. Search existing [issues](https://github.com/jonathan-vella/microsoft-sovereign-cloud-brain-trek/issues)
3. Open a new issue with your question

Thank you for contributing to this project!
