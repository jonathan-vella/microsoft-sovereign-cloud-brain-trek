#Requires -Version 7.0

<#
.SYNOPSIS
    Fixes relative links in README.md files to use absolute paths.

.DESCRIPTION
    README.md files with absolute paths like /level-100/file break when there's
    a baseurl in Jekyll (they go to domain root instead of /baseurl/level-100/file).
    
    This script converts absolute paths to relative paths within README files.
    Changes: [text](/level-100/file) -> [text](file)

.EXAMPLE
    .\Fix-ReadmeLinks.ps1 -DryRun
    
.EXAMPLE
    .\Fix-ReadmeLinks.ps1
#>

[CmdletBinding()]
param(
    [Parameter()]
    [string]$DocsPath = (Join-Path $PSScriptRoot "..\docs"),
    
    [Parameter()]
    [switch]$DryRun
)

$script:TotalReadmeFiles = 0
$script:FilesModified = 0
$script:LinksFixed = 0

function Fix-ReadmeLinks {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$FilePath
    )
    
    $script:TotalReadmeFiles++
    $relativePath = Resolve-Path -Relative $FilePath
    $fileDir = Split-Path -Parent $FilePath
    $levelFolder = Split-Path -Leaf $fileDir
    
    Write-Verbose "Processing: $relativePath (folder: $levelFolder)"
    
    $content = Get-Content $FilePath -Raw
    $originalContent = $content
    $fileChanges = 0
    
    # Pattern: [text](/level-XXX/file) - absolute paths that need to be relative
    # These need to become relative: digital-sovereignty (no path prefix)
    $pattern = '\]\(/' + [regex]::Escape($levelFolder) + '/([a-z0-9\-]+)\)'
    $linkMatches = [regex]::Matches($content, $pattern)
    
    if ($linkMatches.Count -gt 0) {
        Write-Verbose "  Found $($linkMatches.Count) absolute links to fix"
        
        foreach ($match in $linkMatches) {
            $fullMatch = $match.Value
            $fileName = $match.Groups[1].Value
            
            # Convert to relative path (just the filename)
            $newLink = "]($fileName)"
            
            $content = $content.Replace($fullMatch, $newLink)
            $fileChanges++
            $script:LinksFixed++
            
            Write-Verbose "    Fixed: $fullMatch -> $newLink"
        }
    }
    
    if ($fileChanges -gt 0) {
        $script:FilesModified++
        
        if ($DryRun) {
            Write-Host "  [DRY RUN] Would fix $fileChanges links in: $relativePath" -ForegroundColor Yellow
        } else {
            # Create backup
            $backupPath = "$FilePath.backup-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
            Copy-Item $FilePath $backupPath -Force
            
            # Write updated content
            Set-Content -Path $FilePath -Value $content -NoNewline
            Write-Host "  ✅ Fixed $fileChanges links in: $relativePath" -ForegroundColor Green
        }
    } else {
        Write-Verbose "  No changes needed"
    }
}

# Main execution
Write-Host "`n🔧 Fixing README.md relative links..." -ForegroundColor Cyan
Write-Host "📂 Docs path: $DocsPath`n" -ForegroundColor Gray

if ($DryRun) {
    Write-Host "🔍 DRY RUN MODE - No files will be modified`n" -ForegroundColor Yellow
}

if (-not (Test-Path $DocsPath)) {
    Write-Error "Docs path not found: $DocsPath"
    exit 1
}

# Get all README.md files in level-* folders
$readmeFiles = Get-ChildItem -Path $DocsPath -Filter "README.md" -Recurse | 
    Where-Object { $_.DirectoryName -match "level-\d+" }

Write-Host "Found $($readmeFiles.Count) README.md files in level folders`n" -ForegroundColor Cyan

foreach ($file in $readmeFiles) {
    Fix-ReadmeLinks -FilePath $file.FullName
}

# Report results
Write-Host "`n" + ("=" * 80) -ForegroundColor Cyan
Write-Host "📊 FIX SUMMARY" -ForegroundColor Cyan
Write-Host ("=" * 80) -ForegroundColor Cyan

Write-Host "`n📁 README Files Scanned: " -NoNewline
Write-Host $script:TotalReadmeFiles -ForegroundColor Green

Write-Host "📝 Files Modified: " -NoNewline
Write-Host $script:FilesModified -ForegroundColor $(if ($script:FilesModified -gt 0) { "Green" } else { "Yellow" })

Write-Host "🔗 Links Fixed: " -NoNewline
Write-Host $script:LinksFixed -ForegroundColor $(if ($script:LinksFixed -gt 0) { "Green" } else { "Yellow" })

if ($DryRun) {
    Write-Host "`n💡 This was a DRY RUN. Run without -DryRun to apply changes." -ForegroundColor Yellow
} else {
    if ($script:FilesModified -gt 0) {
        Write-Host "`n✅ Changes applied successfully!" -ForegroundColor Green
        Write-Host "📦 Backups created with timestamp suffix" -ForegroundColor Gray
    }
}

Write-Host "`n" + ("=" * 80) -ForegroundColor Cyan

exit 0
