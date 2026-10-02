---
title: "Disconnected operations design"
description: "Plan Azure Local disconnected operations, including the local control plane, eligibility, supported services, identity, DNS, PKI, and update model."
lastVerified: 2026-10-02
sidebar:
  order: 2
---

Disconnected operations move selected Azure control-plane functions into the customer environment. Use this model only when the customer has a validated need to operate without Azure public cloud connectivity. The extra planning work is real because the local control plane becomes part of the customer's production platform.

## Start with eligibility

Microsoft documents disconnected operations as a procured capability with eligibility requirements, not as a toggle in an Azure Local deployment wizard. To be eligible, the customer needs an eligible Microsoft agreement, a Standard or higher support plan, a valid business need to operate disconnected, operational readiness, supported customer-owned hardware, and a dedicated management cluster. The Microsoft online subscription program, or MOSA, is not eligible ([Learn](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview#eligibility-criteria)).

The customer or account team completes the prequalification form and receives a status within 10 business days. The response may be approved, rejected, queued, or need more information ([Learn](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview#get-started)).

Use eligibility as a design gate. If the environment can operate with connected operations and tolerate outages within the documented 30-day limit, disconnected operations may add cost and complexity without solving a requirement.

## Design the management cluster as production infrastructure

Disconnected operations require a separate Azure Local management cluster that hosts the local control plane. Microsoft says the management cluster must be dedicated to control plane and management components, isolated from application or tenant workload clusters, and sized for the disconnected operations appliance ([Learn](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-control-plane-appliance)).

Production deployments require a dedicated three-node management cluster. Evaluation and test topologies can use smaller management clusters, but do not carry that pattern into production without an approved design.

| Configuration | Minimum nodes | Per-node memory | Per-node cores | Per-node storage | Use |
| --- | --- | --- | --- | --- | --- |
| Standard | 3 | 128 GB | 24 physical cores | 6 drives, minimum 2 TB each, plus 960 GB boot drive | Medium deployments, 100 or more nodes |
| Datacenter | 3 | 512 GB | 24 physical cores | 8 drives, minimum 2 TB each, plus 960 GB boot drive | Large datacenter scale, 1000 or more nodes |

Microsoft recommends starting hardware procurement from the Azure Local catalog and selecting solutions marked for disconnected operations. The management cluster should use supported Azure Local hardware from the catalog. Plan capacity headroom for updates, repair, and lifecycle operations, and do not use the management cluster as a general-purpose compute pool.

For proof of concept work, Microsoft documents a four-node hardware configuration with three options. A management-focused POC uses a three-node management cluster and one workload node. A workload-focused POC uses a one-node management cluster and a three-node workload cluster or a single workload node. A multi-cluster-focused POC uses a one-node management cluster and three one-node workload clusters ([Learn](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-control-plane-appliance#proof-of-concept-configurations)).

## Understand the local service set

Disconnected operations provide a subset of Azure capabilities. Microsoft lists the supported services in the disconnected operations overview. Some are core control-plane services, some are infrastructure services, and Kubernetes-related services are preview.

| Status | Services |
| --- | --- |
| Supported | Azure portal, Azure Resource Manager, RBAC, system-assigned managed identity where supported, Arc-enabled servers, Azure Local VMs, Azure Local device management, Azure Container Registry, Azure Key Vault, Azure Policy |
| Preview | Arc-enabled Kubernetes clusters and Azure Kubernetes Service enabled by Arc for Azure Local |

Do not describe AKS disconnected operations as generally available. The Azure Local disconnected operations feature is available for Azure Local 2602 or later, but the supported-services table labels Arc-enabled Kubernetes and AKS enabled by Arc for Azure Local as preview ([Learn](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview#supported-services)).

Microsoft's February 24, 2026 blog states that Azure Local disconnected operations and Microsoft 365 Local disconnected are now available ([Microsoft Blog](https://blogs.microsoft.com/blog/2026/02/24/microsoft-sovereign-cloud-adds-governance-productivity-and-support-for-large-ai-models-securely-running-even-when-completely-disconnected/)). Use Learn for the service table and status details, and use the blog for announcement context.

## Plan identity before deployment

Disconnected operations integrate with an existing identity and access management solution. Learn lists Active Directory for groups and memberships and Active Directory Federation Services for authentication. Only Universal groups are supported for Active Directory group memberships ([Learn](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-identity)).

During deployment, the operator specifies a Root operator. That user owns an operator subscription and adds other operators after deployment. The OpenID Connect endpoint authenticates users, and the LDAP endpoint integrates groups and memberships. Role assignments and policies do not inherit from the operator subscription to individual subscriptions. Each subscription has its own scope.

At design time, collect the identity endpoints and inputs:

| Input | Design note |
| --- | --- |
| LDAP endpoint | Provide IP addresses or FQDNs. If you use an FQDN, DNS must resolve it from the disconnected operations appliance. |
| Login endpoint | Provide the AD FS or OIDC endpoint and certificate chain information. |
| Read-only LDAP account | Used for LDAP v3 group and membership integration. |
| Root group | Defines the start point for membership synchronization. |
| Initial operator UPN | Assigned as the Root operator during setup. |
| Certificate chain information | Provide LDAPS and OIDC certificate chain information for identity endpoint trust. |

The initial synchronization can take up to six hours. After that, synchronization runs periodically. Design operator onboarding and break-glass procedures around that delay.

## Plan DNS, ingress, and PKI together

The disconnected operations appliance uses management and ingress vNICs. The ingress IP must be in the same subnet as the Azure Local instance and outside the reserved IP range used during deployment. External services need to resolve and route to the disconnected operations ingress IP on port 443 ([Learn](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-network)).

DNS needs an explicit zone for the FQDN dedicated to the disconnected operations environment. Learn says the FQDN cannot be on the same level as the domain controller. The zone must resolve wildcard endpoints for dynamically created services, such as Azure Key Vault and Azure Container Registry ([Learn](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-network#dns-requirements)).

PKI secures the endpoints exposed by the appliance. Certificates must come from a public certificate authority or enterprise certificate authority and be part of the Microsoft Trusted Root Program. For fully disconnected deployments, use a private or internal certificate authority. Self-signed certificates are not supported. Learn also states that fully disconnected deployments should not use a public or external CA because CRL and OCSP checks would require internet connectivity ([Learn](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-pki)).

Plan certificate ownership early. The required ingress endpoint certificates include wildcard certificates for Blob storage, Container Registry, queue storage, Service Bus, table storage, Key Vault, and named certificates for Azure Resource Manager, Graph, portal, login, and other appliance services. Management endpoints require server and client certificates.

## Plan updates and offline operations

In disconnected operations, Microsoft says updates, servicing, and onboarding use offline or staged workflows. Operators handle identity, monitoring, and access control locally through supported on-premises integrations. The control plane runs locally and is operated on-premises ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/azure-local/disconnected-operations-overview)).

That model changes operational ownership. The customer must maintain local runbooks for appliance health, identity synchronization, certificate renewal, DNS changes, expansion pack import, model or container registry population, and support diagnostics. If the appliance runs in limited connectivity mode, it can resolve selected Microsoft endpoints for observability and diagnostics. If it is fully disconnected, plan export and import workflows for support data.

## Place workloads that need disconnected support

Microsoft 365 Local is a key disconnected workload. Learn states that it supports both hybrid and fully disconnected deployments ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/m365-local/microsoft-365-local-overview)). The February 24, 2026 Microsoft blog states Microsoft 365 Local disconnected is now available ([Microsoft Blog](https://blogs.microsoft.com/blog/2026/02/24/microsoft-sovereign-cloud-adds-governance-productivity-and-support-for-large-ai-models-securely-running-even-when-completely-disconnected/)).

Foundry Local on Azure Local supports disconnected environments while in preview. The June 2026 Foundry Local release added disconnected environment operations, and the disconnected architecture page explains that extension components, catalog models, and dependencies are imported through expansion packs into the local EdgeArtifacts registry ([What's new](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/whats-new#june-2026), [disconnected overview](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/disconnected-operations/concept-overview)). For disconnected Foundry Local designs, use Azure Local disconnected operations 2604.3.0 or later when you follow the current planning guidance ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-requirements#connected-and-disconnected-implications)).

Agentic Retrieval also supports disconnected deployments in preview. Its overview says it can run in disconnected environments by using a locally imported expansion pack and no internet connectivity at deployment time ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/overview)). Keep status language precise because both Agentic Retrieval and Foundry Local on Azure Local are preview.

## Sources

- [Disconnected operations for Azure Local](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview)
- [Dedicated management cluster for disconnected operations](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-control-plane-appliance)
- [Plan your identity for disconnected operations on Azure Local](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-identity)
- [Plan your network for disconnected operations on Azure Local](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-network)
- [Public key infrastructure for disconnected operations on Azure Local](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-pki)
- [Disconnected operations overview](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/azure-local/disconnected-operations-overview)
- [What is Microsoft 365 Local?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/m365-local/microsoft-365-local-overview)
- [What's new in Foundry Local on Azure Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/whats-new)
- [Requirements for Foundry Local on Azure Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-requirements)
- [Foundry Local on Azure Local in disconnected environments overview](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/disconnected-operations/concept-overview)
- [What is Agentic Retrieval in Agents and Tools with Foundry Local?](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/overview)
- [Microsoft Sovereign Cloud adds governance, productivity and support for large AI models securely running even when completely disconnected](https://blogs.microsoft.com/blog/2026/02/24/microsoft-sovereign-cloud-adds-governance-productivity-and-support-for-large-ai-models-securely-running-even-when-completely-disconnected/)
