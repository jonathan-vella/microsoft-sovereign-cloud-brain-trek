---
title: "Foundry Local use cases"
description: "Explore foundational use cases for Foundry Local on Azure Local and Agentic Retrieval in sovereign, regulated, and disconnected sites."
lastVerified: 2026-10-02
sidebar:
  order: 4
---

Foundry Local on Azure Local and Agentic Retrieval in Foundry Local are preview services for local AI inference and local retrieval at the edge ([Foundry Local source](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/overview), [Agentic Retrieval source](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/overview)). At Level 100, the main design question is simple. Does the AI workload need to run close to private data, local operations, or a disconnected site?

The patterns below follow the capabilities Microsoft documents for both services.

## Regulated knowledge search

Regulated teams often need to search policies, procedures, audit evidence, and operational records without moving sensitive content into a public cloud service. Agentic Retrieval can ingest on-premises sources, index them into collections, and return answers with citations. Foundry Local on Azure Local can provide the local model endpoint for those answers.

The sovereignty reason is data control. Ingested documents, embeddings, agent configurations, and conversation threads stay in the on-premises infrastructure within the customer's network boundaries according to the Agentic Retrieval overview ([source](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/overview#data-on-premises-versus-cloud)).

This pattern fits foundational scenarios such as:

- Asking questions across internal policy libraries.
- Finding the current procedure for an operational control.
- Comparing retrieved source passages before an audit meeting.
- Summarizing a local procedure with citations back to the controlled source.

## Factory and field operations

Manufacturing sites, energy sites, and field facilities may generate data near machines, sensors, and local file shares. Moving every question and document to a public cloud can add latency, bandwidth, or data-governance concerns.

Agentic Retrieval can ground answers in local knowledge sources such as manuals, standard operating procedures, maintenance notes, and images. The platform supports document and image ingestion, and the current architecture separates the embedding models from the language model endpoint. Foundry Local on Azure Local can host the recommended local model endpoint when the site needs inference nearby.

The sovereignty reason is operational control. The site can keep source content and conversations inside local network boundaries while still using an Azure Arc-managed extension model.

## Disconnected and intermittently connected sites

Disconnected sites need a deployment path that does not depend on continuous internet access. Foundry Local on Azure Local added disconnected-environment operations in the June 2026 preview release ([source](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/whats-new#june-2026)). Agentic Retrieval is also supported as part of a preview for disconnected operations on Azure Local ([source](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/overview)).

In a disconnected pattern, expansion packs and local registries replace online dependency retrieval. Local authentication, local model artifacts, and local certificate handling become part of the deployment plan.

The sovereignty reason is continuity. A site can continue inference and retrieval when the public network is unavailable or intentionally separated, subject to the preview requirements and the organization's operating model.

## Government and defense knowledge work

Government and defense environments often separate workloads by classification, mission, geography, or policy boundary. A local RAG and inference pattern can help teams search approved sources inside a controlled enclave.

At this level, do not assume that a preview service is approved for a specific classification level or accreditation. The design value is the placement option. Foundry Local on Azure Local and Agentic Retrieval let architects evaluate whether AI inference, retrieval, citations, and agent conversations can stay inside the same local boundary as the data.

The sovereignty reason is boundary alignment. The AI data plane can align with the same physical, network, and administrative boundaries that protect the source content.

## Healthcare and life sciences support content

Healthcare and life sciences teams work with sensitive records, protocols, research notes, and regulated procedures. A local RAG pattern can help staff search approved local sources without sending private content to a cloud-hosted RAG service.

Agentic Retrieval can index local files and return grounded answers with citations. Foundry Local on Azure Local can keep the model endpoint close to the data when local inference is required.

The sovereignty reason is privacy and traceability. The answer should point back to the approved source, and the private source content should stay within the managed environment.

## When not to use this pattern

Foundry Local on Azure Local and Agentic Retrieval are not the default answer for every AI use case. Consider a cloud-hosted service when the data is already approved for cloud processing, the site has reliable connectivity, and the team does not need local operations. Consider a simpler search system when users only need keyword lookup, not generated answers.

Because both services are in preview, production planning should include preview terms, support expectations, deployment access, and a path to update the design when the services change.

## Sources

- [What is Foundry Local on Azure Local?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/overview)
- [What's new in Foundry Local on Azure Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/whats-new)
- [Requirements for Foundry Local on Azure Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-requirements)
- [What is Agentic Retrieval in Agents and Tools with Foundry Local?](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/overview)
- [What you need for Agentic Retrieval in Foundry Local](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/requirements)
