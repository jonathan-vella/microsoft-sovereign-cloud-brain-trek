# Automated Content Updates - Monthly Maintenance Guide

**Purpose:** Keep Microsoft Sovereign Cloud Brain Trek content fresh with automated monthly updates  
**Target:** Link validation, dependency updates, and content freshness checks  
**Created:** October 21, 2025

---

## 🤖 Automation Strategy

### What to Automate (Monthly)

1. **Link Validation** - Check all Microsoft Learn links for changes/redirects
2. **Dependency Updates** - Update Jekyll gems, plugins, themes
3. **Content Freshness Alerts** - Flag outdated references (> 6 months old)
4. **Visual Asset Updates** - Track when diagrams need refresh
5. **Microsoft Docs Changes** - Monitor referenced documentation for updates

### What NOT to Automate

- ❌ Content rewrites (requires human SME review)
- ❌ New module creation (requires strategic planning)
- ❌ Visual asset redesigns (requires designer)
- ❌ Quiz question updates (requires validation)

---

## 📋 Option 1: GitHub Actions (Recommended)

### Advantages
- Native GitHub integration
- Free for public repos
- Runs on schedule automatically
- Can create issues/PRs automatically

### Setup Steps

**1. Create `.github/workflows/monthly-maintenance.yml`:**

```yaml
name: Monthly Content Maintenance

on:
  schedule:
    # Runs 1st of every month at 9 AM UTC
    - cron: '0 9 1 * *'
  workflow_dispatch: # Manual trigger option

jobs:
  link-validation:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Check all links
        uses: lycheeverse/lychee-action@v1
        with:
          args: --verbose --no-progress 'docs/**/*.md' 'README.md' 'CONTRIBUTING.md'
          fail: false # Don't fail build, just report
          
      - name: Create issue if links broken
        if: env.lychee_exit_code != 0
        uses: actions/github-script@v7
        with:
          script: |
            github.rest.issues.create({
              owner: context.repo.owner,
              repo: context.repo.repo,
              title: '🔗 Broken Links Detected - Monthly Check',
              body: 'Automated link validation found broken links. See workflow run for details.',
              labels: ['maintenance', 'broken-links']
            })

  dependency-updates:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.1'
          bundler-cache: true

      - name: Check for outdated gems
        run: |
          bundle outdated > outdated-gems.txt || true
          
      - name: Create PR for gem updates
        if: hashFiles('outdated-gems.txt') != ''
        uses: peter-evans/create-pull-request@v5
        with:
          commit-message: 'chore: update Jekyll dependencies (monthly)'
          title: '📦 Monthly Dependency Updates'
          body: |
            Automated monthly dependency check found updates available.
            
            Review changes and test locally before merging:
            ```bash
            bundle update
            bundle exec jekyll serve
            ```
          branch: monthly-deps-update
          labels: maintenance, dependencies

  content-freshness-check:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Check for outdated content
        run: |
          # Find files not modified in 6+ months
          find docs -name "*.md" -type f -mtime +180 > stale-content.txt || true
          
      - name: Create issue for stale content
        if: hashFiles('stale-content.txt') != ''
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const staleFiles = fs.readFileSync('stale-content.txt', 'utf8');
            github.rest.issues.create({
              owner: context.repo.owner,
              repo: context.repo.repo,
              title: '📅 Content Freshness Review Needed',
              body: `The following files haven't been updated in 6+ months:\n\n\`\`\`\n${staleFiles}\n\`\`\`\n\nReview for accuracy and update if needed.`,
              labels: ['maintenance', 'content-review']
            })
```

**2. Enable GitHub Actions in Repository Settings:**
- Go to Settings → Actions → General
- Enable "Allow all actions and reusable workflows"
- Set workflow permissions to "Read and write permissions"

**3. Test Manually:**
```bash
# Go to Actions tab → Monthly Content Maintenance → Run workflow
```

---

## 📋 Option 2: Dependabot (Dependency Updates Only)

### Advantages
- Built into GitHub
- Automatic PR creation
- Security vulnerability detection
- Zero configuration for basic use

### Setup Steps

**1. Create `.github/dependabot.yml`:**

```yaml
version: 2
updates:
  # Jekyll gem dependencies
  - package-ecosystem: "bundler"
    directory: "/"
    schedule:
      interval: "monthly"
      day: "monday"
      time: "09:00"
    open-pull-requests-limit: 5
    labels:
      - "dependencies"
      - "maintenance"
    commit-message:
      prefix: "chore"
      include: "scope"

  # GitHub Actions workflows
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "monthly"
    labels:
      - "dependencies"
      - "github-actions"
```

**2. Merge Automatically (Optional):**

Enable auto-merge for Dependabot PRs after tests pass:
```yaml
# Add to .github/workflows/auto-merge-dependabot.yml
name: Auto-merge Dependabot PRs
on: pull_request

