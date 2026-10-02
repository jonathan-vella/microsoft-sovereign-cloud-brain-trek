---
title: "Digital sovereignty defined"
description: "Define digital sovereignty across data, operational, and technological dimensions, and learn why regulated organizations care about control."
lastVerified: 2026-10-02
sidebar:
  order: 1
---

## What digital sovereignty means

**Digital sovereignty** is the ability to make and prove decisions about digital systems under the laws, policies, and risk tolerance that apply to the organization. It is broader than "keep data in a country." It covers where data is stored and processed, who can operate the environment, which legal authorities apply, and whether the organization can keep running when external conditions change.

Microsoft Learn frames digital sovereignty through three related dimensions:

| Dimension | What it asks | Common controls |
| --- | --- | --- |
| Data controls | Where is data stored, processed, protected, and governed? | Region selection, customer-managed keys, encryption in transit, encryption at rest, confidential computing, data transfer controls |
| Operational controls | Who can access production systems, when, and under what oversight? | Customer Lockbox, Data Guardian, Azure Policy, monitoring, incident response evidence |
| Technological independence | Can the organization choose, manage, and secure infrastructure without undue reliance on foreign technology or proprietary constraints? | Azure Local, disconnected operations, Sovereign Private Cloud, National Partner Clouds, Azure Arc for hybrid management |

These dimensions overlap. A workload can meet a residency requirement and still fail an operational requirement if support access is not governed. A disconnected private cloud can meet an independence requirement and still need data classification, key management, and audit evidence.

## Why organizations care

Organizations care about digital sovereignty when law, public policy, mission needs, or customer expectations limit where systems can run and who can operate them.

For public sector and regulated industries, sovereignty questions often appear during architecture reviews:

- Which country or region stores the data at rest?
- Can data move across a border during backup, monitoring, support, or disaster recovery?
- Which personnel can access production systems?
- Can the organization approve or reject provider access to customer data?
- Can the workload run through a network outage, geopolitical event, or policy change?
- Which controls prove the design is still compliant after deployment?

These questions make sovereignty an operating model, not a single product setting. Architects need to classify data, choose a cloud model, define key custody, restrict access, monitor drift, and keep evidence for auditors.

## How the dimensions differ

### Data controls

Data controls focus on the data lifecycle. Microsoft Learn defines data sovereignty as legal and regulatory authority over data, especially where data is stored and processed. Data controls include data ownership, data protection and privacy, cross-border data transfer rules, and legal jurisdiction.

Encryption is one of the main technical controls. Azure services use encryption in transit, services use server-side encryption for data at rest, and confidential computing extends protection to data while it is being processed. The [data residency concepts](/level-100/module-01-digital-sovereignty/data-residency-concepts/) page explains how residency, sovereignty, and localization differ.

### Operational controls

Operational controls focus on provider and operator activity. Microsoft Learn describes them as controls that maintain transparency, accountability, and autonomy over cloud operations and infrastructure.

For Microsoft cloud services, examples include Customer Lockbox for customer approval of eligible Microsoft access requests and Data Guardian for supervised Microsoft personnel access in defined regions. The [operational sovereignty](/level-100/module-01-digital-sovereignty/operational-sovereignty/) page introduces those controls at a conceptual level.

### Technological independence

Technological independence focuses on choice and continuity. Microsoft Learn names it as a dimension of digital sovereignty alongside data controls and operational controls. It is the ability to choose, manage, and secure infrastructure without undue reliance on foreign technologies or proprietary constraints.

In the Microsoft portfolio, this dimension often points to private and hybrid models. Azure Local supports customer-controlled infrastructure and disconnected operations. National Partner Clouds support local operating models where Microsoft works with approved national or regional partners. Later modules cover those models in more detail.

## Microsoft's answer

Microsoft's current portfolio name is [Microsoft Sovereign Cloud](https://learn.microsoft.com/azure/azure-sovereign-clouds/microsoft-sovereign-cloud), formerly Microsoft Cloud for Sovereignty. It brings together public, private, and partner-operated deployment models for governments and regulated industries.

Module 2 defines the portfolio's three deployment models: [Sovereign Public Cloud, Sovereign Private Cloud, and National Partner Clouds](/level-100/module-02-cloud-models/sovereign-cloud-models/).

## Sources

- [What is Microsoft Sovereign Cloud?](https://learn.microsoft.com/azure/azure-sovereign-clouds/microsoft-sovereign-cloud)
- [Technological independence](https://learn.microsoft.com/azure/azure-sovereign-clouds/technological-independence)
- [Data controls](https://learn.microsoft.com/azure/azure-sovereign-clouds/data-controls)
- [Operational controls](https://learn.microsoft.com/azure/azure-sovereign-clouds/operational-controls)
- [What is confidential computing?](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/confidential-computing)
