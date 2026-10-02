---
title: "EU regulations tooling"
description: "Plan Microsoft tooling for NIS2, DORA, and EU AI Act readiness without overstating legal scope or undocumented dates."
lastVerified: 2026-10-02
sidebar:
  order: 5
---

EU regulatory readiness depends on customer obligations, Microsoft contractual commitments, and technical evidence. This page focuses on Microsoft-documented tooling for NIS2, DORA, and the EU AI Act.

## NIS2 tooling

NIS2 is operationalized in Microsoft security tooling through Defender for Cloud, Azure Policy, and Compliance Manager. Defender for Cloud lists **EU 2022 2555 (NIS2) 2022** as an available compliance standard for Azure, AWS, and GCP ([Learn](https://learn.microsoft.com/azure/defender-for-cloud/concept-regulatory-compliance-standards)).

Azure Policy includes two NIS2-related regulatory compliance initiatives in the built-in initiative index:

| Azure Policy initiative | Microsoft description |
| --- | --- |
| EU 2022/2555 (NIS2) 2022 | Enhances cybersecurity across the EU with security measures and incident reporting for critical sectors. |
| NIS2 | Enhances the cybersecurity and resilience of critical infrastructure and digital services across the EU. |

The same Azure Policy index lists the current initiative policy counts and versions, so re-check it before including counts in a customer deliverable ([Learn](https://learn.microsoft.com/azure/governance/policy/samples/built-in-initiatives)).

Compliance Manager includes a premium NIS2 Directive regulation template in its regulations list. Confirm licensing before planning an assessment around that template ([Learn](https://learn.microsoft.com/purview/compliance-manager-regulations-list)).

Use this pattern:

1. Assign the NIS2 standard in Defender for Cloud for the relevant Azure, AWS, and GCP scopes.
2. Assign Azure Policy initiatives for Azure subscriptions where technical guardrails are needed.
3. Use Compliance Manager for action ownership, manual controls, incident process evidence, and management review.
4. Keep regulator-specific reporting procedures outside the tools and attach evidence to the assessment.

## DORA tooling

Microsoft Learn says DORA applies starting January 17, 2025, to EU financial entities and designated critical ICT third-party providers. It standardizes how financial entities report cybersecurity incidents, test digital operational resilience, and manage ICT third-party risk ([Learn](https://learn.microsoft.com/compliance/dora/dora-what-is-dora)).

The DORA page also states that on November 18, 2025, the European Supervisory Authorities published the list of designated Critical ICT Third-Party Providers, and Microsoft Ireland Operations Limited is identified as a Critical Third-Party Provider subject to ESA oversight under the oversight mechanism ([Learn](https://learn.microsoft.com/compliance/dora/dora-what-is-dora)).

Microsoft tooling for DORA includes:

| Tool | Use |
| --- | --- |
| Defender for Cloud | The DORA standard is available for Azure, AWS, and GCP in the Regulatory compliance dashboard ([Learn](https://learn.microsoft.com/azure/defender-for-cloud/concept-regulatory-compliance-standards)). |
| Azure Policy | The DORA 2022 2554 built-in initiative maps regulatory controls to Azure Policy definitions ([Learn](https://learn.microsoft.com/azure/governance/policy/samples/built-in-initiatives)). |
| Microsoft Purview Compliance Manager | Compliance Manager supports third-party risk assessments and vendor compliance management against many standards and regulations. Microsoft's DORA guidance points to Compliance Manager as one of the tools for broader third-party risk work ([Learn](https://learn.microsoft.com/compliance/dora/dora-what-is-dora)). |
| Microsoft Defender for Cloud Apps | Microsoft's DORA guidance identifies Defender for Cloud Apps as a tool for visibility, control, and assessment of third-party apps and services ([Learn](https://learn.microsoft.com/compliance/dora/dora-what-is-dora)). |

For a DORA architecture review, separate three workstreams:

- **Operational resilience.** Availability, incident response, backup, recovery, and testing evidence.
- **ICT third-party risk.** Vendor inventory, contract mapping, and risk assessment evidence.
- **Technical posture.** Defender for Cloud, Azure Policy, logging, identity controls, and vulnerability management.

## EU AI Act tooling

Microsoft Learn documents EU AI Act tooling in Compliance Manager and Defender for Cloud. This page does not state EU AI Act implementation dates because the module is constrained to Microsoft-documented facts.

Compliance Manager provides four premium AI regulatory templates, including the EU Artificial Intelligence Act. These templates apply to generative AI apps supported by Microsoft Purview for AI interactions. The templates are listed under **Premium AI templates** and count toward premium licensing ([Learn](https://learn.microsoft.com/purview/compliance-manager-assessments)).

Compliance Manager also integrates with Azure AI Foundry. Microsoft Learn says the integration syncs evaluation results from Azure AI Foundry directly into Compliance Manager, including 15 automated evaluation actions with pass or fail status and detailed metrics ([Learn](https://learn.microsoft.com/purview/compliance-manager-assessments)).

Defender for Cloud includes the European Union Artificial Intelligence Act standard for Azure, AWS, and GCP in the Regulatory compliance standards list ([Learn](https://learn.microsoft.com/azure/defender-for-cloud/concept-regulatory-compliance-standards)).

Use this tooling pattern for AI workloads:

| Need | Tool |
| --- | --- |
| Cloud resource posture | Defender for Cloud EU AI Act standard. |
| AI governance assessment | Compliance Manager premium AI template for the EU Artificial Intelligence Act. |
| Model or agent evaluation evidence | Azure AI Foundry evaluation results synced to Compliance Manager where supported. |
| Sensitive data use in AI interactions | Microsoft Purview data security posture management for AI and related Compliance Manager recommendations. |

Do not describe the tooling as an EU AI Act certification. It helps assess controls, collect evidence, and track improvement actions.

## Implementation checklist

Use one evidence plan across the three regulation areas:

| Step | Evidence |
| --- | --- |
| Assign standards | Defender for Cloud standard assignments for NIS2, DORA, or the EU AI Act. |
| Apply guardrails | Azure Policy initiative assignments, exemptions, and remediation records. |
| Track manual work | Compliance Manager assessment actions, owners, status, and uploaded evidence. |
| Validate reporting paths | Incident, third-party risk, and AI governance procedures approved by the accountable business owner. |
| Re-verify facts | Source review date, Microsoft Learn URLs, and changed standard or template names. |

## What to leave out

Do not add EU AI Act implementation dates unless a future Microsoft Learn or official Microsoft source documents them and the page is re-verified.

## Sources

- [Regulatory compliance standards in Microsoft Defender for Cloud](https://learn.microsoft.com/azure/defender-for-cloud/concept-regulatory-compliance-standards)
- [Azure Policy built-in initiative definitions](https://learn.microsoft.com/azure/governance/policy/samples/built-in-initiatives)
- [Compliance Manager regulations list](https://learn.microsoft.com/purview/compliance-manager-regulations-list)
- [What is DORA?](https://learn.microsoft.com/compliance/dora/dora-what-is-dora)
- [Build and manage assessments in Compliance Manager](https://learn.microsoft.com/purview/compliance-manager-assessments)
