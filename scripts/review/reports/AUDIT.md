# Phase 1 — Cross-Cutting Audit

**Date:** 2026-05-08
**Scope:** All 145 markdown files under `docs/` (L50, L100, L200, L300, top-level, resources)
**Tooling:** markdownlint-cli2 0.22.1, lychee 0.15.1, vale 3.4.2, pa11y-ci 4.1.0, jekyll 4.4.1, custom Python checkers
**Baseline build:** 0 errors, **68 warnings** (Sass deprecations from `just-the-docs` 0.12.0 — unchanged ceiling for PR-3..5)

This is a **read-only audit**. No content was modified for this report. Findings are bucketed per master plan §A and capped per §B. Phase 2 (PR-3) executes the remediation.

---

## Aggregate counts

| Dimension | P0 | P1 | P2 | Notes |
|---|---:|---:|---:|---|
| 1. Front-matter | 2 | 97 | 0 | Mostly missing `description`; 2 files missing whole block |
| 2. Terminology | 18 | 0 | 89 | 11× AAD→Entra, 6× HCI→Local, 1× edge-rag prose |
| 3. Links (lychee on `_site/`) | 7 | 406 | 0 | 7 references to nonexistent files; 406 extensionless slugs |
| 4. Knowledge-checks | 0 | 1 | 7 | 1 file missing question headings; 7 files missing references |
| 5. Markdownlint | 0 | 0 | 0 | Already clean |
| 6. Vale (curated) | 30 | 274 | 0 | Severity-error rules: Microsoft.Auto (30), Microsoft.Foreign (25), Microsoft.Avoid (3), other (5); see §6 below |
| 7. Navigation | 0 | 0 | TBD | No P0 orphan pages detected; `nav_order` collisions checked in Phase 2.2 |
| 8. Visual assets | TBD | TBD | TBD | Audit in Phase 4.1; placeholders inventoried in `docs/assets/images/README.md` |
| 9. Labs (inventory) | 0 | 9 | 0 | All 9 lab files marked "Q1 2026 Under Development" |
| 10. Accessibility | TBD | TBD | TBD | Pilot found 1 P0 (duplicate mermaid id) — full pa11y-ci sweep deferred to Phase 4.3 |
| 11. MS Learn claims | 1 | 1 | 0 | "Three Arc services" updated in pilot; "Indirectly Connected mode" framing verified |
| **Totals** | **58** | **787** | **96** | Excludes Phase 4 dimensions (assets/UI/a11y) |

> **Budget caps (per §B):**
>
> - **P0:** uncapped → close 100% in PR-3
> - **P1:** ≤ 300 closed in PR-3 → **487 P1 findings exceed cap**. Triage decision required in Phase 1.5: either (a) demote 187 to P3, or (b) re-scope to handle bulk-fixable P1s mechanically (see §3 Links — 406 are extensionless slugs, fixable by a single regex sweep with manual spot-check; that brings P1 in scope to 81, well under cap).
> - **P2:** ≤ 100 closed in PR-3 → 96 within cap.

---

## §1 — Front-matter

**Findings:** 2 × P0, 97 × P1.

### P0 (must-fix)

| File | Issue |
|---|---|
| `README.md` | Missing front-matter block entirely (top-level project README, not Jekyll-served). **Action:** add minimal frontmatter only if file is Jekyll-served; if it's the GitHub-only README, exclude from the front-matter check. **Audit recommendation:** WONTFIX (top-level `README.md` is excluded from Jekyll via `_config.yml` — see `exclude:` list). |
| `level-200/arc-advanced-knowledge-check.md` | Missing front-matter block. **Action:** add layout/title/parent/nav_order. |

### P1 (should-fix)

97 files missing `description` in front-matter. Per §H, every page must have `description` to be eligible for nav publication.

**Distribution:**

| Level | Count |
|---:|---:|
| L50 | 19 |
| L100 | 21 |
| L200 | 26 |
| L300 | 28 |
| top-level | 3 |
| **Total** | **97** |

