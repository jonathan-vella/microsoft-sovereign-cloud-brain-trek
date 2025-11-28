---
layout: default
title: Hardware Planning & Sizing
parent: Azure Local Architecture Deep Dive
nav_order: 2
---

# Hardware Planning and Sizing

Selecting and sizing the correct hardware is fundamental to Azure Local success. This guide helps you make informed decisions about processor selection, memory configuration, storage architecture, and network capabilities.

## CPU Selection and Performance

### Processor Families

**3rd Generation Intel Xeon Scalable (Ice Lake):**

- 40 cores per socket (up to 80 cores dual-socket)
- PCIe 4.0 support (16 GB/s per lane)
- Enhanced encryption capabilities (AVX-512)
- Recommended for most deployments
- Price/performance sweet spot

**4th Generation Intel Xeon Scalable (Sapphire Rapids):**

- Up to 60 cores per socket
- PCIe 5.0 support
- Enhanced AI capabilities
- Newest option, more expensive

**AMD EPYC 9004 Series (Genoa):**

- Up to 192 cores per socket
- PCIe 5.0 support
- Excellent for high-core-count workloads
- Cost-effective for large deployments

### Processor Allocation

Azure Local divides CPU resources between management and compute:

```text
Example 48-core configuration:
- Management partition: 12-16 cores (reserved)
- VM compute capacity: 32-36 cores (available)
- Hyperthreading enabled: 64-72 logical processors
```

**Rule of Thumb:**

- Reserve 1 core for every 4 cores total
- For 3-node cluster: ~10-12 cores per node in management, 36-38 in compute

### Performance Characteristics

**Turbo Frequency Benefits:**

- Turbo modes increase core frequency when not fully loaded
- Beneficial for latency-sensitive workloads
- Careful: Can introduce thermal throttling
- Monitor temperature during heavy workloads

**NUMA Architecture:**

- Processors organize memory into NUMA nodes
- Local NUMA access ~100 ns
- Remote NUMA access ~200 ns
- Proper VM placement critical for performance

## Memory Configuration

### Memory Sizing

**General Guidelines:**

- Minimum: 256 GB per node
- Recommended: 512 GB - 1 TB per node
- For database-heavy workloads: 1-2 TB per node
- Memory grows faster than CPU needs (ratio: 1 GB per core → 2-4 GB per core)

**Azure Local Overhead:**

- Management OS: 80-120 GB
- Reserved cache: 10-20 GB
- Customer VMs: Remainder (typically 300-900 GB per node)

### Memory Types

**DDR5 (Newest):**

- 6000-8000 MT/s speeds
- Available with 4th Gen Xeon (Sapphire Rapids)
- Not available with 3rd Gen Xeon (Ice Lake)
- 10-15% performance improvement over DDR4

**DDR4:**

- 3200-4800 MT/s typical speeds
- Compatible with 3rd Gen Xeon
- Widely available, cost-effective
- Good baseline for most workloads

**ECC Requirement:**

- Mandatory for all Azure Local deployments
- Detects and corrects single-bit errors
- Essential for long-running applications
- Minimal performance impact (< 2%)

### Memory Organization

**DIMM Population:**

- Populate symmetrically across all slots
- Match speeds and capacities
- Avoid mixing DDR4 and DDR5
- Validate in BIOS that all DIMMs recognized

**Dual-Socket Configurations:**

- Two processors share memory
- NUMA latency between sockets: 150-300 ns
- Consider single-socket for better performance
- Dual-socket provides redundancy if socket fails

## Storage Architecture

### Drive Selection

**NVMe SSDs (Cache Tier):**

- Speed: 3,500-7,000 MB/s random read
- Form factor: M.2 2280 or 22110
- Capacity: 800 GB - 2 TB typical
- Cost: $500-1,500 per drive
- Provide ultra-low cache latency

**SAS/SATA SSDs (Capacity Tier):**

- Speed: 500-600 MB/s sequential
- Capacity: 1-4 TB typical
- Cost: $200-600 per drive
- Larger capacity than NVMe at lower cost
- Primary storage tier in most deployments

**SAS HDDs (Archive Tier):**

- Speed: 100-200 MB/s sequential
- Capacity: 2-14 TB typical
- Cost: $50-150 per drive
- Power-hungry compared to SSD
- Used for rarely-accessed historical data

### Storage Configuration

**Minimum Storage:**

- 4 drives per node (minimum recommended)
- Mix: 1 NVMe + 3 SSD typical
- Provides resilience to single drive failure
- ~4-6 TB usable per node with 3-way mirror

**Enterprise Storage:**

- 6-8 drives per node
- Mix: 1-2 NVMe + 3-5 SSD + optional 2-4 HDD
- Allows tiered storage architecture
- ~10-20 TB usable per node

**Example 3-Node Cluster:**

```text
Per Node:
  - 1 × 960 GB NVMe (cache)
  - 4 × 1.6 TB SSD (capacity tier)
  - Optional: 2 × 8 TB HDD (archive)

Per Cluster:
  - Total raw: 19.2 TB (without HDD) or 35.2 TB (with HDD)
  - With 3-way mirror: 6.4 TB usable (SSD only)
  - With 3-way mirror + 2-way HDD: 10.4 TB usable
```

### Storage Pool Design

**Single-Pool Model (Recommended for most):**

- All drives in one pool
- Automatic tiering between NVMe/SSD/HDD
- Simpler management
- Works for diverse workloads

