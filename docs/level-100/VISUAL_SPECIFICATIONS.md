---
layout: default
title: Level 100 Visual Asset Specifications
nav_exclude: true
---

# Level 100 Visual Asset Specifications

Purpose: Detailed design briefs for all 20 Level 100 visual assets (Assets 1–20)
Created: October 21, 2025
Asset Registry: See `docs/assets/images/README.md` for short specs and usage

---

## Module 1: Digital Sovereignty Fundamentals

### Asset 1: Digital Sovereignty Spectrum

Context:
This diagram introduces the foundational concept that digital sovereignty exists on a spectrum from fully managed cloud to air-gapped, disconnected systems. Essential for all learners to understand the continuum of control vs. connectivity trade-offs.

Design Constraints:
- Canvas 900x400 px, 50px margins
- Use Microsoft color palette: Green (public) → Yellow (enhanced) → Orange (dedicated) → Red (isolated)
- Minimum font size 12pt for readability at 800px width
- Maintain WCAG AA color contrast ratios

Content Requirements:
- Horizontal spectrum/ladder with 5 levels
- Level 1: Standard Cloud (Azure Public)
- Level 2: Enhanced Cloud (Azure with sovereignty controls)
- Level 3: Dedicated Cloud (Azure Local Connected)
- Level 4: Isolated Cloud (Azure Local Disconnected)
- Level 5: Air-Gapped (Fully isolated systems)
- Progressive icons showing connectivity level at each step
- Text descriptions for each level (2-3 words max)

Visual Elements:
- Horizontal gradient bar or stepped ladder
- Icons representing connectivity (cloud, partial, on-prem, locked)
- Color progression left to right
- Small connectivity indicators (bidirectional arrows fade out toward right)
- Control level indicators (lock icons progress from open to secured)

Wireframe Guidance:
Left to right flow: Level 1 (full connectivity) → Level 5 (no connectivity). Top row: connectivity icons. Middle row: colored level boxes with brief labels. Bottom row: control level indicators. Legend on bottom.

Acceptance Criteria:
- [ ] All 5 levels clearly labeled and distinct
- [ ] Colors follow green→yellow→orange→red progression
- [ ] Connectivity icons show decreasing connectivity progression
- [ ] Control icons show increasing control progression
- [ ] Text descriptions are concise (max 3 words per level)
- [ ] Readable at 800px width
- [ ] Color contrasts meet WCAG AA standard
- [ ] Gradient or stepped appearance maintained in 1:1 scale
- [ ] Alt text describes progression and color meaning

Microsoft Learn Adaptation:
- Reference: https://learn.microsoft.com/en-us/azure/azure-local/deploy/deployment-introduction?view=azloc-2509
- Reference: https://learn.microsoft.com/en-us/industry/sovereign-cloud/
- Adapt Azure Local and sovereignty documentation concepts

---

### Asset 2: Azure Global Infrastructure Map

Context:
Shows Azure's global presence, emphasizing data center locations, regions, and the EU Data Boundary. Helps learners understand geographic distribution and data residency commitments.

Design Constraints:
- Canvas 1200x700 px
- Use realistic world map projection
- Focus on Azure-relevant regions
- Include EU Data Boundary as special region
- Minimize text overlays for clarity

Content Requirements:
- World map with simplified landmasses
- Azure regions marked by location (60+ regions conceptually)
- Key regions labeled: US, Europe, Asia, Government (US Gov), China (21Vianet)
- EU Data Boundary highlighted as special region
- Availability zones indicated where relevant
- Legend explaining symbols and colors

Visual Elements:
- World map base layer (light gray)
- Region markers with custom icons (Azure blue circles)
- EU Data Boundary as distinct outline (green boundary)
- Government regions marked separately (US Gov: darker blue)
- China regions marked separately (orange)
- Scale indicators for scale reference

Wireframe Guidance:
Full world map. Cluster markers by region. EU boundary as highlighted polygon overlay. Legend on bottom right. Callout boxes for special regions (Gov, China).

Acceptance Criteria:
- [ ] World map clearly recognizable
- [ ] EU Data Boundary clearly highlighted
- [ ] Azure region locations accurate (major regions visible)
- [ ] Government and national cloud regions distinguished
- [ ] Color-coding consistent with Microsoft standards
- [ ] Legend explains all symbols
- [ ] Readable at mobile sizes (600px)
- [ ] No overwhelming text clutter
- [ ] Callout boxes explain special regions

Microsoft Learn Adaptation:
- Reference: https://azure.microsoft.com/en-us/explore/global-infrastructure/
- Reference: https://datacenters.microsoft.com/globe/explore
- Adapt from official Azure global infrastructure map

---

### Asset 3: EU Data Boundary Diagram

Context:
Explains Microsoft's commitment to keep specified data within EU boundaries and how the Customer Lockbox provides control over exceptions. Critical for GDPR and EU compliance discussions.

Design Constraints:
- Canvas 1100x800 px
- Include visual representation of data flows
- Show exception scenario clearly
- Maintain Microsoft brand compliance

Content Requirements:
- EU/EEA geographic boundary (map outline or stylized)
- Data types that stay in EU (customer data, personal data, etc.)
- Arrow flows showing data containment
- Customer Lockbox explanation and workflow
- Exception scenarios (support, legal, security)
- Control mechanism (lockbox approval process)