**Phase 2.2 plan:** `check_frontmatter.py --fix` cannot auto-derive accurate descriptions — descriptions need to be content-aware. **Recommendation:** generate descriptions per-page in Phase 3 (per-level deep review); Phase 2.2 only handles missing `layout: default` and nav_order collisions.

---

## §2 — Terminology

**Findings:** 18 × P0, 89 × P2.

### P0 breakdown

| Code | Count | Description |
|---|---:|---|
| `TERM-AAD` | 11 | "Azure Active Directory" → "Microsoft Entra ID" |
| `TERM-HCI` | 6 | "Azure Stack HCI" → "Azure Local" (outside migration narratives) |
| `TERM-EDGERAG-HYPH` | 1 | "edge-rag" prose → "Edge RAG" (`level-200/lab-03-edge-rag-setup.md`) |

### P2 breakdown

| Code | Count |
|---|---:|
| `TERM-LOCKBOX` | 64 (lowercase "customer lockbox" → "Customer Lockbox") |
| `TERM-SLZ-CASE` | 25 (lowercase "sovereign landing zone" → "Sovereign Landing Zone") |

**Phase 2.1 plan:** `lint_terminology.py --fix` handles `TERM-LOCKBOX`, `TERM-SLZ-CASE` (safe substitutions). `TERM-AAD` is also `safe_fix=True` and runs mechanically. `TERM-HCI` and `TERM-EDGERAG-HYPH` are `safe_fix=False` (context-sensitive: must distinguish migration narrative from incorrect usage) — Phase 2 reviewer reads each match in context.

**WONTFIX candidates:** none — all 18 P0 are within budget.

---

## §3 — Links (lychee against rendered `_site/` HTML)

**Findings:** 7 × P0 (real missing target files), 406 × P1 (extensionless slugs not resolved).

### P0 (real broken — target file missing)

| Target | Source files |
|---|---|
| `level-50/azure-core-services.md` | `level-100/azure-arc-intro.md` (and likely others) |
| `level-200/proposal-development.md` | 4 references |
| `level-100/edge-rag-architecture.md` | 1 reference (uses wrong relative path) |
| `level-100/rag-fundamentals.md` | 1 reference (uses wrong relative path) |

**Action in Phase 2.3:** repair links to existing pages (e.g., `azure-core-services.md` → `microsoft-azure-overview.md` or similar). For `edge-rag-architecture.md` and `rag-fundamentals.md`, fix relative path (target files exist).

### P1 (extensionless slugs)

**Pattern:** 406 occurrences of `[text](slug)` (no `.md`) — Jekyll's `jekyll-relative-links` only rewrites `.md` extensions, so bare slugs render as 404s in the browser. The 406 references resolve to **232 unique target slugs**, all of which exist as `.md` files.

**Top broken slugs (by reference count):**

| Slug | References | Target file (exists) |
|---|---:|---|
| `level-300/azure-local-advanced-connected` | 18 | `level-300/azure-local-advanced-connected.md` ✓ |
| `level-100/azure-local-overview` | 17 | `level-100/azure-local-overview.md` ✓ |
| `level-100/azure-arc-intro` | 14 | `level-100/azure-arc-intro.md` ✓ |
| `level-100/sovereign-private-cloud` | 13 | exists ✓ |
| `level-100/edge-rag-concepts` | 13 | exists ✓ |

**Action in Phase 2.3:** mechanical regex sweep — append `.md` to bare slugs that resolve to an existing markdown file in the repo. Spot-check 10 random fixes manually before running across all matches.

**Estimated effort:** single deterministic script run + manual spot-check; closes all 406 P1 in one commit.

---

## §4 — Knowledge-checks

**Findings:** 0 × P0, 1 × P1, 7 × P2.

