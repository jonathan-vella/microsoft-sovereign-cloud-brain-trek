---
title: "Module 2 - Azure Local Connected"
description: "Module 2: Azure Local at scale (connected mode) — multi-site topologies, advanced storage and network optimizations, update ring strategies, and capacity planning at enterprise scale."
sidebar:
  order: 2
---

## Overview

Scale Azure Local deployments across multiple sites while maintaining cloud connectivity. This module covers multi-site architectures, advanced networking, cloud-integrated updates, and cost optimization for production environments.

**Duration:** 4-5 hours  
**Learning Tracks:** Both Sales & Technical  
**Prerequisites:** Level 200 Azure Local completion

---

## Learning Objectives

### Sales Track

- ✅ Design multi-site scenarios for customers
- ✅ Present scaling economics to stakeholders
- ✅ Differentiate connected vs. disconnected strategies
- ✅ Plan PoC-to-production scaling roadmaps

### Technical Track

- ✅ Design hub-and-spoke and mesh topologies
- ✅ Implement multi-site replication with Azure Site Recovery
- ✅ Optimize network performance for multi-site
- ✅ Manage updates across multiple sites
- ✅ Implement cost optimization strategies

:::note[📝 Note]
Stretch clusters are not supported in Azure Local. For multi-site high availability, use Azure Site Recovery or Storage Replica between separate clusters at each site.
:::


---

## Core Topics

1. **Multi-Site Deployment Patterns** → [azure-local-multi-site.md](/level-300/azure-local-multi-site/)
2. **Advanced Networking** → [azure-local-networking-advanced.md](/level-300/azure-local-networking-advanced/)
3. **Update Management** → [azure-local-advanced-connected.md](/level-300/azure-local-advanced-connected/)

---

## Architecture Decision Tree

---

## Module Content

### Quick Decision Guide

**Choose Hub-and-Spoke when:**

- Centralized management priority
- Bandwidth constraints
- < 5 sites
- Acceptable hub latency

**Choose Full Mesh when:**

- High availability critical
- Low latency requirements
- < 4 sites (complexity increases)
- Bandwidth available

**Choose Hybrid when:**

- Mix of requirements
- Scaling > 5 sites
- Flexible connectivity options
- Optimal for sovereignty

---

## Recommended Learning Path

1. Start: [Multi-Site Patterns](/level-300/azure-local-multi-site/)
2. Deep Dive: [Advanced Networking](/level-300/azure-local-networking-advanced/)
3. Operations: [Connected Updates](/level-300/azure-local-advanced-connected/)

---

**Module Duration:** 8-10 hours  
**Estimated Completion:** 1-1.5 weeks @ 6 hrs/week