Visual Elements:
- EU/EEA outline or highlighted region
- Data flow arrows entering and staying within boundary
- Lock icons for Customer Lockbox
- Exception paths with approval gates
- Color coding: Green (contained), Blue (managed), Orange (exception)
- Process flow showing lockbox workflow

Wireframe Guidance:
Top: EU boundary map. Center-left: data types entering with containment arrows. Center-right: Customer Lockbox control process. Bottom: exception workflow with approval gates. Callout boxes explaining key concepts.

Acceptance Criteria:
- [ ] EU/EEA boundary clearly defined
- [ ] Data containment concept visually clear
- [ ] Lockbox approval process shown step-by-step
- [ ] Exception scenarios depicted with approval gates
- [ ] Color scheme distinguishes contained vs. exception data
- [ ] Arrow flows are unambiguous
- [ ] Readable at 900px width
- [ ] Legend explains symbols and colors
- [ ] Legal/compliance accuracy reviewed

Microsoft Learn Adaptation:
- Reference: https://learn.microsoft.com/en-us/privacy/eudb/eu-data-boundary-learn
- Reference: https://www.microsoft.com/en-us/trust-center/privacy/european-data-boundary
- Use official EU Data Boundary documentation as source

---

### Asset 4: Data Residency vs. Sovereignty Comparison

Context:
A fundamental distinction for learners: data residency is location-only, while sovereignty adds control and jurisdiction. This diagram makes the distinction clear through side-by-side comparison.

Design Constraints:
- Canvas 1000x600 px
- Use clear visual separation between concepts
- Venn diagram or split-panel layout
- Accessibility: use patterns + colors

Content Requirements:
- Left panel: Data Residency (location focus)
  - Data stored in specific geographic location
  - "Where" is specified
  - Limited control guarantees
- Right panel: Data Sovereignty (location + control)
  - Data location guaranteed
  - Control over access and operations
  - Legal jurisdiction specified
  - Compliance framework applied
- Overlap section: Shared characteristics
  - Both location-based
  - Both compliance-relevant

Visual Elements:
- Split-panel or Venn diagram layout
- Icons for location (pin), control (lock), jurisdiction (scales)
- Checkmarks for capabilities
- Comparison matrix showing differences
- Color-coding: Blue (residency), Green (sovereignty), Gray (shared)

Wireframe Guidance:
Left box: Data Residency with location icon and capabilities list. Right box: Data Sovereignty with control/jurisdiction icons and extended capabilities. Center overlap: shared elements. Bottom: comparison matrix.

Acceptance Criteria:
- [ ] Concepts clearly visually separated
- [ ] "Location only" vs. "Location + Control" distinction clear
- [ ] Venn or split-panel layout works at 800px
- [ ] Icons effectively represent concepts
- [ ] Comparison matrix is readable
- [ ] Color contrasts meet WCAG AA
- [ ] Pattern fill used to distinguish colors
- [ ] Alt text explains distinction clearly

Microsoft Learn Adaptation:
- Reference: https://learn.microsoft.com/en-us/industry/sovereign-cloud/overview/digital-sovereignty
- Reference: https://azure.microsoft.com/en-us/explore/global-infrastructure/data-residency/
- Create custom based on documentation concepts

---

### Asset 5: Regulatory Compliance Comparison Matrix

Context:
Shows how various regulatory frameworks (GDPR, FedRAMP, HIPAA, PCI DSS, ITAR) differ and align. Helps learners understand compliance landscape and Azure's compliance offerings.

Design Constraints:
- Canvas 1300x800 px (table format)
- Use table/matrix format with clear headers
- Color-coding for compliance status
- Readable at minimum 12pt font

Content Requirements:
- Rows: GDPR, FedRAMP, HIPAA, PCI DSS, ITAR
- Columns:
  - Regulation name
  - Jurisdiction
  - Key Requirements (abbreviated)
  - Data Location mandates
  - Access Control mandates
  - Azure Compliance (checkmark/note)
- Color-coded cells for quick scanning
- Icons for jurisdiction (EU, US, etc.)

Visual Elements:
- Clean table with alternating row colors
- Flag icons for jurisdictions (EU, US)
- Checkmarks (✓) for compliance
- X marks (✗) for non-compliance
- Partial indicators (◐) for partial compliance
- Bold headers for scannability
- Compact notation for cell contents

Wireframe Guidance:
Header row with regulation names and icons. Data rows with jurisdiction, requirements (abbreviated), and compliance indicators. Use light shading for alternating rows. Legend explaining symbols.

Acceptance Criteria:
- [ ] Table readable and not overcrowded
- [ ] Flag icons clearly identify jurisdictions
- [ ] Compliance status unambiguous (✓/✗/◐)
- [ ] Column headers bold and clear
- [ ] Alternating row shading improves readability
- [ ] Font size 12pt minimum
- [ ] Color contrasts meet WCAG AA
- [ ] Abbreviations/icons explained in legend
- [ ] Accurate regulatory information verified

Microsoft Learn Adaptation:
- Reference: https://learn.microsoft.com/en-us/compliance/regulatory/offering-home
- Reference: https://learn.microsoft.com/en-us/azure/compliance/
- Aggregate information from official compliance documentation

---

### Asset 6: Operational Sovereignty Levels

