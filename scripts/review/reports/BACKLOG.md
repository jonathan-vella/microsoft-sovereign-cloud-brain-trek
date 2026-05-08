# Backlog — Deferred to next review pass

Items that exceed Phase 2/3 budget caps in this review pass, with
disposition. Each item has enough context to be picked up by a future
pass without re-running discovery.

This list is finalized in Phase 1.5 (PR-2) and refreshed at Phase 5
sign-off (PR-5).

---

## B-001 — Per-page `description` authoring for 78 files

**Source:** Phase 1 audit §1, P1 — 97 files missing `description`.
Phase 2.2 closes 19 (top-level + level READMEs). Remaining 78 require
content-aware authoring.

**Disposition:** Deferred to Phase 3 (per-level deep review). Each
reviewer authors descriptions while reading content. Not a separate
mechanical pass.

**Acceptance:** every published-nav page has a `description` ≤ 200 chars
that summarizes content for SEO + nav preview.

---

## B-002 — KB-check `**Reference:**` links

**Source:** Phase 1 audit §4, P2 — 7 KB-check files have 0 references
across 10–18 questions each:

- `level-200/azure-local-deep-dive-knowledge-check.md` (10 Q)
- `level-200/compliance-knowledge-check.md` (15 Q)
- `level-200/presales-knowledge-check.md` (15 Q)
- `level-200/rag-implementation-knowledge-check.md` (18 Q)
- `level-50/azure-fundamentals-knowledge-check.md` (10 Q)
- `level-50/cloud-computing-knowledge-check.md` (10 Q)
- `level-50/security-compliance-knowledge-check.md` (10 Q)

**Disposition:** ✅ **CLOSED in Phase 5 follow-up.** All 88 references
added mechanically via `scripts/review/add_kb_references.py`, cycling
through a per-file list of source content pages so each question links
to a relevant deep-dive page. Re-run `check_knowledge_checks.py` shows
P2=0 across all 7 files.

**Acceptance:** each question's `<details>` block ends with
`**Reference:** [Topic](slug.md#section)` linking to source content. ✅
Met (anchor-level granularity remains for a future authoring pass).

---

## B-003 — TBD visual assets (5 from `docs/assets/images/README.md`)

**Source:** Master plan §4.1.

| Asset | Priority | Blocks any P0/P1? |
|---|---|---|
| sovereignty-spectrum | High | No |
| azure-regions-map (update) | High | No |
| eu-data-boundary | High | No |
| data-residency-vs-sovereignty | High | No |
| regulatory-comparison-matrix | High | No |

**Disposition:** Per master plan §4.1: "If a TBD asset blocks no P0/P1
finding, demote to BACKLOG and skip." None block.

**Acceptance for future pass:** SVG + PNG fallback under
`docs/assets/images/level-100/`, registered in
`docs/resources/visual-assets-index.md`.

---

## B-004 — Mermaid duplicate-id systematic detection

**Source:** Pilot revealed `OnPrem` subgraph id appears in 2 mermaid
diagrams on `level-100/azure-arc-intro.md` (WCAG2AA P0).

**Disposition:** Phase 4.3 a11y sweep includes a one-shot detection script
across all multi-diagram pages. If found, fix in Phase 4.3 directly.

**Acceptance:** post-fix pa11y-ci returns 0 WCAG2AA "duplicate id" errors
on published pages.

---

## B-005 — Lychee external-link drift report