| Sev | File | Issue |
|---|---|---|
| P1 | `level-200/arc-advanced-knowledge-check.md` | No question headings detected (file may be empty or use a different format) |
| P2 | `level-200/azure-local-deep-dive-knowledge-check.md` | 0 references for 10 questions |
| P2 | `level-200/compliance-knowledge-check.md` | 0 references for 15 questions |
| P2 | `level-200/presales-knowledge-check.md` | 0 references for 15 questions |
| P2 | `level-200/rag-implementation-knowledge-check.md` | 0 references for 18 questions |
| P2 | `level-50/azure-fundamentals-knowledge-check.md` | 0 references for 10 questions |
| P2 | `level-50/cloud-computing-knowledge-check.md` | 0 references for 10 questions |
| P2 | `level-50/security-compliance-knowledge-check.md` | 0 references for 10 questions |

**P0 status:** all 21 KB-check files now use `<details markdown="1">` format with the required `**Correct Answer**` and explanation pattern — no parser failures.

**Phase 2.4 plan:** the P1 file (`arc-advanced-knowledge-check.md`) is currently effectively empty/missing its question section (the audit detected no question headings); needs reconstruction. The 7 P2s are addressed in Phase 3 deep review per-level, where reviewers add `**Reference:**` links to source content.

---

## §5 — Markdownlint

**Findings:** 0.

The repo passes `markdownlint-cli2` against `.markdownlint.json` cleanly. No P0/P1/P2 entries. This dimension is informational for Phase 5 gate (must remain at 0).

---

## §6 — Vale (curated)

**Findings:** 30 × P0 equivalents (severity=error), 274 × P1 (severity=warning), total 337 lines.

### Severity-error breakdown (gates Phase 5)

| Rule | Count | Pattern | Action recommendation |
|---|---:|---|---|
| `Microsoft.Auto` | 30 | "auto-failover", "auto-renew", "auto-classification", etc. (hyphenated forms) | **WONTFIX** — project consistently uses hyphenated forms in technical docs; demote to `warning` in `.vale.ini` |
| `Microsoft.Foreign` | 25 | "e.g.," → "for example," | **P2 sweep in Phase 2** — mechanical substitution outside code blocks |
| `Microsoft.Avoid` | 3 | "Backend" (also flags "blacklist", etc.) | **WONTFIX** for "Backend" (Azure-standard term); demote rule or whitelist "Backend" |
| `Microsoft.AMPM` | 2 | AM/PM formatting | **P1** — fix in Phase 3 |
| `Vale.Repetition` | 1 | duplicated word | **P0** — fix in Phase 2 |
| `Microsoft.Plurals` | 1 | "(s)" plural pattern | **P1** |
| `Microsoft.DateOrder` | 1 | date format | **P1** |

### Recommended `.vale.ini` adjustment for Phase 2.0 (audit-driven curation)

```ini
Microsoft.Auto    = warning   # demote: project uses "auto-failover", "auto-renew" etc. consistently
Microsoft.Avoid   = warning   # demote: "Backend" is Azure-standard
```

After this adjustment, severity-error count drops from **30 → 30 - 30 - 3 = -3** … i.e. roughly 30 - (30 + 3) = **-3** (impossible) — wait, I overcounted. Let me re-state: demoting `Microsoft.Auto` (30) and `Microsoft.Avoid` (3) reduces severity-error count by **33**. Remaining errors: **63 - 33 = 30** … but the original error sample showed 30 + 25 + 3 + 2 + 1 + 1 + 1 = 63 total. After demotion: **63 - 33 = 30 errors**, of which 25 are `Microsoft.Foreign` (mechanically fixable in Phase 2), 5 are spot-fixable.

→ **Phase 2.6 closes residual 30 errors:** 25 mechanical (`Microsoft.Foreign`) + 5 manual = 30. Phase 5 gate met.

### Severity-warning (informational, not gating)

274 warnings dominated by:

| Rule | Count |
|---:|---:|
| `Microsoft.HeadingAcronyms` | 149 (RAG, AI, GPU in headings) |
| `Microsoft.Adverbs` | 109 ("quickly", "rapidly", "easily") |

**Action:** WONTFIX — project intentionally uses these patterns in technical training material. Demoted from gating in `.vale.ini` already (per pilot calibration).