Context:
Details the 5 operational sovereignty levels with characteristics of control plane, connectivity, personnel access, and use cases. More detailed than the general spectrum.

Design Constraints:
- Canvas 1100x900 px
- Vertical or stacked layout
- Each level clearly distinguished
- Show progression through color/styling

Content Requirements:
- 5 levels stacked (Level 1: Standard → Level 5: Air-gapped)
- Per level: control plane location, connectivity type, personnel access rules, typical use cases
- Control plane progression: Cloud-managed → Hybrid → On-premises
- Connectivity: Always-on → Periodic sync → Disconnected
- Access: Unrestricted → Restricted → Locked-down
- Use cases for each level

Visual Elements:
- Stacked boxes or stepped pyramid
- Color gradient (green to red) showing increasing operational control
- Icons for control plane, network, personnel, use case
- Arrow indicators showing progression
- Characteristic labels and icons
- Use case callouts

Wireframe Guidance:
Vertical stack of 5 boxes (one per level). Each box: control plane indicator (left), connectivity type (top), personnel access symbol (right), use cases (bottom). Color progression top to bottom. Side legend explaining all symbols.

Acceptance Criteria:
- [ ] All 5 levels clearly labeled and distinct
- [ ] Control plane location progressively changes
- [ ] Connectivity type shows progression
- [ ] Personnel access restrictions visible
- [ ] Use cases provided for each level
- [ ] Color progression is intuitive
- [ ] Icons effectively represent concepts
- [ ] Readable at 800px width
- [ ] Progression logic is clear
- [ ] Legend complete and accurate

Microsoft Learn Adaptation:
- Reference: https://learn.microsoft.com/en-us/azure/azure-local/overview
- Reference: https://learn.microsoft.com/en-us/azure/azure-local/manage/disconnected-operations-overview?view=azloc-2509
- Based on operational sovereignty concepts

---

### Asset 7: Azure Local Connected vs. Disconnected Comparison

Context:
Side-by-side comparison of Azure Local's two deployment modes. Essential for understanding operational flexibility and choosing between connected and disconnected modes.

Design Constraints:
- Canvas 1200x800 px
- Two-column layout for clear comparison
- Feature matrix at bottom
- Accessible color coding

Content Requirements:
- Left column: Connected Mode
  - Architecture showing cloud connection
  - Always-on network link
  - Real-time sync capability
  - Features enabled by connectivity
- Right column: Disconnected Mode
  - Local control plane
  - No cloud dependency
  - Periodic or manual sync option
  - Limited features
- Bottom: Feature matrix (Connected: ✓, Disconnected: ✗, Limited)
  - Real-time monitoring
  - Cloud policy updates
  - Telemetry
  - Local management
  - Disaster recovery options

Visual Elements:
- Architecture diagrams for each mode
- Cloud icon (connected side) vs. lock icon (disconnected side)
- Network connection lines (solid connected, dashed disconnected)
- Feature checkmarks/X marks/Limited indicators
- Use case callouts
- Color coding: Blue (connected), Gray (disconnected)

Wireframe Guidance:
Top: Two architecture diagrams side-by-side. Bottom: Feature matrix comparing capabilities. Include use case examples for each mode.

Acceptance Criteria:
- [ ] Connected mode architecture clearly shows cloud link
- [ ] Disconnected mode shows local autonomy
- [ ] Feature matrix is comprehensive
- [ ] Checkmarks and X marks are clear
- [ ] Limited capabilities indicated with special marker
- [ ] Use cases guide reader to appropriate mode
- [ ] Color-coded for easy scanning
- [ ] Readable at 900px width
- [ ] Accessibility: patterns support color
- [ ] Deployment architecture differences evident

Microsoft Learn Adaptation:
- Reference: https://learn.microsoft.com/en-us/azure/azure-local/deploy/deployment-introduction?view=azloc-2509
- Reference: https://learn.microsoft.com/en-us/azure/azure-local/manage/disconnected-operations-overview?view=azloc-2509
- Based on official deployment documentation

---

## Module 2: Microsoft Sovereign Cloud Models

### Asset 8: Sovereign Cloud Models Comparison

Context:
Compares the three sovereign cloud models (Sovereign Public, Sovereign Private, National Partner). Critical for helping learners and customers choose appropriate model.

Design Constraints:
- Canvas 1300x800 px
- Three-column layout with clear separation
- Consistent styling across columns
- Color-coded for quick identification

Content Requirements:
- Column 1: Sovereign Public Cloud
  - Microsoft-operated, globally distributed
  - Enhanced controls for data residency
  - Shared infrastructure
  - Medium sovereignty level
- Column 2: Sovereign Private Cloud
  - Dedicated infrastructure
  - High operational control
  - On-premises or dedicated hosting
  - High sovereignty level
- Column 3: National Partner Clouds
  - Operated by national partner
  - Maximum sovereignty guarantees
  - Specific jurisdictions (US Gov, China)
  - Highest sovereignty level
- Comparison rows: Infrastructure, Control Level, Compliance, Use Cases, Cost Model, Setup Time

Visual Elements:
- Three column boxes with distinct colors: Blue (Public), Green (Private), Purple (Partner)
- Icons for each model type
- Checkmarks/bars for comparison metrics
- Sovereignty level indicators (Low/Medium/High)
- Call-out boxes for key differentiators