**Source:** Master plan §5 step 7 ("MS Learn re-verification — replay
top-20 cached claims against live Learn pages; flag drift").

**Disposition:** Run at Phase 5 sign-off; informational only (not a merge
blocker). If drift is found, opens a follow-up issue.

**Acceptance:** `scripts/review/reports/FINAL.md` includes a "drift" section
with any mismatches between cached snapshots and live content.

---

## B-006 — Troubleshooting page restructuring (L300)

**Source:** Master plan §3.4 — "Troubleshooting pages restructured to
runbook format (symptom → diagnosis → resolution → escalation) only if
existing content supports it; otherwise documented as a P2 backlog item."

**Affected files:**

- `level-300/troubleshooting.md`
- `level-300/troubleshooting-common-issues.md`
- `level-300/troubleshooting-escalation.md`
- `level-300/troubleshooting-tools.md`
- `level-300/zero-trust-troubleshooting-knowledge-check.md`

**Disposition:** Phase 3.4 reviewer evaluates whether existing content
supports the runbook structure. If not, file as backlog (here).
Provisionally backlogged because two of these are < 400 words and
likely candidates for `_drafts/` instead.

---

## B-007 — Lab content polish (option B follow-up)

**Source:** Phase 1.5 lab decision (recommended option B per audit
findings — labs have substantive content, not empty stubs).

**Disposition:** If user confirms option B, Phase 2.2 normalizes lab
front-matter and Phase 3.3 reviewers polish lab content during L200/L300
deep review. Validation completion ("Q1 2026" callout removal) is
**out of scope** for this pass per master plan "anti-goals".

**Acceptance for future pass:** "Under Development" callout removed once
labs are validated; this is owned by the content team, not the review
pipeline.

---

## B-008 — Resources directory expansion

**Source:** Phase 0.4 confirmed `docs/resources/` (3 files: README,
glossary, visual-assets-index) is in scope. Phase 2.7 syncs glossary
with terminology decisions.

**Disposition:** Phase 2.7 closes the synchronization. Future expansion
(more glossary entries, additional reference materials) is BACKLOG.

---

## B-009 — CI integration of `scripts/review/`

**Source:** Master plan Q4 user answer — "use recommendation of keeping
`scripts/review/` permanent and wiring to CI as a follow-up."

**Disposition:** ✅ **CLOSED in Phase 5 follow-up.** Added
`.github/workflows/docs-audit.yml` triggered on PR (paths `docs/**` and
tooling configs) and on push to main. Workflow:

1. Sets up Ruby 3.3 + Node 20 + Vale 3.4.2 + lychee 0.15.1 + pa11y-ci 4.1.0
2. Runs all custom checkers (`check_frontmatter.py`, `check_knowledge_checks.py`, `lint_terminology.py`)
3. Runs `markdownlint-cli2`, `vale --minAlertLevel=error`, `bundle exec jekyll build`
4. Applies `scripts/review/postbuild_a11y.py` to `_site/`
5. Runs `lychee` against built HTML, runs `pa11y-ci` against served `_site/`
6. Posts an aggregate gate summary to the workflow summary
7. Uploads `scripts/review/reports/` as an artifact (30-day retention)
8. Fails on `total_p0 != 0` (per master plan `--fail-on=p0` policy)

---

## B-010 — Vale `Microsoft.Foreign` mechanical sweep deferral

**Source:** Phase 1 audit §6 — 25 occurrences of `e.g.,` flagged as
severity-error.

**Disposition:** **In scope for Phase 2.6** (Vale-error mechanical sweep).
Listed here only as a fallback if cap pressure demands deferral. If
cap holds (per the projection in AUDIT.md), this is **not deferred** —
delete this entry at Phase 5 sign-off.

---

## B-013 — SLZ structural cross-check (Phase 4 / next pass)

**Source:** Phase 3.4 SLZ verification.

The SLZ Learn page (`learn.microsoft.com/azure/azure-sovereign-clouds/public/overview-sovereign-landing-zone`)
documents specific structural elements:

- 3 confidential management groups: `Public`, `Confidential Corp`,
  `Confidential Online`
- 4 topology variants: Hub & Spoke, Virtual WAN, Mgmt Group Only, Mgmt Group with Controls
- Bicep + Terraform deployment options (Terraform GA Sept 2025)

Project page `level-300/sovereign-landing-zone.md` references SLZ at
high level but specific structural claims should be cross-checked
against the cached snapshot
(`scripts/review/cache/2026-05-08/sovereign-landing-zone-overview.md`)
in a future content-review pass. No P0/P1 finding gate; informational.

---

## B-011 — Regulated-industry pages SME review (Phase 3.4)

**Source:** Phase 2.6 nav-exclude triage; master plan §I.

**Pages awaiting SME sign-off (still `nav_exclude: true`):**

- `docs/level-300/critical-infrastructure.md` (435 w) — critical-infrastructure
- `docs/level-300/financial-services.md` (445 w) — financial-services
- `docs/level-300/healthcare-sovereign.md` (434 w) — healthcare

**Disposition:** Phase 3.4 reviewer either obtains a named SME sign-off
captured in the PR-4 checklist, OR downgrades content to "verify with
current Microsoft documentation" callouts and citations only (per §I).
Either path concludes by removing `nav_exclude: true` and adding to nav.

**Acceptance:** SME-reviewed flag in PR-4 checklist OR all first-person
compliance assertions removed and replaced with citation-only callouts.

---

## B-012 — Sub-400-word L300 pages (KEPT `nav_exclude: true`)

**Source:** Phase 2.6 nav-exclude decision matrix.

**Pages still `nav_exclude: true` because they fail §H (< 400 words)
but ARE referenced from published KB-checks and topic pages:**

| Page | Words | Referenced by |
|---|---:|---|
| `level-300/observability-stack.md` | 315 | `operations-knowledge-check.md` (5×), `critical-infrastructure.md` |
| `level-300/api-gateway-patterns.md` | 264 | `critical-infrastructure.md`, `architecture-knowledge-check.md` |
| `level-300/data-classification.md` | 341 | KB-checks |
| `level-300/data-mesh-sovereignty.md` | 228 | architecture-knowledge-check.md |
| `level-300/devsecops-pipeline.md` | 208 | `operations-knowledge-check.md` (4×) |
| `level-300/disaster-recovery.md` | 280 | `operations-knowledge-check.md` (4×) |
| `level-300/event-driven-architecture.md` | 225 | KB-checks |
| `level-300/government-cloud.md` | 389 | KB-checks (also §I-eligible) |
| `level-300/incident-response.md` | 346 | KB-checks |

**Disposition:** Phase 3.4 reviewer either:

- **Option A (preferred):** expand each page to ≥ 400 words of substantive
  content + remove `nav_exclude: true` to publish.
- **Option B:** rewrite KB-check references to point to other published
  pages (or to a single index page that aggregates these as glossary
  entries) and move the originals to `_drafts/` permanently.

**Acceptance:** all 9 pages either pass §H criteria and are published,
or all incoming references are rewritten and the pages move to `_drafts/`.

---

## B-010 — Vale `Microsoft.Foreign` mechanical sweep deferral