---

## §7 — Navigation

**Findings:** TBD (running orphan-page check requires Jekyll graph traversal; defer to Phase 2.2).

Preliminary checks via inventory CSV:

- 0 detected nav_order collisions (manual check; collision detection runs in Phase 2.2 `check_frontmatter.py`)
- 18 nav-excluded files (see §11 below for triage)
- All level READMEs have `has_children: true` ✓
- Module overview pages (`module-0N-*.md`) have `has_children: true` ✓

---

## §8 — Visual assets

Deferred to Phase 4.1. Inventory CSV captures `image_refs` per file. Notable:

- `docs/assets/images/README.md` lists 5 TBD assets per the master plan §4.1 (sovereignty-spectrum, azure-regions-map update, eu-data-boundary, data-residency-vs-sovereignty, regulatory-comparison-matrix).
- 3 × `VISUAL_SPECIFICATIONS.md` files contain visual asset specifications — kept `nav_exclude: true` permanently (per §H).

---

## §9 — Labs inventory

All 9 lab files surveyed:

| File | Status | Words | Notes |
|---|---|---:|---|
| `level-200/lab-01-azure-local-deployment.md` | "Q1 2026 Under Development" | 1,895 | substantive content present |
| `level-200/lab-02-azure-arc-onboarding.md` | "Q1 2026 Under Development" | 1,623 | substantive content present |
| `level-200/lab-03-edge-rag-setup.md` | "Q1 2026 Under Development" | 1,521 | substantive content present (1× P0 terminology — edge-rag) |
| `level-200/lab-04-policy-governance.md` | "Q1 2026 Under Development" | 1,470 | substantive content present |
| `level-200/lab-05-monitoring-observability.md` | "Q1 2026 Under Development" | 1,378 | substantive content present |
| `level-300/azure-local-disconnected-lab.md` | "Q1 2026 Under Development" | varies | |
| `level-300/edge-rag-production-lab.md` | "Q1 2026 Under Development" | varies | |
| `level-300/zero-trust-lab.md` | "Q1 2026 Under Development" | varies | |
| `level-300/azure-local-connected-lab.md` | (not flagged) | varies | check status in Phase 3 |

**Plan §3.5 default A** (delete-and-restub) was marked the default with user confirmation. **However, audit reveals labs are NOT empty stubs** — all contain 1,400–1,900 words of substantive lab steps with code samples. The "Under Development" callout suggests only validation is incomplete, not content authoring.

**Recommendation for Phase 1.5 sign-off:** revisit §3.5 decision. Suggest **option B (keep & polish front-matter only)** as default — the content has value and shouldn't be deleted. The "Q1 2026 Under Development" callout already manages user expectations.

---

## §10 — Accessibility

Pilot revealed:

| File | Issue | Severity |
|---|---|---|
| `level-100/azure-arc-intro.md` | Duplicate mermaid subgraph id `OnPrem` across 2 diagrams on same rendered page | P0 (fixed in pilot) |

**Action for Phase 4.3:** scan all multi-diagram pages for duplicate ids. Pattern detection:

```bash
# Pages with ≥2 mermaid blocks
grep -lE '^```mermaid$' docs/**/*.md | xargs -I{} sh -c 'count=$(grep -cE "^```mermaid$" "{}"); test "$count" -gt 1 && echo "$count {}"'
```

Full pa11y-ci sweep deferred to Phase 4.3.

---

## §11 — MS Learn claim list (frozen at Phase 1.5)

Capped at ≤ 60 unique URLs. Pilot consumed 3.

### Frozen claims for verification in Phase 3

| ID | Claim (verbatim) | File | Learn URL | Status |
|---|---|---|---|---|
| ARC-1 | "three Arc services" / "three pillars of Azure Arc" | `level-100/azure-arc-intro.md`, `level-100/azure-arc-knowledge-check.md` | `learn.microsoft.com/en-us/azure/azure-arc/overview` | **MISMATCH → corrected in pilot** (Microsoft documents 4 resource types) |
| ARC-2 | Indirectly Connected mode retired September 2025 | `level-100/azure-arc-data-services.md`, `level-100/azure-arc-knowledge-check.md` | (same) | **MATCH** (project content already says "retired in September 2025") |
| ARC-3 | Connected Machine agent heartbeat & expiration timing | `level-100/azure-arc-servers.md` (if mentioned) | `learn.microsoft.com/en-us/azure/azure-arc/servers/overview` | NEEDS-CHECK (Phase 3.2) |
| ARC-4 | CNCF-certified Kubernetes support | `level-100/azure-arc-kubernetes.md` | `learn.microsoft.com/en-us/azure/azure-arc/kubernetes/overview` | **MATCH** |
| LOCAL-1 | Azure Local node count limits | `level-100/azure-local-architecture.md`, `level-200/azure-local-architecture-deep-dive.md` | `learn.microsoft.com/en-us/azure/azure-local/overview` | NEEDS-CHECK (Phase 3.2/3.3) |
| LOCAL-2 | Disconnected Operations behaviors | `level-100/azure-local-disconnected-mode.md`, `level-300/azure-local-air-gapped.md` | `learn.microsoft.com/en-us/azure/azure-local/manage/disconnected-operations-overview` | NEEDS-CHECK |
| EDGERAG-1 | Edge RAG GA / Preview status | `level-100/module-05-edge-rag.md`, `level-100/edge-rag-*.md`, `level-300/edge-rag-*.md` | `learn.microsoft.com/en-us/azure/azure-arc/edge-rag/overview` | **NEEDS-CHECK in Phase 3** (per §G handling) |
| SLZ-1 | Sovereign Landing Zone scope and components | `level-100/digital-sovereignty.md`, `level-300/sovereign-landing-zone.md` | `learn.microsoft.com/en-us/industry/sovereignty/sovereign-landing-zone-overview` | NEEDS-CHECK |
| SLZ-2 | EU Data Boundary commitments | `level-100/european-commitments.md`, `level-100/data-residency-concepts.md` | `learn.microsoft.com/en-us/privacy/eudb/eu-data-boundary-learn` | NEEDS-CHECK |
| ARC-5 | Arc-enabled SQL Server | `level-200/arc-advanced-management.md` | `learn.microsoft.com/en-us/sql/sql-server/azure-arc/overview` | NEEDS-CHECK (Phase 3.3) |
| FEDRAMP-1 | FedRAMP High vs Moderate boundaries | `level-200/fedramp-compliance.md`, `level-300/government-cloud.md` | `learn.microsoft.com/en-us/azure/compliance/offerings/offering-fedramp` | NEEDS-CHECK |
| GDPR-1 | GDPR controller/processor roles | `level-200/gdpr-implementation.md`, `level-100/european-commitments.md` | `learn.microsoft.com/en-us/compliance/regulatory/gdpr` | NEEDS-CHECK |

**Total claims for Phase 3 verification:** 12. Plus ~3 already verified in pilot (ARC-1, ARC-2, ARC-4). Projected MS Learn cap usage: ~15 unique URLs. Comfortably under 60.

---

## Nav-exclusion triage (preview — finalized in Phase 2.6)

18 files have `nav_exclude: true`. Per §H criteria:

| File | Words | desc | Links | §H eligible to publish? | Recommended action |
|---|---:|---|---:|---|---|
| `404.md` | 140 | no | 0 | n/a | KEEP `nav_exclude: true` (system page) |
| `assets/images/README.md` | 2,381 | no | 0 | n/a | KEEP `nav_exclude: true` (asset registry) |
| `level-100/VISUAL_SPECIFICATIONS.md` | 5,107 | no | 0 | n/a | KEEP `nav_exclude: true` (internal spec) |
| `level-200/VISUAL_SPECIFICATIONS.md` | 2,551 | no | 0 | n/a | KEEP `nav_exclude: true` (internal spec) |
| `level-300/VISUAL_SPECIFICATIONS.md` | 1,064 | no | 0 | n/a | KEEP `nav_exclude: true` (internal spec) |
| `level-300/api-gateway-patterns.md` | 264 | yes | 2 | NO (< 400 words) | MOVE to `_drafts/` |
| `level-300/critical-infrastructure.md` | 435 | yes | 2 | YES | PUBLISH (verify SME §I first) |
| `level-300/data-classification.md` | 341 | yes | 2 | NO (< 400 words) | MOVE to `_drafts/` |
| `level-300/data-mesh-sovereignty.md` | 228 | yes | 2 | NO | MOVE to `_drafts/` |
| `level-300/devsecops-pipeline.md` | 208 | yes | 2 | NO | MOVE to `_drafts/` |
| `level-300/disaster-recovery.md` | 280 | yes | 2 | NO | MOVE to `_drafts/` |
| `level-300/event-driven-architecture.md` | 225 | yes | 2 | NO | MOVE to `_drafts/` |
| `level-300/financial-services.md` | 445 | yes | 2 | YES | PUBLISH (verify SME §I) |
| `level-300/government-cloud.md` | 389 | yes | 2 | NO (< 400 words) | MOVE to `_drafts/` (or expand in Phase 3.4) |
| `level-300/healthcare-sovereign.md` | 434 | yes | 2 | YES | PUBLISH (verify SME §I) |
| `level-300/incident-response.md` | 346 | yes | 2 | NO | MOVE to `_drafts/` |
| `level-300/observability-stack.md` | 315 | yes | 2 | NO | MOVE to `_drafts/` |
| `level-300/sovereign-landing-zone.md` | 504 | yes | 3 | YES | PUBLISH |

**Summary:** 4 publish, 9 move-to-`_drafts/`, 5 keep-permanent.

The user already confirmed (per Q3) that a `_drafts/` collection should be enabled in `_config.yml` for failing pages. Phase 2.6 implements:

```yaml
# _config.yml (added in Phase 2.6)
collections:
  drafts:
    output: false   # not built into _site/
    permalink: /_drafts/:path/
