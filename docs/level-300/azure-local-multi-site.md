---
layout: default
title: Multi-Site Azure Local Architectures
parent: Module 2 - Azure Local Connected
nav_order: 1
---

# Multi-Site Azure Local Architectures

{: .no_toc }

## Table of Contents

{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

Deploy Azure Local clusters across multiple physical sites with synchronized operations, failover capabilities, and coordinated governance.

{: .important }
> **📝 Key Distinction:** Azure Local does NOT support stretch clusters (single cluster spanning multiple sites). This page covers **multi-cluster** architectures where each site has its own Azure Local cluster, connected through replication and Arc management.
>
> For **rack-level** high availability within a single cluster, see [Rack-Aware Clustering](../level-200/azure-local-ha-patterns.md#rack-aware-clustering-preview).

<details class="diagram-container">
<summary>View Diagram: Multi-Site Replication Topology</summary>
<div class="diagram-content" markdown="1">

![Azure Local Multi-Site Architecture showing primary, DR, and edge sites with replication topology](../assets/images/level-300/azure-local-multisite.svg)
_Figure 1: Azure Local multi-site deployment with synchronous and asynchronous replication across datacenters_

</div>
</details>

---

## Multi-Site vs. Rack-Aware Clustering

| Feature | Rack-Aware Clustering | Multi-Site Architecture |
|---------|----------------------|------------------------|
| **Cluster Count** | Single cluster | Multiple clusters |
| **Physical Scope** | 2 racks (same campus, ≤1ms latency) | Multiple sites (any distance) |
| **Storage** | Single pool, synchronous | Separate pools, replicated |
| **Replication** | Built-in (Storage Spaces Direct) | Azure Site Recovery or Storage Replica |
| **Failover** | Automatic (zone-aware) | Manual or ASR-automated |
| **Use Case** | Room/building-level HA | Geographic DR |
| **Status** | Preview | GA |

---

## Multi-Site Topology Patterns

```mermaid
graph TB
    subgraph Pattern1[Hub-and-Spoke]
        Hub[Central Hub Site<br/>Control Plane]
        Spoke1[Spoke Site 1<br/>Workloads]
        Spoke2[Spoke Site 2<br/>Workloads]
        Spoke3[Spoke Site 3<br/>Workloads]

        Hub --> Spoke1
        Hub --> Spoke2
        Hub --> Spoke3
    end

    subgraph Pattern2[Peer-to-Peer]
        Site1[Site 1]
        Site2[Site 2]
        Site3[Site 3]

        Site1 <--> Site2
        Site2 <--> Site3
        Site3 <--> Site1
    end

    subgraph Pattern3[Tiered]
        Primary[Primary Site<br/>Control & Data]
        Secondary1[Secondary Site 1<br/>Replicas]
        Secondary2[Secondary Site 2<br/>Replicas]
        Tertiary[Tertiary Site<br/>DR & Archive]

        Primary --> Secondary1
        Primary --> Secondary2
        Secondary1 --> Tertiary
        Secondary2 --> Tertiary
    end

    style Pattern1 fill:#E8F4FD,stroke:#0078D4,stroke-width:2px,color:#000
    style Pattern2 fill:#FFF4E6,stroke:#FF8C00,stroke-width:2px,color:#000
    style Pattern3 fill:#F3E8FF,stroke:#7B3FF2,stroke-width:2px,color:#000
```

### Distributed Hub-and-Spoke

- Central hub site (primary control plane)
- Spoke sites (application workloads)
- Replicated management
- Site-specific data residency

### Peer-to-Peer Federation

- No central hub
- Direct site-to-site communication
- Distributed quorum
- Equal governance rights

### Tiered Architecture

- Primary site (control plane & data)
- Secondary sites (read replicas, compute)
- Tertiary sites (DR & archival)
- Cascading replication

---

## Multi-Site Architecture Comparison


---

## Synchronization Mechanisms

### Management Synchronization

- Cluster configuration sync
- Policy and governance distribution
- Certificate management coordination
- Update and patch orchestration

### Data Replication

- Application data sync
- Database replication
- Storage synchronization
- Consistency requirements

### Workload Distribution

- VM placement policies
- Traffic routing across sites
- Load balancing strategies
- Site affinity rules

---

## Failover and Recovery

- **Site failure scenarios**
  - Single site outage
  - Network partition
  - Complete data center failure

- **Recovery procedures**
  - Failover automation
  - Manual intervention points
  - Data consistency verification
  - Service restoration order

---

## Operational Considerations

- Monitoring across sites
- Log aggregation and correlation
- Remote support coordination
- Maintenance scheduling
- Update deployment sequence

---

**See also:** [Connected Mode Architecture](azure-local-advanced-connected) | [Networking Deep Dive](azure-local-networking-advanced) | [Lab Exercise](azure-local-connected-lab)
