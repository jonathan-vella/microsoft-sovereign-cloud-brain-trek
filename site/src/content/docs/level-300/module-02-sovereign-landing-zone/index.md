---
title: "Module 2: Sovereign Landing Zone"
description: "Design a Sovereign Landing Zone as an Azure landing zone variant with control levels, policy scope, and implementation paths."
lastVerified: 2026-10-02
module:
  duration: "60-90 minutes"
  objectives:
    - Explain how Sovereign Landing Zone extends the Azure landing zone architecture.
    - Map data classification to SLZ management groups and control levels.
    - Select Azure Policy initiatives for data residency, encryption, and confidential computing.
    - Compare the Bicep, Terraform, library, and Microsoft.Sovereign implementation paths.
  prerequisites:
    - /level-200/module-05-compliance/
    - Familiarity with Azure landing zones
---

Sovereign Landing Zone is a variant of the Azure landing zone architecture, not a separate product. It keeps the Azure landing zone design principles and design areas, then adds sovereign workload groups and policy controls for residency, encryption, and confidential computing.

Use this module to decide where workloads belong, which controls they inherit, and how to deploy the platform without treating every workload as highly confidential. The module starts with the management group architecture, then maps policies and data classification to implementation choices.

## Sources

- [Sovereign Landing Zone](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/overview-sovereign-landing-zone)
- [Sovereign Landing Zone implementation options](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/implementation-options)
- [Implement controls and principles in SLZ](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/implement-controls-principles)
- [What is an Azure landing zone?](https://learn.microsoft.com/azure/cloud-adoption-framework/ready/landing-zone/)
