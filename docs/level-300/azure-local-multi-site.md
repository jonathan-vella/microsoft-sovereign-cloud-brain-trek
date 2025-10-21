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

> **📊 Visual Reference Needed**  
> *Multi-Site Deployment Topologies (Asset 46)*  
> Diagram showing three topology patterns with network flows, redundancy levels, failover behavior, and governance model for each.  
> **Specification Reference:** See `docs/level-300/VISUAL_SPECIFICATIONS.md` → Asset 46  
> **Source to adapt:** [Multi-site Azure Local deployment patterns](https://learn.microsoft.com/en-us/azure/azure-local/plan/multi-site-patterns)

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

**See also:** [Connected Mode Architecture](azure-local-advanced-connected.html) | [Networking Deep Dive](azure-local-networking-advanced.html) | [Lab Exercise](azure-local-connected-lab.html)
