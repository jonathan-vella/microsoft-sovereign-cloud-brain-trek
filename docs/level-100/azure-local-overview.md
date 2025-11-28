---
layout: default
title: Overview
parent: Module 3 - Azure Local Overview
nav_order: 1
---

# Azure Local Overview

{: .no_toc }

## Table of Contents

{: .no_toc .text-delta }

1. TOC
{:toc}

---

{: .note }
> ⏱️ **Reading Time:** 20-25 min | 🎯 **Key Topics:** Hyperconverged infrastructure, Azure hybrid, sovereign deployment | 📋 **Prerequisites:** [Cloud Computing Primer](../level-50/cloud-computing-primer.md)

---

## What is Azure Local?

**Azure Local** (formerly known as Azure Stack HCI) is Microsoft's hybrid cloud platform that brings Azure services and cloud-based management to on-premises infrastructure. Released in 2024 as part of Microsoft's Cloud for Sovereignty initiative, Azure Local enables organizations to run virtualized workloads on validated hardware in their own data centers while maintaining consistent management through Azure Arc.

<details class="diagram-container" open>
<summary>View Diagram: Azure Local in Sovereign Cloud Strategy</summary>
<div class="diagram-content" markdown="1">

```mermaid
graph TB
    subgraph Azure["☁️ Azure Cloud"]
        AM[Azure Management]
        AArc[Azure Arc]
    end

    subgraph OnPrem["🏢 On-Premises"]
        AL[Azure Local Cluster]
        VM[Virtual Machines]
        K8s[Kubernetes]
        AI[AI/ML Workloads]
    end

    AM <-->|"Connected Mode"| AArc
    AArc <-->|"Management & Governance"| AL
    AL --> VM
    AL --> K8s
    AL --> AI

    style Azure fill:#e3f2fd,stroke:#0078d4
    style OnPrem fill:#fff3e0,stroke:#ef6c00
    style AL fill:#c8e6c9,stroke:#2e7d32
```

</div>
</details>

### Key Characteristics

Azure Local provides:

- **On-premises compute and storage** with Azure-consistent services
- **Flexible deployment modes**: Connected (hybrid with Azure) or Disconnected (air-gapped)
- **Data sovereignty guarantees** through local data processing and storage
- **Azure Arc integration** for unified management and governance
- **Validated hardware ecosystem** from Microsoft partners
- **Support for modern workloads** including containers, VMs, and AI/ML

### The Role in Sovereign Cloud Strategy

Azure Local serves as the **Sovereign Private Cloud** option in Microsoft's three-model approach to digital sovereignty. It addresses scenarios where organizations need:

- Physical control over infrastructure location
- The ability to operate without continuous cloud connectivity
- Complete operational sovereignty with local control planes
- Data processing that never leaves their premises
- Compliance with strict regulatory requirements

**[Review Digital Sovereignty Concepts →](digital-sovereignty)**

---

## History and Evolution

### From Azure Stack HCI to Azure Local

Azure Local represents the evolution of Microsoft's hybrid infrastructure platform:

**2019-2023: Azure Stack HCI Era**

- Introduced as hyper-converged infrastructure solution
- Focused on virtualization and storage
- Primarily connected mode deployment
- Limited sovereignty features

**2024: Azure Local Launch**

- Rebranded to emphasize cloud-native capabilities
- Enhanced disconnected mode support
- Strengthened sovereignty commitments
- Expanded AI/ML workload support
- Deeper Azure Arc integration

### Why the Evolution Matters

The transition to Azure Local reflects Microsoft's commitment to:

- **Sovereignty-first design**: Built with data residency and operational control as core principles
- **Edge computing readiness**: Optimized for latency-sensitive and disconnected scenarios
- **AI at the edge**: Native support for running AI/ML models locally
- **Simplified management**: Unified experience through Azure Arc

---

## Architecture and Deployment Models

Azure Local supports multiple deployment models to meet different scale and infrastructure requirements:

### Deployment Types

| Deployment Type | Scale | Storage | Status | Use Cases |
|-----------------|-------|---------|--------|-----------|
| **Hyperconverged** | 1-16 machines | Storage Spaces Direct | GA | Standard HCI, edge sites, branch offices |
| **Rack-Aware** | 4-8 machines (2 racks) | Storage Spaces Direct | Preview | Room/building-level HA, manufacturing |
| **Multi-Rack** | 100s of machines (4+ racks) | SAN storage | Preview | Large-scale enterprise, data centers |
| **Disconnected Operations** | 3+ node mgmt cluster | Storage Spaces Direct | Preview | Air-gapped, regulated environments |

