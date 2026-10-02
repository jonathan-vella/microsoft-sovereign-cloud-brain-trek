---
title: "Level 100 visual specifications"
description: "Internal reference for current Level 100 SVG and Mermaid diagrams, sources, update triggers, and retired image files."
lastVerified: 2026-10-02
sidebar:
  hidden: true
---

This page is the internal design reference for Level 100 diagrams. Use it when you update a diagram, add alt text, or check whether an old file is still only present for URL compatibility.

Level 100 SVG diagrams use the same light-theme visual style as the site hero. Use a Fluent 2 and Azure palette: Azure blue `#0078D4`, dark blue `#003A6C` or `#243A5E`, light blue fills `#DEECF9` and `#EFF6FC`, neutral greys `#323130`, `#605E5C`, `#EDEBE9`, and `#F3F2F1`, accent teal `#008575`, purple `#5C2E91`, and amber `#8A5300` on `#FFF4CE` for "Preview" and "Being built" tags. Use the font stack `"Segoe UI", "Segoe UI Variable", Inter, system-ui, sans-serif`. Keep real SVG `<text>` elements, not outlined paths. Add `<title>` and `<desc>` as the first children, and connect them with `role="img"` and `aria-labelledby`. Use at least 14 px for body labels and 18 to 24 px for headings. Keep labels in sentence case unless an official product name uses capitals.

When you replace a diagram, create a new file name instead of overwriting the old one. Keep the old file in `site/public/images/level-100/` so published URLs keep working. Update every page reference and the image alt text in the page that uses the new diagram.

## SVG diagrams

### eu-data-boundary-2026.svg

| Item | Detail |
|---|---|
| File path | `/images/level-100/eu-data-boundary-2026.svg` |
| Used by | [European digital commitments](/level-100/module-01-digital-sovereignty/european-commitments/) |
| What it shows | The EU Data Boundary as a European boundary for in-scope Microsoft enterprise online services, the covered service families, the covered data categories, and product-specific scope rules. |

