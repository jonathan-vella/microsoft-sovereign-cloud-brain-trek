---
title: "Cost estimation"
description: "Structure sovereign solution cost models with Azure Local billing, OEM licensing, Azure Hybrid Benefit, Arc charges, and partner costs."
lastVerified: 2026-10-02
sidebar:
  order: 4
---

Cost estimation for sovereign solutions should show cost drivers and billing models without inventing prices. Use the [Azure pricing page](https://azure.microsoft.com/pricing/) and the [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator/) for current Azure prices, then add hardware and partner quotes.

## Cost model structure

Use the same cost categories across proposals so reviewers can compare options.

| Category | What to include | Who confirms it |
| --- | --- | --- |
| Hardware | Azure Local machines, storage, network, GPUs, racks, spare parts, management cluster hardware, and warranty | OEM or hardware partner |
| Azure Local subscription or license | Per-physical-core host billing, OEM license, or Azure Hybrid Benefit | Microsoft account team, licensing partner, or Azure pricing page |
| Guest operating systems | Windows Server guest VMs, Linux subscriptions, Windows Server Pay-as-you-go via Arc, or OEM license coverage | Licensing partner |
| Azure services | Azure Monitor, Defender for Cloud, Azure Backup, Azure Site Recovery, Log Analytics, key services, and other metered services | Azure pricing calculator |
| AKS and Kubernetes operations | AKS on Azure Local design work, Arc-enabled Kubernetes extensions, GPU node pools, observability, and support | Microsoft, partner, and Azure pricing calculator |
| Microsoft 365 Local | Microsoft 365 Local partner engagement, hardware architecture, Exchange Server, SharePoint Server, Skype for Business Server, and support model | Microsoft 365 Local certified partner |
| AI services | Foundry Local preview deployment, GPU hardware, model cache storage, Agentic Retrieval preview deployment, and model endpoint capacity | Microsoft account team and OEM partner |
| Support | Microsoft support plan, OEM support, managed services, and Standard or higher support for disconnected operations | Microsoft account team and partner |
| Implementation | Assessment, design, migration, test, security validation, documentation, and training | Services partner |

Do not compare options with made-up prices. If a number does not come from a pricing page, quote, contract, or measured run rate, label it as an assumption.

## Azure Local billing options

[Azure Local is priced per physical core on on-premises machines, plus consumption charges for extra Azure services](https://learn.microsoft.com/azure/azure-local/overview/hyperconverged-overview). Charges roll up to the existing Azure subscription.

There are three common host cost models:

| Model | Use when | Key constraint |
| --- | --- | --- |
| Azure subscription billing | Customer uses monthly Azure billing for Azure Local host cores and consumption services | Physical core count drives the host fee. Other Azure services bill separately. |
| Azure Hybrid Benefit for Azure Local | Customer has Windows Server Datacenter licenses with active Software Assurance | [Supported only for hyperconverged, cloud-connected, no-external-storage L1 deployments](https://learn.microsoft.com/azure/azure-local/concepts/azure-hybrid-benefit). L2 and L3 external-storage deployments are not supported. |
| OEM license for Azure Local | Customer buys eligible Azure Local hardware with the OEM license | [Valid for hardware lifetime, covers up to 16 cores with two-core and four-core add-ons, and includes Azure Local, Windows Server Datacenter 2025 guest VMs, and AKS enabled by Azure Arc](https://learn.microsoft.com/azure/azure-local/oem-license). |

Azure Hybrid Benefit waives the Azure Local host service fee and Windows Server guest subscription on the system. Other Azure services still bill as usual.

## OEM license rules

The OEM license simplifies procurement when the customer buys supported hardware through the hardware channel. Include these rules in the commercial assumptions:

- The license remains valid for the lifetime of the hardware.
- It covers up to 16 cores, with extra two-core and four-core add-ons.
- It includes Azure Local, Windows Server Datacenter 2025 guest VMs, and AKS enabled by Azure Arc.
- It is sold through hardware partners.
- All nodes in an Azure Local instance need uniform hardware, operating system, and billing treatment.

[Mixed-node scenarios are not supported for OEM licensing](https://learn.microsoft.com/azure/azure-local/oem-license). Do not mix OEM-licensed nodes and monthly billed nodes in one Azure Local instance.

## Arc costs and layered services

[Azure Arc control plane functions are offered at no extra cost](https://learn.microsoft.com/azure/azure-arc/overview#pricing) for core functions such as resource organization with management groups and tags, Azure Resource Graph search and indexing, Azure RBAC, templates, and extensions.

Layered services bill separately. Include each service the design uses:

- Microsoft Defender for Cloud.
- Azure Monitor and Log Analytics.
- Microsoft Sentinel.
- Azure Backup and Azure Site Recovery.
- Azure Policy or configuration services where pricing applies.
- Arc-enabled data services.

[Windows Server Pay-as-you-go through Azure Arc](https://learn.microsoft.com/azure/azure-arc/servers/cloud-native/licensing-cost-management) is available for Windows Server 2025 and later. It bills through Azure, uses per-core hourly charges, and does not require product keys or client access licenses for base functionality. Use it when the customer wants subscription licensing for eligible servers instead of perpetual licensing.

## Disconnected operations cost considerations

Disconnected operations changes the cost model because it adds a local management cluster and support prerequisites.

Include:

- Dedicated management cluster hardware. Production needs three dedicated nodes, isolated from workload clusters.
- Standard or higher Microsoft support plan, because disconnected operations eligibility requires it.
- OEM or partner implementation effort for disconnected deployment and lifecycle.
- Expansion pack and artifact handling processes for disconnected services.
- Extra testing for update, repair, backup, and break-glass operations.

Do not bury the management cluster inside general "platform overhead". It is a separate hardware and lifecycle line item.

## Microsoft 365 Local cost considerations

Microsoft 365 Local is generally available, but [the Learn page directs customers to deploy through a Microsoft 365 Local solution partner certified by Microsoft](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/m365-local/microsoft-365-local-overview). The cost model should include:

- Azure Local Premier Solution hardware.
- Partner assessment and design.
- Exchange Server, SharePoint Server, and Skype for Business Server Subscription Edition planning.
- Identity, backup, disaster recovery, and monitoring design.
- Connected or disconnected control plane choice.
- Support, update, and operating model.

Do not quote Microsoft 365 Local licensing from memory. Route licensing through the certified partner and Microsoft account team.

## AI cost considerations

Foundry Local on Azure Local and Agentic Retrieval in Foundry Local are preview. Cost models for preview services should be scoped as proof-of-concept or controlled deployment estimates until the account team confirms availability and commercial terms.

Include:

- GPU hardware and warranty.
- CPU worker nodes and storage for model cache.
- Foundry Local gateway, certificate, and Kubernetes dependencies.
- Agentic Retrieval CPU and embedding GPU workers.
- Separate language model endpoint capacity, such as GPT-OSS-20B on Foundry Local.
- Data source storage, NFS, ingestion, and document-preparation work.

Avoid unit prices such as cost per query unless they come from measured load tests and approved financial inputs.

## Proposal cost table

Use a table like this in customer proposals:

| Cost line | Billing basis | Source | Status |
| --- | --- | --- | --- |
| Azure Local host | Physical cores, OEM license, or Azure Hybrid Benefit | Azure pricing page, OEM quote, or licensing review | Pending quote |
| Hardware | Nodes, storage, network, GPU, management cluster | OEM or partner quote | Pending quote |
| Azure services | Consumption | Azure pricing calculator | Estimate |
| Windows Server guests | OEM coverage, Azure Hybrid Benefit, existing licenses, or PAYG via Arc | Licensing review | Pending decision |
| Microsoft 365 Local | Partner-led architecture and licensing | Certified partner | Pending partner scope |
| Foundry Local and Agentic Retrieval | Preview deployment, GPU, storage, and implementation | Account team and partner | Preview risk |
| Support | Microsoft, OEM, and managed services | Contract or support plan | Pending |

## Cost review checks

Before presenting the estimate, verify:

- No invented prices, discounts, or savings percentages appear in the model.
- Each Azure price points to Azure pricing pages or the pricing calculator.
- Hardware, Microsoft 365 Local, and support costs point to partner or account-team confirmation.
- Azure Hybrid Benefit is used only for eligible hyperconverged, cloud-connected, no-external-storage deployments.
- OEM licensing is not mixed with another billing model inside one Azure Local instance.
- Disconnected operations includes the dedicated management cluster and support plan.
- Preview services are marked as preview with commercial assumptions still pending.

## Sources

- [What are hyperconverged deployments of Azure Local?](https://learn.microsoft.com/azure/azure-local/overview/hyperconverged-overview)
- [Azure Hybrid Benefit for Azure Local](https://learn.microsoft.com/azure/azure-local/concepts/azure-hybrid-benefit)
- [OEM license for Azure Local overview](https://learn.microsoft.com/azure/azure-local/oem-license)
- [Azure Arc overview](https://learn.microsoft.com/azure/azure-arc/overview)
- [Cloud-native licensing and cost management with Arc-enabled servers](https://learn.microsoft.com/azure/azure-arc/servers/cloud-native/licensing-cost-management)
- [Disconnected operations for Azure Local](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview)
- [Dedicated management cluster for disconnected operations](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-control-plane-appliance)
- [What is Microsoft 365 Local?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/m365-local/microsoft-365-local-overview)
- [Requirements for Foundry Local on Azure Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-requirements)
- [What you need for Agentic Retrieval in Foundry Local](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/requirements)
- [Azure pricing](https://azure.microsoft.com/pricing/)
- [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator/)
