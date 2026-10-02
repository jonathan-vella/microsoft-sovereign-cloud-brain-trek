---
title: Sovereign Private Cloud
description: "Learn how Sovereign Private Cloud uses Azure Local, Microsoft 365 Local, GitHub Enterprise Local, and Foundry Local in customer-operated environments."
lastVerified: 2026-10-02
sidebar:
  order: 3
---

Sovereign Private Cloud is the Microsoft Sovereign Cloud model for customer-operated environments. It runs on infrastructure the customer owns and manages, with Azure Local as the foundation.

For a comparison of all three models, see [sovereign cloud models](/level-100/module-02-cloud-models/sovereign-cloud-models/).

## Operating pattern

Sovereign Private Cloud supports connected, intermittently connected, and disconnected operation. Connected environments use Azure for services such as centralized monitoring, lifecycle management, and policy. Intermittently connected environments keep workloads running during temporary outages. Disconnected environments run the Azure control plane and management services locally.

Azure Local disconnected operations require Azure Local 2602 or later and are [generally available](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview?view=azloc-2609). AKS on Azure Local with disconnected operations is still [preview](https://learn.microsoft.com/azure/aks-hybrid-edge/local/disconnected-operations/overview).

## Azure Local

[Azure Local](/level-100/module-03-azure-local/) runs virtual machines, storage, networking, and Kubernetes on customer-owned hardware. Microsoft Learn describes hyperconverged, disaggregated, multi-rack, and small form factor deployment types. For this module, the key point is that Azure Local provides the local infrastructure layer for private-cloud workloads.

Azure Local can run connected to Azure or in disconnected operations. Connected deployments can tolerate temporary loss of Azure connectivity without stopping running workloads. Disconnected operations add a local control plane for environments that need to reduce external dependencies.

## Microsoft 365 Local

[Microsoft 365 Local](/level-100/module-06-microsoft-365-local/) runs Exchange Server, SharePoint Server, and Skype for Business Server Subscription Editions on customer-owned Azure Local Premier Solution hardware. Microsoft Learn states that Microsoft 365 Local is now [generally available](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/m365-local/microsoft-365-local-overview).

Use it when productivity workloads must remain on-premises, including connected or fully disconnected environments. It is not the same as Microsoft 365 cloud services running in a public region. It is a local deployment of the server products that make up the Microsoft 365 Local offer.

## GitHub Enterprise Local

GitHub Enterprise Local is [preview](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/github-local/github-local-overview). It runs GitHub Enterprise Server as a self-hosted DevOps platform on Azure Local infrastructure.

Microsoft Learn describes it as a prebuilt virtual appliance on Azure Local. Repositories, metadata, artifacts, and execution remain on-premises. It supports source control, pull requests, issues, GitHub Actions with self-hosted runners, GitHub Packages, GitHub Advanced Security, audit logging, and enterprise identity integration. It can run in connected or disconnected environments.

## Foundry Local on Azure Local

[Foundry Local on Azure Local](/level-100/module-05-foundry-local/) is [preview](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/overview). It runs AI model inference on an Arc-enabled Kubernetes cluster on Azure Local, using ONNX-GenAI and vLLM inference engines.

Agentic Retrieval in Agents and Tools with Foundry Local is also [preview](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/overview). It is the current name for Edge RAG enabled by Azure Arc, and recommends Foundry Local on Azure Local as its language-model endpoint.

## When this model fits

Use Sovereign Private Cloud when the sovereignty requirement is about physical control, local operation, disconnected operations, or local service continuity. It is also the model for workloads that cannot place source code, collaboration data, or AI inference in a public cloud service.

This model adds operational responsibility. The customer or operating partner must manage hardware, lifecycle, capacity, local identity, local backup, and the connected or disconnected update path.

## Sources

- [What is Sovereign Private Cloud?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/overview/sovereign-private-cloud)
- [Connected operations overview](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/azure-local/connected-operations-overview)
- [Disconnected operations for Azure Local](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview?view=azloc-2609)
- [AKS on Azure Local with disconnected operations](https://learn.microsoft.com/azure/aks-hybrid-edge/local/disconnected-operations/overview)
- [What are hyperconverged deployments of Azure Local?](https://learn.microsoft.com/azure/azure-local/overview/hyperconverged-overview?view=azloc-2609)
- [What is Microsoft 365 Local?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/m365-local/microsoft-365-local-overview)
- [What is GitHub Enterprise Local?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/github-local/github-local-overview)
- [What is Foundry Local on Azure Local?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/overview)
- [What is Agentic Retrieval in Agents and Tools with Foundry Local?](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/overview)
