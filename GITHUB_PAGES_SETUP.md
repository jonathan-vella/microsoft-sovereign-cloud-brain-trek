# GitHub Pages Deployment - Quick Start Guide

**Status:** Configuration Complete ✅  
**Theme:** Just the Docs v0.10.0  
**Target URL:** `https://jonathan-vella.github.io/microsoft-sovereign-cloud-brain-trek/`  
**Estimated Time:** 15-20 minutes

---

## ✅ What's Already Done

- [x] Jekyll configuration file (`_config.yml`)
- [x] Ruby dependencies file (`Gemfile`)
- [x] GitHub Actions deployment workflow
- [x] .gitignore updated for Jekyll
- [x] All 79 content files with proper frontmatter
- [x] Directory structure ready
- [x] Visual asset placeholders integrated

---

## 🚀 Deployment Steps

### Step 1: Install Ruby and Bundler (One-Time Setup)

**On Windows (PowerShell):**

```powershell
# Install Ruby using Chocolatey
choco install ruby

# Restart PowerShell, then install Bundler
gem install bundler

# Verify installation
ruby --version
bundle --version
```

**Alternative:** Download Ruby installer from [RubyInstaller.org](https://rubyinstaller.org/downloads/)

---

### Step 2: Install Jekyll Dependencies

```powershell
# Navigate to repository root
cd c:\Repos\microsoft-sovereign-cloud-brain-trek

# Install all gems from Gemfile
bundle install
```

**Expected output:** Installation of ~50 gems including Jekyll, Just the Docs, and plugins

---

### Step 3: Test Locally

```powershell
# Start Jekyll development server
bundle exec jekyll serve

# Or use the workspace task: Ctrl+Shift+P → "Run Task" → "Preview Site Locally"
```

**Access your site:** Open browser to `http://localhost:4000/microsoft-sovereign-cloud-brain-trek/`

**What to check:**
- ✅ Homepage loads
- ✅ Navigation sidebar appears
- ✅ All 3 learning levels accessible
- ✅ Mermaid diagram renders
- ✅ Search box works
- ✅ Links navigate correctly
- ✅ Code blocks have syntax highlighting

**Stop server:** Press `Ctrl+C` in terminal

---

### Step 4: Enable GitHub Pages

1. **Go to Repository Settings**
   - Navigate to `https://github.com/jonathan-vella/microsoft-sovereign-cloud-brain-trek/settings/pages`

2. **Configure Build and Deployment**
   - **Source:** Select "GitHub Actions" (not "Deploy from a branch")
   - This will use the workflow file we created (`.github/workflows/jekyll-deploy.yml`)

3. **Save Changes**
   - No other configuration needed
   - GitHub will automatically detect the workflow

---

### Step 5: Commit and Deploy

```powershell
# Add all new files
git add _config.yml Gemfile .gitignore .github/workflows/jekyll-deploy.yml

# Commit changes
git commit -m "feat: add Jekyll configuration and GitHub Pages deployment

- Configure Just the Docs theme v0.10.0
- Add Ruby dependencies (Gemfile)
- Create GitHub Actions deployment workflow
- Update .gitignore for Jekyll artifacts
- Enable search, Mermaid diagrams, and navigation"

# Push to GitHub
git push origin main
```

---

### Step 6: Monitor Deployment

1. **Go to Actions Tab**
   - Navigate to `https://github.com/jonathan-vella/microsoft-sovereign-cloud-brain-trek/actions`

2. **Watch Build Progress**
   - You'll see "Deploy Jekyll Site to GitHub Pages" workflow running
   - Typical build time: 1-2 minutes

3. **Check for Success**
   - ✅ Green checkmark = successful deployment
   - ❌ Red X = build failed (click for details)

4. **View Live Site**
   - URL: `https://jonathan-vella.github.io/microsoft-sovereign-cloud-brain-trek/`
   - May take 1-2 minutes after deployment completes

---

## 🎨 Just the Docs Theme Features

### Navigation

**Automatic sidebar** generated from:
- `docs/level-100/` folder → "Level 100" section
- `docs/level-200/` folder → "Level 200" section
- `docs/level-300/` folder → "Level 300" section

**Customization** in each file's frontmatter:
```yaml
---
title: Module Name
nav_order: 1
parent: Level 100
---
```

### Search

**Enabled by default** - searches all content across all pages

### Table of Contents

**Auto-generated** for each page from H2/H3 headings

### Mermaid Diagrams

**Already configured** - your learning journey diagram will render automatically

### Dark Mode

**Built-in toggle** in top-right corner

### Code Copy Button

**Enabled** - hover over code blocks to see copy button

---

## ⚙️ Configuration Highlights

### Key Settings in `_config.yml`

```yaml
# Site URL
url: https://jonathan-vella.github.io
baseurl: /microsoft-sovereign-cloud-brain-trek

# Theme
remote_theme: just-the-docs/just-the-docs@v0.10.0

# Features
search_enabled: true
mermaid:
  version: "10.6.1"
enable_copy_code_button: true
heading_anchors: true
```

### Navigation Links

**Top-right buttons:**
- "View on GitHub" → Repository
- "Microsoft Learn" → Official Azure documentation

**Edit** in `_config.yml`:
```yaml
aux_links:
  "View on GitHub": "https://github.com/..."
  "Microsoft Learn": "https://learn.microsoft.com/..."
```

---

## 🔧 Customization Options

### Change Color Scheme

**Edit `_config.yml`:**
```yaml
color_scheme: dark  # Options: light, dark, custom
```

### Add Custom CSS

1. Create `_sass/custom/custom.scss`
2. Add your styles:
```scss
// Microsoft brand colors
$link-color: #0078d4;
$sidebar-color: #f3f2f1;
```

### Modify Footer

**Edit `_config.yml`:**
```yaml
footer_content: >-
  Your custom footer text here
```

---

## 🐛 Troubleshooting

### Build Fails: "Bundler not found"

```powershell
gem install bundler
bundle install
```

### Local Server Error: "Port 4000 already in use"

```powershell
# Kill process on port 4000
netstat -ano | findstr :4000
taskkill /PID <PID_NUMBER> /F

# Or use different port
bundle exec jekyll serve --port 4001
```

### GitHub Actions Error: "Deployment failed"

**Check workflow logs:**
1. Go to Actions tab
2. Click failed workflow
3. Expand "Build with Jekyll" step
4. Look for error messages

**Common issues:**
- YAML syntax errors in frontmatter
- Missing required files
- Invalid theme configuration

### Pages Don't Display Correctly

**Check baseurl:**
- Must be `/microsoft-sovereign-cloud-brain-trek/`
- All content links MUST use Jekyll link tags: `[text]({{ site.baseurl }}{% link level-100/file.md %})`
- Navigation buttons already use this format
- Images should use: `![alt]({{ site.baseurl }}/assets/images/file.svg)`

**Why this matters:**
- ❌ Relative links like `[text](file)` resolve to domain root, not baseurl path
- ❌ Absolute links like `[text](/level-100/file)` also go to domain root
- ✅ Jekyll link tags with baseurl work correctly: `{{ site.baseurl }}{% link level-100/file.md %}`

---

## 📊 Performance & SEO

### Automatic Features

**Already enabled:**
- ✅ SEO tags (title, description, Open Graph)
- ✅ Sitemap generation (`sitemap.xml`)
- ✅ RSS feed (`feed.xml`)
- ✅ HTTPS enforcement
- ✅ Proper heading hierarchy
- ✅ Mobile responsive design

### Accessibility (WCAG AA)

**Built-in compliance:**
- ✅ Proper contrast ratios
- ✅ Keyboard navigation
- ✅ Screen reader support
- ✅ Alt text for images (in your content)

---

## 📈 What Happens Next

### Automatic Updates

**Every push to `main` triggers:**
1. Jekyll build
2. Content validation
3. Deployment to GitHub Pages
4. Cache refresh

**Build time:** ~30 seconds (incremental builds)

### Link Format Validation

**When adding new content:**
- ✅ Use Jekyll link tags: `[text]({{ site.baseurl }}{% link level-100/file.md %})`
- ✅ Run Check-BrokenLinks.ps1 script before committing
- ❌ Never use relative paths like `[text](file)` in content
- ❌ Never use absolute paths like `[text](/level-100/file)` in content

### Visual Assets Integration

**As designer delivers SVG files:**
1. Move to `docs/assets/images/level-XXX/`
2. Update markdown files (replace placeholders)
3. Commit and push
4. Automatic deployment

---

## 🎯 Next Actions

### Immediate (Today)

- [ ] Run `bundle install`
- [ ] Test locally with `bundle exec jekyll serve`
- [ ] Enable GitHub Pages (Settings → Pages → GitHub Actions)
- [ ] Commit and push configuration files
- [ ] Verify live site after 2-3 minutes

### This Week

- [ ] Customize color scheme (if desired)
- [ ] Add custom logo/favicon
- [ ] Review navigation structure
- [ ] Test all links and pages
- [ ] Share preview URL with team

### Ongoing

- [ ] Integrate designer SVG assets weekly
- [ ] Update content as needed
- [ ] Monitor GitHub Actions builds
- [ ] Check site analytics (optional)

---

## 📚 Resources

### Jekyll Documentation
- [Jekyll Docs](https://jekyllrb.com/docs/)
- [GitHub Pages Docs](https://docs.github.com/en/pages)

### Just the Docs Theme
- [Theme Documentation](https://just-the-docs.com/)
- [Configuration Options](https://just-the-docs.com/docs/configuration/)
- [Navigation Structure](https://just-the-docs.com/docs/navigation-structure/)

### Support
- [Jekyll Community](https://talk.jekyllrb.com/)
- [Just the Docs GitHub](https://github.com/just-the-docs/just-the-docs)

---

**Questions?** Check JEKYLL_PREP.md for detailed technical documentation.

**Created:** October 22, 2025  
**Status:** Ready for Deployment ✅
