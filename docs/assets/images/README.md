# Visual Assets for Microsoft Sovereign Cloud Skilling Plan

This directory contains visual assets (diagrams, architecture illustrations, infographics) used throughout the skilling plan documentation.

## 📁 Directory Structure

```
docs/assets/images/
├── README.md (this file)
├── level-100/              # Foundational concept diagrams
│   ├── sovereignty-spectrum.svg
│   ├── azure-regions-map.svg
│   ├── eu-data-boundary.svg
│   ├── data-residency-vs-sovereignty.svg
│   ├── regulatory-comparison-matrix.svg
│   ├── operational-sovereignty-levels.svg
│   └── azure-local-modes-comparison.svg
├── level-200/              # Architecture and pre-sales diagrams
│   ├── azure-local-architecture.svg
│   ├── azure-arc-architecture.svg
│   └── edge-rag-architecture.svg
├── level-300/              # Advanced technical diagrams
│   └── (to be defined)
└── common/                 # Reusable elements and icons
    ├── microsoft-logo.svg
    ├── azure-icons/
    └── flow-diagram-elements/
```

---

## 🎨 Required Visual Assets

### Level 100 - Foundation

#### 1. Digital Sovereignty Spectrum
**File:** `level-100/sovereignty-spectrum.svg`

**Description:** Visual representation of the 5-level sovereignty spectrum from standard cloud to air-gapped systems.

**Content:**
- Level 1: Standard Cloud (Azure Public)
- Level 2: Enhanced Cloud (Azure with sovereignty controls)
- Level 3: Dedicated Cloud (Azure Local Connected Mode)
- Level 4: Isolated Cloud (Azure Local Disconnected Mode)
- Level 5: Air-Gapped (Fully isolated systems)

**Visual Elements:**
- Horizontal spectrum/ladder showing progression
- Icons representing connectivity level
- Text descriptions for each level
- Color coding: Green (public) → Yellow (enhanced) → Orange (dedicated) → Red (isolated/air-gapped)

