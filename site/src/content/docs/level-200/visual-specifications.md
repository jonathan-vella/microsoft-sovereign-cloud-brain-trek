---
title: "Level 200 visual specifications"
description: "Internal specifications for the Level 200 diagrams: the SVG files, the Mermaid diagrams, their sources, and the retired assets they replace."
lastVerified: 2026-10-02
sidebar:
  hidden: true
---

This page describes every diagram used in Level 200 so authors can update a diagram when its facts change. It lists
the SVG files in `site/public/images/level-200/`, the Mermaid diagrams written inline in pages, and the older assets
that stay on disk only so their URLs keep working.

## Style rules for Level 200 SVGs

- Hand-written SVG with a `viewBox` about 960 units wide. No embedded raster images and no external fonts.
- `role="img"` with `aria-labelledby` pointing at a `<title>` and a `<desc>`. The `desc` states the facts the diagram
  shows, so a screen reader user gets the same content.
- Real `<text>` elements in sentence case, at least 12 units high, Segoe UI font stack.
- Fluent 2 and Azure palette: blue `#0F6CBD` and `#2886DE` for Azure and Arc, green `#107C10` for workloads and
  outputs, orange `#FF8C00` for customer-side or external parts, light backgrounds `#F7FAFD` and `#E6F2FD`. The
  reference is `site/public/images/hero/sovereign-cloud-hero-2026.svg`.
- Every label must match the page that uses the diagram. Show preview status in the label when a feature is preview.
- To replace a diagram, add a new file name, update the page reference and alt text, and keep the old file.

## SVG diagrams

| File | Used on | What it shows | Replaces |
|---|---|---|---|
| `storage-spaces-direct-2026.svg` | [Azure Local architecture deep dive](/level-200/module-01-azure-local/azure-local-architecture-deep-dive/) | Hyperconverged storage path: machines with direct-attached drives, the storage bus, the shared pool, resiliency (mirror, dual parity, fault domains), CSV volumes, and Azure Local VMs and AKS. Notes that SAN-backed designs use the disaggregated or multi-rack types. | `storage-spaces-direct.svg` |
| `sdn-architecture-2026.svg` | [Azure Local advanced networking](/level-200/module-01-azure-local/azure-local-advanced-networking/) | SDN enabled by Azure Arc (2506 or later): Azure portal, CLI, and ARM manage logical networks and NSGs through Azure Arc. Network Controller runs as a Failover Cluster service. Virtual networks, SLB, VPN, and L3/GRE gateways are marked as not supported. | `sdn-architecture.svg` |
| `enterprise-arc-topology-2026.svg` | [Arc enterprise patterns](/level-200/module-02-arc/arc-enterprise-patterns/) | Azure landing zone governance (management groups, Azure Policy, RBAC, tags, cost) over Arc resource groups, private cloud operations through Arc resource bridge (Azure Local, VMware vSphere 7.0 or 8.0, SCVMM), and connectivity choices (Arc gateway, Private Link, ExpressRoute or VPN). | `enterprise-arc-topology.svg` |
| `foundry-local-agentic-retrieval-2026.svg` | [Foundry Local deployment](/level-200/module-03-foundry-local/foundry-local-deployment/) | Azure Local with an AKS Arc cluster hosting two sibling Arc extensions: Foundry Local (inference operator, Model and ModelDeployment CRDs, ONNX Runtime or vLLM) and Agentic Retrieval `microsoft.arc.rag` (ingestion, Collections on Milvus and Postgres, agents runtime, MCP server with six search tools, chat UI). | `edge-rag-implementation.svg` |
| `compliance-security-patterns-2026.svg` | [Compliance and security patterns](/level-200/module-05-compliance/compliance-security-patterns/) | Requirements (NIS2, DORA, GDPR, EU AI Act, FedRAMP, sovereign control levels) mapped to Defender for Cloud, Azure Policy, Compliance Manager, Microsoft Entra and Arc, then to evidence outputs. | `security-patterns-matrix.svg` |
| `fedramp-boundaries-2026.svg` | [FedRAMP compliance](/level-200/module-05-compliance/fedramp-compliance/) | Azure commercial and Azure Government FedRAMP High P-ATO scope, the three US Gov regions (only Virginia with availability zones), the two DoD regions, Azure Government Secret, and Azure Government Top Secret. | `fedramp-control-families.svg` |
| `encryption-key-hierarchy-2026.svg` | [Encryption key management](/level-200/module-06-sovereign-public-cloud-controls/encryption-key-management/) | Managed HSM (FIPS 140-3 Level 3, customer-controlled security domain) and the EKM preview path through a customer-run EKM Proxy (wrapKey and unwrapKey only), wrapping data-encryption keys for storage, confidential compute with Secure Key Release, and evidence. | `encryption-key-hierarchy.svg` |

