---
layout: default
title: Level 200 Visual Asset Specifications
nav_exclude: true
---

# Level 200 Visual Asset Specifications

Purpose: Detailed design briefs for all 20 Level 200 visual assets (Assets 21–40)
Created: October 21, 2025
Asset Registry: See `docs/assets/images/README.md` for short specs and usage

---

## Module 1: Azure Local Architecture Deep Dive

### Asset 21: Advanced Networking Architecture

Context:
This diagram helps architects and networking engineers design Azure Local clusters with resilient, high-performance network topologies. It explains SET (Switch Embedded Teaming), VLAN segmentation, and RDMA optimizations needed for low-latency, high-throughput storage and compute traffic.

Design Constraints:
- Canvas 1400x1000 px, 50px margins
- Use Microsoft color palette and Segoe-like typography
- Maintain clarity at 800px width for inline displays
- Compatible with accessibility requirements (patterns + colors)

Content Requirements:
- Physical server with 6–8 NICs
- Virtual switch (vSwitch) + SET team labels
- VLAN segmentation: management, storage, cluster, customer
- RDMA path overlay (separate line style)
- Dual ToR switches and failover paths
- Bandwidth allocation indicators (eg. 10Gb/25Gb/100Gb)
- Legend and short notes

Visual Elements:
- Server icon with adapter slots
- vSwitch block showing teaming
- Color-coded VLAN flows (blue, orange, green, purple)
- Solid arrows for active, dashed for failover
- Small iconography for redundancy and QoS

Wireframe Guidance:
Top: server with ports; center-left: vSwitch visualization; center-right: ToR switches; bottom: RDMA overlay and storage array. Legend on the right.

Acceptance Criteria:
- [ ] Shows 6–8 NICs labeled
- [ ] SET team and vSwitch are clearly depicted
- [ ] VLANs color-coded and legible
- [ ] RDMA paths visually distinct and labeled
- [ ] Dual-switch redundancy is evident
- [ ] Bandwidth nodes present with numeric values
- [ ] Legend explains colors and line styles
- [ ] Alt text provided in final SVG

Microsoft Learn Adaptation:
- Reference: https://learn.microsoft.com/en-us/azure/azure-local/plan/cloud-deployment-network-considerations?view=azloc-2509
- Adapt SET examples and include RDMA notes from system requirements

---

### Asset 22: High-Availability Architecture

Context:
Shows HA patterns for Azure Local: node layout, quorum options, storage resilience, and failover. Useful for operations and DR planning.

Design Constraints:
- Canvas 1300x900 px
- Include options for 3-node and 4-node clusters
- Keep diagrams simple for export to slides

Content Requirements:
- Cluster node arrangement (3/4 nodes)
- Storage Spaces Direct replication modes
- Quorum options: disk, file share, cloud witness
- Replication/backup flows and RTO/RPO annotations
- Failover scenarios illustrated

Visual Elements:
- Circular node layout with storage tier in center
- Arrows for replication paths
- Highlighted quorum options with callouts
- Color states: active/standby/failed

Wireframe Guidance:
Top left: 3-node cluster; top right: 4-node cluster; bottom: quorum options and storage replication details. Provide side column with RTO/RPO guidance.

Acceptance Criteria:
- [ ] Shows both 3-node and 4-node topologies
- [ ] Quorum placement options annotated
- [ ] Storage redundancy types labeled (2-way/3-way/EC)
- [ ] Failover path visible and explained
- [ ] RTO/RPO indicators present
- [ ] Diagram readable at 1024 width
- [ ] Accessibility: color + pattern for states

Microsoft Learn Adaptation:
- References: https://learn.microsoft.com/en-us/azure/azure-local/deploy/create-cluster
- Use official S2D icons and concepts as basis

---

### Asset 23: Hardware Planning Decision Tree

Context:
A decision flowchart guiding hardware selection based on workload class, capacity, redundancy and budget.

Design Constraints:
- Canvas 1200x1400 px (vertical)
- Decision diamonds and endpoint recommendation cards

Content Requirements:
- Start: workload requirements
- Branches: performance tier, capacity, redundancy, environment
- Endpoints: validated BOM recommendations

