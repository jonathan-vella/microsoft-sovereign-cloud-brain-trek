---
title: "Module 5: Compliance and security"
description: "Map sovereignty, compliance, and security requirements to Microsoft controls across Azure, Azure Local, and regulatory tooling."
lastVerified: 2026-10-02
module:
  duration: "90-120 minutes"
  objectives:
    - Map regulatory requirements to Defender for Cloud, Azure Policy, and Microsoft Purview Compliance Manager.
    - Plan Azure Local and Arc-connected workload hardening for sovereign solution designs.
    - Explain GDPR, FedRAMP, NIS2, DORA, and EU AI Act tooling without overstating certification or legal scope.
  prerequisites:
    - /level-100/module-01-digital-sovereignty/
sidebar:
  label: Overview
  order: 5
---

Sovereign solution design turns legal, contractual, and risk requirements into specific controls. In this module, you map common requirements to Microsoft Defender for Cloud, Azure Policy initiatives, Microsoft Purview Compliance Manager, Azure Local security settings, Microsoft Entra, and Microsoft Sovereign Cloud control levels.

The module focuses on what architects can design and verify. Defender for Cloud includes built-in regulatory standards for NIS2, GDPR, FedRAMP "H" and "M", DORA, and the EU AI Act ([Learn](https://learn.microsoft.com/azure/defender-for-cloud/concept-regulatory-compliance-standards)). Compliance Manager provides regulatory templates, including premium templates and premium AI templates, but those assessments do not replace a customer's own legal review or authorization process ([Learn](https://learn.microsoft.com/purview/compliance-manager-regulations)).

Use this module when you need to decide which cloud boundary, control plane, identity model, monitoring path, or compliance evidence path fits a regulated workload. The examples use current Microsoft documentation and avoid unsupported frameworks or undocumented roadmap claims.

## Before you start

Bring three inputs to each compliance design review:

| Input | Why it matters |
| --- | --- |
| Regulatory scope | Identifies whether the workload is subject to GDPR, FedRAMP, NIS2, DORA, the EU AI Act, or another framework. |
| Data and operational boundaries | Determines whether Azure public regions, the EU Data Boundary, Azure Government, Azure Local, or disconnected operations are relevant. |
| Evidence owner | Separates Microsoft's inherited controls from customer controls and shared controls that need implementation evidence. |

Microsoft's compliance tooling helps you inventory, assign, and assess controls. It does not issue customer authorizations, decide lawful basis, or remove the customer's responsibility for system design.

## Sources

- [Regulatory compliance standards in Microsoft Defender for Cloud](https://learn.microsoft.com/azure/defender-for-cloud/concept-regulatory-compliance-standards)
- [Learn about regulations in Compliance Manager](https://learn.microsoft.com/purview/compliance-manager-regulations)
- [Federal Risk and Authorization Management Program](https://learn.microsoft.com/azure/compliance/offerings/offering-fedramp)
- [General Data Protection Regulation](https://learn.microsoft.com/compliance/regulatory/gdpr)
- [What is DORA?](https://learn.microsoft.com/compliance/dora/dora-what-is-dora)
