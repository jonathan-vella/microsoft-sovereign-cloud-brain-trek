---
layout: default
title: Advanced Networking for Connected Mode
parent: Azure Local at Scale - Connected Mode
nav_order: 2
---

# Advanced Networking for Connected Mode

## Overview

Master complex networking scenarios for multi-site Azure Local deployments with direct cloud connectivity, inter-site communication, and sophisticated traffic engineering.

---

## Network Topology Options

### Hybrid Connectivity Models
- Azure ExpressRoute Private Peering
- VPN gateway connections
- Virtual WAN integration
- Dedicated interconnects

### Inter-Site Communication
- Site-to-site VPN
- Private peering protocols
- Direct fiber links
- Redundant paths

### Local Edge Networking
- SD-WAN capabilities
- Quality of Service (QoS)
- Traffic classification
- Policy-based routing

---

## Bandwidth and Latency Optimization

> **📊 Visual Reference Needed** *(Optional)*  
> *Networking Architecture - Connected Mode (Asset 47)*  
> Complete network diagram showing Azure connectivity, multi-site communication, edge networking, redundancy, and traffic flows.  
> **Specification Reference:** See `docs/level-300/VISUAL_SPECIFICATIONS.md` → Asset 47  
> **Source to adapt:** [Azure networking for Azure Local](https://learn.microsoft.com/en-us/azure/azure-local/network-overview)

---

## Advanced Routing Scenarios

### Application-Aware Routing
- Workload-specific paths
- Performance optimization
- Cost optimization paths
- Disaster recovery routes

### Traffic Engineering
- Load balancing algorithms
- Path preferences
- Failover mechanisms
- Traffic shaping policies

### Security Segmentation
- Network policies
- Microsegmentation
- Encrypted tunnels
- Zero-trust networking

---

## Performance Considerations

- **Throughput optimization**
  - Link aggregation
  - Compression
  - Offload capabilities

- **Latency management**
  - Hop count reduction
  - Queue management
  - Congestion avoidance

- **Reliability**
  - Redundant paths
  - Fast convergence
  - Automatic failover

---

## Monitoring and Troubleshooting

- Real-time flow monitoring
- Bandwidth utilization tracking
- Latency measurement
- Link quality metrics
- Packet loss detection

---

**See also:** [Multi-Site Architectures](azure-local-multi-site) | [Connected Mode Overview](azure-local-advanced-connected) | [Lab Exercise](azure-local-connected-lab)
