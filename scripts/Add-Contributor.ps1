<#
.SYNOPSIS
    Adds a new contributor to the Microsoft Sovereign Cloud Brain Trek project.

.DESCRIPTION
    This script automates the process of adding a new contributor to both the
    CODEOWNERS file and CONTRIBUTING.md file. It updates all relevant sections
    to ensure the contributor is properly recognized and assigned review duties.

.PARAMETER GitHubUsername
    The GitHub username of the contributor (without the @ symbol).

.PARAMETER FullName
    The full name of the contributor for display in CONTRIBUTING.md.

.PARAMETER Role
    The role/contribution type of the contributor (default: "Content Contributor (Documentation)").

.PARAMETER IncludeAssets
    Switch to indicate if the contributor should also review visual assets.

.PARAMETER IncludeWorkflows
    Switch to indicate if the contributor should also review GitHub Actions workflows.

.EXAMPLE
    .\Add-Contributor.ps1 -GitHubUsername "sohamda" -FullName "Soham Da"
    
    Adds sohamda as a documentation contributor with standard permissions.

.EXAMPLE
    .\Add-Contributor.ps1 -GitHubUsername "johndoe" -FullName "John Doe" -Role "Technical Reviewer" -IncludeAssets
    
    Adds johndoe as a technical reviewer with asset review permissions.

.NOTES
    Author: Jonathan Vella
    Date: October 22, 2025
    Version: 1.0
#>

[CmdletBinding(SupportsShouldProcess)]
param(
    [Parameter(Mandatory = $true, HelpMessage = "GitHub username (without @)")]
    [ValidateNotNullOrEmpty()]
    [string]$GitHubUsername,

    [Parameter(Mandatory = $true, HelpMessage = "Full name for display")]
    [ValidateNotNullOrEmpty()]
    [string]$FullName,

    [Parameter(Mandatory = $false)]
    [string]$Role = "Content Contributor (Documentation)",

    [Parameter(Mandatory = $false)]
    [switch]$IncludeAssets = $false,

    [Parameter(Mandatory = $false)]
    [switch]$IncludeWorkflows = $false
)

# Set strict mode for better error handling
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# Get the repository root directory (script is in /scripts folder)
$RepoRoot = Split-Path -Parent $PSScriptRoot
$CodeOwnersPath = Join-Path $RepoRoot ".github\CODEOWNERS"
$ContributingPath = Join-Path $RepoRoot "CONTRIBUTING.md"

# Ensure @ prefix for GitHub username
$GitHubHandle = if ($GitHubUsername.StartsWith("@")) { $GitHubUsername } else { "@$GitHubUsername" }

Write-Host "================================" -ForegroundColor Cyan
Write-Host "Add Contributor to Project" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "GitHub Username: $GitHubHandle" -ForegroundColor Yellow
Write-Host "Full Name: $FullName" -ForegroundColor Yellow
Write-Host "Role: $Role" -ForegroundColor Yellow
Write-Host "Include Assets: $IncludeAssets" -ForegroundColor Yellow
Write-Host "Include Workflows: $IncludeWorkflows" -ForegroundColor Yellow
Write-Host ""

# Verify files exist
if (-not (Test-Path $CodeOwnersPath)) {
    throw "CODEOWNERS file not found at: $CodeOwnersPath"
}
if (-not (Test-Path $ContributingPath)) {
    throw "CONTRIBUTING.md file not found at: $ContributingPath"
}

# Function to backup files
function Backup-File {
    param([string]$FilePath)
    
    $BackupPath = "$FilePath.backup.$(Get-Date -Format 'yyyyMMdd_HHmmss')"
    Copy-Item -Path $FilePath -Destination $BackupPath -Force
    Write-Host "✓ Created backup: $BackupPath" -ForegroundColor Green
    return $BackupPath
}

# Function to update CODEOWNERS
function Update-CodeOwners {
    param([string]$FilePath, [string]$Handle)
    
    Write-Host ""
    Write-Host "Updating CODEOWNERS..." -ForegroundColor Cyan
    
    $Content = Get-Content -Path $FilePath -Raw
    
    # Define patterns to update
    $Patterns = @(
        @{ Pattern = '(/docs/) (@[\w-]+ )*'; Scope = "Documentation content" }
        @{ Pattern = '(/docs/level-100/) (@[\w-]+ )*'; Scope = "Level 100 content" }
        @{ Pattern = '(/docs/level-200/) (@[\w-]+ )*'; Scope = "Level 200 content" }
        @{ Pattern = '(/docs/level-300/) (@[\w-]+ )*'; Scope = "Level 300 content" }
        @{ Pattern = '(/docs/resources/) (@[\w-]+ )*'; Scope = "Resources folder" }
        @{ Pattern = '(/CHANGELOG\.md) (@[\w-]+ )*'; Scope = "Changelog" }
        @{ Pattern = '(/docs/README\.md) (@[\w-]+ )*'; Scope = "Docs README" }
    )
    
    # Add assets pattern if requested
    if ($IncludeAssets) {
        $Patterns += @{ Pattern = '(/docs/assets/) (@[\w-]+ )*'; Scope = "Visual assets" }
    }
    
    # Add workflows pattern if requested
    if ($IncludeWorkflows) {
        $Patterns += @{ Pattern = '(/\.github/workflows/) (@[\w-]+ )*'; Scope = "GitHub workflows" }
    }
    
    $UpdateCount = 0
    foreach ($Item in $Patterns) {
        $Pattern = $Item.Pattern
        $Scope = $Item.Scope
        
        if ($Content -match $Pattern) {
            $Match = $Matches[0]
            
            # Check if user already exists in this line
            if ($Match -notlike "*$Handle*") {
                $NewMatch = $Match.TrimEnd() + " $Handle"
                $Content = $Content -replace [regex]::Escape($Match), $NewMatch
                Write-Host "  ✓ Added to: $Scope" -ForegroundColor Green
                $UpdateCount++
            } else {
                Write-Host "  ⊘ Already present in: $Scope" -ForegroundColor DarkGray
            }
        }
    }
    
    if ($UpdateCount -gt 0) {
        Set-Content -Path $FilePath -Value $Content -NoNewline
        Write-Host ""
        Write-Host "✓ CODEOWNERS updated with $UpdateCount change(s)" -ForegroundColor Green
        return $true
    } else {
        Write-Host ""
        Write-Host "⊘ No changes needed in CODEOWNERS (user already present)" -ForegroundColor Yellow
        return $false
    }
}

