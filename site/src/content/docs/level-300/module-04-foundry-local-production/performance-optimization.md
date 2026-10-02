---
title: "Performance optimization"
description: "Choose Foundry Local runtimes, model sizes, GPU settings, routing, and context windows for production inference on Azure Local."
lastVerified: 2026-10-02
sidebar:
  order: 2
---

[Foundry Local on Azure Local is in preview](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/overview), so performance tuning starts with measurement in your cluster. Learn documents the supported runtimes, GPU planner, model caching, model parallelism, and inference-aware routing. It does not document a universal service-level objective, concurrency target, or cost formula for every model.

## Runtime decision table

Foundry Local chooses the runtime for catalog models from the model catalog entry. For custom models, you set the runtime in the `ModelDeployment` spec. Use this decision table before you size nodes or GPUs.

| Decision | ONNX-GenAI | vLLM |
| --- | --- | --- |
| Hardware | CPU or GPU | GPU only |
| Model format | ONNX | Hugging Face safetensors |
| Better fit | Smaller models, CPU inference, constrained edge environments, lower overhead | Large language models, concurrent chat, high throughput, GPU memory optimization |
| Memory behavior | Standard ONNX Runtime behavior | PagedAttention, continuous batching, KV-cache planning, chunked prefill |
| Automatic GPU tuning | Not used | vLLM planner validates memory and context settings |
| Model parallelism | Not documented for Foundry Local | Tensor parallelism and pipeline parallelism |

ONNX-GenAI is the only documented runtime for CPU generative inference. Use it when the model supports CPU and your latency target allows CPU serving, or when GPU capacity must be reserved for other workloads. vLLM is the documented GPU-only path for high-throughput generative inference, especially with concurrent chat workloads and larger models.

## Model and GPU sizing

Use the Learn model reference for model-specific values, then validate with your prompts and concurrency. The reference values below are from the [vLLM runtime model reference](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/reference-models), which is part of the preview documentation.

| Model | Publisher | Max context length | Required GPU memory on NVIDIA A10 | Design note |
| --- | --- | --- | --- | --- |
| Phi-3.5-mini-instruct | Microsoft | 29,472 | 8.428 GB | Small chat model when the application can fit below a 30K context. |
| Phi-4-mini-instruct | Microsoft | 93,520 | 7.806 GB | Larger context window than Phi-3.5-mini with lower listed A10 memory. |
| Phi-4-mini-reasoning | Microsoft | 93,520 | 7.806 GB | Use for reasoning tasks only after validating output quality and latency. |
| Mistral-7B-Instruct-v0.2 | Mistral AI | 29,328 | 15.64 GB | Higher listed A10 memory than the Phi mini models. |
| gpt-oss-20b | OpenAI | 96,784 | 14.793 GB | Recommended endpoint for Agentic Retrieval when hosted through Foundry Local. |