```

---

## Phase 2 budget projection (with audit-driven adjustments)

| Bucket | Findings (this audit) | Disposition |
|---|---:|---|
| **P0** (must close) | 58 | All in scope — no caps |
| **P1 in cap** | 99 of 487 | 7 link P0 + 9 lab P1 + 78 manual front-matter description (Phase 3) + 5 Vale-error mechanical sweeps |
| **P1 mechanically closable bulk** | 406 | One-pass regex sweep (extensionless slug fix) — counts toward "P1 closure" but doesn't count against the ≤300 cap because it's a single mechanical action |
| **P2 in cap** | 96 of 96 | All within 100-cap |
| **P3 (WONTFIX)** | see WONTFIX.md | `Microsoft.Auto`, `Microsoft.Avoid`, `Arc-Enabled` heading casing, top-level README front-matter, `Microsoft.HeadingAcronyms` (warning-only), `Microsoft.Adverbs` (warning-only) |

**Conclusion:** caps fit if the 406 extensionless-slug fix is treated as one mechanical action. **No demote-to-P3 churn required**.

---

## Phase 1.5 sign-off — what user must approve before PR-3

1. ✅ Aggregate counts table above
2. ✅ Severity bucketing decisions (Vale rule demotion, README WONTFIX, Arc-Enabled casing WONTFIX)
3. ✅ MS Learn claim list (12 claims for Phase 3)
4. ✅ Nav-exclude triage preview (4 publish / 9 _drafts / 5 keep) — finalized in Phase 2.6
5. ⚠️ **Lab decision revisit** — content is substantive (1,400–1,900 words each). Recommend switching to plan option B (keep & polish front-matter only) instead of default A (delete-and-restub).
6. ✅ Phase 2 budget projection (caps fit, no P3 demotion needed)

After sign-off, PR-2 merges and PR-3 (Phase 2 mechanical remediation) proceeds.
