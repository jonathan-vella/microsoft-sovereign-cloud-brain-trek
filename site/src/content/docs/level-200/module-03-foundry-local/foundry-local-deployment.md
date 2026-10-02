---
title: "Foundry Local deployment"
description: "Plan Foundry Local on Azure Local deployment requirements, model runtime choices, authentication, and ingress exposure."
lastVerified: 2026-10-02
sidebar:
  order: 2
---

Foundry Local on Azure Local serves AI models from an Arc-enabled Kubernetes cluster on Azure Local. The service is in preview, and deployment access is available by request during preview ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/overview)).

![Azure Local and AKS Arc cluster running Foundry Local inference beside Agentic Retrieval services for ingestion, collections, agents, MCP, and chat.](/images/level-200/foundry-local-agentic-retrieval-2026.svg)

## Deployment shape

Foundry Local is an Azure Arc extension. It installs an inference operator that reconciles Kubernetes resources for model serving. The `Model` custom resource defines model metadata, and the `ModelDeployment` custom resource defines runtime intent such as replicas, compute target, endpoint exposure, and authentication ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/overview#architecture-summary)).

Applications call OpenAI-compatible endpoints exposed through the cluster. Foundry Local can serve catalog models or custom models from your own registry. It also syncs model catalog metadata into the cluster so teams can discover supported models consistently.

Plan the deployment in this order:

1. Confirm preview access, Azure subscription, Entra permissions, and AKS Arc permissions.
2. Build the Azure Local and AKS Arc baseline.
3. Add worker pools sized for the selected models and runtimes.
4. Install networking, certificate, and Gateway API dependencies.
5. Deploy the Foundry Local extension.
6. Deploy one model, test inference, then add replicas and external exposure.

## Platform requirements

Foundry Local requires an AKS Arc cluster on Azure Local that runs Kubernetes 1.29 or later. The cluster must be registered with Azure Arc as a `connectedClusters` resource ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-requirements)).

Worker nodes must meet the model plan, not only the extension minimum. The documented minimum worker VM size is `Standard_D4s_v3` with 4 vCPU and 16 GiB memory. The recommended size is `Standard_D8s_v3` with 8 vCPU and 32 GiB memory. Microsoft warns not to use the `az aksarc create` default `Standard_A4_v2` worker size because it has only 8 GiB memory ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-requirements#worker-node-capacity)).

| Requirement | Minimum | Recommended design |
| --- | --- | --- |
| Kubernetes | AKS Arc 1.29 or later | Use a currently supported AKS Arc release and patch before extension install. |
| Worker node size | `Standard_D4s_v3` | `Standard_D8s_v3` or larger for production model serving. |
| Worker node count | 1 | 2 or more, especially when separating GPU and CPU pools. |
| Gateway API | Istio 1.29 or later plus Gateway API CRDs 1.4.0 or later | Treat the gateway stack as part of the platform baseline. |
| Model cache | 100 GiB PVC default | Increase for larger models and multiple replicas. |
| Disconnected Azure Local | Disconnected Operations 2604.3.0 or later | Import expansion packs and model artifacts before deployment. |

Foundry Local is available as an Azure Arc extension in 18 regions, including East US, West Europe, UK South, Japan East, and Australia East. Check the current region list before deployment because preview availability can change ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/overview#supported-regions)).

## Runtime selection

Foundry Local supports ONNX Runtime through ONNX-GenAI and vLLM for generative inference. The catalog model usually determines the runtime. For custom models, set the runtime in the `ModelDeployment` spec. The default is `onnx-genai` ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-inference-runtimes)).

| Runtime | Hardware | Best fit | Constraints |
| --- | --- | --- | --- |
| ONNX Runtime | CPU or GPU | Smaller models, CPU inference, lower overhead, edge-constrained deployments | One model per pod. Throughput is usually lower than vLLM under high concurrency. |
| vLLM | GPU only | Larger language models, high concurrency, continuous batching, efficient GPU memory use | Requires CUDA GPU and uses Hugging Face safetensors format. |

