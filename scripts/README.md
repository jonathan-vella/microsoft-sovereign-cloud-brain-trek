# Project Automation Scripts# Project Automation Scripts# Project Automation Scripts



This folder previously contained PowerShell scripts for repository maintenance.



> **All automation has been migrated to GitHub Actions workflows.**  This folder previously contained PowerShell scripts for repository maintenance.This folder previously contained PowerShell scripts for repository maintenance.

> See [AUTOMATION.md](../AUTOMATION.md) for monthly maintenance procedures.



---

> **All automation has been migrated to GitHub Actions workflows.**> **Note:** All automation has been migrated to GitHub Actions workflows in `.github/workflows/`.

## Active Automation

> See [AUTOMATION.md](../AUTOMATION.md) for monthly maintenance procedures.> See [AUTOMATION.md](../AUTOMATION.md) for monthly maintenance procedures.

All automation now runs via GitHub Actions in `.github/workflows/`:



- **Link Validation** → `.github/workflows/link-check.yml`

  - Validates all internal and external links---## GitHub Actions Workflows

  - Manual trigger only

  - Creates issue if broken links found



- **Content Freshness Check** → `.github/workflows/content-freshness.yml`## Active AutomationActive automation (replaces local scripts):

  - Identifies stale content (180+ days old)

  - Manual trigger only- **Link Validation** → `.github/workflows/link-check.yml` (manual trigger)

  - Reports content needing updates

All automation now runs via GitHub Actions in `.github/workflows/`:- **Content Freshness** → `.github/workflows/content-freshness.yml` (manual trigger)

- **Microsoft Learn Link Monitor** → `.github/workflows/ms-learn-monitor.yml`

  - Checks Microsoft Learn URLs for changes- **Microsoft Learn Monitoring** → `.github/workflows/ms-learn-monitor.yml` (manual trigger)

  - Manual trigger only

  - Alerts on deprecated/moved content- **Link Validation** → `.github/workflows/link-check.yml`



---  - Validates all internal and external links## Previously Available Scripts



## Running Automation  - Manual trigger only



Trigger workflows from GitHub Actions tab:  - Creates issue if broken links found### Add-Contributor.ps1 (Removed - October 2025)



1. Go to **Actions** tab in repository

2. Select desired workflow

3. Click **Run workflow**- **Content Freshness Check** → `.github/workflows/content-freshness.yml`**Reason for removal:** Manual contributor management preferred; script unused.

4. View results and any created issues

  - Identifies stale content (180+ days old)

---

  - Manual trigger only**To add contributors now:**

## Local Development

  - Reports content needing updates

For local validation before committing:

- ✅ Updates CODEOWNERS with review permissions for documentation paths

```bash

# Install markdownlint- **Microsoft Learn Link Monitor** → `.github/workflows/ms-learn-monitor.yml`- ✅ Adds contributor to CONTRIBUTING.md Contributors section

npm install -g markdownlint-cli

  - Checks Microsoft Learn URLs for changes- ✅ Creates automatic backups before making changes

# Check markdown syntax

markdownlint docs/**/*.md  - Manual trigger only- ✅ Validates file existence and changes before applying



# Preview Jekyll site locally (requires Ruby + Jekyll)  - Alerts on deprecated/moved content- ✅ Provides clear summary and next steps

bundle exec jekyll serve

```- ✅ Supports optional permissions for assets and workflows



------



## Adding Contributors#### Basic Usage



To add contributors to the project:## Running Automation



1. **Update `.github/CODEOWNERS`**```powershell



   ```plaintextTrigger workflows from GitHub Actions tab:# Add a standard documentation contributor

   /docs/ @jonathan-vella @new-contributor

   ```.\scripts\Add-Contributor.ps1 -GitHubUsername "sohamda" -FullName "Soham Da"



2. **Update `CONTRIBUTING.md`**1. Go to **Actions** tab in repository```



   ```markdown2. Select desired workflow

   - [Contributor Name](https://github.com/username) - Role

   ```3. Click **Run workflow**#### Advanced Usage



3. **Commit changes**4. View results and any created issues



   ```bash```powershell

   git add .github/CODEOWNERS CONTRIBUTING.md

   git commit -m "Add [name] as contributor"---# Add contributor with custom role

   ```

.\scripts\Add-Contributor.ps1 `

---

## Local Development    -GitHubUsername "johndoe" `

## Migration History

    -FullName "John Doe" `

**October 2025:**

- Removed `Check-BrokenLinks.ps1` (superseded by `link-check.yml` workflow)For local validation before committing:    -Role "Technical Reviewer"

- Removed `Fix-ReadmeLinks.ps1` (one-time fix completed)

- All functionality preserved in GitHub Actions workflows



---```bash# Add contributor with asset review permissions



**Last Updated:** October 23, 2025# Install markdownlint.\scripts\Add-Contributor.ps1 `


npm install -g markdownlint-cli    -GitHubUsername "janedoe" `

    -FullName "Jane Doe" `

# Check markdown syntax    -Role "Visual Designer" `

markdownlint docs/**/*.md    -IncludeAssets



# Preview Jekyll site locally (requires Ruby + Jekyll)# Add contributor with workflow review permissions

