# MS Learn snapshot — 2026-05-08

**Source:** <https://learn.microsoft.com/en-us/azure/azure-arc/edge-rag/overview>
**Cache date:** 2026-05-08
**Used by:** Phase 3.2 L100 Module 5 verification (§G Edge RAG status)

## Status

> Edge RAG Preview, enabled by Azure Arc is currently in **PREVIEW**.
> See the [Supplemental Terms of Use for Microsoft Azure Previews] for
> legal terms that apply to Azure features that are in beta, preview, or
> otherwise not yet released into general availability.

→ **Authoritative status as of 2026-05-08: PREVIEW**

The product name on Learn is consistently "**Edge RAG Preview**" (or
"Edge RAG Preview, enabled by Azure Arc"). Project content uses
"Edge RAG" without the "Preview" suffix in many places — Phase 3.2
adds preview labels where a specific capability claim is made, but
keeps "Edge RAG" as the short product name in casual prose.

## Architecture (verbatim excerpts)

> Edge RAG Preview is an Azure Arc-enabled Kubernetes extension that
> enables you to search on-premises data with generative AI, using
> Retrieval Augmented Generation (RAG).

> Edge RAG is supported and validated on Azure Arc-enabled Kubernetes
> on Azure Local (formerly Azure Stack HCI) infrastructure and as part
> of a preview for disconnected operations for Azure Local.

## Data flow / sovereignty

> Edge RAG sends only system metadata and organizational identifiable
> Information like subscription ID and cluster names to Microsoft. All
> customer content always stays in the on-premises infrastructure
> within the network boundaries defined by customers.

→ Project sovereignty claims about Edge RAG keeping data on-premises
**MATCH** the Learn documentation.

## Verification entries (claim list)

| ID | Project doc claim | File | Outcome |
|---|---|---|---|
| EDGERAG-1 | Edge RAG GA/Preview status | various L100/L300 | **PREVIEW** — project content should use "Edge RAG (preview)" or callouts where appropriate |
| EDGERAG-2 | Customer data stays on-premises | `level-100/edge-rag-concepts.md`, `level-100/edge-rag-use-cases.md` | **MATCH** |
| EDGERAG-3 | Edge RAG is an Arc-enabled Kubernetes extension | `level-100/edge-rag-architecture.md` | **MATCH** |
| EDGERAG-4 | Supports Azure Local connected and disconnected (preview for disconnected) | `level-100/edge-rag-concepts.md` | **MATCH** with caveat: disconnected support is itself in preview as of cache date |
