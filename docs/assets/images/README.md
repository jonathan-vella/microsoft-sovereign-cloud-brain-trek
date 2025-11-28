---
layout: default
title: Visual Assets for Microsoft Sovereign Cloud Skilling Plan
nav_exclude: true
---

# Visual Assets for Microsoft Sovereign Cloud Skilling Plan

This directory contains visual assets (diagrams, architecture illustrations, infographics) used throughout the skilling plan documentation.

## 📁 Directory Structure

```text
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

- Adapt from: [Azure Local deployment models](https://learn.microsoft.com/en-us/azure/azure-local/deploy/deployment-introduction?view=azloc-2509)
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
- Reference: [Disconnected scenarios](https://learn.microsoft.com/en-us/azure/azure-local/manage/disconnected-operations-overview?view=azloc-2509)

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

- Adapt from: [Azure Local deployment options](https://learn.microsoft.com/en-us/azure/azure-local/deploy/deployment-introduction?view=azloc-2509)
- Reference: [Disconnected deployment](https://learn.microsoft.com/en-us/azure/azure-local/manage/disconnected-operations-overview?view=azloc-2509)

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

---

## Module 3: Azure Local Overview - Visual Assets

### Asset 11: Azure Local Architecture Diagram
**File:** `level-100/azure-local-architecture.svg`  
**Priority:** High  
**Status:** Documented (Not Created)

**Description:** Comprehensive system architecture showing Azure Local components, connectivity modes, and Azure integration.

**Content:**
- Left: On-premises Azure Local stack (hardware, virtualization, system layer, management)
- Center: Data and control plane separation
- Right: Azure cloud control plane
- Network connectivity paths (Connected vs. Disconnected)

**Visual Elements:**
- Hardware layer components
- Software stack layers
- Bidirectional arrows (Connected mode)
- Dashed lines (optional Disconnected sync)
- Color coding: Blue (on-prem), Light blue (Azure), Green (data), Orange (management)

**Size:** 1400x1000px

**Source:** [Azure Local Architecture](https://learn.microsoft.com/en-us/azure/azure-local/overview?view=azloc-2509)

**Used In:**
- `docs/level-100/azure-local-overview.html`
- `docs/level-100/azure-local-architecture.html`

---

### Asset 12: Connected vs. Disconnected Mode Comparison
**File:** `level-100/azure-local-modes-comparison.svg`  
**Priority:** High  
**Status:** Documented (Not Created)

**Description:** Side-by-side comparison of Connected and Disconnected deployment modes with feature matrix.

**Content:**
- Left panel: Connected Mode characteristics and architecture
- Right panel: Disconnected Mode characteristics and architecture
- Bottom: Feature availability matrix (✓ / ✗ / Limited)
- Use case callouts for each mode

**Visual Elements:**
- Two parallel architectures
- Feature comparison table
- Checkmarks and X marks for features
- Brief use case examples
- Icons for connectivity state

**Size:** 1200x800px

**Design Notes:** Use green checkmarks and red X's consistently, show connectivity lines clearly

**Used In:**
- `docs/level-100/azure-local-overview.html`
- `docs/level-100/azure-local-connected-mode.html`
- `docs/level-100/azure-local-disconnected-mode.html`

---

### Asset 13: Hardware Topology Diagram
**File:** `level-100/azure-local-hardware-topology.svg`  
**Priority:** Medium  
**Status:** Documented (Not Created)

**Description:** Physical hardware configuration showing typical 2-3 node cluster setup.

**Content:**
- Node layout (2-4 nodes shown)
- Per-node components: CPU, memory, storage, network adapters
- Network topology: ToR switches, management network, storage network
- External connections: WAN, storage array (optional)
- Redundancy indicators

**Visual Elements:**
- Server hardware illustrations
- Network connectivity lines
- Cable/connection types labeled
- Redundancy indicators (dual power, dual switches)
- Component specifications callouts

**Size:** 1400x1000px

**Source:** [Azure Local System Requirements](https://learn.microsoft.com/en-us/azure/azure-local/concepts/system-requirements-23h2?view=azloc-2509)

**Used In:**
- `docs/level-100/azure-local-hardware.html`
- `docs/level-100/azure-local-architecture.html`

---

## Module 4: Azure Arc Introduction - Visual Assets

### Asset 14: Azure Arc Architecture
**File:** `level-100/azure-arc-architecture.svg`  
**Priority:** High  
**Status:** Documented (Not Created)

**Description:** Unified view of Azure Arc connecting on-premises resources to Azure management plane.

**Content:**
- Left: On-premises resources (servers, Kubernetes, databases)
- Center: Azure Arc control plane
- Right: Azure cloud services (Portal, Monitor, Policy, Security Center)
- Connection flows showing registration and management

**Visual Elements:**
- Three Arc services highlighted (Servers, Kubernetes, Data)
- Color coding: Green (Servers), Blue (Kubernetes), Purple (Data Services)
- Bidirectional arrows (management commands, telemetry)
- Azure service icons

**Size:** 1400x900px

**Source:** [Azure Arc Overview](https://learn.microsoft.com/en-us/azure/azure-arc/overview)

**Used In:**
- `docs/level-100/azure-arc-intro.html`
- All Arc sub-pages

---

### Asset 15: Arc Services Comparison Matrix
**File:** `level-100/azure-arc-services-comparison.svg`  
**Priority:** Medium  
**Status:** Documented (Not Created)

**Description:** Comparison table showing capabilities of Arc Servers, Kubernetes, and Data Services.

**Content:**
- Three columns: Servers | Kubernetes | Data Services
- Rows: Target resources, Management, Governance, Monitoring, Licensing, Best For
- Visual indicators for feature availability

**Visual Elements:**
- Clean table layout
- Service icons
- Checkmarks for capabilities
- Brief descriptions in cells
- Color-coded headers

**Size:** 1200x800px

**Used In:**
- `docs/level-100/azure-arc-intro.html`

---

### Asset 16: Arc Deployment Topology
**File:** `level-100/azure-arc-deployment-topology.svg`  
**Priority:** Low  
**Status:** Documented (Not Created)

**Description:** Multi-site deployment showing Arc managing resources across locations.

**Content:**
- Multiple sites (data center, branch office, edge location)
- Arc-enabled resources at each site
- Central Azure management plane
- Network connectivity paths

**Visual Elements:**
- Geographic distribution representation
- Site-specific resources
- Unified management layer
- Connection indicators

**Size:** 1200x800px

**Used In:**
- `docs/level-100/azure-arc-intro.html`
- `docs/level-100/azure-arc-servers.html`

---

## Module 5: Edge RAG Concepts - Visual Assets

### Asset 17: Edge RAG System Architecture
**File:** `level-100/edge-rag-architecture.svg`  
**Priority:** High  
**Status:** Documented (Not Created)

**Description:** Complete Edge RAG system architecture showing all components and data flow.

**Content:**
- Document sources and ingestion pipeline
- Embeddings generation and vector database
- Query processing flow
- Local LLM inference
- Response generation with citations
- Optional cloud connection (dashed)

**Visual Elements:**
- Component boxes with icons
- Data flow arrows
- Numbers indicating sequence (1, 2, 3...)
- Color coding: Blue (data), Green (processing), Purple (AI)
- Callouts for key components

**Size:** 1400x1000px

**Design Notes:** Show edge components prominently, cloud as optional/secondary

**Used In:**
- `docs/level-100/edge-rag-concepts.html`
- `docs/level-100/edge-rag-architecture.html`

---

### Asset 18: Traditional LLM vs. RAG Comparison
**File:** `level-100/llm-vs-rag-comparison.svg`  
**Priority:** High  
**Status:** Documented (Not Created)

**Description:** Side-by-side comparison showing Traditional LLM flow vs. RAG-augmented flow.

**Content:**
- Left panel: Traditional LLM (Query → LLM → Answer)
- Right panel: RAG flow (Query → Retrieval → Context + LLM → Answer with sources)
- Comparison table: Accuracy, recency, citations, hallucinations

**Visual Elements:**
- Two parallel workflows
- Simple flow diagrams
- Comparison matrix
- Icons for documents, LLM, search
- Green/red indicators for pros/cons

**Size:** 1200x800px

**Used In:**
- `docs/level-100/edge-rag-concepts.html`
- `docs/level-100/rag-fundamentals.html`

---

### Asset 19: Edge RAG Deployment Options
**File:** `level-100/edge-rag-deployment-options.svg`  
**Priority:** Medium  
**Status:** Documented (Not Created)

**Description:** Three deployment topology options for Edge RAG systems.

**Content:**
- Option 1: Local edge only (disconnected/air-gapped)
- Option 2: Edge with cloud sync (connected/hybrid)
- Option 3: Multi-edge deployment with central coordination
- Data flow patterns for each option

**Visual Elements:**
- Three topology diagrams
- Network connectivity indicators
- Data flow arrows
- Use case labels
- Pros/cons callouts

**Size:** 1300x900px

**Used In:**
- `docs/level-100/edge-rag-concepts.html`
- `docs/level-100/edge-rag-architecture.html`

---

### Asset 20: RAG Components and Data Flow
**File:** `level-100/rag-components-flow.svg`  
**Priority:** Medium  
**Status:** Documented (Not Created)

**Description:** Detailed data flow showing how a query moves through RAG system components.

**Content:**
- Step-by-step data flow with numbered sequence:
  1. User query input
  2. Query embedding generation
  3. Vector database similarity search
  4. Document retrieval (top-K)
  5. Context assembly
  6. LLM prompt construction
  7. Answer generation
  8. Response with citations

**Visual Elements:**
- Sequential flow diagram
- Component icons
- Data transformation at each step
- Example data snippets
- Timing/latency indicators

**Size:** 1400x900px

**Source:** [RAG Patterns](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/use-your-data)

**Used In:**
- `docs/level-100/edge-rag-architecture.html`
- `docs/level-100/rag-fundamentals.html`

---

## Visual Asset Summary

### Total Assets by Module
- **Module 1 (Digital Sovereignty):** 7 assets (previously documented)
- **Module 2 (Sovereign Cloud Models):** 3 assets (previously documented)
- **Module 3 (Azure Local):** 3 assets ✅ NEWLY DOCUMENTED
- **Module 4 (Azure Arc):** 3 assets ✅ NEWLY DOCUMENTED
- **Module 5 (Edge RAG):** 4 assets ✅ NEWLY DOCUMENTED

**Total Level 100 Assets:** 20 diagrams
**Status:** All specifications documented, 0 created (creation is next phase)

### Priority Distribution
- **High Priority:** 8 assets (core concepts, architecture diagrams)
- **Medium Priority:** 10 assets (supporting visualizations)
- **Low Priority:** 2 assets (supplementary materials)

---

## LEVEL 200 - INTERMEDIATE: VISUAL ASSETS

### Module 1: Azure Local Architecture Deep Dive

#### Asset 21: Advanced Networking Architecture
**File:** `level-200/azure-local-advanced-networking.svg`  
**Priority:** High  
**Status:** 🔴 Needed

**Description:** Detailed networking architecture showing SET configuration, VLAN organization, RDMA optimization, and network topology for enterprise Azure Local deployments.

**Content:**
- Switch Embedded Teaming (SET) configuration with multiple NICs
- VLAN segmentation (management, storage, cluster, customer VLANs)
- RDMA network topology
- Network adapter teaming and failover paths
- Physical and virtual NIC mapping
- Bandwidth allocation and QoS policies

**Visual Elements:**
- Physical server with multiple network adapters
- Virtual switch diagram showing SET teams
- VLAN color-coded flows (management blue, storage orange, cluster green)
- RDMA acceleration overlay (separate path)
- Redundancy indicators (dual switches, failover paths)
- Legend for adapter types

**Size:** 1400x1000px

**Used In:**
- `docs/level-200/azure-local-advanced-networking.md`
- `docs/level-200/azure-local-architecture-deep-dive.md`

**Source Refs:** [SET Documentation](https://learn.microsoft.com/en-us/azure/azure-local/plan/cloud-deployment-network-considerations?view=azloc-2509), [RDMA Configuration](https://learn.microsoft.com/en-us/azure/azure-local/concepts/system-requirements#network-requirements)

---

#### Asset 22: High-Availability Architecture
**File:** `level-200/azure-local-ha-architecture.svg`  
**Priority:** High  
**Status:** 🔴 Needed

**Description:** Complete HA architecture showing multi-node cluster topology, quorum configuration, storage resilience, and failover mechanisms.

**Content:**
- 3-node or 4-node cluster layout
- Quorum witness location and types (disk, file share, cloud)
- Storage Spaces Direct redundancy (2-way mirror, 3-way mirror, erasure coding)
- Node failure scenarios and recovery
- Replication paths and latency considerations
- Automatic failover indicators

**Visual Elements:**
- Cluster nodes arranged in circle/triangle
- Storage connections showing replication
- Quorum placement options (highlighted)
- Failure scenarios with recovery paths
- Color coding: Active (green), Standby (yellow), Failed (red)
- RTO/RPO indicators

**Size:** 1300x900px

**Used In:**
- `docs/level-200/azure-local-ha-patterns.md`
- `docs/level-200/azure-local-architecture-deep-dive.md`

**Source Refs:** [HA Patterns](https://learn.microsoft.com/en-us/azure/azure-local/deploy/create-cluster), [Quorum Configuration](https://learn.microsoft.com/en-us/azure/azure-local/concepts/quorum)

---

#### Asset 23: Hardware Planning Decision Tree
**File:** `level-200/azure-local-hardware-decision-tree.svg`  
**Priority:** Medium  
**Status:** 🔴 Needed

**Description:** Interactive decision flowchart to guide hardware selection based on customer requirements (performance, capacity, redundancy, budget).

**Content:**
- Starting point: "What are your workload requirements?"
- Decision nodes:
  - Performance tier? (Tier 1, 2, 3)
  - Capacity requirement? (Storage in TB, VM density)
  - Redundancy level? (2-way, 3-way mirror, erasure coding)
  - Budget constraint?
  - Geographic/climate requirements?
- Endpoints: Specific recommended configurations with BOM

**Visual Elements:**
- Diamond decision nodes with yes/no branches
- Color-coded paths
- Configuration recommendations at endpoints
- Cost/performance indicators
- Icons for each decision type

**Size:** 1200x1400px (vertical flow)

**Used In:**
- `docs/level-200/azure-local-hardware-planning.md`

**Source Refs:** [Validated Hardware](https://learn.microsoft.com/en-us/azure/azure-local/deploy/deployment-prerequisites?view=azloc-2509)

---

### Module 2: Arc Advanced Management

#### Asset 24: Arc Governance Framework
**File:** `level-200/arc-governance-framework.svg`  
**Priority:** High  
**Status:** 🔴 Needed

**Description:** Multi-layer governance and compliance framework showing policy hierarchy, role-based access control (RBAC), and compliance monitoring across Arc-managed resources.

**Content:**
- Policy layers: Tenant → Subscription → Resource Group → Resource
- RBAC role hierarchy
- Policy application pathways
- Compliance monitoring feedback loops
- Non-compliance remediation flows
- Audit trail and reporting

**Visual Elements:**
- Hierarchical pyramid or layered diagram
- Policy flow arrows showing inheritance and enforcement
- RBAC role boxes with icons
- Compliance status indicators (compliant/non-compliant)
- Remediation loops with arrows
- Dashboard/reporting callouts

**Size:** 1300x900px

**Used In:**
- `docs/level-200/arc-policy-and-governance.md`
- `docs/level-200/arc-advanced-management.md`

**Source Refs:** [Arc Governance](https://learn.microsoft.com/en-us/azure/azure-arc/servers/security-overview), [Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/overview)

---

#### Asset 25: Arc Cost Optimization Flows
**File:** `level-200/arc-cost-optimization.svg`  
**Priority:** Medium  
**Status:** 🔴 Needed

**Description:** Cost flow diagram showing resource allocation, licensing models, and cost reduction strategies across Arc infrastructure.

**Content:**
- Resource consumption flows (compute, storage, bandwidth)
- Licensing model options (Arc servers, data services, hybrid benefit)
- Cost reduction strategies:
  - Reserved instances
  - Spot VMs
  - Hybrid benefits (Azure Hybrid Benefit, SQL Server)
  - Right-sizing recommendations
- Cost analytics and chargeback models

**Visual Elements:**
- Dollar flow diagram showing allocation
- Multiple optimization paths
- Percentage savings indicators
- Cost lever callouts
- Before/after cost comparison

**Size:** 1200x800px

**Used In:**
- `docs/level-200/arc-cost-optimization.md`

**Source Refs:** [Arc Pricing](https://azure.microsoft.com/en-us/pricing/details/azure-arc/), [Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/)

---

#### Asset 26: Enterprise Deployment Topology
**File:** `level-200/arc-enterprise-deployment.svg`  
**Priority:** High  
**Status:** 🔴 Needed

**Description:** Multi-site enterprise deployment showing Arc managing diverse infrastructure across data centers, branch offices, and edge locations with centralized governance.

**Content:**
- Multiple geographic sites (HQ data center, branch office, retail edge, mobile)
- Arc-enabled resources at each site
- Central management plane in Azure
- Network connectivity (direct, hybrid, satellite/intermittent)
- Management agent communication patterns
- Hybrid connectivity options (ExpressRoute, VPN, Kubernetes API server)

**Visual Elements:**
- Geographic site distribution
- Site-specific resource clusters
- Central management dashboard
- Network connection types with latency indicators
- Agent communication paths
- Resilience indicators (online/offline status)

**Size:** 1400x900px

**Used In:**
- `docs/level-200/arc-enterprise-patterns.md`
- `docs/level-200/arc-advanced-management.md`

**Source Refs:** [Arc at Scale](https://learn.microsoft.com/en-us/azure/azure-arc/servers/onboard-group-policy-powershell), [Hybrid Connectivity](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/hybrid/)

---

### Module 3: Edge RAG Implementation

#### Asset 27: Production RAG Architecture (Detailed)
**File:** `level-200/edge-rag-production-architecture.svg`  
**Priority:** High  
**Status:** 🔴 Needed

**Description:** Full production-grade Edge RAG architecture showing high-availability setup, load balancing, persistence, monitoring, and optional cloud sync.

**Content:**
- Load balancer/ingress layer
- Multiple RAG service replicas (for HA)
- Vector database (Weaviate) with replication and backup
- LLM inference services (Ollama) with multiple model instances
- Data ingestion pipeline with queue
- Monitoring and logging stack
- Optional cloud sync layer (dashed)
- Storage persistence layers (local, backup, archive)

**Visual Elements:**
- Layered architecture diagram
- Service replicas and redundancy
- Data flow paths (ingestion, query, inference, monitoring)
- Storage and backup indicated
- Color coding: Application (blue), AI/ML (purple), Infrastructure (gray), Monitoring (orange)
- Optional/cloud components in dashed lines

**Size:** 1400x1100px

**Used In:**
- `docs/level-200/edge-rag-implementation.md`
- `docs/level-200/rag-deployment-strategies.md`

**Source Refs:** [Weaviate Deployment](https://weaviate.io/blog/how-to-deploy-weaviate), [Ollama Production Setup](https://github.com/ollama/ollama)

---

#### Asset 28: LLM Inference Optimization
**File:** `level-200/llm-inference-optimization.svg`  
**Priority:** High  
**Status:** 🔴 Needed

**Description:** Optimization strategies for LLM inference showing quantization, batching, caching, and hardware acceleration techniques.

**Content:**
- Model optimization techniques:
  - Full precision (FP32) → Quantization (INT8, INT4, mixed precision)
  - Model size comparisons and latency/accuracy tradeoffs
- Inference optimization strategies:
  - Request batching and queue management
  - KV cache for multi-turn conversations
  - Hardware acceleration paths (CPU, GPU, TPU, NPU)
- Performance metrics impact: latency, throughput, accuracy

**Visual Elements:**
- Model pipeline showing optimization stages
- Branching paths for different optimization techniques
- Performance indicators (latency axis, throughput axis)
- Hardware acceleration options with performance curves
- Tradeoff visualization (accuracy vs. speed)
- Resource consumption heatmap

**Size:** 1300x900px

**Used In:**
- `docs/level-200/llm-inference-optimization.md`

**Source Refs:** [LLM Optimization](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/model-versions), [Ollama Quantization](https://ollama.ai)

---

#### Asset 29: Vector Database Architecture Comparison
**File:** `level-200/vector-db-comparison.svg`  
**Priority:** Medium  
**Status:** 🔴 Needed

**Description:** Comparison of vector database options for edge deployments showing architecture, performance characteristics, and deployment considerations.

**Content:**
- Three columns: Weaviate | Milvus | PostgreSQL+pgvector
- Comparison dimensions:
  - Architecture (embedded, standalone, distributed)
  - Indexing method (HNSW, IVF, scalar quantization)
  - Query latency and throughput
  - Memory footprint
  - High availability options
  - Backup/recovery capabilities
  - Cost model

**Visual Elements:**
- Clean three-column layout
- Architecture diagrams for each
- Performance comparison charts
- Feature matrix with checkmarks
- Recommended use cases for each

**Size:** 1400x1000px

**Used In:**
- `docs/level-200/vector-databases-edge.md`

**Source Refs:** [Vector Database Comparison](https://learn.microsoft.com/en-us/semantic-kernel/concepts/vector-store-connectors/), [Weaviate vs. Milvus](https://weaviate.io)

---

#### Asset 30: RAG Deployment Topology Options
**File:** `level-200/rag-deployment-topologies.svg`  
**Priority:** Medium  
**Status:** 🔴 Needed

**Description:** Multiple RAG deployment topology options for different customer scenarios and scale requirements.

**Content:**
- Option 1: Single-node edge (development/small scale)
- Option 2: High-availability cluster (production)
- Option 3: Multi-site federation (geographic distribution)
- Option 4: Hybrid cloud+edge (optional cloud sync)
- For each: architecture, latency profile, failover capabilities, cost

**Visual Elements:**
- Four topology diagrams arranged in grid
- Use case labels
- Latency/throughput characteristics
- Failover and HA capabilities
- Cost per option
- Scaling path indicators

**Size:** 1400x900px

**Used In:**
- `docs/level-200/rag-deployment-strategies.md`

**Source Refs:** [RAG Patterns](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/use-your-data)

---

#### Asset 31: RAG Monitoring and Observability
**File:** `level-200/rag-monitoring-observability.svg`  
**Priority:** Medium  
**Status:** 🔴 Needed

**Description:** Comprehensive monitoring and observability architecture for production RAG systems showing metrics, logs, traces, and alerting flows.

**Content:**
- Data collection points (application, vector DB, LLM, infrastructure)
- Metrics collection (Prometheus style)
- Log aggregation (ELK, Azure Monitor)
- Distributed tracing
- Alert evaluation and routing
- Dashboard and reporting
- Feedback loop for continuous improvement

**Visual Elements:**
- Data collection arrows from all components
- Processing pipelines for metrics/logs/traces
- Alert evaluation and escalation flows
- Visualization layer (dashboards, reports)
- Feedback loop back to RAG system
- Color coding: Data flow (blue), Processing (gray), Visualization (green)

**Size:** 1300x900px

**Used In:**
- `docs/level-200/rag-operations-monitoring.md`

**Source Refs:** [Observability](https://learn.microsoft.com/en-us/azure/architecture/best-practices/monitoring), [OpenTelemetry](https://opentelemetry.io)

---

### Module 4: Pre-Sales & Solution Design

#### Asset 32: Customer Discovery Framework
**File:** `level-200/customer-discovery-framework.svg`  
**Priority:** Medium  
**Status:** 🔴 Needed

**Description:** Structured customer discovery process showing key questions, evaluation criteria, and decision points for sovereign cloud solutions.

**Content:**
- Discovery phases:
  1. Business objectives and drivers
  2. Technical requirements and constraints
  3. Regulatory and compliance requirements
  4. Budget and timeline
  5. Success criteria and KPIs
- Key questions for each phase
- Customer pain point mapping
- Decision tree leading to solution recommendation

**Visual Elements:**
- Funnel or circular discovery process
- Question callouts for each phase
- Decision points with branching paths
- Customer profile building as information accumulates

**Size:** 1200x800px

**Used In:**
- `docs/level-200/customer-discovery.md`
- `docs/level-200/presales-solution-design.md`

---

#### Asset 33: Solution Sizing Framework
**File:** `level-200/solution-sizing-framework.svg`  
**Priority:** Medium  
**Status:** 🔴 Needed

**Description:** Interactive sizing process showing how to translate customer requirements into infrastructure specifications and cost estimates.

**Content:**
- Input variables: workload type, user count, data volume, growth projection
- Calculation layers: compute sizing, storage sizing, network bandwidth
- Output: infrastructure recommendation with redundancy/HA options
- Cost calculation and ROI analysis

**Visual Elements:**
- Input boxes at top
- Calculation flows showing multipliers and formulas
- Decision points for HA/redundancy
- Output configurations with cost
- Confidence intervals/ranges shown

**Size:** 1300x800px

**Used In:**
- `docs/level-200/solution-sizing.md`

---

#### Asset 34: TCO and ROI Analysis Model
**File:** `level-200/tco-roi-model.svg`  
**Priority:** Medium  
**Status:** 🔴 Needed

**Description:** Total Cost of Ownership and Return on Investment comparison framework for sovereign vs. standard cloud solutions.

**Content:**
- TCO cost categories (hardware, licensing, operations, personnel)
- TCO timeline (3-year, 5-year models)
- ROI drivers (agility, compliance enablement, data value, risk reduction)
- Break-even analysis and payback period
- Competitive positioning (Azure Local vs. competitors)
- Sensitivity analysis (what-if scenarios)

**Visual Elements:**
- Stacked cost breakdown chart
- TCO trend lines over time
- ROI waterfall showing benefits realization
- Sensitivity tornado chart
- Competitive landscape overlay

**Size:** 1400x900px

**Used In:**
- `docs/level-200/cost-estimation.md`

---

### Module 5: Compliance & Security Patterns

#### Asset 35: GDPR Compliance Mapping
**File:** `level-200/gdpr-compliance-mapping.svg`  
**Priority:** High  
**Status:** 🔴 Needed

**Description:** Detailed mapping of GDPR requirements to Azure Local, Arc, and Edge RAG technical controls.

**Content:**
- GDPR principles: lawfulness, fairness, transparency, integrity, confidentiality
- Key requirements: data processing, consent, right to access, right to erasure, DPA, breach notification
- Azure Local controls addressing each requirement (encryption, access control, audit logging)
- Arc management controls (policy, governance, monitoring)
- Compliance evidence collection and reporting

**Visual Elements:**
- Left: GDPR requirements hierarchy
- Center: Technical controls and Azure services
- Right: Compliance evidence/audit trail
- Color-coded requirement satisfaction (green checkmark)
- References to specific controls (Data Residency, encryption, RBAC)

**Size:** 1400x900px

**Used In:**
- `docs/level-200/gdpr-implementation.md`
- `docs/level-200/compliance-security-patterns.md`

**Source Refs:** [GDPR in Azure](https://learn.microsoft.com/en-us/compliance/regulatory/gdpr), [EU Data Boundary](https://learn.microsoft.com/en-us/privacy/eudb/eu-data-boundary-learn)

---

#### Asset 36: FedRAMP Compliance Architecture
**File:** `level-200/fedramp-compliance-architecture.svg`  
**Priority:** High  
**Status:** 🔴 Needed

**Description:** FedRAMP compliance architecture showing security control families, Azure Local configuration for FedRAMP compliance, and validation points.

**Content:**
- 14 FedRAMP security control families
- Azure Local architectural components addressing each family
- Confidentiality, Integrity, Availability (C-I-A) across layers
- Encryption (in-transit, at-rest, in-use)
- Access controls and audit logging
- System security plans and continuous monitoring
- Assessment and authorization process

**Visual Elements:**
- Control family categories with icons
- Layered architecture showing control implementation
- C-I-A indicators for each layer
- Compliance assessment steps
- Authority to Operate (ATO) roadmap

**Size:** 1400x1000px

**Used In:**
- `docs/level-200/fedramp-compliance.md`

**Source Refs:** [FedRAMP Requirements](https://www.fedramp.gov/documents-repository/), [Azure Government FedRAMP Services](https://learn.microsoft.com/en-us/azure/azure-government/compliance/azure-services-in-fedramp-auditscope)

---

#### Asset 37: Encryption and Key Management Architecture
**File:** `level-200/encryption-key-mgmt-architecture.svg`  
**Priority:** High  
**Status:** 🔴 Needed

**Description:** Comprehensive encryption and key management architecture for sovereign cloud deployments showing key lifecycle, HSM integration, and customer-controlled keys.

**Content:**
- Encryption layers: data at-rest (OS, application data, backups), in-transit (TLS), in-use (confidential computing)
- Key hierarchy: tenant keys, data encryption keys, master keys
- Key management lifecycle: generation, rotation, revocation, archival
- Azure Key Vault integration (cloud-based)
- Customer-managed keys (BYOK) and Bring Your Own HSM (BYOHSM)
- Hardware Security Module (HSM) options
- Key access controls and audit

**Visual Elements:**
- Encryption layer stack
- Key hierarchy pyramid
- Key lifecycle flowchart
- Management plane showing Key Vault and HSM
- Access control points with authentication indicators

**Size:** 1400x1000px

**Used In:**
- `docs/level-200/encryption-key-management.md`

**Source Refs:** [Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/overview), [Encryption at Rest](https://learn.microsoft.com/en-us/azure/security/fundamentals/encryption-atrest)

---

#### Asset 38: Zero-Trust Security Architecture
**File:** `level-200/zero-trust-architecture.svg`  
**Priority:** High  
**Status:** 🔴 Needed

**Description:** Zero-Trust security model implementation for sovereign cloud showing "never trust, always verify" principles applied to identities, devices, networks, and applications.

**Content:**
- Zero-Trust pillars:
  1. Verify explicitly (authentication, authorization, attributes)
  2. Assume breach (detection, response, minimal access)
  3. Secure every layer (identity, endpoints, networks, data, applications)
- Control areas: Identity & Access, Endpoints, Networks, Data, Applications
- Azure implementations: Microsoft Entra ID, Conditional Access, Azure AD B2C, Network Security Groups, encryption

**Visual Elements:**
- Core Zero-Trust concept (verify icon in center)
- Five pillar rings surrounding core
- Control areas with specific Azure services
- Detection and response loops
- Least-privilege access indicators

**Size:** 1300x1000px

**Used In:**
- `docs/level-200/compliance-security-patterns.md`

**Source Refs:** [Zero-Trust Architecture](https://learn.microsoft.com/en-us/security/zero-trust/), [Azure Security Best Practices](https://learn.microsoft.com/en-us/azure/security/)

---

### Module 6: Hands-On Labs

#### Asset 39: Lab Architecture Progression
**File:** `level-200/labs-architecture-progression.svg`  
**Priority:** Medium  
**Status:** 🔴 Needed

**Description:** Visual showing how each lab builds on previous, creating an integrated infrastructure by Lab 5.

**Content:**
- Lab 1: Azure Local cluster setup (foundation)
- Lab 2: Arc integration on Lab 1 cluster (management plane)
- Lab 3: Edge RAG deployment on Lab 1 cluster (application layer)
- Lab 4: Governance policies applied to Labs 1-3 (control layer)
- Lab 5: Monitoring across all Labs 1-4 (observability layer)
- Cumulative architecture at each stage
- Dependencies and data flow

**Visual Elements:**
- Five stages showing progressive architecture
- Dependency arrows showing which labs depend on prior labs
- Color coding: Infrastructure (Lab 1), Management (Lab 2), Application (Lab 3), Governance (Lab 4), Observability (Lab 5)
- Cumulative resource growth visualization
- Cost and time estimates at each stage

**Size:** 1400x900px

**Used In:**
- `docs/level-200/labs-overview.md`

---

#### Asset 40: Lab Environment Cost and Time Matrix
**File:** `level-200/labs-cost-time-matrix.svg`  
**Priority:** Low  
**Status:** 🔴 Needed

**Description:** Matrix showing estimated costs and duration for each lab and cumulative totals.

**Content:**
- Lab-by-lab breakdown:
  - Estimated duration (hours)
  - Azure resource costs (daily, total)
  - Hardware/infrastructure costs
  - Cumulative totals
- Cost breakdown by resource type (compute, storage, networking)
- Timeline visualization (gantt-style)
- Variables affecting cost (region, resource sizing, duration)

**Visual Elements:**
- Data table with visual encodings (color for cost ranges, bar charts for duration)
- Cumulative trend lines
- Cost breakdown pie charts
- Timeline bar chart

**Size:** 1200x800px

**Used In:**
- `docs/level-200/labs-overview.md`

---

## Level 200 Visual Assets Summary

### Total Level 200 Assets: 20 diagrams
- **Module 1 (Azure Local Advanced):** 3 assets
- **Module 2 (Arc Advanced Management):** 3 assets
- **Module 3 (Edge RAG Implementation):** 5 assets
- **Module 4 (Pre-Sales & Solution Design):** 3 assets
- **Module 5 (Compliance & Security Patterns):** 4 assets
- **Module 6 (Hands-On Labs):** 2 assets

### Priority Distribution (Level 200)
- **High Priority:** 9 assets (core architectures, compliance frameworks)
- **Medium Priority:** 10 assets (supporting and reference materials)
- **Low Priority:** 1 asset (supplementary matrix)

### Total Project Assets (Levels 100 + 200)
- **Level 100:** 20 diagrams (100% specified, 0% created)
- **Level 200:** 20 diagrams (100% specified, 0% created)
- **Level 300:** TBD (estimated 15-20 diagrams)
- **TOTAL:** 40+ diagrams planned across current levels

---

## Design Guidelines

### Style Guide
**Colors:**
- Microsoft Blue: #0078D4
- Azure colors: Various blues
- Success/Active: #107C10 (green)
- Warning: #FFB900 (yellow)
- Error/Critical: #D83B01 (red/orange)
- Neutral: #605E5C (gray)

**Typography:**
- Primary: Segoe UI or similar sans-serif
- Headings: Bold, 16-24pt
- Body text: Regular, 10-14pt
- Labels: 8-12pt

**Diagram Elements:**
- Clean, minimalist design
- Consistent icon style
- Clear hierarchy
- Adequate whitespace
- Color-blind friendly palette

### File Specifications
- **Format:** SVG (scalable, web-friendly)
- **Resolution:** Optimized for 96 DPI screens
- **Size:** As specified per asset (typically 1200x800 to 1400x1000px)
- **Optimization:** Minified SVG for web delivery
- **Accessibility:** Include alt text descriptions

---

## Creation Workflow

1. **Review Specifications:** Read full specification for each asset
2. **Gather References:** Review linked Microsoft Learn documentation
3. **Design Draft:** Create initial design following style guide
4. **Review:** Validate against content requirements
5. **Refine:** Incorporate feedback
6. **Optimize:** Minify SVG, ensure accessibility
7. **Integrate:** Place in appropriate directory, update references

---

## Tools and Resources

**Design Tools:**
- **draw.io / diagrams.net:** Free, web-based
- **Figma:** Collaborative, professional
- **Adobe Illustrator:** Professional, paid
- **Inkscape:** Free, desktop-based
- **Microsoft Visio:** Enterprise diagramming

**Icon Resources:**
- [Azure Architecture Icons](https://learn.microsoft.com/en-us/azure/architecture/icons/)
- [Microsoft 365 Icons](https://developer.microsoft.com/en-us/fluentui#/styles/web/icons)
- [Font Awesome](https://fontawesome.com/) (for generic icons)

**Templates:**
- [Azure Architecture Diagrams](https://learn.microsoft.com/en-us/azure/architecture/browse/)
- [Microsoft PowerPoint templates](https://www.microsoft.com/en-us/download/details.aspx?id=41937)

---

---

## Asset Documentation Status

### Current Status Summary

| Level | Modules | Diagrams | Documented | Specified | Placeholders | Created | Status |
|-------|---------|----------|------------|-----------|--------------|---------|--------|
| **100** | 5 | 20 | 20 (100%) | 20 (100%) | 20 (100%) | 0 (0%) | � Ready for Creation |
| **200** | 6 | 20 | 20 (100%) | 20 (100%) | 20 (100%) | 0 (0%) | � Ready for Creation |
| **300** | TBD | ~15-20 | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) | ⚪ Not Started |
| **TOTAL** | 11+ | 55+ | 40 (73%) | 40 (100% of L100/L200) | 40 (100% of L100/L200) | 0 (0%) | 🔄 In Progress |

### Key Metrics

- **Total Specifications Documented:** 40 (Levels 100 & 200)
- **Total Specifications Detailed:** 40 (Levels 100 & 200 with full briefs)
- **Assets with Placeholder Integration:** 40 (100% of Levels 100 & 200)
- **Assets Ready for Creation:** 40 (100% of Levels 100 & 200)
- **Estimated Creation Hours:**
  - Level 100: 14-16 hours (20 diagrams @ 0.7-0.8 hrs each)
  - Level 200: 16-18 hours (20 diagrams @ 0.8-0.9 hrs each)
  - **Total:** 30-34 hours to create all documented visual assets

### Phase Progress

**Phase 1: Documentation** ✅ COMPLETE
- Level 100: 20 assets documented (COMPLETE)
- Level 200: 20 assets documented (COMPLETE)
- 3-step workflow for visual asset creation

**Phase 2: Detailed Specifications** ✅ COMPLETE
- Level 100: 20 detailed briefs in `docs/level-100/VISUAL_SPECIFICATIONS.md` (COMPLETE)
- Level 200: 20 detailed briefs in `docs/level-200/VISUAL_SPECIFICATIONS.md` (COMPLETE)

**Phase 3: Content Placeholder Integration** ✅ COMPLETE
- Level 100: 20 asset placeholders added to 12 markdown files (COMPLETE)
- Level 200: 20 asset placeholders added to 22 markdown files (COMPLETE)

**Phase 4: Asset Creation** 🔄 QUEUED
- Level 100: Awaiting designer/creator (30-34 total hours for both levels, estimated 3-4 week timeline)
- Level 200: Awaiting designer/creator
- Designer Handoff: See `VISUAL_SPECIFICATIONS.md` files in each level folder

---

## Level 300 - Advanced Technical

### Module 1: Zero Trust Security for Sovereign Cloud

#### Asset 41: Zero Trust Security Pillars
**File:** `level-300/zero-trust-pillars.svg`  
**Priority:** High  
**Status:** 🟡 Specified (Ready for Creation)

**Description:** The six pillars of Zero Trust security model applied to sovereign cloud environments with specific examples and implementation points.

**Used In:** `docs/level-300/zero-trust.md`  
**Source Refs:** [Zero Trust Architecture](https://learn.microsoft.com/en-us/security/zero-trust/)

---

#### Asset 42: Sovereign Cloud Zero Trust Comparison
**File:** `level-300/zero-trust-sovereign-comparison.svg`  
**Priority:** High  
**Status:** 🟡 Specified (Ready for Creation)

**Description:** Side-by-side comparison showing how Zero Trust implementation differs across sovereign cloud deployment models.

**Used In:** `docs/level-300/zero-trust.md`  
**Source Refs:** [Cloud models comparison](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-area/identity-access)

---

#### Asset 43: Zero Trust Implementation Architecture
**File:** `level-300/zero-trust-implementation-architecture.svg`  
**Priority:** High  
**Status:** 🟡 Specified (Ready for Creation)

**Description:** Complete end-to-end architecture showing Zero Trust implementation components and interactions in sovereign environments.

**Used In:** `docs/level-300/zero-trust-architecture.md`  
**Source Refs:** [Azure Architecture Reference](https://learn.microsoft.com/en-us/azure/architecture/)

---

#### Asset 44: Defense-in-Depth Strategy
**File:** `level-300/defense-in-depth-layers.svg`  
**Priority:** High  
**Status:** 🟡 Specified (Ready for Creation)

**Description:** Defense-in-depth security model showing multiple overlapping security layers and control points across infrastructure.

**Used In:** `docs/level-300/zero-trust-architecture.md`  
**Source Refs:** [Defense-in-depth strategy](https://learn.microsoft.com/en-us/security/zero-trust/)

---

#### Asset 45: Compliance Mapping - Zero Trust to Frameworks
**File:** `level-300/compliance-zero-trust-mapping.svg`  
**Priority:** Medium  
**Status:** 🟡 Specified (Ready for Creation)

**Description:** Matrix showing how Zero Trust controls map to compliance frameworks (FedRAMP, GDPR, HIPAA, ITAR).

**Used In:** `docs/level-300/zero-trust-architecture.md`  
**Source Refs:** [Compliance in Azure](https://learn.microsoft.com/en-us/compliance/)

---

### Module 2: Azure Local - Connected Mode at Scale

#### Asset 46: Multi-Site Azure Local Deployment Topologies
**File:** `level-300/multi-site-topologies.svg`  
**Priority:** High  
**Status:** 🟡 Specified (Ready for Creation)

**Description:** Three deployment topology patterns for multi-site Azure Local deployments with architecture, failover, and governance implications.

**Used In:** `docs/level-300/azure-local-multi-site.md`  
**Source Refs:** [Azure Local deployment patterns](https://learn.microsoft.com/en-us/azure/azure-local/)

---

#### Asset 47: Connected Mode Networking Architecture
**File:** `level-300/connected-mode-networking.svg`  
**Priority:** Medium  
**Status:** 🟡 Specified (Ready for Creation)

**Description:** Complete networking architecture for connected-mode Azure Local showing cloud connectivity, inter-site communication, and edge networking.

**Used In:** `docs/level-300/azure-local-networking-advanced.md`  
**Source Refs:** [Azure networking](https://learn.microsoft.com/en-us/azure/networking/)

---

#### Asset 48: Multi-Site Failover & Recovery Procedures
**File:** `level-300/multi-site-failover-procedures.svg`  
**Priority:** Medium  
**Status:** 🟡 Specified (Ready for Creation)

**Description:** Flowchart showing failover detection, execution, and recovery procedures for multi-site deployments.

**Used In:** `docs/level-300/azure-local-connected-lab.md`  
**Source Refs:** [Disaster recovery](https://learn.microsoft.com/en-us/azure/azure-local/)

---

### Module 3: Azure Local - Disconnected Mode

#### Asset 49: Air-Gapped Architecture Pattern
**File:** `level-300/air-gapped-architecture.svg`  
**Priority:** High  
**Status:** 🟡 Specified (Ready for Creation)

**Description:** Complete air-gapped Azure Local deployment showing isolated network zones, air-gap boundaries, and secure transfer mechanisms.

**Used In:** `docs/level-300/azure-local-air-gapped.md`  
**Source Refs:** [Disconnected operations](https://learn.microsoft.com/en-us/azure/azure-local/manage/disconnected-operations-overview)

---

#### Asset 50: Manual Update Flow - Disconnected
**File:** `level-300/manual-update-flow.svg`  
**Priority:** High  
**Status:** 🟡 Specified (Ready for Creation)

**Description:** Step-by-step process showing export, secure transfer, validation, and import of updates in air-gapped systems.

**Used In:** `docs/level-300/azure-local-disconnected-lab.md`  
**Source Refs:** [Manual update procedures](https://learn.microsoft.com/en-us/azure/azure-local/update/about-updates-23h2?view=azloc-2509-disconnected)

---

#### Asset 51: Certificate Lifecycle Management
**File:** `level-300/certificate-lifecycle.svg`  
**Priority:** Medium  
**Status:** 🟡 Specified (Ready for Creation)

**Description:** Timeline showing certificate issuance, validity periods, renewal windows, and key procedures for disconnected environments.

**Used In:** `docs/level-300/azure-local-certificate-management.md`  
**Source Refs:** [Certificate lifecycle](https://learn.microsoft.com/en-us/azure/azure-local/manage/manage-secrets-rotation?view=azloc-2509)

---

### Module 4: Production Edge RAG at Scale

#### Asset 52: Production RAG Architecture
**File:** `level-300/production-rag-architecture.svg`  
**Priority:** High  
**Status:** 🟡 Specified (Ready for Creation)

**Description:** Enterprise-scale Retrieval-Augmented Generation system showing ingestion, retrieval, inference, and monitoring components.

**Used In:** `docs/level-300/edge-rag-architecture-production.md`  
**Source Refs:** [RAG architecture](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview)

---

#### Asset 53: Performance Optimization Strategies & Trade-offs
**File:** `level-300/rag-optimization-matrix.svg`  
**Priority:** High  
**Status:** 🟡 Specified (Ready for Creation)

**Description:** Decision matrix showing optimization approaches with performance vs resource utilization trade-offs.

**Used In:** `docs/level-300/edge-rag-optimization.md`  
**Source Refs:** [ML optimization](https://learn.microsoft.com/en-us/azure/machine-learning/)

---

#### Asset 54: MLOps Pipeline for Edge RAG
**File:** `level-300/mlops-edge-pipeline.svg`  
**Priority:** High  
**Status:** 🟡 Specified (Ready for Creation)

**Description:** End-to-end MLOps workflow showing model training, validation, deployment, monitoring, and retraining triggers.

**Used In:** `docs/level-300/edge-rag-mlops.md`  
**Source Refs:** [MLOps](https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment)

---

#### Asset 55: Vector Database Comparison - Edge Deployment
**File:** `level-300/vector-database-comparison.svg`  
**Priority:** Medium  
**Status:** 🟡 Specified (Ready for Creation)

**Description:** Comparison matrix of vector database options for edge deployment showing capabilities, performance, and deployment requirements.

**Used In:** `docs/level-300/edge-rag-production-lab.md`  
**Source Refs:** [Vector search](https://learn.microsoft.com/en-us/azure/search/vector-search-overview)

---

#### Asset 56: RAG Quality Metrics & Observability
**File:** `level-300/rag-quality-metrics.svg`  
**Priority:** Medium  
**Status:** 🟡 Specified (Ready for Creation)

**Description:** Framework showing quality metrics, observability points, and monitoring dashboards for production RAG systems.

**Used In:** `docs/level-300/edge-rag-production-lab.md`  
**Source Refs:** [Monitoring and diagnostics](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-monitor-model-performance)

---

### Module 5: Advanced Troubleshooting & Optimization

#### Asset 57: Troubleshooting Decision Tree
**File:** `level-300/troubleshooting-decision-tree.svg`  
**Priority:** High  
**Status:** 🟡 Specified (Ready for Creation)

**Description:** Interactive flowchart showing symptom classification, investigation paths, and diagnostic procedures.

**Used In:** `docs/level-300/troubleshooting-tools.md`  
**Source Refs:** [Troubleshooting guide](https://learn.microsoft.com/en-us/troubleshoot/azure/)

---

#### Asset 58: Diagnostic Tools Reference Matrix
**File:** `level-300/diagnostic-tools-matrix.svg`  
**Priority:** High  
**Status:** 🟡 Specified (Ready for Creation)

**Description:** Matrix showing diagnostic tools, capabilities, use cases, and output examples for troubleshooting.

**Used In:** `docs/level-300/troubleshooting-tools.md`  
**Source Refs:** [Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/overview)

---

#### Asset 59: Escalation Procedures & Support Workflow
**File:** `level-300/escalation-procedures.svg`  
**Priority:** Medium  
**Status:** 🟡 Specified (Ready for Creation)

**Description:** Process flowchart showing escalation paths, ticket routing, information requirements, and SLA expectations at each level.

**Used In:** `docs/level-300/troubleshooting-escalation.md`  
**Source Refs:** [Azure support options](https://learn.microsoft.com/en-us/support/azure/)

---

## Asset Documentation Status

### Current Status Summary

| Level | Modules | Diagrams | Documented | Specified | Placeholders | Created | Status |
|-------|---------|----------|------------|-----------|--------------|---------|--------|
| **100** | 5 | 20 | 20 (100%) | 20 (100%) | 20 (100%) | 0 (0%) | 🟡 Specified (Ready) |
| **200** | 6 | 20 | 20 (100%) | 20 (100%) | 20 (100%) | 0 (0%) | 🟡 Specified (Ready) |
| **300** | 5 | 19 | 19 (100%) | 19 (100%) | 19 (100%) | 0 (0%) | 🟡 Specified (Ready) |
| **TOTAL** | 16 | 59 | 59 (100%) | 59 (100%) | 59 (100%) | 0 (0%) | ✅ **READY FOR DESIGNER HANDOFF** |

---

## Visual Asset Creation Workflow (For Future Use)

### Recommended Process for Level 300 and Beyond

1. **Documentation Phase (Step #3)** - Current Template
   - Document all visual assets needed for the level in this README
   - Create comprehensive specifications for each diagram
   - Update summary tables with new counts
   - Set status to 🔴 Needed for all new assets
   - **Deliverable:** Complete specification becomes source of truth

2. **Specification Phase (Step #1)** - Detailed Planning
   - Create visual specs document referencing this README
   - Include detailed mockups or wireframes
   - Validate alignment with content
   - **Deliverable:** Ready for designer/creator

3. **Implementation Phase (Step #2)** - Content Integration
   - Add placeholder callouts to all content files
   - Link to asset specifications
   - Create ingestion pipeline for finished assets
   - **Deliverable:** Content ready for visual asset insertion

### How to Use This Template for Level 300

When creating Level 300 documentation:

1. **Before creating any content:** Follow Step #3 first
   - Document all required visual assets in this README
   - Use the Asset 21-40 structure as template
   - Maintain consistent formatting
   - Update summary tables

2. **While creating content:** Follow Step #1
   - Develop comprehensive specs in the marked sections
   - Include all required metadata (file, priority, status, description, content, visual elements, size, sources, usage)

3. **When integrating content:** Follow Step #2
   - Add placeholder callouts using Level 100/200 as template
   - Maintain visual reference consistency
   - Link back to asset specifications

---

**Last Updated:** October 2025
**Total Assets Documented:** 40 (20 Level 100 + 20 Level 200)
**Assets Created:** 0 (pending creation phase)
**Process Documentation:** Complete - 3-step workflow for future levels established
