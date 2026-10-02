---
title: "Agentic Retrieval deployment"
description: "Plan Agentic Retrieval deployment modes, GPUs, model endpoints, NetworkPolicy, ingress, and disconnected support."
lastVerified: 2026-10-02
sidebar:
  order: 3
---

Agentic Retrieval is the Azure Arc-enabled Kubernetes extension at the center of Agents and Tools with Foundry Local. It provides local RAG, agents, MCP server access, ingestion, collections, and chat on Azure Local. Agentic Retrieval is in preview ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/overview)).

## What the extension installs

The extension type remains `microsoft.arc.rag`, even after the June 2026 rename from Edge RAG to Agentic Retrieval ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/release-notes#june-2026)). The extension can deploy the agentic layer, the knowledge layer, or both.

The agentic layer includes the Agents Runtime, Knowledge Base Manager, Knowledge Sources service, and built-in MCP server. The knowledge layer includes the Ingestion API, Inference API, Collections API, BGE-M3 text embedding, CLIP ViT-L/14 image embedding, Docling parser, Milvus, and PostgreSQL ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/deploy-overview#agentic-retrieval-architecture-and-components)).

| Component | Runs in | Purpose |
| --- | --- | --- |
| Agents Runtime | Agentic layer | Threads, messages, runs, and SSE streaming. |
| Knowledge Base Manager | Agentic layer | Manages knowledge bases and links sources. |
| MCP Server | Agentic layer | Exposes six built-in search tools over Model Context Protocol. |
| Ingestion API | Knowledge layer | Parses, chunks, embeds, and indexes source files. |
| Collections API | Knowledge layer | Manages vector data collections and collection lifecycle. |
| Milvus and PostgreSQL | Knowledge layer | Store vectors, metadata, and collection state. |
| Local chat experience | Full platform | Provides the built-in browser chat app. |

## Deployment modes

The `layerSelection` parameter controls what the extension deploys. Use it to avoid paying for components you do not need.

| Mode | What it deploys | GPU need | Use when |
| --- | --- | --- | --- |
| `combined` | Agentic layer and knowledge layer | 2 embedding GPUs plus a separate model endpoint | You need ingestion, local collections, agents, MCP, and chat. |
| `agentic` | Agents, knowledge bases, knowledge sources, and MCP server | No GPUs for Agentic Retrieval | You already have tools or external MCP sources and do not need local ingestion. |
| `knowledge` | Ingestion, inference, and collections | 2 embedding GPUs | You need local RAG without agent orchestration. |

All modes require a language model endpoint that supports an OpenAI-compatible chat completions API. Agentic Retrieval no longer bundles Phi-3.5 or Mistral-7B models. The recommended local endpoint is GPT-OSS-20B served by Foundry Local on Azure Local ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/requirements#language-model-requirement)).

## Language model endpoint

Agentic Retrieval sends generation requests to a model endpoint outside its own deployment. In the preferred Azure Local design, Foundry Local runs on the same AKS Arc cluster and serves GPT-OSS-20B. Microsoft recommends this pairing for the best experience, with Foundry Local installed first and its endpoint URL supplied during Agentic Retrieval deployment ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/requirements#language-model-requirement)).

For GPT-OSS-20B via Foundry Local, the model host needs its own GPU separate from the Agentic Retrieval embedding GPUs. The documented minimum is one NVIDIA GPU with at least 24 GB VRAM, 8 or more vCPUs, 32 GB RAM, and at least 50 GB storage. The recommended production baseline is one NVIDIA GPU with at least 48 GB VRAM, 16 or more vCPUs, 64 GB RAM, and 50 to 100 GB storage per replica ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/requirements#hardware-requirements-gpt-oss-20b-via-foundry-local)).

Microsoft's July 2026 release notes recommend a 32K token context window for the Foundry Local model used with Agentic Retrieval ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/release-notes#july-2026)). Use a smaller context only after testing the actual retrieval and tool-use flows.

## Cluster capacity

Agentic Retrieval is validated on Azure Local. The requirements page lists Azure Local 2504 as the minimum Azure Local version for connected deployments ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/requirements#minimum-software-requirements)).

