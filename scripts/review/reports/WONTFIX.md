# WONTFIX Register

Findings intentionally not closed in this review pass. Each entry has a
rationale tied to the master plan §A (P3) policy: "style-package opinion
mismatches with project voice; intentional legacy references in migration
narratives; draft pages explicitly kept as drafts."

This file is finalized in **Phase 1.5 sign-off** (PR-2). Phase 5 final
report cross-checks this list to ensure the gates were not weakened
silently.

---

## P3 — Style-package vs project voice

| ID | Rule / Pattern | Why WONTFIX | Affected files (sample) |
|---|---|---|---|
| WX-001 | `Microsoft.Auto` (severity=error) | Project consistently uses hyphenated forms ("auto-failover", "auto-renew", "auto-classification") aligned with Azure documentation conventions. Demoting to `warning` in `.vale.ini`. | 30 occurrences across L300 KB-checks |
| WX-002 | `Microsoft.Avoid` flag on "Backend" | "Backend" is standard Azure terminology (e.g., Azure Front Door backend pool). Demoting rule to `warning`. | `level-300/api-gateway-patterns.md`, 2 others |
| WX-003 | `Microsoft.HeadingAcronyms` (warning-only) | Project uses RAG, AI, GPU, TCO, ROI, etc. in section headings as standard practice for technical training. Suppression already configured. | 149 occurrences |
| WX-004 | `Microsoft.Adverbs` (warning-only) | "quickly", "rapidly", "easily" appear in marketing-adjacent sections of sales-track content. Suppression already configured. | 109 occurrences |
| WX-005 | `Microsoft.FirstPerson` (warning-only) | Sovereign training intentionally uses "we / you" voice (per master plan §E). Suppression already configured. | site-wide |
| WX-006 | `Microsoft.Wordiness`, `Microsoft.Negative`, `Microsoft.Passive`, `Microsoft.SentenceLength`, `Microsoft.OxfordComma`, `Microsoft.Dashes`, `Microsoft.HeadingPunctuation`, `Microsoft.Headings`, `Microsoft.Vocab`, `Microsoft.Terms` | Aggregate suppressions per pilot calibration § (noise ratio 16.98 → 0.96 / 1000 words after curation). All listed in `.vale.ini` with inline comments. | site-wide |
| WX-007 | `Vale.Spelling`, `Vale.Terms` | Spelling: SovereignCloud vocab is the source of truth (121 product/technical terms). Vale.Spelling is too noisy on technical product names. | site-wide |

---

## P3 — Intentional terminology preservation

| ID | Pattern | Why WONTFIX | Affected files |
|---|---|---|---|
| WX-101 | `Arc-Enabled` (title-case) in section headings | Project intentionally uses sentence-case in body and title-case in headings ("# Arc-Enabled Servers", "## Arc-Enabled Kubernetes"). Both forms are acceptable per Azure docs. Mechanical sweep would change valid headings. | `level-100/azure-arc-servers.md`, `level-100/azure-arc-kubernetes.md`, `level-100/azure-arc-data-services.md`, `level-200/arc-advanced-management.md` |
| WX-102 | `Azure Stack HCI` mentions inside migration narratives | Per `lint_terminology.py` migration-narrative detection (paragraphs containing "legacy", "formerly", "previously known", "rebranded", "renamed", "history", "evolution", "Era", or short headings naming both products). These are intentional historical references. | `level-100/azure-local-overview.md` (history section), `level-50/cloud-deployment-models.md` (fixed in Phase 2.1), `resources/README.md` (community channel names — see WX-103) |
| WX-103 | "Azure Stack HCI Community" / "AzureStackHCI" YouTube channel | These are proper nouns of existing Microsoft Tech Community channels and YouTube channels. Renaming would invalidate the link references. | `resources/README.md` lines 117, 128 |
| WX-104 | `edge-rag` as Kubernetes namespace name | The string `edge-rag` is the literal Kubernetes namespace identifier in lab `kubectl` commands. Cannot rename without invalidating the lab. The display text "Namespace \"edge-rag\" created" in `**Expected Output:**` is the literal kubectl output and must match the namespace. | `level-200/lab-03-edge-rag-setup.md` |

---

## P3 — Top-level / system files

| ID | File | Why WONTFIX | Note |
|---|---|---|---|
| WX-201 | `README.md` (root) | This is the GitHub repo README, **excluded from Jekyll build** via `_config.yml` `exclude:` list. Front-matter is not required. | False positive in `check_frontmatter.py`; will add an `--exclude-list` flag in Phase 2.2 to silence. |

---

## P3 — Build infrastructure noise (informational)

| ID | Pattern | Why WONTFIX | Note |
|---|---|---|---|
| WX-301 | 68 Sass deprecation warnings from `just-the-docs` 0.12.0 | Upstream theme issue; project does not own the theme. | Treat 68 as the immutable Phase 5 baseline ceiling. Reduction requires theme upgrade (out of scope per master plan "anti-goals"). |

---

## P3 — Lychee external link rate limits

| ID | Pattern | Why WONTFIX | Note |
|---|---|---|---|
| WX-401 | `learn.microsoft.com/*` link checks | learn.microsoft.com aggressively rate-limits CI checks (returns 429 / 403 frequently). Already excluded from `lychee.toml`. | If a citation URL is wrong, it will be caught at content-review time, not by lychee. |

---

## Future-pass (BACKLOG, not P3)

The following are explicitly **not WONTFIX** but are pushed to BACKLOG.md
because they exceed the budget caps for this pass and the master plan
forbids over-engineering:

- Per-page description generation for 78 files (Phase 3 work, not Phase 2 mechanical)
- Adding `**Reference:**` links to 7 KB-checks missing them (Phase 3 work)
- Authoring 5 TBD visual assets (deferred unless they block a P0/P1 finding, per §4.1)
- Mermaid duplicate-id systematic sweep (deferred to Phase 4.3 a11y pass)

See `BACKLOG.md` for the full deferred list.
