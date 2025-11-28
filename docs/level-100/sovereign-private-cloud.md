---
layout: default
title: Sovereign Private Cloud
parent: Module 2 - Sovereign Cloud Models
nav_order: 2.2
---

# Sovereign Private Cloud

{: .no_toc }

Dedicated infrastructure running Azure services on-premises via Azure Local, providing physical isolation and local control.

---

## Table of Contents

{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What is Sovereign Private Cloud?

**Sovereign Private Cloud** delivers Azure services on dedicated, customer-owned infrastructure, providing the **highest level of sovereignty and control** while maintaining Azure-consistent operations and management. It represents the evolution from traditional on-premises infrastructure to modern hyperconverged infrastructure (HCI) with cloud-like capabilities.

### Core Concept

Sovereign Private Cloud brings Azure **to your data**, not your data to Azure. It provides:

- **Physical Isolation:** Dedicated hardware in customer-controlled facilities
- **Operational Independence:** Ability to operate with or without cloud connectivity
- **Local Control:** Customer control over hardware, updates, and operations
- **Azure Consistency:** Same APIs, tools, and management as Azure cloud
- **Flexible Connectivity:** Connected (hybrid) or Disconnected (air-gapped) modes

**Powered By: Azure Local** (formerly Azure Stack HCI)

**Key Principle:** "Azure services anywhere, including completely disconnected"

---

## Azure Local: Foundation of Sovereign Private Cloud

### What is Azure Local?

**Azure Local** is Microsoft's hyperconverged infrastructure (HCI) solution that brings Azure services to on-premises or edge locations. It combines:

- **Compute:** Hyper-V virtualization for VMs and containers
- **Storage:** Storage Spaces Direct for software-defined storage
- **Networking:** Software-Defined Networking (SDN) for virtual networks
- **Management:** Azure Arc for cloud-based management (Connected mode) or Windows Admin Center (Disconnected mode)

**Official Definition from Microsoft:**
> "Azure Local is a hyperconverged infrastructure (HCI) cluster solution that hosts virtualized Windows and Linux workloads and their storage in a hybrid on-premises environment. Azure Local brings Azure services, cloud-based management, and security to customer datacenters and edge locations." - [Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-local/overview)

---

### Azure Local vs. Traditional Infrastructure

| Aspect | Traditional On-Premises | Azure Local |
|--------|-------------------------|-------------|
| **Infrastructure Model** | Separate compute, storage, networking | Hyperconverged (integrated) |
| **Scalability** | Scale by adding separate components | Scale by adding nodes |
| **Management** | Multiple vendor tools | Unified Azure management |
| **Updates** | Manual, per-component | Orchestrated cluster updates |
| **Cloud Integration** | Limited or custom | Native Azure integration |
| **Deployment Time** | Weeks to months | Days to weeks |
| **Cost Model** | Pure CapEx | CapEx + subscription |
| **Azure Services** | Not available | Available (VMs, AKS, Arc) |

---

## Operating Modes: Connected vs. Disconnected

Azure Local supports two operating modes that provide different levels of sovereignty and cloud integration:

### Connected Mode (Hybrid Cloud)

**Description:** Azure Local cluster maintains **ongoing connectivity to Azure** for hybrid services, monitoring, and management.

**Connectivity Requirements:**

- Outbound HTTPS (port 443) to Azure endpoints
- Minimum bandwidth: 100 Mbps (1 Gbps recommended)
- Latency: <200ms to Azure region
- Internet connectivity (direct or via proxy)

**Key Capabilities:**

- ✅ Azure Arc-enabled management
- ✅ Azure portal visibility and management
- ✅ Azure Monitor and Log Analytics
- ✅ Azure Backup and Site Recovery
- ✅ Azure Update Management
- ✅ Azure Kubernetes Service (AKS) on Azure Local
- ✅ Azure Virtual Desktop on Azure Local
- ✅ Billing and cost management via Azure
- ✅ Azure Arc-enabled data services (SQL Managed Instance, PostgreSQL)

**Management Experience:**

- Manage from Azure portal
- Use Azure CLI, PowerShell, ARM templates
- Unified experience with Azure cloud
- Azure RBAC for access control
- Azure Policy for governance

**When to Use Connected Mode:**

- Hybrid cloud scenarios with some workloads in Azure, some on-premises
- Need for cloud-based management and monitoring
- Integration with Azure services (backup, DR, AI/ML)
- Acceptable to have dependency on Azure connectivity
- Want latest Azure innovations immediately

**[Learn More: Connected deployment](https://learn.microsoft.com/en-us/azure/azure-local/deploy/deployment-introduction?view=azloc-2509)**

---

### Disconnected Mode (Air-Gapped)

**Description:** Azure Local cluster operates **without any connectivity to Azure or the internet**, providing maximum sovereignty and operational independence.

**Connectivity Requirements:**

- ❌ No internet connectivity required
- ❌ No Azure connectivity required
- ✅ Local network only (optional)
- ✅ Can be completely air-gapped

**Key Capabilities:**

- ✅ Fully functional without internet
- ✅ Local control plane (no cloud dependencies)
- ✅ Windows Admin Center for management
- ✅ Run VMs and containers
- ✅ Software-defined storage and networking
- ✅ Local updates via removable media
- ✅ Complete operational independence

**Limited Capabilities (vs. Connected):**

- ❌ No Azure portal management
- ❌ No cloud-based monitoring (Azure Monitor)
- ❌ No Azure Arc services
- ❌ Manual update process
- ❌ Local backup solutions only

**Management Experience:**

- Windows Admin Center on management PC
- PowerShell remoting to cluster nodes
- Local domain controllers for identity
- Local monitoring tools (System Center, third-party)
- Manual license activation via phone or email

**When to Use Disconnected Mode:**

- Defense and intelligence workloads (classified information)
- Critical infrastructure with air-gap requirements
- Compliance mandates preventing internet connectivity
- Harsh environments (maritime, remote locations)
- Maximum sovereignty and zero external dependencies

**[Learn More: Disconnected deployment](https://learn.microsoft.com/en-us/azure/azure-local/manage/disconnected-operations-overview?view=azloc-2509)**

---

### Mode Comparison

| Feature | Connected Mode | Disconnected Mode |
|---------|---------------|-------------------|
| **Internet Connectivity** | Required | Not required |
| **Azure Portal Management** | Yes | No |
| **Azure Arc** | Yes | No |
| **Azure Monitor** | Yes | No (local tools) |
| **Azure Backup** | Yes | No (local backup) |
| **AKS on Azure Local** | Yes | No |
| **Updates** | Azure Update Management | Manual (offline) |
| **Licensing** | Online activation | Offline activation |
| **Billing** | Azure subscription | Separate licensing |
| **Support** | Azure support portal | Phone/email support |
| **Ideal For** | Hybrid scenarios | Air-gapped/maximum sovereignty |

---

## Hardware and Infrastructure Requirements

### Validated Hardware Partners

Azure Local runs on **validated hardware** from Microsoft partner OEMs, ensuring compatibility, support, and performance:

**Premier Integrated System Partners:**

- **Dell Technologies** - PowerEdge servers with Azure Local
- **HPE (Hewlett Packard Enterprise)** - ProLiant servers with Azure Local
- **Lenovo** - ThinkSystem servers with Azure Local
- **DataON** - Integrated systems optimized for Azure Local

**Benefits of Validated Hardware:**

- ✅ Pre-tested configurations
- ✅ Joint support from Microsoft and OEM
- ✅ Warranty and maintenance from OEM
- ✅ Reference architectures and deployment guides
- ✅ Consistent performance and reliability

**[Official Azure Local Catalog](https://azurestackhcisolutions.azure.microsoft.com/)**

---

### Cluster Architecture

**Minimum Configuration:**

- **2 nodes** for basic HA (minimum, not recommended for production)
- **4 nodes** recommended for production (provides better resilience)
- **Up to 16 nodes** per cluster (maximum scale)

**Per-Node Requirements:**

**Compute:**

- **CPU:** 64-bit Intel Nehalem or AMD EPYC (or later) with virtualization support
- **Cores:** Minimum 8 physical cores per node (16+ recommended)
- **Memory:** Minimum 96 GB per node (256 GB+ recommended for production)

**Storage:**

- **Minimum:** 4 drives per node (2 for cache, 2 for capacity)
- **Recommended:** 6+ drives per node for better performance
- **Drive Types:**
  - NVMe or SSD for cache tier
  - SSD or HDD for capacity tier
- **Total Capacity:** Minimum 4 TB raw capacity per node

**Network:**

- **Minimum:** 2x 10 Gbps network adapters per node
- **Recommended:** 2x 25 Gbps for production
- **Optional:** RDMA (RoCE or iWARP) for storage performance
- **Dedicated networks:**
  - Management network
  - Compute network
  - Storage network

**Example Production Node:**

```text
Dell PowerEdge R750
- CPU: 2x Intel Xeon Gold 6338 (32 cores each, 64 total)
- Memory: 512 GB DDR4
- Storage:
  - 2x 1.6 TB NVMe SSD (cache)
  - 8x 3.84 TB SATA SSD (capacity)
- Network: 2x 25 Gbps Ethernet + 2x 10 Gbps RDMA
- Cost: ~$25,000-$35,000 per node
```

---

### Storage Architecture: Storage Spaces Direct

**Storage Spaces Direct (S2D)** is the software-defined storage technology in Azure Local that pools local drives across cluster nodes.

**Key Capabilities:**

- **Storage pooling:** Aggregates drives across all nodes
- **Resilience:** Two-way mirror, three-way mirror, or erasure coding
- **Performance:** SSD caching with automatic data tiering
- **Scalability:** Add capacity by adding nodes

**Storage Resiliency Options:**

| Resiliency Type | Nodes Required | Failure Tolerance | Capacity Efficiency | Use Case |
|----------------|----------------|-------------------|---------------------|----------|
| **Two-Way Mirror** | 2 nodes | 1 node or drive | 50% | Cost-effective HA |
| **Three-Way Mirror** | 3 nodes | 2 nodes or drives | 33% | Production workloads |
| **Mirror-Accelerated Parity** | 4 nodes | 2 nodes or drives | 50-67% | Archive/backup data |
| **Nested Resiliency** | 4 nodes | 2 nodes or drives | 25-50% | Single-site resilience |

{: .note }
> **📝 Note:** Stretch clusters (cross-site synchronous replication) are not supported in Azure Local. For multi-site deployments, use Azure Site Recovery or Storage Replica between separate clusters.

**[Learn More: Storage Spaces Direct](https://learn.microsoft.com/en-us/azure-stack/hci/concepts/storage-spaces-direct-overview)**

---

### Network Architecture: Software-Defined Networking

**Software-Defined Networking (SDN)** provides network virtualization and management capabilities:

**Core SDN Components:**

**Network Controller:**

- Centralized management plane
- REST API for automation
- Policy enforcement
- Network monitoring

**Software Load Balancer (SLB):**

- Layer 4 load balancing
- Distributed across cluster
- NAT and VIP management

**RAS Gateway:**

- Site-to-site VPN
- Point-to-site VPN
- Network Address Translation (NAT)

**Features:**

- ✅ Virtual networks (VNets) like Azure
- ✅ Network Security Groups (NSGs)
- ✅ Software load balancing
- ✅ Multi-tenancy support
- ✅ Hybrid connectivity (VPN, Express Route)

**When to Deploy SDN:**

- Multi-tenant scenarios
- Advanced networking (load balancing, NAT)
- Hybrid connectivity to Azure
- Network policy enforcement

**[Learn More: SDN overview](https://learn.microsoft.com/en-us/azure-stack/hci/concepts/software-defined-networking)**

---

## Use Cases and Customer Scenarios

### Scenario 1: Defense Contractor - Classified Workloads

**Organization:** Aerospace defense contractor handling Top Secret / SCI information

**Requirements:**

- NISP (National Industrial Security Program) compliance
- Air-gapped environment (no internet)
- SCIF (Sensitive Compartmented Information Facility) deployment
- US persons only access
- Offline operations for classified design work

**Solution: Azure Local Disconnected Mode**

**Implementation:**

- Deploy 4-node Azure Local cluster in SCIF
- No external network connectivity (air-gapped)
- Local Active Directory for identity
- Windows Admin Center on management workstation (in SCIF)
- Deploy VMs for classified CAD/CAM workloads
- Local SQL Server for design databases
- Azure DevOps Server (on-premises version) for source control

**Update Process:**

- Microsoft releases updates on removable media (encrypted USB)
- Security officer retrieves media from classified mail room
- Updates applied manually via Windows Admin Center
- Testing in dev environment before production

**Outcomes:**

- ✅ Achieved NISP compliance for Top Secret workloads
- ✅ Enabled digital engineering in classified environment
- ✅ Reduced hardware footprint by 60% (vs. traditional infrastructure)
- ✅ Maintained complete operational independence
- ✅ Zero external connectivity (air-gap maintained)

**Sales Talking Point:**
"Azure Local Disconnected Mode is the only solution that brings modern cloud-like capabilities to completely air-gapped environments. Defense contractors can modernize classified workloads without compromising security or sovereignty."

---

### Scenario 2: Maritime Operations - Cruise Ship Fleet

**Organization:** Cruise line operating 15 ships worldwide with onboard IT services

**Requirements:**

- IT services for crew and passengers (Wi-Fi, entertainment, reservations)
- Unreliable satellite connectivity
- Must operate when no connectivity available
- Central management from shore-based HQ
- Predictive maintenance for ship systems

**Solution: Azure Local Connected Mode (with intermittent connectivity)**

**Implementation:**

- Deploy 2-node Azure Local cluster on each ship
- Azure Arc management (syncs when connectivity available)
- Local VMs for reservations, point-of-sale, crew services
- Azure IoT Edge for ship system monitoring (engines, HVAC, etc.)
- Local caching of entertainment content
- Azure Stack Edge for AI inference (crew face recognition, predictive maintenance)

**Operations:**

- When in port or near shore: Full Azure connectivity, sync updates, upload telemetry
- When at sea: Operates independently with local services
- Shore-based IT can view fleet status and deploy updates when ships connect

**Outcomes:**

- ✅ 99.9% uptime for passenger services (even at sea)
- ✅ Reduced operational costs with predictive maintenance (25% reduction in unscheduled repairs)
- ✅ Centralized management across 15-ship fleet
- ✅ Modern services for passengers and crew
- ✅ Operates seamlessly with intermittent connectivity

**Sales Talking Point:**
"Azure Local is ideal for edge locations with intermittent connectivity. When connected, you get full Azure capabilities. When disconnected, services continue running locally with no interruption."

---

### Scenario 3: Healthcare - Rural Hospital Network

**Organization:** Regional healthcare system with 1 main hospital and 5 rural clinics

**Requirements:**

- HIPAA compliance for patient health records
- Electronic Health Records (EHR) access with <50ms latency
- Medical imaging (PACS) with instant load times
- Local resilience (can't depend on internet for critical care)
- Integration with central Azure for analytics and AI

**Solution: Azure Local at each location (Connected Mode)**

**Implementation:**

- Deploy 2-node Azure Local at main hospital
- Deploy 2-node Azure Local at each rural clinic (5 clusters total)
- Each cluster hosts:
  - Local VMs for EHR application servers
  - Local storage for medical imaging (PACS)
  - Azure Virtual Desktop for clinicians
- Azure Arc connects all clusters to central Azure
- Azure Backup for disaster recovery to Azure
- Power BI for population health analytics (in Azure)

**Hybrid Architecture:**

- **Local (Azure Local):** EHR, PACS, patient scheduling, lab systems
- **Azure (Cloud):** Data warehouse, analytics, AI/ML, disaster recovery

**Benefits:**

- ✅ <10ms latency for medical imaging (vs. 100ms+ from cloud)
- ✅ Local resilience if internet fails (critical for patient care)
- ✅ HIPAA compliance with data residency control
- ✅ Centralized IT management across 6 locations
- ✅ Azure AI for diagnostic support and predictive analytics

**Outcomes:**

- ✅ Radiologists report 50% faster image review
- ✅ Zero EHR downtime even during internet outages
- ✅ Reduced IT costs by 30% (vs. separate infrastructure per location)
- ✅ Enabled telemedicine across rural clinics

**Sales Talking Point:**
"For healthcare, latency and reliability are critical. Azure Local provides local performance and resilience while maintaining compliance. It's the best of both worlds - edge performance with cloud intelligence."

---

### Scenario 4: Manufacturing - Smart Factory

**Organization:** Automotive parts manufacturer with factory floor automation

**Requirements:**

- Real-time control of manufacturing equipment (CNC, robotics)
- <10ms latency for operational technology (OT)
- Air-gap between OT and IT networks (Purdue Model)
- Edge analytics for quality control and predictive maintenance
- Integration with corporate ERP in Azure

**Solution: Azure Local Disconnected Mode for OT + Azure for IT**

**Implementation:**

- **OT Network (Air-Gapped):**
  - Deploy Azure Local Disconnected Mode on factory floor
  - Host SCADA, MES (Manufacturing Execution System), historian
  - Deploy Azure IoT Edge for edge analytics
  - ML models for quality inspection (defect detection)
  - Predictive maintenance models for equipment

- **IT Network (Connected to Azure):**
  - Corporate network with Azure ExpressRoute
  - ERP system (SAP) in Azure
  - Data warehouse and Power BI for reporting

- **Data Flow:**
  - One-way data diode from OT to IT (security)
  - Aggregate, anonymized data flows to IT/Azure
  - No control signals from IT to OT (security)

**Outcomes:**

- ✅ Achieved <5ms latency for manufacturing control
- ✅ Maintained OT/IT separation (IEC 62443 compliance)
- ✅ Detected defects in real-time with AI (reducing scrap by 15%)
- ✅ Predictive maintenance reduced downtime by 20%
- ✅ ERP integration for supply chain visibility

**Sales Talking Point:**
"Azure Local enables Industry 4.0 transformation while maintaining OT security. Air-gapped OT networks get AI and analytics capabilities without internet connectivity, meeting both innovation and security needs."

---

## Migration and Deployment Strategies

### Migration from On-Premises to Azure Local

**Assessment Phase:**

**Step 1: Inventory Current Infrastructure**

- Document all VMs, applications, and workloads
- Identify dependencies between workloads
- Measure current resource utilization (CPU, memory, storage, IOPS)
- Assess network connectivity requirements

**Step 2: Compatibility Assessment**

- Verify OS compatibility (Windows Server 2012 R2+, various Linux distros)
- Check application dependencies
- Identify any hardware dependencies (USB devices, special cards)
- Assess backup and DR requirements

**Step 3: Sizing Azure Local Cluster**

- Calculate required compute (vCPUs, memory)
- Calculate storage capacity and performance (IOPS, throughput)
- Add 20-30% buffer for growth
- Determine node count (4 nodes recommended for production)

**Tool:** [Azure Migrate](https://learn.microsoft.com/en-us/azure/migrate/how-to-create-azure-vmware-solution-assessment) (works for Azure Local sizing)

---

### Deployment Process

**Phase 1: Hardware Procurement (4-6 weeks)**

1. Select Azure Local Integrated System partner (Dell, HPE, Lenovo)
2. Size configuration based on assessment
3. Order hardware
4. Plan data center space, power, cooling, networking

**Phase 2: Infrastructure Deployment (1-2 weeks)**

1. Rack and cable hardware
2. Configure out-of-band management (iDRAC, iLO, etc.)
3. Deploy cluster using Azure Local deployment tool
4. Validate cluster health and storage
5. Configure networking (VLANs, VNets, NSGs if using SDN)

**Phase 3: Workload Migration (4-12 weeks)**

1. Create management VMs (domain controllers, DNS, etc.)
2. Migrate non-production workloads (dev/test)
3. Test and validate
4. Migrate production workloads in phases
5. Cutover and decommission old infrastructure

**Deployment Options:**

**Option A: Integrated System (Recommended)**

- Purchase pre-configured hardware from OEM
- Hardware delivered ready to deploy
- Faster time to production (1-2 weeks vs. 4-6 weeks)
- Joint support from Microsoft and OEM

**Option B: Validated Nodes**

- Build cluster from catalog-validated components
- More flexibility in configuration
- Longer deployment time
- Requires more in-house expertise

---

### Best Practices for Deployment

✅ **Start with Connected Mode**

- Easier to deploy and manage
- Get familiar with Azure Local capabilities
- Transition to Disconnected later if needed

✅ **Deploy Non-Production First**

- Test cluster performance and operations
- Train IT staff on new tools
- Validate backup and DR procedures

✅ **Plan for Growth**

- Size for 3-5 year capacity
- Leave room for additional nodes
- Plan network bandwidth for scale

✅ **Implement Monitoring from Day 1**

- Deploy monitoring before production workloads
- Set up alerting for capacity, performance, health
- Establish baseline metrics

✅ **Document Everything**

- Network diagrams and IP addressing
- Cluster configuration and settings
- Operational runbooks
- Contact information for support

---

## Licensing and Cost Considerations

### Licensing Model

**Azure Local Licensing:**

- **Per-core subscription** ($10 per physical core per month typical, varies by program)
- Includes rights to run unlimited Windows Server and Hyper-V VMs
- Includes Azure Arc management (if Connected mode)

**Windows Server Licensing (Guest VMs):**

- Covered by Azure Local subscription (no additional cost)
- Unlimited Windows Server VMs on cluster

**SQL Server Licensing:**

- Separate licensing required
- Options: Per-core, Server+CAL, or Azure Hybrid Benefit
- Consider Azure Arc-enabled SQL Managed Instance (included in Azure Local)

**Other Software:**

- Linux VMs: No Microsoft licensing cost
- Third-party software: Follow vendor licensing terms

---

### Total Cost of Ownership (TCO)

**Capital Expenditure (CapEx):**

- Hardware: $25,000-$35,000 per node (typical)
- 4-node cluster: $100,000-$140,000
- Networking: $20,000-$50,000 (switches, cables)
- Rack, power, cooling: $10,000-$30,000
- **Total CapEx:** $130,000-$220,000

**Operational Expenditure (OpEx) - Annual:**

- Azure Local subscription: ~$15,000-$25,000/year (for 4-node cluster)
- Hardware support/maintenance: ~$20,000-$30,000/year (20% of hardware cost)
- Power and cooling: ~$5,000-$10,000/year
- IT staff time: Variable (estimate 0.5-1 FTE)
- **Total OpEx:** $40,000-$65,000/year

**5-Year TCO:** $330,000-$545,000

**TCO Comparison (4-Node Cluster):**

| Infrastructure Type | 5-Year TCO | Notes |
|---------------------|------------|-------|
| **Traditional On-Premises** | $500,000-$700,000 | Separate compute, storage, networking |
| **Azure Local** | $330,000-$545,000 | Hyperconverged, included software |
| **Azure Public Cloud** | $400,000-$800,000 | Depends heavily on utilization |

**When Azure Local Makes Financial Sense:**

- ✅ Steady-state workloads (vs. bursty workloads favor cloud)
- ✅ Data gravity (large datasets, high I/O)
- ✅ Latency requirements (can't tolerate cloud latency)
- ✅ Compliance/sovereignty (must be on-premises)
- ✅ 3-5 year commitment (CapEx investment)

---

## Microsoft 365 Local: Productivity in Sovereign Environments

{: .note }
> **📝 Source:** [What is Microsoft 365 Local?](https://learn.microsoft.com/en-us/azure/azure-local/concepts/microsoft-365-local-overview) — Microsoft Learn (November 2025)

### What is Microsoft 365 Local?

**Microsoft 365 Local** enables organizations to run **Exchange Server**, **SharePoint Server**, and **Skype for Business Server** on Azure Local infrastructure that is entirely customer-owned and managed. It provides enhanced control over data residency, access, and compliance to meet sovereignty requirements.

Designed for organizations needing productivity tools in a private cloud environment, Microsoft 365 Local leverages **Azure Arc** to provide a unified control plane with simplified deployment and streamlined updates. The solution includes a validated reference architecture with certified hardware, along with a hardened security baseline and robust controls.

**Private Sovereign Cloud is designed for:**

- **Governments** requiring the highest standards of data residency and operational autonomy
- **Critical industries** such as defense contractors and intelligence agencies  
- **Regulated sectors** with strict compliance and sovereignty requirements
- **Disconnected environments** needing productivity services without cloud connectivity

### Key Benefits of Microsoft 365 Local

**1. Complete Sovereignty**

- Physical control over all productivity data (email, documents, collaboration)
- Data never leaves your datacenter
- No external dependencies for core productivity functions
- Meets stringent government and regulatory requirements

**2. Simplified Deployment**

- Validated reference architecture on Azure Local platform
- Unified deployment and management framework
- Reduced complexity vs. traditional separate server deployments
- Hyperconverged infrastructure benefits (reduced hardware footprint)

**3. Full Control**

- Customer controls all security, compliance, and governance policies
- Local administrator access and management
- Complete audit trail of all activities
- Integration with customer identity systems (Active Directory)

**4. Disconnected Operations Support**

- Works in both Connected and Disconnected Azure Local modes
- Enables productivity services in air-gapped networks
- Periodic synchronization when connectivity available (Connected mode)
- Complete autonomy when required (Disconnected mode)

### Supported Workloads

**Available with Microsoft 365 Local:**

- **Exchange Server** — Enterprise email, calendaring, contacts, and unified communications
- **SharePoint Server** — Document management, collaboration, intranet sites, and enterprise search  
- **Skype for Business Server** — Unified communications, presence, and instant messaging

**Key Capabilities:**

- Certified and validated solutions by Microsoft and hardware partners
- Full-stack deployment based on validated reference architecture
- Supports hybrid connectivity and fully disconnected operations
- Arc-enabled management for hybrid control

### Example Deployment Scenario

**Federal Agency Classified Email and Collaboration**

**Requirements:**

- Provide email and collaboration services on classified networks (SIPRNET, JWICS)
- Complete air-gap (no internet connectivity allowed)
- Support 10,000+ government employees across multiple facilities
- NIST 800-53 High compliance for classified information
- Zero cloud dependencies

**Solution:**

- Deploy Azure Local in Disconnected Mode at each classified facility
- Install Microsoft 365 Local (Exchange Server + SharePoint Server)
- Local Active Directory for identity management
- Local certificate authority for encryption and signing
- Windows Admin Center for management

**Outcomes:**

- ✅ Full email and collaboration in air-gapped environment
- ✅ 100% data sovereignty (no data leaves facility)
- ✅ Meets all classification and compliance requirements
- ✅ Reduced infrastructure footprint by 50% vs. traditional deployment
- ✅ Unified management across multiple locations
- ✅ Modern productivity tools without cloud dependency

### Discovery Questions for Microsoft 365 Local

**Sovereignty and Compliance:**

1. Do you need email and collaboration services in air-gapped or classified environments?
2. What are your data residency requirements for productivity data?
3. Do you have compliance mandates preventing productivity data in public cloud?
4. Are you required to maintain complete operational control over communication systems?

**Current State:**
5. Are you currently running Exchange Server or SharePoint Server on separate physical infrastructure?
6. What version of Exchange/SharePoint are you running today?
7. How many mailboxes and SharePoint users do you support?
8. What challenges do you face with your current productivity infrastructure?

**Requirements:**
9. Do you need to operate productivity services without continuous internet connectivity?
10. What high availability and disaster recovery requirements do you have?
11. How do you handle updates and patching in disconnected environments?
12. What integration requirements do you have with other systems?

**Reference:** [Microsoft 365 Local Documentation](https://learn.microsoft.com/en-us/microsoft-365/local/)

---

## Sales Talking Points

### Value Propositions

**1. "Azure Anywhere - Even Air-Gapped"**

- Only solution that brings Azure services to completely disconnected environments
- Maintain operational independence while getting cloud-like capabilities
- Future-proof: Easy transition from disconnected to connected as requirements change
- **Differentiator:** AWS Outposts requires persistent connectivity

**2. "Modernize Without Migrating"**

- Modernize on-premises infrastructure without cloud migration
- Azure-consistent management and operations
- Hybrid ready when you are (start disconnected, connect later)
- **ROI:** 40-60% cost reduction vs. traditional on-premises infrastructure

**3. "Edge Performance with Cloud Management"**

- <10ms latency for latency-sensitive workloads
- Local data processing for real-time applications
- Cloud management for centralized control (Connected mode)
- **Use Cases:** Healthcare imaging, manufacturing OT, VDI, SQL databases

**4. "Validated Hardware, Joint Support"**

- Pre-tested configurations from Dell, HPE, Lenovo
- Joint support from Microsoft and OEM
- Warranty and maintenance from trusted vendors
- **Reduced Risk:** No "finger-pointing" between vendors

---

### Discovery Questions

**Sovereignty and Compliance:**

1. "Do you have workloads that cannot be in public cloud due to sovereignty requirements?"
2. "Are there scenarios where you need to operate without internet connectivity?"
3. "Do you have air-gap requirements for any systems?"
4. "What compliance frameworks require on-premises deployment?"

**Performance and Latency:**
5. "Which applications are most latency-sensitive?"
6. "What latency do you currently experience, and what is acceptable?"
7. "Do you have large datasets that are expensive to move to cloud?"
8. "Are there bandwidth constraints to/from cloud?"

**Current Infrastructure:**
9. "What is the age of your current on-premises infrastructure?"
10. "When is your next refresh cycle planned?"
11. "Are you using hyperconverged infrastructure (HCI) today?"
12. "How many data centers or edge locations do you have?"

**Cloud Strategy:**
13. "What is your hybrid cloud strategy?"
14. "Are some workloads in Azure already?"
15. "Do you want centralized management across cloud and edge?"
16. "What prevents you from moving all workloads to cloud?"

---

## Competitive Differentiation

### vs. AWS Outposts

**Microsoft Advantages:**

1. **Disconnected Operations:**
   - ✅ Microsoft: Azure Local Disconnected Mode for air-gapped environments
   - ❌ AWS: Outposts requires persistent connectivity to AWS
   - **Impact:** Defense, maritime, and high-sovereignty scenarios not possible with AWS

2. **Flexible Connectivity:**
   - ✅ Microsoft: Connected or Disconnected mode
   - ⚠️ AWS: Always-connected only
   - **Impact:** Can't operate independently with AWS

3. **Smaller Footprint:**
   - ✅ Microsoft: Minimum 2 nodes, flexible sizing
   - ⚠️ AWS: Large footprint (42U rack minimum)
   - **Impact:** Fits in more locations (offices, stores, ships)

4. **Integrated Hardware Options:**
   - ✅ Microsoft: Multiple OEM partners (Dell, HPE, Lenovo, DataON)
   - ⚠️ AWS: Single vendor (AWS-branded)
   - **Impact:** More vendor choice, competitive pricing

---

### vs. Traditional VMware

**Microsoft Advantages:**

1. **Licensing Simplicity:**
   - ✅ Microsoft: Simple per-core subscription
   - ⚠️ VMware: Complex per-CPU, feature-based licensing
   - **Impact:** More predictable costs, easier budgeting

2. **Cloud Integration:**
   - ✅ Microsoft: Native Azure integration via Arc
   - ⚠️ VMware: Third-party integration required
   - **Impact:** Seamless hybrid cloud experience

3. **Software-Defined Storage:**
   - ✅ Microsoft: Included (Storage Spaces Direct)
   - ⚠️ VMware: Separate product (vSAN, additional cost)
   - **Impact:** Lower total cost

4. **Modern Management:**
   - ✅ Microsoft: Azure portal, PowerShell, ARM templates
   - ⚠️ VMware: vCenter (separate management)
   - **Impact:** Unified management experience

---

## Common Challenges and Solutions

### Challenge 1: Complexity Perception

**Concern:** "This sounds complicated. Is it harder to manage than traditional infrastructure?"

**Solution:**

- Azure Local uses familiar tools (Hyper-V, PowerShell, Windows Admin Center)
- Pre-built validated hardware reduces deployment complexity
- Microsoft FastTrack available for deployment assistance
- Training available via Microsoft Learn (free)
- **Reality:** Easier than managing separate compute, storage, networking

---

### Challenge 2: Update Management in Disconnected Mode

**Concern:** "How do we keep systems updated without internet access?"

**Solution:**

- Microsoft releases quarterly updates on encrypted removable media
- Updates delivered via classified channels (for defense customers)
- Test updates in non-production cluster first
- Windows Admin Center automates update orchestration across cluster
- **Process:** Similar to existing classified update processes

---

### Challenge 3: Skill Requirements

**Concern:** "Do we need new skills, or can our current team manage this?"

**Solution:**

- Builds on existing Windows Server and Hyper-V skills
- No need to learn new hypervisor (if coming from Hyper-V)
- Windows Admin Center provides GUI for common tasks
- Training paths available on Microsoft Learn
- **Timeline:** 2-4 weeks to train existing Windows admins

---

### Challenge 4: Support for Disconnected Mode

**Concern:** "How do we get support if we can't connect to internet or call Microsoft?"

**Solution:**

- Phone support with classified support line
- Email support via secure channels (SIPRNET for DoD)
- Joint support from Microsoft and OEM hardware vendor
- Remote support via SATCOM or disconnected VPN (for maritime)
- **Escalation:** Microsoft dedicated support team for disconnected scenarios

---

## Next Steps and Learning Resources

### Continue Learning

- **[← Back to Sovereign Cloud Models Overview](sovereign-cloud-models)**
- **[→ Next: National Partner Clouds](national-partner-clouds)**
- **[Explore: Operational Sovereignty Concepts](operational-sovereignty)**

### Hands-On Learning

1. **[Azure Local deployment quickstart](https://learn.microsoft.com/en-us/azure-stack/hci/deploy/deployment-quickstart)**
2. **[Azure Local on-premises deployment](https://learn.microsoft.com/en-us/azure-stack/hci/deploy/deployment-introduction)**
3. **[Windows Admin Center guide](https://learn.microsoft.com/en-us/windows-server/manage/windows-admin-center/overview)**

### Additional Resources

- **[Azure Local overview](https://learn.microsoft.com/en-us/azure/azure-local/overview)** - Official product documentation
- **[Azure Local pricing](https://azure.microsoft.com/en-us/pricing/details/azure-stack/hci/)** - Pricing calculator
- **[Azure Local catalog](https://azurestackhcisolutions.azure.microsoft.com/)** - Validated hardware
- **[Azure Arc documentation](https://learn.microsoft.com/en-us/azure/azure-arc/)** - Hybrid management

---

**Last Updated:** October 2025
