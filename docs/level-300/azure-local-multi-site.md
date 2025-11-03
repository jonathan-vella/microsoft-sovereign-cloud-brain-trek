---
layout: default
title: Multi-Site Azure Local Architectures
parent: Azure Local at Scale - Connected Mode
nav_order: 1
---

# Multi-Site Azure Local Architectures

## Overview

Deploy Azure Local clusters across multiple physical sites with synchronized operations, failover capabilities, and coordinated governance.

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