Wireframe Guidance:
Three columns with header (model type + icon). Rows below with comparison attributes. Icons and color-coded badges for each attribute. Sovereignty level bar at bottom of each column.

Acceptance Criteria:
- [ ] Three models clearly distinguished by color and icon
- [ ] Sovereignty level progression visible (Medium → High → Maximum)
- [ ] Comparison rows cover all key attributes
- [ ] Infrastructure differences evident
- [ ] Cost/complexity differences indicated
- [ ] Use cases provided for each model
- [ ] Column headers bold and clear
- [ ] Readable at 1000px width
- [ ] Color contrasts meet WCAG AA
- [ ] Decision criteria evident from comparison

Microsoft Learn Adaptation:
- Reference: https://learn.microsoft.com/en-us/industry/sovereign-cloud/
- Reference: https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deployment-stacks
- Create custom based on sovereign cloud documentation

---

### Asset 9: Sovereign Cloud Model Decision Tree

Context:
Interactive decision flowchart helping customers select the appropriate sovereign cloud model based on their requirements for control, compliance, and jurisdiction.

Design Constraints:
- Canvas 1200x1400 px (vertical flow)
- Diamond-shaped decision nodes
- Clear yes/no branches
- Color-coded outcomes

Content Requirements:
- Start node: "What are your sovereignty requirements?"
- Decision nodes (in sequence):
  1. Data residency guarantee needed?
  2. Operational control required?
  3. Disconnected operations needed?
  4. National compliance mandated?
  5. Budget constraints?
- End nodes (outcomes): Recommended model with rationale
  - Sovereign Public Cloud (cost-effective, residency focus)
  - Sovereign Private Cloud (control-focused, operational autonomy)
  - National Partner Clouds (maximum sovereignty, specific jurisdictions)
  - Hybrid approach (multiple models)

Visual Elements:
- Diamond nodes for decisions
- Rectangular boxes for outcomes
- Yes/No labels on branches
- Color-coded paths and outcomes matching model colors
- Scenario examples at endpoints
- Icons for decision types

Wireframe Guidance:
Top: Start node. Vertical flow with diamond decision nodes. Branches left/right for yes/no. Bottom: Outcome boxes with recommendations and example scenarios.

Acceptance Criteria:
- [ ] Decision flow is logical and comprehensive
- [ ] All major decision criteria included
- [ ] Yes/No branches clear at each node
- [ ] Outcomes/recommendations at endpoints
- [ ] Example scenarios provided
- [ ] Color-coded paths match model colors
- [ ] Readable at 1024px width
- [ ] Diamond and box shapes distinct
- [ ] No ambiguous branching paths
- [ ] Target audience (sales, architects) considered

Microsoft Learn Adaptation:
- Reference: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/decision-guides/
- Reference: https://learn.microsoft.com/en-us/industry/sovereign-cloud/
- Create custom decision tree based on model characteristics

---

### Asset 10: National Partner Clouds Map

Context:
Shows geographic distribution of national partner clouds (Azure Government, Azure China, historical Azure Germany). Explains sovereignty model for each region and operator.

Design Constraints:
- Canvas 1200x700 px
- World map focus on relevant regions
- Clear highlighting for special regions
- Legend explaining sovereignty levels

Content Requirements:
- World map with simplified geography
- Azure Government Cloud (US): Virginia, Texas, Arizona, DoD regions highlighted
- Azure China (21Vianet): Beijing, Shanghai highlighted
- Azure Germany (historical reference with sunset note)
- Network isolation visualization (separate bubbles)
- Operator information per region
- Connectivity constraints noted

Visual Elements:
- World map base layer
- Regional highlights with distinct colors
- Flag icons (US, China)
- Operator logos/names (Microsoft, 21Vianet)
- Isolated region bubbles showing no cross-region data flow
- Callout boxes for each major region
- Legend explaining sovereignty levels

Wireframe Guidance:
World map background. Regional highlights: US Gov (top left with expansion detail), China (bottom right with expansion detail), Germany (center with sunset callout). Arrows showing isolation between regions. Legend on bottom right.

Acceptance Criteria:
- [ ] Major national cloud regions clearly marked
- [ ] Geographic locations accurate
- [ ] Isolation between regions clearly shown
- [ ] Operator information included
- [ ] Sovereignty level indicators provided
- [ ] US Gov regions (including DoD) detailed
- [ ] China regions highlighted
- [ ] Germany sunset note included
- [ ] Color scheme consistent with Azure standards
- [ ] Readable at 900px width
- [ ] Legend complete and clear

Microsoft Learn Adaptation:
- Reference: https://azure.microsoft.com/en-us/explore/global-infrastructure/
- Reference: https://learn.microsoft.com/en-us/azure/active-directory/develop/authentication-national-cloud
- Reference: Historical Azure Germany documentation
- Adapt from official global infrastructure maps

---

## Module 3: Azure Local Overview

### Asset 11: Azure Local System Architecture

Context:
Comprehensive architecture diagram showing Azure Local's hardware, software layers, and connectivity to Azure cloud. Essential for understanding system components and data flows.

Design Constraints:
- Canvas 1400x1000 px, 50px margins
- Three-section layout (on-premises left, cloud right, center connectivity)
- Component labels clear at 800px viewing
- Color-coded by layer

