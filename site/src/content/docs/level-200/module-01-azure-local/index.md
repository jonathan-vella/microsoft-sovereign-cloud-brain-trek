---
title: "Module 1: Azure Local architecture"
description: "Plan Azure Local deployment types, hardware, resiliency, networking, VM management, and AKS design at intermediate depth."
lastVerified: 2026-10-02
module:
  duration: "60-90 minutes"
  objectives:
    - Choose the right Azure Local deployment type for scale, storage, and connectivity requirements.
    - Plan hardware, storage, network, update, and high-availability choices using Microsoft-supported limits.
    - Explain how Azure Local VMs, unmanaged VMs, Arc-enabled servers, and AKS on Azure Local differ.
  prerequisites:
    - /level-100/module-03-azure-local/
sidebar:
  label: Overview
---

Azure Local runs Azure-managed infrastructure on customer-owned hardware. In this module, you move beyond the Level 100 overview and plan an Azure Local instance using current deployment limits, hardware categories, update requirements, resiliency patterns, and networking models.

The module uses the current Azure Local release model. Azure Local now follows a monthly release train such as 2607, 2608, and 2609, and a system must stay within six months of the latest release to remain supported ([Learn](https://learn.microsoft.com/azure/azure-local/release-information-23h2)). Older guidance that was specific to Azure Stack HCI 23H2 no longer applies because that OS reached end of support in April 2026 ([Learn](https://learn.microsoft.com/azure/azure-local/release-information-23h2#os-version-23h2)).

## Before you start

You should already know what Azure Local is, how Azure Arc connects it to Azure, and why organizations use connected or disconnected operations. If you need that foundation, review the prerequisite module first.

This module focuses on design choices that affect production outcomes:

- Scale and deployment type, including hyperconverged, disaggregated, multi-rack, and small form factor.
- Hardware procurement, solution categories, Solution Builder Extension updates, and system requirements.
- Resiliency, including Storage Spaces Direct, failover clustering, switchless designs, rack-aware clustering, and disaster recovery.
- Network planning with Network ATC intents, RDMA, switched and switchless storage, SDN enabled by Arc, and Arc gateway.
- Workload management for Azure Local VMs and AKS on Azure Local.

## Sources

- [Find your Azure Local deployment type](https://learn.microsoft.com/azure/azure-local/plan/find-your-deployment-type)
- [Azure Local release information](https://learn.microsoft.com/azure/azure-local/release-information-23h2)
- [Connected operations overview](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/azure-local/connected-operations-overview)
- [Disconnected operations for Azure Local](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview)
