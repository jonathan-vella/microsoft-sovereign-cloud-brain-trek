# Visual Asset Creation Process

## Overview

This document codifies the **3-step mandatory workflow** for creating visual assets (diagrams, architecture illustrations, infographics) for the Microsoft Sovereign Cloud Brain Trek documentation.

**Why this process matters:**
- Ensures consistency across all documentation levels
- Establishes single source of truth for asset requirements
- Prevents rework and miscommunication between content creators and designers
- Enables efficient asset prioritization and reuse across levels
- Scales effectively for Level 300 and future content

---

## The 3-Step Workflow

### Step #3: Documentation/Specification Phase ← START HERE
**Owner:** Content Creator  
**Timeline:** 30 minutes per level  
**Deliverable:** Comprehensive asset specifications in `docs/assets/images/README.md`

#### What to Do

1. **Add Level Section** to `docs/assets/images/README.md`
   - Create new section: `## LEVEL [X] - [LEVEL NAME]: VISUAL ASSETS`
   - Organize by module within the level

2. **Document Every Visual Asset** using template:
   ```markdown
   #### Asset [#]: [Asset Name]
   **File:** `level-[#]/[descriptive-name].svg`  
   **Priority:** High | Medium | Low  
   **Status:** 🔴 Needed

   **Description:** [1-2 sentence overview]

   **Content:**
   - Bullet list of what diagram shows
   - All components or concepts included
   - Data flows or relationships depicted

   **Visual Elements:**
   - Design elements used (boxes, arrows, icons, etc.)
   - Color coding scheme
   - Layout structure

   **Size:** [Width]x[Height]px

   **Used In:**
   - `docs/level-[#]/[file1].md`
   - `docs/level-[#]/[file2].md`

   **Source Refs:** [Links to Microsoft Learn or references]
   ```

3. **Update Summary Table** in README
   ```markdown
   ### Total Level [X] Assets: [Count] diagrams
   - **Module 1:** # assets
   - **Module 2:** # assets
   - etc.
   ```

4. **Update Project Summary** at end of README
   - Total assets documented
   - Priority distribution
   - Estimated creation hours (assume 0.7-0.9 hrs per diagram)

#### Quality Checklist for Step #3

- [ ] All assets required for the level are documented
- [ ] Each asset has complete metadata (file, priority, status, description)
- [ ] Asset placement in content files is specified ("Used In" section)
- [ ] Priority levels are realistically assigned (High = core, Medium = supporting, Low = supplementary)
- [ ] Source references link to official Microsoft documentation where applicable
- [ ] Visual elements are clearly described (colors, layout, icons)
- [ ] Estimated sizing is realistic for content context
- [ ] Summary tables are updated with new counts
- [ ] README markdown passes linting (expected MD022, MD032 for list formatting)

#### Example from Current Project

**Level 100 Assets (20 diagrams documented)**
- Module 1: 7 assets
- Module 2: 3 assets
- Module 3: 3 assets
- Module 4: 3 assets
- Module 5: 4 assets
- **Status:** 100% specifications complete, 0% created

**Level 200 Assets (20 diagrams documented)**
- Module 1: 3 assets
- Module 2: 3 assets
- Module 3: 5 assets
- Module 4: 3 assets
- Module 5: 4 assets
- Module 6: 2 assets
- **Status:** 100% specifications complete, 0% created

---

### Step #1: Detailed Specification Phase
**Owner:** Content Creator / Solution Architect  
**Timeline:** 1-2 hours per level  
**Deliverable:** `docs/level-[#]/VISUAL_SPECIFICATIONS.md` (optional but recommended)

#### What to Do

1. **Create Detailed Asset Brief** for each diagram
   - Expand each README specification into full brief
   - Include business context and learning objectives
   - Add acceptance criteria for design quality
   - Reference actual content snippets where diagram will be used

2. **Develop Wireframe or Mockup** (recommended)
   - Sketch basic layout and component placement
   - Show key relationships and data flows
   - Validate against content requirements
   - Gather feedback from content reviewers

3. **Define Design Constraints**
   - Brand alignment (Microsoft colors, Segoe UI typography)
   - Accessibility requirements (color-blind friendly, sufficient contrast, alt text)
   - File size optimization goals
   - Responsive scaling for different screen sizes

4. **Create Prioritization Matrix**
   - Identify critical vs. nice-to-have assets
   - Estimate time and resource requirements
   - Recommend creation order (typically High → Medium → Low priority)

#### Quality Checklist for Step #1

- [ ] Each asset has expanded context and learning objectives
- [ ] Wireframes/mockups created for complex diagrams
- [ ] Microsoft brand guidelines reviewed and noted
- [ ] Accessibility requirements documented
- [ ] Design constraints clearly specified
- [ ] Creation prioritization clear and defensible
- [ ] Estimated hours realistic for each asset type
- [ ] Sources and references verified and accessible
- [ ] Content cross-references validated (all "Used In" files exist)
- [ ] Designer feedback incorporated (if applicable)

#### Deliverable Template

Create optional file: `docs/level-[#]/VISUAL_SPECIFICATIONS.md`

```markdown
# Level [#] Visual Asset Specifications

## Overview
- Total assets: [#]
- Estimated creation time: [X-Y hours]
- Priority distribution: [High: #, Medium: #, Low: #]
- Target completion date: [Date]

## Asset Briefs (Detailed)

### Asset [#]: [Name]
**Priority:** High | Medium | Low  
**Estimated Hours:** [X hours]

**Context:**
[Why this diagram is needed, where it appears in learning path, what problem it solves]

**Content Requirements:**
[What information must be shown, what relationships depicted]

**Design Notes:**
[Specific design preferences, layout suggestions, examples of similar diagrams]

**Acceptance Criteria:**
- [ ] Shows all required components
- [ ] Relationships clearly indicated
- [ ] Color-blind accessible
- [ ] Text readable at typical viewing size
- [ ] Aligned with Microsoft brand

**Files Using This Asset:**
- [List actual .md files and line numbers where referenced]

---

## Prioritization Summary

**Create First (High Priority - 8 hours):**
- [Asset list in recommended order]

**Create Next (Medium Priority - 10 hours):**
- [Asset list in recommended order]

**Create Last (Low Priority - 2 hours):**
- [Asset list]

---
```

---

### Step #2: Content Integration Phase
**Owner:** Content Creator  
**Timeline:** 2-3 hours per level  
**Deliverable:** Markdown files with visual asset placeholder callouts

#### What to Do

1. **Add Visual Asset Placeholders** to every relevant content file
   - Use consistent format across all files
   - Reference the asset number and name from README
   - Link to specification (if created)
   - Indicate expected placement and sizing

2. **Placeholder Format** (Match Level 100 style)

   **Option A: Detailed Placeholder**
   ```markdown
   > **📊 Visual Asset Placeholder**  
   > **Asset [#]: [Asset Name]**  
   > *Expected location: [top/middle/bottom of section]*  
   > This section will include [brief description of what diagram shows].  
   > Asset specifications: [docs/assets/images/README.md#asset-xx]  
   > Diagram will illustrate: [key concepts shown]
   ```

   **Option B: Minimal Placeholder (Quick Reference)**
   ```markdown
   > **[Asset #: Asset Name]** ← [expected dimensions]
   ```

3. **Placement Guidelines**
   - Place after section introduction but before detailed text
   - Position before concept first appears in prose
   - Group related diagrams when multiple appear in section
   - Leave adequate space for final diagram (e.g., 400px width = ~2 inches)

4. **Link Diagram to Content**
   - Add caption under placeholder: `*Figure [#]: [Title]*`
   - Include source attribution if adapted from Microsoft Learn
   - Add cross-reference link to related diagrams

#### Quality Checklist for Step #2

- [ ] Placeholder added to all files where diagram is used ("Used In" list)
- [ ] Placeholder format consistent across all files
- [ ] Asset number and name clearly visible
- [ ] Expected dimensions noted
- [ ] Placement logical relative to content flow
- [ ] Links to README specifications work correctly
- [ ] Captions prepared for final diagrams
- [ ] Source attributions documented
- [ ] Cross-references between related diagrams noted
- [ ] All markdown files pass linting (ignore asset placeholder callouts in lint results)

#### Placeholder Integration Examples

**Example 1: Architecture Section**
```markdown
## Azure Local Architecture

Azure Local uses a layered architecture that separates the management plane from the data plane.

> **📊 Visual Asset Placeholder**  
> **Asset 11: Azure Local Architecture Diagram**  
> This diagram shows the complete Azure Local architecture including:
> - Hardware layer (compute, storage, network)
> - Software layers (virtualization, system, applications)
> - Management plane and data plane separation
> - Connection to Azure cloud control plane
> [Asset Spec: docs/assets/images/README.md#asset-11-azure-local-architecture]

The architecture consists of three main components...
```

**Example 2: Comparison Section**
```markdown
## Connected vs. Disconnected Modes

Azure Local supports two operational modes with different capabilities.

> **📊 Asset 7: Azure Local Modes Comparison** (1200x800px)
> *Shows side-by-side comparison with feature matrix*

### Connected Mode
In connected mode, the cluster maintains continuous connectivity to Azure...

### Disconnected Mode
In disconnected mode, the cluster operates independently...
```

**Example 3: Multi-Diagram Section**
```markdown
## Security Architecture Layers

The zero-trust security model applies across multiple layers:

> **[Asset 37: Encryption & Key Management Architecture]** (1400x1000px)  
> Shows encryption at-rest, in-transit, and in-use with key hierarchy

> **[Asset 38: Zero-Trust Security Architecture]** (1300x1000px)  
> Shows pillars: Identity, Endpoints, Networks, Data, Applications

The following sections detail each layer...
```

---

## Template for Future Levels

### For Level 300 (and beyond)

1. **Before Creating Any Content:**
   - Follow Step #3 first
   - Document all visual assets in `docs/assets/images/README.md`
   - Organize by level and module (mirror structure of Levels 100/200)
   - Use the Assets 21-40 as template for formatting and metadata

2. **While Creating Content:**
   - Follow Step #1 (optional for simple diagrams, required for complex architecture)
   - Create `docs/level-[#]/VISUAL_SPECIFICATIONS.md` if Level 300 is complex
   - Validate asset list with team
   - Prioritize assets for creation

3. **When Integrating Content:**
   - Follow Step #2
   - Add placeholder callouts immediately
   - Document all "Used In" references
   - Prepare for asset insertion

### Reusable Templates

**Asset Documentation Template**
```markdown
#### Asset [#]: [Asset Name]
**File:** `level-[#]/[descriptive-name].svg`  
**Priority:** High | Medium | Low  
**Status:** 🔴 Needed

**Description:** [1-2 sentence overview]

**Content:**
- [Component/concept 1]
- [Component/concept 2]
- [Relationship/flow]

**Visual Elements:**
- [Design element 1]
- [Design element 2]
- [Color scheme]

**Size:** [Width]x[Height]px

**Used In:**
- `docs/level-[#]/[file].md`

**Source Refs:** [Links to references]
```

**Placeholder Template**
```markdown
> **📊 Visual Asset Placeholder**  
> **Asset [#]: [Asset Name]**  
> This section will include [brief description].  
> Reference: [docs/assets/images/README.md#asset-xx]
```

**Specification Brief Template**
```markdown
### Asset [#]: [Name]
**Priority:** High | Medium | Low  
**Estimated Hours:** [X hours]

**Context:**
[Why needed, where appears, what problem solves]

**Content Requirements:**
[What must be shown, relationships depicted]

**Acceptance Criteria:**
- [ ] Shows all required components
- [ ] Relationships clearly indicated
- [ ] Color-blind accessible
```

---

## Quality Standards

### Design Standards

All visual assets should meet these criteria:

- **Clarity:** Concepts clearly visible, not cluttered
- **Consistency:** Style and colors match across all diagrams
- **Accessibility:** 
  - Color-blind friendly (avoid red+green combinations)
  - Sufficient contrast (WCAG AA minimum)
  - Descriptive alt text
- **Microsoft Brand Alignment:**
  - Colors: Microsoft Blue (#0078D4), Azure colors
  - Typography: Segoe UI or sans-serif equivalent
  - Style: Clean, modern, professional
- **Technical Accuracy:**
  - Validated against Microsoft Learn documentation
  - Endorsed by solution architects or subject matter experts
- **File Optimization:**
  - SVG format (scalable, small file size)
  - Minified for web delivery
  - Responsive scaling support

### Review Process

Before marking an asset as **Complete** (🟢):

1. **Content Validation:** Confirm diagram matches content requirements
2. **Brand Review:** Check colors, typography, style
3. **Accessibility Check:** Verify contrast, color-blindness, alt text
4. **Technical Review:** Validate accuracy with SMEs
5. **Performance Check:** Verify file size and rendering speed
6. **Final Approval:** Sign-off from content owner

---

## Tools and Resources

### Recommended Design Tools

| Tool | Type | Cost | Best For |
|------|------|------|----------|
| **draw.io** | Web-based diagramming | Free | Quick diagrams, flowcharts |
| **Figma** | Cloud design platform | Free/Paid | Collaboration, UI design |
| **Adobe Illustrator** | Professional vector editor | Paid | Complex illustrations |
| **Inkscape** | Open-source vector editor | Free | Detailed graphics |
| **Microsoft Visio** | Enterprise diagramming | Paid | Complex architectures |
| **Microsoft PowerPoint** | Office tool | Paid | Simple diagrams (export to SVG) |

### Icon and Asset Resources

- **[Azure Architecture Icons](https://learn.microsoft.com/en-us/azure/architecture/icons/)** - Official Microsoft icons
- **[Microsoft 365 Icons](https://developer.microsoft.com/en-us/fluentui#/styles/web/icons)** - Fluent Design System
- **[Font Awesome](https://fontawesome.com/)** - Generic icons
- **[Azure Designs](https://github.com/microsoft/Azure-Design)** - Community diagrams

### Color Reference

```
Microsoft Blue:     #0078D4
Azure Light Blue:   #0078D4
Azure Dark Blue:    #005A9C
Success Green:      #107C10
Warning Yellow:     #FFB900
Error Red:          #D83B01
Neutral Gray Dark:  #323130
Neutral Gray Mid:   #605E5C
Neutral Gray Light: #F3F2F1
```

### Microsoft Documentation

- **[Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/)** - Reference architectures
- **[Microsoft Cloud for Sovereignty](https://learn.microsoft.com/en-us/industry/sovereign-cloud/)** - Sovereign cloud content
- **[Azure Local Documentation](https://learn.microsoft.com/en-us/azure-local/)** - Azure Local specifics
- **[Azure Arc Overview](https://learn.microsoft.com/en-us/azure/azure-arc/overview)** - Arc reference

---

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│ NEW CONTENT LEVEL CREATION                                   │
└─────────────────────────────────────────────────────────────┘

    ↓

┌─────────────────────────────────────────────────────────────┐
│ STEP #3: DOCUMENTATION/SPECIFICATION PHASE                  │
│ ─────────────────────────────────────────────────────────── │
│ Owner: Content Creator                                       │
│ Timeline: 30 minutes per level                               │
│ ─────────────────────────────────────────────────────────── │
│ Tasks:                                                       │
│  1. Document all visual assets in README                     │
│  2. Create comprehensive specs with metadata                 │
│  3. Update summary tables and counts                         │
│  4. Set all assets to 🔴 Needed status                      │
│ ─────────────────────────────────────────────────────────── │
│ Deliverable: Specification entries in README                │
│ Status: SINGLE SOURCE OF TRUTH for what's needed            │
└─────────────────────────────────────────────────────────────┘

    ↓

┌─────────────────────────────────────────────────────────────┐
│ STEP #1: DETAILED SPECIFICATION PHASE                       │
│ ─────────────────────────────────────────────────────────── │
│ Owner: Content Creator / Solution Architect                  │
│ Timeline: 1-2 hours per level                                │
│ ─────────────────────────────────────────────────────────── │
│ Tasks:                                                       │
│  1. Expand README specs into detailed briefs                 │
│  2. Create wireframes/mockups for complex diagrams           │
│  3. Define design constraints and brand alignment            │
│  4. Prioritize creation order (High → Medium → Low)          │
│  5. Create prioritization matrix                             │
│ ─────────────────────────────────────────────────────────── │
│ Deliverable: VISUAL_SPECIFICATIONS.md (optional)            │
│ Status: Ready for designer/creator                          │
└─────────────────────────────────────────────────────────────┘

    ↓

┌─────────────────────────────────────────────────────────────┐
│ STEP #2: CONTENT INTEGRATION PHASE                          │
│ ─────────────────────────────────────────────────────────── │
│ Owner: Content Creator                                       │
│ Timeline: 2-3 hours per level                                │
│ ─────────────────────────────────────────────────────────── │
│ Tasks:                                                       │
│  1. Add placeholder callouts to all content files            │
│  2. Use consistent placeholder format (Level 100 style)      │
│  3. Link to asset specifications                             │
│  4. Prepare captions and source attributions                 │
│  5. Document cross-references between diagrams               │
│ ─────────────────────────────────────────────────────────── │
│ Deliverable: Content files with placeholders                │
│ Status: Ready for visual asset insertion                    │
└─────────────────────────────────────────────────────────────┘

    ↓

┌─────────────────────────────────────────────────────────────┐
│ ASSET CREATION PHASE (Future)                               │
│ ─────────────────────────────────────────────────────────── │
│ Owner: Designer / Visual Creator                             │
│ Timeline: 0.7-0.9 hours per diagram                          │
│ ─────────────────────────────────────────────────────────── │
│ Using: Step #1 specifications and Step #2 placeholders       │
│ ─────────────────────────────────────────────────────────── │
│ Process:                                                     │
│  1. Review detailed spec from Step #1                        │
│  2. Check placeholder placement from Step #2                 │
│  3. Create SVG/diagram following brand guidelines            │
│  4. Validate with SMEs                                       │
│  5. Insert into placeholders and remove placeholders         │
│  6. Update asset status to 🟢 Complete                      │
│ ─────────────────────────────────────────────────────────── │
│ Deliverable: SVG files + updated content files              │
│ Status: Diagrams live in documentation                      │
└─────────────────────────────────────────────────────────────┘

    ↓

┌─────────────────────────────────────────────────────────────┐
│ DOCUMENTATION COMPLETE                                       │
│ ─────────────────────────────────────────────────────────── │
│ Content is production-ready with visual assets               │
│ Update README: 🟢 [Asset count] assets created              │
│ Update progress tracking with completion date                │
└─────────────────────────────────────────────────────────────┘
```

---

## Current Status

### Levels 100 & 200 (Complete - Steps #3, #1, #2)

| Step | Level 100 | Level 200 | Status |
|------|-----------|-----------|--------|
| **#3 Documentation** | ✅ 20 assets documented | ✅ 20 assets documented | 🟢 Complete |
| **#1 Specification** | ⏳ Pending detailed briefs | ⏳ Pending detailed briefs | 🟡 Ready Next |
| **#2 Integration** | ⏳ Pending placeholders | ⏳ Pending placeholders | 🟡 Ready Next |
| **Asset Creation** | 🔴 Not started | 🔴 Not started | 🔴 Estimated 30-34 hrs |

### Level 300 (TBD)

- [ ] Follow Step #3 before creating any Level 300 content
- [ ] Document 15-20 visual assets in README
- [ ] Use Assets 41+ numbering
- [ ] Organize by Level 300 modules (to be determined)
- [ ] Follow same process: #3 → #1 → #2 → Creation

---

## Checklist for Implementation

### When Starting a New Content Level

- [ ] **Step #3 Complete?**
  - [ ] All visual assets documented in README
  - [ ] Comprehensive specs with metadata
  - [ ] Summary tables updated
  - [ ] Status set to 🔴 Needed for all assets

- [ ] **Step #1 Complete?**
  - [ ] Detailed briefs written for all assets
  - [ ] Wireframes/mockups created for complex diagrams
  - [ ] Design constraints defined
  - [ ] Creation priorities assigned
  - [ ] Team review completed

- [ ] **Step #2 Complete?**
  - [ ] Placeholder callouts added to all files
  - [ ] Consistent formatting used throughout
  - [ ] Links to specifications work
  - [ ] Captions and attributions prepared
  - [ ] Cross-references documented

### Before Publishing Content

- [ ] All three steps #3, #1, #2 complete
- [ ] README updated with asset counts
- [ ] Placeholder callouts present in all content files
- [ ] Links to external resources verified
- [ ] Markdown linting passed (expected: MD022, MD032 for lists)
- [ ] Content is production-ready for asset insertion

---

## Document Maintenance

- **Last Updated:** October 2025
- **Process Owner:** Project Lead
- **Review Cycle:** Quarterly (or when new level created)
- **Questions?** Open an issue in the project repository

---

## References

- [docs/assets/images/README.md](../docs/assets/images/README.md) - Visual asset specifications
- [docs/level-100/README.md](../docs/level-100/README.md) - Level 100 placeholder examples
- [docs/level-200/README.md](../docs/level-200/README.md) - Level 200 placeholder examples
- [CONTRIBUTING.md](./CONTRIBUTING.md) - General contribution guidelines
