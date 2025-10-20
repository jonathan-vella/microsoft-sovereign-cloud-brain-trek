---
layout: default
title: Level 200 - Intermediate
nav_order: 4
has_children: true
description: "Intermediate architecture and pre-sales skills for Microsoft Sovereign Cloud solutions"
---

# Level 200: Intermediate - Architecture & Pre-Sales
{: .no_toc }

## Overview
{: .no_toc .text-delta }

Develop the ability to design solutions, plan deployments, and address customer-specific requirements for sovereign cloud architectures.

---

## Learning Objectives

By the end of Level 200, you will be able to:

### Sales & Pre-Sales Track

- ✅ Map customer requirements to appropriate sovereign cloud models
- ✅ Conduct TCO and ROI analysis for Azure Local deployments
- ✅ Position solutions against competitive offerings
- ✅ Qualify Edge RAG opportunities
- ✅ Present complete business cases to customers

### Technical Track

- ✅ Design Sovereign Landing Zone architectures
- ✅ Plan Azure Local deployments (connected and disconnected)
- ✅ Understand Edge RAG deployment prerequisites
- ✅ Architect hybrid connectivity solutions
- ✅ Implement governance and compliance controls

---

## Prerequisites

Before starting Level 200, ensure you have:

- [x] Completed Level 100 learning objectives
- [ ] Recommended: AZ-900 (Azure Fundamentals) certification or equivalent knowledge
- [ ] Access to an Azure subscription (for technical track)
- [ ] Access to lab environment or Azure Local hardware catalog for sizing exercises

**Estimated Time Commitment:** 4-6 hours per week  
**Total Duration:** 4-6 weeks  
**Total Hours:** 16-36 hours

---

## Learning Modules

### 1. Sovereign Landing Zone Architecture

**Duration:** 4-6 hours

- [SLZ vs. Standard Azure Landing Zone](slz-architecture.html)
- [Design Principles and Implementation](slz-architecture.html#design-principles)
- [Governance at Scale](slz-architecture.html#governance)

### 2. Azure Local Deployment Planning - Connected Mode

**Duration:** 4-6 hours

- [Prerequisites and Requirements](azure-local-connected.html)
- [Azure Arc Integration](azure-local-connected.html#arc-integration)
- [Hybrid Service Configuration](azure-local-connected.html#hybrid-services)

### 3. Azure Local Deployment Planning - Disconnected Mode

**Duration:** 4-6 hours

- [Air-Gapped Requirements](azure-local-disconnected.html)
- [Certificate Management](azure-local-disconnected.html#certificates)
- [Offline Operations](azure-local-disconnected.html#operations)

### 4. Edge RAG Deployment Prerequisites

**Duration:** 3-5 hours

- [Infrastructure Requirements](edge-rag-deployment.html)
- [NFS Server Configuration](edge-rag-deployment.html#nfs)
- [Language Model Selection](edge-rag-deployment.html#models)

### 5. TCO/ROI Modeling

**Duration:** 3-4 hours

- [Cost Components](tco-roi.html)
- [Connected vs. Disconnected Economics](tco-roi.html#comparison)
- [Business Case Development](tco-roi.html#business-case)

---

## Recommended Microsoft Learn Resources

### Essential Learning

1. **[Implement Azure Landing Zones](https://learn.microsoft.com/en-us/training/modules/enterprise-scale-introduction/)**
   - Foundation for sovereign landing zones

2. **[Configure Azure Arc-enabled Kubernetes](https://learn.microsoft.com/en-us/training/modules/configure-azure-arc-enabled-kubernetes/)**
   - Essential for Azure Local management

3. **[Manage hybrid workloads with Azure Arc](https://learn.microsoft.com/en-us/training/paths/manage-hybrid-infrastructure-with-azure-arc/)**
   - Complete learning path for hybrid scenarios

### Recommended Reading

- **[Sovereign Landing Zone architecture](https://learn.microsoft.com/en-us/industry/sovereign-cloud/sovereign-public-cloud/sovereign-landing-zone/overview-slz)** - SLZ design principles
- **[Azure Local deployment overview](https://learn.microsoft.com/en-us/azure/azure-local/deploy/deployment-introduction)** - Deployment planning guide
- **[Disconnected operations overview](https://learn.microsoft.com/en-us/azure/azure-local/manage/disconnected-operations-overview)** - Air-gapped deployment guidance
- **[Edge RAG deployment prerequisites](https://learn.microsoft.com/en-us/azure/azure-arc/edge-rag/complete-prerequisites)** - Complete prerequisites checklist

---

## Hands-On Labs

### Lab 1: Sovereign Landing Zone Setup

**Objective:** Configure a test Sovereign Landing Zone with management groups and policies

**Prerequisites:**
- Azure subscription with Owner access
- Azure CLI or PowerShell

**Estimated Time:** 2-3 hours

**[Lab Instructions →](labs/lab-01-slz-setup.html)**

### Lab 2: Azure Local Deployment Planning

**Objective:** Plan and document an Azure Local deployment for a test environment

**Prerequisites:**
- Access to Azure Local sizing tool
- Understanding of customer requirements

**Estimated Time:** 2-3 hours

**[Lab Instructions →](labs/lab-02-azure-local-planning.html)**

### Lab 3: Edge RAG Prerequisites

**Objective:** Set up NFS server and prepare infrastructure for Edge RAG deployment

**Prerequisites:**
- AKS Arc cluster or ability to create one
- Linux VM for NFS server

**Estimated Time:** 3-4 hours

**[Lab Instructions →](labs/lab-03-edge-rag-prereqs.html)**

---

## Success Criteria

### Sales Track Completion ✅

You have successfully completed Level 200 (Sales Track) when you can:

- ✓ Develop and present a complete business case (TCO/ROI) for Azure Local
- ✓ Handle common customer objections confidently
- ✓ Position solutions against competitive offerings (VMware, Nutanix, etc.)
- ✓ Qualify Edge RAG opportunities with clear value proposition
- ✓ Map customer requirements to appropriate deployment models

### Technical Track Completion ✅

You have successfully completed Level 200 (Technical Track) when you can:

- ✓ Design and document a Sovereign Landing Zone architecture
- ✓ Plan Azure Local deployments for both connected and disconnected modes
- ✓ Complete prerequisites checklist for Edge RAG deployment
- ✓ Size Azure Local hardware appropriately
- ✓ Successfully complete all hands-on labs

---

## Next Steps

Once you've completed Level 200:

1. ✅ Complete all hands-on labs
2. ✅ Review solution architectures
3. ✅ Practice customer presentations
4. 🎯 **[Proceed to Level 300: Advanced Expertise →](../level-300/)**

---

**Last Updated:** October 2025
