---
title: "Regulatory overview"
description: "Review GDPR, NIS2, DORA, and EU AI Act Microsoft tooling for foundational sovereignty and compliance conversations."
lastVerified: 2026-10-02
sidebar:
  order: 5
---

## What this page covers

This page introduces the EU regulations that come up most in sovereignty conversations and the Microsoft tooling mapped to each. It does not cover every global framework.

For prerequisite terms such as security controls, compliance frameworks, and shared responsibility, start with [Level 50 security and compliance basics](/level-50/module-02-security-compliance/security-compliance-basics/).

## GDPR

The General Data Protection Regulation is the baseline privacy law most European sovereignty conversations start from. Microsoft Learn describes Microsoft as a data processor and the customer as the controller for GDPR purposes. It also states that GDPR requires controllers to use processors that provide sufficient guarantees for technical and organizational measures.

For cloud architecture, the main Level 100 lesson is role clarity. Microsoft provides contractual, technical, and compliance resources. The customer remains responsible for knowing what personal data it processes, why it processes it, where it places it, and how it handles data subject requests.

Microsoft Learn lists six GDPR data subject request activities: Discovery, Access, Rectification, Restriction, Export, and Deletion. Microsoft Purview Compliance Manager also has a prebuilt GDPR assessment template for eligible Enterprise E5 customers.

## NIS2

The NIS2 Directive is now visible in Microsoft tooling rather than only in narrative guidance. Microsoft Learn lists **EU 2022 2555 (NIS2) 2022** as an available built-in regulatory compliance standard in Microsoft Defender for Cloud for Azure, AWS, and GCP. The same page explains that Defender for Cloud continually assesses in-scope environments against controls that can be automatically assessed.

Microsoft Purview Compliance Manager also lists **NIS2 Directive (EU) 2022/2555 of the European Parliament and of the Council** in its regulations list. In a discovery conversation, that means teams can map NIS2 to both cloud posture assessment and compliance assessment work.

## DORA

The Digital Operational Resilience Act applies to EU financial entities and relevant ICT third-party providers. Microsoft Learn states that organizations had to be ready to comply [starting January 17, 2025](https://learn.microsoft.com/compliance/dora/dora-what-is-dora).

On [November 18, 2025](https://learn.microsoft.com/compliance/dora/dora-what-is-dora), the European Supervisory Authorities (EBA, EIOPA, and ESMA) published the list of designated critical ICT third-party providers under DORA. Microsoft Ireland Operations Limited is on that list as a Critical ICT Third-Party Provider and is subject to direct ESA oversight.

Microsoft Learn points DORA risk management work toward Microsoft tooling such as Defender for Cloud, Microsoft 365 Service Health Dashboard, Secure Score, Azure Service Health, Purview, and Compliance Manager. Defender for Cloud also lists **Digital Operational Resilience Act (DORA)** as an available regulatory compliance standard for Azure, AWS, and GCP.

## EU AI Act tooling

This page covers the EU AI Act only through Microsoft tooling. Microsoft Learn lists **European Union Artificial Intelligence Act (EU AI Act)** as an available built-in regulatory compliance standard in Defender for Cloud for Azure, AWS, and GCP.

Microsoft Purview Compliance Manager lists **EU Artificial Intelligence Act** under Premium AI templates. Its assessment documentation also says Compliance Manager integrates with Azure AI Foundry to sync AI model and agent evaluation results into Compliance Manager for assessments such as the EU AI Act, NIST AI RMF, and ISO/IEC standards.

Microsoft Learn doesn't publish the Act's phased application dates. Check the regulation itself for its timeline.

## Sources

- [General Data Protection Regulation](https://learn.microsoft.com/compliance/regulatory/gdpr)
- [Compliance Manager regulations list](https://learn.microsoft.com/purview/compliance-manager-regulations-list)
- [Regulatory compliance standards in Microsoft Defender for Cloud](https://learn.microsoft.com/azure/defender-for-cloud/concept-regulatory-compliance-standards)
- [What is DORA?](https://learn.microsoft.com/compliance/dora/dora-what-is-dora)
- [Build and manage assessments in Compliance Manager](https://learn.microsoft.com/purview/compliance-manager-assessments)