Content Requirements:
- Left section: On-premises Azure Local Stack
  - Hardware layer (servers, storage, networking)
  - Virtualization layer (Hyper-V, storage spaces)
  - System layer (Azure Local software stack)
  - Management layer
- Center: Data and control plane separation
  - Data plane (local processing)
  - Control plane (cloud or hybrid)
- Right section: Azure Cloud Control Plane
  - Azure services
  - Management interfaces
- Connectivity paths:
  - Solid lines for connected mode
  - Dashed lines for optional disconnected sync

Visual Elements:
- Layered architecture boxes
- Component icons (servers, storage, network, cloud)
- Bidirectional arrows for connected mode
- Optional dashed lines for disconnected
- Color coding: Blue (on-prem), Light blue (Azure), Green (data), Orange (control)
- Callout boxes for key components

Wireframe Guidance:
Left third: Hardware/software stack with layers. Middle third: Data/control plane separation. Right third: Azure cloud services. Connectivity arrows between sections. Legend on bottom.

Acceptance Criteria:
- [ ] Hardware layer clearly distinguished from software
- [ ] All major components labeled (servers, storage, network)
- [ ] Virtualization layer (Hyper-V, Storage Spaces) shown
- [ ] System software components identified
- [ ] Data/control plane separation clear
- [ ] Azure control plane services shown
- [ ] Connected and disconnected modes indicated
- [ ] Color coding consistent and meaningful
- [ ] Readable at 1024px width
- [ ] Connectivity flows unambiguous

Microsoft Learn Adaptation:
- Reference: https://learn.microsoft.com/en-us/azure/azure-local/overview?view=azloc-2509
- Reference: https://learn.microsoft.com/en-us/azure/azure-local/concepts/system-requirements-23h2?view=azloc-2509
- Use official architecture documentation as basis

---

### Asset 12: Connected vs. Disconnected Mode Feature Matrix

Context:
Detailed feature comparison showing what capabilities are available in each mode. Helps operators choose and plan deployments.

Design Constraints:
- Canvas 1300x900 px (table/matrix format)
- Clear row/column structure
- Feature groupings by category
- Accessibility with patterns + colors

Content Requirements:
- Column headers: Feature Category, Connected Mode, Disconnected Mode, Notes
- Row categories:
  - Connectivity & Management
  - Monitoring & Diagnostics
  - Policy & Governance
  - Updates & Patches
  - Disaster Recovery
  - Scaling & Operations
  - Support & Assistance
- Cells: ✓ (supported), ✗ (not supported), ◐ (limited), with notes where applicable

Visual Elements:
- Clean table with bordered cells
- Category headers with background shading
- Checkmarks (✓) in green
- X marks (✗) in red/gray
- Limited indicators (◐) in yellow
- Notes column with detailed callouts
- Icons for feature categories

Wireframe Guidance:
Header row with column names. Feature category rows below. Connected/Disconnected columns with checkmarks/X marks/limited indicators. Notes column on right. Category icon on left of each row.

Acceptance Criteria:
- [ ] All major feature categories covered
- [ ] Features accurately categorized
- [ ] Checkmarks and X marks are clear
- [ ] Notes explain limitations or details
- [ ] Color contrasts meet WCAG AA
- [ ] Patterns support color-only differentiation
- [ ] Font size 12pt minimum
- [ ] Table not overcrowded
- [ ] Useful for planning/decisions
- [ ] Operational accuracy verified

Microsoft Learn Adaptation:
- Reference: https://learn.microsoft.com/en-us/azure/azure-local/deploy/deployment-introduction?view=azloc-2509
- Reference: https://learn.microsoft.com/en-us/azure/azure-local/manage/disconnected-operations-overview?view=azloc-2509
- Create custom based on operational documentation

---

### Asset 13: Azure Local Hardware Topology

Context:
Shows typical hardware configuration for Azure Local cluster (2-4 node cluster, network, storage topology). Useful for planning and understanding physical architecture.

Design Constraints:
- Canvas 1400x1000 px
- Physical layout emphasis
- Component labels and specifications
- Redundancy clearly shown

Content Requirements:
- 3-node cluster layout (primary view)
- Per-node components:
  - CPUs and memory (specs callout)
  - Network adapters (6-10 NICs per node)
  - Storage capacity (local and shared)
- Network topology:
  - ToR switches (dual for redundancy)
  - Management network
  - Storage network
  - Cluster heartbeat network
- External connections:
  - WAN link to Azure
  - Storage array (if external storage)
  - Management console
- Redundancy indicators (dual power supplies, dual switches)

Visual Elements:
- Server hardware illustrations with component labels
- Network adapter visualization
- Switch topology diagram
- Storage array connection
- Redundancy indicators (dual lines for paired components)
- Specification callouts (CPU cores, RAM, network speeds)
- Component connection types labeled

Wireframe Guidance:
Top: 3-node cluster with hardware components labeled. Middle: Network switches and connectivity. Bottom: External connections (WAN, storage array). Right side: Component specifications and redundancy notes.