jobs:
  auto-merge:
    runs-on: ubuntu-latest
    if: github.actor == 'dependabot[bot]'
    steps:
      - name: Enable auto-merge
        run: gh pr merge --auto --squash "$PR_URL"
        env:
          PR_URL: ${{github.event.pull_request.html_url}}
          GITHUB_TOKEN: ${{secrets.GITHUB_TOKEN}}
```

---

## 📋 Option 3: Microsoft Learn Content Monitoring

### Track Microsoft Learn Changes

**Problem:** Microsoft Learn documentation changes frequently, breaking your references.

**Solution:** Monitor specific Microsoft Learn pages for changes.

**Setup with GitHub Actions:**

```yaml
# .github/workflows/monitor-ms-learn.yml
name: Monitor Microsoft Learn Changes

on:
  schedule:
    - cron: '0 10 1 * *' # 1st of month, 10 AM UTC
  workflow_dispatch:

jobs:
  check-ms-learn-links:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Extract Microsoft Learn URLs
        run: |
          grep -roh 'https://learn.microsoft.com[^)]*' docs/ | sort -u > ms-learn-urls.txt

      - name: Check each URL
        run: |
          while read url; do
            status=$(curl -o /dev/null -s -w "%{http_code}" "$url")
            if [ "$status" != "200" ]; then
              echo "BROKEN: $url (Status: $status)" >> broken-links.txt
            fi
          done < ms-learn-urls.txt

      - name: Create issue if broken links
        if: hashFiles('broken-links.txt') != ''
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const brokenLinks = fs.readFileSync('broken-links.txt', 'utf8');
            github.rest.issues.create({
              owner: context.repo.owner,
              repo: context.repo.repo,
              title: '🔗 Microsoft Learn Links Need Update',
              body: `Monthly check found broken Microsoft Learn links:\n\n\`\`\`\n${brokenLinks}\n\`\`\`\n\nPlease update content with current links.`,
              labels: ['maintenance', 'microsoft-learn', 'broken-links']
            })
```

---

## 📋 Option 4: Content Update Reminders

### Human-in-Loop Approach

**Create Monthly Issue Reminders:**

```yaml
# .github/workflows/monthly-reminder.yml
name: Monthly Content Review Reminder

on:
  schedule:
    - cron: '0 9 1 * *' # 1st of every month

jobs:
  create-reminder:
    runs-on: ubuntu-latest
    steps:
      - name: Create monthly review issue
        uses: actions/github-script@v7
        with:
          script: |
            const date = new Date();
            const month = date.toLocaleString('default', { month: 'long' });
            const year = date.getFullYear();
            
            github.rest.issues.create({
              owner: context.repo.owner,
              repo: context.repo.repo,
              title: `📅 Monthly Content Review - ${month} ${year}`,
              body: `## Monthly Maintenance Checklist\n\n### Content Updates\n- [ ] Review Level 100 modules for outdated info\n- [ ] Review Level 200 modules for outdated info\n- [ ] Review Level 300 modules for outdated info\n- [ ] Check all Microsoft Learn links\n- [ ] Verify Azure service names (rebranding?)\n- [ ] Update quiz questions if needed\n\n### Technical Updates\n- [ ] Update Jekyll dependencies\n- [ ] Check for security vulnerabilities\n- [ ] Test local build\n- [ ] Verify GitHub Pages deployment\n\n### Visual Assets\n- [ ] Check if any diagrams need refresh\n- [ ] Verify all SVG files loading correctly\n\n### Documentation\n- [ ] Update CHANGELOG.md with any changes\n- [ ] Review README.md for accuracy\n- [ ] Check all cross-references working\n\n**Assign to:** Content owner\n**Due:** End of month`,
              labels: ['maintenance', 'monthly-review'],
              assignees: ['${context.repo.owner}']
            })
