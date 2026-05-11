# Dev Container Configuration

This directory contains the development container configuration for the
Sovereign Cloud Brain Trek project.

## Overview

The dev container provides a consistent, pre-configured environment for
building and contributing to the Astro Starlight documentation site.

## Base Image

- **Image:** `mcr.microsoft.com/devcontainers/javascript-node:1-20-bookworm`
- **OS:** Debian 12 (Bookworm)
- **Node.js:** 20.x pre-installed

## Included Features

| Feature | Version | Purpose                                  |
| ------- | ------- | ---------------------------------------- |
| Python  | 3.12    | Ad-hoc scripts (no longer required for builds) |

## VS Code Extensions

The following extensions are installed automatically:

| Extension              | Purpose                                |
| ---------------------- | -------------------------------------- |
| Astro                  | `.astro` and `.mdx` language support   |
| markdownlint           | Markdown linting                       |
| Markdown All in One    | Markdown editing features              |
| Markdown Mermaid       | Mermaid diagram preview                |
| YAML                   | YAML language support                  |
| EditorConfig           | Consistent editor settings             |
| Prettier               | Code formatting                        |

## Forwarded Ports

| Port | Service                       |
| ---- | ----------------------------- |
| 4321 | Astro dev / preview server    |

## Getting Started

1. **Open in VS Code** with the Dev Containers extension installed.
2. **Rebuild Container** when prompted (or use Command Palette →
   _Dev Containers: Rebuild Container_).
3. **Wait for setup** — `postCreateCommand` runs `npm ci --prefix site` and
   `pre-commit install`.

### Running the Site Locally

```bash
cd site
npm run dev                 # dev server with live reload
npm run check               # type and content-collection check
npm run build               # full static build into site/dist/
npm run preview             # serve the built site
```

The dev server is reachable at
`http://localhost:4321/microsoft-sovereign-cloud-brain-trek/`.

### Running Linters

```bash
# Lint all markdown
npx markdownlint-cli2

# Run pre-commit hooks against the working tree
pre-commit run --all-files
```

## Customization

### Adding VS Code Extensions

Edit `devcontainer.json` and add extension IDs to
`customizations.vscode.extensions`.

### Adding System Packages

Append to `postCreateCommand`:

```json
"postCreateCommand": "... && sudo apt-get install -y <package>"
```

## Troubleshooting

### Container Build Fails

1. Confirm Docker is running.
2. Try _Dev Containers: Rebuild Container Without Cache_.
3. Check `postCreateCommand` for errors.

### Astro Dev Server Won't Start

```bash
# Re-install dependencies cleanly
cd site
rm -rf node_modules
npm ci

# Check for port conflicts
lsof -i :4321
```
