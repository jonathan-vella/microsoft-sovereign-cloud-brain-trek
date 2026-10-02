---
title: "Module 7: Sovereign Private Cloud stack"
description: "Plan the Sovereign Private Cloud stack across Azure Local, Microsoft 365 Local, GitHub Enterprise Local, Foundry Local, and disconnected operations."
lastVerified: 2026-10-02
module:
  duration: "75-105 minutes"
  objectives:
    - Explain how Azure Local anchors the Sovereign Private Cloud stack.
    - Choose between connected, intermittent, and disconnected operating models.
    - Plan Microsoft 365 Local and disconnected operations at an intermediate design level.
  prerequisites:
    - /level-100/module-03-azure-local/
    - /level-200/module-01-azure-local/
sidebar:
  label: Overview
  order: 7
---

Sovereign Private Cloud runs Microsoft cloud services on infrastructure the customer owns and operates. Azure Local is the platform layer for compute, storage, networking, lifecycle management, virtual machines, and AKS Arc-enabled clusters. Microsoft documents the private-cloud portfolio as Azure Local, Microsoft 365 Local, GitHub Enterprise Local, and Foundry Local on Azure Local ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/overview/sovereign-private-cloud)).

This module is for architects who need to place regulated productivity, developer, AI, and infrastructure workloads across connected and disconnected environments. You compare deployment types, plan the local control plane for disconnected operations, and size Microsoft 365 Local with a certified partner. Microsoft 365 Local is generally available ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/m365-local/microsoft-365-local-overview)); GitHub Enterprise Local, Foundry Local on Azure Local, and Agentic Retrieval in Foundry Local are preview capabilities ([GitHub Enterprise Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/github-local/github-local-overview), [Foundry Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/overview), [Agentic Retrieval](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/overview)).

## Key terms

| Term | Meaning in this module |
| --- | --- |
| Azure Local | The on-premises platform for Sovereign Private Cloud. It hosts VMs, AKS Arc-enabled clusters, and Microsoft private-cloud workloads. |
| Connected operations | Azure Local operates with periodic connectivity to Azure for control-plane activities and tolerates intermittent disconnections up to 30 days without affecting running workloads ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/azure-local/connected-operations-overview)). |
| Disconnected operations | Azure Local runs without ongoing connectivity to Azure. A local control plane appliance provides a subset of Azure management capabilities on a dedicated management cluster ([Learn](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview)). |
| Microsoft 365 Local | Exchange Server, SharePoint Server, and Skype for Business Server Subscription Editions on Azure Local Premier Solutions hardware. |
| Agentic Retrieval | The preview Azure Arc extension formerly called Edge RAG. It adds local ingestion, vector search, agents, and an MCP server for private data ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/whats-new#june-2026)). |

## Sources

- [What is Sovereign Private Cloud?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/overview/sovereign-private-cloud)
- [Connected operations overview](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/azure-local/connected-operations-overview)
- [Disconnected operations for Azure Local](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview)
- [What is Microsoft 365 Local?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/m365-local/microsoft-365-local-overview)
- [What is GitHub Enterprise Local?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/github-local/github-local-overview)
- [What is Foundry Local on Azure Local?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/overview)
- [What is Agentic Retrieval in Agents and Tools with Foundry Local?](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/overview)