Visual Elements:
- Diamonds for decisions, rectangles for actions
- Color-coded outcome paths for recommended tiers
- Cost/perf mini-metrics on endpoints

Wireframe Guidance:
Top: start node. Follow vertical tree down with 3–5 layers. Endpoints at bottom with recommended configs.

Acceptance Criteria:
- [ ] Flow covers performance, capacity, redundancy, budget
- [ ] Endpoints include BOM and short rationale
- [ ] No decision path exceeds 5 hops
- [ ] Visuals use accessible colors and patterns
- [ ] All endpoints have brief cost guidance

Microsoft Learn Adaptation:
- Reference: https://learn.microsoft.com/en-us/azure/azure-local/deploy/deployment-prerequisites?view=azloc-2509

---

## Module 2: Arc Advanced Management

### Asset 24: Arc Governance Framework

Context:
Explains layered governance across tenant, subscription, resource group and resource using Azure Policy and RBAC for Arc-managed resources.

Design Constraints:
- Canvas 1300x900 px
- Hierarchical/pyramid visual

Content Requirements:
- Policy layers and inheritance arrows
- RBAC role mapping examples
- Monitoring feedback loops and remediation paths

Visual Elements:
- Layered pyramid with arrows, small RBAC boxes, policy iconography
- Compliance status indicators (green/red)

Wireframe Guidance:
Left: pyramid showing layers; center: enforcement arrows; right: monitoring and remediation loops.

Acceptance Criteria:
- [ ] Shows inheritance across layers
- [ ] RBAC roles and example permissions shown
- [ ] Remediation/monitoring feedback loops illustrated
- [ ] Links to policy definition examples included

Microsoft Learn Adaptation:
- Arc Policy: https://learn.microsoft.com/en-us/azure/azure-arc/servers/security-overview
- Azure Policy overview: https://learn.microsoft.com/en-us/azure/governance/policy/overview

---

### Asset 25: Arc Cost Optimization Flows

Context:
Guides discussions about cost levers and chargeback models for Arc-managed resources, helping presales and architects.

Design Constraints:
- Canvas 1200x800 px
- Emphasize flow and before/after comparisons

Content Requirements:
- Resource consumption flows
- Cost levers: reserved, spot, right-size, hybrid benefits
- Analytics & chargeback model

Visual Elements:
- Dollar-flow diagrams, percentage savings callouts, before/after visuals

Wireframe Guidance:
Left: consumption sources; center: cost levers; right: savings/outcome panel

Acceptance Criteria:
- [ ] Shows 4–6 clear cost levers
- [ ] Includes visual savings example
- [ ] Includes chargeback model callout
- [ ] Uses correct palette and icons

Microsoft Learn Adaptation:
- Arc pricing and cost mgmt references: https://azure.microsoft.com/en-us/pricing/details/azure-arc/

---

### Asset 26: Enterprise Deployment Topology

Context:
Shows multi-site Arc-managed topology with central governance and hybrid connectivity options for enterprise deployments.

Design Constraints:
- Canvas 1400x900 px
- Include network types (ExpressRoute, VPN), satellite hints optional

Content Requirements:
- Multiple sites with local resources
- Central Azure control plane and management agents
- Connectivity patterns and latency notes

Visual Elements:
- Geographic site icons, central dashboard, connection line styles for latency

Wireframe Guidance:
Map layout: HQ on left, branch/retail on right, cloud control plane top center. Include legend for connection types.

Acceptance Criteria:
- [ ] Shows central management clearly
- [ ] Distinguishes connection types and latency cues
- [ ] Agent communication patterns labeled
- [ ] Resilience and offline scenarios noted

Microsoft Learn Adaptation:
- Arc at scale: https://learn.microsoft.com/en-us/azure/azure-arc/servers/onboard-group-policy-powershell

---

## Module 3: Edge RAG Implementation

### Asset 27: Production RAG Architecture (Detailed)

Context:
A production-grade Edge RAG topology with load balancing, HA, vector DB replication, LLM inference services and persistence.

Design Constraints:
- Canvas 1400x1100 px
- Show both HA and optional cloud sync (dashed lines)

Content Requirements:
- Load balancer/ingress
- Replica services for RAG components
- Vector DB replication and backup
- LLM inference cluster (Ollama or equivalent)
- Ingestion pipeline and storage
- Monitoring/alerting stack

