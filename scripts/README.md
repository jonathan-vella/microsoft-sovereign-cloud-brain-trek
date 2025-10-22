# Project Automation Scripts

This folder contains PowerShell scripts to automate common repository maintenance tasks.

## Available Scripts

### Add-Contributor.ps1

Automates adding new contributors to the project by updating both the CODEOWNERS file and CONTRIBUTING.md file.

#### Features

- ✅ Updates CODEOWNERS with review permissions for documentation paths
- ✅ Adds contributor to CONTRIBUTING.md Contributors section
- ✅ Creates automatic backups before making changes
- ✅ Validates file existence and changes before applying
- ✅ Provides clear summary and next steps
- ✅ Supports optional permissions for assets and workflows

#### Basic Usage

```powershell
# Add a standard documentation contributor
.\scripts\Add-Contributor.ps1 -GitHubUsername "sohamda" -FullName "Soham Da"
```

#### Advanced Usage

```powershell
# Add contributor with custom role
.\scripts\Add-Contributor.ps1 `
    -GitHubUsername "johndoe" `
    -FullName "John Doe" `
    -Role "Technical Reviewer"

# Add contributor with asset review permissions
.\scripts\Add-Contributor.ps1 `
    -GitHubUsername "janedoe" `
    -FullName "Jane Doe" `
    -Role "Visual Designer" `
    -IncludeAssets

# Add contributor with workflow review permissions
.\scripts\Add-Contributor.ps1 `
    -GitHubUsername "alexsmith" `
    -FullName "Alex Smith" `
    -Role "DevOps Engineer" `
    -IncludeWorkflows
```

#### Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `GitHubUsername` | Yes | - | GitHub username (without @) |
| `FullName` | Yes | - | Full name for display in CONTRIBUTING.md |
| `Role` | No | "Content Contributor (Documentation)" | Role description |
| `IncludeAssets` | No | False | Grant review permissions for /docs/assets/ |
| `IncludeWorkflows` | No | False | Grant review permissions for /.github/workflows/ |

#### What Gets Updated

**CODEOWNERS File:**
- `/docs/` - Documentation content
- `/docs/level-100/` - Level 100 content
- `/docs/level-200/` - Level 200 content
- `/docs/level-300/` - Level 300 content
- `/docs/resources/` - Resources folder
- `/CHANGELOG.md` - Changelog file
- `/docs/README.md` - Documentation README
- `/docs/assets/` - Visual assets (if `-IncludeAssets` specified)
- `/.github/workflows/` - GitHub Actions (if `-IncludeWorkflows` specified)

**CONTRIBUTING.md File:**
- Adds entry to Contributors section with name, GitHub link, and role

#### Backups

The script automatically creates timestamped backups before making changes:

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