Acceptance Criteria:
- [ ] Cluster topology clearly shown (3 nodes)
- [ ] Per-node components labeled with specifications
- [ ] Network adapters shown and labeled
- [ ] Switch topology shows dual redundancy
- [ ] Management, storage, and cluster networks distinguished
- [ ] External connectivity (WAN, storage) shown
- [ ] Power redundancy indicated
- [ ] Specifications clear and readable
- [ ] Typical configuration represented
- [ ] Scalable appearance (shows 4-node variant feasibility)

Microsoft Learn Adaptation:
- Reference: https://learn.microsoft.com/en-us/azure/azure-local/concepts/system-requirements-23h2?view=azloc-2509
- Reference: https://learn.microsoft.com/en-us/azure/azure-local/plan/cloud-deployment-network-considerations?view=azloc-2509
- Based on validated hardware configurations

---

## Module 4: Azure Arc Introduction

### Asset 14: Azure Arc Architecture

Context:
Unified view showing how Azure Arc connects on-premises resources to Azure management plane. Essential for understanding Arc's role in hybrid cloud operations.

Design Constraints:
- Canvas 1400x900 px
- Three-section layout (on-prem, Arc, Azure)
- Clear service separation (Servers, Kubernetes, Data)
- Color-coded by Arc service

Content Requirements:
- Left section: On-premises Resources
  - Servers (Windows, Linux)
  - Kubernetes clusters
  - SQL databases, PostgreSQL
  - Other resources
- Center: Azure Arc Control Plane
  - Arc Servers agent
  - Arc Kubernetes agent
  - Arc Data Services agent
  - Registration and connectivity
- Right section: Azure Cloud Services
  - Azure Portal management
  - Azure Monitor
  - Azure Policy
  - Azure Security Center
  - Azure Update Management
- Connection flows:
  - Bidirectional arrows (commands out, telemetry in)
  - Arc agents as bridges

Visual Elements:
- Three Arc services highlighted with distinct colors:
  - Green for Servers
  - Blue for Kubernetes
  - Purple for Data Services
- Component icons for resource types
- Bidirectional arrows for management flows
- Service icons on right (Monitor, Policy, Security, Updates)
- Agent icons showing registration

Wireframe Guidance:
Left third: On-premises resource icons. Middle third: Arc services with agent symbols. Right third: Azure cloud services. Arrows connecting resources through Arc to cloud services. Legend on bottom identifying colors and arrow meanings.

Acceptance Criteria:
- [ ] All three Arc services clearly shown
- [ ] On-premises resource types identified
- [ ] Arc agents represented as bridges/mediators
- [ ] Azure services listed on right
- [ ] Bidirectional flows shown (commands + telemetry)
- [ ] Color-coding distinguishes services (Servers/Kubernetes/Data)
- [ ] Icons effectively represent resource types
- [ ] Readable at 1000px width
- [ ] Architecture logic is clear
- [ ] Connection flows unambiguous

Microsoft Learn Adaptation:
- Reference: https://learn.microsoft.com/en-us/azure/azure-arc/overview
- Reference: https://learn.microsoft.com/en-us/azure/azure-arc/servers/overview
- Reference: https://learn.microsoft.com/en-us/azure/azure-arc/kubernetes/overview
- Based on official Arc architecture

---

### Asset 15: Arc-Enabled Resources Comparison

Context:
Comparison table showing capabilities and use cases for Arc Servers, Arc Kubernetes, and Arc Data Services. Helps learners understand when to use each.

Design Constraints:
- Canvas 1200x800 px (table format)
- Three main columns (one per Arc service)
- Clear comparison rows
- Accessible color-coding

Content Requirements:
- Rows:
  - Resource Types
  - Primary Use Cases
  - Management Capabilities
  - Compliance & Governance
  - Monitoring & Observability
  - Patching & Updates
  - Licensing
  - Best Suited For
- Columns: Arc Servers | Arc Kubernetes | Arc Data Services
- Cells with concise descriptions

Visual Elements:
- Three-column table with distinct header colors
- Service icons in header
- Feature icons within cells (checkmarks, limited indicators)
- Color-coded for quick scanning: Green/Blue/Purple matching Arc services
- Concise cell content
- Legend explaining icons

Wireframe Guidance:
Header row with Arc service icons and titles. Feature rows below. Three columns with service-specific information. Icons and compact text in cells. Legend on bottom explaining icons.

Acceptance Criteria:
- [ ] All three Arc services well-represented
- [ ] Comparison rows cover all essential aspects
- [ ] Use cases clear for each service
- [ ] Licensing differences noted
- [ ] Management capabilities compared
- [ ] Monitoring capabilities shown
- [ ] Font size 12pt minimum
- [ ] Color contrasts meet WCAG AA
- [ ] Decision-making support evident
- [ ] Accuracy verified against Arc documentation

Microsoft Learn Adaptation:
- Reference: https://learn.microsoft.com/en-us/azure/azure-arc/servers/overview
- Reference: https://learn.microsoft.com/en-us/azure/azure-arc/kubernetes/overview
- Reference: https://learn.microsoft.com/en-us/azure/azure-arc/data/overview
- Create custom based on service comparison

---

### Asset 16: Arc Deployment Topology

Context:
Shows multi-site/multi-location deployment with Arc managing resources across distributed environments. Useful for understanding enterprise deployment patterns.

Design Constraints:
- Canvas 1300x900 px
- Geographic distribution emphasis
- Central management visual
- Site-specific details

Content Requirements:
- Multiple sites (3-4):
  - Data center
  - Branch office
  - Edge location
  - Remote office
