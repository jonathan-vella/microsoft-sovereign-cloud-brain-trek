---
layout: default
title: Azure Local at Scale - Connected Mode
parent: Level 300 - Advanced
nav_order: 2
has_children: true
---

# Module 2: Azure Local at Scale - Connected Mode
{: .no_toc }

## Overview

Scale Azure Local deployments across multiple sites while maintaining cloud connectivity. This module covers multi-site architectures, advanced networking, cloud-integrated updates, and cost optimization for production environments.

**Duration:** 8-10 hours  
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
- ✅ Implement stretch clusters across sites
- ✅ Optimize network performance for multi-site
- ✅ Manage updates across multiple sites
- ✅ Implement cost optimization strategies

---

## Core Topics

1. **Multi-Site Deployment Patterns** → [azure-local-multi-site.md](azure-local-multi-site)
2. **Advanced Networking** → [azure-local-networking-advanced.md](azure-local-networking-advanced)
3. **Update Management** → [azure-local-advanced-connected.md](azure-local-advanced-connected)
4. **Hands-On Lab** → [azure-local-connected-lab.md](azure-local-connected-lab)

---

## Architecture Decision Tree

> **📊 Visual Reference Needed**  
> *Multi-Site Azure Local Architectures (Asset 46)*  
> Three side-by-side deployment patterns: Hub-and-Spoke, Full Mesh, and Hybrid, showing topology, connections, and key metrics.  
> **Specification Reference:** See `docs/level-300/VISUAL_SPECIFICATIONS.md` → Asset 46  
> **Source to adapt:** [Azure Local deployment patterns](https://learn.microsoft.com/en-us/azure/azure-local/deploy/deployment-introduction?view=azloc-2509)

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

1. Start: [Multi-Site Patterns](azure-local-multi-site)
2. Deep Dive: [Advanced Networking](azure-local-networking-advanced)
3. Operations: [Connected Updates](azure-local-advanced-connected)
4. Hands-On: [Lab](azure-local-connected-lab)

---

**Module Duration:** 8-10 hours  
**Estimated Completion:** 1-1.5 weeks @ 6 hrs/week
