#!/usr/bin/env bash
# Docs review audit orchestrator (Phase 1 + Phase 5 re-run).
# Plan reference: §0.1 Tool installation; §1 Cross-cutting audit dimensions.
#
# Usage:
#   bash scripts/review/run-audit.sh                  # full audit
#   bash scripts/review/run-audit.sh --scope docs/level-100/module-04-azure-arc.md  # pilot
#   bash scripts/review/run-audit.sh --fail-on=p0     # fail script if any P0 findings
#
# Output: all reports under scripts/review/reports/
set -uo pipefail

cd "$(git rev-parse --show-toplevel)" || exit 2

REPORTS_DIR="scripts/review/reports"
mkdir -p "$REPORTS_DIR"

SCOPE=""
FAIL_ON="none"
SKIP_BUILD="false"

for arg in "$@"; do
  case $arg in
    --scope=*) SCOPE="${arg#--scope=}" ;;
    --scope)   shift; SCOPE="$1" ;;
    --fail-on=*) FAIL_ON="${arg#--fail-on=}" ;;
    --skip-build) SKIP_BUILD="true" ;;
    -h|--help)
      sed -n '1,12p' "$0"; exit 0 ;;
  esac
done

echo "================================================================"
echo "Docs review audit  $(date -u +%FT%TZ)  scope=${SCOPE:-full}"
echo "================================================================"

# 1. Inventory (always full — pilot still benefits from full inventory)
echo "[1/8] inventory..."
python3 scripts/review/inventory.py --docs-root docs --out "$REPORTS_DIR/inventory.csv" \
  | tee "$REPORTS_DIR/inventory.log"

# 2. Front-matter
echo "[2/8] front-matter..."
python3 scripts/review/check_frontmatter.py --docs-root docs --out "$REPORTS_DIR/frontmatter.txt" || true

# 3. Knowledge-checks
echo "[3/8] knowledge-checks..."
python3 scripts/review/check_knowledge_checks.py --docs-root docs --out "$REPORTS_DIR/knowledge-checks.txt" || true

# 4. Terminology
echo "[4/8] terminology..."
python3 scripts/review/lint_terminology.py --docs-root docs --out "$REPORTS_DIR/terminology.txt" || true

# 5. Markdownlint
echo "[5/8] markdownlint..."
if [[ -n "$SCOPE" ]]; then
  npx --yes markdownlint-cli2 "$SCOPE" 2>&1 | tee "$REPORTS_DIR/markdownlint.txt" || true
else
  npx --yes markdownlint-cli2 "docs/**/*.md" 2>&1 | tee "$REPORTS_DIR/markdownlint.txt" || true
fi

# 6. Vale (severity≥error gate, warnings informational)
echo "[6/8] vale..."
if command -v vale >/dev/null 2>&1; then
  if [[ -n "$SCOPE" ]]; then
    vale --output=line --no-exit "$SCOPE" 2>&1 | tee "$REPORTS_DIR/vale.txt" || true
  else
    vale --output=line --no-exit docs 2>&1 | tee "$REPORTS_DIR/vale.txt" || true
  fi
else
  echo "vale not installed — skip" | tee "$REPORTS_DIR/vale.txt"
fi

# 7. Lychee (link check)
echo "[7/8] lychee..."
if command -v lychee >/dev/null 2>&1; then
  TARGET="${SCOPE:-docs/**/*.md}"
  lychee --config lychee.toml --format markdown "$TARGET" \
    > "$REPORTS_DIR/lychee.md" 2>&1 || true
  # Summary line for the orchestrator
  grep -E "(\\[ERROR\\]|^\\| Total|^Summary)" "$REPORTS_DIR/lychee.md" | head -20 || true
else
  echo "lychee not installed — skip" | tee "$REPORTS_DIR/lychee.md"
fi

# 8. Jekyll baseline build (gate)
echo "[8/8] jekyll build..."
if [[ "$SKIP_BUILD" == "true" ]]; then
  echo "build skipped (--skip-build)" | tee "$REPORTS_DIR/build.log"
else
  bundle exec jekyll build --strict_front_matter --safe \
    > "$REPORTS_DIR/build.log" 2>&1 || true
  tail -20 "$REPORTS_DIR/build.log" || true
  # Post-build a11y fix (idempotent, see scripts/review/postbuild_a11y.py)
  if [[ -d "_site" ]]; then
    python3 scripts/review/postbuild_a11y.py --site-root _site \
      | tee -a "$REPORTS_DIR/build.log" || true
  fi
fi

# Aggregate counts
{
  echo "# Audit summary  $(date -u +%FT%TZ)"
  echo
  echo "scope: ${SCOPE:-full}"
  echo
  echo "| Dimension | P0 | P1 | P2 |"
  echo "|---|---:|---:|---:|"
  for f in frontmatter terminology knowledge-checks; do
    file="$REPORTS_DIR/$f.txt"
    if [[ -f "$file" ]]; then
      p0=$(grep -c "^P0 " "$file" 2>/dev/null || echo 0)
      p1=$(grep -c "^P1 " "$file" 2>/dev/null || echo 0)
      p2=$(grep -c "^P2 " "$file" 2>/dev/null || echo 0)
      printf "| %s | %s | %s | %s |\n" "$f" "$p0" "$p1" "$p2"
    fi
  done
  echo
  echo "Build log: $(wc -l < "$REPORTS_DIR/build.log" 2>/dev/null || echo 0) lines"
  if [[ -f "$REPORTS_DIR/build.log" ]]; then
    warn=$(grep -ciE "warn|deprecat" "$REPORTS_DIR/build.log" 2>/dev/null || echo 0)
    err=$(grep -ciE "error|fatal|abort" "$REPORTS_DIR/build.log" 2>/dev/null || echo 0)
    echo "Build warnings (approx): $warn — errors (approx): $err"
  fi
} | tee "$REPORTS_DIR/AUDIT-SUMMARY.md"

# Final gate
if [[ "$FAIL_ON" == "p0" ]]; then
  total_p0=$(grep -h "^P0 " "$REPORTS_DIR"/frontmatter.txt "$REPORTS_DIR"/terminology.txt "$REPORTS_DIR"/knowledge-checks.txt 2>/dev/null | wc -l)
  if [[ "$total_p0" -gt 0 ]]; then
    echo "FAIL: $total_p0 P0 findings"
    exit 1
  fi
fi
echo "Audit complete. Reports under $REPORTS_DIR/"
