---
title: "Azure Local disconnected operations"
description: "Design Azure Local disconnected operations with a local control plane, management cluster, PKI, identity, updates, and workload support."
lastVerified: 2026-10-02
sidebar:
  order: 5
---

Disconnected operations move selected Azure control-plane functions into the customer environment. Azure Local workloads and the local management plane run without a connection to Azure public cloud. Use this model when regulation, classification, remote operations, or network isolation prevents periodic connectivity to Azure.

![Disconnected operations: a management cluster hosts the local control plane and manages Azure Local workload instances inside the customer boundary, with no connection to Azure](/images/level-300/azure-local-disconnected-operations-2026.svg)

Microsoft introduced disconnected operations as a preview in the 2411 release. The current disconnected operations page states that [the feature requires Azure Local 2602 or later](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview?view=azloc-2609), and the February 24, 2026 Microsoft blog described "Azure Local disconnected operations" as now available. AKS under disconnected operations remains preview.

## What runs locally

Disconnected operations provide a local Azure portal and Azure CLI experience through a local control plane. The supported-services table lists Azure portal, Azure Resource Manager, role-based access control, managed identity, Arc-enabled servers, Azure Local VMs, Arc-enabled Kubernetes clusters in preview, AKS enabled by Arc for Azure Local in preview, Azure Local device management, Azure Container Registry, Azure Key Vault, and Azure Policy.

The architecture has two kinds of Azure Local clusters:

- A dedicated management cluster that hosts the disconnected operations appliance and local control plane.
- One or more workload clusters that run Azure Local VMs, AKS on Azure Local in preview, Microsoft 365 Local, and other supported workloads.

Keep those clusters separate. Microsoft states that production deployments require a dedicated three-node Azure Local management cluster and that tenant workloads should not run on that management cluster.

## Eligibility and acquisition

Disconnected operations is not a self-service feature for every subscription. Microsoft lists these eligibility criteria:

| Criterion | Requirement |
| --- | --- |
| Agreement | Eligible Microsoft agreement. The Microsoft online subscription program is not eligible. |
| Support | Active Standard or higher support plan with Microsoft, or a partner with an active support plan. |
| Business need | A valid need to operate without Azure connectivity because of connectivity or regulatory restrictions. |
| Operations | Staff or partner capability to deploy and operate disconnected operations. |
| Hardware | Azure Local Premier Solutions, dedicated management cluster, and supported configurations from the Azure Local catalog. |

Access is requested through the disconnected operations prequalification process. Microsoft says customers receive an approved, rejected, queued, or need-more-information notification within 10 business days.

## Deployment types and workload support

Disconnected operations is a connectivity model layered on Azure Local. It is supported with hyperconverged and disaggregated deployment types, not multi-rack or small form factor. The general Azure Local deployment-type page lists disconnected operations support for hyperconverged and disaggregated deployments only.

The supported workload picture is narrower than connected Azure Local:

| Workload or service | Disconnected operations status |
| --- | --- |
| Azure Local VMs | Supported through disconnected operations. |
| Azure Container Registry | Supported locally for container images and artifacts. |
| Azure Key Vault | Supported for local key vault management. |
| Azure Policy | Supported for standards and governance when creating resources. |
| Arc-enabled Kubernetes clusters | Preview. |
| AKS enabled by Arc for Azure Local | Preview. |
| Microsoft 365 Local disconnected | Now available, according to the February 24, 2026 Microsoft blog. |
| Foundry Local disconnected | Supported in preview and requires Azure Local disconnected operations 2604.3.0 or later. |

For AKS, do not state or imply general availability in disconnected operations. Microsoft labels AKS on Azure Local with disconnected operations as preview.

## Management cluster sizing

The management cluster hosts the local control plane, so it is not optional infrastructure. Microsoft documents two production hardware configurations:

| Configuration | Minimum nodes | Per-node memory | Per-node cores | Storage | Scale target |
| --- | --- | --- | --- | --- | --- |
| Standard | 3 | 128 GB | 24 physical cores | 6 drives, 2 TB or larger each | 100 or more nodes |
| Datacenter | 3 | 512 GB | 24 physical cores | 8 drives, 2 TB or larger each | 1000 or more nodes |

Evaluation can use a four-node Azure Local hardware configuration arranged in one of three proof-of-concept layouts: management-focused, workload-focused, or multi-cluster-focused. Microsoft still recommends the production-style configuration even for proof-of-concept work when possible.

Architects should reserve management-cluster headroom for updates, node repair, appliance lifecycle operations, and local portal availability. Do not size the management cluster as a general compute pool.

## Identity and PKI

