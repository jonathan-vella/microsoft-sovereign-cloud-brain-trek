# Phase 4 Designer Quick Start Guide

**Start Here:** This 5-minute guide gets you oriented for Phase 4 asset creation.

---

## What You're Building

Create **20 production SVG diagrams** for the Microsoft Sovereign Cloud Brain Trek Level 200 content.

- **Assets:** 21-40 (Advanced topics for architects and solution professionals)
- **Format:** SVG (scalable, web-ready)
- **Deadline:** 30-34 hours over 3-4 weeks
- **Directory:** `docs/assets/images/level-200/`

---

## The 4-Step Workflow

### 1️⃣ Preparation (1 hour - Do First!)

Read these documents in order:

1. **`.github/VISUAL_ASSET_PROCESS.md`** (25.8 KB)
   - Overview of 3-step workflow
   - Pages 750-850: Design Standards (Microsoft brand, accessibility, SVG best practices)

2. **`docs/level-200/VISUAL_SPECIFICATIONS.md`** (8 KB)
   - Detailed specs for all 20 assets (Assets 21-40)
   - Each asset has 7 sections: Context, Constraints, Content, Visuals, Wireframe, Criteria, Learn Adaptation

3. **`docs/assets/images/README.md`** (59.3 KB)
   - Master asset registry with metadata
   - Design guidelines, color palette, typography standards

### 2️⃣ Create SVGs (24-28 hours)

For each asset:

1. Read the specification in `docs/level-200/VISUAL_SPECIFICATIONS.md`
2. Create wireframe using "Wireframe Guidance" section
3. Design SVG following "Visual Elements" requirements
4. Validate against "Acceptance Criteria" (7-10 checkpoints)
5. Save to: `docs/assets/images/level-200/asset-[##]-[name].svg`

**Design Standards:**
- Canvas: 1200x800px (adjust per asset)
- Colors: Microsoft brand palette (documented)
- Fonts: Arial, Segoe UI (web-safe)
- Optimization: Valid SVG, < 100KB, web-ready

### 3️⃣ Quality Validation (2-3 hours)

For each completed asset:

- ✅ Self-review against acceptance criteria
- ✅ Technical check: SVG syntax, file size, browser compatibility
- ✅ Brand alignment: Colors, typography, style consistency
- ✅ Accessibility: Text contrast, semantic markup, screen reader support
- ✅ Content accuracy: Verified by SME

### 4️⃣ Delivery (2-4 hours)

- 📁 Save 20 SVG files to `docs/assets/images/level-200/`
- 📝 Update `docs/assets/images/README.md` status to "🟢 Available"
- ✅ Verify placeholder callouts in content resolve to SVG paths
- 📋 Document any deviations from specifications

---

## Assets at a Glance

### Module 1: Azure Local Advanced (3 assets)
- **Asset 21:** Advanced Networking Topology (RDMA, teaming, VLANs)
- **Asset 22:** HA Failover Scenarios (quorum, failover mechanisms)
- **Asset 23:** Hardware Planning Matrix (CPU/memory/storage comparison)

### Module 2: Azure Arc Advanced (3 assets)
- **Asset 24:** Arc Governance Framework (policy, compliance, multi-cloud)
- **Asset 25:** Cost Optimization Flowchart (strategies and decisions)
- **Asset 26:** Enterprise Patterns Diagram (hub-spoke, zero-trust, federation)

### Module 3: Edge RAG Implementation (5 assets)
- **Asset 27:** RAG Production Architecture (end-to-end pipeline)
- **Asset 28:** LLM Deployment Options (edge inference patterns)
- **Asset 29:** Vector Database Integration (embedding storage)
- **Asset 30:** Deployment Topology (multi-node RAG setup)
- **Asset 31:** Monitoring & Observability (metrics, logging, alerting)

### Module 4: Pre-Sales Solution Design (3 assets)
- **Asset 32:** Customer Discovery Framework (requirements, assessment)
- **Asset 33:** Solution Sizing Worksheet (capacity planning visual)
- **Asset 34:** TCO Analysis Dashboard (multi-year cost projection)

