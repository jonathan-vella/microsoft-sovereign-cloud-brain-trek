---
title: "Foundry Local operations"
description: "Operate Foundry Local and Agentic Retrieval with evaluation, monitoring, authentication, updates, disconnected operations, and support diagnostics."
lastVerified: 2026-10-02
sidebar:
  order: 5
---

Operating Foundry Local on Azure Local means managing Kubernetes health, model quality, authentication, gateway exposure, and preview release change. The same runbook should cover Agentic Retrieval when the two extensions are deployed together.

## Model evaluation

Foundry Local added on-cluster model evaluation in the August 2026 preview release. You can upload a test dataset, run evaluators, and download structured results. Evaluation runs inside your environment, and Microsoft says no data leaves the cluster. It supports NLP metrics such as F1, BLEU, and ROUGE, plus quality evaluators that use a second deployed model as a judge for coherence, fluency, relevance, and similarity ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/whats-new#august-2026)).

Use evaluation before you promote a model or change context length. A useful test set should include normal user prompts, long prompts, tool-heavy prompts, refusal cases, and prompts that should retrieve local content. If Agentic Retrieval supplies the context, run both model-only and knowledge-grounded tests so you can separate model behavior from retrieval behavior.

Evaluation also works in disconnected environments ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/whats-new#august-2026)). That matters for regulated sites because you can keep test datasets and outputs inside the local boundary.

## Monitoring and diagnostics

Foundry Local troubleshooting starts with Kubernetes state. Microsoft recommends checking operator pods, cert-manager pods, certificates, and `ModelDeployment` resources before deeper debugging ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/troubleshoot#check-core-component-health)). For support cases, collect recent events, pod descriptions, and component logs by using `az k8s-extension troubleshoot`, `kubectl get events`, `kubectl describe modeldeployment`, and `kubectl logs` ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/troubleshoot#collect-diagnostic-logs-for-support)).

| Signal | Command or source | What it tells you |
| --- | --- | --- |
| Operator health | `kubectl get pods -n foundry-local-operator` | Whether the control plane is running. |
| Certificate health | `kubectl get certificates -n foundry-local-operator` | Whether TLS dependencies are ready. |
| Deployment status | `kubectl get modeldeployment -A` | Which models are deployed and whether reconciliation succeeded. |
| Scheduling issues | `kubectl get events -A --sort-by=.lastTimestamp` | Pending pods, node pressure, missing secrets, or device issues. |
| Resource pressure | `kubectl top nodes` and `kubectl top pods -A` | CPU and memory pressure during inference. |
| Support bundle | `az k8s-extension troubleshoot` | Extension diagnostics for escalation. |

Agentic Retrieval publishes metrics to Azure Monitor for the installed extension. You can view them in the Azure portal from the AKS cluster on Azure Local extension blade or in Azure Managed Grafana by selecting the Kubernetes Azure Arc resource and the `Microsoft.KubernetesConfiguration/extensions` namespace ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/observability)). Use those metrics with cluster infrastructure monitoring from Azure Monitor for containers.

## Authentication operations

Foundry Local supports API key, Entra ID, and Kubernetes service account token authentication for data-plane inference requests ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-authentication-authorization)). These methods can coexist on the same inference endpoint, but each request must send one credential type.

API keys are generated as primary and secondary keys and stored in Kubernetes Secrets. They work inside the cluster and do not need external Azure connectivity. Entra ID validates JWTs and checks Azure RBAC. It caches signing keys and RBAC results, but extended Azure Resource Manager loss can produce `503` for callers without a cached authorization result. Service account token authentication is for in-cluster workloads. It uses Kubernetes TokenReview and SubjectAccessReview and fails closed if Kubernetes authentication or authorization cannot be checked.

Use this selection rule:

| Caller | Preferred authentication | Reason |
| --- | --- | --- |
| In-cluster application | Kubernetes service account token | No shared key, Kubernetes RBAC scoped to the `ModelDeployment`. |
| Enterprise user or app outside the cluster | Entra ID | Per-identity authorization and Azure RBAC. |
| Automation, fallback, or disconnected service path | API key | Simple and resilient when external identity services are unavailable. |

