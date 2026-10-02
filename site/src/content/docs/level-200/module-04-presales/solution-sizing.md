---
title: "Solution sizing"
description: "Build a sizing model for Azure Local, disconnected operations, Microsoft 365 Local, Foundry Local, and Agentic Retrieval."
lastVerified: 2026-10-02
sidebar:
  order: 3
---

Solution sizing converts discovery facts into a bill of materials and a risk list. Use Microsoft Learn limits where they exist, then label every workload-specific number as a measured value, partner input, or assumption.

## Sizing workflow

1. Choose the Microsoft Sovereign Cloud deployment model.
2. For Sovereign Private Cloud, choose the Azure Local deployment type.
3. Identify workload support limits for that deployment type.
4. Capture workload measurements, including users, throughput, storage, recovery, network, GPU, and growth.
5. Add management-plane capacity, disconnected operations capacity, and high availability requirements.
6. Separate sourced Microsoft limits from example assumptions.
7. Validate with the Azure Local sizer, OEM partner tools, or a proof of concept.

The [Azure Local deployment-type guide](https://learn.microsoft.com/azure/azure-local/plan/find-your-deployment-type) links to the Azure Local sizer tool. Use it as a starting point, then validate the result with the hardware partner because Microsoft 365 Local and disconnected operations also have partner-specific design inputs.

## Deployment type limits

| Deployment type | Sizing limit from Learn | Sizing implication |
| --- | --- | --- |
| Hyperconverged | 1 to 16 machines, with rack-aware clusters capped at 8 machines | Good default when compute and storage scale together. Check whether rack awareness lowers the maximum. |
| Disaggregated | 1 to 64 machines with SAN storage | Use when compute and storage grow at different rates or storage procurement is separate. |
| Multi-rack | Prescriptive racks that scale to hundreds of machines, with shared fact-pack guidance of up to 128 nodes per instance | Use for large rack-scale environments, but do not size Microsoft 365 Local or GitHub Enterprise Local on this type. |
| Small form factor | Compact appliance for space and power constrained sites | Use for branch or edge. AI workloads and Foundry Local are preview on this type. |

[Disconnected operations is a connectivity mode](https://learn.microsoft.com/azure/azure-local/plan/find-your-deployment-type), not a fifth deployment type. It applies to hyperconverged and disaggregated deployments.

## Azure Local system requirements and hardware path

Start with the Azure Local catalog and the deployment-type article. For each candidate design, record:

- Number of Azure Local machines and whether storage is hyperconverged or SAN-backed.
- CPU cores per machine, because Azure Local host billing is per physical core unless an OEM license or Azure Hybrid Benefit changes the commercial model.
- RAM per machine, including headroom for failover and updates.
- Storage capacity, drive type, resiliency, and boot drive size.
- Network topology, switch requirements, VLANs, latency, and routable IP requirements.
- GPU SKUs, driver support, and DDA passthrough if AI workloads need GPUs.
- Hardware catalog category, such as Premier Solution, Integrated System, or Validated Node.

For Microsoft 365 Local, the Learn page says the solution must run on an Azure Local Premier Solution and through a Microsoft-certified Microsoft 365 Local solution partner. Treat partner sizing as required, not optional.

## Disconnected operations management cluster

Disconnected operations adds a local control plane. [Production deployments require a dedicated three-node Azure Local management cluster](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-control-plane-appliance). Do not run tenant workloads on it.

| Management cluster profile | Minimum nodes | Per-node requirements | Intended scale |
| --- | --- | --- | --- |
| Standard configuration | 3 | 128 GB RAM, 24 physical cores, 6 drives of at least 2 TB, 960 GB boot drive | Medium deployments, 100+ nodes |
| Datacenter configuration | 3 | 512 GB RAM, 24 physical cores, 8 drives of at least 2 TB, 960 GB boot drive | Large datacenter scale, 1000+ nodes |
| Proof of concept | 4-node hardware configuration | Microsoft recommends the production-capable hardware profile. If you diverge, the control-plane nodes need at least 256 GB RAM, 24 cores, 4 TB dedicated SSD or NVMe storage, and a 960 GB boot drive. | Evaluation and test configurations |

The proof-of-concept patterns can emphasize management, workload, or multi-cluster management. Use them to prove operating behavior before committing to the production layout.

## Foundry Local GPU sizing

[Foundry Local on Azure Local is in preview](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-requirements). It runs on AKS Arc on Azure Local and supports CPU-backed and GPU-backed model deployments.

Foundry Local sizing starts with worker node capacity:

| Requirement | Minimum | Recommended |
| --- | --- | --- |
| Worker node VM size | Standard_D4s_v3, 4 vCPU and 16 GiB | Standard_D8s_v3, 8 vCPU and 32 GiB |
| Allocatable memory per node | At least 14 GiB | At least 28 GiB |
| Worker node count | 1 | 2 or more for high availability or GPU pool separation |

For GPU workloads, Foundry Local supports NVIDIA DDA-passthrough SKUs including Standard_NC*_A2, Standard_NC*_L4_*, Standard_NC*_L40_*, Standard_NC*_L40S_*, Standard_NC*_RTX6000Pro_*, and Tesla T4 Standard_NK*. AMD GPUs are not supported. The cluster must also have NVIDIA CUDA drivers and the Kubernetes device plugin.

The default model cache persistent volume claim is 100 GiB. Increase model cache storage for large models or multiple replicas.

## Agentic Retrieval sizing

[Agentic Retrieval in Foundry Local is in preview](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/requirements). It does not bundle a language model. You provide an OpenAI-compatible chat completions endpoint, with GPT-OSS-20B via Foundry Local on Azure Local recommended in the Learn requirements.

| Requirement | Minimum or recommended value |
| --- | --- |
| Combined mode cluster capacity | 3 Standard_D8s_v3 CPU workers plus 1 GPU worker, 24+ total vCPU, 96+ GB RAM, and 60+ pods |
| Knowledge-only mode cluster capacity | 2 Standard_D8s_v3 CPU workers, 0 to 1 GPU worker, 16 total vCPU, and 64 GB RAM |
| Embedding GPUs | 2 GPU-enabled VMs in the node pool, one for BGE-M3 text embedding and one for CLIP ViT-L/14 image processing |
| Language model endpoint | Required in all modes |
| NFS data source | Required for combined and knowledge modes, not required for agentic mode |

If the language model endpoint is GPT-OSS-20B on Foundry Local, size it separately:

| Resource | Minimum | Recommended for production |
| --- | --- | --- |
| GPU | 1 NVIDIA GPU with at least 24 GB VRAM | 1 NVIDIA GPU with at least 48 GB VRAM |
| CPU | 8+ vCPUs | 16+ vCPUs |
| RAM | 32 GB | 64 GB |
| Storage | At least 50 GB | 50 to 100 GB per replica |

Combined mode therefore needs capacity for the Agentic Retrieval CPU and embedding workers plus the separate language model GPU endpoint.

## Microsoft 365 Local sizing

[Microsoft 365 Local is generally available](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/m365-local/microsoft-365-local-overview) and must be deployed through a Microsoft 365 Local solution partner certified by Microsoft. Its Learn page gives an example large-scale connected-mode reference architecture:

| Role | Example allocation |
| --- | --- |
| SharePoint Server and SQL Server workloads | Three servers configured as a three-node Azure Local instance |
| Exchange Server mailbox roles | Four servers, each configured as a single-node Azure Local instance |
| Exchange Server edge transport roles | Two servers, each configured as a single-node Azure Local instance |

The same page states that alternative configurations support different scales. Use the example to understand role separation, not as a default bill of materials. The partner must size mailbox count, SharePoint content, SQL Server needs, network segmentation, identity, backup, and disconnected or connected control plane.

## Worked example

This example shows how to label sourced facts and assumptions. It is not a recommendation.

| Design item | Value | Source or assumption |
| --- | --- | --- |
| Deployment type | Hyperconverged | Assumption based on need for Microsoft 365 Local and GitHub Enterprise Local, which are supported on hyperconverged and disaggregated only. |
| Cluster size | 6 Azure Local machines | Example assumption. Validate with Azure Local sizer and partner tools. |
| Connectivity mode | Connected | Assumption. Customer can meet the 30-day outbound connectivity requirement. |
| AI workload | Foundry Local on Azure Local | Preview status from Microsoft Learn. |
| Foundry Local worker baseline | 2 Standard_D8s_v3 workers | Recommended worker size and high availability direction from Learn. |
| Agentic Retrieval mode | Combined mode | Example assumption for knowledge plus agents. |
| Agentic Retrieval cluster capacity | 3 Standard_D8s_v3 CPU workers plus 1 GPU worker | Learn minimum for combined mode. |
| GPT-OSS-20B endpoint | 1 NVIDIA GPU with at least 48 GB VRAM | Learn recommended production value. |
| Microsoft 365 Local | Partner-sized | Learn requires certified partner deployment on Azure Local Premier Solution. |

Use this format in a customer proposal so reviewers can separate documented product requirements from assumptions that need validation.

## Sizing risks to call out

- Preview services can change before general availability.
- GPU model availability differs by OEM, region, and procurement path.
- Disconnected operations adds management cluster cost before workload capacity.
- Microsoft 365 Local and GitHub Enterprise Local restrict deployment type choice.
- AI sizing cannot be completed from user count alone. Measure model, context window, concurrency, document size, retrieval mode, and latency targets.

## Sources

- [Find your Azure Local deployment type](https://learn.microsoft.com/azure/azure-local/plan/find-your-deployment-type)
- [What are hyperconverged deployments of Azure Local?](https://learn.microsoft.com/azure/azure-local/overview/hyperconverged-overview)
- [Connected operations overview](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/azure-local/connected-operations-overview)
- [Disconnected operations for Azure Local](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview)
- [Dedicated management cluster for disconnected operations](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-control-plane-appliance)
- [Requirements for Foundry Local on Azure Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/concept-requirements)
- [What you need for Agentic Retrieval in Foundry Local](https://learn.microsoft.com/azure/azure-arc/agents-tools-foundry-local/requirements)
- [What is Microsoft 365 Local?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/m365-local/microsoft-365-local-overview)
