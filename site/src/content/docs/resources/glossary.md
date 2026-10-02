---
title: Glossary
description: "Definitions for current Microsoft Sovereign Cloud, Azure Local, Azure Arc, security, compliance, and AI terms."
lastVerified: 2026-10-02
sidebar:
  order: 2
---

This glossary defines terms used across the Microsoft Sovereign Cloud Brain Trek. Product names use current Microsoft documentation.

## A

### Agentic Retrieval

Agentic Retrieval (formerly Edge RAG) is the [preview](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/overview) Azure Arc-enabled Kubernetes extension in Agents and Tools with Foundry Local for local agentic RAG over on-premises data. Microsoft documented the rename in the [June 2026 release](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/whats-new#june-2026). See [Foundry Local in production](/level-300/module-04-foundry-local-production/).

### Air-gapped

An air-gapped environment has no external network connection. In this site, use the Microsoft term **disconnected operations** when you refer to Azure Local environments that run a local control plane.

### Azure Arc

Azure Arc projects servers, Kubernetes clusters, Azure data services, and other non-Azure resources into Azure Resource Manager for management and governance. See [Azure Arc overview](https://learn.microsoft.com/azure/azure-arc/overview).

### Azure Arc-enabled data services

Azure Arc-enabled data services run selected Azure data services on Kubernetes outside Azure. Azure Arc-enabled PostgreSQL server was [retired July 14, 2025](https://learn.microsoft.com/azure/azure-arc/data/release-notes), and indirectly connected mode for Arc-enabled data services was [retired in September 2025](https://learn.microsoft.com/azure/azure-arc/data/release-notes).

### Azure Arc-enabled Kubernetes

Azure Arc-enabled Kubernetes lets you attach supported Kubernetes clusters to Azure for inventory, extensions, GitOps, policy, and governance. It is the management path used by Foundry Local on Azure Local and Agentic Retrieval.

### Azure Arc-enabled servers

Azure Arc-enabled servers are Windows or Linux machines outside Azure that are registered with Azure Arc. After registration, they can use Azure management services such as Azure Policy, Microsoft Defender for Cloud, and Azure Monitor.

### Azure Copilot

Azure Copilot is the current Microsoft Learn name for the Azure portal AI assistant that was also described in older docs as Microsoft Copilot in Azure. Azure Copilot is available in commercial Azure and is [not available in national clouds](https://learn.microsoft.com/azure/copilot/overview), including Azure Government and Microsoft Azure operated by 21Vianet.

### Azure Government

Azure Government is a dedicated Azure cloud for eligible US government agencies and partners. It uses physically isolated US datacenters and has three listed Azure Government regions, with separate Azure Government Secret and Azure Government Top Secret offerings described in the compliance offerings documentation.

### Azure landing zone

An Azure landing zone is a platform and workload architecture for governing, securing, and scaling a multi-subscription Azure environment. Sovereign Landing Zone builds on this model.

### Azure Local

Azure Local is Microsoft's infrastructure for running Azure-consistent compute, storage, networking, and management on customer-owned hardware. It was formerly branded Azure Stack HCI, but training content should use Azure Local except where a legacy resource type requires the old name. See [Azure Local advanced](/level-300/module-01-azure-local-advanced/).

### Azure Policy

Azure Policy creates, assigns, and evaluates rules for Azure resources. Sovereign Landing Zone and Sovereign Control Panel use policy signals as part of sovereignty posture management.

## C

### Cloud operating model

A cloud operating model defines how an organization governs, secures, deploys, and operates cloud resources. For sovereign environments, it must also define who can operate the platform, where control planes run, and how evidence is collected.

### Compliance framework

A compliance framework is a set of legal, regulatory, contractual, or industry requirements. Examples in this site include GDPR, DORA, FedRAMP, and sector-specific security standards.

### Connected operations

Connected operations describe Azure Local environments that maintain required connectivity to Azure for registration, monitoring, billing, updates, and Arc-enabled management. Azure Local workloads can continue through short Azure connectivity interruptions, but the operating model still depends on Azure connectivity.

### Critical ICT Third-Party Provider (CTPP)

A Critical ICT Third-Party Provider is an ICT provider designated for direct oversight under DORA. Microsoft Ireland Operations Limited is named as a CTPP in the [Microsoft DORA guidance](https://learn.microsoft.com/compliance/dora/dora-what-is-dora), based on the European Supervisory Authorities list published on November 18, 2025.

### Customer Lockbox

Customer Lockbox is an approval workflow for Microsoft support access to customer content in supported services. Use it when customer approval of support access is part of the control requirement.

## D

### Data Guardian

Data Guardian is a Sovereign Public Cloud capability for enhanced operational oversight. It requires Microsoft personnel access in defined regions such as EU and EFTA to be monitored by authorized European-resident personnel and logged in a tamper-evident ledger.

### Data residency

Data residency is the geographic or jurisdictional location where data is stored and processed. Microsoft services apply residency rules differently by service, tenant geography, region selection, and product terms.

### Data sovereignty

Data sovereignty is the requirement that data remains subject to specific laws, governance controls, and operational rules. It includes data location, access control, encryption, and evidence that the controls work.

### Digital sovereignty

Digital sovereignty is the ability of an organization, government, or jurisdiction to control digital assets, data, operations, and dependencies according to its own requirements. Microsoft Sovereign Cloud maps this need to public cloud, private cloud, and national partner cloud models.

### Disconnected operations

Disconnected operations for Azure Local let approved customers deploy and manage Azure Local instances without a connection to the Azure public cloud by using a local control plane. Azure Local disconnected operations require Azure Local 2602 or later, while AKS under disconnected operations remains [preview](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview). See [Azure Local disconnected operations](/level-300/module-01-azure-local-advanced/azure-local-disconnected-operations/).

### DORA

DORA is the EU Digital Operational Resilience Act for financial entities and ICT providers. Microsoft Learn states that financial entities and designated critical ICT third-party service providers needed to be ready to comply starting [January 17, 2025](https://learn.microsoft.com/compliance/dora/dora-what-is-dora).

## E

### Edge computing

Edge computing places compute and data processing close to where data is created or consumed. In this site, Azure Local, Azure Arc, Foundry Local on Azure Local, and Agentic Retrieval are the main Microsoft edge technologies.

### Embedding

An embedding is a numerical representation of content used for similarity search. Agentic Retrieval creates embeddings for local knowledge sources and stores them in local collections.

### EU Data Boundary

The EU Data Boundary is a defined boundary where Microsoft commits to store and process Customer Data and personal data for covered Microsoft enterprise online services, subject to documented exceptions. It covers EU and EFTA countries for in-scope services.

### External Key Management (EKM)

External Key Management means encryption keys are generated, stored, and managed outside cloud infrastructure while protecting cloud data. Managed HSM External Key Management is [in preview](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/external-key-management) and delegates wrap and unwrap operations to a customer-run EKM Proxy.

## F

### FedRAMP

FedRAMP is the US Federal Risk and Authorization Management Program for cloud products and services. Microsoft documents Azure compliance offerings and Azure Government compliance scope in Microsoft compliance documentation.

### Foundry Local

Foundry Local on Azure Local is a [preview](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/overview) Arc-enabled Kubernetes extension for local AI inference on Azure Local. It is the recommended local language model endpoint for Agentic Retrieval. See [Foundry Local in production](/level-300/module-04-foundry-local-production/).

## G

### GDPR

GDPR is the European Union General Data Protection Regulation. In sovereign cloud design, GDPR conversations usually focus on data protection roles, lawful processing, residency, transfer mechanisms, and audit evidence.

### GitHub Enterprise Local

GitHub Enterprise Local is a [preview](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/github-local/github-local-overview) solution for running GitHub Enterprise Server on Azure Local infrastructure. It targets regulated environments that need local repositories, local CI/CD, and disconnected operations.

### GitOps

GitOps is an operating model that uses Git repositories as the source of truth for declarative configuration. Azure Arc-enabled Kubernetes can apply GitOps configuration across attached clusters.

### Global Secure Access

Global Secure Access is the unifying Microsoft Entra term for Microsoft Entra Internet Access and Microsoft Entra Private Access. These services are Microsoft's Security Service Edge solution and are now [generally available](https://learn.microsoft.com/entra/global-secure-access/overview-what-is-global-secure-access).

## H

### HIPAA

HIPAA is a US healthcare law that includes privacy and security requirements for protected health information. Healthcare sovereign designs often map HIPAA requirements to identity, encryption, audit, and data access controls.

### Hybrid cloud

Hybrid cloud combines cloud services with on-premises, edge, or partner-operated infrastructure. Azure Arc and Azure Local provide the management and infrastructure patterns used throughout this training.

### Hyperconverged infrastructure

Hyperconverged infrastructure combines compute, storage, and networking in a software-defined system. Azure Local hyperconverged deployments are [generally available](https://learn.microsoft.com/azure/azure-local/overview/hyperconverged-overview) and scale from one to 16 machines.

## I

### Indirectly connected mode

Indirectly connected mode was a connectivity mode for Arc-enabled data services. It is [retired as of September 2025](https://learn.microsoft.com/azure/azure-arc/data/release-notes), so new training should describe direct connectivity for supported Arc data services.

### Infrastructure as Code

Infrastructure as Code is the practice of defining infrastructure in source-controlled templates or code. Sovereign Landing Zone implementations use infrastructure as code for repeatable policy, management group, and subscription deployment.

### ITAR

ITAR is the US International Traffic in Arms Regulations. When ITAR applies, design discussions normally include eligibility, access restrictions, data handling, and the correct cloud environment.

## K

### Kubernetes

Kubernetes is a container orchestration platform for deploying and managing containerized applications. Azure Local uses AKS enabled by Azure Arc for Kubernetes workloads, and Arc-enabled Kubernetes hosts Foundry Local on Azure Local and Agentic Retrieval.

## L

### Landing zone

A landing zone is a prepared cloud environment for workload deployment. It includes governance, identity, networking, security, and management controls.

### Large language model (LLM)

A large language model is an AI model that generates or reasons over text and other inputs. In local sovereign AI designs, the model endpoint might run in Foundry Local on Azure Local.

## M

### Managed HSM

Azure Key Vault Managed HSM is a fully managed, highly available, single-tenant cloud service for HSM-protected cryptographic keys. Microsoft Learn states that Managed HSM uses [FIPS 140-3 Level 3](https://learn.microsoft.com/azure/key-vault/managed-hsm/overview) validated HSMs.

### Managed identity

Managed identity is an Azure identity that a service can use to authenticate to resources that support Microsoft Entra ID. It reduces the need to store credentials in application code or configuration.

### Management cluster

The management cluster is the dedicated Azure Local cluster that hosts the local control plane for disconnected operations. Production deployments require a [dedicated three-node Azure Local management cluster](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-control-plane-appliance), separate from tenant workload clusters. See [Azure Local disconnected operations](/level-300/module-01-azure-local-advanced/azure-local-disconnected-operations/).

### Microsoft 365 Local

Microsoft 365 Local runs Exchange Server, SharePoint Server, and Skype for Business Server on customer-owned Azure Local infrastructure. Microsoft Learn states that Microsoft 365 Local is [generally available](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/m365-local/microsoft-365-local-overview).

### Microsoft Entra Agent ID

Microsoft Entra Agent ID is an identity and security framework for AI agents. It gives agents governed identities and extends Microsoft Entra controls such as access protection, identity governance, and audit logging.

### Microsoft Entra ID

Microsoft Entra ID is Microsoft's cloud identity and access management service. It provides authentication, authorization, Conditional Access, identity governance, workload identities, and related identity controls.

### Microsoft Sovereign Cloud

Microsoft Sovereign Cloud is the current name for the portfolio formerly called Microsoft Cloud for Sovereignty. It includes Sovereign Public Cloud, Sovereign Private Cloud, and National Partner Clouds.

## N

### National Partner Clouds

National Partner Clouds are local partner-operated cloud environments that use Microsoft technology with local ownership and governance. Microsoft Learn names Bleu in France and Delos Cloud in Germany as examples.

## O

### Operational sovereignty

Operational sovereignty is control over who can operate a platform, where operations occur, and how operational access is approved, monitored, and evidenced. Data Guardian, Customer Lockbox, and disconnected operations are examples of controls that support operational sovereignty.

## P

### PCI DSS

PCI DSS is the Payment Card Industry Data Security Standard. It applies to organizations that store, process, or transmit cardholder data.

### Policy as Code

Policy as Code stores policy definitions and assignments in source-controlled artifacts. Sovereign Landing Zone uses policy as code to apply residency, encryption, and confidential computing controls.

### Private cloud

Private cloud is cloud infrastructure dedicated to one organization or a controlled set of users. Sovereign Private Cloud uses Azure Local and related Microsoft services to run private cloud workloads in customer-controlled environments.

## R

### RBAC

Role-based access control grants access based on assigned roles. Azure RBAC, Microsoft Entra roles, Kubernetes RBAC, and local product roles can all appear in sovereign designs.

### Retrieval-Augmented Generation

Retrieval-Augmented Generation, or RAG, combines retrieval from external knowledge sources with model generation. Agentic Retrieval extends RAG with agents, MCP tools, knowledge sources, and local collections.

## S

### Sovereign Control Panel

Sovereign Control Panel is the current name for Regulated Environment Management. Microsoft Learn states that [Regulated Environment Management is now Sovereign Control Panel](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/sovereign-control-panel), and describes a Discover, Control, and Act operating model.

### Sovereign controls

Sovereign controls are technical and operational measures for data residency, encryption, operational oversight, policy enforcement, evidence collection, and continuity. The control set depends on the chosen deployment model.

### Sovereign Landing Zone

Sovereign Landing Zone is a variant of Azure landing zone architecture for sovereign public cloud requirements. It adds sovereign policy and management group patterns while retaining the Azure landing zone design areas. See [Sovereign Landing Zone architecture](/level-300/module-02-sovereign-landing-zone/slz-architecture/).

### Sovereign Private Cloud

Sovereign Private Cloud is the Microsoft deployment model for customer-controlled or partner-operated private cloud environments. Microsoft Learn describes it as built on Azure Local, Microsoft 365 Local, GitHub Enterprise Local ([preview](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/github-local/github-local-overview)), and Foundry Local on Azure Local.

### Sovereign Public Cloud

Sovereign Public Cloud is the Microsoft deployment model that adds sovereignty controls to hyperscale Microsoft cloud regions. It includes capabilities such as Data Guardian, External Key Management, Sovereign Control Panel, and Sovereign Landing Zone.

## T

### Tenant

A tenant is a logical instance of a cloud identity or service boundary for an organization. Tenant design affects identity, billing, policy, governance, and data boundary decisions.

### Trusted Launch

Trusted Launch is an Azure VM security capability that uses secure boot, virtual TPM, and boot integrity monitoring. In sovereign designs, it can support platform hardening and attestation goals.

## V

### Vector database

A vector database stores embeddings and supports similarity search. Agentic Retrieval uses local collections backed by vector storage to retrieve relevant content for agents.

### Virtual machine

A virtual machine is a software-defined computer that runs on a hypervisor. Azure Local hosts Windows and Linux VMs on customer-owned infrastructure and can manage supported VMs through Azure Arc.

## W

### Workload

A workload is an application, service, data platform, or business capability and the resources required to run it. Sovereign architecture decisions should be made per workload because data, residency, access, and availability requirements differ.

## Z

### Zero Trust

Zero Trust is a security approach based on "never trust, always verify." Microsoft describes three principles: verify explicitly, use least privilege access, and assume breach. See [Zero Trust architecture](/level-300/module-05-zero-trust/zero-trust-architecture/).

## Sources

- [What is Microsoft Sovereign Cloud?](https://learn.microsoft.com/azure/azure-sovereign-clouds/microsoft-sovereign-cloud)
- [What is Sovereign Public Cloud?](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/overview-sovereign-public-cloud)
- [What is Sovereign Private Cloud?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/overview/sovereign-private-cloud)
- [National Partner Clouds](https://learn.microsoft.com/azure/azure-sovereign-clouds/partner/overview-national-partner-clouds)
- [Sovereign Landing Zone](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/overview-sovereign-landing-zone)
- [What is Data Guardian?](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/data-guardian)
- [What is External Key Management?](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/external-key-management)
- [Sovereign Control Panel](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/sovereign-control-panel)
- [What is Azure Key Vault Managed HSM?](https://learn.microsoft.com/azure/key-vault/managed-hsm/overview)
- [What are hyperconverged deployments of Azure Local?](https://learn.microsoft.com/azure/azure-local/overview/hyperconverged-overview)
- [Disconnected operations for Azure Local](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview)
- [Dedicated management cluster for disconnected operations](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-control-plane-appliance)
- [Azure Arc overview](https://learn.microsoft.com/azure/azure-arc/overview)
- [Release notes for Azure Arc-enabled data services](https://learn.microsoft.com/azure/azure-arc/data/release-notes)
- [What is Microsoft 365 Local?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/m365-local/microsoft-365-local-overview)
- [What is GitHub Enterprise Local? (preview)](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/github-local/github-local-overview)
- [What is Foundry Local on Azure Local?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/overview)
- [What is Agentic Retrieval in Agents and Tools with Foundry Local?](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/overview)
- [What's new in Agentic Retrieval in Foundry Local](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/whats-new)
- [Zero Trust as a security foundation](https://learn.microsoft.com/security/zero-trust/zero-trust-overview)
- [What is Microsoft Defender for Cloud?](https://learn.microsoft.com/azure/defender-for-cloud/defender-for-cloud-introduction)
- [What is Microsoft Entra Agent ID?](https://learn.microsoft.com/entra/agent-id/what-is-microsoft-entra-agent-id)
- [What is Global Secure Access?](https://learn.microsoft.com/entra/global-secure-access/overview-what-is-global-secure-access)
- [What is Azure Copilot?](https://learn.microsoft.com/azure/copilot/overview)
- [Azure, Dynamics 365, Microsoft 365, and Power Platform compliance offerings](https://learn.microsoft.com/azure/compliance/offerings/)
- [What is DORA?](https://learn.microsoft.com/compliance/dora/dora-what-is-dora)
- [What is Azure Government?](https://learn.microsoft.com/azure/azure-government/documentation-government-welcome)
- [What is an Azure landing zone?](https://learn.microsoft.com/azure/cloud-adoption-framework/ready/landing-zone/)
