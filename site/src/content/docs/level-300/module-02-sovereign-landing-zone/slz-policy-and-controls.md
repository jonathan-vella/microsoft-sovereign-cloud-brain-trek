---
title: "SLZ policy and controls"
description: "Map Sovereign Landing Zone control levels to Azure Policy initiatives, management group scope, exemptions, and posture reporting."
lastVerified: 2026-10-02
sidebar:
  order: 2
---

SLZ controls are policy-driven. The architecture separates workload placement from enforcement, then uses Azure Policy assignments at management group scope to audit or block resources that do not meet the selected sovereign control level.

Microsoft Learn defines three foundational sovereign controls in Sovereign Public Cloud:

| Control level | What it protects | Common enforcement point |
| --- | --- | --- |
| Level 1 | Data residency | Allowed regions and service location policies |
| Level 2 | Encryption at rest and in transit | Customer-managed keys, Managed HSM where supported, HTTPS, TLS, private connectivity |
| Level 3 | Encryption in use | Confidential computing SKUs, confidential PaaS options, attestation, and Secure Key Release |

These levels are cumulative. A Confidential Corp workload needs Level 1, Level 2, and Level 3 controls. A Corp workload normally needs Level 1 and Level 2. A Public workload can use standard ALZ security policies without sovereign control levels unless the data classification says otherwise.

## Level 1: Data residency

Level 1 policies restrict deployments to approved Azure regions. This is the first control because it sets the boundary for where data-bearing resources are created and where deployment metadata is stored.

Region policy is necessary but not sufficient. Azure has regional services, where the service and data location can be selected, and non-regional services, where the service uses regional deployments with global replication. Microsoft Learn lists Azure Front Door, Traffic Manager, Azure Policy, and Azure DNS as examples of non-regional services in the data residency discussion. Architects must record those exceptions instead of assuming that an allowed location policy covers every data movement.

Use Level 1 at the Landing Zones parent if every workload must stay inside the same geography. Use Level 1 at Online, Corp, Confidential Online, and Confidential Corp when only classified workloads have residency requirements. Keep policy parameters in source control, because allowed regions change by jurisdiction and service availability.

## Level 2: Encryption at rest and in transit

Level 2 adds encryption controls. Azure services use platform-managed encryption at rest by default, but sovereign controls use customer-managed keys when the service supports them. For higher assurance, Microsoft Learn recommends Azure Key Vault Managed HSM for workloads with elevated sovereignty or compliance requirements.

Encryption at rest policy should check both the encryption mode and the key source. Some services support customer-managed keys from Key Vault but not Managed HSM. Some services store temporary data with platform-managed keys even when customer-managed keys protect the main data store. Treat each service's customer-managed key support as a design dependency, not a generic platform promise.

Encryption in transit policy should require HTTPS or current TLS settings for supported services. For network paths outside Microsoft controlled physical boundaries, Azure uses MACsec on Microsoft-controlled backbone links. For customer endpoints, use TLS, VPN, VPN over ExpressRoute, or ExpressRoute MACsec where the workload requires transport encryption that does not depend on application protocol behavior.

## Level 3: Encryption in use

Level 3 uses confidential computing to protect data while it is processed in memory. Azure Confidential Computing uses trusted execution environments and attestation so code and data are protected from unauthorized access outside the workload.

Secure Key Release ties this model to key management. With Secure Key Release, a private key in Azure Key Vault Premium or Managed HSM is released only after the workload proves that it runs in an approved trusted execution environment and satisfies the key's release policy. Use this pattern for workloads where encrypted data must never be decrypted outside an attested environment.

Treat Level 3 enforcement as progressive. Start with audit mode to find unsupported SKUs, services without confidential options, or platform dependencies outside the trusted execution boundary. Move to deny only after the workload design and subscription vending process can supply compliant SKUs by default.

## Built-in policy initiatives

Microsoft documents two overlapping Azure Policy surfaces for sovereignty. They are not interchangeable.

The mature initiatives are in the Regulatory Compliance category:

| Initiative | Category | Policies | Version | How to use it |
| --- | --- | --- | --- | --- |
| Sovereignty Baseline - Global Policies | Regulatory Compliance | 5 | 1.2.0 | Baseline residency policy for workloads that need global sovereign controls. |
| Sovereignty Baseline - Confidential Policies | Regulatory Compliance | 22 | 1.2.0 | Confidential policy baseline for workloads that need region restrictions, customer-managed keys, and Azure Confidential Computing backed resources. |

The newer initiatives are in the separate Sovereignty category and are marked preview in the built-in initiative index:

| Initiative | Policies | Version |
| --- | --- | --- |
| [Preview]: Enforce Data Residency across Azure Services | 6 | 1.0.0-preview |
| [Preview]: Enforce Encryption-at-Rest with Customer Managed Keys (CMK) across Azure Services | 49 | 2.0.0-preview |
| [Preview]: Enforce Encryption-at-Rest with Customer Managed Keys (CMK) with Azure Key Vault Managed HSM Keys across Azure Services | 1 | 1.0.0-preview |
| [Preview]: Enforce Encryption-in-Transit across Azure Services - HTTPS | 19 | 1.1.0-preview |
| [Preview]: Enforce Encryption-in-Transit across Azure Services - TLS Version | 20 | 1.1.0-preview |
| [Preview]: Enforce Encryption-in-Use across Azure Services | 4 | 1.0.0-preview |
| [Preview]: Private Endpoint configured across Azure Services | 40 | 1.0.0-preview |
| [Preview]: Restrict Public Network Access across Azure Services | 44 | 1.0.0-preview |

There is no Azure Policy initiative named "Sovereignty Confidential Computing" in the Microsoft built-in initiative list. Use "Sovereignty Baseline - Confidential Policies" when you mean the Regulatory Compliance baseline, or "[Preview]: Enforce Encryption-in-Use across Azure Services" when you mean the granular preview initiative for confidential computing backed resources.

## Assignment scope

Assign controls where inheritance matches the workload pattern.

| Scope | Assignment pattern |
| --- | --- |
| Landing Zones | Shared controls that apply to every workload landing zone, such as allowed regions for a sovereign boundary. |
| Online and Corp | Level 1 and Level 2 controls for normal business workloads that carry general or confidential data. |
| Confidential Online and Confidential Corp | Level 1, Level 2, and Level 3 controls for highly confidential or secret workloads. |
| Public | Standard ALZ security controls and organization policies. Do not apply unnecessary sovereign controls unless the public workload stores classified data. |
| Platform | Level 1 and Level 2 for platform services that support sovereign workloads. Add Level 3 where the service supports confidential computing. |

Prefer management group assignments over per-subscription assignments. Per-subscription policy should be the exception for a workload-specific control that does not belong in the group baseline.

## Audit, deny, and rollout

Azure Policy effects change what happens during evaluation. `Audit` and `AuditIfNotExists` record non-compliance. `Deny` blocks non-compliant create or update requests. `DeployIfNotExists` can configure supporting resources after a resource is created, and `Modify` can change supported properties during a create or update request.

Start sovereign controls in audit when the estate is brownfield or when service support is uncertain. Use audit results to identify non-regional services, services without customer-managed key support, and workloads that need SKU changes. Move to deny for new deployments only after subscription vending, reference architectures, and workload templates can produce compliant resources.

Do not use Azure Policy as a workload deployment engine. The CAF FAQ states that Azure Policy should control, govern, and keep workloads compliant, while infrastructure as code deploys the workload itself.

## Exemptions

Exemptions are part of the design. They keep a resource in compliance reporting while recording why a policy should not evaluate it or why non-compliance is temporarily accepted. Azure Policy supports two exemption categories:

| Category | Use |
| --- | --- |
| Mitigated | The policy intent is met through another method. |
| Waiver | Non-compliance is temporarily accepted. |

Require an owner, approval reference, expiration date, and remediation plan for every exemption. Expired exemptions are preserved for record keeping, but Azure Policy no longer honors them after the expiration date. Review exemptions during architecture review and operational governance boards.

## Sovereign Control Panel posture

Sovereign Control Panel is the current name for Regulated Environment Management. Microsoft Learn states that SCP uses a Discover, Control, and Act model. Discover provides an evidence-based view across residency, confidentiality, operational sovereignty, and continuity. Control sets and enforces sovereignty rules. Act helps teams prioritize sovereign risk and remediate drift.

SCP is not only a policy compliance screen. Microsoft states that it combines Azure Policy evaluations with direct resource configuration reads, so posture is not limited to resources with policy alias coverage. Use SCP as a posture view and evidence source, but keep policy assignments, parameters, and exemptions in the landing zone operating model.

## Sources

- [Controls and principles in Sovereign Public Cloud](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/overview-controls-principles)
- [Implement controls and principles in SLZ](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/implement-controls-principles)
- [Azure Policy built-in initiative definitions](https://learn.microsoft.com/azure/governance/policy/samples/built-in-initiatives)
- [Azure Policy definitions effect basics](https://learn.microsoft.com/azure/governance/policy/concepts/effects)
- [Azure Policy exemption structure](https://learn.microsoft.com/azure/governance/policy/concepts/exemption-structure)
- [Sovereign Control Panel](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/sovereign-control-panel)