Visual Elements:
- Layered sections for ingress, processing, storage, monitoring
- Colored overlays for optional cloud components

Wireframe Guidance:
Top: ingress/load balancer; mid: RAG services and vector DB; bottom: storage and monitoring; right: optional cloud sync dashed overlay.

Acceptance Criteria:
- [ ] HA and replicas are indicated
- [ ] Vector DB replication/backups labeled
- [ ] LLM inference cluster and model instances visible
- [ ] Ingestion pipeline with queue shown
- [ ] Monitoring stack illustrated with metrics/log flow
- [ ] Optional cloud components dashed and labeled

Microsoft Learn Adaptation:
- Weaviate deployment notes: https://weaviate.io/blog/how-to-deploy-weaviate
- Ollama setup: https://github.com/ollama/ollama

---

### Asset 28: LLM Inference Optimization

Context:
Visualizes inference optimizations like quantization, batching, caching and hardware acceleration to help engineers trade off latency vs accuracy.

Design Constraints:
- Canvas 1300x900 px
- Include performance curves or small charts

Content Requirements:
- Quantization options, batching strategies, caching (KV cache)
- Hardware paths: CPU/GPU/NPU options
- Tradeoffs: latency vs accuracy

Visual Elements:
- Pipeline diagram with branches for optimization approaches
- Small performance curves or heatmap

Wireframe Guidance:
Left: model baseline; center: optimization branches; right: performance curves and recommended hardware.

Acceptance Criteria:
- [ ] Shows quantization techniques and tradeoffs
- [ ] Shows batching and cache impact
- [ ] Hardware options mapped to performance curves
- [ ] Clear recommendations for edge configurations

Microsoft Learn Adaptation:
- LLM optimization references: https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/model-versions

---

### Asset 29: Vector Database Architecture Comparison

Context:
Compares Weaviate, Milvus and PostgreSQL+pgvector across architecture, performance and operational considerations.

Design Constraints:
- Canvas 1400x1000 px
- Three-column comparative layout

Content Requirements:
- Architecture style, indexing, HA, backup, cost and recommended use-cases

Visual Elements:
- Three columns with micro-architecture sketches, charts and feature matrix

Wireframe Guidance:
Three vertical panels: left Weaviate, center Milvus, right pgvector; bottom row: feature matrix and recommendation

Acceptance Criteria:
- [ ] Each DB has architecture sketch
- [ ] Feature matrix compares all critical dimensions
- [ ] Recommendations per use-case present
- [ ] Performance indicators and cost notes included

Microsoft Learn Adaptation:
- Vector DB comparison reference: https://learn.microsoft.com/en-us/semantic-kernel/concepts/vector-store-connectors/

---

### Asset 30: RAG Deployment Topology Options

Context:
Shows multiple RAG topology templates to map customer scale and availability needs to architecture.

Design Constraints:
- Canvas 1400x900 px
- Include four topology variants in grid

Content Requirements:
- Single-node edge, HA cluster, multi-site federation, hybrid cloud+edge
- Latency/throughput and cost tradeoffs per variant

Visual Elements:
- Four topology diagrams in 2x2 grid with short metrics and pros/cons

Wireframe Guidance:
Top left: single-node; top right: HA cluster; bottom left: multi-site; bottom right: hybrid cloud+edge

Acceptance Criteria:
- [ ] All four topologies clearly shown
- [ ] Each has latency/cost/scale notes
- [ ] Pros/cons bullets present

Microsoft Learn Adaptation:
- RAG patterns: https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/use-your-data

---

### Asset 31: RAG Monitoring and Observability

Context:
Provides a map of metrics/logs/traces and alerting for a production RAG deployment, enabling ops to set up observability.

Design Constraints:
- Canvas 1300x900 px
- Include Prometheus-style metrics and Azure Monitor integration pointers

Content Requirements:
- Data collection points, processing pipelines (metrics/logs/traces), alert routing, dashboards

Visual Elements:
- Pipelines with arrows from components to monitoring stack
- Dashboard mockups and feedback loop

Wireframe Guidance:
Left: RAG components; center: metrics & logs pipelines; right: dashboards & alerts