**Multi-Pool Model (Advanced):**

- Separate pools for performance vs. capacity
- Useful for high-performance demanding workload isolation
- More complex to manage
- Not recommended for initial deployments

## Network Interface Selection

### Network Adapter Types

**1 Gbps Adapters (Legacy):**

- Only suitable for management networks
- Insufficient for storage or cluster traffic
- Not recommended for new deployments

**10 Gbps Adapters:**

- Acceptable for small clusters or management
- Limited for storage traffic
- Can work for 2-node clusters if well-tuned

**25 Gbps Adapters (Recommended):**

- Sweet spot for most production deployments
- Sufficient headroom for storage and cluster
- Reasonable cost/performance
- Good inter-node communication

**100 Gbps Adapters:**

- For very large clusters (6+ nodes)
- Significant network investment
- Overkill for most deployments
- Consider only for specialized scenarios

### RDMA Support

**iWARP (Recommended):**

- Works over regular Ethernet networks
- Lower latency than TCP/IP for storage
- No special switch configuration needed
- Supported by most vendors

**RoCE (RDMA over Converged Ethernet):**

- Lower latency than iWARP
- Requires Priority Flow Control (PFC)
- Needs converged network expertise
- Higher performance at higher complexity

**No RDMA:**

- Slower storage communication
- Uses standard TCP/IP
- Not recommended for production
- May be acceptable for POC

## Capacity Planning Examples

### Example 1: 3-Node Small/Medium Cluster

**Use Case:** Mid-market company, mixed workloads

```text
Hardware per Node:
  - Processor: 2 × 16-core Xeon (32 cores total)
  - Memory: 512 GB DDR4
  - Storage: 1 NVMe (960 GB) + 4 SSD (1.6 TB each)
  - Network: 2 × 25 Gbps (converged network)
  - Power: ~2-3 kW per node

Per-Node Usable:
  - CPU for VMs: ~24 cores (24/32)
  - Memory for VMs: ~350 GB (512 - 162 overhead)
  - Storage: ~2 TB (with 3-way mirror)

3-Node Cluster Total:
  - Total compute: 72 cores, 1.05 TB memory
  - Total storage: 6 TB usable
  - Power: 6-9 kW (plus networking)
  - Dimensions: 3 × 2U servers or 1 × 6U integrated
```

### Example 2: 3-Node Large Enterprise Cluster

**Use Case:** Enterprise, performance-demanding workloads

```text
Hardware per Node:
  - Processor: 2 × 32-core Xeon (64 cores total)
  - Memory: 1 TB DDR5
  - Storage: 2 NVMe (1.6 TB each) + 6 SSD (3.2 TB each)
  - Network: 2 × 100 Gbps (dedicated storage network)
  - Power: ~8-10 kW per node

Per-Node Usable:
  - CPU for VMs: ~48 cores (48/64)
  - Memory for VMs: ~800 GB (1 TB - 200 GB overhead)
  - Storage: ~12 TB (with 3-way mirror, all tiers)

3-Node Cluster Total:
  - Total compute: 144 cores, 2.4 TB memory
  - Total storage: 36 TB usable
  - Power: 24-30 kW
  - Can support: 20-30 large VMs or 50-100 small containers
```

### Example 3: Multi-Node Federation

**Use Case:** Large enterprise with multiple Azure Local clusters

```text
Site 1 (Headquarters):
  - 3-node cluster (specifications as above)
  - 6 TB usable storage

Site 2 (Regional Office):
  - 2-node cluster
  - 2 TB usable storage

Site 3 (Branch Office):
  - 1-node cluster (POC/small workloads)
  - 500 GB local storage

Total Deployment:
  - 6 nodes across 3 sites
  - 8.5 TB usable storage total
  - Centralized management via Azure Arc
```

## Hardware Procurement

### Validation Checklist

Before purchasing, verify:

- [ ] Server model supported by Azure Local
- [ ] All processors, memory, storage supported
- [ ] Network adapters support RDMA (iWARP or RoCE)
- [ ] Power infrastructure adequate (kW budgets)
- [ ] Cooling capacity verified
- [ ] Rack space available
- [ ] Network switching capable of VLAN/QoS
- [ ] Windows Server 2022/2025 certification

### TCO Calculation

**3-Year Total Cost of Ownership:**

```text
Hardware (Year 1): $120,000 (3-node cluster)
Software (none): $0
Power/Cooling (3 years): $15,000
Maintenance (3 years): $10,000
Network switches & cabling: $20,000
Professional services: $30,000

Total: $195,000
Per TB storage: $32,500 (6 TB usable)
Per VM capacity: ~$10,000 (assuming 20 VMs)
```

Compare to:

- Hyper-converged infrastructure: $250,000+
- Traditional SAN + servers: $300,000+
- Public cloud migration: Ongoing $/month

---

## Key Takeaways

1. **Processor Selection:** Choose based on core count needs; 3rd Gen Xeon/EPYC 9004 recommended
2. **Memory:** Plan for 2-4 GB per vCore; DDR5 preferred if available
3. **Storage:** Use tiered approach (NVMe + SSD + HDD) for best cost/performance
4. **Network:** 25 Gbps minimum for production, 100 Gbps for large clusters
5. **Capacity:** Plan for 18-month growth horizon
6. **Validation:** Ensure hardware on official support list before purchasing