{: .note }
> **📝 Source:** [Azure Local Scalability and Deployments](https://learn.microsoft.com/en-us/azure/azure-local/scalability-deployments) — Microsoft Learn (November 2025)

### Hyperconverged Deployments (GA)

The standard deployment model for most Azure Local scenarios:

**Characteristics:**

- **Scale:** 1-16 physical machines per cluster
- **Storage:** Storage Spaces Direct (local NVMe/SSD/HDD)
- **Networking:** Customer-managed physical switches and VLANs
- **Management:** Azure portal, CLI, ARM templates, Windows Admin Center

**Best For:**

- Edge computing and branch offices
- Sovereign and regulated workloads
- AI/ML inference at the edge
- Development and test environments
- Small to medium production workloads

**Reference:** [Hyperconverged Deployments Overview](https://learn.microsoft.com/en-us/azure/azure-local/overview/hyperconverged-overview)

### Rack-Aware Clustering (Preview)

Advanced architecture providing rack-level fault tolerance:

**Characteristics:**

- **Scale:** 4-8 machines across exactly 2 physical racks
- **Configuration:** Balanced nodes (2+2, 3+3, or 4+4)
- **Latency:** ≤1ms round-trip between racks required
- **Availability Zones:** Each rack functions as a local availability zone

**Best For:**

- Room or building-level high availability
- Manufacturing plants, hospitals, airports
- Environments requiring rack-level fault tolerance
- Mission-critical applications

**Reference:** [Rack-Aware Clustering Overview](https://learn.microsoft.com/en-us/azure/azure-local/concepts/rack-aware-cluster-overview)

### Multi-Rack Deployments (Preview)

Enterprise-scale deployments for large data center environments:

**Characteristics:**

- **Scale:** Hundreds of servers across multiple racks
- **Minimum:** 4 racks (1 aggregation + 3 compute racks)
- **Storage:** Built-in SAN storage shared across compute racks
- **Networking:** Azure-managed network devices and configuration
- **Hardware:** Prescriptive BOM with preintegrated racks

**Best For:**

- Large enterprise data centers
- High-performance computing environments
- Massive AI/ML training workloads
- Hyperscale sovereign deployments

{: .important }
> **Preview Access:** Multi-rack deployments are available for qualified opportunities. Contact your Microsoft account team to participate.

**Reference:** [Multi-Rack Deployments Overview](https://learn.microsoft.com/en-us/azure/azure-local/multi-rack/multi-rack-overview)

### System Architecture


---

### Deployment Modes Comparison


---

## Core Capabilities

### 1. Edge Compute and Storage

Azure Local delivers enterprise-grade compute and storage at customer locations:

**Compute Capabilities:**

- Hyper-V virtualization for Windows and Linux VMs
- Azure Kubernetes Service (AKS) for containerized workloads
- GPU acceleration support for AI/ML inference
- High-performance computing for specialized workloads
- Support for thousands of VMs per cluster

**Storage Capabilities:**

- Storage Spaces Direct for software-defined storage
- Tiered storage (NVMe, SSD, HDD) for performance optimization
- Deduplication and compression for efficiency
- Replication and erasure coding for data protection
- Up to petabytes of capacity per cluster

### 2. Disconnected Operation Capability

One of Azure Local's most powerful features is the ability to operate completely independently:

**Key Benefits:**

- **Air-gapped environments**: Run without any internet connectivity
- **Resilient to outages**: Continue operations during WAN failures
- **Sensitive workloads**: Keep classified or regulated data isolated
- **Periodic synchronization**: Update when connectivity is available
- **Local management**: All control functions available locally

**Use Case Example:**
> A manufacturing plant processes quality control data from IoT sensors using local AI models. Even during internet outages, production continues uninterrupted with all processing happening on Azure Local infrastructure.

### 3. Data Residency Guarantees

Azure Local ensures data sovereignty through:

- **Physical control**: All data stays on customer-owned hardware
- **Geographic boundaries**: Infrastructure deployed within specific locations
- **No automatic replication**: Data doesn't leave premises without explicit action
- **Encryption at rest**: All storage volumes encrypted by default
- **Compliance alignment**: Meet GDPR, HIPAA, FedRAMP requirements

**[Learn More About Data Residency →](data-residency-concepts)**

### 4. Customization and Control

Organizations maintain complete control over:

**Infrastructure Configuration:**

- Hardware selection from validated partners
- Network topology and security policies
- Storage architecture and tiering
- Resource allocation and scheduling

**Operational Control:**

- Local administrator access
- Update scheduling and deployment
- Backup and disaster recovery procedures
- Performance tuning and optimization

### 5. Integration with Azure Services

When deployed in Connected Mode, Azure Local integrates with:

**Management Services:**

- Azure Arc for unified governance
- Azure Monitor for observability
- Azure Security Center for threat protection
- Azure Backup for cloud-based data protection

**Application Services:**

- Azure Virtual Desktop for remote work
- Azure IoT Edge for device management
- Azure Machine Learning for AI/ML workflows
- Azure Data Services for managed databases

### 6. Support for AI/ML Workloads at Edge

Azure Local excels at running AI/ML workloads on-premises:

**Capabilities:**

- Local model deployment and inference
- GPU/NPU acceleration support
- Integration with Azure Machine Learning
- Support for popular frameworks (TensorFlow, PyTorch, ONNX)
- Real-time data processing for low-latency scenarios

**Edge RAG Benefits:**

- Run Retrieval-Augmented Generation systems locally
- Process sensitive documents without cloud transmission
- Maintain privacy for confidential information
- Reduce latency for real-time AI responses

**[Explore Edge RAG Concepts →](edge-rag-concepts)**

### 7. Microsoft 365 Local: Productivity at the Edge

{: .note }
> **📝 Source:** [What is Microsoft 365 Local?](https://learn.microsoft.com/en-us/azure/azure-local/concepts/microsoft-365-local-overview) — Microsoft Learn (November 2025)

**Microsoft 365 Local** enables organizations to run Exchange Server, SharePoint Server, and Skype for Business Server on Azure Local infrastructure that is entirely customer-owned and managed. It provides enhanced control over data residency, access, and compliance to meet sovereignty requirements.

**Key Capabilities:**

- **Complete Productivity Stack:** Exchange Server, SharePoint Server, and Skype for Business Server
- **Validated Architecture:** Full-stack deployment based on validated reference architecture with certified hardware
- **Azure Arc Integration:** Unified control plane with simplified deployment and streamlined updates
- **Sovereign Private Cloud:** Built on Azure Local with Arc-enabled management for hybrid control
- **Connectivity Flexibility:** Supports both hybrid connectivity and fully disconnected operations

**Supported Workloads:**

- **Exchange Server** — Enterprise email, calendaring, and unified communications
- **SharePoint Server** — Document management, collaboration, and intranet
- **Skype for Business Server** — Unified communications and presence

**Designed For:**

- **Governments:** Organizations needing the strictest jurisdictional and sovereignty mandates
- **Regulated Industries:** Finance, healthcare, defense requiring complete data residency control
- **Sovereign Cloud:** Organizations requiring private cloud with Azure-consistent management
- **Disconnected Environments:** Air-gapped operations with complete isolation

**Hardware Requirements (Enterprise Baseline):**

The baseline architecture consists of 9 physical servers (Premier Solutions certified):

| Role | Configuration | Purpose |
|------|---------------|--------|
| SharePoint + SQL | 3-node Azure Local cluster | Document management and databases |
| Exchange Mailbox | 4 × single-node clusters | Email storage and processing |
| Exchange Edge Transport | 2 × single-node clusters | Mail routing and security |

{: .important }
> **Partner Deployment Required:** Microsoft 365 Local must be deployed by a certified Microsoft 365 Local solution partner. Contact your Microsoft account team or visit [https://aka.ms/m365localsignup](https://aka.ms/m365localsignup).

**Use Case Example:**
> A government agency runs Microsoft 365 Local on Azure Local in Disconnected Mode to provide email, collaboration, and unified communications on classified networks. All productivity data remains within the air-gapped environment.

**Reference:** [What is Microsoft 365 Local?](https://learn.microsoft.com/en-us/azure/azure-local/concepts/microsoft-365-local-overview) — Microsoft Learn

### 8. Security and Encryption at Rest

Azure Local implements defense-in-depth security:

**Security Layers:**

- **BitLocker encryption**: All volumes encrypted by default
- **Secure Boot and TPM**: Hardware root of trust
- **Code integrity**: Signed drivers and components only
- **Network isolation**: Micro-segmentation support
- **RBAC and MFA**: Granular access controls
- **Security baselines**: CIS and STIG compliance

**Reference:** [Azure Local Security Best Practices](https://learn.microsoft.com/en-us/azure/azure-local/concepts/security-features?view=azloc-2509)

---

## Deployment Modes Comparison

Azure Local supports two distinct deployment modes, each optimized for different scenarios.

### Connected Mode

**Definition:** Azure Local clusters maintain continuous or regular connectivity to Azure cloud services.

**Characteristics:**

- Bidirectional communication with Azure
- Real-time synchronization of management data
- Full access to hybrid cloud features
- Cloud-based monitoring and alerting
- Automatic updates from Azure
- Azure-based backup and disaster recovery

**Network Requirements:**

- Outbound HTTPS (443) connectivity
- Minimum 1-5 Mbps bandwidth
- Latency < 250ms to Azure region
- Intermittent connectivity acceptable (not continuous)

**Best For:**

- Organizations with reliable internet connectivity
- Scenarios requiring cloud integration
- Workloads needing Azure services
- Standard enterprise deployments

### Disconnected Mode

**Definition:** Azure Local clusters operate independently without continuous Azure connectivity.

**Characteristics:**

- Autonomous operation for extended periods
- Local management and monitoring
- Periodic synchronization (when connected)
- Limited feature set vs. Connected Mode
- All data and processing stays on-premises
- Manual update deployment

**Network Requirements:**

- No continuous connectivity required
- Optional periodic connection for updates
- Can be completely air-gapped
- Local management network only

**Best For:**

- Air-gapped environments
- Classified or highly sensitive workloads
- Remote locations with unreliable connectivity
- Compliance requirements prohibiting cloud communication
- Defense and intelligence agencies

### Comparison Table: Connected vs. Disconnected

| Feature | Connected Mode | Disconnected Mode |
|---------|---------------|-------------------|
| **Azure Connectivity** | Continuous or regular | Optional/periodic |
| **Real-time Monitoring** | ✅ Yes | ❌ No (local only) |
| **Cloud-based Backup** | ✅ Available | ❌ Limited |
| **Automatic Updates** | ✅ Yes | ❌ Manual only |
| **Azure Arc Management** | ✅ Full integration | ⚠️ Limited |
| **Azure Services** | ✅ Many available | ❌ Very limited |
| **Offline Operation** | ⚠️ Limited duration | ✅ Indefinite |
| **Data Sovereignty** | ✅ High | ✅ Maximum |
| **Operational Complexity** | 🟢 Lower | 🟡 Higher |
| **Recommended Use** | Most scenarios | Air-gapped only |

**Decision Guidance:**

- **Choose Connected** if you have reliable internet and want full Azure integration
- **Choose Disconnected** if you must operate air-gapped or have strict isolation requirements
- **Consider Hybrid** approach: Start Connected, support Disconnected fallback

---

## Architecture Overview

### Physical Architecture

Azure Local physical architecture includes:

**Hardware Layer:**

- 1-16 node clusters (2-4 nodes typical for HA)
- Validated hardware from Microsoft partners
- Server-grade processors (Intel Xeon, AMD EPYC)
- 384GB-6TB RAM per node
- NVMe SSD and HDD storage
- 10GbE or 25GbE networking minimum
- Redundant power supplies and fans

**Network Architecture:**

- Management network (1GbE minimum)
- Storage network (10/25GbE recommended)
- Compute network (10/25GbE recommended)
- Optional external connectivity
- Software-defined networking (SDN) support

**[Deep Dive: Hardware Requirements →](azure-local-hardware)**

### Logical Components

**Control Plane:**

- Azure Arc agents (Connected Mode)
- Local management APIs
- PowerShell and Windows Admin Center
- Failover clustering services
- Health monitoring services

**Data Plane:**

- Hyper-V virtualization
- Storage Spaces Direct
- Software-defined networking
- VM and container workloads
- Storage volumes and shares

**Management Plane:**

- Azure portal (Connected Mode)
- Windows Admin Center (both modes)
- PowerShell scripting
- Azure Policy enforcement
- Update management


### Integration Points with Azure

When in Connected Mode:

**Management Integration:**

- Azure Arc for resource inventory
- Azure Monitor for metrics and logs
- Azure Security Center for security posture
- Azure Policy for governance compliance
- Azure Update Manager for patch management

**Data Integration:**

- Azure Backup for VM protection
- Azure Site Recovery for DR
- Azure File Sync for file services
- Azure Blob replication (optional)

**Application Integration:**

- Azure Virtual Desktop sessions
- Azure IoT Edge modules
- Azure Machine Learning endpoints
- Azure Cognitive Services

### Network Requirements and Considerations

**Bandwidth Planning:**

- **Minimum**: 1-5 Mbps per cluster for management
- **Recommended**: 50-100 Mbps for hybrid features
- **Optimal**: 1+ Gbps for data replication/backup

**Latency Targets:**

- To Azure region: < 250ms acceptable
- Between nodes: < 2ms required
- Storage network: < 1ms optimal

**Firewall Requirements:**

- Outbound HTTPS (443) for Azure services
- Specific URLs for Azure Arc, monitoring, updates
- No inbound connections from internet required

**[Deep Dive: Network Architecture →](azure-local-architecture)**

### Scalability Patterns

**Vertical Scaling:**

- Add memory and storage to existing nodes
- Upgrade CPUs to newer generations
- Increase network bandwidth
- Add GPU/NPU accelerators

**Horizontal Scaling:**

- Add nodes to cluster (up to 16)
- Distribute workloads across nodes
- Increase aggregate resources
- Improve redundancy and availability

**Multi-Cluster:**

- Deploy multiple independent clusters
- Geographic distribution for DR
- Workload isolation by environment
- Centralized management via Azure Arc

### High Availability Design

Azure Local provides multiple HA mechanisms:

**Cluster-Level:**

- Node failure tolerance (N-1 or N-2)
- Automatic VM live migration
- Storage replica for data protection
- Network path redundancy

**Storage-Level:**

- Two-way or three-way mirroring
- Erasure coding for capacity optimization
- Auto-repair of failed disks
- No single point of failure

**Network-Level:**

- NIC teaming for redundancy
- Multiple paths for storage traffic
- SDN for traffic optimization
- Load balancing across links

---

## Customer Scenarios

### Scenario 1: Manufacturing Plant Quality Control (Disconnected Mode)

**Industry:** Manufacturing  
**Company Size:** Large multinational manufacturer  
**Location:** Multiple plants worldwide

**Challenge:**

- Real-time quality control using AI/ML vision systems
- Process sensitive manufacturing data that cannot leave premises
- Unreliable internet connectivity in some plant locations
- Need to comply with industrial espionage prevention policies
- 99.9% uptime requirement for production lines

**Solution: Disconnected Azure Local Deployment**

**Implementation:**

- 4-node Azure Local clusters at each plant
- GPU acceleration for AI model inference
- Local storage for manufacturing data (100TB+)
- Disconnected Mode operation with monthly sync for updates
- Edge RAG system for equipment manual queries

**Technical Details:**

- Hyper-V VMs running quality control software
- AKS for containerized AI workloads
- Storage Spaces Direct with three-way mirroring
- Local backup to separate Azure Local cluster
- Windows Admin Center for local management

**Benefits Achieved:**

- ✅ 100% data sovereignty - no data leaves plant
- ✅ Zero dependency on internet connectivity
- ✅ Sub-10ms latency for quality control decisions
- ✅ Reduced cloud costs (no egress, no continuous licensing)
- ✅ Meets compliance requirements for IP protection

**Sales Talking Point:**
> "Azure Local Disconnected Mode gives manufacturers the power of Azure's AI and analytics while guaranteeing that sensitive production data never leaves the facility. You get cloud capabilities without cloud dependency."

**Discovery Questions:**

- How critical is internet connectivity to your operations?
- What happens to your production if WAN goes down?
- Do you process sensitive intellectual property on-premises?
- What are your data residency requirements?

---

### Scenario 2: Hospital Network with HIPAA Compliance (Connected Mode)

**Industry:** Healthcare  
**Company Size:** Regional hospital network (5 facilities)  
**Location:** United States (single state)

**Challenge:**

- Manage patient data across multiple facilities
- Meet HIPAA compliance requirements
- Provide high-performance access to EMR/EHR systems
- Support radiology image processing (large files)
- Enable disaster recovery and business continuity
- Control costs vs. pure cloud deployment

**Solution: Connected Azure Local with Hybrid Cloud**

**Implementation:**

- 3-node Azure Local cluster per facility (15 nodes total)
- Connected Mode with Azure Arc management
- Azure Backup for cloud-based data protection
- Azure Site Recovery for cross-facility DR
- Encrypted replication between sites

**Technical Details:**

- VMs hosting electronic medical records (EMR) systems
- SQL Server on Azure Local for patient databases
- High-speed storage for radiology images (PACS)
- Azure Policy enforcement for HIPAA controls
- Azure Security Center for threat monitoring

**Benefits Achieved:**

- ✅ HIPAA-compliant infrastructure with auditing
- ✅ Low-latency access to patient records (< 5ms)
- ✅ Data stays within US (meets residency requirements)
- ✅ Cloud-based DR without moving primary data
- ✅ 60% cost savings vs. running only in Azure
- ✅ Centralized security and compliance management

**Sales Talking Point:**
> "Healthcare providers get local performance for patient care systems while maintaining HIPAA compliance and centralized Azure-based governance. It's the best of both worlds."

**Discovery Questions:**

- What's your current EMR/EHR response time requirement?
- Where does your patient data currently reside?
- How do you handle disaster recovery today?
- What compliance frameworks must you maintain?

---

### Scenario 3: Financial Services Branch Network (Connected Mode)

**Industry:** Financial Services (Regional Bank)  
**Company Size:** 150 branch locations, 5000 employees  
**Location:** European Union (multi-country)

**Challenge:**

- Real-time transaction processing at branch locations
- Data residency requirements (GDPR, local banking regulations)
- Low-latency customer-facing applications
- Need for consistent security policies across all branches
- Integration with central Azure environment
- Support for AI-powered fraud detection

**Solution: Connected Azure Local at Branch Edge**

**Implementation:**

- 2-node Azure Local clusters at each branch (300 nodes total)
- Connected Mode for Azure Arc centralized management
- Local transaction processing with Azure integration
- AI model deployment for fraud detection
- Centralized policy and update management

**Technical Details:**

- Branch banking applications on local VMs
- Azure SQL Edge for local transaction databases
- Real-time replication to central Azure SQL Database
- Azure Arc-enabled SQL for consistent management
- GPU-enabled nodes for AI/ML fraud detection

**Benefits Achieved:**

- ✅ Sub-5ms response time for customer transactions
- ✅ GDPR compliance (data stays in EU)
- ✅ 99.95% uptime even during internet disruptions
- ✅ Centralized security policy enforcement
- ✅ Real-time fraud detection at point of transaction
- ✅ Unified management for 150+ locations via Azure Arc

**Sales Talking Point:**
> "Banks can provide instant customer service while meeting strict EU data residency laws. Azure Arc lets them manage 150 locations as easily as 1, with consistent security and governance."

**Discovery Questions:**

- How many remote locations do you operate?
- What's your latency requirement for transactions?
- What data residency requirements do you have?
- How do you manage security across distributed locations?

---

### Scenario 4: Retail Distribution Center Inventory (Disconnected Mode)

**Industry:** Retail  
**Company Size:** Global retailer with 50 distribution centers  
**Location:** Worldwide

**Challenge:**

- Manage inventory systems during WAN outages
- 24/7 operations cannot tolerate connectivity dependencies
- Periodic synchronization with central systems
- Need for local analytics and reporting
- Support seasonal peak demand variations
- Meet regional data residency requirements

**Solution: Disconnected Azure Local with Scheduled Sync**

**Implementation:**

- 3-node Azure Local clusters at each distribution center
- Disconnected Mode for autonomous operation
- Nightly synchronization with central Azure (when available)
- Local SQL Server for inventory database
- Power BI reports generated locally

**Technical Details:**

- Warehouse management system (WMS) on local VMs
- AKS for microservices architecture
- Azure Data Box for bulk data transfer
- Scheduled sync during off-peak hours
- Local redundancy for business continuity

**Benefits Achieved:**

- ✅ 100% uptime during WAN failures
- ✅ Zero impact from internet outages
- ✅ Local analytics and reporting available 24/7
- ✅ Reduced WAN bandwidth costs
- ✅ Data sovereignty for each region
- ✅ Cloud capabilities without cloud dependency

**Sales Talking Point:**
> "Retailers need operations that never stop. Azure Local Disconnected Mode means inventory systems run perfectly whether the internet is up or down. Sync to cloud when convenient, operate independently always."

**Discovery Questions:**

- How often do you experience WAN outages?
- What's the business impact of connectivity loss?
- Do you need real-time sync with headquarters?
- What analytics do you need at each location?

---

### Scenario 5: Research Facility Machine Learning (Connected Mode)

**Industry:** Scientific Research  
**Company Size:** National research laboratory  
**Location:** Multiple global sites

**Challenge:**

- Train and run ML models on sensitive research data
- Data cannot leave country due to national security
- Need massive compute for simulations
- Support for GPU-accelerated workloads
- Collaboration with cloud-based researchers (limited)
- Ensure data sovereignty while enabling innovation

**Solution: Connected Azure Local with GPU Acceleration**

**Implementation:**

- 8-node Azure Local cluster with NVIDIA GPUs
- Connected Mode for Azure ML integration
- Local training on sensitive datasets
- Selective result sharing to Azure
- Hybrid approach: sensitive local, general in cloud

**Technical Details:**

- VMs with GPU passthrough for ML training
- AKS with GPU support for inference
- Large-scale storage (1PB+) for datasets
- Azure Machine Learning integration
- Jupyter notebooks and ML frameworks

**Benefits Achieved:**

- ✅ Train models on sensitive data locally
- ✅ GPU performance for compute-intensive workloads
- ✅ Data never leaves facility without approval
- ✅ Integration with Azure ML for approved workloads
- ✅ Cost savings vs. cloud GPU compute (50%+)
- ✅ Meets national security data requirements

**Sales Talking Point:**
> "Researchers get the compute power they need for breakthrough science while ensuring sensitive data stays under their control. Train locally on classified data, deploy to cloud only what's approved."

**Discovery Questions:**

- What type of compute workloads do you run?
- Is GPU acceleration required?
- What are your data classification levels?
- Can any workloads move to cloud?

---

## Sales Talking Points

### For All Customers

**1. Sovereignty + Performance = Azure Local**

- Keep sensitive data and processing on your premises
- Get Azure-consistent management and services
- Meet data residency requirements without compromise
- Maintain operational control and independence

**2. Keep Sensitive Data and Processing On-Premises**

- Physical control over infrastructure location
- Data never leaves your facility (Disconnected Mode)
- Meet strictest compliance and regulatory requirements
- Protect intellectual property and trade secrets

**3. No Internet Dependency for Critical Workloads**

- Operate continuously during WAN outages
- Zero cloud dependency for core operations
- Ideal for remote locations with poor connectivity
- Business continuity without cloud connectivity

**4. Consistent Azure Experience at the Edge**

- Same tools and processes as Azure public cloud
- Familiar management interfaces (portal, PowerShell)
- Consistent security and governance policies
- Simplified operations across hybrid environment

**5. Enterprise-Grade SLA and Support**

- Microsoft-validated hardware ecosystem
- Premier support from Microsoft and partners
- 99.9% uptime SLA when properly configured
- Regular updates and security patches

**6. Cost-Effective for Compute-Heavy Workloads**

- No egress charges for local processing
- Predictable costs with owned hardware
- Lower total cost for sustained workloads
- Avoid cloud compute costs for 24/7 operations

**7. Seamless Hybrid with Azure Cloud**

- Connected Mode integrates with Azure services
- Unified management via Azure Arc
- Cloud backup and disaster recovery
- Flexibility to move workloads as needed

### Competitive Differentiation

**vs. AWS Outposts:**

- More flexible licensing (no minimum commitments)
- Better disconnected mode support
- Stronger sovereignty commitments
- More hardware partner choices

**vs. Google Anthos:**

- Deeper operating system integration
- Better VM workload support
- More mature hybrid management (Azure Arc)
- Stronger in regulated industries

**vs. Pure On-Premises:**

- Cloud-based management and updates
- Access to Azure services when connected
- Modern architecture (SDN, containers)
- Future-proof investment

---

## Discovery Questions for Customers

### Data Sovereignty and Compliance

1. **What data residency requirements do you have?**
   - Helps identify sovereignty needs
   - Determines Connected vs. Disconnected mode

2. **What compliance frameworks apply to your workloads?**
   - GDPR, HIPAA, FedRAMP, ITAR, etc.
   - Validates Azure Local's compliance alignment

3. **Do you process sensitive or classified data?**
   - Identifies need for physical isolation
   - Determines security requirements

### Connectivity and Operations

1. **How critical is continuous cloud connectivity to your operations?**
   - Determines deployment mode
   - Identifies resilience requirements

2. **What happens to your operations if internet/WAN fails?**
   - Quantifies business impact
   - Justifies Disconnected Mode investment

3. **What's your typical bandwidth to the internet?**
   - Validates feasibility of Connected Mode
   - Identifies potential constraints

### Workloads and Requirements

1. **What applications would you run on Azure Local?**
   - VMs, containers, databases, AI/ML
   - Determines sizing and configuration

2. **Are you running AI/ML workloads?**
   - Identifies need for GPU acceleration
   - Validates edge RAG scenarios

3. **What's your performance requirement (latency, throughput)?**
   - Determines storage and network specs
   - Validates need for on-premises deployment

### Investment and Timeline

1. **What's your hardware refresh timeline?**
    - Identifies opportunity for Azure Local
    - Validates investment timing

2. **What's your budget for infrastructure investment?**
    - Determines cluster size and configuration
    - Validates hardware choices

3. **Do you have existing VMware or Hyper-V infrastructure?**
    - Identifies migration opportunities
    - Validates Azure Local as upgrade path

---

## Decision Framework

### When to Choose Azure Local

Azure Local is the right choice when you need:

**✅ Strong Yes Indicators:**

- Data must stay on-premises for sovereignty/compliance
- Low-latency access to data is critical (< 10ms)
- Operations must continue during internet outages
- Compute-intensive workloads run 24/7
- Strict control over infrastructure is required
- Edge AI/ML processing is needed

**⚠️ Consider Carefully:**

- Budget for hardware investment available
- Staff to manage on-premises infrastructure
- Compliance requirements justify the complexity
- Workload performance justifies local deployment

**❌ Not Recommended:**

- Workloads are purely development/test
- No specific data residency requirements
- Limited infrastructure management expertise
- Highly variable compute demands (cloud bursting better)
- Very small scale (< 10 VMs)

### Decision Tree: Connected vs. Disconnected Mode

```text
Start
  ↓
Can you have continuous/regular internet connectivity?
  ├─ Yes → Do you need Azure integration (backup, monitoring, management)?
  │         ├─ Yes → CHOOSE CONNECTED MODE
  │         └─ No → Can you tolerate occasional outages?
  │                   ├─ Yes → CHOOSE CONNECTED MODE (simpler)
  │                   └─ No → CHOOSE DISCONNECTED MODE
  └─ No → Do you need to operate air-gapped?
            ├─ Yes → CHOOSE DISCONNECTED MODE (required)
            └─ No → Do you have unreliable connectivity?
                      ├─ Yes → CHOOSE DISCONNECTED MODE
                      └─ No → Re-evaluate connectivity assumption
```


### Comparison with Alternatives

| Criteria | Azure Local | Sovereign Public Cloud | Pure On-Premises |
|----------|-------------|----------------------|------------------|
| **Data Location Control** | ✅ Complete | ⚠️ Logical only | ✅ Complete |
| **Cloud Integration** | ✅ Full (Connected) | ✅ Native | ❌ Limited |
| **Disconnected Operation** | ✅ Yes | ❌ No | ✅ Yes |
| **Management Complexity** | 🟡 Medium | 🟢 Low | 🔴 High |
| **Initial Investment** | 🟡 Moderate-High | 🟢 Low (OpEx) | 🔴 High |
| **Operational Costs** | 🟡 Medium | 🟡 Medium-High | 🟢 Low (no cloud) |
| **Scalability** | 🟡 Good (hardware-limited) | ✅ Excellent | ❌ Poor |
| **Time to Deploy** | 🟡 Weeks | 🟢 Minutes | 🔴 Months |
| **Best For** | Edge, sovereignty, hybrid | Sovereign + scale | Legacy, specialized |

### Cost Considerations

**Initial Investment (per cluster):**

- Hardware: $50,000 - $500,000+
- Licensing: Windows Server DataCenter, Azure Local licenses
- Network infrastructure: $10,000 - $50,000
- Professional services: $20,000 - $100,000
- **Total**: $80,000 - $650,000+ per cluster

**Ongoing Costs:**

- Azure management services (Connected Mode): $1,000 - $10,000/year
- Support and maintenance: 15-20% of hardware cost annually
- Power and cooling: $5,000 - $50,000/year depending on scale
- Staff time: Varies by organization

**Break-Even Analysis:**

- Typically 2-3 years vs. equivalent cloud compute
- Faster break-even for 24/7 compute workloads
- Consider data egress savings for data-intensive apps

### Timeline for Deployment

**Typical Deployment Schedule:**

**Weeks 1-2: Planning**

- Requirements gathering
- Sizing and hardware selection
- Network design
- Compliance validation

**Weeks 3-4: Procurement**

- Hardware ordering
- Lead time for delivery
- Licensing acquisition

**Weeks 5-6: Installation**

- Hardware rack and stack
- Network configuration
- Physical security setup

**Weeks 7-8: Deployment**

- Azure Local cluster installation
- Azure Arc registration (if Connected)
- Testing and validation
- Security hardening

**Weeks 9-10: Migration**

- Workload migration
- Performance testing
- User acceptance testing
- Documentation

**Total: 10-12 weeks** for typical deployment

**Expedited: 6-8 weeks** with pre-validated configurations  
**Complex: 16-20 weeks** for large or highly customized deployments

---

## Deep Dive Topics

Ready to explore Azure Local in depth? Continue with these detailed topics:

### [Azure Local Architecture Deep Dive](azure-local-architecture)

Explore the physical and logical architecture, including hardware topology, networking design, storage architecture, and high availability patterns.

**Topics Covered:**

- Physical infrastructure requirements
- Hardware topology and placement
- Networking architecture details
- Security layers and encryption
- Control plane vs. data plane
- Integration with Azure cloud control plane

**Duration:** 25-30 minutes

---

### [Connected Mode Operations](azure-local-connected-mode)

Learn how Azure Local integrates with Azure services in Connected Mode, including management, monitoring, backup, and hybrid workloads.

**Topics Covered:**

- Prerequisites and connectivity requirements
- Real-time synchronization with Azure
- Feature availability in Connected Mode
- Management and monitoring capabilities
- Update and patching procedures
- Customer use cases

**Duration:** 20-25 minutes

---

### [Disconnected Mode Operations](azure-local-disconnected-mode)

Understand how Azure Local operates in air-gapped and disconnected environments, including management strategies and feature limitations.

**Topics Covered:**

- What is Disconnected Mode?
- When Disconnected Mode is necessary
- Feature limitations vs. Connected Mode
- Periodic synchronization strategy
- Management without continuous cloud connection
- Security in disconnected scenarios

**Duration:** 25-30 minutes

---

### [Hardware Requirements & Planning](azure-local-hardware)

Get detailed guidance on hardware requirements, validated partners, sizing, and deployment planning.

**Topics Covered:**

- Hardware requirements overview
- Approved hardware partners and systems
- CPU, memory, storage specifications
- Network adapter requirements
- Sizing guidance based on workload types
- Deployment checklist

**Duration:** 20-25 minutes

---

## Knowledge Check

Ready to test your understanding of Azure Local? Take the module quiz:

### [Azure Local Knowledge Check Quiz →](azure-local-quiz)

**Quiz Details:**

- 15 multiple-choice questions
- Mix of conceptual and scenario-based questions
- Covers all aspects of Azure Local
- Passing score: 80% (12 of 15)
- Estimated time: 15-20 minutes

**Topics Covered:**

- Azure Local fundamentals and capabilities
- Connected vs. Disconnected mode selection
- Architecture and hardware requirements
- Customer scenarios and use cases
- Decision-making and planning
- Compliance and sovereignty aspects

---

## Next Steps

After completing this module:

1. **✅ Review Deep Dive Topics**
   - Read all four sub-pages for comprehensive understanding
   - Focus on areas most relevant to your role

2. **✅ Take the Knowledge Check**
   - Complete the quiz to validate your learning
   - Review explanations for missed questions

3. **✅ Explore Related Modules**
   - [Digital Sovereignty Fundamentals](digital-sovereignty) - Core concepts
   - [Microsoft Sovereign Cloud Models](sovereign-cloud-models) - Model comparison
   - [Azure Arc Introduction](azure-arc-intro) - Hybrid management

4. **🎯 Continue to Next Module**
   - [Azure Arc Introduction →](azure-arc-intro) - Learn how Arc extends Azure management

---

## Additional Resources

### Microsoft Learn Modules

- **[What is Azure Local?](https://learn.microsoft.com/en-us/azure/azure-local/overview?view=azloc-2509)**
  - Official product overview
  - Architecture fundamentals
  - Getting started guide

- **[Azure Local Concepts](https://learn.microsoft.com/en-us/azure/azure-local/overview?view=azloc-2509)**
  - Deep technical documentation
  - Architecture patterns
  - Best practices

- **[Plan an Azure Local deployment](https://learn.microsoft.com/en-us/azure/azure-local/plan/cloud-deployment-network-considerations?view=azloc-2509)**
  - Sizing calculator
  - Hardware requirements
  - Network planning

### Partner Resources

- **[Azure Local Hardware Partners](https://azurestackhcisolutions.azure.microsoft.com/)**
  - Validated hardware catalog
  - Partner solutions
  - Pricing information

- **[Azure Local YouTube Channel](https://www.youtube.com/@AzureLocal)**
  - Product demos
  - Technical deep dives
  - Customer stories

### Community and Support

- **[Azure Local Tech Community](https://techcommunity.microsoft.com/t5/azure-local/ct-p/AzureLocal)**
  - Discussion forums
  - Product updates
  - Best practices

- **[Azure Local Blog](https://techcommunity.microsoft.com/t5/azure-local-blog/bg-p/AzureLocalBlog)**
  - Latest announcements
  - Feature updates
  - Case studies

---

**Last Updated:** October 2025
