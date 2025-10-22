#Requires -Version 7.0

<#
.SYNOPSIS
    Checks for broken internal links in markdown files.

.DESCRIPTION
    Scans all markdown files in the docs/ folder and validates internal links.
    Reports links that use incorrect formats or point to non-existent files.

.PARAMETER DocsPath
    Path to the docs folder. Defaults to ../docs relative to script location.

.PARAMETER ExcludeExternal
    Skip validation of external (http/https) links.

.EXAMPLE
    .\Check-BrokenLinks.ps1

.EXAMPLE
    .\Check-BrokenLinks.ps1 -DocsPath "C:\Repos\project\docs" -Verbose
#>

[CmdletBinding()]
param(
    [Parameter()]
    [string]$DocsPath = (Join-Path $PSScriptRoot "..\docs"),
    
    [Parameter()]
    [switch]$ExcludeExternal
)

# Initialize counters
$script:TotalFiles = 0
$script:TotalLinks = 0
$script:ProblematicLinks = @()
$script:JekyllLinks = 0
$script:RelativeLinks = 0
$script:HtmlExtensionLinks = 0
$script:ExternalLinks = 0

function Test-MarkdownLink {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$FilePath,
        
        [Parameter(Mandatory)]
        [string]$Link,
        
        [Parameter(Mandatory)]
        [int]$LineNumber
    )
    
    $script:TotalLinks++
    
    # Skip anchors
    if ($Link -match '^#') {
        return
    }
    
    # Skip mailto links
    if ($Link -match '^mailto:') {
        return
    }
    
    # Check external links
    if ($Link -match '^https?://') {
        $script:ExternalLinks++
        return
    }
    
    # Check for Jekyll link tags (correct format)
    if ($Link -match '\{\{.*\}\}.*\{%.*link.*%\}' -or $Link -match '\{%.*link.*%\}') {
        $script:JekyllLinks++
        return  # These are handled by Jekyll at build time
    }
    
    # Check for .html extensions (problematic with pretty URLs)
    if ($Link -match '\.html($|#)') {
        $script:HtmlExtensionLinks++
        $script:ProblematicLinks += [PSCustomObject]@{
            File = (Resolve-Path -Relative $FilePath)
            Line = $LineNumber
            Link = $Link
            Issue = "Uses .html extension (Jekyll uses pretty URLs without extensions)"
            Severity = "High"
        }
        return
    }
    
    # Check relative links
    if ($Link -notmatch '^/') {
        $script:RelativeLinks++
        
        # Try to resolve the link relative to the current file
        $currentDir = Split-Path -Parent $FilePath
        $targetPath = Join-Path $currentDir $Link
        
        # Remove anchor if present
        $targetPathNoAnchor = $targetPath -replace '#.*$', ''
        
        # Check if file exists (add .md if not specified)
        $exists = Test-Path $targetPathNoAnchor
        if (-not $exists -and $targetPathNoAnchor -notmatch '\.(md|html)$') {
            $exists = Test-Path "$targetPathNoAnchor.md"
        }
        
        if (-not $exists) {
            # Check if it's a directory link (should point to README.md)
            $readmePath = Join-Path $targetPathNoAnchor "README.md"
            $exists = Test-Path $readmePath
            
            if (-not $exists) {
                $script:ProblematicLinks += [PSCustomObject]@{
                    File = (Resolve-Path -Relative $FilePath)
                    Line = $LineNumber
                    Link = $Link
                    Issue = "Target file not found (checked: $targetPathNoAnchor, ${targetPathNoAnchor}.md, $readmePath)"
                    Severity = "Critical"
                }
            }
        }
    }
}

