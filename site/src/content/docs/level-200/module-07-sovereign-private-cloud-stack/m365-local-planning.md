---
title: "Microsoft 365 Local planning"
description: "Plan Microsoft 365 Local on Azure Local, including partner engagement, deployment type, reference architecture, connectivity, DR, and support commitments."
lastVerified: 2026-10-02
sidebar:
  order: 3
---

Microsoft 365 Local brings core productivity server workloads into the Sovereign Private Cloud boundary. Plan it as a partner-delivered Azure Local workload, not as a do-it-yourself lift of existing Exchange or SharePoint servers.

## Define what Microsoft 365 Local includes

Learn states that Microsoft 365 Local enables organizations to run Exchange Server, SharePoint Server, and Skype for Business Server on customer-owned and customer-managed Azure Local infrastructure ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/m365-local/microsoft-365-local-overview)). The product uses the Subscription Editions of those server products. The same Learn page states that Microsoft 365 Local is now generally available.

Microsoft 365 Local is built for organizations that need productivity services in a private-cloud environment with stronger control over data residency, access, and operations. It supports hybrid connectivity and fully disconnected deployments. In connected mode, the architecture uses Azure as the cloud-connected control plane. In disconnected mode, it uses a local control plane.

## Engage the right partner path

Microsoft requires Microsoft 365 Local deployment through a Microsoft 365 Local solution partner certified by Microsoft. The Learn deployment section describes a typical partner engagement as assessment, planning, acquisition, and deployment ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/m365-local/microsoft-365-local-overview#microsoft-365-local-deployment)).

| Phase | Planning output |
| --- | --- |
| Assessment | Business requirements, compliance drivers, data residency constraints, service scope, and current Exchange, SharePoint, and Skype for Business estate. |
| Planning | Azure Local deployment type, hardware profile, migration approach, identity integration, network design, and availability model. |
| Acquisition | Premier Solution hardware, software, licenses, partner services, and any disconnected operations prerequisites. |
| Deployment | Azure Local setup, Microsoft 365 Local workload deployment, migration, validation, operations handover, and support model. |

Authorized partners can start from the Microsoft 365 Local sign-up path at [aka.ms/m365localsignup](https://aka.ms/m365localsignup). Customers should contact their Microsoft account team or certified partner rather than trying to deploy from generic Azure Local documentation.

## Choose supported Azure Local deployment types

Microsoft 365 Local must run on an Azure Local Premier Solution that meets the hardware requirements for Microsoft 365 Local ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/m365-local/microsoft-365-local-overview#microsoft-365-local-hardware-requirements)). The Azure Local deployment-type table lists Microsoft 365 Local as supported on hyperconverged and disaggregated deployments, and not supported on multi-rack or small form factor deployments ([Learn](https://learn.microsoft.com/azure/azure-local/plan/find-your-deployment-type#workload-availability-by-deployment-type)).

| Deployment type | Microsoft 365 Local fit |
| --- | --- |
| Hyperconverged | Supported. Use when compute and storage should run on the same machines and the environment fits the hyperconverged scale point. |
| Disaggregated | Supported. Use when compute and storage need to scale independently or when SAN-backed storage is part of the design. |
| Multi-rack | Not listed as supported for Microsoft 365 Local in the deployment-type table. |
| Small form factor | Not listed as supported for Microsoft 365 Local in the deployment-type table. |

This does not mean the whole sovereign environment cannot include multi-rack or small form factor Azure Local. It means Microsoft 365 Local placement should use supported hyperconverged or disaggregated instances.

## Use the reference architecture as an example, not a sizing formula

The Microsoft 365 Local overview includes a large-scale connected-mode example. It has one three-node Azure Local instance that supports SharePoint Server and SQL Server workloads, four single-node Azure Local instances for Exchange Server mailbox roles, and two single-node Azure Local instances for Exchange Server edge transport roles ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/m365-local/microsoft-365-local-overview#server-role-allocation)).

| Role area | Example allocation |
| --- | --- |
| SharePoint and SQL Server | One three-node Azure Local instance |
| Exchange mailbox role | Four single-node Azure Local instances |
| Exchange edge transport role | Two single-node Azure Local instances |

Use this example to understand role separation and scale-out shape. Do not copy it into a proposal as a universal bill of materials. The same Learn section states that alternative configurations and hardware specifications are available for different scales and that customers should work with an authorized Microsoft partner to size and design their deployment.

For the planning workshop, collect these inputs before the partner sizes the environment:

| Input | Why it matters |
| --- | --- |
| Mailbox count, mailbox size, retention, and mail flow pattern | Drives Exchange mailbox and edge transport sizing. |
| SharePoint content size, site count, and SQL Server requirements | Drives storage, SQL Server, and SharePoint topology. |
| Skype for Business voice, conferencing, and federation needs | Drives network, certificate, and availability design. |
| Identity source and authentication model | Determines Active Directory, certificate, and access dependencies. |
| Connected or disconnected control plane | Changes monitoring, updates, identity, DNS, PKI, and support workflows. |
| Recovery objectives | Determines backup, replica, local failover, and public-cloud fallback design. |

## Decide connected, disconnected, and DR patterns

Microsoft 365 Local supports hybrid connectivity and fully disconnected deployment models ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/m365-local/microsoft-365-local-overview)). In connected mode, Azure provides the cloud-connected control plane for monitoring, updates, and policy. In disconnected mode, the local control plane handles the management functions that the environment can use without Azure public cloud connectivity.

