---
title: "Confidential computing"
description: "Plan Azure confidential VMs, confidential containers, attestation, and Secure Key Release for encryption-in-use requirements."
lastVerified: 2026-10-02
sidebar:
  order: 4
---

Confidential computing addresses Level 3 Sovereign Public Cloud requirements by protecting data while it is processed. It uses hardware-based trusted execution environments, attestation, and policy-based key release to reduce exposure to cloud operators, host administrators, and infrastructure-level compromise.

Use confidential computing when the requirement includes data in use. If the requirement only says data must stay in a geography or be encrypted at rest, Level 1 or Level 2 controls may be enough.

## Azure confidential computing options

Microsoft Learn lists current Azure confidential computing offerings across virtual machines, containers, confidential services, and supplementary services ([Learn](https://learn.microsoft.com/azure/confidential-computing/overview-azure-products)). The main design choices are the compute boundary and the attestation pattern.

| Workload pattern | Azure option | Current status to cite in design |
|---|---|---|
| Rehost existing VM workloads on AMD SEV-SNP | DCasv5, DCadsv5, ECasv5, and ECadsv5 confidential VMs | Generally available series listed by Microsoft Learn ([Learn](https://learn.microsoft.com/azure/confidential-computing/overview-azure-products)) |
| Rehost VM workloads on Intel TDX | DCesv6, DCedsv6, ECesv6, and ECedsv6 confidential VMs | Generally available series listed by Microsoft Learn ([Learn](https://learn.microsoft.com/azure/confidential-computing/overview-azure-products)) |
| Use fourth-generation AMD EPYC confidential VMs | DCasv6 and ECasv6 | Gated preview ([Learn](https://learn.microsoft.com/azure/confidential-computing/overview-azure-products)) |
| Protect AI and machine learning workloads with linked CPU and GPU TEEs | NCCads H100 v5 confidential GPU VM | An Azure VM series that combines AMD SEV-SNP with NVIDIA H100 GPU TEEs. Check regional availability before you design around it ([Learn](https://learn.microsoft.com/azure/virtual-machines/sizes/gpu-accelerated/nccadsh100v5-series)) |
| Rehost containers in Kubernetes | Confidential AKS worker nodes | Supported on AKS with generally available DCasv5 and ECasv5 confidential VM series ([Learn](https://learn.microsoft.com/azure/confidential-computing/confidential-node-pool-aks)) |
| Run container groups with container-level integrity | Confidential containers on Azure Container Instances | Supported with CCE policies and remote guest attestation ([Learn](https://learn.microsoft.com/azure/container-instances/container-instances-confidential-overview)) |

## VM-level confidentiality

Confidential VMs protect the VM boundary. AMD SEV-SNP and Intel TDX are designed to protect VM memory and state from the hypervisor and other host management code. This pattern works well for lift-and-shift applications because the operating system and application can often move with fewer code changes than enclave-based designs.

Use VM-level confidentiality when:

- The application is hard to split into enclave-aware components.
- The main risk is host or operator access to VM memory.
- You need disk encryption and key release tied to VM boot and attestation.
- The workload can run on supported confidential VM SKUs.

Check SKU availability in the chosen Azure region before committing. Confidential compute requirements can conflict with region restrictions, quota, GPU availability, or existing VM size standards.

## Container-level confidentiality

Confidential AKS worker nodes use confidential VMs as Kubernetes nodes. They are useful when you want Kubernetes scheduling and platform operations but need the node memory protected by AMD SEV-SNP hardware. Microsoft Learn describes AKS support for confidential VM node pools with generally available DCasv5 and ECasv5 confidential VM series ([Learn](https://learn.microsoft.com/azure/confidential-computing/confidential-node-pool-aks)).

Confidential containers on Azure Container Instances provide a container group with a hardware-based and attested trusted execution environment. They support confidential computing enforcement policies, also called CCE policies, which define the components allowed to run in the container group ([Learn](https://learn.microsoft.com/azure/container-instances/container-instances-confidential-overview)).

Use ACI confidential containers when:

- The workload is a Linux container group.
- You need policy evidence for the exact container components that can run.
- You want remote guest attestation before releasing secrets.
- You can generate CCE policies through the Azure CLI confcom extension.

## Attestation

Attestation proves that software was instantiated on a trusted platform. Microsoft Azure Attestation receives evidence from compute entities, validates it against policies, and produces cryptographic proofs for relying parties ([Learn](https://learn.microsoft.com/azure/attestation/overview)).

For confidential VMs, Azure Attestation supports AMD SEV-SNP platform and guest attestation. For confidential containers, the container group can produce an SNP hardware attestation report and exchange it with Azure Attestation. Your application or sidecar can use the attestation token before it retrieves a secret or key.

Plan attestation as an application dependency, not only a platform feature. Decide:

- Which claims prove the workload is the expected workload.
- Which attestation authority is trusted.
- How the relying party validates token signatures and claim values.
- What happens if attestation fails.
- How claim changes are tested during platform updates.

## Secure Key Release

Secure Key Release ties key release to attestation. Azure Key Vault Premium and Managed HSM can release an HSM-protected key only when the workload presents an Azure Attestation token that satisfies the key release policy ([Learn](https://learn.microsoft.com/azure/confidential-computing/concept-skr-attestation)).

This pattern is useful for Level 3 workloads because it joins encryption in use with key control. The data remains encrypted until the workload proves that it is running in the expected trusted environment. Then the key is released into that environment.

Do not confuse SKR with Managed HSM External Key Management. SKR is an attestation-gated key release pattern. EKM is a preview key custody pattern that delegates wrap and unwrap operations to an external HSM. The EKM preview does not support SKR.

## Level 3 design checklist

- Classify the data. Use Level 3 only where data in use is part of the risk statement.
- Choose the boundary. VM-level, node-level, and container-level confidentiality solve different problems.
- Validate region and SKU availability. Sovereign controls often constrain geography before compute choice.
- Define attestation claims. An attestation token is only useful if the policy checks claims that matter.
- Pair confidential computing with key management. Use SKR when key release must depend on attestation.
- Keep operations realistic. Backup, monitoring, patching, debugging, and incident response all need procedures that respect the TEE boundary.

## Sources

- [What is confidential computing?](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/confidential-computing)
- [Azure confidential computing offerings](https://learn.microsoft.com/azure/confidential-computing/overview-azure-products)
- [NCCads H100 v5 sizes series](https://learn.microsoft.com/azure/virtual-machines/sizes/gpu-accelerated/nccadsh100v5-series)
- [Confidential VM node pool support on AKS with AMD SEV-SNP confidential VMs](https://learn.microsoft.com/azure/confidential-computing/confidential-node-pool-aks)
- [Confidential containers on Azure Container Instances](https://learn.microsoft.com/azure/container-instances/container-instances-confidential-overview)
- [Microsoft Azure Attestation](https://learn.microsoft.com/azure/attestation/overview)
- [Secure Key Release feature with AKV and Azure Confidential Computing](https://learn.microsoft.com/azure/confidential-computing/concept-skr-attestation)
