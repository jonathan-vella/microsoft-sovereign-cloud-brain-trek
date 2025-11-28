---
layout: default
title: Azure Local Hardware Requirements
parent: Module 3 - Azure Local Overview
nav_order: 3.4
---

# Azure Local Hardware Requirements & Planning

{: .no_toc }

## Table of Contents

{: .no_toc .text-delta }

1. TOC
{:toc}

---

{: .note }
> ⏱️ **Reading Time:** 15-20 min | 🎯 **Key Topics:** Validated hardware, sizing, vendor selection | 📋 **Prerequisites:** [Azure Local Overview](azure-local-overview.md)

---

## Overview

Selecting the right hardware is critical for Azure Local success. This page provides comprehensive guidance on hardware requirements, validated partners, sizing strategies, and deployment planning.

**Key Topics:**

- Hardware specifications and requirements
- Validated hardware partners and systems
- Sizing guidance based on workload types
- Network adapter and storage requirements
- Deployment planning checklist

**[← Back to Azure Local Overview](azure-local-overview)**

---

## Hardware Requirements Overview

### Minimum vs. Recommended Specifications

**Minimum Configuration (Testing/POC Only):**

- 1 physical server
- 8-core CPU
- 128 GB RAM
- 4 drives minimum
- 2x 10 GbE NICs
- **Not recommended for production**

**Production Recommended:**

- 2-4 physical servers (for HA)
- 16+ core CPU per server
- 384+ GB RAM per server
- 8+ drives per server (mix of NVMe, SSD, HDD)
- 2x 25 GbE or faster NICs (RDMA-capable)
- Validated hardware from Microsoft partners

### Server Form Factor

**Rack-Mount Servers (Most Common):**

- 1U or 2U form factor
- Standard 19-inch racks
- Hot-swap components
- Redundant power supplies
- Remote management (iDRAC, iLO, etc.)

**Blade Servers:**

- Higher density
- Shared infrastructure (power, cooling)
- More complex networking
- Limited expandability

**Tower Servers:**

- Suitable for branch offices
- Lower cost entry point
- Limited scalability
- Not recommended for multi-node clusters

---

## Physical Topology and Network Architecture

### Cluster Hardware Topology


---

## Approved Hardware Partners and Systems

Microsoft maintains a catalog of validated Azure Local solutions from OEM and system builder partners.

### Tier 1 OEM Partners

**Dell Technologies:**