Use ONNX Runtime when the site has no GPU, when the chosen model fits CPU performance goals, or when a smaller model is enough. Use vLLM when the workload needs high throughput, long context windows, or large models on GPU. For multireplica vLLM deployments, plan extra capacity for one Endpoint Picker pod per `ModelDeployment` ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-requirements#worker-node-capacity)).

## GPU planning

GPU nodes are required for vLLM and for GPU model variants such as `*-cuda-gpu`. Foundry Local supports NVIDIA DDA-passthrough SKUs including `Standard_NC*_A2`, `Standard_NC*_L4_*`, `Standard_NC*_L40_*`, `Standard_NC*_L40S_*`, `Standard_NC*_RTX6000Pro_*`, and Tesla T4 `Standard_NK*`. AMD GPUs are not supported ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-requirements#gpu-requirements)).

Confirm three layers before you deploy a GPU model:

- The Azure Local host exposes a supported NVIDIA GPU through DDA passthrough.
- The AKS Arc GPU node pool has CUDA drivers and the NVIDIA Kubernetes device plugin.
- The selected model fits the GPU memory and context-length plan.

Foundry Local validates GPU compatibility during deployment and returns an error when resources are insufficient ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-requirements#gpu-requirements)). Test each model in a non-production cluster before you commit hardware for production.

## Model deployment resources

A production deployment should keep model metadata, model deployment intent, and client routing separate. Use the `Model` resource to declare what model is available. Use the `ModelDeployment` resource to declare how it runs.

Design each `ModelDeployment` with these fields in mind:

| Decision | Why it matters |
| --- | --- |
| Runtime and compute | Determines CPU versus GPU placement and container image selection. |
| Replica count | Drives concurrency and availability. Multireplica vLLM turns on inference-aware routing by default. |
| Context length | Controls memory pressure and conversation quality. |
| Endpoint exposure | Selects internal, external, or no gateway exposure. |
| Authentication methods | Controls whether callers use API keys, Entra ID, or service account tokens. |
| Model cache storage | Prevents repeated downloads and supports disconnected or low-bandwidth sites. |

Use the model catalog for supported models when possible. For vLLM, the catalog includes Microsoft Phi models, Mistral-7B-Instruct-v0.2, and `gpt-oss-20b` entries ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/reference-models)). Recheck the catalog before deployment because model availability changes.

## Authentication and endpoint exposure

Foundry Local supports three data-plane authentication methods: API key, Microsoft Entra ID, and Kubernetes service account token authentication ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-authentication-authorization)). API key authentication is simple and works fully inside the cluster. Entra ID adds identity-based Azure RBAC checks. Service account token authentication is for in-cluster workloads and uses Kubernetes RBAC against the selected `ModelDeployment`.

Gateway exposure is separate from authentication. Foundry Local routes model traffic through Kubernetes Gateway API with Istio as the provider. A deployment can use internal exposure, external exposure through a LoadBalancer gateway, or no gateway exposure beyond the ClusterIP service ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/whats-new#july-2026)). Use a customer-managed TLS certificate for production external endpoints.

:::tip[Pair authentication with network reach]
For line-of-business apps outside the cluster, use Gateway API with TLS and Entra ID or API keys. For pods inside the same cluster, service account token authentication avoids separate shared credentials.
:::

## Disconnected deployment

Foundry Local supports disconnected environments as of the June 2026 preview release, with Azure Local Disconnected Operations 2604.3.0 or later required ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/whats-new#june-2026)). In disconnected deployments, extension assets, Gateway API dependencies, certificates, model catalog data, and model artifacts come from imported expansion packs or local registries instead of online sources.

Disconnected design changes the operational checklist. You must stage expansion packs, certificate chains, local registry content, model artifacts, and identity configuration before deployment day. The inference endpoint can still use API key authentication and service account token authentication without public cloud reach, but Entra ID paths depend on the disconnected identity setup.

## Sources

- [What is Foundry Local on Azure Local?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/overview)
- [Requirements for Foundry Local on Azure Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-requirements)
- [Inference runtimes in Foundry Local on Azure Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-inference-runtimes)
- [Authentication and authorization in Foundry Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-authentication-authorization)
- [What's new in Foundry Local on Azure Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/whats-new)
- [vLLM runtime model reference for Foundry Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/reference-models)
