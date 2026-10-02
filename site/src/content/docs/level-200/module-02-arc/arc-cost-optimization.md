---
title: "Arc cost optimization"
description: "Plan Azure Arc cost ownership with free control-plane capabilities, paid layered services, Windows Server licensing, ESU, and governance controls."
lastVerified: 2026-10-02
sidebar:
  order: 4
---

Azure Arc cost optimization starts by separating the free control plane from the Azure services layered on top of Arc resources. Do not estimate Arc costs by counting connected resources alone. Estimate the services, data, licensing, and network paths each resource uses.

## Know what is included

The Azure Arc overview states that several Azure Arc-enabled server control-plane capabilities are offered at no extra cost, including resource organization through management groups and tags, search and indexing through Azure Resource Graph, RBAC, and templates and extensions ([Learn](https://learn.microsoft.com/azure/azure-arc/overview#pricing)).

For Azure Arc-enabled VMware vSphere and SCVMM, the same overview says discovery, inventory, VM lifecycle operations, power operations, RBAC delegation, and management through portal, CLI, REST APIs, SDKs, and infrastructure-as-code templates are offered at no extra cost. Azure services used with those resources, such as Microsoft Defender for Cloud or Azure Monitor, are charged according to the pricing for those services ([Learn](https://learn.microsoft.com/azure/azure-arc/overview#pricing)).

Use this cost model:

| Layer | Cost planning question |
| --- | --- |
| Arc control plane | Is the activity included, such as tags, RBAC, inventory, extensions framework, or resource projection? |
| Attached Azure service | Does the resource use Azure Monitor, Defender for Cloud, Microsoft Sentinel, Update Manager, machine configuration, Automation, Key Vault, Private Link, or another billed service? |
| Data volume | How much log, metric, change tracking, inventory, and security data is ingested or retained? |
| Licensing | Is the server using Windows Server pay-as-you-go, SQL Server pay-as-you-go, ESU through Arc, or existing license attestation? |
| Network | Does the design use Private Link endpoints, ExpressRoute, VPN, egress filtering, or data export that has its own billing model? |

For prices, link customers to current pricing pages instead of copying numbers into training material. Pricing changes by region, service tier, reservation, licensing entitlement, and data volume.

## Treat linked services as the main cost driver

The Cloud Adoption Framework cost governance page for Arc-enabled servers is deprecated and scheduled for removal on October 30, 2026, but it clearly states the cost boundary: Arc control-plane functionality is provided at no extra cost, while Azure services used with Arc-enabled servers incur costs according to their usage ([Learn](https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/hybrid/arc-enabled-servers/eslz-cost-governance)). The deprecation is a documentation lifecycle note, not a product retirement.

Common linked services include:

| Service | Cost driver to watch | Pricing source |
| --- | --- | --- |
| Azure Monitor | Log ingestion, retention, export, alerts, and workspace design. | [Azure Monitor pricing](https://azure.microsoft.com/pricing/details/monitor/) |
| Microsoft Defender for Cloud | Defender plan selection and covered server count. | [Microsoft Defender for Cloud pricing](https://azure.microsoft.com/pricing/details/azure-defender/) |
| Microsoft Sentinel | Data ingestion, retention, analytics, and automation. | [Microsoft Sentinel pricing](https://azure.microsoft.com/pricing/details/azure-sentinel/) |
| Azure Update Manager | Arc server update management usage and eligibility through Windows Server benefits. | [Azure Update Manager pricing](https://azure.microsoft.com/pricing/details/azure-update-management-center/) |
| Machine configuration | Policy evaluation and guest configuration usage unless included through Windows Server Management enabled by Azure Arc. | [Azure Policy pricing](https://azure.microsoft.com/pricing/details/azure-policy/) |
| Private Link | Private endpoint and data processing. | [Private Link pricing](https://azure.microsoft.com/pricing/details/private-link/) |

When an Arc design looks expensive, first inspect data volume and service attachment. Common causes are broad log collection, duplicate monitoring tools, Defender plans enabled beyond the intended scope, and long retention defaults copied from security workloads into operational workspaces.

## Use Windows Server licensing paths intentionally

Windows Server pay-as-you-go through Azure Arc is available for Windows Server 2025 and later. Microsoft describes it as a per-core, per-hour Azure billing model that does not require product keys or client access licenses for base functionality ([Learn](https://learn.microsoft.com/azure/azure-arc/servers/cloud-native/licensing-cost-management#windows-server-pay-as-you-go)).

Use it for variable or short-lived servers where consumption billing is cleaner than buying perpetual licenses. Do not use it as a blanket recommendation for every server. A customer with existing Software Assurance or subscription licenses may instead attest eligible servers for Windows Server Management enabled by Azure Arc benefits.

Windows Server Management enabled by Azure Arc gives eligible attested servers or Windows Server pay-as-you-go enrollees access to services such as Azure Update Manager, Change Tracking and Inventory, Azure Machine Configuration, Windows Admin Center in Azure for Arc, Remote Support, Network HUD, Best Practices Assessment, Azure Site Recovery configuration, and Azure File Sync benefits at no extra cost beyond linked networking, storage, and log ingestion costs ([Learn](https://learn.microsoft.com/azure/azure-arc/servers/windows-server-management-overview#billing)).

Record the chosen licensing path per server:

| Server category | Cost question |
| --- | --- |
| Windows Server 2025 and later without existing rights | Should Windows Server pay-as-you-go through Arc replace upfront licensing? |
| Server with Software Assurance or active subscription license | Has the customer attested eligibility for Windows Server Management enabled by Azure Arc benefits? |
| Down-level server nearing or past end of support | Is ESU through Arc needed, and when does billing start? |
| Non-Windows server | Which Arc-attached services are billed separately? |

## Plan ESU through Arc as a lifecycle cost

Extended Security Updates enabled by Azure Arc provide a pay-as-you-go monthly path for eligible Windows Server versions after end of support. Microsoft states that Windows Server 2012 and 2012 R2 reached end of support on October 10, 2023, Windows Server 2016 reaches end of support on January 12, 2027, and Windows Server 2016 ESU configuration in the Azure portal starts August 3, 2026, with billing beginning January 13, 2027 ([Learn](https://learn.microsoft.com/azure/azure-arc/servers/cloud-native/licensing-cost-management#extended-security-updates-esus)).

For cost planning, ESU is not a substitute for modernization. Treat it as a dated exception with a retirement plan:

1. Identify servers by operating system version and business owner.
2. Decide whether to migrate, upgrade, retire, or enroll in ESU.
3. Track ESU coverage in Azure.
4. Include ESU costs in the same showback view as Azure Monitor, Defender, and Sentinel.
5. Review exceptions quarterly.

## Retire Automanage assumptions

Azure Automanage Best Practices for Azure Arc-enabled servers is scheduled for retirement on September 30, 2027. Microsoft says creating a new configuration profile or onboarding a new subscription to the service will result in an error after retirement, and points customers toward migration to Azure Policy ([Learn](https://learn.microsoft.com/azure/automanage/automanage-arc)).

Do not build new cost models around Automanage onboarding. Use Azure Policy, machine configuration, Update Manager, and the Windows Server Management enabled by Azure Arc benefits path where those services fit.

## Use tags, budgets, and policy for cost control

Arc resources need the same FinOps basics as Azure-native resources:

| Control | What it prevents |
| --- | --- |
| Required tags | Unowned resources, missing chargeback keys, and unmanaged production assets. |
| Budgets and alerts | Month-end surprises for shared subscriptions or central Log Analytics workspaces. |
| Data collection rules | Over-collection of logs and metrics from servers that need only baseline monitoring. |
| Policy assignments | Unapproved extensions, missing cost tags, or services enabled outside the intended scope. |
| Workspace design | Mixing high-volume operational logs with security logs that need different retention. |

Use Azure Cost Management for Azure-billed services and join it with Arc tags. For on-premises infrastructure cost, use the customer's hardware and facilities accounting system. Arc does not make local hardware, virtualization, support contracts, or datacenter power costs appear in Azure billing unless the customer models them separately.

## Build a review rhythm

Monthly reviews should focus on changes:

| Review item | Question |
| --- | --- |
| New connected resources | Were they assigned the right tags, policies, and service attachments? |
| Log ingestion | Did any workspace have an unexpected spike? |
| Defender and Sentinel | Did plan or data source changes expand coverage beyond approved scope? |
| Update and configuration services | Are benefits through Windows Server Management enabled by Azure Arc reducing duplicate spend? |
| ESU | Are legacy servers on a dated migration or retirement plan? |
| Private Link and networking | Are private endpoints and circuits still required for each scope? |

The outcome of the review should be a small set of actions, not a dashboard screenshot. Good actions include removing duplicate agents, reducing noisy logs, fixing tags, splitting workspaces by retention need, and retiring servers that are connected only because no one owns the shutdown decision.

## Sources

- [Azure Arc overview](https://learn.microsoft.com/azure/azure-arc/overview#pricing)
- [Cost governance for Azure Arc-enabled servers](https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/hybrid/arc-enabled-servers/eslz-cost-governance)
- [Cloud-native licensing and cost management with Arc-enabled servers](https://learn.microsoft.com/azure/azure-arc/servers/cloud-native/licensing-cost-management)
- [Windows Server Management enabled by Azure Arc](https://learn.microsoft.com/azure/azure-arc/servers/windows-server-management-overview)
- [Azure Automanage for Machines Best Practices - Azure Arc-enabled servers](https://learn.microsoft.com/azure/automanage/automanage-arc)
- [Azure Monitor pricing](https://azure.microsoft.com/pricing/details/monitor/)
- [Microsoft Defender for Cloud pricing](https://azure.microsoft.com/pricing/details/azure-defender/)
- [Microsoft Sentinel pricing](https://azure.microsoft.com/pricing/details/azure-sentinel/)
- [Azure Update Manager pricing](https://azure.microsoft.com/pricing/details/azure-update-management-center/)
- [Azure Policy pricing](https://azure.microsoft.com/pricing/details/azure-policy/)
- [Private Link pricing](https://azure.microsoft.com/pricing/details/private-link/)
