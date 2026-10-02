---
title: "Microsoft 365 Local overview"
description: "Understand what Microsoft 365 Local includes, why it matters for sovereignty, and how its support commitment differs by server product."
lastVerified: 2026-10-02
sidebar:
  order: 6.1
---

Microsoft 365 Local is Microsoft's option for running selected productivity server workloads in a customer-owned private cloud. It is [generally available](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/m365-local/microsoft-365-local-overview#get-started-with-microsoft-365-local).

Microsoft defines Microsoft 365 Local as Exchange Server, SharePoint Server, and Skype for Business Server running on Azure Local infrastructure that the customer owns and manages. For lifecycle planning, these are the Subscription Edition products. Microsoft lists the earliest possible end of support date as [December 31, 2035](https://learn.microsoft.com/lifecycle/additional-support-server-modern-lifecycle-policy) for Exchange Server Subscription Edition, SharePoint Server Subscription Edition, and Skype for Business Server Subscription Edition. Project Server Subscription Edition is listed on the same lifecycle page with an earliest possible end of support date of [December 31, 2031](https://learn.microsoft.com/lifecycle/additional-support-server-modern-lifecycle-policy), but Project Server is not listed as a Microsoft 365 Local workload in the Microsoft 365 Local overview.

## Why Microsoft 365 Local matters for sovereignty

Microsoft 365 Local matters when an organization needs productivity workloads inside a private operational boundary. Learn describes it as a way to keep data residency, access, and compliance under customer control while still using Azure-consistent management on Azure Local.

For a sovereignty architect, the important point is placement. The productivity workloads run on customer-owned Azure Local infrastructure instead of in a Microsoft 365 cloud service. That placement can support requirements where data, operational control, or cloud connectivity must remain within the customer's boundary.

Microsoft 365 Local sits in the [Sovereign Private Cloud](/level-100/module-02-cloud-models/sovereign-private-cloud/) part of the sovereign cloud model. The same private cloud stack can also include Azure Local infrastructure and other local workloads. In a connected design, Azure provides the cloud-connected control plane. In a disconnected design, the control plane runs locally.

## What Microsoft 365 Local includes

Microsoft Learn lists three Microsoft 365 Local productivity workloads:

| Workload | Role in the local environment |
| --- | --- |
| Exchange Server Subscription Edition | Email services hosted on customer-owned Azure Local infrastructure. |
| SharePoint Server Subscription Edition | Document management and collaboration sites hosted on customer-owned Azure Local infrastructure. |
| Skype for Business Server Subscription Edition | Unified communications hosted on customer-owned Azure Local infrastructure. |

Microsoft 365 Local must be deployed on an Azure Local Premier Solution that meets Microsoft 365 Local hardware requirements. Learn also says customers should work with an authorized Microsoft partner to size and design the deployment.

## What Microsoft 365 Local is not

The name doesn't mean the full Microsoft 365 cloud suite runs locally. The Learn overview defines Microsoft 365 Local by the three server workloads above. It does not list Microsoft Teams or the broader Microsoft 365 cloud services as included Microsoft 365 Local workloads.

Microsoft 365 Local also does not remove the need for deployment planning. The overview describes reference architectures and partner-led deployment phases, but says the overall architecture is tailored to each customer's needs.

## Connected and disconnected choices

Microsoft 365 Local supports both hybrid connectivity and fully disconnected operation. Connected operation can use Azure services for management, monitoring, updates, and policy enforcement. Disconnected operation keeps the control plane local for environments that require isolation from the Azure public cloud.

Microsoft's February 24, 2026 blog states that [Microsoft 365 Local disconnected is now available](https://blogs.microsoft.com/blog/2026/02/24/microsoft-sovereign-cloud-adds-governance-productivity-and-support-for-large-ai-models-securely-running-even-when-completely-disconnected/). The same blog describes the disconnected form as Exchange Server, SharePoint Server, and Skype for Business Server running inside the customer's sovereign operational boundary on Azure Local.

## Sources

- [What is Microsoft 365 Local?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/m365-local/microsoft-365-local-overview)
- [Additional support for select server products following Modern Lifecycle Policy](https://learn.microsoft.com/lifecycle/additional-support-server-modern-lifecycle-policy)
- [Microsoft Sovereign Cloud adds governance, productivity and support for large AI models, securely running even when completely disconnected](https://blogs.microsoft.com/blog/2026/02/24/microsoft-sovereign-cloud-adds-governance-productivity-and-support-for-large-ai-models-securely-running-even-when-completely-disconnected/)