Agentic Retrieval adds another sizing constraint. Its requirements page recommends GPT-OSS-20B through Foundry Local. For that endpoint, Learn lists [one NVIDIA GPU with at least 24 GB VRAM as the minimum and one NVIDIA GPU with at least 48 GB VRAM for production](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/requirements#hardware-requirements-gpt-oss-20b-via-foundry-local). Do not replace those figures with generic GPU-memory estimates.

## Automatic GPU inference tuning

[Automatic GPU inference tuning](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-gpu-inference-planner) applies to generative vLLM deployments that use GPU compute. The planner reads the model configuration, inspects allocated GPUs, profiles memory with the installed vLLM runtime, and resolves a safe starting configuration.

The planner can set or validate memory-sensitive settings such as:

- `max_model_len`
- `gpu_memory_utilization`
- `enable_auto_tool_choice`
- `tool_call_parser`
- `reasoning_parser`
- `language_model_only`

The planner does not remove the need to benchmark. It gives a memory-safe starting point. If your application needs a specific combined prompt and output limit, set `max_model_len` explicitly and test the deployment under representative traffic. If the setting does not fit the available GPU memory, deployment validation fails instead of silently reducing your requested shape.

## Context window for Agentic Retrieval

Agentic Retrieval recommends a [32K token context window](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/whats-new#july-2026) for the Foundry Local model to improve retrieval and tool-use quality. Treat 32K as the starting requirement for Agentic Retrieval, not as the maximum context any Foundry Local model can support. The model reference lists higher maximum context lengths for some vLLM models, but Agentic Retrieval quality also depends on retrieval, tool calls, agent memory compaction, and the language model endpoint.

For production, test at least three traffic patterns:

1. Single-turn questions with short retrieved context.
2. Multi-turn conversations where prefix-cache locality matters.
3. Tool-heavy agentic conversations where Agentic Retrieval compacts active context.

## Model caching and StoreModel

Foundry Local caches model artifacts before it creates serving resources. The operator creates an internal `StoreModel` resource, then a cache job downloads model artifacts and pushes them to the local OCI registry. Inference pods use an init container to pull the cached model files before the main inference container starts.

`StoreModel` phases are `Pending`, `Storing`, `Available`, and `Error`. A deployment waits for `Available` before serving. If caching fails, the operator deletes the `StoreModel` so the next deployment attempt can retry.

This flow matters for performance in three ways:

- First deployment latency includes model caching time.
- Large models need enough cache job memory. In [July 2026](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/whats-new#july-2026), the StoreModel cache job default memory increased to a 16 GiB request and 32 GiB limit.
- Disconnected deployments pull catalog model artifacts from the local `edgeartifacts` registry instead of the online catalog.

## Multi-GPU model parallelism

[Multi-GPU model parallelism was added in August 2026](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/whats-new#august-2026) for vLLM deployments. Use it when the model and runtime state do not fit on one GPU, or when measured single-GPU performance does not meet workload requirements.

Foundry Local documents two strategies:

| Strategy | What it does | Use when |
| --- | --- | --- |
| Tensor parallelism | Partitions model weights across GPUs. Workers combine partial results for the same request. | A single GPU lacks memory or performance capacity, and the model supports the selected tensor parallel size. |
| Pipeline parallelism | Assigns model layer groups to different GPUs. Activations move stage by stage. | Layer partitioning fits the model or hardware better, or tensor parallel communication is too costly. |

The required GPU count for one replica is `tensor_parallel_size * pipeline_parallel_size`. Request that value in `spec.resources.limits.gpu`. Learn also states that all GPUs for one replica must be on the same cluster node. If the node cannot provide the requested GPUs, the pod remains `Pending`.

## Inference-aware routing effect

Endpoint Picker (EPP) is enabled by default for multi-replica vLLM deployments. It routes by live backend signals instead of round-robin. Learn reports two measured effects for a three-replica vLLM deployment with output capped at 256 tokens:

- For single-turn traffic with 20 concurrent users, average time to first token was [14 percent lower](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-inference-runtimes#performance-benefits) than Gateway round-robin.
- For three-turn chat, per-user throughput was [16 percent higher at one concurrent user and 10 percent higher at five concurrent users](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-inference-runtimes#performance-benefits).

Those numbers describe the documented test shape, not a guarantee for every deployment. EPP is most useful when queue depth, KV-cache use, or prefix-cache locality affects the user experience. Learn says you may disable EPP for throughput-maximizing batch workloads with very long unbounded outputs at high concurrency, where the ExtProc cost can outweigh the routing benefit.

## Performance design checklist

| Question | Decision |
| --- | --- |
| Does the model support CPU and meet latency needs on CPU? | Start with ONNX-GenAI CPU only if the workload proves acceptable without GPU. |
| Does the workload need concurrent chat throughput? | Prefer vLLM on GPU and test EPP with realistic multi-turn traffic. |
| Does the model exceed a single GPU's capacity? | Use vLLM model parallelism, and place all GPUs for one replica on the same node. |
| Does Agentic Retrieval call the endpoint? | Configure a 32K context window unless testing proves a different setting is acceptable. |
| Will the deployment run disconnected? | Import the extension and model expansion packs, then sync the catalog before deployment. |
| Is first deployment time a problem? | Treat model caching as part of rollout time and size cache job resources. |

## Sources

- [Inference runtimes in Foundry Local on Azure Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-inference-runtimes)
- [Automatic GPU inference tuning with vLLM planner in Foundry Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-gpu-inference-planner)
- [Model caching and StoreModel lifecycle in Foundry Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-model-caching)
- [Model parallelism for multi-GPU inference in Foundry Local on Azure Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-model-parallelism)
- [vLLM runtime model reference for Foundry Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/reference-models)
- [Requirements for Foundry Local on Azure Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-requirements)
- [What's new in Foundry Local on Azure Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/whats-new)
- [What's new in Agentic Retrieval in Foundry Local](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/whats-new)
- [What you need for Agentic Retrieval in Foundry Local](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/requirements)
