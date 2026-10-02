---
title: "Module 4: Azure Arc"
description: "Learn how Azure Arc brings Azure governance, inventory, policy, and selected services to servers, Kubernetes, SQL, and private cloud resources outside Azure."
lastVerified: 2026-10-02
module:
  duration: "35-45 minutes"
  objectives:
    - Explain what Azure Arc adds to hybrid and multicloud resources.
    - Distinguish the Arc control plane from workload data planes.
    - Identify current Arc support for servers, Kubernetes, data services, resource bridge, and Arc gateway.
    - Describe current retirements and pricing facts that affect Arc planning.
  prerequisites:
    - /level-100/module-01-digital-sovereignty/
    - /level-100/module-03-azure-local/
sidebar:
  label: Overview
  order: 4
---

Azure Arc projects resources outside Azure into Azure Resource Manager so you can organize, govern, and monitor them with familiar Azure tools. The resources keep running where they are, such as on-premises, on Azure Local, or in another cloud.

This module focuses on the current L100 facts that matter for sovereign cloud planning. You will see where Arc is only a control plane, where services layered on Arc add cost or data movement, and which Arc capabilities have changed since earlier training material was written.

## Sources

- [Azure Arc overview](https://learn.microsoft.com/azure/azure-arc/overview)
- [What is Azure Arc-enabled Kubernetes?](https://learn.microsoft.com/azure/azure-arc/kubernetes/overview)
- [Connectivity mode and requirements](https://learn.microsoft.com/azure/azure-arc/data/connectivity)
- [Release notes, Azure Arc-enabled data services](https://learn.microsoft.com/azure/azure-arc/data/release-notes)
- [Simplify network configuration requirements with Azure Arc gateway](https://learn.microsoft.com/azure/azure-arc/servers/arc-gateway)
- [What is Azure Arc resource bridge?](https://learn.microsoft.com/azure/azure-arc/resource-bridge/overview)