Acceptance Criteria:
- [ ] Data collection arrows from all major components
- [ ] Monitoring and logging tools labeled (Prometheus, Azure Monitor)
- [ ] Tracing and alert routing visible
- [ ] Dashboard and feedback loop included

Microsoft Learn Adaptation:
- Observability best practices: https://learn.microsoft.com/en-us/azure/architecture/best-practices/monitoring

---

## Module 4: Pre-Sales & Solution Design

### Asset 32: Customer Discovery Framework

Context:
Guides presales through discovery phases to map business drivers to solution recommendations.

Design Constraints:
- Canvas 1200x800 px
- Funnel or circular process

Content Requirements:
- Phases 1–5 with key questions
- Decision points and KPIs
- Mapping to solution recommendations

Visual Elements:
- Funnel with callouts, decision nodes, customer profiles

Wireframe Guidance:
Circular or funnel flow left-to-right with phase callouts and final recommendation box

Acceptance Criteria:
- [ ] All discovery phases present with key questions
- [ ] Decision tree leads to solution suggestions
- [ ] KPIs and success criteria included

Microsoft Learn Adaptation:
- Use customer-discovery context in docs/level-200/customer-discovery.md

---

### Asset 33: Solution Sizing Framework

Context:
Translates customer inputs into compute/storage/network sizing and cost estimates.

Design Constraints:
- Canvas 1300x800 px
- Include formula flow and outputs

Content Requirements:
- Input variables and calculation layers
- Example outputs and confidence ranges

Visual Elements:
- Flow diagram with inputs, calculations, and outputs; confidence/range visuals

Wireframe Guidance:
Top: inputs; mid: calculation layer with formulas; bottom: outputs and cost/ROI summary

Acceptance Criteria:
- [ ] Inputs, calculation layers, and outputs clearly shown
- [ ] Example numbers or formulas present
- [ ] Confidence ranges included

Microsoft Learn Adaptation:
- Cross-reference to docs/level-200/solution-sizing.md

---

### Asset 34: TCO and ROI Analysis Model

Context:
Comparative TCO/ROI modeling for sovereign vs standard cloud to aid decisions.

Design Constraints:
- Canvas 1400x900 px
- Include timeline graphs and sensitivity diagrams

Content Requirements:
- TCO categories, timeline, ROI drivers, break-even analysis

Visual Elements:
- Stacked cost charts, ROI waterfall and tornado sensitivity

Wireframe Guidance:
Top: stacked cost by year; mid: ROI waterfall; bottom: sensitivity chart

Acceptance Criteria:
- [ ] Breakdowns by cost category visible
- [ ] ROI waterfall and break-even point shown
- [ ] Sensitivity analysis present

Microsoft Learn Adaptation:
- Use cost-estimation guidance in docs/level-200/cost-estimation.md

---

## Module 5: Compliance & Security Patterns

### Asset 35: GDPR Compliance Mapping

Context:
Maps GDPR articles/principles to technical controls and evidence collection strategies in Azure Local and Arc deployments.

Design Constraints:
- Canvas 1400x900 px
- Include three-column layout (requirements → controls → evidence)

Content Requirements:
- GDPR principles and mapping to Azure controls
- Evidence examples and audit trace paths

Visual Elements:
- Three-column map, checkmark color coding, audit trail arrows

Wireframe Guidance:
Left: GDPR principles; center: technical controls; right: evidence and reporting flows

Acceptance Criteria:
- [ ] All major GDPR principles mapped
- [ ] Technical controls and service names present
- [ ] Evidence collection pathways shown
- [ ] References to EU Data Boundary where applicable

Microsoft Learn Adaptation:
- GDPR & EU Data Boundary references: https://learn.microsoft.com/en-us/privacy/eudb/eu-data-boundary-learn

---

### Asset 36: FedRAMP Compliance Architecture

Context:
Shows how Azure Local can be configured to meet FedRAMP control families and the ATO process.

Design Constraints:
- Canvas 1400x1000 px
- Highlight control-family mapping and continuous monitoring

Content Requirements:
- Control family mappings, encryption and access controls, continuous monitoring pipeline

Visual Elements:
- Layered architecture with control-family overlays and ATO roadmap

