# Pull Request

## Description

<!-- Provide a brief description of your changes -->

## Type of Change

<!-- Mark the relevant option with an 'x' -->

- [ ] 📝 Content update (documentation, tutorials, knowledge checks)
- [ ] 🐛 Bug fix (broken links, typos, formatting issues)
- [ ] ✨ New feature (new module, lab, or learning path)
- [ ] 🎨 Visual asset (diagrams, images, mermaid charts)
- [ ] 🔧 Configuration change (Astro, workflows, tooling)
- [ ] 📚 Other (please describe)

## Learning Level Affected

<!-- Mark all that apply -->

- [ ] Level 50 - Essentials
- [ ] Level 100 - Foundational
- [ ] Level 200 - Intermediate
- [ ] Level 300 - Advanced
- [ ] Resources
- [ ] N/A (infrastructure changes)

## Modules Affected

<!-- Mark all that apply -->

- [ ] Digital Sovereignty
- [ ] Cloud Models
- [ ] Azure Local
- [ ] Azure Arc
- [ ] Edge RAG / Foundry Local
- [ ] Microsoft 365 Local
- [ ] Sovereign Public Cloud controls
- [ ] Sovereign Private Cloud stack
- [ ] Sovereign Landing Zone
- [ ] Security & Compliance
- [ ] Pre-Sales & Discovery
- [ ] Other/Infrastructure

## Checklist

<!-- Ensure all items are completed before submitting -->

- [ ] I have read the [CONTRIBUTING.md](../CONTRIBUTING.md) guidelines
- [ ] My changes follow the project's markdown formatting standards
- [ ] I have run `markdownlint-cli2` and fixed any issues
- [ ] I have run `npm run check` and `npm run build` from `site/` and both pass
- [ ] I have run `npm run emit-legacy-stubs`, `npm run check:urls`, and `npm run lint:content` from `site/` and they pass
- [ ] Moved, renamed, or deleted pages have entries in `site/redirects.json` (no entries removed)
- [ ] All links are valid and use root-relative Starlight slugs (no `.md` extension, trailing slash, no hard-coded base path)
- [ ] Images have descriptive alt text
- [ ] YAML front matter is complete and valid (title + description required)
- [ ] Code blocks specify the correct language

## Content Quality Checklist

<!-- For content changes only -->

- [ ] Learning objectives are clearly stated
- [ ] Content is technically accurate
- [ ] Facts checked against Microsoft Learn or official Microsoft blogs; `lastVerified` set on every changed page
- [ ] Every changed page ends with a `## Sources` section; volatile facts (status, dates, limits, legal) are cited inline
- [ ] Unslop pass done on new and rewritten prose (`.github/skills/unslop/SKILL.md`)
- [ ] Page-audit coverage: every page this PR owns in the rebuild outline is done, or listed below as pending
- [ ] Microsoft Learn references include full URLs
- [ ] Knowledge check questions have explanations
- [ ] Terminology is consistent with project standards

## Validation

<!-- Paste each command you ran from site/ with its result (passed / failed) -->

## Screenshots

<!-- If applicable, add screenshots to demonstrate changes -->

## Related Issues

<!-- Link any related issues using #issue-number -->

Closes #

## Additional Notes

<!-- Any additional context or information for reviewers -->