- Per-site resources:
  - Servers (Windows/Linux)
  - Kubernetes clusters
  - Databases (optional)
- Central Azure management plane
- Network connectivity (internet or hybrid)
- Arc agent deployment at each site

Visual Elements:
- Site locations with geographic labels
- Resource icons at each site
- Central management hub (Azure)
- Network connectivity lines to hub
- Arc agent representation
- Site-specific callouts with details
- Scale indicators (small sites vs. large)

Wireframe Guidance:
Center: Azure management plane with Arc services. Around edges: Multiple sites (4 positions). Connectivity lines from each site to center. Per-site resources shown. Site details in callout boxes.

Acceptance Criteria:
- [ ] Multiple sites clearly shown (minimum 3)
- [ ] Geographic distribution evident
- [ ] Arc agents represented at each site
- [ ] Central management hub clear
- [ ] Connectivity to Azure shown
- [ ] Site-specific resource types visible
- [ ] Scalability concept demonstrated
- [ ] Color-coding consistent with Arc services
- [ ] Readable at 1000px width
- [ ] Enterprise topology patterns evident

Microsoft Learn Adaptation:
- Reference: https://learn.microsoft.com/en-us/azure/azure-arc/servers/overview
- Reference: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/
- Create custom based on enterprise deployment patterns

---

## Module 5: Edge RAG Concepts

### Asset 17: Edge RAG System Architecture

Context:
Complete system architecture showing all components of an edge RAG (Retrieval-Augmented Generation) system and how data flows through for query processing and answer generation.

Design Constraints:
- Canvas 1400x1000 px
- Component emphasis with data flow annotations
- Sequential numbering showing query flow
- Color-coded by component type

Content Requirements:
- Document source inputs (PDFs, databases, text files)
- Ingestion pipeline (chunking, cleaning)
- Embeddings generation (vector creation)
- Vector database storage
- Query input
- Query embedding
- Vector similarity search
- Document retrieval (top-K)
- Context assembly
- LLM prompt construction
- Local LLM inference
- Response generation
- Answer output with citations
- Optional cloud connection (dashed lines)

Visual Elements:
- Component boxes with icons (document, database, compute, LLM)
- Numbered data flow arrows (1→2→3... sequence)
- Color coding: Blue (input/output), Green (processing), Purple (AI/LLM), Orange (storage)
- Sequential numbers on arrows
- Optional cloud connection (dashed lines)
- Latency/performance indicators (fast path highlighted)

Wireframe Guidance:
Left: Document sources and ingestion. Center-left: Vector database and embedding. Center: Query processing with numbered sequence. Right: LLM and response. Top-right: Optional cloud connection. Legend showing color meanings and component types.

Acceptance Criteria:
- [ ] All major RAG components included
- [ ] Document ingestion pipeline clear
- [ ] Vector database storage shown
- [ ] Query processing flow numbered and sequential
- [ ] LLM inference clearly labeled
- [ ] Response with citations shown
- [ ] Optional cloud connection indicated (dashed)
- [ ] Color-coding meaningful
- [ ] Sequential flow unambiguous
- [ ] Edge-centric (not cloud-centric)
- [ ] Readable at 1024px width

Microsoft Learn Adaptation:
- Reference: https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/use-your-data
- Reference: https://learn.microsoft.com/en-us/azure/ai-services/
- Create custom based on RAG concepts and LLM/embeddings architecture

---

### Asset 18: Traditional LLM vs. RAG Comparison

Context:
Side-by-side comparison showing the fundamental difference between traditional LLM responses and RAG-augmented responses. Illustrates why RAG addresses hallucinations and recency.

Design Constraints:
- Canvas 1200x800 px
- Two-column split layout
- Clear workflow visualization
- Comparison matrix at bottom

Content Requirements:
- Left panel: Traditional LLM
  - Query input
  - Direct LLM processing
  - Answer generation from training data
  - No external information
  - Potential hallucinations
  - No source citations
- Right panel: RAG-Augmented Flow
  - Query input
  - Retrieval from knowledge base
  - Context assembly
  - LLM with context
  - Answer with sources
  - No hallucinations (grounded in data)
- Comparison matrix (bottom):
  - Accuracy
  - Hallucinations
  - Recency
  - Citations
  - Training data dependency

Visual Elements:
- Two parallel workflows with arrows
- Query box at top (shared)
- Left: Direct LLM flow
- Right: Retrieval + context + LLM flow
- Comparison matrix with checkmarks/X marks/indicators
- Icons for each step
- Color coding: Blue (input), Green (retrieval), Purple (LLM), Orange (output)

Wireframe Guidance:
Top: Query input (center/shared). Left column: Direct LLM workflow. Right column: RAG workflow. Bottom: Comparison matrix. Side callouts highlighting key differences.

Acceptance Criteria:
- [ ] Traditional LLM flow clearly shown
- [ ] RAG flow clearly shown
- [ ] Key difference (retrieval step) highlighted
- [ ] Comparison matrix covers accuracy, hallucinations, recency
- [ ] Citations/sources addressed
- [ ] Benefits of RAG evident
- [ ] Color-coding helps distinguish approaches
- [ ] Readable at 900px width
- [ ] Workflow arrows unambiguous
- [ ] Decision support evident (when to use each)

