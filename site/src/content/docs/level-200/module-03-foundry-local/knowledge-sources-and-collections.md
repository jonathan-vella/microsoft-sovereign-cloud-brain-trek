---
title: "Knowledge sources and collections"
description: "Design Agentic Retrieval collections, ingestion, chunking, embeddings, and search patterns for on-premises RAG data."
lastVerified: 2026-10-02
sidebar:
  order: 1
---

Agentic Retrieval uses the knowledge layer to turn local documents and images into searchable context. The platform is in preview, and each collection maps to Milvus vector collections and Postgres tables in the cluster ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/collections-overview)).

## How collections organize data

A collection is a named container for ingested vector data. When you ingest content, Agentic Retrieval parses the files, chunks the extracted content, generates embeddings, and stores vectors plus metadata in the selected collection. When a user or agent asks a question, the query specifies which collection to search.

Use collections as the design boundary for data isolation and lifecycle. A single team with one dataset can use the default `edgeragapp` collection. A department-scoped design should use one collection per department. A tenant-scoped design should use one collection per tenant and align app roles with the collection names. For versioned data, create collections such as `catalog-2026-q1` and delete old collections after retention review.

Each collection can map internally to up to four Milvus vector collections and related Postgres tables. GPU mode creates text and image structures. CPU-only mode creates the text structures only ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/collections-overview)). Keep collection names stable because collection names become access-control and API inputs.

| Design choice | Use when | Planning note |
| --- | --- | --- |
| Default collection | One dataset and one access group | Fastest path for a pilot, but it can become a shared bucket. |
| Collection per department | HR, finance, engineering, or operations data needs separate access | Match collection-specific app roles to the collection names. |
| Collection per tenant | Customer data must stay isolated | Do not mix tenant content in one collection and rely only on filtering. |
| Collection per release | Policies, product catalogs, or manuals change by period | Keep rollback possible by leaving the prior collection online until validation passes. |
| Collection per confidentiality class | Public, internal, and confidential data need different readers | Use different collection roles and separate ingestion jobs. |

## Ingestion pipeline

The knowledge layer ingests content from supported on-premises sources. Agentic Retrieval requirements list NFS v3.0 and v4.1 with AUTH_SYS authentication for all deployments. For disconnected on-premises deployments, it also supports NFS v4.1 with Kerberos `krb5p` and SharePoint Server Subscription Edition with High-Trust Server-to-Server authentication ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/requirements)).

During ingestion, the parser extracts text, tables, image references, and document structure where supported. The system then chunks the extracted content and embeds it. Text embeddings use BGE-M3. Image embeddings use CLIP ViT-L/14. Docling parses documents on CPU, not GPU ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/requirements)).

Plan ingestion with three checks:

1. Confirm the source is reachable from the AKS Arc cluster and that the service account can read the files.
2. Remove password protection or file encryption that blocks parsing.
3. Decide whether the dataset needs image retrieval, hybrid search, or text-only search before you size GPU capacity.

July 2026 release notes added faster parallel parsing, automatic retries, skipped-file reporting, parsing coverage, and clean cancellation for ingestion runs ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/release-notes#july-2026)). Use those signals in validation. A successful ingestion job is not enough if the skipped-file report shows important content was excluded.

## Chunking decisions

Chunking splits source content into smaller blocks for embedding and retrieval. Smaller chunks improve precision because each vector represents a narrower idea. Larger chunks preserve more context but can retrieve extra text that distracts the language model. Overlap keeps references, definitions, and table context across chunk boundaries, but it increases storage and embedding work.

Microsoft's knowledge-layer guidance recommends a chunk size of 2000 for GPU and CPU-only processing. The maximum chunk size is 4000 for GPU and 2000 for CPU-only. It recommends chunk overlap of 200, with maximum overlap of 1000 for GPU and 200 for CPU-only ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/knowledge-layer-overview#chunk-settings)). Start with those defaults, then test against real questions from the target users.

| Content shape | Suggested adjustment | Why it helps |
| --- | --- | --- |
| Short procedures | Smaller chunks with modest overlap | Keeps each retrieved result focused on one task. |
| Long policy documents | Default chunk size with 10 to 15 percent overlap | Preserves definitions that span paragraphs. |
| Tables and manuals | Test advanced parsing before reducing chunk size | Structure matters more than smaller text blocks. |
| Image-heavy documents | Use GPU mode and multimodal search | CPU-only mode does not create the image vector structures. |

## Search patterns

Agentic Retrieval supports full text, vector, hybrid, and hybrid multimodal search ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/overview)). Choose the search type based on the query pattern.

Vector search works well when users ask in natural language and the source uses different wording. Full text search works well for exact codes, part numbers, and policy names. Hybrid search combines keyword and vector signals, so it is the default choice for mixed enterprise content. Hybrid multimodal search adds image retrieval when answers need diagrams, photos, or scanned visual context.

The built-in MCP server exposes six search tools over Model Context Protocol, and a knowledge source can map an agent to a collection through `indexed_source_ref` ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/collections-overview)). That mapping is the bridge from agents to collections. Keep it explicit in design documents so each agent has a clear data scope.

## Access control

Collection access uses Entra app roles. `EdgeRAGDeveloper` can manage and access all collections. `EdgeRAGEndUser` needs a matching collection-specific role, such as `finance-docs`, to query that collection through the external endpoint ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/collections-overview#collections-and-rbac)).

:::caution[Do not test only with port forwarding]
Azure RBAC checks are bypassed when you use port forwarding or internal Dapr calls for development. Test end-user access through the external endpoint before release.
:::

## Sources

- [Collections in Agentic Retrieval in Foundry Local](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/collections-overview)
- [Knowledge layer configuration for Agentic Retrieval in Foundry Local](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/knowledge-layer-overview)
- [What you need for Agentic Retrieval in Foundry Local](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/requirements)
- [Release notes for Agentic Retrieval in Foundry Local](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/release-notes)
- [What is Agentic Retrieval in Agents and Tools with Foundry Local?](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/overview)
