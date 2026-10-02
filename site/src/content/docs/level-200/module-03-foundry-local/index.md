---
title: "Module 3: Foundry Local on Azure Local"
description: "Plan Foundry Local inference and Agentic Retrieval on Azure Local, including Kubernetes, GPUs, collections, operations, and RAG design."
lastVerified: 2026-10-02
module:
  duration: "60-90 minutes"
  objectives:
    - Plan a Foundry Local on Azure Local deployment, including GPU and Kubernetes prerequisites.
    - Choose between ONNX Runtime and vLLM for local inference workloads.
    - Design Agentic Retrieval collections, ingestion, and deployment modes for on-premises data.
    - Operate local AI endpoints with authentication, monitoring, evaluation, and disconnected deployment constraints.
  prerequisites:
    - /level-100/module-03-azure-local/
    - /level-100/module-05-edge-rag/
sidebar:
  label: Overview
  order: 3
---

Foundry Local on Azure Local runs AI inference on an Arc-enabled Kubernetes cluster on Azure Local. It is in preview, and preview deployment is request-only during preview ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/overview)). Agentic Retrieval in Agents and Tools with Foundry Local is a sibling Azure Arc extension for local RAG, agents, MCP tools, and chat. It is also in preview ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/overview)).

Agentic Retrieval was called Edge RAG until June 2026, when Microsoft renamed the extension and added an agentic layer for orchestration ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/whats-new#june-2026)). Treat the two extensions as separate building blocks. Foundry Local serves the model endpoint. Agentic Retrieval handles ingestion, collections, search, agents, MCP access, and the chat experience.

## Before you start

This module assumes you can read AKS Arc and Azure Local requirements, reason about GPU-backed node pools, and explain basic RAG terms such as embeddings, vector search, chunking, grounding, and citations. If the deployment must run without internet connectivity, also review Azure Local disconnected operations before you size the cluster.

## Sources

- [What is Foundry Local on Azure Local?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/overview)
- [Requirements for Foundry Local on Azure Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-requirements)
- [What is Agentic Retrieval in Agents and Tools with Foundry Local?](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/overview)
- [What's new in Agentic Retrieval in Foundry Local](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/whats-new)