function Get-MarkdownLinks {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$FilePath
    )
    
    $content = Get-Content $FilePath -Raw
    $lineNumber = 0
    
    # Split into lines to track line numbers
    $lines = $content -split "`r?`n"
    
    foreach ($line in $lines) {
        $lineNumber++
        
        # Match markdown links: [text](url)
        $matches = [regex]::Matches($line, '\[([^\]]+)\]\(([^)]+)\)')
        
        foreach ($match in $matches) {
            $linkText = $match.Groups[1].Value
            $linkUrl = $match.Groups[2].Value
            
            # Remove any attributes like {: .btn}
            $linkUrl = ($linkUrl -split '\s+')[0]
            
            Test-MarkdownLink -FilePath $FilePath -Link $linkUrl -LineNumber $lineNumber
        }
    }
}

# Main execution
Write-Host "`n🔍 Scanning markdown files for broken links..." -ForegroundColor Cyan
Write-Host "📂 Docs path: $DocsPath`n" -ForegroundColor Gray

if (-not (Test-Path $DocsPath)) {
    Write-Error "Docs path not found: $DocsPath"
    exit 1
}

# Get all markdown files
$markdownFiles = Get-ChildItem -Path $DocsPath -Filter "*.md" -Recurse

foreach ($file in $markdownFiles) {
    $script:TotalFiles++
    Write-Verbose "Checking: $($file.FullName)"
    Get-MarkdownLinks -FilePath $file.FullName
}

# Report results
Write-Host "`n" + ("=" * 80) -ForegroundColor Cyan
Write-Host "📊 LINK CHECK SUMMARY" -ForegroundColor Cyan
Write-Host ("=" * 80) -ForegroundColor Cyan

Write-Host "`n📁 Files Scanned: " -NoNewline
Write-Host $script:TotalFiles -ForegroundColor Green

Write-Host "🔗 Total Links Found: " -NoNewline
Write-Host $script:TotalLinks -ForegroundColor Green

Write-Host "`n📋 Link Types:" -ForegroundColor Yellow
Write-Host "  ✅ Jekyll link tags (correct): " -NoNewline
Write-Host $script:JekyllLinks -ForegroundColor Green
Write-Host "  🌐 External links: " -NoNewline
Write-Host $script:ExternalLinks -ForegroundColor Cyan
Write-Host "  📝 Relative links: " -NoNewline
Write-Host $script:RelativeLinks -ForegroundColor Yellow
Write-Host "  ⚠️  .html extension links: " -NoNewline
Write-Host $script:HtmlExtensionLinks -ForegroundColor Magenta

# Display problematic links
if ($script:ProblematicLinks.Count -gt 0) {
    Write-Host "`n❌ PROBLEMATIC LINKS FOUND: " -NoNewline
    Write-Host $script:ProblematicLinks.Count -ForegroundColor Red
    Write-Host "`n" + ("-" * 80) -ForegroundColor Red
    
    # Group by severity
    $critical = $script:ProblematicLinks | Where-Object Severity -eq "Critical"
    $high = $script:ProblematicLinks | Where-Object Severity -eq "High"
    
    if ($critical.Count -gt 0) {
        Write-Host "`n🚨 CRITICAL - Broken Links (target not found):" -ForegroundColor Red
        $critical | Format-Table -Property File, Line, Link, Issue -Wrap | Out-String | Write-Host
    }
    
    if ($high.Count -gt 0) {
        Write-Host "`n⚠️  HIGH - Format Issues:" -ForegroundColor Yellow
        $high | Format-Table -Property File, Line, Link, Issue -Wrap | Out-String | Write-Host
    }
    
    Write-Host "`n💡 RECOMMENDATIONS:" -ForegroundColor Cyan
    Write-Host "  1. Replace .html extensions with Jekyll link tags: {{ site.baseurl }}{% link docs/path/file.md %}"
    Write-Host "  2. Use absolute Jekyll links for cross-level navigation"
    Write-Host "  3. Verify all file paths are correct"
    Write-Host "  4. Test changes locally with: bundle exec jekyll serve"
    
} else {
    Write-Host "`n✅ No problematic links found!" -ForegroundColor Green
}

Write-Host "`n" + ("=" * 80) -ForegroundColor Cyan

# Exit with error code if problems found
if ($script:ProblematicLinks.Count -gt 0) {
    exit 1
} else {
    exit 0
}