- **Product Line:** PowerEdge R650, R750
- **Configuration:** 2U, 2-socket, Intel or AMD
- **Strengths:** Comprehensive support, global availability
- **URL:** [Dell Azure Local Solutions](https://www.dell.com/azure-stack)

**Hewlett Packard Enterprise (HPE):**

- **Product Line:** ProLiant DL380, DL385
- **Configuration:** 2U, 2-socket, Intel or AMD
- **Strengths:** iLO management, InfoSight integration
- **URL:** [HPE Azure Local Solutions](https://www.hpe.com/azure-stack)

**Lenovo:**

- **Product Line:** ThinkSystem SR650, SR850
- **Configuration:** 2U, 2-socket, scalable to 4-socket
- **Strengths:** Competitive pricing, XClarity management
- **URL:** [Lenovo Azure Local Solutions](https://www.lenovo.com/azure-stack)

**Fujitsu:**

- **Product Line:** PRIMERGY RX2530, RX2540
- **Configuration:** 2U, 2-socket, Intel Xeon
- **Strengths:** European manufacturing, strong EMEA presence
- **URL:** [Fujitsu Azure Local Solutions](https://www.fujitsu.com/azure-stack)

### Tier 2 System Builders

**Supermicro:**

- Custom-built solutions
- Wide range of configurations
- Cost-effective options
- Strong for specialized workloads (GPU, high-density)

**DataON:**

- Azure Local-optimized systems
- Pre-configured solutions
- Direct support relationship with Microsoft
- Focus on storage performance

**QCT (Quanta Cloud Technology):**

- ODM solutions
- Competitive pricing
- Hyperscale heritage
- Strong in Asia-Pacific

**Wortmann AG:**

- European system integrator
- TERRA servers
- Strong DACH region presence
- Local support

### Benefits of Validated Hardware

**Pre-Tested and Certified:**

- Microsoft-validated configurations
- Guaranteed compatibility
- Firmware and driver validation
- Performance benchmarking

**Simplified Support:**

- Single point of contact
- Coordinated troubleshooting
- Faster resolution times
- Clear escalation paths

**Optimized Performance:**

- Tuned for Azure Local workloads
- RDMA configuration validated
- Storage performance validated
- Power efficiency optimized

**Reference:** [Azure Local Solutions Catalog](https://azurestackhcisolutions.azure.microsoft.com/)

---

## CPU, Memory, and Storage Specifications

### Processor Requirements

**Supported Processors:**

- **Intel:** Xeon Scalable (Skylake or newer)
- **AMD:** EPYC 7002 series or newer
- 64-bit x86 architecture only

**Required Features:**

- **Virtualization Extensions:** Intel VT-x or AMD-V
- **Second Level Address Translation (SLAT):** Intel EPT or AMD RVI
- **Hardware-Assisted Virtualization:** Mandatory
- **Intel VT-d / AMD-Vi:** For device passthrough

**Core Count Recommendations:**

**Small Deployments (< 50 VMs):**

- Minimum: 8 cores per CPU, 16 cores per node
- Recommended: 12-16 cores per CPU, 24-32 cores per node

**Medium Deployments (50-200 VMs):**

- Recommended: 16-24 cores per CPU, 32-48 cores per node

**Large Deployments (200+ VMs):**

- Recommended: 24-32 cores per CPU, 48-64 cores per node

**Special Workloads:**

- **VDI:** 32+ cores per node
- **AI/ML:** High core count + GPUs
- **HPC:** Maximum cores (64+)

### Memory Requirements

**Minimum:** 128 GB DDR4 ECC  
**Recommended Production:** 384 GB - 1 TB  
**Large Deployments:** 1 TB - 6 TB

**Memory Sizing Formula:**

```text
Total Memory = (Base OS + Storage Spaces Direct + VMs + Overhead)

Where:
- Base OS: 8-16 GB per node
- Storage Spaces Direct: 2-4 GB per TB of cache + 1 GB per TB of capacity
- VMs: Sum of VM memory allocations
- Overhead: 20% buffer for spikes
```

**Example Calculation (4-node cluster):**

- Base OS: 12 GB × 4 = 48 GB
- S2D (10 TB cache, 100 TB capacity): 40 GB + 100 GB = 140 GB
- VMs: 200 VMs × 8 GB average = 1,600 GB
- Overhead: 20% = 320 GB
- **Total: 2,108 GB (divide by 4 nodes = 528 GB per node)**

**Memory Type:**

- **DDR4 or DDR5:** ECC (Error-Correcting Code) required
- **Speed:** 2666 MHz or faster recommended
- **Configuration:** Populate all memory channels for maximum bandwidth
- **NUMA:** Be aware of NUMA node boundaries for VM placement

### Storage Requirements

**Drive Types:**

**OS Drives (Required):**

- 2x 240 GB+ SATA SSD (mirrored)
- Used for host OS and boot
- Separate from Storage Spaces Direct pool
- M.2 or SATA form factor

**Cache Tier (Recommended):**

- NVMe SSD for optimal performance
- 2-8x drives per node
- 800 GB - 3.2 TB per drive
- PCIe 3.0 x4 or better
- Enterprise-grade (high endurance)

**Capacity Tier:**

- SSD or HDD based on performance needs
- 4-16x drives per node
- 1-16 TB per drive
- SATA or SAS interface

**Minimum Drive Configuration:**

- 4 drives per node (minimum)
- All nodes must have same drive configuration
- Mix of drive types (NVMe + SSD or NVMe + HDD)

**Recommended Drive Configuration:**

**Performance-Optimized:**

- 2-4x NVMe SSD (cache): 1.6-3.2 TB each
- 6-10x SATA SSD (capacity): 4-8 TB each
- **Use Case:** Databases, VDI, latency-sensitive apps

**Balanced:**

- 2x NVMe SSD (cache): 1.6 TB each
- 4-6x SATA SSD (capacity): 4 TB each
- 4-6x SATA HDD (capacity): 8-12 TB each
- **Use Case:** General virtualization

**Capacity-Optimized:**

- 2x NVMe SSD (cache): 800 GB each
- 10-12x SATA HDD (capacity): 12-16 TB each
- **Use Case:** File servers, archives, backup

**Storage Sizing Formula:**

```text
Usable Capacity = (Total Raw Capacity × Efficiency Factor × Resiliency Factor)

Efficiency Factors:
- Deduplication/Compression: 1.5-3x (varies by data type)
- Without dedupe: 1x

Resiliency Factors:
- Two-way mirror: 0.5 (50% efficiency)
- Three-way mirror: 0.33 (33% efficiency)
- Parity (erasure coding): 0.5-0.8 (depends on configuration)
```

**Example:**

- 4 nodes × 10x 4TB SSD = 160 TB raw
- Two-way mirror: 160 TB × 0.5 = 80 TB usable
- Three-way mirror: 160 TB × 0.33 = 53 TB usable

---

## Network Adapter Requirements

### Minimum Requirements

**Adapter Count:** 2 adapters (for redundancy)  
**Speed:** 10 GbE minimum  
**Features:** SR-IOV, RDMA (for storage traffic)

### Recommended Configuration

**Management/Compute:**

- 2x 10 GbE or 25 GbE adapters
- Bonded/teamed for redundancy
- Standard Ethernet (no special requirements)

**Storage:**

- 2x 25 GbE or faster (40/50/100 GbE)
- RDMA-capable (iWARP, RoCE v2, or InfiniBand)
- Dedicated for Storage Spaces Direct traffic
- DCB-capable (for RoCE)

### RDMA Technologies

**iWARP (Internet Wide Area RDMA Protocol):**

- Works over standard Ethernet
- Easier to configure (no DCB required)
- Slightly higher CPU usage
- **Recommendation:** Good choice for most deployments

**RoCE v2 (RDMA over Converged Ethernet):**

- Higher performance than iWARP
- Lower CPU usage
- Requires DCB (Data Center Bridging)
- More complex network configuration
- **Recommendation:** Best for large, high-performance clusters

**InfiniBand:**

- Highest performance
- Separate network fabric required
- Less common in Azure Local
- Higher cost
- **Recommendation:** Specialized use cases only

### Popular Network Adapters

**Mellanox/NVIDIA:**

- ConnectX-5, ConnectX-6
- 25/40/50/100 GbE
- Excellent RDMA performance
- Strong software support

**Intel:**

- E810-C series
- 25/40/100 GbE
- Good iWARP support
- Broad compatibility

**Broadcom:**

- BCM57xxx series
- 25/50/100 GbE
- Enterprise-grade reliability
- Good OEM support

### Network Configuration Best Practices

**NIC Teaming/Bonding:**

- Use Switch Independent mode
- Dynamic load balancing
- Redundant paths to switches

**Jumbo Frames:**

- Enable for storage network (MTU 9000+)
- Reduces CPU overhead
- Improves throughput

**Quality of Service (QoS):**

- Prioritize storage traffic
- Bandwidth reservation
- Prevent starvation

**VLAN Segmentation:**

- Separate management, storage, compute traffic
- Improves security
- Reduces broadcast domains

---

## Redundancy and High Availability Hardware Setup

### Node Redundancy

**2-Node Clusters:**

- Tolerates 1 node failure
- Requires file share witness (for quorum)
- 50% capacity overhead
- Most cost-effective HA configuration

**3-Node Clusters:**

- Tolerates 1 node failure
- Better performance than 2-node
- 33% capacity overhead
- Good balance of cost and resilience

**4-Node Clusters (Recommended):**

- Tolerates 1 node failure
- 25% capacity overhead
- Better performance distribution
- Most common configuration

**5-16 Node Clusters:**

- Tolerates 1-2 node failures (depends on resiliency)
- Lower overhead percentage
- Higher aggregate capacity
- For large deployments

### Storage Redundancy

**Drive-Level Protection:**

- Hot-spare capability
- Automatic rebuild
- Multiple drive failures tolerated
- RAID not used (Storage Spaces Direct handles this)

**Node-Level Protection:**

- Data replicated across nodes
- Two-way or three-way mirror
- Erasure coding (parity) option
- Configurable per volume

### Network Redundancy

**Adapter-Level:**

- NIC teaming (bonding)
- Active-passive or active-active
- Automatic failover

**Switch-Level:**

- Dual top-of-rack switches
- Each node connected to both switches
- Eliminates single point of failure

**Path-Level:**

- Multiple paths to storage
- Multipath I/O (MPIO)
- Automatic path failover

### Power Redundancy

**Node-Level:**

- Dual power supplies per server
- Each PSU on separate circuit
- Automatic failover on PSU failure

**Facility-Level:**

- Dual power feeds to rack
- UPS for graceful shutdown
- Generator for extended outages
- Power distribution units (PDUs)

### Cooling and Environmental

**Cooling:**

- Hot aisle / cold aisle configuration
- Adequate airflow (front-to-back)
- Temperature monitoring
- Redundant cooling units

**Environmental Monitoring:**

- Temperature and humidity sensors
- Water leak detection
- Smoke detection
- Integration with facility management

---

## Sizing Guidance Based on Workload Types

### General Virtualization

**Typical Profile:**

- Mixed Windows and Linux VMs
- Moderate I/O requirements
- Standard enterprise applications

**Recommended Configuration (per node):**

- CPU: 2x 16-core (32 cores total)
- Memory: 512 GB
- Storage: 2x NVMe (1.6 TB) + 6x SSD (4 TB)
- Network: 2x 25 GbE (RDMA)

**Expected Capacity:**

- 40-60 VMs per node
- 160-240 VMs per 4-node cluster

### VDI (Virtual Desktop Infrastructure)

**Typical Profile:**

- Many small VMs (2-4 GB each)
- Burst I/O patterns
- Graphics requirements (optional)

**Recommended Configuration (per node):**

- CPU: 2x 24-core (48 cores total)
- Memory: 768 GB - 1 TB
- Storage: 4x NVMe (3.2 TB) + 6x SSD (4 TB)
- Network: 2x 25 GbE (RDMA)
- GPU: Optional (NVIDIA T4 or similar)

**Expected Capacity:**

- 100-150 VDI sessions per node
- 400-600 VDI sessions per 4-node cluster

### Database Workloads

**Typical Profile:**

- High IOPS requirements
- Low latency critical
- High memory usage

**Recommended Configuration (per node):**

- CPU: 2x 20-core (40 cores total)
- Memory: 768 GB - 1.5 TB
- Storage: 4-8x NVMe (3.2 TB) - All-flash
- Network: 2x 25 GbE or faster (RDMA)

**Expected Capacity:**

- 10-20 database VMs per node
- 500K+ IOPS per cluster
- Sub-millisecond latency

### AI/ML and GPU Workloads

**Typical Profile:**

- GPU-accelerated compute
- Large memory requirements
- High storage bandwidth

**Recommended Configuration (per node):**

- CPU: 2x 24-core (48 cores total)
- Memory: 1 TB - 2 TB
- Storage: 4x NVMe (3.2 TB) + high-bandwidth network storage
- Network: 2x 25 GbE or faster
- GPU: 2-4x NVIDIA A100 or H100

**Expected Capacity:**

- 5-10 ML training jobs concurrent
- 50-100 inference workloads

### File Server / Storage-Heavy

**Typical Profile:**

- High capacity requirements
- Moderate performance needs
- Deduplication and compression

**Recommended Configuration (per node):**

- CPU: 2x 16-core (32 cores total)
- Memory: 384 GB
- Storage: 2x NVMe (800 GB) + 12x HDD (12-16 TB)
- Network: 2x 25 GbE (RDMA)

**Expected Capacity:**

- 500 TB - 1 PB usable (with parity)
- 3-5 GB/s throughput

### Edge / Branch Office

**Typical Profile:**

- Small footprint (1-2 nodes)
- 10-30 VMs
- Local services (AD, DNS, DHCP, file shares)

**Recommended Configuration (per node):**

- CPU: 1-2x 12-core (12-24 cores total)
- Memory: 256-384 GB
- Storage: 2x NVMe (800 GB) + 4x SSD (2 TB)
- Network: 2x 10 GbE

**Expected Capacity:**

- 15-25 VMs per node
- 30-50 VMs for 2-node cluster

---

## Power and Cooling Requirements

### Power Consumption

**Per Node Estimates:**

**Small Node:**

- Idle: 150-250 watts
- Average: 300-500 watts
- Peak: 600-800 watts

**Medium Node:**

- Idle: 250-350 watts
- Average: 500-800 watts
- Peak: 1000-1200 watts

**Large Node (with GPUs):**

- Idle: 350-500 watts
- Average: 800-1200 watts
- Peak: 1500-2000 watts

**4-Node Cluster (Medium):**

- Idle: 1-1.4 kW
- Average: 2-3.2 kW
- Peak: 4-4.8 kW
- Plus networking gear: +300-500 watts

### Power Requirements

**Electrical:**

- 208V or 240V (most efficient)
- Dedicated circuits recommended
- PDUs with monitoring
- Surge protection

**UPS (Uninterruptible Power Supply):**

- Size for 15-30 minutes runtime
- For 4-node cluster: 5-10 kVA UPS
- Includes networking gear
- Allows graceful shutdown

**Generator (Optional):**

- For extended outages
- Size for sustained load
- Automatic transfer switch (ATS)
- Regular testing required

### Cooling Requirements

**Heat Output:**

- Power consumption = heat output (BTU/hr = Watts × 3.412)
- 4-node cluster average: 2.5 kW = 8,500 BTU/hr
- Plus switch gear and UPS losses

**Cooling Capacity:**

- Size for peak load, not average
- Include overhead (15-20%)
- 4-node cluster: 10,000-12,000 BTU/hr cooling required

**Airflow:**

- Front-to-back or back-to-front (depends on system)
- 250-500 CFM per server
- Hot aisle / cold aisle configuration
- Ensure no recirculation

**Temperature:**

- Maintain 18-27°C (64-80°F)
- Below 32°C (90°F) maximum
- Monitor inlet and outlet temperatures
- Alert on thermal excursions

**Humidity:**

- Maintain 20-80% relative humidity
- 45-55% optimal
- Monitor and alert

---

## Rack and Deployment Considerations

### Rack Requirements

**Standard 42U Rack:**

- 19-inch width (standard)
- 600-800mm depth (depends on server depth)
- 1000mm width (for cable management)
- Cable management arms
- PDU mounting

**Space Requirements:**

- 1-2U per node (typical)
- 1-2U per switch
- 2-4U for UPS (or separate rack)
- 2-4U for patch panels and cable management
- Total: 8-16U for 4-node cluster

### Cable Management

**Best Practices:**

- Use cable management arms
- Label all cables clearly
- Separate power and data cables
- Use color-coding for cable types
- Document cable routing

**Cable Types:**

- Power: C13/C14 or C19/C20
- Management: Cat6 or better
- Storage: DAC (Direct Attach Copper) or fiber
- Compute: DAC or fiber (for 25G+)

### Physical Security

**Rack Security:**

- Lockable rack doors
- Side panels secured
- Serial number tracking
- Tamper-evident seals

**Facility Security:**

- Badge access
- Video surveillance
- Visitor logs
- Environmental monitoring

---

## Upgrade Paths and Future-Proofing

### Upgrade Strategies

**Vertical Scaling (Scale-Up):**

- Add memory to existing nodes
- Upgrade CPUs (same generation)
- Add drives to storage pool
- Upgrade network adapters
- **Advantage:** No new hardware purchase
- **Limitation:** Socket and slot constraints

**Horizontal Scaling (Scale-Out):**

- Add nodes to cluster (up to 16)
- Automatic rebalancing
- Increase aggregate capacity
- **Advantage:** More flexibility
- **Limitation:** 16-node max

**Cluster Refresh:**

- Replace entire cluster with newer hardware
- Migrate VMs to new cluster
- Decommission old cluster
- **Advantage:** Latest technology
- **Limitation:** Significant investment

### Technology Trends

**Processor Evolution:**

- Higher core counts per socket
- More memory channels
- PCIe 5.0 and beyond
- CXL (Compute Express Link)

**Storage Evolution:**

- NVMe over Fabric (NVMe-oF)
- PCIe 5.0 SSDs (higher bandwidth)
- Persistent memory (PMem)
- QLC and PLC NAND (higher density)

**Networking Evolution:**

- 100 GbE and 200 GbE adapters
- Faster RDMA (RoCE v3)
- SmartNICs and DPUs
- Quantum networking (long-term)

### Future-Proofing Recommendations

**1. Plan for Growth:**

- Size for 3-5 year horizon
- Leave room for expansion
- Choose upgradeable platforms

**2. Standardize on Latest Generation:**

- Don't buy previous-gen hardware
- Invest in PCIe 4.0 or 5.0
- Use DDR5 if available

**3. Modular Design:**

- Separate clusters by workload
- Use Azure Arc for unified management
- Enable workload mobility

**4. Software-Defined Everything:**

- SDN for networking flexibility
- Software-defined storage
- Policy-based management
- Reduces hardware lock-in

---

## Cost Analysis of Hardware Investment

### Initial Hardware Costs

**Small Deployment (2-node, branch office):**

- Servers: $15,000 - $25,000 per node = $30,000 - $50,000
- Networking: $5,000 - $10,000
- Rack and infrastructure: $5,000 - $10,000
- **Total: $40,000 - $70,000**

**Medium Deployment (4-node, production):**

- Servers: $25,000 - $50,000 per node = $100,000 - $200,000
- Networking: $15,000 - $30,000
- Rack and infrastructure: $10,000 - $20,000
- **Total: $125,000 - $250,000**

**Large Deployment (8-node, enterprise):**

- Servers: $40,000 - $80,000 per node = $320,000 - $640,000
- Networking: $50,000 - $100,000
- Rack and infrastructure: $20,000 - $40,000
- **Total: $390,000 - $780,000**

### Software Licensing

**Windows Server Datacenter:**

- Per-core licensing
- ~$6,000 per 16-core license
- 2-socket server = $12,000 - $24,000

**Azure Local Subscription:**

- Per-core pricing
- ~$10 per core per month
- 4-node cluster (32 cores each): $1,280/month

### Ongoing Costs

**Annual Maintenance (Hardware):**

- 15-20% of hardware cost per year
- Includes parts replacement
- On-site support

**Power and Cooling:**

- Electricity: $0.10 - $0.20 per kWh
- 4-node cluster: 2.5 kW average = $2,200 - $4,400/year
- Cooling: ~1.5x power consumption

**Staffing:**

- Varies greatly by organization
- Plan for 0.5-2 FTE per cluster
- Training and certification costs

### Total Cost of Ownership (TCO) - 5 Years

**Medium Deployment (4-node) Example:**

- Initial hardware: $150,000
- Licensing (one-time): $50,000
- Azure Local subscription (5 years): $76,800
- Maintenance (5 years): $150,000
- Power (5 years): $15,000
- **Total 5-Year TCO: $441,800**

**Per VM Cost:**

- Assuming 200 VMs
- $441,800 / 200 VMs / 5 years = $442/VM/year
- Compare to public cloud (varies widely by workload)

**Break-Even Analysis:**

- Typically 2-3 years vs. public cloud
- Faster for 24/7 workloads
- Slower for sporadic workloads

---

## Deployment Checklist

### Pre-Deployment (2-4 weeks)

**Planning:**

- [ ] Define workload requirements
- [ ] Size cluster appropriately
- [ ] Select hardware vendor
- [ ] Design network topology
- [ ] Plan IP addressing
- [ ] Document architecture

**Procurement:**

- [ ] Order hardware
- [ ] Order network gear
- [ ] Procure licenses
- [ ] Order rack and PDUs
- [ ] Plan delivery logistics

**Facility Preparation:**

- [ ] Verify power capacity
- [ ] Verify cooling capacity
- [ ] Prepare rack location
- [ ] Install power circuits
- [ ] Install network drops

### Deployment Week 1

**Physical Installation:**

- [ ] Rack servers
- [ ] Install network switches
- [ ] Connect power cables
- [ ] Connect network cables
- [ ] Install management station
- [ ] Verify all connections

**Initial Configuration:**

- [ ] Configure BIOS settings
- [ ] Enable virtualization features
- [ ] Configure RAID for OS drives
- [ ] Configure BMC/iDRAC
- [ ] Verify hardware inventory

### Deployment Week 2

**Operating System:**

- [ ] Install Windows Server
- [ ] Apply latest updates
- [ ] Configure networking
- [ ] Join to domain
- [ ] Install Hyper-V role
- [ ] Install required features

**Cluster Creation:**

- [ ] Validate cluster hardware
- [ ] Create failover cluster
- [ ] Configure cluster networking
- [ ] Test cluster failover

### Deployment Week 3

**Storage Spaces Direct:**

- [ ] Enable Storage Spaces Direct
- [ ] Verify all drives
- [ ] Create storage pools
- [ ] Create volumes
- [ ] Test storage performance
- [ ] Configure resiliency

**Azure Integration (if Connected Mode):**

- [ ] Register with Azure Arc
- [ ] Configure monitoring
- [ ] Set up backup
- [ ] Apply policies
- [ ] Test connectivity

### Deployment Week 4

**Validation:**

- [ ] Run validation tests
- [ ] Performance benchmarking
- [ ] Failover testing
- [ ] Backup and restore test
- [ ] Security hardening
- [ ] Documentation review

**Handover:**

- [ ] Train operations team
- [ ] Provide runbooks
- [ ] Transfer to operations
- [ ] Schedule follow-up

---

## Next Steps

**Continue Learning:**

- [Azure Local Overview →](azure-local-overview)
- [Connected Mode Operations →](azure-local-connected-mode)
- [Disconnected Mode Operations →](azure-local-disconnected-mode)
- [Azure Local Quiz →](azure-local-quiz)

**External Resources:**

- [Azure Local System Requirements](https://learn.microsoft.com/en-us/azure/azure-local/concepts/system-requirements-23h2?view=azloc-2509)
- [Hardware Sizing Calculator](https://azurestackhcisolutions.azure.microsoft.com/)
- [Validated Hardware Catalog](https://azurestackhcisolutions.azure.microsoft.com/)

---

**Last Updated:** October 2025