**Recommended Source:**
- Adapt from: [Azure Local deployment models](https://learn.microsoft.com/en-us/azure/azure-local/concepts/deployment-options)
- Reference: [Microsoft Cloud for Sovereignty](https://learn.microsoft.com/en-us/industry/sovereign-cloud/)

**Used In:**
- `docs/level-100/digital-sovereignty.md`
- `docs/level-100/operational-sovereignty.md`

---

#### 2. Azure Global Infrastructure Map
**File:** `level-100/azure-regions-map.svg`

**Description:** World map showing Azure regions, availability zones, and data center locations.

**Content:**
- Azure regions marked by geographic location
- EU Data Boundary highlighted
- Key regions labeled (US Gov, Germany, China 21Vianet)
- Legend explaining symbols

**Visual Elements:**
- World map base layer
- Region markers with labels
- Special highlighting for sovereign regions
- Color-coded by geographic area

**Recommended Source:**
- Adapt from: [Azure global infrastructure](https://azure.microsoft.com/en-us/explore/global-infrastructure/)
- Use: [Azure geographies map](https://datacenters.microsoft.com/globe/explore)

**Used In:**
- `docs/level-100/data-residency-concepts.md`
- `docs/level-100/european-commitments.md`

---

#### 3. EU Data Boundary Diagram
**File:** `level-100/eu-data-boundary.svg`

**Description:** Visual representation of Microsoft's EU Data Boundary commitment showing what data stays in the EU and documented exceptions.

**Content:**
- EU boundary perimeter
- Data types stored/processed in EU
- Customer Lockbox workflow
- Exception scenarios with customer control
- Data flow arrows

**Visual Elements:**
- Map outline of EU/EEA region
- Data flow diagrams
- Lock icons for security controls
- Exception callouts with explanations

**Recommended Source:**
- Adapt from: [EU Data Boundary documentation](https://learn.microsoft.com/en-us/privacy/eudb/eu-data-boundary-learn)
- Reference: [EU Data Boundary for Microsoft Cloud](https://www.microsoft.com/en-us/trust-center/privacy/european-data-boundary)

**Used In:**
- `docs/level-100/european-commitments.md`
- `docs/level-100/digital-sovereignty.md`

---

#### 4. Data Residency vs. Sovereignty Comparison
**File:** `level-100/data-residency-vs-sovereignty.svg`

**Description:** Side-by-side comparison showing the difference between data residency (location only) and data sovereignty (location + control).

**Content:**
- Two columns: "Data Residency" vs. "Data Sovereignty"
- Visual representations of each concept
- Key differentiators highlighted
- Venn diagram showing relationship

**Visual Elements:**
- Split diagram or comparison table
- Icons for location, control, compliance
- Color coding to distinguish concepts
- Checkmarks/X marks for capabilities

**Recommended Source:**
- Create custom based on: [Digital sovereignty overview](https://learn.microsoft.com/en-us/industry/sovereign-cloud/overview/digital-sovereignty)
- Reference: [Azure data residency](https://azure.microsoft.com/en-us/explore/global-infrastructure/data-residency/)

**Used In:**
- `docs/level-100/data-residency-concepts.md`
- `docs/level-100/digital-sovereignty.md`

---

#### 5. Regulatory Compliance Comparison Matrix
**File:** `level-100/regulatory-comparison-matrix.svg`

**Description:** Table/matrix comparing GDPR, FedRAMP, HIPAA, PCI DSS, and ITAR requirements side-by-side.

**Content:**
- Rows: Regulations (GDPR, FedRAMP, HIPAA, PCI DSS, ITAR)
- Columns: Jurisdiction, Key Requirements, Data Location, Access Controls, Azure Compliance
- Color-coded cells for quick scanning

**Visual Elements:**
- Structured table with alternating row colors
- Flag icons for jurisdictions
- Checkmarks for compliance status
- Bold headers for readability

**Recommended Source:**
- Aggregate from: [Microsoft Trust Center Compliance Offerings](https://learn.microsoft.com/en-us/compliance/regulatory/offering-home)
- Reference: [Azure compliance documentation](https://learn.microsoft.com/en-us/azure/compliance/)

**Used In:**
- `docs/level-100/regulatory-overview.md`
- `docs/level-100/digital-sovereignty.md`

---

#### 6. Operational Sovereignty Levels
**File:** `level-100/operational-sovereignty-levels.svg`

**Description:** Detailed breakdown of the 5 operational sovereignty levels with control characteristics at each level.

**Content:**
- 5 levels stacked vertically
- For each level: control plane location, connectivity, personnel access, use cases
- Progressive restriction indicators

**Visual Elements:**
- Layered diagram or stepped pyramid
- Icons for control plane, network, personnel
- Use case examples for each level
- Color gradient showing increasing sovereignty

**Recommended Source:**
- Adapt from: [Azure Local overview](https://learn.microsoft.com/en-us/azure/azure-local/overview)
- Reference: [Disconnected scenarios](https://learn.microsoft.com/en-us/azure/azure-local/concepts/disconnected-scenarios)

**Used In:**
- `docs/level-100/operational-sovereignty.md`
- `docs/level-100/digital-sovereignty.md`

---

#### 7. Azure Local Modes Comparison
**File:** `level-100/azure-local-modes-comparison.svg`

**Description:** Side-by-side comparison of Azure Local Connected Mode vs. Disconnected Mode.

**Content:**
- Two columns: Connected vs. Disconnected
- Control plane architecture for each
- Connectivity requirements
- Management capabilities
- Feature comparison table

**Visual Elements:**
- Split diagram with architecture visuals
- Cloud icon for connected mode, on-premises icon for disconnected
- Flow diagrams showing management paths
- Feature matrix at bottom

**Recommended Source:**
- Adapt from: [Azure Local deployment options](https://learn.microsoft.com/en-us/azure/azure-local/concepts/deployment-options)
- Reference: [Disconnected deployment](https://learn.microsoft.com/en-us/azure/azure-local/concepts/disconnected-scenarios)

**Used In:**
- `docs/level-100/operational-sovereignty.md`
- `docs/level-100/digital-sovereignty.md` (Decision Framework)

---

#### 8. Sovereign Cloud Models Comparison
**File:** `level-100/sovereign-cloud-models-comparison.svg`

**Description:** Side-by-side comparison of the three sovereign cloud models showing key characteristics, use cases, and decision criteria.

**Content:**
- Three columns: Sovereign Public | Sovereign Private | National Partner
- Comparison rows: Infrastructure, Control Level, Compliance, Use Cases, Cost Model
- Visual indicators for sovereignty level (Low/Medium/High)
- Decision criteria for selecting each model

**Visual Elements:**
- Three-column layout with clear separation
- Icons for each model type (cloud icon for Public, server icon for Private, partner icon for Partner)
- Color coding: Blue (Public), Green (Private), Purple (Partner)
- Comparison table with checkmarks and detailed attributes
- Call-out boxes for key differentiators

**Recommended Source:**
- Create custom based on: [Microsoft Cloud for Sovereignty](https://learn.microsoft.com/en-us/industry/sovereign-cloud/)
- Reference: [Azure deployment models](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/)

**Used In:**
- `docs/level-100/sovereign-cloud-models.md`

**Estimated Creation Time:** 2 hours

---

#### 9. Model Decision Tree
**File:** `level-100/model-decision-tree.svg`

**Description:** Decision flowchart to help customers select the appropriate sovereign cloud model based on their requirements.

**Content:**
- Start: "What are your sovereignty requirements?"
- Decision nodes:
  - Data residency only? → Sovereign Public Cloud
  - Operational control needed? → Check connectivity requirements
  - Disconnected operations? → Sovereign Private Cloud (Disconnected)
  - National regulations? → National Partner Clouds
  - Connected with control? → Sovereign Private Cloud (Connected)
- End nodes: Recommended model for each path with example scenarios

**Visual Elements:**
- Flowchart with decision diamonds (yes/no branches)
- Clear yes/no paths with arrows
- Color-coded outcomes matching model colors
- Example scenarios at each endpoint
- Icons for each decision type (data, control, network, compliance)

**Recommended Source:**
- Create custom decision tree
- Reference: [Azure decision guides](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/decision-guides/)

**Used In:**
- `docs/level-100/sovereign-cloud-models.md`

**Estimated Creation Time:** 1.5 hours

---

#### 10. National Partner Clouds Map
**File:** `level-100/partner-clouds-map.svg`

**Description:** World map showing geographic distribution of national partner clouds and their sovereign guarantees.

**Content:**
- World map with regions highlighted
- Azure Government (US regions): Virginia, Texas, Arizona, DoD regions
- Azure China (21Vianet regions): Beijing, Shanghai
- Azure Germany (historical, discontinued): Lessons learned callout
- Legend showing sovereignty level and operator information
- Connectivity lines showing isolation from global Azure

**Visual Elements:**
- World map base (simplified, focus on relevant regions)
- Regional highlights with callouts and details
- Flag icons for countries (US, China, Germany)
- Sovereignty level indicators (color-coded)
- Operator logos/names (Microsoft, 21Vianet, T-Systems historical)
- Network isolation visualization (separate bubbles)

**Recommended Source:**
- Adapt from: [Azure global infrastructure](https://azure.microsoft.com/en-us/explore/global-infrastructure/)
- Reference: [National clouds documentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/authentication-national-cloud)

**Used In:**
- `docs/level-100/national-partner-clouds.md`
- `docs/level-100/sovereign-cloud-models.md`

**Estimated Creation Time:** 1 hour

---

### Level 200 - Intermediate (Placeholder)

#### 11. Azure Local Architecture
**File:** `level-200/azure-local-architecture.svg`

**Description:** Detailed architecture diagram of Azure Local infrastructure.

**Recommended Source:**
- [Azure Local architecture](https://learn.microsoft.com/en-us/azure/azure-local/concepts/system-requirements)

**Used In:** (To be determined when Level 200 content is created)

---

#### 12. Azure Arc Architecture
**File:** `level-200/azure-arc-architecture.svg`

**Description:** Azure Arc unified control plane architecture showing on-premises, edge, and multi-cloud management.

**Recommended Source:**
- [Azure Arc overview](https://learn.microsoft.com/en-us/azure/azure-arc/overview)

**Used In:** (To be determined when Level 200 content is created)

---

#### 13. Edge RAG Architecture
**File:** `level-200/edge-rag-architecture.svg`

**Description:** Edge RAG solution architecture showing data ingestion, vector database, LLM integration, and retrieval flow.

**Recommended Source:**
- [Azure Arc-enabled data services](https://learn.microsoft.com/en-us/azure/azure-arc/data/overview)

**Used In:** (To be determined when Level 200 content is created)

---

## 🛠️ Asset Creation Guidelines

### File Format Standards

- **Primary Format:** SVG (Scalable Vector Graphics)
  - Reason: Resolution-independent, small file size, editable
  - Alternative: PNG (300 DPI minimum if SVG not available)

- **Naming Convention:** lowercase-with-hyphens.svg
  - ✅ Good: `sovereignty-spectrum.svg`
  - ❌ Bad: `SovereigntySpectrum.svg` or `sovereignty spectrum.svg`

### Design Specifications

**Color Palette:**
- Microsoft Blue: `#0078D4`
- Azure Blue: `#008AD7`
- Success Green: `#107C10`
- Warning Yellow: `#FFB900`
- Error Red: `#E81123`
- Gray Scale: `#323130`, `#605E5C`, `#F3F2F1`

**Typography:**
- Primary Font: Segoe UI (Microsoft standard)
- Fallback: Arial, sans-serif
- Minimum Font Size: 12pt for body, 16pt for headings

**Accessibility:**
- Ensure sufficient color contrast (WCAG AA minimum)
- Include alt text descriptions
- Avoid relying solely on color to convey information
- Use patterns/textures in addition to colors where possible

**Sizing:**
- Recommended Width: 800-1200px for full-width diagrams
- Recommended Width: 400-600px for inline diagrams
- Maintain 16:9 or 4:3 aspect ratios where possible

### Sourcing Diagrams

**Priority Order:**
1. **Microsoft Learn Official Diagrams:** Use directly if available and licensing permits
2. **Microsoft Learn Adapted Diagrams:** Modify official diagrams to fit our content
3. **Custom Created Diagrams:** Create from scratch using guidelines above

**Licensing:**
- Microsoft Learn content is typically licensed under Creative Commons
- Always attribute source with links in image captions
- Verify licensing terms before using any diagram

**Tools Recommended:**
- **Draw.io (diagrams.net):** Free, web-based, exports to SVG
- **Microsoft Visio:** Professional diagramming (requires license)
- **PowerPoint/Keynote:** For simple diagrams (export to SVG)
- **Inkscape:** Free, open-source vector graphics editor

---

## 📝 Asset Tracking

### Status Legend
- 🟢 **Available:** Asset exists and is ready to use
- 🟡 **In Progress:** Asset is being created or adapted
- 🔴 **Needed:** Asset required but not yet created
- ⚪ **Optional:** Nice-to-have but not critical

### Current Status

| Asset Name | Status | Priority | Assignee | Notes |
|------------|--------|----------|----------|-------|
| sovereignty-spectrum.svg | 🔴 Needed | High | TBD | Critical for multiple pages |
| azure-regions-map.svg | 🔴 Needed | High | TBD | Can use Microsoft Learn map |
| eu-data-boundary.svg | 🔴 Needed | High | TBD | Official diagram available |
| data-residency-vs-sovereignty.svg | 🔴 Needed | Medium | TBD | Custom creation needed |
| regulatory-comparison-matrix.svg | 🔴 Needed | Medium | TBD | Table format, easy to create |
| operational-sovereignty-levels.svg | 🔴 Needed | High | TBD | Critical for operational concepts |
| azure-local-modes-comparison.svg | 🔴 Needed | High | TBD | Side-by-side comparison |
| sovereign-cloud-models-comparison.svg | 🔴 Needed | High | TBD | Module 2 - Three model comparison |
| model-decision-tree.svg | 🔴 Needed | High | TBD | Module 2 - Decision flowchart |
| partner-clouds-map.svg | 🔴 Needed | High | TBD | Module 2 - Geographic map |
| azure-local-architecture.svg | 🔴 Needed | Low | TBD | Level 200 content (future) |
| azure-arc-architecture.svg | 🔴 Needed | Low | TBD | Level 200 content (future) |
| edge-rag-architecture.svg | 🔴 Needed | Low | TBD | Level 200 content (future) |

---

## 🔗 Implementation in Markdown

### How to Reference Images

**Standard Image Reference:**
```markdown
![Alt text describing the image](../assets/images/level-100/sovereignty-spectrum.svg)
*Figure 1: Digital Sovereignty Spectrum showing five levels of control*
```

**Image with Link:**
```markdown
[![Alt text](../assets/images/level-100/eu-data-boundary.svg)](https://learn.microsoft.com/en-us/privacy/eudb/eu-data-boundary-learn)
*Source: [Microsoft EU Data Boundary Documentation](https://learn.microsoft.com/en-us/privacy/eudb/eu-data-boundary-learn)*
```

**Image with Caption and Attribution:**
```markdown
![Azure Global Infrastructure Map](../assets/images/level-100/azure-regions-map.svg)

**Figure 2: Azure Global Infrastructure**  
*Azure operates 60+ regions worldwide with multiple availability zones for high availability and disaster recovery.*  
*Source: Adapted from [Azure Global Infrastructure](https://azure.microsoft.com/en-us/explore/global-infrastructure/)*
```

### Placeholder Usage

Until assets are created, use placeholders:

```markdown
> **📊 Visual Reference Needed**  
> *Sovereignty Spectrum Diagram*  
> This section will include a visual diagram showing the 5 levels of digital sovereignty from standard cloud to air-gapped systems.  
> **Source to adapt:** [Azure Local deployment models](https://learn.microsoft.com/en-us/azure/azure-local/concepts/deployment-options)
```

---

## 📋 Next Steps

### Immediate Actions (Level 100 Priority)

**Module 1: Digital Sovereignty (7 diagrams)**

1. **Create sovereignty-spectrum.svg**
   - Reference operational-sovereignty.md content
   - Show 5 levels with characteristics
   - Est. time: 2 hours

2. **Adapt azure-regions-map.svg**
   - Use Microsoft Learn global infrastructure map
   - Highlight EU Data Boundary
   - Est. time: 1 hour

3. **Adapt eu-data-boundary.svg**
   - Use official Microsoft EU Data Boundary diagram
   - Add callouts for exceptions and controls
   - Est. time: 1 hour

4. **Create data-residency-vs-sovereignty.svg**
   - Custom comparison diagram
   - Show relationship and differences
   - Est. time: 1.5 hours

5. **Create regulatory-comparison-matrix.svg**
   - Table/matrix format
   - Extract data from regulatory-overview.md
   - Est. time: 1 hour

6. **Create operational-sovereignty-levels.svg**
   - Similar to sovereignty spectrum but more detailed
   - Include control plane details
   - Est. time: 2 hours

7. **Create azure-local-modes-comparison.svg**
   - Side-by-side comparison
   - Architecture diagrams for each mode
   - Est. time: 2 hours

**Module 2: Sovereign Cloud Models (3 diagrams)**

8. **Create sovereign-cloud-models-comparison.svg**
   - Three-column comparison of models
   - Icons and color coding
   - Est. time: 2 hours

9. **Create model-decision-tree.svg**
   - Flowchart for model selection
   - Decision nodes and outcomes
   - Est. time: 1.5 hours

10. **Create partner-clouds-map.svg**
    - World map with partner cloud locations
    - Azure Government, Azure China, historical Azure Germany
    - Est. time: 1 hour

**Total Estimated Time: 14 hours (10 diagrams)**

### Future Actions (Level 200/300)

- Create detailed architecture diagrams for Azure Local
- Develop Azure Arc architecture visuals
- Design Edge RAG solution architecture diagrams
- Create hands-on lab screenshots and walkthroughs

---

## 🤝 Contributing Visual Assets

If you create or adapt visual assets for this project:

1. **Follow the guidelines** in this document
2. **Name files correctly** using the naming convention
3. **Place in appropriate directory** (level-100, level-200, etc.)
4. **Update the status table** above
5. **Add attribution** to source materials
6. **Verify accessibility** (color contrast, alt text)
7. **Test rendering** in both light and dark themes
8. **Optimize file size** (compress SVGs, use appropriate PNG resolution)

**Submit via Pull Request** with:
- Visual asset file(s)
- Updated README.md status table
- Description of changes
- Attribution/source information

---

## 📚 Additional Resources

**Microsoft Design Resources:**
- [Azure Architecture Icons](https://learn.microsoft.com/en-us/azure/architecture/icons/)
- [Microsoft Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks)
- [Fluent 2 Design System](https://fluent2.microsoft.design/)

**Diagramming Tools:**
- [Draw.io Azure Icon Library](https://github.com/pacodelacruz/diagrams.net-azure-libraries)
- [Azure Icons Collection (GitHub)](https://github.com/microsoft/Azure-Design)
- [Lucidchart Azure Template](https://www.lucidchart.com/pages/templates/cloud-architecture/azure)

**Learning Resources:**
- [Microsoft Learn Diagram Examples](https://learn.microsoft.com/en-us/azure/architecture/)
- [Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/)

---

**Last Updated:** October 2025  
**Maintained By:** Project Contributors  
**Questions?** Open an issue in the GitHub repository
