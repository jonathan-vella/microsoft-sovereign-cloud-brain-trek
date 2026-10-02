---
title: "Azure Local architecture"
description: "Understand Azure Local architecture, including the Azure Arc management plane, local workloads, platform services, hardware, deployment types, and scale limits."
lastVerified: 2026-10-02
sidebar:
  order: 2
---

## Architecture layers

Azure Local brings an Azure-consistent management model to infrastructure that runs in your datacenter, branch, edge site, or disconnected facility. The architecture has a cloud management plane, local workloads, a local platform layer, and validated hardware.

![Azure management plane connects through Azure Arc to Azure Local VMs and AKS on Azure Local running on Hyper-V, Storage Spaces Direct, failover clustering, networking, and one to 16 hyperconverged machines.](/images/level-100/azure-local-architecture-2026.svg)

At Level 100, use this model:

| Layer | What it does |
| --- | --- |
| Azure management plane | Uses Azure Arc, Azure portal, Azure CLI, Azure Resource Manager templates, Azure Monitor, Azure Policy, and Microsoft Defender for Cloud when the environment is connected. |
| Workload layer | Runs Azure Local VMs enabled by Azure Arc, AKS on Azure Local, and other supported workloads for the selected deployment type. |
| Platform layer | Uses Hyper-V, Storage Spaces Direct, Failover Clustering, software-defined networking, lifecycle management, and update orchestration. |
| Hardware layer | Uses catalog hardware from Microsoft partners. Hyperconverged deployments support one to 16 physical machines in a single instance ([source](https://learn.microsoft.com/azure/azure-local/overview/hyperconverged-overview?view=azloc-2609#features-and-architecture)). |

The data plane stays local. VMs, containers, application data, storage I/O, and east-west workload traffic run on Azure Local hardware. In connected operations, Azure services provide management, governance, monitoring, and lifecycle coordination when connectivity is available. In disconnected operations, selected control plane functions run locally.

## Azure Arc management

Azure Arc is the bridge between Azure and Azure Local. For Azure Local VMs enabled by Azure Arc, Azure Arc resource bridge provides lifecycle operations such as starting and stopping VMs, changing memory or vCPU, and adding or removing data disks and network interfaces ([source](https://learn.microsoft.com/azure/azure-local/concepts/compare-vm-management-capabilities?view=azloc-2609#types-of-vms-on-azure-local)).

That distinction matters. An Azure Arc-enabled server on Azure Local can use Azure Arc extensions for governance, monitoring, and protection, but it does not have the same lifecycle management as an Azure Local VM. An unmanaged VM has no Azure management. Microsoft Learn also states that conversion from an Arc-enabled server or unmanaged VM to an Azure Local VM is not supported ([source](https://learn.microsoft.com/azure/azure-local/concepts/compare-vm-management-capabilities?view=azloc-2609#types-of-vms-on-azure-local)).

## Deployment types

Azure Local deployment type is separate from connectivity mode. You choose a deployment type for scale and architecture, then choose connected or disconnected operations where supported.

| Deployment type | Current scale | Storage model | L100 notes |
| --- | --- | --- | --- |
| Hyperconverged | 1 to 16 machines. Rack-aware clusters are a subset with a maximum of 8 machines. | Compute and storage on the same machines with hyperconverged storage. | The simplest operational model and the most common starting point. |
| Disaggregated | 1 to 64 machines. | SAN-backed storage with compute and storage scaled separately. | Use when storage and compute grow at different rates or when an existing SAN strategy is required. |
| Multi-rack | Up to 128 nodes per instance, with integrated racks that expand to hundreds of machines. | SAN-backed, rack-scale design. | Designed for large datacenter environments. Microsoft Learn states that multi-rack spans multiple racks and scales up to 128 nodes each ([source](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/azure-local/connected-operations-overview#multi-rack-deployments)). |
| Rack-aware clustering | 2 racks, starting at 2+2 nodes and expanding to 3+3 or 4+4. | Hyperconverged storage. | Requires Azure Local 2510 or later, up to 1 ms round-trip latency between racks, and no external SAN ([source](https://learn.microsoft.com/azure/azure-local/concepts/rack-aware-cluster-overview?view=azloc-2609)). |
| Small form factor | Compact edge appliance. | Compact hardware design. | Used for space-constrained and power-constrained sites. The deployment type guide lists small form factor as connected mode only, with AI workloads and Foundry Local on small form factor in preview ([source](https://learn.microsoft.com/azure/azure-local/plan/find-your-deployment-type?view=azloc-2609#workload-availability-by-deployment-type)). |

Disconnected operations can run on hyperconverged and disaggregated deployments. The deployment type guide states that multi-rack and small form factor deployments are connected mode only ([source](https://learn.microsoft.com/azure/azure-local/plan/find-your-deployment-type?view=azloc-2609#overview)).

## Scale and fleet wording

Do not read "thousands of nodes" as a single-instance maximum. The single-instance maxima remain 16 machines for hyperconverged, 64 machines for disaggregated, and 128 nodes for multi-rack.

Microsoft Learn says connected operations can scale "from one node to thousands of nodes" ([source](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/azure-local/connected-operations-overview#deployment-options)). The April 2026 Microsoft blog clarifies the meaning. Azure Local can support deployments of up to thousands of servers within a single sovereign environment, and Sovereign Private Cloud can grow "from hundreds up to thousands of servers within a single sovereign boundary" ([source](https://blogs.microsoft.com/blog/2026/04/27/microsoft-sovereign-private-cloud-scales-to-thousands-of-nodes-with-azure-local/)). That is fleet scale across many Azure Local instances under one sovereign operating model, not a single Azure Local instance limit.

## Workload availability

Workload support varies by deployment type. The deployment type guide lists Azure Local VMs across hyperconverged, disaggregated, and multi-rack, but not small form factor. It lists AKS on Azure Local across all four deployment types. Microsoft 365 Local and GitHub Enterprise Local ([preview](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/github-local/github-local-overview)) are listed for hyperconverged and disaggregated only. Foundry Local is listed for hyperconverged and disaggregated, and for small form factor in preview ([source](https://learn.microsoft.com/azure/azure-local/plan/find-your-deployment-type?view=azloc-2609#workload-availability-by-deployment-type)).

At L100 depth, this means architects should avoid one universal Azure Local design. Start with workload needs, connectivity mode, scale, and hardware category. Then confirm the selected workload is supported on the selected deployment type.

## Sources

- [What are hyperconverged deployments of Azure Local?](https://learn.microsoft.com/azure/azure-local/overview/hyperconverged-overview?view=azloc-2609)
- [Connected operations overview](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/azure-local/connected-operations-overview)
- [Find your Azure Local deployment type](https://learn.microsoft.com/azure/azure-local/plan/find-your-deployment-type?view=azloc-2609)
- [Rack-aware clustering overview](https://learn.microsoft.com/azure/azure-local/concepts/rack-aware-cluster-overview?view=azloc-2609)
- [Compare management capabilities of VMs on Azure Local](https://learn.microsoft.com/azure/azure-local/concepts/compare-vm-management-capabilities?view=azloc-2609)
- [Microsoft Sovereign Private Cloud scales to thousands of nodes with Azure Local](https://blogs.microsoft.com/blog/2026/04/27/microsoft-sovereign-private-cloud-scales-to-thousands-of-nodes-with-azure-local/)
