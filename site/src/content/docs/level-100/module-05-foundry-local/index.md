---
title: "Module 5: Foundry Local"
description: "Foundational overview of Foundry Local on Azure Local and Agentic Retrieval for local AI inference and retrieval at the edge."
lastVerified: 2026-10-02
module:
  duration: "35-45 minutes"
  objectives:
    - Explain how Foundry Local on Azure Local runs AI inference on Arc-enabled Kubernetes.
    - Describe how Agentic Retrieval grounds AI responses in local knowledge sources.
    - Distinguish vendor-neutral RAG concepts from Microsoft Foundry Local services.
    - Identify sovereignty reasons to run inference and retrieval close to private data.
  prerequisites:
    - /level-100/module-02-cloud-models/sovereign-private-cloud/
    - /level-100/module-03-azure-local/
    - /level-100/module-04-azure-arc/
sidebar:
  label: Overview
  order: 5
---

Foundry Local on Azure Local brings AI inference to Azure Local infrastructure through an Azure Arc extension on Arc-enabled Kubernetes. Agentic Retrieval in Foundry Local adds local retrieval, collections, agents, a built-in Model Context Protocol (MCP) server, and a chat experience. Both Foundry Local on Azure Local and Agentic Retrieval in Foundry Local are in preview ([Foundry Local source](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/overview), [Agentic Retrieval source](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/overview)).

This module starts with vendor-neutral retrieval-augmented generation (RAG) concepts, then maps those concepts to the current Microsoft services. You will see how Foundry Local on Azure Local supplies model endpoints, how Agentic Retrieval uses those endpoints for grounded answers, and why a sovereign private cloud design may place AI processing next to regulated or disconnected data.

## Sources

- [What is Foundry Local on Azure Local?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/overview)
- [What is Agentic Retrieval in Agents and Tools with Foundry Local?](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/overview)
- [What's new in Agentic Retrieval in Foundry Local](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/whats-new)