| Encoded fact | Microsoft source |
|---|---|
| The boundary consists of the 27 European Union member states plus EFTA countries Iceland, Liechtenstein, Norway, and Switzerland. | [What is the EU Data Boundary?](https://learn.microsoft.com/privacy/eudb/eu-data-boundary-learn#eu-data-boundary-countries-and-datacenter-locations) |
| Azure, Dynamics 365, Power Platform, and Microsoft 365 are in the EU Data Boundary service scope. | [What is the EU Data Boundary?](https://learn.microsoft.com/privacy/eudb/eu-data-boundary-learn#overview-of-the-eu-data-boundary) |
| The data categories are Customer Data, personal data in system-generated logs, and Professional Services Data stored at rest. | [What is the EU Data Boundary?](https://learn.microsoft.com/privacy/eudb/eu-data-boundary-learn#overview-of-the-eu-data-boundary) |
| Personal data in system-generated logs is pseudonymized. Microsoft contrasts this with anonymization. | [Pseudonymization in system-generated logs](https://learn.microsoft.com/privacy/eudb/eu-data-boundary-learn#pseudonymization-in-system-generated-logs) |
| Azure scope depends on deployment in an EU Data Boundary region for regional services. Non-regional services need service-specific configuration. | [How to configure services for use in the EU Data Boundary](https://learn.microsoft.com/privacy/eudb/eu-data-boundary-learn#how-to-configure-services-for-use-in-the-eu-data-boundary) |
| Microsoft 365 scope depends on tenant sign-up location in an EU or EFTA country or region. Multi-Geo customers are excluded. | [How to configure services for use in the EU Data Boundary](https://learn.microsoft.com/privacy/eudb/eu-data-boundary-learn#how-to-configure-services-for-use-in-the-eu-data-boundary) |
| Dynamics 365 and Power Platform scope requires tenant and environments in the EU and EFTA Macro Region Geography plus a billing address in an EU Data Boundary country. | [How to configure services for use in the EU Data Boundary](https://learn.microsoft.com/privacy/eudb/eu-data-boundary-learn#how-to-configure-services-for-use-in-the-eu-data-boundary) |

Update this diagram if the EU Data Boundary geography changes, Microsoft changes the service list, Microsoft changes the covered data categories, or product-specific scope rules change.

### sovereign-cloud-models-2026.svg

| Item | Detail |
|---|---|
| File path | `/images/level-100/sovereign-cloud-models-2026.svg` |
| Used by | [Sovereign cloud models](/level-100/module-02-cloud-models/sovereign-cloud-models/) |
| What it shows | The three Microsoft Sovereign Cloud deployment models: Sovereign Public Cloud, Sovereign Private Cloud, and National Partner Clouds. It compares who operates each model, where it runs, and the building blocks shown at Level 100 depth. |

| Encoded fact | Microsoft source |
|---|---|
| Microsoft Sovereign Cloud is the current name for the portfolio formerly called Microsoft Cloud for Sovereignty. | [What is Microsoft Sovereign Cloud?](https://learn.microsoft.com/azure/azure-sovereign-clouds/microsoft-sovereign-cloud) |
| The portfolio has three deployment models: Sovereign Public Cloud, Sovereign Private Cloud, and National Partner Clouds. | [What is Microsoft Sovereign Cloud?](https://learn.microsoft.com/azure/azure-sovereign-clouds/microsoft-sovereign-cloud) |
| Sovereign Public Cloud uses Microsoft-operated Azure public regions with sovereignty controls inside defined geopolitical boundaries. | [What is Sovereign Public Cloud?](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/overview-sovereign-public-cloud) |
| Sovereign Public Cloud capabilities include Data Guardian, External Key Management, Azure confidential computing, and Sovereign Control Panel. | [Capabilities of Sovereign Public Cloud](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/sovereign-public-cloud-capabilities) |
| Sovereign Private Cloud is delivered through Azure Local, Microsoft 365 Local, GitHub Enterprise Local, and Foundry Local on Azure Local. | [What is Sovereign Private Cloud?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/overview/sovereign-private-cloud) |
| GitHub Enterprise Local is in preview. The diagram uses a "Preview" tag next to that building block. | [GitHub Enterprise Local overview](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/github-local/github-local-overview) |
| Foundry Local on Azure Local is in preview. The diagram uses a "Preview" tag next to that building block. | [What is Foundry Local on Azure Local?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/overview) |
| Bleu is the National Partner Cloud in France, and Delos Cloud is the National Partner Cloud in Germany. Microsoft describes both as being built. | [National Partner Clouds](https://learn.microsoft.com/azure/azure-sovereign-clouds/partner/overview-national-partner-clouds) |

Update this diagram if GitHub Enterprise Local or Foundry Local on Azure Local leave preview, Microsoft 365 Local status changes, Bleu or Delos Cloud launch, Microsoft names another National Partner Cloud, or Microsoft changes the portfolio name or the three-model structure.

### azure-local-architecture-2026.svg

| Item | Detail |
|---|---|
| File path | `/images/level-100/azure-local-architecture-2026.svg` |
| Used by | [Azure Local architecture](/level-100/module-03-azure-local/azure-local-architecture/) |
| What it shows | Azure management services connect through Azure Arc to an on-premises Azure Local instance. The instance contains a workload layer, a platform layer, and validated hardware. |

| Encoded fact | Microsoft source |
|---|---|
| Azure Local can be viewed, monitored, and managed through the Azure portal, and it uses Azure Arc services such as Azure Policy, Azure Monitor, and Microsoft Defender for Cloud. | [What are hyperconverged deployments of Azure Local?](https://learn.microsoft.com/azure/azure-local/overview/hyperconverged-overview?view=azloc-2609) |
| Azure Local includes Azure Local VMs enabled by Azure Arc and AKS enabled by Azure Arc as foundational workload services. | [What are hyperconverged deployments of Azure Local?](https://learn.microsoft.com/azure/azure-local/overview/hyperconverged-overview?view=azloc-2609#common-azure-services-used-with-azure-local) |
| Azure Local is built on Hyper-V, Storage Spaces Direct, Failover Clustering, and Azure management services. | [What are hyperconverged deployments of Azure Local?](https://learn.microsoft.com/azure/azure-local/overview/hyperconverged-overview?view=azloc-2609#features-and-architecture) |
| Hyperconverged Azure Local deployments support one to 16 physical machines in an instance. | [What are hyperconverged deployments of Azure Local?](https://learn.microsoft.com/azure/azure-local/overview/hyperconverged-overview?view=azloc-2609#features-and-architecture) |
| Disaggregated deployments support one to 64 machines. | [Connected operations overview](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/azure-local/connected-operations-overview#deployment-options) |
| Multi-rack deployments scale up to 128 nodes per instance. | [Connected operations overview](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/azure-local/connected-operations-overview#multi-rack-deployments) |

Update this diagram if Azure Local deployment type limits change, Microsoft changes the platform component list, Azure Local workload names change, or the recommended Azure management services change.

### vector-embedding-process-2026.svg

| Item | Detail |
|---|---|
| File path | `/images/level-100/vector-embedding-process-2026.svg` |
| Used by | [RAG fundamentals](/level-100/module-05-foundry-local/rag-fundamentals/) |
| What it shows | A vendor-neutral retrieval-augmented generation flow. Documents are split into chunks, converted to embeddings, stored as vectors, searched by a question vector, and passed as grounding context to a language model. |

| Encoded fact | Microsoft source |
|---|---|
| RAG pipelines divide documents into chunks, generate embeddings for those chunks, and use those embeddings for vector search. | [RAG generate embeddings phase](https://learn.microsoft.com/azure/architecture/ai-ml/guide/rag/rag-generate-embeddings) |
| A RAG solution embeds the user query with the same embedding model as the chunks, then searches for semantically relevant vectors. | [RAG generate embeddings phase](https://learn.microsoft.com/azure/architecture/ai-ml/guide/rag/rag-generate-embeddings) |
| The original text of relevant chunks passes to the language model as grounding data. | [RAG generate embeddings phase](https://learn.microsoft.com/azure/architecture/ai-ml/guide/rag/rag-generate-embeddings) |
| Chunking helps retrieval by splitting large documents into smaller pieces that can be matched independently. | [Retrieval-augmented generation in Azure AI Search](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview#content-preparation-for-rag) |

Update this diagram if the Level 100 RAG page moves away from the current vendor-neutral flow, if the course adds a Microsoft-specific Foundry Local product diagram for this section, or if Microsoft Learn changes the recommended RAG sequence.

## Mermaid diagrams

| Page | Diagram title or location | What it shows |
|---|---|---|
| [Azure Arc introduction](/level-100/module-04-azure-arc/azure-arc-intro/) | Azure Arc control plane and local data planes | Azure Resource Manager projects inventory, tags, RBAC, policy, and extensions onto Arc-enabled servers, Kubernetes, SQL Managed Instance, and Arc resource bridge while workload data remains local. |
| [Azure Arc-enabled servers](/level-100/module-04-azure-arc/azure-arc-servers/) | Arc-enabled server management path | Azure tools and Azure Resource Manager send management through the Connected Machine agent to a Windows or Linux server, with Azure Policy, Azure Update Manager, and Windows Server management using the same agent path. |
| [Azure Arc-enabled Kubernetes](/level-100/module-04-azure-arc/azure-arc-kubernetes/) | Arc-enabled Kubernetes control flow | Azure Resource Manager creates the connected cluster resource, Arc agents connect the cluster, and GitOps, Azure Policy, and extensions apply to the Kubernetes cluster. |
| [Azure Arc-enabled Kubernetes](/level-100/module-04-azure-arc/azure-arc-kubernetes/) | GitOps with Flux | A pull request updates a Git repository, Flux controllers reconcile the repository into namespaces and workloads, and Azure configuration points Flux at the desired state. |
| [Foundry Local overview](/level-100/module-05-foundry-local/foundry-local-overview/) | Foundry Local family on Azure Local | Users and apps call Agentic Retrieval, which uses collections and local sources plus the Foundry Local extension and model deployments inside AKS on Azure Local, with Azure Arc management. |
| [Microsoft 365 Local architecture](/level-100/module-06-microsoft-365-local/m365-local-architecture/) | Stack view | Users reach Exchange, SharePoint, and Skype workloads on VMs. The VMs run on Azure Local and Premier Solution hardware, with either Azure connected management or a local disconnected control plane. |

## Retired images

Keep these old files so old URLs keep resolving. Do not use them in current Level 100 pages.

| Old file | Replaced by | Reason |
|---|---|---|
| `/images/level-100/eu-data-boundary.svg` | `/images/level-100/eu-data-boundary-2026.svg` | The old diagram says "customer data stays in EU," uses imprecise diagnostic and service-generated data labels, omits Professional Services Data at rest, and mixes EU Data Boundary scope with controls such as customer-managed keys and support access. |
| `/images/level-100/sovereign-cloud-models-comparison.svg` and `/images/level-100/sovereign-cloud-models-comparison.png` | `/images/level-100/sovereign-cloud-models-2026.svg` | The old spider chart and scoring matrix use subjective ratings, split connected and disconnected Azure Local into separate models, and omit the current three-model Microsoft Sovereign Cloud portfolio, Bleu, Delos Cloud, current naming, and preview tags. |
| `/images/level-100/azure-local-architecture.svg` and `/images/level-100/azure-local-architecture.png` | `/images/level-100/azure-local-architecture-2026.svg` | The old diagram centers Windows Admin Center and "AKS Hybrid." The current diagram emphasizes Azure Arc, Azure Resource Manager, Azure Policy, Azure Monitor, Microsoft Defender for Cloud, Azure Local VMs enabled by Azure Arc, AKS on Azure Local, and validated catalog hardware. |
| `/images/level-100/vector-embedding-process.svg` and `/images/level-100/vector-embedding-process.png` | `/images/level-100/vector-embedding-process-2026.svg` | The old diagram includes product and vendor names, hard-coded model comparisons, unsourced scores, and decorative icons. It also misses the query path from embedded question to top chunks, prompt, language model, and cited answer. |
| `/images/level-100/data-classification-pyramid.svg` | No current Level 100 replacement | The old pyramid is a generic classification diagram. It treats "sovereign cloud" as a top-secret-style control and uses labels such as classified, ITAR, and customer PII without the current Microsoft source framing. |

These files live under `site/public/images/level-100/` but are still referenced by Level 50 content or the resource index:

- `/images/level-100/azure-regions-map.svg` is used by [Azure global infrastructure](/level-50/module-03-azure-intro/azure-global-infrastructure/). That Level 50 page owns it.
- `/images/level-100/regulatory-timeline.svg` is used by [Compliance frameworks](/level-50/module-02-security-compliance/compliance-frameworks/). That Level 50 page owns it. The diagram is outdated because it does not show the DORA January 17, 2025 enforcement date or the November 18, 2025 designation of Microsoft Ireland Operations Limited as a Critical ICT Third-Party Provider.
- `/images/level-100/capex-opex-comparison.svg` is used by [Cloud computing primer](/level-50/module-01-cloud-computing/cloud-computing-primer/). That Level 50 page owns it.
- `/images/level-100/nist-cloud-characteristics.svg` has no current page reference under `site/src/content/docs/`. It is listed in the resources visual asset index, not owned by Level 100.

## Sources

- [What is the EU Data Boundary?](https://learn.microsoft.com/privacy/eudb/eu-data-boundary-learn)
- [What is Microsoft Sovereign Cloud?](https://learn.microsoft.com/azure/azure-sovereign-clouds/microsoft-sovereign-cloud)
- [What is Sovereign Public Cloud?](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/overview-sovereign-public-cloud)
- [Capabilities of Sovereign Public Cloud](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/sovereign-public-cloud-capabilities)
- [What is Sovereign Private Cloud?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/overview/sovereign-private-cloud)
- [GitHub Enterprise Local overview](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/github-local/github-local-overview)
- [What is Foundry Local on Azure Local?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/overview)
- [National Partner Clouds](https://learn.microsoft.com/azure/azure-sovereign-clouds/partner/overview-national-partner-clouds)
- [What are hyperconverged deployments of Azure Local?](https://learn.microsoft.com/azure/azure-local/overview/hyperconverged-overview)
- [Connected operations overview](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/azure-local/connected-operations-overview)
- [RAG generate embeddings phase](https://learn.microsoft.com/azure/architecture/ai-ml/guide/rag/rag-generate-embeddings)
- [Retrieval-augmented generation in Azure AI Search](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview)
- [What is DORA?](https://learn.microsoft.com/compliance/dora/dora-what-is-dora)
