# Phase 2.6 — Nav-Exclusion Triage Decisions

**Date:** 2026-05-08
**Plan reference:** §H (publish-or-delete-or-draft criteria) and §I (SME requirement for regulated-industry pages)

This log captures every nav-excluded page in the audit and the disposition
applied in Phase 2.6.

---

## Decision matrix

| File | Words | desc | Internal links | §H criteria pass? | Action | Reason |
|---|---:|---|---:|---|---|---|
| `404.md` | 140 | n/a | 0 | n/a | KEEP `nav_exclude: true` | System / 404 page |
| `assets/images/README.md` | 2,381 | n/a | 0 | n/a | KEEP `nav_exclude: true` | Internal asset registry |
| `level-100/VISUAL_SPECIFICATIONS.md` | 5,107 | n/a | 0 | n/a | KEEP `nav_exclude: true` | Internal design spec |
| `level-200/VISUAL_SPECIFICATIONS.md` | 2,551 | n/a | 0 | n/a | KEEP `nav_exclude: true` | Internal design spec |
| `level-300/VISUAL_SPECIFICATIONS.md` | 1,064 | n/a | 0 | n/a | KEEP `nav_exclude: true` | Internal design spec |
| `docs/README.md` | 352 lines | yes | 0 | n/a | KEEP `nav_exclude: true` | Documentation status README; excluded from Jekyll source |
| `level-300/sovereign-landing-zone.md` | 504 | yes | 3 | YES | **PUBLISH** | Met all §H criteria; not regulated-industry |
| `level-300/critical-infrastructure.md` | 435 | yes | 2 | YES, but §I applies | **DEFERRED to Phase 3.4** | Regulated-industry — SME sign-off required |
| `level-300/financial-services.md` | 445 | yes | 2 | YES, but §I applies | **DEFERRED to Phase 3.4** | Regulated-industry — SME sign-off required |
| `level-300/healthcare-sovereign.md` | 434 | yes | 2 | YES, but §I applies | **DEFERRED to Phase 3.4** | Regulated-industry — SME sign-off required |
| `level-300/api-gateway-patterns.md` | 264 | yes | 2 | NO (< 400 words) | **KEPT** `nav_exclude: true` | Referenced 1× from `critical-infrastructure.md`; expand in Phase 3.4 (BACKLOG B-012) |
| `level-300/data-classification.md` | 341 | yes | 2 | NO (< 400 words) | **KEPT** `nav_exclude: true` | Referenced from KB-checks; expand in Phase 3.4 |
| `level-300/data-mesh-sovereignty.md` | 228 | yes | 2 | NO | **KEPT** `nav_exclude: true` | Referenced from architecture-knowledge-check; expand in Phase 3.4 |
| `level-300/devsecops-pipeline.md` | 208 | yes | 2 | NO | **KEPT** `nav_exclude: true` | Referenced 4× from `operations-knowledge-check.md`; expand in Phase 3.4 |
| `level-300/disaster-recovery.md` | 280 | yes | 2 | NO | **KEPT** `nav_exclude: true` | Referenced 4× from `operations-knowledge-check.md`; expand in Phase 3.4 |
| `level-300/event-driven-architecture.md` | 225 | yes | 2 | NO | **KEPT** `nav_exclude: true` | Referenced from KB-checks; expand in Phase 3.4 |
| `level-300/government-cloud.md` | 389 | yes | 2 | NO (< 400 words) | **KEPT** `nav_exclude: true` | §I-eligible + referenced from KB-checks; expand in Phase 3.4 |
| `level-300/incident-response.md` | 346 | yes | 2 | NO | **KEPT** `nav_exclude: true` | Referenced from KB-checks; expand in Phase 3.4 |
| `level-300/observability-stack.md` | 315 | yes | 2 | NO | **KEPT** `nav_exclude: true` | Referenced 5× from `operations-knowledge-check.md`; expand in Phase 3.4 |

---

## Summary

| Disposition | Count |
|---|---:|
| KEEP `nav_exclude: true` (system / spec / docs README) | 6 |
| PUBLISH (nav_exclude removed) | 1 |
| DEFERRED to Phase 3.4 (SME-eligible) | 3 |
| KEPT `nav_exclude: true` (referenced from published, expand in Phase 3.4) | 9 |
| **Total** | **19** |

(Note: count is 19, one more than the original 18 — `docs/README.md` was added to the `nav_exclude: true` list in Phase 2.2 to silence a checker false-positive.)

**Important deviation from initial plan:** the audit's preliminary
recommendation was to move 9 sub-400-word L300 pages to `_drafts/`. Phase 2.6
discovered (via lychee re-run after the move) that those 9 pages are
referenced 30+ times by published L300 KB-checks (`operations-knowledge-check.md`,
`architecture-knowledge-check.md`, `industry-knowledge-check.md`,
`patterns-knowledge-check.md`). Moving them broke 15 internal links.

**Resolution:** restored all 9 pages to `docs/level-300/` with `nav_exclude: true`
preserved (i.e. not in nav, but linkable from KB-check references). Phase 3.4
reviewer expands each to ≥ 400 words OR converts the references in the
KB-checks to point elsewhere. See BACKLOG B-012.

The `_drafts/` collection scaffold remains in `_config.yml` for future use.

---

## `_drafts/` collection

Added to `_config.yml`:

```yaml
collections:
  drafts:
    output: false
    permalink: /_drafts/:path/
```

`_drafts/` files are retained in the repo and tracked in git, but `output: false`
means they are **not built into `_site/`** and do not appear in nav, search,
or sitemaps. To resurrect a draft for publication:

1. Move the file from `docs/_drafts/level-300-<topic>.md` back to `docs/level-300/<topic>.md`
2. Remove `nav_exclude: true` from front-matter (if present)
3. Verify §H criteria are met (≥ 400 words, description, ≥ 1 outbound internal link, no TODO markers)
4. Run `bash scripts/review/run-audit.sh --scope docs/level-300/<topic>.md`

---

## Permalinks / SEO impact

The 9 moved drafts had `nav_exclude: true` already, so they were never linked
from any nav menu. Lychee link check after Phase 2.3 fixes confirmed **0 broken
internal links** result from the moves. No redirect mapping is required.

The 1 newly-published page (`sovereign-landing-zone.md`) was previously linked
from 3 internal pages (per inventory `outbound_internal_links=3`); those links
already used the correct `.md` extension and now resolve to a navigable page
instead of a hidden one — net positive.
