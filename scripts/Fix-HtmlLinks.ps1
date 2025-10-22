#Requires -Version 7.0

<#
.SYNOPSIS
    Removes .html extensions from internal markdown links.

.DESCRIPTION
    Scans all markdown files and converts links from .html to extensionless format
    for Jekyll pretty URLs. Backs up files before modification.

.PARAMETER DocsPath
    Path to the docs folder. Defaults to ../docs relative to script location.

.PARAMETER DryRun
    Preview changes without modifying files.

.EXAMPLE
    .\Fix-HtmlLinks.ps1 -DryRun

.EXAMPLE
    .\Fix-HtmlLinks.ps1 -Verbose
#>

[CmdletBinding(SupportsShouldProcess)]
param(
    [Parameter()]
    [string]$DocsPath = (Join-Path $PSScriptRoot "..\docs"),
    
    [Parameter()]
    [switch]$DryRun
)

# Initialize counters
$script:TotalFiles = 0
$script:FilesModified = 0
$script:LinksFixed = 0
$script:Changes = @()

function Fix-MarkdownLinks {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$FilePath
    )
    
    $script:TotalFiles++
    $relativePath = Resolve-Path -Relative $FilePath
    
    Write-Verbose "Processing: $relativePath"
    
    $content = Get-Content $FilePath -Raw
    $originalContent = $content
    $fileChanges = 0
    
    # Pattern 1: [text](file.html) -> [text](file)
    # Match .html at end of path (before anchor or closing paren)
    $pattern1 = '\]\(([^)]+?)\.html(#[^)]+)?\)'
    $matches1 = [regex]::Matches($content, $pattern1)
    
    if ($matches1.Count -gt 0) {
        Write-Verbose "  Found $($matches1.Count) .html links"
        
        foreach ($match in $matches1) {
            $fullMatch = $match.Value
            $pathWithoutHtml = $match.Groups[1].Value
            $anchor = $match.Groups[2].Value
            
            # Skip external URLs
            if ($pathWithoutHtml -match '^https?://') {
                continue
            }
            
            # Reconstruct link without .html
            $newLink = "](${pathWithoutHtml}${anchor})"
            
            $content = $content.Replace($fullMatch, $newLink)
            $fileChanges++
            $script:LinksFixed++
            
            $script:Changes += [PSCustomObject]@{
                File = $relativePath
                Original = $fullMatch
                Fixed = $newLink
            }
        }
    }
    
    # Pattern 2: [text](../path/file.html) -> [text](../path/file)
    # This is covered by pattern1 but let's be explicit about relative paths
    
    if ($fileChanges -gt 0) {
        $script:FilesModified++
        
        if ($DryRun) {
            Write-Host "  [DRY RUN] Would fix $fileChanges links in: $relativePath" -ForegroundColor Yellow
        } else {
            if ($PSCmdlet.ShouldProcess($relativePath, "Fix $fileChanges .html links")) {
                # Create backup
                $backupPath = "$FilePath.backup-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
                Copy-Item $FilePath $backupPath -Force
                Write-Verbose "  Created backup: $backupPath"
                
                # Write updated content
                Set-Content -Path $FilePath -Value $content -NoNewline
                Write-Host "  ✅ Fixed $fileChanges links in: $relativePath" -ForegroundColor Green
            }
        }
    }
}

# Main execution
Write-Host "`n🔧 Fixing .html extensions in markdown links..." -ForegroundColor Cyan
Write-Host "📂 Docs path: $DocsPath" -ForegroundColor Gray

if ($DryRun) {
    Write-Host "🔍 DRY RUN MODE - No files will be modified`n" -ForegroundColor Yellow
} else {
    Write-Host "⚠️  Files will be modified (backups created)`n" -ForegroundColor Yellow
}

if (-not (Test-Path $DocsPath)) {
    Write-Error "Docs path not found: $DocsPath"
    exit 1
}

# Get all markdown files
$markdownFiles = Get-ChildItem -Path $DocsPath -Filter "*.md" -Recurse

Write-Host "Found $($markdownFiles.Count) markdown files`n" -ForegroundColor Cyan

foreach ($file in $markdownFiles) {
    Fix-MarkdownLinks -FilePath $file.FullName
}

# Report results
Write-Host "`n" + ("=" * 80) -ForegroundColor Cyan
Write-Host "📊 FIX SUMMARY" -ForegroundColor Cyan
Write-Host ("=" * 80) -ForegroundColor Cyan

Write-Host "`n📁 Files Scanned: " -NoNewline
Write-Host $script:TotalFiles -ForegroundColor Green

Write-Host "📝 Files Modified: " -NoNewline
Write-Host $script:FilesModified -ForegroundColor $(if ($script:FilesModified -gt 0) { "Green" } else { "Yellow" })

Write-Host "🔗 Links Fixed: " -NoNewline
Write-Host $script:LinksFixed -ForegroundColor $(if ($script:LinksFixed -gt 0) { "Green" } else { "Yellow" })

if ($script:Changes.Count -gt 0 -and $Verbose) {
    Write-Host "`n📋 Sample Changes (first 10):" -ForegroundColor Yellow
    $script:Changes | Select-Object -First 10 | Format-Table -Property File, Original, Fixed -Wrap | Out-String | Write-Host
}

if ($DryRun) {
    Write-Host "`n💡 This was a DRY RUN. Run without -DryRun to apply changes." -ForegroundColor Yellow
} else {
    Write-Host "`n✅ Changes applied successfully!" -ForegroundColor Green
    Write-Host "📦 Backups created with timestamp suffix" -ForegroundColor Gray
    
    if ($script:FilesModified -gt 0) {
        Write-Host "`n📝 Next Steps:" -ForegroundColor Cyan
        Write-Host "  1. Review changes: git diff" -ForegroundColor Gray
        Write-Host "  2. Test locally: bundle exec jekyll serve" -ForegroundColor Gray
        Write-Host "  3. Commit: git add docs/" -ForegroundColor Gray
        Write-Host "  4. Push: git commit -m 'fix: remove .html extensions from internal links' && git push" -ForegroundColor Gray
    }
}

Write-Host "`n" + ("=" * 80) -ForegroundColor Cyan

# Exit with success
exit 0