### Module 5: Compliance & Security (4 assets)
- **Asset 35:** GDPR Compliance Checklist (residency, consent, retention)
- **Asset 36:** FedRAMP Authorization Path (levels, audit, boundaries)
- **Asset 37:** Encryption & Key Management (hierarchy, rotation, access)
- **Asset 38:** Zero-Trust Security Model (identity-first, verification, microsegmentation)

### Module 6: Hands-On Labs (2 assets)
- **Asset 39:** Lab Progression Roadmap (sequential learning path)
- **Asset 40:** Lab Cost-Time Matrix (time and cost estimates)

---

## Timeline

| Week | Hours | Task |
|------|-------|------|
| **1** | 4-6 | Read all reference docs & prepare workspace |
| **2** | 10-12 | Create Assets 21-30 (Batch 1) |
| **3** | 10-12 | Create Assets 31-40 (Batch 2) + refinement |
| **4** | 2-4 | Delivery & final checks |

**Total:** 30-34 hours over 3-4 weeks

---

## Files You'll Need

| File | Purpose | Size |
|------|---------|------|
| VISUAL_ASSET_PROCESS.md | Design standards & best practices | 25.8 KB |
| VISUAL_SPECIFICATIONS.md | 20 asset design briefs | 8 KB |
| README.md (assets) | Brand guidelines, asset registry | 59.3 KB |
| Content files (34 .md) | Context for asset placement | Show where assets are used |

---

## Quality Checklist (Per Asset)

✅ **Specification Compliance**
- [ ] All elements from "Content Requirements" included
- [ ] Visual elements match specification
- [ ] Layout follows Wireframe Guidance

✅ **Technical Requirements**
- [ ] Valid SVG syntax
- [ ] File size < 100 KB
- [ ] Renders in modern browsers
- [ ] Responsive zoom levels

✅ **Brand & Accessibility**
- [ ] Microsoft brand colors
- [ ] Standard typography (Arial, Segoe UI)
- [ ] WCAG AA text contrast (4.5:1)
- [ ] Semantic SVG structure

✅ **Content Accuracy**
- [ ] Diagram matches specification
- [ ] Labels clear and readable
- [ ] Relationships properly visualized
- [ ] Technical accuracy (SME verified)

✅ **Acceptance Criteria**
- [ ] All 7-10 criteria from spec met
- [ ] Performance benchmarks achieved
- [ ] No known issues

---

## Key Decisions

### Color Palette
Use Microsoft brand colors documented in `VISUAL_ASSET_PROCESS.md`:
- Primary: Microsoft Blue
- Secondary: Microsoft Gray
- Accent colors: As documented

### Typography
- **Headers:** Arial Bold or Segoe UI Bold
- **Body:** Arial Regular or Segoe UI Regular
- **Sizes:** Per wireframe guidance

### Canvas Sizes
Default: 1200x800px  
Adjust per asset wireframe guidance (some may be 1200x900, 1200x750, etc.)

---

## File Naming Convention

**Format:** `asset-[##]-[descriptive-name].svg`

**Examples:**
- `asset-21-advanced-networking-topology.svg`
- `asset-22-ha-failover-scenarios.svg`
- `asset-27-rag-production-architecture.svg`

---

## Where to Save

```
docs/assets/images/level-200/
├── asset-21-*.svg
├── asset-22-*.svg
├── ...
└── asset-40-*.svg
```

**Important:** Must be in `level-200/` subdirectory (NOT in `level-100/`)

---

## Success Criteria

✅ All 20 assets created  
✅ Files saved to correct directory  
✅ Each asset passes acceptance criteria  
✅ Design standards followed  
✅ README.md status updated to "🟢 Available"  
✅ Ready for Jekyll/GitHub Pages deployment

---

## Questions?

**For specifications:** See `docs/level-200/VISUAL_SPECIFICATIONS.md`  
**For design standards:** See `VISUAL_ASSET_PROCESS.md` pages 750-850  
**For brand guidelines:** See `docs/assets/images/README.md`  
**For content context:** Review "Used In" references in asset registry

---

## Next Step

👉 **Start with Step 1:** Read `.github/VISUAL_ASSET_PROCESS.md` (design standards sections)

Then proceed to `docs/level-200/VISUAL_SPECIFICATIONS.md` and begin asset creation.

**Estimated completion:** 3-4 weeks at 30-34 hours total effort

---

**Ready to create 20 amazing SVG diagrams? Let's go!** 🚀
