---
title: "Customer discovery"
description: "Use a structured question bank to map sovereignty, regulatory, connectivity, control, and AI requirements to the right Microsoft model."
lastVerified: 2026-10-02
sidebar:
  order: 1
---

Customer discovery separates a stated "data sovereignty" need from the controls, locations, workloads, and operating model the customer can defend to auditors. The output is a requirements map that lets you choose between Sovereign Public Cloud, Sovereign Private Cloud, and National Partner Clouds.

## Start with the deployment model

[Microsoft Sovereign Cloud has three deployment models](https://learn.microsoft.com/azure/azure-sovereign-clouds/microsoft-sovereign-cloud). Each model answers a different ownership and operations question.

| Deployment model | Use it when the answer points to | Discovery signal |
| --- | --- | --- |
| Sovereign Public Cloud | Microsoft-operated cloud services inside defined geopolitical boundaries, with added sovereignty controls | The customer can use public cloud if data residency, access approval, encryption, and policy controls satisfy the requirement. |
| Sovereign Private Cloud | Customer-owned infrastructure using Azure Local, Microsoft 365 Local, GitHub Enterprise Local, and Foundry Local on Azure Local | The customer needs local control plane options, disconnected operation, or workloads that must remain on-premises. |
| National Partner Clouds | Partner-operated or jointly governed clouds for a national jurisdiction | The customer must use a national cloud operator or a jurisdiction-specific model, such as [Bleu in France or Delos Cloud in Germany](https://learn.microsoft.com/azure/azure-sovereign-clouds/partner/overview-national-partner-clouds). |

Bleu France and Delos Cloud Germany are still being built as of the current Microsoft documentation. Treat them as qualification paths that need account-team confirmation, not as default landing zones.

## Confirm data boundary and residency requirements

Many customers say "keep data in country" when they mean one of several things. Ask for the law, regulator, data type, and acceptable processing location.

For European customers, the [EU Data Boundary](https://learn.microsoft.com/privacy/eudb/eu-data-boundary-learn) covers Azure, Dynamics 365, Power Platform, and Microsoft 365. It covers the 27 EU member states plus EFTA countries. Azure workloads must still be configured in eligible EU Data Boundary regions, and non-regional services need separate review.

Capture these details before proposing a design:

- Which data is in scope: customer content, personal data, telemetry, logs, support data, or professional services data.
- Which boundary is required: country, EU Data Boundary, EU plus EFTA, United States, classified enclave, or another jurisdiction.
- Whether processing, support access, backup, logging, and key material have the same boundary as primary data.
- Whether the customer has a regulator-approved list of acceptable services or regions.

## Classify connectivity

Connectivity determines whether the Azure control plane can stay in Azure or must move local.

| Connectivity pattern | What to ask | Design direction |
| --- | --- | --- |
| Connected | Can each Azure Local machine make HTTPS outbound connections to Azure endpoints at least every 30 days? | Connected Azure Local and Sovereign Public Cloud remain viable. |
| Intermittent | How long can sites lose internet access before operations must change? Which workloads must keep running? | Connected Azure Local can tolerate short disconnections, but management, update, and monitoring assumptions need testing. |
| Disconnected | Does regulation, classification, or mission need no public-cloud connectivity for management? | Consider Azure Local disconnected operations. The local control plane requires a dedicated management cluster and an eligible agreement and support plan. |

[Disconnected operations for Azure Local require Azure Local 2602 or later](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview), an eligible Microsoft agreement, and a Standard or higher support plan. [AKS on Azure Local with disconnected operations remains in preview](https://learn.microsoft.com/azure/aks-hybrid-edge/local/disconnected-operations/overview), so do not present container workloads in disconnected mode as fully general availability.

## Map regulatory drivers to evidence

Regulations do not map one-to-one to deployment models. They identify evidence, control, and audit requirements.

| Driver | What it often changes in discovery | Microsoft evidence to use |
| --- | --- | --- |
| GDPR | Controller and processor responsibilities, data subject request process, personal data location, and subprocessor review | Microsoft GDPR guidance and the EU Data Boundary. |
| NIS2 | Cybersecurity governance, incident reporting, supply chain controls, and essential or important entity scope | Microsoft Defender for Cloud and Purview Compliance Manager regulatory mappings. |
| DORA | Operational resilience, ICT third-party risk, exit planning, concentration risk, and financial-sector oversight | Microsoft DORA guidance, contract mapping, service health, and operational risk tooling. |
| FedRAMP | U.S. federal authorization boundary, region scope, and agency authorization path | Azure and Azure Government FedRAMP offerings. |

Don't state a Microsoft position on a scheme that Microsoft hasn't documented, such as FedRAMP 20x or EUCS. If the customer asks, record it as an open action for the account team.

## Discover control needs

Sovereignty controls are design requirements, not product names to add after the architecture is finished.

| Control need | What to ask | What the answer points to |
| --- | --- | --- |
| Customer-controlled keys | Who owns the root key material? Must the key encryption key remain outside Microsoft? | Azure Key Vault Managed HSM for key sovereignty. Managed HSM External Key Management is in preview and needs account-team enablement. |
| Confidential workloads | Must data stay protected while in use? Which workloads need attestation or trusted execution environments? | Azure confidential computing services, confidential VMs, confidential AKS worker nodes, or service-specific confidential features. |
| Support access oversight | Must Microsoft engineer access be approved, monitored, or logged by regional personnel? | Data Guardian for EU and EFTA remote-access monitoring, and Customer Lockbox for explicit access approval where supported. |
| Local productivity services | Must Exchange, SharePoint, or Skype for Business run on customer-owned infrastructure? | Microsoft 365 Local on Azure Local Premier Solutions through a certified partner. |
| Local AI inference | Must generative AI run on-premises, close to data, or in a disconnected environment? | Foundry Local on Azure Local, which is in preview and request-only during preview. |

## Question bank

Use this table during qualification. It keeps the meeting focused on decision points rather than product pitches.

| Question | Why it matters | What the answer points to |
| --- | --- | --- |
| Which law, contract, or regulator creates the sovereignty requirement? | A design can satisfy only the requirement you can name. | GDPR, DORA, NIS2, FedRAMP, national security policy, contractual data location, or customer policy. |
| Which data categories are in scope? | Customer content, personal data, logs, model prompts, and telemetry can have different rules. | Boundary scoping for Azure regions, Microsoft 365 tenant location, logging, and support data. |
| Is the required boundary country, EU Data Boundary, U.S. public sector, or another jurisdiction? | Region selection and service availability follow the required boundary. | Sovereign Public Cloud, Azure Government, National Partner Cloud, or private cloud. |
| Can Microsoft operate the service if access is approved and logged? | Some customers need evidence and approval, not local operation. | Data Guardian, Customer Lockbox, and audit logging. |
| Must encryption keys stay outside Microsoft control? | Key placement changes architecture, operations, and preview risk. | Managed HSM, customer-managed keys, or EKM preview assessment. |
| Can the environment connect outbound to Azure at least every 30 days? | Azure Local connected mode depends on periodic outbound connectivity. | Connected Azure Local, intermittent operations plan, or disconnected operations. |
| Does regulation require a local control plane? | A local control plane changes hardware, support, lifecycle, and cost. | Azure Local disconnected operations and a dedicated management cluster. |
| Which workloads must run locally? | Workload support varies by Azure Local deployment type. | Hyperconverged or disaggregated for Microsoft 365 Local and GitHub Enterprise Local. |
| Do you need Microsoft 365 services to continue if public cloud is unavailable? | Productivity continuity can drive Microsoft 365 Local. | Microsoft 365 Local sizing through an authorized partner. |
| Do AI prompts, embeddings, or model outputs need to stay on-premises? | AI data flows often trigger new privacy and IP review. | Foundry Local on Azure Local, Agentic Retrieval in Foundry Local, or a public-cloud AI service with controls. |
| Which identity system owns administrator access? | Identity determines approval, privileged access, audit, and break-glass design. | Microsoft Entra ID, local identity, privileged identity workflows, or disconnected authentication. |
| What support plan and Microsoft agreement do you have? | Disconnected operations has eligibility requirements. | Account-team validation before proposing disconnected operations. |
| Who signs off on risk: CISO, data protection officer, regulator, procurement, or mission owner? | The decision maker may not be the platform team. | Stakeholder map and evidence package. |
| What is the acceptable proof of value? | A proof of concept should test the control that creates risk. | Residency test, disconnected operations test, AI inference test, or cost model validation. |

## Discovery output

End discovery with a short, signed-off summary:

- Deployment model candidates and rejected options.
- In-scope data and boundary requirements.
- Connectivity pattern and control-plane assumption.
- Required controls and their status, including preview items.
- Workloads, workload owners, and expected growth.
- Sizing facts that still need measurement.
- Commercial facts that need account-team or partner confirmation.

This summary becomes the input for solution design, sizing, and cost estimation.

## Sources

- [What is Microsoft Sovereign Cloud?](https://learn.microsoft.com/azure/azure-sovereign-clouds/microsoft-sovereign-cloud)
- [What is Sovereign Public Cloud?](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/overview-sovereign-public-cloud)
- [What is Sovereign Private Cloud?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/overview/sovereign-private-cloud)
- [National Partner Clouds](https://learn.microsoft.com/azure/azure-sovereign-clouds/partner/overview-national-partner-clouds)
- [What is the EU Data Boundary?](https://learn.microsoft.com/privacy/eudb/eu-data-boundary-learn)
- [Disconnected operations for Azure Local](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview)
- [AKS on Azure Local with disconnected operations](https://learn.microsoft.com/azure/aks-hybrid-edge/local/disconnected-operations/overview)
- [What is External Key Management?](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/external-key-management)
- [What is confidential computing?](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/confidential-computing)
- [What is Data Guardian?](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/data-guardian)
- [Customer Lockbox for Microsoft Azure](https://learn.microsoft.com/azure/security/fundamentals/customer-lockbox-overview)
- [What is Microsoft 365 Local?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/m365-local/microsoft-365-local-overview)
- [What is Foundry Local on Azure Local?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/overview)
