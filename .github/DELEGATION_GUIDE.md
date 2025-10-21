# GitHub Copilot Coding Agent - Delegation Guide

**Project:** Microsoft Sovereign Cloud Brain Trek  
**Phase:** 2, 3, 4 (Visual Asset Alignment Continuation)  
**Last Updated:** October 21, 2025  
**Status:** ✅ Phase 1 Complete - Ready for Phase 2-4 Delegation  

---

## 📋 Quick Reference

| Phase | Task | Time | Owner | Status |
|-------|------|------|-------|--------|
| **Phase 1** | Documentation + Process | 0.5 hrs | ✅ Complete | DONE |
| **Phase 2** | Detailed Specifications (Step #1) | 1-2 hrs | GitHub Copilot Agent | ⏳ READY |
| **Phase 3** | Placeholder Integration (Step #2) | 2-3 hrs | GitHub Copilot Agent | ⏳ QUEUED |
| **Phase 4** | Asset Creation (Step #3) | 30-34 hrs | 🔴 External Design Team | FUTURE |

---

## 🎯 Phase 1 Summary: What's Been Done

**Completed October 21, 2025 (30 minutes)**

### ✅ Deliverables

1. **Visual Asset Process Documentation** (`.github/VISUAL_ASSET_PROCESS.md` - 25.8 KB)
   - Complete 3-step mandatory workflow with full instructions
   - Quality checklists per step (8-10 items each)
   - Reusable templates and design standards
   - Level 300+ instructions included

2. **Level 200 Visual Assets Registry** (`docs/assets/images/README.md` - extended 59.3 KB total)
   - 20 Level 200 visual asset specifications (Assets 21-40)
   - Complete metadata: file, priority, description, content, visual elements, size, used-in, sources
   - Module-by-module organization (6 modules)

3. **Project Status Reports**
   - `VISUAL_ASSETS_ALIGNMENT_SUMMARY.md` (11.4 KB) - Status + alignment matrix
   - `PHASE_1_COMPLETION_REPORT.md` (12.5 KB) - Executive summary
   - Updated `README.md` with process integration

4. **Delegation Instructions**
   - Updated `copilot-instructions.md` with Phase 2-4 guidance
   - This file: `DELEGATION_GUIDE.md` - Detailed handoff instructions

### 🎯 Context Established

- **Level 100:** 20 visual assets documented (all modules complete)
- **Level 200:** 20 visual assets documented (all modules complete)
- **Total:** 40 visual assets fully specified with metadata
- **Priority Distribution:** High (17), Medium (20), Low (3)
- **Process:** Standardized 3-step workflow with templates for reuse

---

## 🚀 Phase 2: Detailed Visual Specifications

### 📌 Task Description

Execute **Step #1** from `.github/VISUAL_ASSET_PROCESS.md` to expand brief asset specifications into detailed briefs with wireframes, design constraints, and acceptance criteria.

### 📂 Key Reference Files

**Primary:** `.github/VISUAL_ASSET_PROCESS.md` - Read Step #1 section (lines ~500-750)
- Detailed instructions (what to create per asset)
- Quality checklist (8 items)
- Specification template (reusable format)
- Wireframe guidelines

**Asset Registry:** `docs/assets/images/README.md`
- Level 200 section: Assets 21-40 with current brief specs
- Use these as input for expanded specifications

**Content Context:** `docs/level-200/` (all 34 markdown files)
- Understand content structure and asset usage patterns
- Review where visual assets will be integrated

### ✅ Acceptance Criteria

For **each of the 20 Level 200 assets (21-40)**:

- [ ] Asset has expanded specification with 3-5 paragraphs of detail
- [ ] Specification includes:
  - **Context**: Why this asset matters, where it fits in learning flow
  - **Design Constraints**: Technical limitations, style requirements
  - **Content Requirements**: Specific elements, labels, data to show
  - **Visual Elements**: Colors, icons, layout guidance
  - **Acceptance Criteria**: How to know the asset is done correctly
  - **Wireframe Guidance**: ASCII sketch or layout description
  - **Microsoft Learn Adaptation**: How to adapt from official sources
  
- [ ] Specification follows VISUAL_ASSET_PROCESS.md template format
- [ ] All specifications use consistent structure and terminology
- [ ] Quality checklist from VISUAL_ASSET_PROCESS.md is satisfied

### 📤 Output

**Create or Update One File:**

```
docs/level-200/VISUAL_SPECIFICATIONS.md
```

**File Structure (recommended):**

```markdown
# Level 200 Visual Asset Specifications

**Purpose:** Detailed briefs for all 20 Level 200 visual assets (Assets 21-40)  
**Created:** [Date]  
**Asset Registry:** See `docs/assets/images/README.md` for full metadata

---

## Module 1: Azure Local Architecture Deep Dive

### Asset 21: Advanced Networking Architecture

**Context:**  
[2-3 paragraphs explaining why this asset matters]

**Design Constraints:**  
[Technical and style limitations]

**Content Requirements:**  
- [Bulleted list of specific elements to show]

**Visual Elements:**  
[Colors, icons, layout descriptions]

**Wireframe Guidance:**
[ASCII sketch or descriptive layout]

**Acceptance Criteria:**  
- [ ] Shows SET configuration with multiple NICs clearly labeled
- [ ] VLAN colors match color palette (blue/orange/green)
- [ ] RDMA paths visually distinguished from regular network
- [Additional 3-5 acceptance criteria]

**Microsoft Learn Adaptation:**  
[How to adapt from official Microsoft sources]

---

### Asset 22: High-Availability Architecture

[Repeat structure for each asset...]

---

## Module 2: Arc Advanced Management

[Continue for all 20 assets...]
```

### 📊 Scale & Time Estimate

- **20 assets** × 3-5 min per specification = **60-100 minutes**
- Plus template consistency validation = **1-2 hours total**

### ✋ Stop Point for Validation

**Before proceeding to Phase 3**, user should:
1. Review output `docs/level-200/VISUAL_SPECIFICATIONS.md`
2. Validate quality against VISUAL_ASSET_PROCESS.md checklist
3. Confirm specifications are sufficient for design team
4. Approve or request adjustments

---

## 🔄 Phase 3: Content Placeholder Integration

### 📌 Task Description

Execute **Step #2** from `.github/VISUAL_ASSET_PROCESS.md` to add visual asset placeholder callouts to all 34 Level 200 markdown content files.

### 📂 Key Reference Files

**Primary:** `.github/VISUAL_ASSET_PROCESS.md` - Read Step #2 section (lines ~750-1000)
- Detailed instructions for integration
- Quality checklist (8 items)
- **3 placeholder format examples** (choose one consistently)
- Integration examples

**Asset Registry:** `docs/assets/images/README.md`
- Asset 21-40 specifications for reference during integration
- See "Used In" field to identify which files need placeholders

**Content Files to Update:** `docs/level-200/*.md` (34 files total)
- Files listed in asset "Used In" fields
- Review content structure to find optimal placeholder locations

### ✅ Acceptance Criteria

For **each of the 34 Level 200 markdown files**:

- [ ] File has been reviewed for visual asset integration points
- [ ] Each identified integration point has a placeholder callout added
- [ ] Placeholder uses one of 3 consistent formats from VISUAL_ASSET_PROCESS.md
- [ ] Placeholder references specific asset number and name
- [ ] Placeholder includes figure caption
- [ ] Placeholder is placed immediately before or after relevant section
- [ ] All 20 assets (21-40) are referenced in at least one file
- [ ] No orphaned assets (all assets appear in content files)

### 📋 Placeholder Format (Choose One Consistently)

**Format Option 1: Simple Callout Box**
```markdown
> **📊 Visual Reference: Asset [#] - [Asset Name]**  
> *Placeholder - See docs/assets/images/README.md#asset-[#]*  
> [1-2 sentence description of what diagram shows]
```

**Format Option 2: Comment-Based Marker**
```markdown
<!-- VISUAL ASSET NEEDED: Asset [#] - [Asset Name] -->
<!-- Location: This diagram should appear after the [section name] paragraph -->
<!-- Description: [What the visual shows] -->
```

**Format Option 3: Structured Note**
```markdown
**Figure [#]: [Asset Name]**  
*Status: Diagram needed - See docs/assets/images/README.md#asset-[#]*

[Brief explanation of what this diagram will show]
```

### 📂 Files to Update (34 total in `docs/level-200/`)

**Module 1 Files (5 files):**
- azure-local-architecture-deep-dive.md → Assets 21-23
- azure-local-hardware-planning.md → Asset 23
- azure-local-ha-patterns.md → Asset 22
- azure-local-advanced-networking.md → Asset 21
- azure-local-deep-dive-quiz.md → Optional Assets 21-23

**Module 2 Files (5 files):**
- arc-policy-and-governance.md → Asset 24
- arc-cost-optimization.md → Asset 25
- arc-enterprise-patterns.md → Asset 26
- arc-advanced-management.md → Assets 24-26
- arc-advanced-quiz.md → Optional Assets 24-26

**Module 3 Files (6 files):**
- edge-rag-implementation.md → Assets 27-28
- llm-inference-optimization.md → Asset 28
- vector-databases-edge.md → Asset 29
- rag-deployment-strategies.md → Assets 27, 30
- rag-operations-monitoring.md → Asset 31
- rag-implementation-quiz.md → Optional Assets 27-31

**Module 4 Files (3 files):**
- customer-discovery.md → Asset 32
- solution-sizing.md → Asset 33
- presales-solution-design.md → Assets 32-34

**Module 5 Files (4 files):**
- gdpr-implementation.md → Asset 35
- fedramp-compliance.md → Asset 36
- encryption-key-management.md → Asset 37
- compliance-security-patterns.md → Assets 35-38

**Module 6 Files (2 files):**
- labs-overview.md → Assets 39-40
- lab-*-*.md files → Assets 39-40

**Other Files (9 files):**
- cost-estimation.md → Asset 34
- compliance-quiz.md → Assets 35-38
- presales-quiz.md → Assets 32-34
- README.md → General overview placeholders
- [5 other support files]

### 📊 Scale & Time Estimate

- **34 files** × 3-5 placeholders per file = **~100-170 placeholders**
- Plus file update validation = **2-3 hours total**

### ✋ Stop Point for Validation

**Before proceeding to Phase 4**, user should:
1. Verify all 34 files have been updated
2. Confirm all 20 assets (21-40) are referenced
3. Check placeholder consistency across files
4. Approve for handoff to design team

---

## 🎨 Phase 4: Visual Asset Creation (External - Design Team)

### 📌 Task Description

Professional designer creates SVG files for all 20 Level 200 visual assets using Phase 2-3 specifications and placeholders.

**Status:** 🔴 NOT YET DELEGATED (Pending Phase 2-3 completion)

### 📦 Designer Handoff Package

When ready to delegate to design team, provide:

1. **Process Document:** `.github/VISUAL_ASSET_PROCESS.md`
   - Complete design guidelines (Step #3, lines ~1000-1200)
   - Design standards and accessibility requirements
   - Recommended tools and resources
   - Quality gates and review process

2. **Asset Specifications:** `docs/assets/images/README.md` + `docs/level-200/VISUAL_SPECIFICATIONS.md`
   - Complete metadata for all 20 assets (21-40)
   - Detailed specifications from Phase 2 output
   - "Used In" references showing context

3. **Content Context:** All 34 Level 200 markdown files (with Phase 3 placeholders)
   - Designers see where assets are integrated
   - Placeholders show exact figure locations
   - Content provides context for design

4. **Design Deliverables:** Checklist
   - Create SVG files in `docs/assets/images/level-200/` directory
   - Name files: `level-200/[descriptive-name].svg`
   - Follow design standards (color palette, typography, accessibility)
   - Validate with SMEs for technical accuracy
   - Update README.md status: 🟡 In Progress → 🟢 Available

### 📊 Design Metrics

- **20 assets** × 1.5-2 hours per asset = **30-40 hours**
- Average: **35 hours** (approximately 4-5 design days)
- Estimate: **3-4 weeks** with typical design availability

---

## 📞 How to Delegate Each Phase

### For Phase 2 (Detailed Specifications)

**Invoke GitHub Copilot Coding Agent with:**

```
Please execute Phase 2 of the Visual Asset Alignment project:

Task: Create detailed visual asset specifications for Level 200 diagrams (Assets 21-40)

Reference Documents:
- Primary instructions: .github/VISUAL_ASSET_PROCESS.md (Step #1 section)
- Asset registry: docs/assets/images/README.md (Level 200 section)
- Context files: docs/level-200/*.md (all content files)

Deliverable: 
- Create or update: docs/level-200/VISUAL_SPECIFICATIONS.md
- Include detailed briefs for all 20 assets (21-40)
- Follow template and quality checklist from VISUAL_ASSET_PROCESS.md

Output format:
- File: docs/level-200/VISUAL_SPECIFICATIONS.md
- Structure: By module, one section per asset
- Completeness: All 20 assets with full specification details
```

### For Phase 3 (Placeholder Integration)

**Invoke GitHub Copilot Coding Agent with:**

```
Please execute Phase 3 of the Visual Asset Alignment project:

Task: Integrate visual asset placeholders into Level 200 content files (Step #2)

Reference Documents:
- Primary instructions: .github/VISUAL_ASSET_PROCESS.md (Step #2 section)
- Asset specifications: docs/assets/images/README.md + docs/level-200/VISUAL_SPECIFICATIONS.md
- Content files: docs/level-200/*.md (34 files total)

Deliverable:
- Update all 34 Level 200 markdown files
- Add placeholder callouts for 20 visual assets (21-40)
- Use consistent placeholder format from VISUAL_ASSET_PROCESS.md
- Place placeholders at logical content integration points

Output format:
- Files: All docs/level-200/*.md files updated
- Placeholders: One of 3 consistent formats (choose one)
- Coverage: All 20 assets referenced, no orphaned assets
- Quality: Follow Step #2 quality checklist from VISUAL_ASSET_PROCESS.md
```

### For Phase 4 (Design Team Handoff)

**Prepare and Share:**

1. Send `.github/VISUAL_ASSET_PROCESS.md` as primary reference
2. Attach `docs/assets/images/README.md` for asset metadata
3. Attach `docs/level-200/VISUAL_SPECIFICATIONS.md` for detailed briefs
4. Include all 34 Level 200 markdown files showing placeholder context
5. Specify file naming convention: `level-200/[descriptive-name].svg`
6. Provide color palette and typography guidelines from VISUAL_ASSET_PROCESS.md

---

## 🔍 Quality Gates

### Phase 2 Sign-Off

User verification before Phase 3:
- ✅ Specification file created/updated with all 20 assets
- ✅ Each specification includes context, constraints, requirements, visual elements, wireframe guidance, acceptance criteria
- ✅ Specifications follow consistent template format
- ✅ Specifications are detailed enough for designer to understand intent

### Phase 3 Sign-Off

User verification before Phase 4:
- ✅ All 34 files have been updated
- ✅ All 20 assets (21-40) are referenced in content
- ✅ No asset is orphaned (each appears in at least one file)
- ✅ Placeholder format is consistent across all files
- ✅ Placeholders are placed at logical content locations
- ✅ Placeholder references match asset names and numbers

### Phase 4 Delivery

Designer sign-off:
- ✅ All 20 SVG files created and named correctly
- ✅ Files placed in `docs/assets/images/level-200/` directory
- ✅ Design follows brand guidelines and color palette
- ✅ Technical accuracy validated with SMEs
- ✅ Accessibility standards met (color contrast, alt text)
- ✅ README.md status updated: 🟡 → 🟢 Available

---

## 📚 Key Document Locations

| Document | Purpose | Size | Location |
|----------|---------|------|----------|
| VISUAL_ASSET_PROCESS.md | Complete 3-step workflow | 25.8 KB | `.github/VISUAL_ASSET_PROCESS.md` |
| Visual Assets Registry | 40 asset specs (L100+L200) | 59.3 KB | `docs/assets/images/README.md` |
| Phase 2 Output | Detailed specifications (create) | ~10 KB | `docs/level-200/VISUAL_SPECIFICATIONS.md` |
| Copilot Instructions | Project tracking & delegation | ~20 KB | `.github/copilot-instructions.md` |
| Delegation Guide | This file | ~15 KB | `.github/DELEGATION_GUIDE.md` |
| Status Report | Phase 1 completion summary | 11.4 KB | `VISUAL_ASSETS_ALIGNMENT_SUMMARY.md` |
| Completion Report | Executive summary | 12.5 KB | `PHASE_1_COMPLETION_REPORT.md` |

---

## 🎯 Success Criteria

### Overall Project Success

- ✅ Phase 1: Documentation + process codification (COMPLETE)
- ✅ Phase 2: 20 detailed visual specifications created
- ✅ Phase 3: Placeholders integrated into all 34 Level 200 files
- ✅ Phase 4: 20 production SVG assets created and deployed
- ✅ Level 200 content fully aligned with Level 100 visual standards
- ✅ Process documented for reuse on Level 300+ modules

### Delegation Readiness

- ✅ Clear task definitions with reference documentation
- ✅ Acceptance criteria specified for each phase
- ✅ File locations and naming conventions documented
- ✅ Quality gates established and communicated
- ✅ Handoff between phases defined and validated
- ✅ Context sufficient for independent execution

---

## 📞 Questions or Issues?

Refer to:
- `.github/VISUAL_ASSET_PROCESS.md` - Primary reference for all phases
- `.github/copilot-instructions.md` - Project context and progress tracking
- `VISUAL_ASSETS_ALIGNMENT_SUMMARY.md` - Current project status
- This file (`DELEGATION_GUIDE.md`) - Phase-by-phase breakdown

**Last Updated:** October 21, 2025  
**Next Review:** After Phase 2 completion  
**Project Owner:** [Contact info]

