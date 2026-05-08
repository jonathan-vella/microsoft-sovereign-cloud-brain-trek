cd /workspaces/sov-cloud-brain-trek
export PATH="$HOME/.local/bin:$HOME/.npm-global/bin:$PATH"

mkdir -p scripts/review/reports

python3 scripts/review/check_frontmatter.py --docs-root docs --out scripts/review/reports/frontmatter.txt > /dev/null
python3 scripts/review/lint_terminology.py --docs-root docs --out scripts/review/reports/terminology.txt > /dev/null
python3 scripts/review/check_knowledge_checks.py --docs-root docs --out scripts/review/reports/knowledge-checks.txt > /dev/null
python3 scripts/review/inventory.py --docs-root docs --out scripts/review/reports/inventory.csv > /dev/null

npx --yes markdownlint-cli2 "docs/**/*.md" > scripts/review/reports/markdownlint.txt 2>&1
ml=$(grep -cE "^docs/.+:[0-9]+" scripts/review/reports/markdownlint.txt || echo 0)

vale --config=.vale.ini --output=line --no-exit --minAlertLevel=warning docs/ > scripts/review/reports/vale.txt 2>&1
ve=$(vale --config=.vale.ini --output=line --no-exit --minAlertLevel=error docs/ 2>&1 | wc -l)
vw=$(wc -l < scripts/review/reports/vale.txt)

rm -rf _site .lycheecache
bundle exec jekyll build --strict_front_matter --safe > scripts/review/reports/build.log 2>&1
bex=$?
bw=$(grep -ciE 'warning|deprecat' scripts/review/reports/build.log)
be=$(grep -ciE '\\bError\\b|\\bfatal\\b' scripts/review/reports/build.log)

lychee --config lychee.toml --format markdown --offline '_site/**/*.html' > scripts/review/reports/lychee-html.md 2>&1 || true
lyt=$(grep -E "🔍 .*Total" scripts/review/reports/lychee-html.md | head -1)
lye=$(grep -c "^✗ \\[ERR\\]" scripts/review/reports/lychee-html.md)

echo "============================================================"
echo "PHASE 2 FINAL AUDIT — 2026-05-08"
echo "============================================================"
echo ""
echo "Inventory: $(wc -l < scripts/review/reports/inventory.csv) lines"
echo ""
echo "| Dimension          | P0 | P1 | P2 |"
echo "|--------------------|----|----|----|"
printf "| Frontmatter        | %2d | %2d | %2d |\n" "$(grep -c '^P0 ' scripts/review/reports/frontmatter.txt)" "$(grep -c '^P1 ' scripts/review/reports/frontmatter.txt)" 0
printf "| Terminology        | %2d |  - | %2d |\n" "$(grep -c '^P0 ' scripts/review/reports/terminology.txt)" "$(grep -c '^P2 ' scripts/review/reports/terminology.txt)"
printf "| Knowledge-checks   | %2d | %2d | %2d |\n" "$(grep -c '^P0 ' scripts/review/reports/knowledge-checks.txt)" "$(grep -c '^P1 ' scripts/review/reports/knowledge-checks.txt)" "$(grep -c '^P2 ' scripts/review/reports/knowledge-checks.txt)"
echo ""
echo "Markdownlint:    $ml findings"
echo "Vale errors:     $ve"
echo "Vale warnings:   $vw"
echo "Build:           exit=$bex warnings=$bw errors=$be"
echo "Lychee summary:  $lyt"
echo "Lychee errors:   $lye"

echo ""
echo "=== Per-level sanity (orphans / drafts) ==="
echo "_drafts/ files:"
ls docs/_drafts/ 2>/dev/null | wc -l
echo ""
echo "Files still nav_excluded:"
python3 -c "
import csv
try:
    with open('scripts/review/reports/inventory.csv') as f:
        rows = [r for r in csv.DictReader(f) if r['nav_excluded']=='true']
        for r in rows:
            print(f'  {r[\"path\"]}')
        print(f'Total: {len(rows)}')
except Exception as e:
    print(f'Error reading inventory: {e}')
"
