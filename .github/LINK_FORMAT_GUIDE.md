# Jekyll Link Format Guide

**Critical for GitHub Pages with baseurl**

## The Problem

When GitHub Pages uses a `baseurl` (like `/microsoft-sovereign-cloud-brain-trek/`), standard markdown links break:

- ❌ Relative links: `[text](file)` → Goes to `https://domain.com/file`
- ❌ Absolute links: `[text](/level-100/file)` → Goes to `https://domain.com/level-100/file`

Both resolve to the **domain root** instead of including the baseurl path.

## The Solution

Use **Jekyll link tags with baseurl** for ALL internal content links:

```markdown
[Link Text]({{ site.baseurl }}{% link level-100/file-name.md %})
```

This generates: `https://domain.com/microsoft-sovereign-cloud-brain-trek/level-100/file-name/`

## Examples

### ✅ Content Links (in README.md, module files)

```markdown
[Digital Sovereignty Overview]({{ site.baseurl }}{% link level-100/digital-sovereignty.md %})
[Azure Arc Introduction]({{ site.baseurl }}{% link level-100/azure-arc-intro.md %})
[Knowledge Check Quiz]({{ site.baseurl }}{% link level-100/knowledge-check.md %})
```

### ✅ Navigation Buttons

```markdown
**[Start Level 100 →]({{ site.baseurl }}{% link level-100/README.md %})**
**[Next Module →]({{ site.baseurl }}{% link level-200/arc-advanced-management.md %})**
```

### ✅ Images

```markdown
![Architecture Diagram]({{ site.baseurl }}/assets/images/level-100/azure-local-architecture.svg)
```

### ❌ NEVER Use These Formats

```markdown
❌ [Link](file-name)                    # Relative path
❌ [Link](file-name.md)                 # With extension  
❌ [Link](/level-100/file-name)         # Absolute path
❌ [Link](../level-200/file-name)       # Parent relative
❌ [Link](./file-name)                  # Current dir
```

## Link Format by File Type

### In README.md Files

All links to sibling files in the same level:

```markdown
- [Module Name]({{ site.baseurl }}{% link level-100/module-name.md %})
```

### In Module Content Files

Links to other modules in the same or different level:

```markdown
**Prerequisites:** [Azure Arc Basics]({{ site.baseurl }}{% link level-100/azure-arc-intro.md %})

**Next:** [Advanced Patterns]({{ site.baseurl }}{% link level-200/arc-enterprise-patterns.md %})
```

### In index.md or introduction.md

Navigation to level landing pages:

```markdown
[Get Started with Level 100]({{ site.baseurl }}{% link level-100/README.md %})
```

## Path Structure

Jekyll paths are **relative to the source directory** (`docs/`):

```yaml
# _config.yml
source: docs
```

So paths in link tags should be:

- ✅ `level-100/file.md` (relative to docs/)
- ❌ `docs/level-100/file.md` (docs/ prefix not needed)
- ❌ `/level-100/file.md` (leading slash not needed)

## External Links

External links use normal markdown (no Jekyll tags):

```markdown
✅ [Microsoft Learn](https://learn.microsoft.com/azure)
✅ [Azure Portal](https://portal.azure.com)
```

## Validation

Before committing changes, validate all links:

```powershell
.\scripts\Check-BrokenLinks.ps1
```

This script checks:
- ✅ Jekyll link tag format
- ✅ File existence
- ✅ No .html extensions
- ❌ Broken relative paths
- ❌ Broken absolute paths

## Converting Existing Links

If you have files with wrong link formats, use the fix script:

```powershell
# Dry run first
.\scripts\Fix-ReadmeLinks.ps1 -DryRun

# Apply fixes
.\scripts\Fix-ReadmeLinks.ps1
```

This converts:
- `[text](file)` → `[text]({{ site.baseurl }}{% link level-XXX/file.md %})`

## Benefits

1. **Works with baseurl** - Links include the correct path prefix
2. **Build-time validation** - Jekyll fails if linked file doesn't exist
3. **Refactoring safe** - Rename files and Jekyll updates links automatically
4. **Clean URLs** - Generated as pretty URLs without .html extensions

## Testing

### Local Testing

```powershell
bundle exec jekyll serve
```

Access: `http://localhost:4000/microsoft-sovereign-cloud-brain-trek/`

Click all links - they should work.

### Production Testing

After deployment: `https://jonathan-vella.github.io/microsoft-sovereign-cloud-brain-trek/`

- ✅ Navigation sidebar links work
- ✅ Content inline links work  
- ✅ Button links work
- ✅ All include baseurl prefix

## Common Mistakes

### Mistake 1: Using .html extension

```markdown
❌ [Link](file.html)
✅ [Link]({{ site.baseurl }}{% link level-100/file.md %})
```

Jekyll generates pretty URLs without extensions.

### Mistake 2: Including docs/ in path

```markdown
❌ {% link docs/level-100/file.md %}
✅ {% link level-100/file.md %}
```

The `source: docs` config means paths are relative to docs/.

### Mistake 3: Forgetting {{ site.baseurl }}

```markdown
❌ [Link]({% link level-100/file.md %})
✅ [Link]({{ site.baseurl }}{% link level-100/file.md %})
```

Without baseurl, links work locally but break in production.

### Mistake 4: Using relative paths "because they're shorter"

```markdown
❌ [Link](file-name)  # Shorter, but BREAKS with baseurl
✅ [Link]({{ site.baseurl }}{% link level-100/file-name.md %})  # Longer, but WORKS
```

Always use the correct format, even if verbose.

## Quick Reference Card

```markdown
# Internal content link
[Text]({{ site.baseurl }}{% link level-100/file.md %})

# Navigation button
**[Start →]({{ site.baseurl }}{% link level-100/README.md %})**

# Image
![Alt]({{ site.baseurl }}/assets/images/level-100/diagram.svg)

# External link
[Microsoft Learn](https://learn.microsoft.com)
```

---

**Remember:** When in doubt, match the format used in navigation buttons. They already work correctly!

**Last Updated:** October 22, 2025
