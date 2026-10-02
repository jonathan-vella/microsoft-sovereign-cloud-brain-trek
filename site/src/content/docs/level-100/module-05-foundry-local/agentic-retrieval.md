---
title: "Agentic Retrieval"
description: "Map the former Edge RAG concepts to Agentic Retrieval in Foundry Local, including collections, APIs, MCP, and model endpoints."
lastVerified: 2026-10-02
sidebar:
  order: 3
---

Agentic Retrieval in Foundry Local is the current name for the capability formerly called Edge RAG enabled by Azure Arc. The June 2026 Microsoft Learn changelog says the release renamed Edge RAG to Agentic Retrieval and added an agentic layer for AI agent orchestration ([source](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/whats-new#june-2026)). Agentic Retrieval in Foundry Local is in preview ([source](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/overview)).

Foundry Local on Azure Local is the recommended local model endpoint for Agentic Retrieval, and it is also in preview ([source](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/overview)). The two services are related, but they do different jobs. Foundry Local serves models. Agentic Retrieval ingests local sources, searches collections, and orchestrates agents that use model endpoints.

## Concept map from Edge RAG to Agentic Retrieval

Use this table when you see older Edge RAG material in diagrams, presentations, or legal notes.

| Former Edge RAG concept | Current Foundry Local-family concept | What changed |
|---|---|---|
| Ingestion and local RAG pipeline | Local knowledge sources in Agentic Retrieval | The pipeline still parses, chunks, embeds, and indexes local data. The current docs organize it around knowledge sources and collections. |
| Vector store or semantic-search database | Collections | Collections map to Milvus vector collections and Postgres tables, and each collection has its own lifecycle and role-based access control. |
| Bundled local language model | Foundry Local on Azure Local endpoint or external Bring Your Own Model endpoint | Phi-3.5 and Mistral-7B are no longer bundled. All deployments now require a language model endpoint ([source](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/whats-new#june-2026)). |
| Azure Arc extension packaging | Azure Arc-enabled Kubernetes extension `microsoft.arc.rag` | The Arc extension model remains. |
| AKS on Azure Local runtime | Arc-enabled Kubernetes on Azure Local | The validated runtime remains Azure Local infrastructure with AKS enabled by Azure Arc. |
| Prompt and evaluation tooling | Agentic Retrieval evaluation and Foundry Local model evaluation | Evaluation is split across the retrieval and model-serving layers. |
| Prepackaged chat UI | Local chat experience | The current chat solution is a static React app with streaming responses, citations, and optional Microsoft Entra ID sign-in. |
| Azure-equivalent APIs | Seven REST API groups | The June 2026 release published API references for Agents Runtime, Knowledge Base Manager, Knowledge Sources, Collections, MCP Server, Ingestion, and Inference. |
| No agent orchestration layer | Agents Runtime and built-in MCP server | The agentic layer is new. It adds threads, messages, runs, streaming, knowledge orchestration, and MCP tools. |

## What the June 2026 release changed

The June 2026 release is the dividing line between the older Edge RAG design and the current Agentic Retrieval design. Microsoft documents these changes:

- Edge RAG enabled by Azure Arc was renamed to Agentic Retrieval in Foundry Local.
- An agentic layer was added for multistep conversations and tool use.
- Phi-3.5 and Mistral-7B stopped being bundled with the extension.
- All deployments now require a language model endpoint.
- The recommended local model endpoint is Foundry Local on Azure Local.
- GPU requirements for the Agentic Retrieval deployment dropped from four GPUs to two GPUs. The two GPUs serve the text embedding model and image embedding model, while Docling runs on CPU.
- Deployment modes were added through the `layerSelection` parameter. `combined` deploys the full platform, `agentic` deploys agents without local ingestion, and `knowledge` deploys the knowledge layer without agent orchestration.

These changes make the architecture more modular. A team can run inference through Foundry Local on Azure Local, use an external OpenAI-compatible model endpoint, or deploy only the layer it needs.

## Core layers

Agentic Retrieval has two main layers.

The **knowledge layer** ingests local documents and images, chunks content, creates embeddings, and stores searchable vectors in collections. It supports search methods such as full text, vector, hybrid, and hybrid multimodal search. Access is controlled through Azure role-based access control.

The **agentic layer** adds agents, threads, messages, runs, tool invocation, and a built-in MCP server. Agents can use knowledge bases and knowledge sources to answer across multiple data sources. The built-in MCP server exposes search tools, and the platform can connect to external MCP servers.

The local chat experience sits above those layers. It lets users create conversations, stream answers, and inspect citations while backend services handle model calls, token validation, data scoping, and tool use.

## Transparency Note naming

The Edge RAG Transparency Note still uses the old Edge RAG name ([source](https://learn.microsoft.com/legal/edge-rag/transparency-note)). It remains the responsible AI reference for the preview capability, but the product documentation uses Agentic Retrieval.

## Sources

- [What is Agentic Retrieval in Agents and Tools with Foundry Local?](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/overview)
- [What's new in Agentic Retrieval in Foundry Local](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/whats-new)
- [What you need for Agentic Retrieval in Foundry Local](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/requirements)
- [Transparency Note: Edge RAG Preview enabled by Azure Arc](https://learn.microsoft.com/legal/edge-rag/transparency-note)
- [What is Foundry Local on Azure Local?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/overview)
