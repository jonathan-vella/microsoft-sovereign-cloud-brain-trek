# Docs Content Review Tooling

Permanent tooling for the `/docs` content review pipeline. See
`plan-docsContentReview.prompt.md` (PR-1) for the master plan.

## Layout

```text
scripts/review/
├── README.md                       # This file
├── run-audit.sh                    # Orchestrator (Phase 1, Phase 5 re-run)
├── check_frontmatter.py            # Validator + --fix (Phase 2.2)
├── check_knowledge_checks.py       # Validator only (Phase 2.4 uses fix_*.py)
├── lint_terminology.py             # Validator + --fix (Phase 2.1, 2.7)
├── inventory.py                    # Builds reports/inventory.csv (Phase 0.3)
├── cache/                          # MS Learn snapshots (≤ 60 unique URLs)
│   └── <YYYY-MM-DD>/<slug>.md
└── reports/                        # All audit output (gitignored except summaries)
    ├── baseline-build.log          # Phase 0.2
    ├── inventory.csv               # Phase 0.3
    ├── pilot-results.md            # Phase 0.5
    ├── AUDIT.md                    # Phase 1
    ├── WONTFIX.md                  # Phase 1
    ├── BACKLOG.md                  # Phase 1
    ├── nav-exclude-decisions.md    # Phase 2.6
    ├── level-<N>-changes.md        # Phase 3.x (one per level)
    └── FINAL.md                    # Phase 5
```

## Tool prerequisites

The following must be on `PATH` (one-time install per dev environment):

| Tool | Min version | Install hint |
|---|---|---|
| `markdownlint-cli2` | 0.21 | `npm i -g markdownlint-cli2` (already in `package.json`) |
| `lychee` | 0.15 | prebuilt binary from <https://github.com/lycheeverse/lychee/releases> |
| `vale` | 3.4 | prebuilt binary from <https://github.com/errata-ai/vale/releases> |
| `pa11y-ci` | 4.1 | `npm i -g pa11y-ci` |
| `bundle` / `jekyll` | Jekyll 4.4 | `bundle install` (Gemfile already configured) |
| `python3` | 3.10+ | dev container default |

## Running the audit

```bash
# Full audit (Phase 1 + Phase 5 re-run)
bash scripts/review/run-audit.sh

# Single-module pilot (Phase 0.5 calibration)
bash scripts/review/run-audit.sh --scope level-100/module-04

# --fix mode for safe substitutions only (Phase 2)
python3 scripts/review/check_frontmatter.py --fix
python3 scripts/review/lint_terminology.py --fix
```

All outputs land under `scripts/review/reports/`. Treat that directory as
the source of truth for review status.

## Cap & severity policy

See the master plan §A (severity rubric) and §B (budget caps). Reports
must surface findings bucketed by severity P0/P1/P2/P3.

## CI integration (follow-up)

This tooling is designed to live in the repo permanently and be wired to
CI as a follow-up after PR-5. The audit script is non-interactive and
returns a non-zero exit code only on P0 findings (configurable via
`--fail-on=p0|p1|none`).