Wireframe Guidance:
Top: control families; mid: architecture mappings; bottom: monitoring and ATO steps

Acceptance Criteria:
- [ ] Control families annotated and mapped to services
- [ ] Encryption and access controls shown
- [ ] ATO steps and continuous monitoring pipeline illustrated

Microsoft Learn Adaptation:
- FedRAMP and Azure Government references: https://www.fedramp.gov/documents-repository/

---

### Asset 37: Encryption and Key Management Architecture

Context:
Depicts key lifecycle, HSM integration, BYOK/BYOHSM options, and where keys are used across systems.

Design Constraints:
- Canvas 1400x1000 px
- Use key lifecycle flow and pyramid hierarchy

Content Requirements:
- Key hierarchy, lifecycle stages, Key Vault/HSM integration, access controls, audit trails

Visual Elements:
- Pyramid for hierarchy, flowchart for lifecycle, management plane with Key Vault icons

Wireframe Guidance:
Top left: key hierarchy; top right: lifecycle flow; bottom: Key Vault/HSM integration and access controls

Acceptance Criteria:
- [ ] Key lifecycle shown with stages
- [ ] BYOK and HSM options depicted
- [ ] Integration with Key Vault illustrated
- [ ] Access control points and audits included

Microsoft Learn Adaptation:
- Key Vault overview: https://learn.microsoft.com/en-us/azure/key-vault/general/overview

---

### Asset 38: Zero-Trust Security Architecture

Context:
Visualizes Zero-Trust applied to identities, devices, networks, apps and data in sovereign cloud deployments.

Design Constraints:
- Canvas 1300x1000 px
- Centralized core with rings for pillars

Content Requirements:
- Core principle (verify, assume breach, secure layers) and mapping to Azure services

Visual Elements:
- Central core with radial pillars, service icons around ring, detection/response loop

Wireframe Guidance:
Core center: verify icon; surrounding rings: identity, endpoints, networks, data, apps; outer: detection & response

Acceptance Criteria:
- [ ] Core Zero-Trust principle shown
- [ ] Pillars mapped to Azure services
- [ ] Detection and response loop shown

Microsoft Learn Adaptation:
- Zero Trust guidance: https://learn.microsoft.com/en-us/security/zero-trust/

---

## Module 6: Hands-On Labs

### Asset 39: Lab Architecture Progression

Context:
Shows how labs build on each other producing an integrated stack by Lab 5; useful for instructors and students to see progression.

Design Constraints:
- Canvas 1400x900 px
- Stage-based layout

Content Requirements:
- Five lab stages with key components and dependencies
- Cumulative architecture snapshots
- Timing and cost indicators per stage

Visual Elements:
- Stacked stages with incremental complexity indicators
- Arrows for dependencies

Wireframe Guidance:
Left-to-right stage progression with mini-diagrams per lab and cumulative view at right

Acceptance Criteria:
- [ ] Each lab stage is clearly labeled and shows added components
- [ ] Dependencies and progression arrows present
- [ ] Cost/time per stage shown

Microsoft Learn Adaptation:
- Map to labs: docs/level-200/lab-01-azure-local-deployment.md etc.

---

### Asset 40: Lab Environment Cost and Time Matrix

Context:
Provides a matrix of estimated time and cost per lab and cumulative totals to help planning.

Design Constraints:
- Canvas 1200x800 px
- Table with bar-chart visual overlays

Content Requirements:
- Lab durations, resource costs, hardware costs, cumulative totals, variables

Visual Elements:
- Matrix table, timeline bar chart, cost pie breakdowns

Wireframe Guidance:
Top: matrix table with small chart overlays; bottom: timeline bar chart with cumulative markers

Acceptance Criteria:
- [ ] Duration and cost fields for each lab present
- [ ] Cumulative totals calculated and shown
- [ ] Variables and assumptions listed

Microsoft Learn Adaptation:
- Relate to labs overview: docs/level-200/labs-overview.md

---

## Summary & Next Steps

- Total assets specified: 20 (Assets 21–40)
- Each asset includes context, constraints, content, visuals, wireframes, acceptance criteria, and Learn references
- Next: integrate placeholders into `docs/level-200/*.md` (Phase 3)

---

Last Updated: October 21, 2025
