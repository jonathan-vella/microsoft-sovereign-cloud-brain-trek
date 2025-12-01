# Dev Container Configuration

This directory contains the development container configuration for the Sovereign Cloud Brain Trek project.

## Overview

The dev container provides a consistent, pre-configured development environment with all the tools needed to build, test, and contribute to this Jekyll-based documentation site.

## Base Image

- **Image:** `mcr.microsoft.com/devcontainers/jekyll:2-bookworm`
- **OS:** Debian 12 (Bookworm)
- **Ruby:** Pre-installed with Jekyll and Bundler

## Included Features

| Feature | Version | Purpose |
|---------|---------|---------|
| Node.js | LTS | markdownlint-cli2, npm scripts |
| Python | 3.12 | Diagram generation scripts |

## Pre-installed Tools

### Ruby/Jekyll

- `jekyll` — Static site generator
- `bundler` — Ruby dependency management
- `github-pages` gem — GitHub Pages compatibility

### Node.js

- `markdownlint-cli2` — Markdown linting
- `npm` — Package management

### Python

- `matplotlib` — Diagram generation
- `pillow` — Image processing
- `diagrams` — Infrastructure diagrams
- `cartopy` — Geographic mapping
- `pre-commit` — Git hooks

### System

- `graphviz` — DOT graph rendering
- `libgeos-dev`, `libproj-dev` — Cartopy dependencies

## VS Code Extensions

The following extensions are automatically installed:

| Extension | Purpose |
|-----------|---------|
| Ruby LSP | Ruby language support |
| Shopify Liquid | Liquid template syntax |
| markdownlint | Markdown linting |
| Markdown All in One | Markdown editing features |
| Markdown Mermaid | Mermaid diagram preview |
| YAML | YAML language support |
| EditorConfig | Consistent editor settings |
| Prettier | Code formatting |

## Forwarded Ports

| Port | Service |
|------|---------|
| 4000 | Jekyll development server |

## Getting Started

1. **Open in VS Code** with the Dev Containers extension installed
2. **Rebuild Container** when prompted (or use Command Palette → "Dev Containers: Rebuild Container")
3. **Wait for setup** — the `postCreateCommand` installs dependencies automatically

### Running the Site Locally

```bash
# Start Jekyll development server
bundle exec jekyll serve --livereload

# Or use the npm script
npm run serve
```

The site will be available at `http://localhost:4000`.

### Running Linters

```bash
# Lint all markdown files
npx markdownlint-cli2 "docs/**/*.md"

# Run pre-commit hooks manually
pre-commit run --all-files
```

## Customization

### Adding VS Code Extensions

Edit `devcontainer.json` and add extension IDs to the `customizations.vscode.extensions` array.

### Adding System Packages

Append to the `postCreateCommand` in `devcontainer.json`:

```json
"postCreateCommand": "... && sudo apt-get install -y <package-name>"
```

### Adding Python Packages

Add to `requirements.txt` in the repository root.

## Troubleshooting

### Container Build Fails

1. Check Docker is running
2. Try "Dev Containers: Rebuild Container Without Cache"
3. Check `postCreateCommand` for errors

### Jekyll Won't Start

```bash
# Reinstall gems
bundle install

# Check for port conflicts
lsof -i :4000
```

### Markdownlint Issues

```bash
# Reinstall markdownlint-cli2
npm install -g markdownlint-cli2
```