The February 24, 2026 Microsoft blog states that Microsoft 365 Local disconnected is now available and that Exchange Server, SharePoint Server, and Skype for Business Server can run inside the customer's sovereign operational boundary on Azure Local ([Microsoft Blog](https://blogs.microsoft.com/blog/2026/02/24/microsoft-sovereign-cloud-adds-governance-productivity-and-support-for-large-ai-models-securely-running-even-when-completely-disconnected/)). Use that fact when a customer asks whether a disconnected productivity design is supported, then use Learn for the design details.

Microsoft also describes Microsoft 365 Local as a disaster recovery and business continuity option. The overview states that organizations can operate in the public cloud with the option to continue locally during crisis scenarios ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/m365-local/microsoft-365-local-overview#why-use-microsoft-365-local)). A practical pattern is to keep the local environment sized for critical communications, priority document workflows, and defined user groups during a public-cloud outage or a sovereignty-driven isolation event.

Do not treat local fallback as automatic. The design must specify identity behavior, DNS cutover, client access names, certificate trust, mail routing, backup and restore, monitoring, and the conditions that trigger local operation.

:::caution[Plan the operating model]
Microsoft 365 Local keeps the workloads inside the customer boundary, but it does not remove the need for Exchange, SharePoint, Skype for Business, Azure Local, identity, certificate, and backup operations. Assign those responsibilities before the design is approved.
:::

## Plan lifecycle and support expectations

The Microsoft 365 Local overview says Microsoft announced support for the Subscription Editions of Exchange Server, SharePoint Server, and Skype for Business through at least 2035 ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/m365-local/microsoft-365-local-overview#microsoft-365-local-capabilities)). The Modern Lifecycle page gives the exact "Earliest Possible EoS Date" of December 31, 2035 for Exchange Server Subscription Edition, SharePoint Server Subscription Edition, and Skype for Business Subscription Edition ([Learn](https://learn.microsoft.com/lifecycle/additional-support-server-modern-lifecycle-policy)).

That date is not a reason to defer lifecycle planning. The customer still needs update windows, certificate renewal, storage expansion, backup validation, test restores, health checks, and partner support procedures. In disconnected environments, add offline update and support-data exchange steps to the runbook.

## Planning checklist

Use this checklist before moving from discovery to design.

| Decision | Required answer |
| --- | --- |
| Workload scope | Which Exchange, SharePoint, and Skype for Business services are in scope? |
| Deployment type | Hyperconverged or disaggregated Azure Local? |
| Hardware | Which Premier Solution and partner-validated configuration? |
| Connectivity | Connected, intermittent connected behavior, or disconnected operations? |
| Identity and access | Which directory, authentication, privileged access, and break-glass model? |
| Network and names | Which client access names, certificates, firewall paths, and DNS records? |
| DR behavior | Which users and services must continue locally, and what triggers fallback? |
| Operations | Which team owns Azure Local, server workloads, backup, monitoring, updates, and partner escalation? |

## Sources

- [What is Microsoft 365 Local?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/m365-local/microsoft-365-local-overview)
- [Find your Azure Local deployment type](https://learn.microsoft.com/azure/azure-local/plan/find-your-deployment-type)
- [Disconnected operations for Azure Local](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview)
- [Additional support for select server products following Modern Lifecycle Policy](https://learn.microsoft.com/lifecycle/additional-support-server-modern-lifecycle-policy)
- [Microsoft Sovereign Cloud adds governance, productivity and support for large AI models securely running even when completely disconnected](https://blogs.microsoft.com/blog/2026/02/24/microsoft-sovereign-cloud-adds-governance-productivity-and-support-for-large-ai-models-securely-running-even-when-completely-disconnected/)
