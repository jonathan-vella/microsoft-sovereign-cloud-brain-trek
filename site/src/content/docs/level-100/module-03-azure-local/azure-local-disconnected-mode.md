---
title: "Azure Local disconnected operations"
description: "Learn how Azure Local disconnected operations use a local control plane, eligible agreements, Premier hardware, and selected Arc-enabled services for isolated environments."
lastVerified: 2026-10-02
sidebar:
  order: 4
---

## What disconnected operations means

Disconnected operations for Azure Local let an organization deploy and manage Azure Local instances without a connection to Azure public cloud. Microsoft Learn describes the feature as a way to use selected Azure Arc-enabled services from a local control plane while getting a familiar Azure portal and Azure CLI experience ([source](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview?view=azloc-2609#overview)).

Disconnected operations are generally available for Azure Local 2602 or later, as reflected in Microsoft Learn and the February 2026 Microsoft blog announcement that "Azure Local disconnected operations" are "now available" ([Learn source](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview?view=azloc-2609), [blog source](https://blogs.microsoft.com/blog/2026/02/24/microsoft-sovereign-cloud-adds-governance-productivity-and-support-for-large-ai-models-securely-running-even-when-completely-disconnected/)).

This mode is for environments where connectivity to Azure public cloud is not allowed or not practical. Examples include regulated sovereign environments, remote or isolated sites, and security-sensitive networks that need a smaller external attack surface.

## What works locally

Disconnected operations provide a local control plane for selected services. The supported-services table includes:

| Service area | Local capability |
| --- | --- |
| Azure portal and Azure Resource Manager | Local portal, subscriptions, resource groups, templates, and CLI. |
| Access control | Role-based access control for subscriptions and resource groups. |
| Identity for resources | System-assigned managed identity for resource types that support it. |
| Compute | Azure Local device management, Azure Local VMs, and Arc-enabled servers. |
| Containers | Arc-enabled Kubernetes clusters in preview and AKS enabled by Arc for Azure Local in preview. |
| Platform services | Azure Container Registry, Azure Key Vault, and Azure Policy for supported local scenarios. |

AKS on Azure Local with disconnected operations is preview. The AKS documentation has an explicit preview notice, and the Azure Local supported-services table labels both Arc-enabled Kubernetes clusters and AKS enabled by Arc for Azure Local as preview under disconnected operations ([AKS source](https://learn.microsoft.com/azure/aks-hybrid-edge/local/disconnected-operations/overview), [Azure Local source](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview?view=azloc-2609#supported-services)).

Microsoft 365 Local can also run in fully disconnected environments on Azure Local. [Module 6: Microsoft 365 Local](/level-100/module-06-microsoft-365-local/) covers that workload.

## Management cluster requirement

Disconnected operations need a dedicated management cluster that hosts the local control plane. Microsoft Learn states that production deployments require a dedicated three-node Azure Local management cluster and that tenant workloads must run on separate Azure Local clusters ([source](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-control-plane-appliance?view=azloc-2609#overview)).

This separation matters because the management cluster is not a general-purpose compute pool. It runs the control plane appliance and management services. Workload clusters host VMs and applications. Keeping them separate improves control plane availability and makes lifecycle operations more predictable.

The management cluster hardware page lists two production configurations. Both require three nodes and 24 physical cores per node. The standard configuration lists 128 GB memory per node and six drives of at least 2 TB per node. The datacenter configuration lists 512 GB memory per node and eight drives of at least 2 TB per node for larger environments ([source](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-control-plane-appliance?view=azloc-2609#management-cluster-hardware-requirements)).

## Eligibility basics

Disconnected operations are not a self-service toggle for every subscription. Microsoft Learn lists these eligibility criteria:

| Criterion | L100 explanation |
| --- | --- |
| Eligible agreement | You need an eligible Microsoft agreement. Microsoft online subscription program, or MOSA, is not eligible ([source](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview?view=azloc-2609#eligibility-criteria)). |
| Support plan | You need an active Microsoft support plan, Standard or higher, or a partner with an active support plan. |
| Business need | You need a valid business need for disconnected operation, such as regulatory restrictions or connectivity limits. |
| Operational readiness | Your organization or partner must be able to deploy and operate disconnected operations. |
| Hardware | Disconnected operations support Premier Solutions for Azure Local and require a dedicated management cluster. |

The access flow also has an approval step. Microsoft Learn states that after the prequalification form is submitted, the requester receives approved, rejected, queued, or needs-more-information status within 10 business days ([source](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview?view=azloc-2609#get-started)).

## How to position disconnected operations

Use disconnected operations when the control plane, operations, and selected Azure-like services must stay inside the local boundary. Do not position it as the default for every Azure Local deployment. It adds hardware, procurement, approval, operational, identity, network, PKI, monitoring, and update requirements.

For a connected environment that only needs resilience to temporary connectivity loss, use connected operations and design around the 30-day tolerance. For an environment that cannot depend on Azure public cloud at all, plan disconnected operations from the start.

## Sources

- [Disconnected operations for Azure Local](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview?view=azloc-2609)
- [Dedicated management cluster for disconnected operations](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-control-plane-appliance?view=azloc-2609)
- [AKS on Azure Local with disconnected operations (preview)](https://learn.microsoft.com/azure/aks-hybrid-edge/local/disconnected-operations/overview)
- [Find your Azure Local deployment type](https://learn.microsoft.com/azure/azure-local/plan/find-your-deployment-type?view=azloc-2609)
- [Microsoft Sovereign Cloud adds governance, productivity and support for large AI models securely running even when completely disconnected](https://blogs.microsoft.com/blog/2026/02/24/microsoft-sovereign-cloud-adds-governance-productivity-and-support-for-large-ai-models-securely-running-even-when-completely-disconnected/)
