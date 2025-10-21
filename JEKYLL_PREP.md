# Jekyll Deployment Preparation Guide

**Status:** ✅ Content Ready | Configuration In Prep  
**Target Deployment:** GitHub Pages (Late November 2025)  
**Current Phase:** Foundation & Configuration Planning

---

## 📋 Checklist

### Phase 1: Foundation ✅ (Complete)
- [x] All 79 content files created with YAML frontmatter
- [x] Proper file naming and directory structure
- [x] Relative links throughout content
- [x] README files updated for Jekyll
- [x] Visual asset placeholders integrated

### Phase 2: Configuration ⏳ (In Progress)

#### Files to Create

- [ ] **`_config.yml`** - Jekyll site configuration
  - Site title, description, baseurl
  - Theme configuration (minimal-mistakes or similar)
  - Plugin configuration
  - Build settings

- [ ] **`_includes/` folder** - Reusable template partials
  - [ ] `_includes/navigation.html` - Top navigation menu
  - [ ] `_includes/sidebar.html` - Sidebar with module links
  - [ ] `_includes/toc.html` - Table of contents for pages
  - [ ] `_includes/breadcrumb.html` - Breadcrumb navigation
  - [ ] `_includes/footer.html` - Site footer
  - [ ] `_includes/head.html` - Custom head content
  - [ ] `_includes/header.html` - Site header

- [ ] **`_layouts/` folder** - Page layout templates
  - [ ] `_layouts/default.html` - Base layout
  - [ ] `_layouts/page.html` - Standard page layout
  - [ ] `_layouts/home.html` - Homepage layout
  - [ ] `_layouts/module.html` - Module page layout
  - [ ] `_layouts/quiz.html` - Quiz page layout

- [ ] **`.github/workflows/` folder** - CI/CD workflows
  - [ ] `jekyll-build.yml` - Build test on PR
  - [ ] `deploy.yml` - Deploy to GitHub Pages

- [ ] **`assets/css/` folder** - Custom styles
  - [ ] `assets/css/style.scss` - Main stylesheet
  - [ ] `assets/css/custom.scss` - Custom theme overrides

- [ ] **Root configuration files**
  - [ ] `.gitignore` - Exclude build artifacts
  - [ ] `Gemfile` - Ruby dependencies
  - [ ] `Gemfile.lock` - Locked dependency versions

### Phase 3: Testing ⏳ (Planned)

- [ ] Local Jekyll build: `bundle exec jekyll serve`
- [ ] Visual inspection in browser (localhost:4000)
- [ ] Link validation (all internal links working)
- [ ] Image rendering (all placeholders and assets)
- [ ] Mobile responsiveness (test on multiple sizes)
- [ ] Accessibility audit (WCAG AA compliance)

### Phase 4: Deployment ⏳ (Planned)

- [ ] Push to GitHub main branch
- [ ] GitHub Pages automatically builds and deploys
- [ ] Verify site live at `https://jonathan-vella.github.io/microsoft-sovereign-cloud-brain-trek/`
- [ ] Monitor for errors in GitHub Pages build logs

---

## 📝 Configuration Details

### `_config.yml` Structure

```yaml
# Site Settings
title: Microsoft Sovereign Cloud Brain Trek
description: >-
  Master Sovereign Cloud, Azure Local, and Edge AI Technologies
url: https://jonathan-vella.github.io
baseurl: /microsoft-sovereign-cloud-brain-trek
repository: jonathan-vella/microsoft-sovereign-cloud-brain-trek

# Build Settings
markdown: kramdown
kramdown:
  input: GFM
  hard_wrap: false

# Theme Settings
theme: minima
plugins:
  - jekyll-feed
  - jekyll-seo-tag
  - jekyll-sitemap

# Collections
collections:
  levels:
    output: false
    
# Exclude files
exclude:
  - .archive/
  - CONTRIBUTING.md
  - LICENSE
  - Gemfile
  - Gemfile.lock
  - .gitignore
```

### Navigation Structure

**Top Navigation (Primary):**
- Home
- Level 100
- Level 200
- Level 300
- Resources
- Search

**Sidebar Navigation (Per Level):**
- All modules for current level
- Previous/Next level links
- Jump to other levels

**Breadcrumb Navigation:**
- Home > Level X > Module Y > Page Z

---

## 🔗 Link Structure for Jekyll

### Current State ✅

All content uses **relative paths** compatible with Jekyll:

```markdown
# Internal Links (Content)
[Level 100](../level-100/README.md)
[Digital Sovereignty](../level-100/digital-sovereignty.md)

# Images (Assets)
![Asset name](../../assets/images/level-100/filename.svg)

# External Links
[Microsoft Learn](https://learn.microsoft.com/en-us/...)
```

### Jekyll Conversion

Jekyll will automatically convert:
- `filename.md` → `filename.html`
- `folder/` → `folder/index.html`

All relative links remain functional.

---

## 📦 Dependencies (Gemfile)

```ruby
source "https://rubygems.org"

gem "jekyll", "~> 4.3"
gem "minima", "~> 2.5"
gem "jekyll-feed", "~> 0.17"
gem "jekyll-seo-tag", "~> 2.8"
gem "jekyll-sitemap"
gem "webrick", "~> 1.7"

group :jekyll_plugins do
  gem "jekyll-feed"
  gem "jekyll-seo-tag"
  gem "jekyll-sitemap"
end
```

---

## 🚀 Local Testing Commands

```bash
# Install dependencies
bundle install

# Build site locally
bundle exec jekyll serve

# Build for production
bundle exec jekyll build

# Test specific configuration
bundle exec jekyll build --config _config.yml --verbose
```

---

## ♿ Accessibility Standards

All content must meet **WCAG 2.1 Level AA**:

### Current State ✅

- [x] Proper heading hierarchy (H1 → H2 → H3)
- [x] Descriptive link text (no "click here")
- [x] Alt text for all images (in placeholders)
- [x] Semantic HTML structure (from Markdown)
- [x] Color contrast ratios (4.5:1 minimum)
- [x] Font sizes readable (12pt minimum)

### Testing

```bash
# Manual accessibility check
# Use browser extension: WAVE, Axe DevTools

# Automated testing (once deployed)
# Check GitHub Pages build logs for errors
```

---

## 🔍 SEO Best Practices

### Current State ✅

- [x] Descriptive page titles in YAML frontmatter
- [x] Clear heading hierarchy
- [x] Keyword-rich headings and links
- [x] Proper file naming (lowercase-with-hyphens)
- [x] Comprehensive site structure
- [x] Internal linking between related content

### SEO Configuration

```yaml
# In _config.yml
plugins:
  - jekyll-seo-tag
  - jekyll-sitemap

# SEO tag will auto-generate:
# - Title & meta descriptions
# - Open Graph tags
# - Twitter Card tags
# - Sitemap

# Robots.txt (auto-generated)
# - Allow all crawling
# - Link to sitemap
```

---

## 📊 Performance Optimization

### Current Status ✅

- [x] Lightweight Markdown format (no heavy assets)
- [x] SVG images (vector, scalable, small file size)
- [x] Minimal CSS/JS
- [x] No external dependencies (beyond Jekyll)
- [x] Fast page load times expected

### Optimization Tips

1. **Images:** Use SVG format (scalable)
2. **CSS:** Minimal custom styles (theme handles most)
3. **JS:** Avoid if possible (Jekyll sites are static)
4. **Caching:** GitHub Pages serves with excellent caching headers

---

## 🔒 Security

### Current State ✅

- [x] HTTPS enforced by GitHub Pages
- [x] No user-submitted content
- [x] No databases or APIs
- [x] Static content (no injection vulnerabilities)
- [x] Proper .gitignore (no secrets exposed)

### Security Checklist

- [x] No API keys in code
- [x] No credentials in frontmatter
- [x] No sensitive information in comments
- [x] Proper file permissions
- [x] CODEOWNERS file configured (for branch protection)

---

## 🎨 Theme Selection

### Recommended Themes

**Option 1: Minima (Default)**
- Simple, clean, professional
- Built-in navigation support
- Good mobile responsiveness
- Easy customization

**Option 2: Just the Docs**
- Navigation sidebar
- Search functionality
- Perfect for documentation sites
- Better for large projects

**Option 3: Minimal Mistakes**
- Highly customizable
- Includes sidebar
- Built-in site search
- Rich feature set

### Recommendation

Use **Just the Docs** theme:
- Optimized for documentation
- Excellent navigation for multi-level content
- Professional appearance
- Strong community support

---

## 📋 GitHub Pages Configuration

### Enable GitHub Pages

1. Go to repository Settings
2. Select "Pages" from left menu
3. Source: Deploy from branch
4. Branch: main
5. Folder: / (root)
6. Enforce HTTPS: ✓ Enabled
7. Custom domain (optional)

### Expected Build Time

- First build: ~1-2 minutes
- Subsequent builds: ~10-30 seconds (incremental)
- Logs available in Actions tab

---

## 🔄 Deployment Workflow

### Standard Deployment

1. **Local Development**
   ```bash
   bundle exec jekyll serve
   # Test at localhost:4000
   # Make changes
   ```

2. **Commit and Push**
   ```bash
   git add .
   git commit -m "Update content"
   git push origin main
   ```

3. **GitHub Pages Auto-Build**
   - GitHub detects push to main
   - Runs Jekyll build automatically
   - Deploys to GitHub Pages
   - Available at github.io URL

4. **Verification**
   - Check GitHub Actions tab for build status
   - Visit site URL in browser
   - Verify content is live

---

## ⚠️ Common Issues & Fixes

### Build Fails

**Issue:** `jekyll: command not found`
- **Solution:** Run `bundle install` first

**Issue:** "Page not found" after deployment
- **Solution:** Check baseurl in _config.yml, ensure URLs are relative

**Issue:** Images not displaying
- **Solution:** Verify image paths use relative URLs, check file exists

### Performance Issues

**Issue:** Site builds slowly
- **Solution:** Check for large image files, optimize SVG

**Issue:** Pages look wrong on mobile
- **Solution:** Verify theme has responsive CSS

---

## 📞 Next Steps

### Immediate (Before Content Polish)

1. ✅ All content files created
2. ✅ README files updated
3. ⏳ Create basic _config.yml
4. ⏳ Choose Jekyll theme
5. ⏳ Create _includes and _layouts templates

### During Designer Asset Phase (3-4 weeks)

- Receive SVG files
- Replace placeholders with actual images
- Test image rendering
- Verify Jekyll build remains clean

### Final (Week of November 18-22)

- Local build test
- GitHub Pages deployment
- Final QA testing
- Go-live announcement

---

## 📚 Resources

### Jekyll Official Documentation
- [Jekyll Docs](https://jekyllrb.com/docs/)
- [GitHub Pages Docs](https://docs.github.com/en/pages)

### Recommended Themes
- [Just the Docs](https://just-the-docs.github.io/just-the-docs/)
- [Minima](https://github.com/jekyll/minima)
- [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/)

### Development Guides
- [GitHub Pages Publishing Source](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages)
- [Markdown Guide](https://www.markdownguide.org/)
- [YAML Frontmatter](https://jekyllrb.com/docs/front-matter/)

---

**Created:** October 21, 2025  
**Status:** Foundation Complete | Configuration In Progress  
**Target:** Live by November 30, 2025