## Mermaid diagrams

These diagrams are fenced `mermaid` blocks in the pages. The site applies the Azure palette at build time.

| Page | Diagram |
|---|---|
| [Azure Local high availability patterns](/level-200/module-01-azure-local/azure-local-ha-patterns/) | HA stack: validated hardware, failover clustering, Storage Spaces Direct or SAN, redundant networking, VMs and AKS, backup and DR, and solution updates. |
| [Arc policy and governance](/level-200/module-02-arc/arc-policy-and-governance/) | Policy flow from a management group assignment to Arc-enabled servers (machine configuration) and Arc-enabled Kubernetes (Azure Policy extension and Gatekeeper). |
| [Inference runtimes and GPUs](/level-200/module-03-foundry-local/inference-runtimes-and-gpus/) | Request path: Gateway API with TLS, authentication (API key, Entra ID, or service account token), then ONNX Runtime (CPU or GPU) or vLLM (GPU only, Endpoint Picker for multireplica). |
| [Pre-sales solution design](/level-200/module-04-presales/presales-solution-design/) | From discovery requirements to an operating boundary: Sovereign Public Cloud controls or the Sovereign Private Cloud stack, then Azure Local deployment type and workload zones. |
| [GDPR implementation](/level-200/module-05-compliance/gdpr-implementation/) | Controller and processor roles: the customer defines purpose and selects services and regions, Microsoft processes under instructions, and DSR and DPIA evidence is kept. |
| [Sovereign Public Cloud controls](/level-200/module-06-sovereign-public-cloud-controls/sovereign-public-cloud-controls/) | The four capabilities and the EU Data Boundary mapped to Level 1, 2, and 3 controls. |
| [Private cloud stack architecture](/level-200/module-07-sovereign-private-cloud-stack/private-cloud-stack-architecture/) | Azure Local as the platform for Microsoft 365 Local, GitHub Enterprise Local, Foundry Local, and Agentic Retrieval across connected and disconnected operations. |

## Retired assets

These files stay in `site/public/images/level-200/` so old links keep working. No Level 200 page uses them. Don't
reference them in new content.

| File | Why it was retired |
|---|---|
| `edge-rag-implementation.svg` | Shows Edge RAG with bundled language models. Edge RAG was renamed Agentic Retrieval in June 2026 and no longer bundles a model. |
| `storage-spaces-direct.svg`, `sdn-architecture.svg`, `enterprise-arc-topology.svg` | Generated diagrams with numbers and topology details that couldn't be verified against Microsoft Learn. |
| `security-patterns-matrix.svg`, `security-patterns-matrix.png` | Matrix included unverified coverage claims. |
| `fedramp-control-families.svg`, `fedramp-control-families.png` | Showed control-family counts instead of the Azure and Azure Government authorization boundaries the page teaches. |
| `encryption-key-hierarchy.svg` | Generic key hierarchy without the Managed HSM and External Key Management status. |

## Sources

- [Storage Spaces Direct overview](https://learn.microsoft.com/azure/azure-local/concepts/storage-spaces-direct-overview)
- [Software defined networking enabled by Azure Arc on Azure Local](https://learn.microsoft.com/azure/azure-local/concepts/sdn-overview)
- [Azure Arc resource bridge overview](https://learn.microsoft.com/azure/azure-arc/resource-bridge/overview)
- [What is Foundry Local on Azure Local?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/overview)
- [What's new in Agentic Retrieval in Foundry Local](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/whats-new)
- [Regulatory compliance standards in Microsoft Defender for Cloud](https://learn.microsoft.com/azure/defender-for-cloud/concept-regulatory-compliance-standards)
- [Federal Risk and Authorization Management Program](https://learn.microsoft.com/azure/compliance/offerings/offering-fedramp)
- [Managed HSM External Key Management](https://learn.microsoft.com/azure/key-vault/managed-hsm/external-key-management-overview)
