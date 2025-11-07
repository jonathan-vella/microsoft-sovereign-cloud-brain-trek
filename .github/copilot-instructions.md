<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# Project: Microsoft Sovereign Cloud Brain Trek

## Project Overview
- **Official Name:** Microsoft Sovereign Cloud Brain Trek
- **Tagline:** Master Sovereign Cloud, Azure Local, and Edge AI Technologies
- **Subtitle:** A comprehensive learning journey for architects and solutions professionals
- **Type:** Static documentation site / Comprehensive skilling program
- **Target Audience:** Sales professionals, architects, and technical experts learning Microsoft Sovereign Cloud, Azure Local, and Edge AI technologies
- **Delivery:** Markdown-based content in /docs folder, deployed via Jekyll/GitHub Pages
- **Structure:** 3 progressive learning levels (100/200/300) with 16 modules, 10 labs, 75+ assessments
- **Status:** Content 100% complete, Jekyll deployed and configured (October 2025)

## Current Project Status (October 31, 2025)

### ✅ Content Development: 100% COMPLETE
- **79 markdown files** across 3 learning levels
- **16 modules** with progressive learning paths (Crawl → Walk → Run)
- **10 hands-on labs** with 58+ practical exercises
- **75+ quiz questions** with detailed explanations
- **~10,000 lines** of educational content

### 🎨 Visual Assets: Designer Phase
- **59 diagrams specified** across all levels
- Documentation complete in `docs/assets/images/README.md`
- Specifications ready in `docs/level-XXX/VISUAL_SPECIFICATIONS.md`
- Placeholder integration complete in all content files
- Designer handoff package ready in `.github/PHASE_4_DESIGNER_HANDOFF_L300.md`
- Estimated completion: 3-4 weeks (external designers)

### 📚 Documentation: Complete & Polished
- ✅ README.md with Learning Journey Map (Mermaid diagram)
- ✅ 9 technology/platform badges (Azure, Kubernetes, GitHub Copilot, Claude Haiku, etc.)
- ✅ CONTRIBUTING.md with contribution guidelines
- ✅ CHANGELOG.md tracking all changes
- ✅ HANDOFF.md with next steps for all stakeholders
- ✅ JEKYLL_PREP.md with complete deployment guide
- ✅ AUTOMATION.md with monthly maintenance workflows
- ✅ All 3 level README files (100/200/300)

### 🤖 Automation: GitHub Actions Configured
- ✅ Link validation workflow (manual trigger)
- ✅ Content freshness check (manual trigger)
- ✅ Microsoft Learn link monitor (manual trigger)
- ✅ Jekyll deployment workflow (auto-deploy to GitHub Pages)
- ✅ PR labeling workflow (auto-labels PRs)
- ✅ Dependabot for dependency updates
- All workflows tested and operational

### 🚀 Jekyll Deployment: Complete & Configured
- ✅ Jekyll configuration complete (_config.yml with Just the Docs theme)
- ✅ Ruby dependencies configured (Gemfile)
- ✅ GitHub Actions deployment workflow configured
- ✅ Automated deployment to GitHub Pages on push
- ✅ Link structure validated (relative paths throughout)
- Site URL: https://jonathan-vella.github.io/microsoft-sovereign-cloud-brain-trek/

### 🎯 Repository Status: Production-Ready
- Clean folder structure (active files only, historical files archived)
- `.github/PROJECT_FILES.md` documenting active project files
- Workspace file created with recommended extensions and tasks
- All cross-references updated and validated
- GitHub Pages deployment configured and automated
- Just the Docs theme v0.10.0 with Mermaid support

## Key Files for Reference

### Documentation
- `README.md` - Project overview with Learning Journey Map
- `CONTRIBUTING.md` - Contribution guidelines
- `CHANGELOG.md` - Complete change history
- `HANDOFF.md` - Stakeholder handoff documentation
- `JEKYLL_PREP.md` - Jekyll deployment guide (420+ lines)
- `GITHUB_PAGES_SETUP.md` - GitHub Pages quick start guide
- `AUTOMATION.md` - Monthly maintenance automation guide

### Designer Resources
- `.github/DESIGNER_QUICK_REFERENCE.md` - Quick start for designers
- `.github/PHASE_4_DESIGNER_HANDOFF_L300.md` - Level 300 asset specifications
- `.github/VISUAL_ASSET_PROCESS.md` - Complete design workflow
- `docs/assets/images/README.md` - Asset registry (59 diagrams)
- `docs/level-XXX/VISUAL_SPECIFICATIONS.md` - Detailed asset specs per level

### Content Structure
- `docs/level-100/` - Foundational concepts (20 files, 5 modules)
- `docs/level-200/` - Intermediate skills (34 files, 6 modules + 5 labs)
- `docs/level-300/` - Advanced expertise (23 files, 5 modules + capstone)

### Automation
- `.github/workflows/link-check.yml` - Link validation
- `.github/workflows/content-freshness.yml` - Stale content detection
- `.github/workflows/ms-learn-monitor.yml` - Microsoft Learn link monitoring
- `.github/workflows/jekyll-deploy.yml` - GitHub Pages deployment
- `.github/workflows/label.yml` - PR auto-labeling
- `.github/dependabot.yml` - Dependency updates
- `scripts/Add-Contributor.ps1` - Automated contributor management

## Working with This Project

### Content Editing Guidelines
- All content files use YAML frontmatter
- Markdown formatting with relative links
- Visual asset placeholders integrated (see VISUAL_ASSET_PROCESS.md)
- Cross-references between modules maintained
- Heading hierarchy: H1 (title) → H2 (sections) → H3 (subsections)

### File Organization
- Active project files in `.github/` directory
- Historical planning docs archived in `.archive/`
- Content organized by learning level (100/200/300)
- Visual assets in `docs/assets/images/` with complete registry

### Next Steps
1. **Designer Engagement** - Share 3 handoff files with designer for visual assets
2. **Asset Integration** - Replace placeholders as SVG files arrive (weekly batches)
3. **GitHub Pages Activation** - Enable GitHub Pages in repository settings
4. **Content Updates** - Monthly maintenance using automation workflows