Disconnected operations integrates with local identity. Microsoft documents Active Directory for groups and memberships and AD FS for authentication. Only Universal groups are supported for Active Directory group memberships. The deployment identifies a root operator, operator subscription, and operator role assignments for local operations.

PKI is a first-order dependency. [Disconnected operations PKI guidance](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-pki?view=azloc-2609) says certificates must come from a public CA or enterprise CA and be part of the Microsoft Trusted Root Program. For fully disconnected deployments, use a private or internal CA. Microsoft states that public or external CA certificates fail in fully disconnected deployments because CRL and OCSP services require internet connectivity.

Plan these certificate categories before deployment:

- Ingress endpoint certificates for the local appliance services.
- Management endpoint server and client certificates.
- Root certificate export in Base64 encoded format.
- LDAPS and OIDC certificate chain information for identity integration.
- CRL endpoints that are reachable from the disconnected operations infrastructure.

## Updates and servicing

Disconnected operations uses offline or staged update workflows. The disconnected update page says operators download the update from the Azure portal, verify files such as `Docker.wim`, `OS.wim`, `Package.zip`, `EFI.wim`, `Manifest.xml`, `OperationsModule.zip`, and `Notice.txt`, copy them to the seed node, load the OperationsModule, upload the update package, wait for staging, store BitLocker keys, and then start the appliance update.

The documented trigger command is:

```powershell
Start-ApplianceUpdate -TargetVersion $updatePackageResult.UpdatePackageVersion -Wait
```

Microsoft warns that updates can take several hours and might reboot the control plane appliance. If an update fails, the system attempts to roll back to the last known good state.

Azure Local node updates in disconnected environments also have version-specific requirements. For example, Microsoft documents a required sequence when updating from Azure Local 2602 to 2604: update disconnected operations from 2602 to 2604, then update Azure Local from 2602 to 2603, then update Azure Local from 2603 to 2604. Keep appliance version, Azure Local build, and target solution version aligned.

## Disconnected operations versus connected operations

| Design area | Connected operations | Disconnected operations |
| --- | --- | --- |
| Control plane | Azure control plane with periodic connectivity. | Local appliance and local portal experience. |
| Connectivity tolerance | Up to 30 days of Azure disconnection without affecting running workloads. | No ongoing Azure connection required. |
| Identity | Azure and connected identity services. | Active Directory and AD FS integration. |
| Updates | Azure Local update workflow through Azure portal or PowerShell. | Offline or staged download, transfer, upload, staging, and appliance update. |
| PKI | Platform and Arc certificates managed through connected lifecycle processes. | Customer PKI for appliance endpoints, management endpoints, and identity trust. |
| Best fit | Sites that can periodically connect to Azure. | Sovereign, classified, regulated, remote, or isolated environments. |

Do not use connected operations with a plan to "just disconnect longer." The connected tolerance is a short-term continuity feature. If no Azure connectivity is allowed by design, use disconnected operations and plan the local control plane.

## Planning checklist

- Confirm eligibility and approval before final architecture commitments.
- Reserve separate hardware for the management cluster.
- Keep management and workload clusters isolated.
- Select only supported deployment types.
- Mark AKS and Arc-enabled Kubernetes under disconnected operations as preview.
- Build the PKI hierarchy, CRL reachability, and certificate rotation runbooks before deployment.
- Document identity, operator roles, and recovery for lost operator access.
- Store BitLocker recovery keys before updates.
- Plan offline update transfer, staging, rollback, and support procedures.
- Confirm whether Foundry Local disconnected requires disconnected operations 2604.3.0 or later for the planned version.

## Sources

- [Disconnected operations for Azure Local](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview?view=azloc-2609)
- [Dedicated management cluster for disconnected operations](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-control-plane-appliance?view=azloc-2609)
- [Public key infrastructure for disconnected operations on Azure Local](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-pki?view=azloc-2609)
- [Plan your identity for disconnected operations on Azure Local](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-identity?view=azloc-2609)
- [About updates for disconnected operations](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-update?view=azloc-2609)
- [Find your Azure Local deployment type](https://learn.microsoft.com/azure/azure-local/plan/find-your-deployment-type?view=azloc-2609)
- [AKS on Azure Local with disconnected operations](https://learn.microsoft.com/azure/aks-hybrid-edge/local/disconnected-operations/overview)
- [What's new in Foundry Local on Azure Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/whats-new)
- [What is Microsoft 365 Local?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/m365-local/microsoft-365-local-overview)
- [Microsoft Sovereign Cloud adds governance, productivity and support for large AI models securely running even when completely disconnected](https://blogs.microsoft.com/blog/2026/02/24/microsoft-sovereign-cloud-adds-governance-productivity-and-support-for-large-ai-models-securely-running-even-when-completely-disconnected/)