Microsoft Learn Adaptation:
- Reference: https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/use-your-data
- Reference: https://learn.microsoft.com/en-us/azure/cognitive-services/openai/concepts/models
- Create custom based on LLM and RAG concepts

---

### Asset 19: Edge RAG Deployment Topology Options

Context:
Shows three deployment topology options for Edge RAG: local-only, edge-with-cloud, and multi-edge. Helps learners understand deployment flexibility and trade-offs.

Design Constraints:
- Canvas 1300x900 px
- Three topology diagrams arranged horizontally or stacked
- Connectivity differences clear
- Use cases labeled

Content Requirements:
- Option 1: Local Edge Only (Air-gapped)
  - Edge device fully independent
  - No cloud connection
  - All processing local
  - Use case: Classified/disconnected environments
- Option 2: Edge with Cloud Sync (Hybrid)
  - Edge for real-time processing
  - Periodic cloud synchronization
  - Cloud backup/analytics
  - Use case: Most common/production
- Option 3: Multi-Edge Deployment (Distributed)
  - Multiple edge sites
  - Central coordination
  - Data synchronization between sites
  - Use case: Large enterprises/multi-location

Visual Elements:
- Three topology diagrams
- Edge devices shown as boxes
- Cloud shown as cloud shape or region
- Connectivity lines: Solid (always-on), Dashed (periodic), None (disconnected)
- Data flow arrows
- Use case labels below each option
- Pro/con callouts
- Color coding: Edge (blue/green), Cloud (light blue)

Wireframe Guidance:
Three columns or stacked rows, one per deployment option. Each shows topology diagram with edge + cloud representation. Connectivity lines indicate mode. Below each: use case and pro/con summary.

Acceptance Criteria:
- [ ] All three deployment options shown
- [ ] Connectivity differences clear (always-on vs. periodic vs. none)
- [ ] Edge independence emphasized in Option 1
- [ ] Hybrid integration shown in Option 2
- [ ] Multi-site coordination shown in Option 3
- [ ] Use cases provided for each
- [ ] Pro/con callouts helpful
- [ ] Color-coding consistent
- [ ] Readable at 900px width
- [ ] Deployment decisions supported

Microsoft Learn Adaptation:
- Reference: https://learn.microsoft.com/en-us/azure/ai-services/
- Reference: https://learn.microsoft.com/en-us/azure/azure-local/manage/disconnected-operations-overview?view=azloc-2509
- Create custom based on deployment patterns and edge computing

---

### Asset 20: RAG Components and Data Flow Diagram

Context:
Detailed sequential data flow showing exactly how a query moves through RAG system components, with step numbers, data transformations, and timing information.

Design Constraints:
- Canvas 1400x900 px
- Sequential flow with step numbers
- Data transformation visibility
- Performance/latency callouts

Content Requirements:
- Step-by-step sequence (8-10 steps):
  1. User query input
  2. Query embedding generation (local embeddings model)
  3. Vector similarity search in database
  4. Document retrieval (top-K results, e.g., top-5)
  5. Retrieved documents/chunks displayed
  6. Context assembly (combine chunks)
  7. Prompt construction with context and query
  8. Local LLM inference
  9. Answer generation
  10. Response with citations and source links
- Timing/latency estimates per step
- Component ownership (local compute, vector DB, LLM)
- Data transformation examples

Visual Elements:
- Numbered boxes for each step
- Arrows connecting steps with data flowing
- Component icons (embeddings, search, LLM, output)
- Sample data snippets or examples within boxes
- Timing annotations (fast, medium latency)
- Color coding: Blue (input), Green (processing), Purple (AI), Orange (output)
- Data format indicators (text, vectors, tokens)

Wireframe Guidance:
Top to bottom or left to right sequential flow. Each step in numbered box with icon. Arrows between steps with data format labels. Side column with timing/latency info. Bottom: legend explaining colors and symbols.

Acceptance Criteria:
- [ ] All major steps included (input through output)
- [ ] Sequential flow is logical and clear
- [ ] Step numbers are prominent
- [ ] Data transformations visible (text→vectors→chunks→prompt)
- [ ] Timing/latency indicators provided
- [ ] Component ownership clear
- [ ] Example data snippets helpful
- [ ] Color-coding meaningful
- [ ] Readable at 1024px width
- [ ] Technical accuracy verified

Microsoft Learn Adaptation:
- Reference: https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/use-your-data
- Reference: https://learn.microsoft.com/en-us/azure/cognitive-services/openai/
- Create custom based on detailed RAG architecture

---

## Summary

**Level 100 Visual Asset Specifications Complete:**
- 20 detailed asset briefs (Assets 1-20)
- 5 modules across foundational learning level
- Comprehensive design constraints, content requirements, visual elements, wireframes, and acceptance criteria
- All assets linked to Microsoft Learn source documentation
- Ready for designer handoff and SVG creation

**Next Steps:**
1. Share this document with assigned designers
2. Each designer reviews relevant asset briefs
3. SVG creation follows acceptance criteria
4. Assets saved to `docs/assets/images/level-100/[asset-name].svg`
5. Status updated in `docs/assets/images/README.md`
6. Placeholder content removed and SVGs integrated into markdown files

**Timeline:** 14-16 hours for all 20 assets (design + creation + QA)
