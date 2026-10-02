---
title: "Data classification for SLZ"
description: "Use Microsoft Purview classification and sensitivity labels to place workloads in the right Sovereign Landing Zone management group."
lastVerified: 2026-10-02
sidebar:
  order: 4
---

Data classification is the decision that turns a Sovereign Landing Zone from a diagram into an operating model. The platform team can create Public, Online, Corp, Confidential Online, and Confidential Corp management groups, but those groups only work when workload owners can explain what data they process and which sovereign controls that data requires.

Use classification to answer four questions before subscription vending:

1. What data does the workload store, process, transmit, or log?
2. Which geography or jurisdiction must the data remain in?
3. Which encryption model is required at rest, in transit, and in use?
4. Does the workload need internet exposure, corporate-only connectivity, or full isolation?

## Classification and control levels

Microsoft's Sovereign Public Cloud control model maps data sensitivity to three control levels. Public data can use standard security controls. Internal data normally needs Level 1 data residency. Confidential data needs Level 1 and Level 2 controls. Secret data needs Level 1, Level 2, and Level 3 controls.

| Classification | Control level | SLZ management group | Required controls |
| --- | --- | --- | --- |
| Public | ALZ defaults and organization controls | Public | Standard security baseline. No private network path into sovereign workload groups. |
| Internal | Level 1 when residency applies | Online or Corp | Allowed regions, service availability checks, logging, and standard ALZ policies. |
| Confidential | Level 1 and Level 2 | Online or Corp | Allowed regions, customer-managed keys where supported, encryption in transit, private endpoints where required, and restricted public network access. |
| Highly confidential | Level 1, Level 2, and Level 3 | Confidential Online or Confidential Corp | Confidential computing where supported, customer-managed keys, Managed HSM when supported, Secure Key Release patterns, and attestation review. |
| Secret | Level 1, Level 2, and Level 3 | Confidential Online or Confidential Corp | Same as highly confidential, with stricter exception handling, narrower access, and explicit approval for each platform dependency. |

The network placement still matters. A customer portal with highly confidential data belongs in Confidential Online because it needs internet access. An internal finance analytics platform with the same data sensitivity belongs in Confidential Corp because it is not directly internet-facing.

## Public, Corp, Online, and Confidential placement

The Public group is for information that can be disclosed publicly. Keep it isolated from Corp, Online, Confidential Corp, and Confidential Online. If a public app calls a controlled system, use an authenticated API path and monitor the transaction. Do not add private Layer 3 connectivity from Public workloads into sovereign workload networks.

Use Online when users need authenticated internet access to the workload. Use Corp when the workload is internal only and connects through corporate networks or controlled hub connectivity. Both groups normally inherit Level 1 and Level 2 controls for confidential data.

Use Confidential Online and Confidential Corp when the data classification requires encryption in use. The key design question is not only whether the workload can run on confidential compute. You must also check whether dependent databases, storage, analytics services, key stores, and integration services can meet the same control level or have an approved exception.

## Microsoft Purview for discovery

Microsoft Purview Data Map scans registered data sources, captures technical metadata, and can automatically classify file and column assets. During scanning, Purview compares sampled data to system classifications or custom classification rules. A scan can add classifications such as national identification numbers to assets when the data matches the rule.

Use Purview scanning to reduce guesswork in brownfield environments. Register the data sources, scan them, review the classification reports, and compare the findings with the workload owner's declared classification. Resolve differences before you place the subscription in a management group.

Purview classifications identify what data exists in an asset. Microsoft Learn describes classifications as regular expressions or patterns that help identify data types inside an asset. They are useful for discovery and review, but they do not replace the business decision about impact, legal handling, or the SLZ control level.

## Microsoft Purview sensitivity labels

Sensitivity labels describe business impact and can enforce protection settings. Microsoft Learn states that sensitivity labels identify the sensitivity of data and can enforce protection settings appropriate to that sensitivity. Labels can also be extended to Microsoft Purview Data Map.

[Sensitivity labels in Microsoft Purview Data Map are currently in preview](https://learn.microsoft.com/purview/data-map-sensitivity-labels). In Data Map, labels can be applied to files in storage such as Azure Data Lake or Azure Files and to table columns in Azure SQL Database. Purview can apply labels automatically when an auto-labeling policy maps detected classifications or sensitive information types to a label.

Use one label taxonomy across Microsoft 365, Purview, and Azure data assets where possible. Duplicate label sets create conflicting operational rules. For SLZ, the labels should map to placement decisions and policy controls:

| Sensitivity label example | SLZ decision |
| --- | --- |
| Public | Place in Public if no private dependency requires Corp or Online. |
| General | Place in Online or Corp based on network exposure. Add Level 1 only if residency applies. |
| Confidential | Place in Online or Corp. Apply Level 1 and Level 2 controls. |
| Highly confidential | Place in Confidential Online or Confidential Corp. Apply Level 1, Level 2, and Level 3 controls where supported. |
| Secret | Place in Confidential Online or Confidential Corp with stricter access, attestation, and exemption review. |

## Decision workflow

Use this workflow before subscription vending or migration:

1. Define the classification taxonomy with compliance, legal, security, and workload owners.
2. Map each classification to SLZ control levels and management groups.
3. Register and scan known data sources in Purview Data Map.
4. Review Purview classifications and sensitivity labels with the workload owner.
5. Choose the target management group based on data classification and network exposure.
6. Confirm service support for customer-managed keys, Managed HSM, private endpoints, and confidential computing.
7. Assign policy in audit mode for brownfield workloads, then remediate or document exemptions.
8. Move new workloads to deny mode once templates and service choices are known to be compliant.

## Common failure modes

The first failure mode is treating all regulated data as Level 3. That design burns cost and implementation effort while still missing non-regional services and platform dependencies. Match the control level to the classification.

The second failure mode is classifying only the primary database. Logs, backups, caches, search indexes, AI prompts, telemetry, and exported reports can carry the same sensitivity as the source system. Include them in the data map and in the landing zone review.

The third failure mode is placing a subscription by team ownership instead of data handling. A single team might own public websites, internal analytics, and highly confidential records. Those workloads can require different management groups even when the same team owns them.

The fourth failure mode is using policy exemptions as a permanent operating model. Exemptions are valid when the policy intent is met another way or when temporary non-compliance is accepted, but they need an owner, reason, expiration, and remediation plan.

## Sources

- [Controls and principles in Sovereign Public Cloud](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/overview-controls-principles)
- [Implement controls and principles in SLZ](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/implement-controls-principles)
- [Automatically apply classifications on assets in Data Map](https://learn.microsoft.com/purview/data-map-classification-apply-auto)
- [Learn about sensitivity labels](https://learn.microsoft.com/purview/sensitivity-labels)
- [Learn about sensitivity labels in Data Map](https://learn.microsoft.com/purview/data-map-sensitivity-labels)
- [Sensitivity labels in Data Map FAQ](https://learn.microsoft.com/purview/data-map-sensitivity-labels-faq)
