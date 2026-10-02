---
title: "Module 2: Azure Arc at scale"
description: "Design Azure Arc operations at scale, including gateway connectivity, policy governance, enterprise onboarding, and cost controls."
lastVerified: 2026-10-02
module:
  duration: "60-90 minutes"
  objectives:
    - Plan Azure Arc gateway, resource bridge, and server management capabilities for hybrid estates.
    - Apply Azure Policy, machine configuration, and Kubernetes policy patterns to Arc resources.
    - Choose enterprise onboarding, network, tagging, RBAC, and cost governance patterns for Arc at scale.
  prerequisites:
    - /level-100/module-04-azure-arc/
sidebar:
  label: Overview
---

Azure Arc projects servers, Kubernetes clusters, private cloud VMs, and data services into Azure Resource Manager so teams can govern hybrid and multicloud assets with Azure tools. This module focuses on intermediate planning decisions: how traffic reaches Azure, how governance applies to servers and clusters, how resource bridge supports VM operations, and where costs appear.

You also update retired assumptions. Indirectly connected mode for Azure Arc-enabled data services is retired, Azure Arc-enabled PostgreSQL server retired in July 2025, and Arc gateway is now a core connectivity option for Arc-enabled servers and Azure Local deployments ([Learn](https://learn.microsoft.com/azure/azure-arc/overview), [Learn](https://learn.microsoft.com/azure/azure-arc/data/release-notes), [Learn](https://learn.microsoft.com/azure/azure-arc/servers/arc-gateway)).

## Before you start

Use the Level 100 Azure Arc module as the baseline for resource types and onboarding. In this module, assume you already know how a single server or cluster connects to Azure Arc. The design work here is about scale, change control, network restrictions, and cost ownership.

Key terms you will use:

| Term | What it means in this module |
| --- | --- |
| Arc gateway | An Azure resource and local proxy component that reduces required outbound Arc endpoints and lets teams audit Arc traffic. |
| Arc resource bridge | A Kubernetes-based appliance that projects Azure Local, VMware vSphere, or SCVMM resources into Azure for VM lifecycle operations. |
| Machine configuration | The Azure Policy feature that audits or configures operating system settings on Azure and Arc-enabled machines. It was formerly called Guest Configuration. |
| Custom location | An Azure resource that maps a deployment target to a private cloud or Arc-enabled Kubernetes cluster. |

## Sources

- [Azure Arc overview](https://learn.microsoft.com/azure/azure-arc/overview)
- [Simplify network configuration requirements with Azure Arc gateway](https://learn.microsoft.com/azure/azure-arc/servers/arc-gateway)
- [Release notes - Azure Arc-enabled data services](https://learn.microsoft.com/azure/azure-arc/data/release-notes)
