---
title: "Level 300 visual specifications"
description: "Specifications for the Level 300 diagrams: what each SVG and Mermaid diagram shows, the facts it depends on, and the style rules."
lastVerified: 2026-10-02
sidebar:
  hidden: true
---

This page describes the diagrams used in Level 300. Use it when you update a diagram or check one against current
Microsoft Learn facts. Every SVG lives in `site/public/images/level-300/` and is referenced with a root-relative
`/images/level-300/<name>.svg` path.

## Style rules

- Palette: Fluent 2 and Azure colors. Blue `#0F6CBD` for Azure and cloud services, green `#107C10` for on-premises
  and compute, orange `#C25E00` for items added by a new capability or for preview badges, purple `#5C2E91` for
  identity, policy, and routing, gray `#616161` for supporting or out-of-scope items.
- Background: the light gradient from `#F7FAFD` to `#EEF5FC` used by the 2026 hero image.
- Text: real `<text>` elements in `Inter Variable, Segoe UI, sans-serif`, 11 px minimum, 22 px titles.
- Accessibility: each SVG has `role="img"`, a `<title>`, and a `<desc>` that states the facts in the drawing. Pages
  add alt text that describes the content, not the shape.
- Status: mark preview features in the drawing itself, with a badge or "(preview)" in the label.
- Prefer Mermaid for simple flows. Use an SVG when the layout carries meaning, such as a hierarchy or a boundary.
- When a diagram goes out of date, draw a new file with a new name, for example `<name>-2026.svg`, and keep the old
  file so its URL keeps working.

## Current SVG diagrams