Combined mode deploys more than 60 pods. The documented minimum cluster capacity for combined mode is three CPU workers at `Standard_D8s_v3` plus one GPU worker, with 24 or more vCPU and 96 or more GB RAM. Knowledge-only mode requires two `Standard_D8s_v3` CPU workers and 16 vCPU with 64 GB RAM, plus GPU capacity when you use embedding GPUs ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/requirements#minimum-cluster-node-capacity)).

| Capacity item | Combined mode | Knowledge mode | Agentic mode |
| --- | --- | --- | --- |
| CPU workers | 3 or more | 2 or more | 3 or more |
| Embedding GPUs | 2 | 2 | 0 |
| Language model endpoint | Required | Required | Required |
| NFS data source | Required | Required | Not required |
| Entra app registration | Required | Required | Required |

The two Agentic Retrieval GPUs are for embedding models. GPU 1 runs BGE-M3 for text embedding. GPU 2 runs CLIP ViT-L/14 for image embedding. Docling runs on CPU, and the language model runs through the external endpoint ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/requirements#language-model-requirement)).

## NetworkPolicy and ingress

July 2026 release notes require a CNI that enforces Kubernetes NetworkPolicy. Microsoft recommends Calico, and the installer checks for this prerequisite ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/release-notes#july-2026)). Do not treat NetworkPolicy as optional hardening. It is part of the platform requirement.

Agentic Retrieval ships and manages its own ingress controller. Bring-your-own ingress is not supported for the extension ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/release-notes#july-2026)). Plan one routable static IP for MetalLB, DNS for the chat and API endpoints, and a production TLS certificate signed by a trusted CA. The requirements page allows a self-signed certificate if you do not provide one, but it says not to use self-signed certificates in production ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/requirements#azure-resources)).

## Deployment workflow

A reliable rollout starts with the model endpoint and storage, not the chat UI.

1. Prepare Azure Local, AKS Arc, GPU node pools, MetalLB, DNS, certificates, and CNI.
2. Deploy Foundry Local and validate the model endpoint if you use the recommended local model path.
3. Create the Entra app registration and assign users and groups.
4. Deploy Agentic Retrieval with the selected `layerSelection` mode and model endpoint settings.
5. Validate extension health and chat endpoint reachability.
6. Configure collections, data sources, chunking, and query settings.
7. Connect agents to knowledge sources if you use the agentic layer.
8. Monitor and evaluate the deployment.

If Agentic Retrieval calls Foundry Local with managed identity, assign the Foundry app role, ARM Reader, and Azure RBAC roles described in the deployment overview. Missing one layer can cause 401 or 403 responses ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/deploy-overview#required-roles-for-foundry-local-inference)).

## Disconnected support

Agentic Retrieval supports disconnected deployment on Azure Local in preview ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/disconnected-operations/overview-disconnected)). Disconnected deployment uses the same Arc-enabled Kubernetes extension model, but you import an expansion pack into Azure Local Disconnected Operations before installation. The expansion pack registers the extension type locally, imports container images into the `edgeartifacts` registry, and publishes model artifacts to the registry.

Disconnected deployments still need a reachable OpenAI-compatible language model endpoint. The recommended option is Foundry Local on Azure Local on the same disconnected cluster. NetworkPolicy still applies, and the extension uses MetalLB with an ingress IP that you provide at install time ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/disconnected-operations/overview-disconnected)).

:::note[Plan disconnected identity early]
End-user sign-in in disconnected deployments does not use public Entra ID endpoints. You create the Entra application registration on the disconnected stamp with the disconnected Microsoft Graph endpoint.
:::

## Sources

- [What is Agentic Retrieval in Agents and Tools with Foundry Local?](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/overview)
- [What you need for Agentic Retrieval in Foundry Local](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/requirements)
- [Deployment overview for Agentic Retrieval in Foundry Local](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/deploy-overview)
- [Release notes for Agentic Retrieval in Foundry Local](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/release-notes)
- [Disconnected operations for Agentic Retrieval in Foundry Local](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/disconnected-operations/overview-disconnected)