```

---

## 🔧 Recommended Automation Stack

### Minimal Setup (15 minutes)
1. ✅ **Dependabot** - Auto dependency updates
2. ✅ **Link Checker** - Monthly broken link detection
3. ✅ **Monthly Reminder Issue** - Human review checklist

### Full Setup (1-2 hours)
1. ✅ All minimal setup items
2. ✅ **Content Freshness Check** - Flag stale content
3. ✅ **MS Learn Monitor** - Track Microsoft doc changes
4. ✅ **Auto-merge Dependabot** - Automatic safe updates
5. ✅ **Build Test on PR** - Prevent broken deployments

---

## 📊 Monitoring Dashboard

### Track Automation Health

**Add badges to README.md:**

```markdown
[![Monthly Maintenance](https://github.com/jonathan-vella/microsoft-sovereign-cloud-brain-trek/actions/workflows/monthly-maintenance.yml/badge.svg)](https://github.com/jonathan-vella/microsoft-sovereign-cloud-brain-trek/actions/workflows/monthly-maintenance.yml)
[![Link Check](https://github.com/jonathan-vella/microsoft-sovereign-cloud-brain-trek/actions/workflows/link-check.yml/badge.svg)](https://github.com/jonathan-vella/microsoft-sovereign-cloud-brain-trek/actions/workflows/link-check.yml)
```

### Review Actions History

1. Go to **Actions** tab in GitHub
2. See all workflow runs
3. Click any run to see details
4. Review logs for failures

---

## 🔄 Manual Monthly Review Process

### Even with automation, perform manual checks:

**Monthly Checklist (30 minutes):**

1. **Review Automation Results**
   - Check GitHub Issues created by workflows
   - Review Dependabot PRs
   - Address broken links

2. **Content Spot Check**
   - Open 3-5 random pages
   - Verify screenshots/diagrams accurate
   - Check for outdated Azure service names
   - Verify Microsoft Learn links work

3. **Technology Changes**
   - Check Microsoft Tech Community for major announcements
   - Review Azure updates blog
   - Check for service rebranding

4. **Analytics (if enabled)**
   - Which pages most visited?
   - Which pages have high bounce rate?
   - Update popular content first

---

## 🚀 Quick Start: Enable Basic Automation Now

**5-Minute Setup:**

1. **Create `.github/workflows/` folder:**
   ```bash
   mkdir -p .github/workflows
   ```

2. **Add link checker workflow:**
   - Copy `monthly-maintenance.yml` from above
   - Commit and push

3. **Enable Dependabot:**
   - Copy `dependabot.yml` from above
   - Commit and push

4. **Test manually:**
   - Go to Actions → Run workflow
   - Verify it works

5. **Review first results:**
   - Check created issues
   - Address any broken links

---

## 📚 Additional Tools

### Link Validation
- [Lychee](https://github.com/lycheeverse/lychee) - Fast link checker
- [markdown-link-check](https://github.com/tcort/markdown-link-check) - Alternative

### Dependency Management
- [Dependabot](https://github.com/dependabot) - Built into GitHub
- [Renovate](https://github.com/renovatebot/renovate) - More powerful alternative

### Content Monitoring
- [ChangeDetection.io](https://changedetection.io/) - Monitor external pages
- [Visualping](https://visualping.io/) - Visual change detection

### Jekyll Specific
- [jekyll-last-modified-at](https://github.com/gjtorikian/jekyll-last-modified-at) - Auto-update dates
- [jekyll-sitemap](https://github.com/jekyll/jekyll-sitemap) - Auto-generate sitemap

---

## 📝 Best Practices

### DO:
✅ Start with minimal automation (Dependabot + Link checker)  
✅ Test workflows manually before scheduling  
✅ Review automated PRs before merging  
✅ Keep humans in the loop for content changes  
✅ Document what each workflow does  
✅ Set realistic schedules (monthly is good)  

### DON'T:
❌ Auto-merge content changes without review  
❌ Run heavy workflows too frequently (GitHub rate limits)  
❌ Ignore automation failures  
❌ Over-automate (humans add value)  
❌ Skip testing after dependency updates  

---

## 🔒 Security Considerations

### Workflow Permissions

- Use least-privilege access
- Review third-party actions before using
- Pin action versions (e.g., `@v4` not `@main`)
- Never commit secrets to workflows

### Safe Automation

```yaml
# Good: Specific permissions
permissions:
  contents: read
  issues: write
  pull-requests: write

# Bad: Too broad
permissions: write-all
```

---

## 📅 Suggested Schedule

| Task | Frequency | Automation |
|------|-----------|------------|
| Link validation | Monthly | GitHub Actions |
| Dependency updates | Monthly | Dependabot |
| Content freshness check | Monthly | GitHub Actions |
| Manual content review | Quarterly | Human |
| Visual asset refresh | Annually | Human |
| Major content updates | As needed | Human |

---

## 🎯 Success Metrics

Track these to measure automation effectiveness:

- **Broken links detected/fixed** per month
- **Dependency update lag** (days from release to merge)
- **Stale content count** (files > 6 months old)
- **Automation failure rate** (workflow runs failed)
- **Time saved** (manual work → automated)

---

## 🔗 Next Steps

1. **This week:** Set up Dependabot and link checker
2. **Next month:** Add content freshness checks
3. **Quarter 1 2026:** Add MS Learn monitoring
4. **Quarter 2 2026:** Implement auto-merge for safe updates

---

**Created:** October 21, 2025  
**For:** Microsoft Sovereign Cloud Brain Trek  
**Maintained By:** Repository owner  
**Questions?** Open an issue with label `automation`