| File | Used on | What it shows | Facts it depends on |
|---|---|---|---|
| `azure-local-disconnected-operations-2026.svg` | [Disconnected operations](/level-300/module-01-azure-local-advanced/azure-local-disconnected-operations/) | Customer datacenter with no Azure connection. A management cluster of three or more machines runs the local control plane (portal, Azure Resource Manager, RBAC, managed identity, Key Vault, Container Registry, Azure Policy, Arc-enabled servers) and manages workload instances with Azure Local VMs, AKS (preview), Arc-enabled Kubernetes (preview), and Microsoft 365 Local. Active Directory with AD FS, customer PKI, and transferred media feed the appliance. | GA from Azure Local 2602, supported services table, AKS preview, identity and PKI integration ([Learn](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview)) |
| `sovereign-landing-zone-2026.svg` | [SLZ architecture](/level-300/module-02-sovereign-landing-zone/slz-architecture/) | Management group hierarchy. Platform with Management, Connectivity, Identity, and the added Security group with Managed HSM. Landing zones with Public, Online, Corp, and the added Confidential Online and Confidential Corp, each with its Level 1 to 3 badges. Sandbox and Decommissioned shown as ALZ carry-over groups. | Management group table and control levels ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/implement-controls-principles)) |
| `foundry-local-production-2026.svg` | [Foundry Local in production](/level-300/module-04-foundry-local-production/) | Clients and Agentic Retrieval (formerly Edge RAG) call a Gateway API (Istio) endpoint with TLS. The gateway routes to ONNX-GenAI deployments directly, and the Endpoint Picker routes multi-replica vLLM deployments on NVIDIA GPU nodes by live inference signals. The inference operator, Model and ModelDeployment resources, and the StoreModel cache sit in a multi-node AKS cluster on Azure Local. Preview badge. | Components, runtimes, Gateway API and routing, multi-node, auth options ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/whats-new)) |
| `foundry-local-model-lifecycle-2026.svg` | [Model lifecycle](/level-300/module-04-foundry-local-production/model-lifecycle/) | Six stages: source (catalog sync, expansion pack in the EdgeArtifacts registry, or your own OCI registry), cache, deploy, evaluate on the cluster, serve through the gateway, monitor. A loop shows a new model version. Preview badge. | Disconnected model sourcing and evaluation ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/disconnected-operations/concept-overview)) |
| `zero-trust-pillars-2026.svg` | [Zero Trust architecture](/level-300/module-05-zero-trust/zero-trust-architecture/) | Three principles, Conditional Access as the policy engine, seven technology pillars with example products (SecOps highlighted), and the four-layer adoption model. | Seven pillars and adoption layers ([Learn](https://learn.microsoft.com/security/zero-trust/deploy/overview)) |
| `security-monitoring-flow.svg` | [Zero Trust monitoring](/level-300/module-05-zero-trust/zero-trust-monitoring/) | Security data sources, Log Analytics, Microsoft Sentinel, Defender for Cloud, detection rules, playbooks, and reporting. Kept because its labels are generic and still accurate. | Defender for Cloud and Sentinel roles ([Learn](https://learn.microsoft.com/azure/defender-for-cloud/defender-for-cloud-introduction)) |

## Replaced SVG diagrams

These files stay in the repository so old links keep working. Level 300 pages no longer reference them.

| Old file | Replaced by | Why |
|---|---|---|
| `edge-rag-production.svg` | `foundry-local-production-2026.svg` | Edge RAG is now Agentic Retrieval. The old drawing showed bundled Phi-3 and Mistral models and AKS-HCI naming. |
| `mlops-pipeline.svg` | `foundry-local-model-lifecycle-2026.svg` | Showed an Edge RAG fine-tuning pipeline that does not match the Foundry Local lifecycle. |
| `air-gapped-architecture.svg` | `azure-local-disconnected-operations-2026.svg` | Showed Windows Admin Center as the management plane and no management cluster or local control plane. |
| `sovereign-landing-zone.svg` | `sovereign-landing-zone-2026.svg` | Missing the Public, Confidential Online, Confidential Corp, and Security management groups. |
| `zero-trust-architecture.svg` | `zero-trust-pillars-2026.svg` | Did not show the seven technology pillars. |
| `azure-local-multisite.svg` | Mermaid on the multi-site page | Showed synchronous replication between sites, which current Azure Local guidance does not describe. |
| `financial-services.svg` | Mermaid on the financial services page | Labeled Managed HSM as FIPS 140-2. Managed HSM is FIPS 140-3 Level 3. |
| `government-cloud.svg` | Mermaid on the government cloud page | Impact-level placement could not be verified on Microsoft Learn. |
| `healthcare-sovereign.svg`, `observability-stack.svg` | Mermaid on the healthcare and observability pages | Depended on details that could not be verified, such as a HIPAA workbook and a fixed retention period. |
| `multi-region-sovereign.svg`, `hybrid-identity.svg` | Not used | The SLZ page now uses one hierarchy diagram. |

Other Level 300 SVGs (`api-gateway-patterns.svg`, `event-driven-architecture.svg`, `data-mesh-sovereignty.svg`,
`disaster-recovery-topology.svg`, `critical-infrastructure.svg`) are not referenced by Level 300 pages. The pattern
pages use Mermaid.

## Mermaid diagrams

Mermaid blocks use the site-wide Azure palette from `site/astro.config.mjs`. Keep them to about 15 nodes, quote
labels that contain spaces, and update them with the page text.

| Page | Diagram |
|---|---|
| [Multi-site](/level-300/module-01-azure-local-advanced/azure-local-multi-site/) | Separate Azure Local instances per site with recovery between them and central Arc management |
| [Certificate management](/level-300/module-01-azure-local-advanced/azure-local-certificate-management/) | Certificate and secret rotation flow |
| [Architecture patterns](/level-300/module-03-architecture-patterns/) and its five pattern pages | Pattern flows for API gateways, events, data mesh, disaster recovery, and DevSecOps |
| [Production architecture](/level-300/module-04-foundry-local-production/production-architecture/) | Foundry Local and Agentic Retrieval component layout |
| [Zero Trust architecture](/level-300/module-05-zero-trust/zero-trust-architecture/) | Request flow through the policy engine |
| [Observability stack](/level-300/module-06-operations/observability-stack/), [incident response](/level-300/module-06-operations/incident-response/), [troubleshooting](/level-300/module-06-operations/troubleshooting/) | Telemetry flow, incident lifecycle, troubleshooting method |
| [Industry solutions](/level-300/module-07-industry-solutions/) and its four industry pages | Reference architectures per industry |

## Sources

- [Disconnected operations for Azure Local](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview)
- [Plan your identity for disconnected operations on Azure Local](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-identity)
- [Implement controls and principles in SLZ](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/implement-controls-principles)
- [What's new in Foundry Local on Azure Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/whats-new)
- [Foundry Local on Azure Local in disconnected environments overview](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/disconnected-operations/concept-overview)
- [Zero Trust deployment overview](https://learn.microsoft.com/security/zero-trust/deploy/overview)
- [What is Microsoft Defender for Cloud?](https://learn.microsoft.com/azure/defender-for-cloud/defender-for-cloud-introduction)
- [Azure Key Vault Managed HSM overview](https://learn.microsoft.com/azure/key-vault/managed-hsm/overview)
- [Azure architecture icons](https://learn.microsoft.com/azure/architecture/icons/)
