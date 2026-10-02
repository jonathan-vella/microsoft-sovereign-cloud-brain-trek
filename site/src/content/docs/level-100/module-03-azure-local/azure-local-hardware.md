---
title: "Azure Local hardware"
description: "Learn the Azure Local hardware catalog categories, when Premier Solutions matter, and how to choose hardware for connected, disconnected, and workload-specific scenarios."
lastVerified: 2026-10-02
sidebar:
  order: 5
---

## Start with the catalog

Azure Local is a hardware-backed platform. You do not build it from arbitrary servers. Microsoft points customers to validated hardware from Microsoft hardware partners and the Azure Local catalog ([source](https://learn.microsoft.com/azure/azure-local/overview/hyperconverged-overview?view=azloc-2609#overview)).

The catalog matters for support because Azure Local depends on a tested combination of server hardware, firmware, drivers, storage, networking, and update integration. Partner validation also matters for Solution Builder Extension updates, which can provide drivers, firmware, and partner-specific content through the Azure Local update process.

## Hardware catalog categories

The current hardware catalog uses three categories:

| Category | What it means at L100 depth | Typical use |
| --- | --- | --- |
| Validated Nodes | Hardware validated for Azure Local, with OEM-documented update processes. | Teams that want more configuration control and can manage OEM-specific processes. |
| Integrated Systems | Preconfigured systems from hardware partners, with fuller integration than individual nodes. | Standard production deployments that benefit from a more guided hardware stack. |
| Premier Solutions | Microsoft-recommended, partner-collaborative solutions designed for the best Azure Local experience. | Sovereign private cloud workloads that need the strongest integrated support path, Microsoft 365 Local, or disconnected operations management clusters. |

The OEM license page names Premier Solutions, Integrated Systems, and Validated Nodes as Azure Local hardware categories ([source](https://learn.microsoft.com/azure/azure-local/oem-license?view=azloc-2609#about-the-oem-license)). The hyperconverged overview says Microsoft recommends purchasing Premier Solutions with hardware partners and lists partners including ASUS, Blue Chip, DataON, Dell EMC, Fujitsu, HPE, Hitachi, Lenovo, NEC, primeLine Solutions, QCT, and Supermicro ([source](https://learn.microsoft.com/azure/azure-local/overview/hyperconverged-overview?view=azloc-2609#hardware-and-software-partners)).

## When Premier Solutions are required

Premier Solutions are more than a "nice to have" in some sovereign private cloud scenarios.

Microsoft 365 Local must run on an Azure Local Premier Solution that meets Microsoft 365 Local hardware requirements ([source](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/m365-local/microsoft-365-local-overview#microsoft-365-local-hardware-requirements)). [Module 6: Microsoft 365 Local](/level-100/module-06-microsoft-365-local/) covers the workload itself.

Disconnected operations also have a Premier hardware requirement. The disconnected operations eligibility criteria state that disconnected operations support Premier Solutions for Azure Local and require a dedicated management cluster ([source](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview?view=azloc-2609#eligibility-criteria)). The management cluster hardware page tells planners to select catalog hardware with the disconnected operations solution capability ([source](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-control-plane-appliance?view=azloc-2609#hardware-procurement)).

## Choose hardware by deployment type

Match hardware to the deployment type before you size individual machines.

| Deployment need | Hardware decision |
| --- | --- |
| Small branch or edge site | Consider hyperconverged or small form factor. Small form factor is connected mode only in the deployment type guide. |
| Standard private cloud instance | Start with hyperconverged. It supports one to 16 machines and uses compute and storage on the same machines. |
| Compute and storage grow separately | Consider disaggregated. It supports up to 64 machines with SAN-backed storage. |
| Large datacenter footprint | Consider multi-rack. It is a connected deployment type for rack-scale environments, with up to 128 nodes per instance. |
| Fully disconnected operation | Plan Premier hardware, a dedicated management cluster, and separate workload clusters. |
| Microsoft 365 Local | Use an Azure Local Premier Solution and a Microsoft 365 Local certified solution partner. |

The deployment type guide is the starting point because it ties connectivity, scale, architecture, and workload availability together ([source](https://learn.microsoft.com/azure/azure-local/plan/find-your-deployment-type?view=azloc-2609)).

## Choosing at L100 depth

At foundational depth, do not start with CPU, memory, and drive counts. Start with four decisions:

1. Can the environment use connected operations, or does it need disconnected operations?
2. Which workloads must run on the platform?
3. Which deployment type supports those workloads and the required scale?
4. Which catalog category gives the required support path?

After those decisions, use the Azure Local sizer and partner guidance for detailed sizing. The exact bill of materials belongs in deeper planning with the hardware partner, Microsoft account team, and workload owners.

## Billing and licensing hardware considerations

Hardware choice can affect billing treatment. Azure Local can be billed monthly through the Azure subscription on a per-physical-core basis ([source](https://learn.microsoft.com/azure/azure-local/overview/hyperconverged-overview?view=azloc-2609#benefits)). Azure Hybrid Benefit can waive the host fee only for hyperconverged, cloud-connected deployments with no external storage ([source](https://learn.microsoft.com/azure/azure-local/concepts/azure-hybrid-benefit?view=azloc-2609#what-is-azure-hybrid-benefit-for-azure-local)).

The OEM license is purchased through hardware partners with Azure Local hardware. It remains valid for the hardware lifetime, covers up to 16 cores with two-core and four-core add-ons for larger systems, and includes Azure Local, Windows Server Datacenter guest VMs, and AKS enabled by Azure Arc ([source](https://learn.microsoft.com/azure/azure-local/oem-license?view=azloc-2609#about-the-oem-license)).

Microsoft Learn warns that mixed-node scenarios with different hardware models, operating system versions, or billing models in one Azure Local instance are not supported ([source](https://learn.microsoft.com/azure/azure-local/oem-license?view=azloc-2609#mixed-node-scenarios)). Keep hardware and billing treatment consistent within an instance.

## Sources

- [What are hyperconverged deployments of Azure Local?](https://learn.microsoft.com/azure/azure-local/overview/hyperconverged-overview?view=azloc-2609)
- [Find your Azure Local deployment type](https://learn.microsoft.com/azure/azure-local/plan/find-your-deployment-type?view=azloc-2609)
- [OEM license for Azure Local overview](https://learn.microsoft.com/azure/azure-local/oem-license?view=azloc-2609)
- [Azure Hybrid Benefit for Azure Local](https://learn.microsoft.com/azure/azure-local/concepts/azure-hybrid-benefit?view=azloc-2609)
- [Disconnected operations for Azure Local](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview?view=azloc-2609)
- [Dedicated management cluster for disconnected operations](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-control-plane-appliance?view=azloc-2609)
- [What is Microsoft 365 Local?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/m365-local/microsoft-365-local-overview)
