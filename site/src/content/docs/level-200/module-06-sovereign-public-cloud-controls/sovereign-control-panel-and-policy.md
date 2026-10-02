---
title: "Sovereign Control Panel and policy"
description: "Use Sovereign Control Panel and Azure Policy initiatives to evaluate, enforce, and prove sovereignty posture in Azure."
lastVerified: 2026-10-02
sidebar:
  order: 5
---

Sovereign controls need evidence. Sovereign Control Panel helps teams discover and act on sovereignty posture, while Azure Policy initiatives audit or enforce resource configuration. Use both. Sovereign Control Panel gives posture visibility. Azure Policy gives control at management group, subscription, or resource group scope.

Microsoft Learn states that Regulated Environment Management is now Sovereign Control Panel ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/sovereign-control-panel)). Use the current name in designs and migration notes.

## Sovereign Control Panel

Sovereign Control Panel is a unified Azure portal experience for viewing, managing, and evaluating sovereignty posture across tenant resources. Microsoft describes it as the integration point for sovereignty in the public cloud and organizes it around Discover, Control, and Act ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/sovereign-control-panel)).

| SCP function | What it does | Design use |
|---|---|---|
| Discover | Measures posture with a read-only evidence view across residency, confidentiality, operational sovereignty, and continuity | Establish the starting state and prepare audit evidence |
| Control | Sets and enforces required controls, including customer sovereignty rules | Translate requirements into rules and guardrails |
| Act | Prioritizes sovereign risk and helps remediate resources that drift from the expected state | Triage exceptions and track remediation |

SCP combines Azure Policy evaluations with direct resource configuration reads, so it is not limited to coverage exposed by Azure Policy aliases ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/sovereign-control-panel)). That distinction matters when auditors ask whether the posture view is only a policy assertion. SCP can read configuration signals directly and correlate them with policy results.

Microsoft Learn says typical SCP users include governments and regulated industries that need to align resources with local laws and policy frameworks, including the EU SEAL framework ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/sovereign-control-panel)).

## Azure Policy sovereignty initiatives

Azure Policy has two sovereignty-related surfaces that are easy to confuse.

The first surface is the Regulatory Compliance category. It includes:

| Initiative | Policies | Version | Use |
|---|---:|---:|---|
| Sovereignty Baseline - Global Policies | 5 | 1.2.0 | Denies creation of resources outside approved regions |
| Sovereignty Baseline - Confidential Policies | 22 | 1.2.0 | Denies resources outside approved regions, resources not backed by Azure Confidential Computing, and data storage resources that do not use customer-managed keys |

These initiatives still use the older "Microsoft Cloud for Sovereignty" wording in their descriptions on the built-in initiatives page, but the current portfolio name is Microsoft Sovereign Cloud. Keep the official initiative names unchanged.

The second surface is the newer Sovereignty category. It contains granular preview initiatives ([Learn](https://learn.microsoft.com/azure/governance/policy/samples/built-in-initiatives)):

| Preview initiative | Main control |
|---|---|
| [Preview]: Enforce Data Residency across Azure Services | Level 1 data residency |
| [Preview]: Enforce Encryption-at-Rest with Customer Managed Keys (CMK) across Azure Services | Level 2 encryption at rest with CMK |
| [Preview]: Enforce Encryption-at-Rest with Customer Managed Keys (CMK) with Azure Key Vault Managed HSM Keys across Azure Services | Level 2 encryption at rest with Managed HSM |
| [Preview]: Enforce Encryption-in-Transit across Azure Services - HTTPS | Level 2 HTTPS enforcement |
| [Preview]: Enforce Encryption-in-Transit across Azure Services - TLS Version | Level 2 TLS version enforcement |
| [Preview]: Enforce Encryption-in-Use across Azure Services | Level 3 encryption in use through confidential compute-backed services and SKUs |
| [Preview]: Private Endpoint configured across Azure Services | Private endpoint audit |
| [Preview]: Restrict Public Network Access across Azure Services | Public network exposure reduction |

There is no built-in initiative named "Sovereignty Confidential Computing". Use the exact names above when you write designs or policy assignments.

## How SCP and Azure Policy work together

Azure Policy can deny, audit, deploy, or remediate configuration. SCP turns sovereignty posture into a review workflow. A design should state which tool owns each outcome:

| Outcome | Use Azure Policy | Use SCP |
|---|---|---|
| Prevent non-approved regions | Assign deny policy at management group or subscription scope | Show residency posture and drift |
| Require CMK or Managed HSM where supported | Assign audit or deny policy after service validation | Show key-control posture across resources |
| Require confidential compute SKUs | Assign preview encryption-in-use initiatives where the SKU set fits the workload | Show Level 3 posture and remediation priority |
| Review exceptions | Use exemptions with expiration and justification | Show risk, owner, and remediation state |
| Prepare audit evidence | Export compliance state and assignment metadata | Use SCP posture views and direct configuration evidence |

Use policy progressively. Start in audit mode when the initiative is preview, service coverage is incomplete, or the resource estate has unknown exceptions. Move to deny after you validate false positives, remediation paths, and emergency change handling.

## Link to the landing zone

Sovereign Landing Zone applies policy-as-code and management group structure for sovereign workloads. In this repository, the current page on disk is [Sovereign Landing Zone](/level-300/sovereign-landing-zone/). Use that page for the current internal link until the Level 300 module move lands.

## Implementation checklist

- Define the control target. Use Level 1, Level 2, and Level 3 requirements from the workload classification.
- Choose the right initiative family. Use Regulatory Compliance baseline initiatives for the current baseline names and versions. Use the Sovereignty category preview initiatives for granular controls when preview status is acceptable.
- Assign at the right scope. Management group scope is common for shared sovereignty controls. Subscription or resource group scope may be better for exceptions or phased rollout.
- Decide audit or deny. Deny can block deployments. Use audit first if service behavior or exceptions are not yet understood.
- Add exemptions with expiration. Every exception needs owner, justification, review date, and compensating control.
- Use SCP for evidence. SCP can combine policy state and direct resource configuration reads, which helps with posture review.
- Keep names exact. Do not invent initiatives or rename official built-ins.

## Sources

- [Sovereign Control Panel (SCP)](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/sovereign-control-panel)
- [Azure Policy built-in initiative definitions](https://learn.microsoft.com/azure/governance/policy/samples/built-in-initiatives)
- [Controls and principles in Sovereign Public Cloud](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/overview-controls-principles)
- [Sovereign Landing Zone](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/overview-sovereign-landing-zone)
