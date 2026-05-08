# Phase 1 — Cross-cutting Audit Reports

This folder is the source of truth for review status. It is produced by
`scripts/review/run-audit.sh` and contains:

| File | Phase | Type | Tracked in git? |
|---|---|---|---|
| `inventory.csv` | 0.3 | Generated | Yes (snapshot) |
| `baseline-build.log` | 0.2 | Generated | Yes (single committed reference baseline) |
| `frontmatter.txt`, `terminology.txt`, `knowledge-checks.txt` | 1 | Generated | No |
| `markdownlint.txt`, `vale.txt`, `lychee.md`, `build.log` | 1 / 5 | Generated | No |
| `AUDIT-SUMMARY.md` | 1 / 5 | Generated | No (human-readable rollup) |
| `pilot-results.md` | 0.5 | Narrative | Yes |
| `AUDIT.md`, `WONTFIX.md`, `BACKLOG.md` | 1 | Narrative | Yes |
| `nav-exclude-decisions.md` | 2.6 | Narrative | Yes |
| `level-<N>-changes.md` | 3.x | Narrative | Yes |
| `FINAL.md` | 5 | Narrative | Yes |

Re-run anytime with:

```bash
bash scripts/review/run-audit.sh
```
