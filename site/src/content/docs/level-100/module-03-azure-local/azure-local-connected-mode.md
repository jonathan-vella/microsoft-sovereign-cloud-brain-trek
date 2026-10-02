---
title: "Azure Local connected operations"
description: "Learn how connected Azure Local deployments use periodic Azure connectivity for management, governance, lifecycle operations, and monitoring while workloads stay local."
lastVerified: 2026-10-02
sidebar:
  order: 3
---

## What connected operations means

Connected operations is the standard Azure Local operating model for environments that can reach Azure public cloud periodically. Microsoft Learn describes connected operations as a model where Azure Local uses periodic Azure connectivity for control plane activities while workloads and data remain on-premises ([source](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/azure-local/connected-operations-overview)).

Connected does not mean every workload depends on Azure for runtime. VMs, containers, storage, and application data run locally on Azure Local hardware. Azure provides management and operational services when connectivity is available.

## The 30-day tolerance

Connected Azure Local deployments support intermittent disconnections of up to 30 days without impacting running workloads ([source](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/azure-local/connected-operations-overview#what-does-connected-mean)). This tolerance covers temporary connectivity loss, such as an ISP outage or a planned network maintenance window.

That 30-day tolerance is not the same as disconnected operations. A connected deployment still expects periodic Azure connectivity. A disconnected deployment uses a local control plane and has separate eligibility, hardware, and operating requirements.

## What needs connectivity

Connected operations use Azure connectivity for control plane tasks. The exact services depend on your design, but the common categories are:

| Connectivity use | What Azure provides |
| --- | --- |
| Management | Azure portal, Azure CLI, Azure Resource Manager templates, and Azure Arc views of Azure Local resources. |
| Governance | Azure role-based access control, Azure Policy, resource organization, and tags. |
| Monitoring | Azure Monitor, Log Analytics, alerts, and fleet visibility when the environment can send telemetry. |
| Security | Microsoft Defender for Cloud recommendations and posture management where enabled. |
| Lifecycle | Azure-coordinated deployment, update, scaling, and hardware solution validation workflows. |
| Billing | Azure Local per-physical-core billing through the Azure subscription, unless an eligible benefit or OEM license changes the billing treatment. |

Azure Local also requires outbound HTTPS connectivity to Azure endpoints at least every 30 days for connected hyperconverged deployments ([source](https://learn.microsoft.com/azure/azure-local/overview/hyperconverged-overview?view=azloc-2609#what-you-need-to-get-started-with-azure-local)).

## What stays local

Connected operations are designed to keep workload execution on-premises. Application owners should understand the boundary:

- VM disks, application databases, files, and container workloads run on Azure Local hardware.
- Storage Spaces Direct or SAN-backed storage serves workload storage locally.
- East-west traffic between local workloads stays inside the local network unless the application is designed to call external services.
- Azure receives management data, inventory, health, metrics, logs, and configuration data needed for the enabled Azure services.

This split is useful for sovereignty. You can use Azure management services without moving the primary workload data plane to Azure public cloud. You still need to review logs, telemetry, backup, and support processes because those can carry metadata or selected data depending on the services you enable.

## Connected deployment types

Connected operations support the broadest set of deployment types. The deployment type guide lists connected paths for hyperconverged, disaggregated, multi-rack, and small form factor deployments ([source](https://learn.microsoft.com/azure/azure-local/plan/find-your-deployment-type?view=azloc-2609#recommended-documentation-path)).

Connected is also the only connectivity mode for multi-rack and small form factor in the current deployment type guide. Disconnected operations are listed only for hyperconverged and disaggregated deployment paths ([source](https://learn.microsoft.com/azure/azure-local/plan/find-your-deployment-type?view=azloc-2609#overview)).

## Update planning

Connected systems must still stay current. Azure Local follows the Modern Lifecycle Policy, and systems must stay within six months of the most recent release to remain supported ([source](https://learn.microsoft.com/azure/azure-local/update/about-updates-23h2?view=azloc-2609#lifecycle-cadence)). The update article lists monthly cumulative updates, semi-annual feature updates, hotfixes as needed, and Solution Builder Extension updates as needed.

Azure Arc resource bridge has a related lifecycle requirement. Microsoft Learn says solution updates must be applied within one year to keep certificates valid and Azure Local VM functionality working ([source](https://learn.microsoft.com/azure/azure-local/update/about-updates-23h2?view=azloc-2609#lifecycle-cadence)).

## When connected operations fit

Connected operations fit when the environment can permit periodic outbound Azure connectivity and wants Azure-based management. Common reasons include centralized fleet visibility, update orchestration, Azure policy governance, Azure Monitor, Microsoft Defender for Cloud, Azure Backup, or Azure Site Recovery.

Use disconnected operations instead when policy or regulation prevents connectivity to Azure public cloud, or when the control plane itself must remain inside the local sovereign boundary.

## Sources

- [Connected operations overview](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/azure-local/connected-operations-overview)
- [What are hyperconverged deployments of Azure Local?](https://learn.microsoft.com/azure/azure-local/overview/hyperconverged-overview?view=azloc-2609)
- [Find your Azure Local deployment type](https://learn.microsoft.com/azure/azure-local/plan/find-your-deployment-type?view=azloc-2609)
- [About updates for Azure Local](https://learn.microsoft.com/azure/azure-local/update/about-updates-23h2?view=azloc-2609)