bundle exec jekyll serve.\scripts\Add-Contributor.ps1 `

```    -GitHubUsername "alexsmith" `

    -FullName "Alex Smith" `

---    -Role "DevOps Engineer" `

    -IncludeWorkflows

## Adding Contributors```



To add contributors to the project:#### Parameters



1. **Update `.github/CODEOWNERS`:**| Parameter | Required | Default | Description |

   ```|-----------|----------|---------|-------------|

   /docs/ @jonathan-vella @new-contributor| `GitHubUsername` | Yes | - | GitHub username (without @) |

   ```| `FullName` | Yes | - | Full name for display in CONTRIBUTING.md |

| `Role` | No | "Content Contributor (Documentation)" | Role description |

2. **Update `CONTRIBUTING.md`:**| `IncludeAssets` | No | False | Grant review permissions for /docs/assets/ |

   ```markdown| `IncludeWorkflows` | No | False | Grant review permissions for /.github/workflows/ |

   - [Contributor Name](https://github.com/username) - Role

   ```#### What Gets Updated



3. **Commit changes:****CODEOWNERS File:**

   ```bash- `/docs/` - Documentation content

   git add .github/CODEOWNERS CONTRIBUTING.md- `/docs/level-100/` - Level 100 content

   git commit -m "Add [name] as contributor"- `/docs/level-200/` - Level 200 content

   ```- `/docs/level-300/` - Level 300 content

- `/docs/resources/` - Resources folder

---- `/CHANGELOG.md` - Changelog file

- `/docs/README.md` - Documentation README

## Migration History- `/docs/assets/` - Visual assets (if `-IncludeAssets` specified)

- `/.github/workflows/` - GitHub Actions (if `-IncludeWorkflows` specified)

**October 2025:**

- Removed `Check-BrokenLinks.ps1` (superseded by `link-check.yml` workflow)**CONTRIBUTING.md File:**

- Removed `Fix-ReadmeLinks.ps1` (one-time fix completed)- Adds entry to Contributors section with name, GitHub link, and role

- All functionality preserved in GitHub Actions workflows

#### Backups

---

The script automatically creates timestamped backups before making changes:

**Last Updated:** October 23, 2025

```
.github/CODEOWNERS.backup.20251022_143015
CONTRIBUTING.md.backup.20251022_143015
```

To restore from backup:

```powershell
Copy-Item '.github/CODEOWNERS.backup.20251022_143015' -Destination '.github/CODEOWNERS' -Force
Copy-Item 'CONTRIBUTING.md.backup.20251022_143015' -Destination 'CONTRIBUTING.md' -Force
```

#### Example Output

```
================================
Add Contributor to Project
================================

GitHub Username: @sohamda
Full Name: Soham Da
Role: Content Contributor (Documentation)
Include Assets: False
Include Workflows: False

Creating backups...
✓ Created backup: .github/CODEOWNERS.backup.20251022_143015
✓ Created backup: CONTRIBUTING.md.backup.20251022_143015

Updating CODEOWNERS...
  ✓ Added to: Documentation content
  ✓ Added to: Level 100 content
  ✓ Added to: Level 200 content
  ✓ Added to: Level 300 content
  ✓ Added to: Resources folder
  ✓ Added to: Changelog
  ✓ Added to: Docs README

✓ CODEOWNERS updated with 7 change(s)

Updating CONTRIBUTING.md...
✓ Added to Contributors section

================================
Summary
================================
✓ Successfully added contributor: Soham Da (@sohamda)

Files updated:
  • .github/CODEOWNERS
  • CONTRIBUTING.md

Next steps:
  1. Review the changes in both files
  2. Commit and push the changes:
     git add .github/CODEOWNERS CONTRIBUTING.md
     git commit -m "Add Soham Da as contributor"
     git push

  3. Notify @sohamda that they've been added

Backups created:
  • .github/CODEOWNERS.backup.20251022_143015
  • CONTRIBUTING.md.backup.20251022_143015
```

#### Error Handling

The script includes comprehensive error handling:

- Validates file existence before making changes
- Checks if contributor already exists (prevents duplicates)
- Creates backups before any modifications
- Provides restore instructions if errors occur
- Uses strict mode and stops on errors

#### Requirements

- PowerShell 5.1 or later
- Write permissions to repository files
- Repository cloned locally

## Future Scripts

Planned automation scripts for this repository:

- `Update-MSLearnLinks.ps1` - Batch update Microsoft Learn URLs
- `Generate-ChangelogEntry.ps1` - Create formatted changelog entries
- `Validate-ContentFreshness.ps1` - Check for outdated content
- `Export-LearningPath.ps1` - Generate learning path reports

## Contributing

To add new automation scripts:

1. Create script in `/scripts/` folder
2. Include comprehensive comment-based help
3. Add entry to this README.md
4. Test thoroughly before committing
5. Follow PowerShell best practices:
   - Use approved verbs (Get, Set, New, etc.)
   - Include parameter validation
   - Add error handling
   - Create backups when modifying files
   - Provide clear output and summaries

## Support

If you encounter issues with any script:

1. Check script help: `Get-Help .\scripts\ScriptName.ps1 -Full`
2. Review backups in repository root
3. Open an issue with error details
4. Contact repository maintainers

---

**Last Updated:** October 22, 2025