For Agentic Retrieval with Foundry Local managed identity, assign all required roles from the Agentic Retrieval deployment overview. Azure RBAC alone is not enough because the Foundry authentication sidecar also validates Entra app roles ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/deploy-overview#required-roles-for-foundry-local-inference)).

## Updates and version tracking

Foundry Local releases are tied to extension versions. Recent 2026 preview releases added multi-node support, disconnected operations, vLLM, model caching, Gateway API routing, Endpoint Picker routing, model evaluation, multi-GPU model parallelism, and service account token authentication ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/whats-new)). Track these changes by extension version because preview behavior can change before general availability.

Agentic Retrieval uses its own extension versions. The June 2026 `0.9.3` release renamed the product and changed the architecture by removing bundled language models. The July 2026 `0.9.5` release added ingestion reliability improvements, context compaction, NetworkPolicy enforcement checks, and disconnected improvements ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/release-notes)).

A safe update plan includes:

1. Export current extension configuration, model deployments, and collection inventory.
2. Read release notes for breaking behavior, security fixes, and new prerequisites.
3. Test extension updates in a non-production AKS Arc cluster with representative models and collections.
4. Run model evaluation and Agentic Retrieval chat tests before promoting the update.
5. Keep the previous model deployment online until the new deployment meets latency and quality targets.

## Disconnected operations

Foundry Local supports disconnected deployments when Azure Local Disconnected Operations is version 2604.3.0 or later ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-requirements#requirements-by-environment)). In disconnected mode, extension dependencies, Gateway API components, certificate tools, model artifacts, and catalog data are sourced from imported expansion packs or local registries.

Agentic Retrieval disconnected deployments also use expansion packs. You import the Agentic Retrieval expansion pack in a connected environment, transfer it to the disconnected environment, and import it on the Azure Local Disconnected Operations machine. The extension then pulls container images and model artifacts from the local `edgeartifacts` registry ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/disconnected-operations/overview-disconnected)).

Disconnected operations require stricter release management. Record which expansion-pack versions, model artifacts, certificates, and extension settings were imported. Treat each update as a controlled content transfer.

## Security fixes and vulnerability response

Do not assume a fixed security-fix cadence for preview extensions. Instead, monitor the current release notes. Agentic Retrieval release notes show security work in specific releases. For example, the February 2026 preview release fixed a critical Next.js denial-of-service vulnerability and a high-severity Langchain XML External Entity vulnerability ([Learn](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/release-notes#february-2026)).

For production planning, define who reads release notes, who imports expansion packs for disconnected sites, who approves extension updates, and how fast critical fixes must be deployed after validation.

## Common incident paths

| Symptom | First checks | Likely area |
| --- | --- | --- |
| Model pod stays pending | Node capacity, pod limits, GPU plugin, events | Scheduling or capacity. |
| GPU memory error | Model context length, replica count, vLLM preferences | Runtime sizing. |
| TLS secret missing | cert-manager pods, certificates, trust-manager | Certificate management. |
| SAT request fails | `satAuth.enabled`, `ModelDeployment` auth methods, service account RBAC | Kubernetes auth. |
| Agentic Retrieval query returns 403 | Entra roles, collection-specific app role | Collection authorization. |
| Evaluation fails | Model under test, judge model, pod readiness | Model availability. |

End each incident review with a change to the deployment checklist, monitoring chart, or test set. If the failure came from source data quality, update the ingestion validation process rather than only the cluster runbook.

## Sources

- [What's new in Foundry Local on Azure Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/whats-new)
- [Troubleshoot Foundry Local on Azure Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/troubleshoot)
- [Authentication and authorization in Foundry Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-authentication-authorization)
- [Requirements for Foundry Local on Azure Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-requirements)
- [Deployment overview for Agentic Retrieval in Foundry Local](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/deploy-overview)
- [Monitor Agentic Retrieval in Foundry Local](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/observability)
- [Release notes for Agentic Retrieval in Foundry Local](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/release-notes)
- [Disconnected operations for Agentic Retrieval in Foundry Local](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/disconnected-operations/overview-disconnected)