# Function to update CONTRIBUTING.md
function Update-Contributing {
    param([string]$FilePath, [string]$Handle, [string]$Name, [string]$ContribRole)
    
    Write-Host ""
    Write-Host "Updating CONTRIBUTING.md..." -ForegroundColor Cyan
    
    $Content = Get-Content -Path $FilePath -Raw
    
    # Check if user already exists
    if ($Content -match [regex]::Escape("[$Handle]")) {
        Write-Host "⊘ User already exists in Contributors section" -ForegroundColor Yellow
        return $false
    }
    
    # Find the Contributors section and add the new entry
    $ContributorEntry = "- **[$Handle](https://github.com/$($Handle.TrimStart('@')))** - $ContribRole"
    
    # Pattern to find the end of contributors list (before "## License" section)
    $Pattern = '(- \*\*\[@[\w-]+\]\([^\)]+\)\*\* - [^\r\n]+)'
    
    if ($Content -match $Pattern) {
        # Find the last contributor entry
        $AllMatches = [regex]::Matches($Content, $Pattern)
        $LastMatch = $AllMatches[$AllMatches.Count - 1]
        
        # Insert after the last contributor
        $InsertPosition = $LastMatch.Index + $LastMatch.Length
        $Content = $Content.Insert($InsertPosition, "`r`n$ContributorEntry")
        
        Set-Content -Path $FilePath -Value $Content -NoNewline
        Write-Host "✓ Added to Contributors section" -ForegroundColor Green
        return $true
    } else {
        Write-Host "⚠ Could not find Contributors section pattern" -ForegroundColor Red
        Write-Host "  Please manually add: $ContributorEntry" -ForegroundColor Yellow
        return $false
    }
}

# Main execution
try {
    # Create backups
    Write-Host "Creating backups..." -ForegroundColor Cyan
    $CodeOwnersBackup = Backup-File -FilePath $CodeOwnersPath
    $ContributingBackup = Backup-File -FilePath $ContributingPath
    
    # Update files
    $CodeOwnersChanged = Update-CodeOwners -FilePath $CodeOwnersPath -Handle $GitHubHandle
    $ContributingChanged = Update-Contributing -FilePath $ContributingPath -Handle $GitHubHandle -Name $FullName -ContribRole $Role
    
    # Summary
    Write-Host ""
    Write-Host "================================" -ForegroundColor Cyan
    Write-Host "Summary" -ForegroundColor Cyan
    Write-Host "================================" -ForegroundColor Cyan
    
    if ($CodeOwnersChanged -or $ContributingChanged) {
        Write-Host "✓ Successfully added contributor: $FullName ($GitHubHandle)" -ForegroundColor Green
        Write-Host ""
        Write-Host "Files updated:" -ForegroundColor Yellow
        if ($CodeOwnersChanged) { Write-Host "  • .github/CODEOWNERS" }
        if ($ContributingChanged) { Write-Host "  • CONTRIBUTING.md" }
        
        Write-Host ""
        Write-Host "Next steps:" -ForegroundColor Yellow
        Write-Host "  1. Review the changes in both files" -ForegroundColor White
        Write-Host "  2. Commit and push the changes:" -ForegroundColor White
        Write-Host "     git add .github/CODEOWNERS CONTRIBUTING.md" -ForegroundColor DarkGray
        Write-Host "     git commit -m `"Add $FullName as contributor`"" -ForegroundColor DarkGray
        Write-Host "     git push" -ForegroundColor DarkGray
        Write-Host ""
        Write-Host "  3. Notify $GitHubHandle that they've been added" -ForegroundColor White
        Write-Host ""
        Write-Host "Backups created:" -ForegroundColor DarkGray
        Write-Host "  • $CodeOwnersBackup" -ForegroundColor DarkGray
        Write-Host "  • $ContributingBackup" -ForegroundColor DarkGray
    } else {
        Write-Host "⊘ No changes made (contributor may already exist)" -ForegroundColor Yellow
    }
    
} catch {
    Write-Host ""
    Write-Host "✗ Error occurred: $_" -ForegroundColor Red
    Write-Host ""
    Write-Host "Backups are available at:" -ForegroundColor Yellow
    Write-Host "  • $CodeOwnersBackup" -ForegroundColor DarkGray
    Write-Host "  • $ContributingBackup" -ForegroundColor DarkGray
    Write-Host ""
    Write-Host "To restore from backup:" -ForegroundColor Yellow
    Write-Host "  Copy-Item '$CodeOwnersBackup' -Destination '$CodeOwnersPath' -Force" -ForegroundColor DarkGray
    Write-Host "  Copy-Item '$ContributingBackup' -Destination '$ContributingPath' -Force" -ForegroundColor DarkGray
    exit 1
}
