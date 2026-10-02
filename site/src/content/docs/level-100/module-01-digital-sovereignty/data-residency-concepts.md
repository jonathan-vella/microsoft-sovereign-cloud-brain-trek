---
title: "Data residency concepts"
description: "Compare data residency, data sovereignty, and data localization, then map data states and Azure regions to sovereignty planning."
lastVerified: 2026-10-02
sidebar:
  order: 2
---

## Three terms that sound alike

Residency, sovereignty, and localization often appear in the same customer conversation. They are not the same requirement.

| Term | Plain meaning | Example question |
| --- | --- | --- |
| Data residency | The physical country, region, or geography where data is stored. | Does this database stay in an Azure region inside Germany? |
| Data sovereignty | The legal and governance authority over data, especially where it is stored and processed. | Which laws apply, and which safeguards restrict access to the data? |
| Data localization | A legal or policy requirement to store, process, or keep a copy of data in a specific location. | Does this law require a local copy or local processing for this data type? |

Data residency is usually the easiest term to measure because it maps to a service location or region. Data sovereignty adds access, legal process, encryption, auditability, and operational control. Data localization is a mandate, not an architecture pattern.

## Where data lives

Sovereignty reviews should follow data across the states where cloud services handle it.

| Data state | What to check | Common Azure controls |
| --- | --- | --- |
| At rest | Where primary data, replicas, backups, and logs are stored. | Region selection, storage replication settings, backup vault location, customer-managed keys |
| In transit | Which networks, endpoints, and regions data crosses. | TLS, private endpoints, routing controls, service-specific data transfer documentation |
| In processing | Where compute runs and whether operators or platform layers can see plaintext data. | Region selection, confidential computing, attestation, customer-managed keys, access controls |

Most residency conversations begin with data at rest, but they should not stop there. A design that stores data in the right region can still transfer data through a global feature, replicate backups outside the approved geography, or expose support access in a way the customer cannot approve.

## Data classification and sovereignty

Data classification tells you which sovereignty controls to apply. A public website and a restricted government workload should not receive the same design.

A simple classification exercise should answer these questions:

- Does the data include personal data, regulated business data, health data, payment data, export-controlled data, or classified information?
- Which country, region, sector, or contract controls the data?
- Is cross-border transfer allowed, and under which safeguards?
- Who may access plaintext data?
- Does the workload need to operate during disconnection from public cloud services?

Classification also prevents overdesign. If every workload is treated as the highest classification, teams add cost and operational friction where it is not needed. If classification is too coarse, sensitive data can move into services or regions that do not meet policy.

## Azure geographies and regions

Azure uses regions as deployment locations for many resources. A region is a set of datacenters deployed within a latency-defined perimeter and connected through a dedicated regional low-latency network. Azure geographies are broader market and data-residency areas that can contain one or more regions.

When you deploy a regional Azure service, the selected region is the main data residency decision. Service-specific features can change that decision. Examples include geo-redundant replication, cross-region disaster recovery, global routing, or non-regional services that need separate configuration.

Microsoft Learn currently distinguishes between exact and rounded region counts. The Azure regions list enumerates [57 public Azure regions](https://learn.microsoft.com/azure/reliability/regions-list), while the compliance offerings overview uses a rounded ["more than 60 regions worldwide"](https://learn.microsoft.com/azure/compliance/offerings/) statement. Learn doesn't reconcile the two figures, so quote the exact count only with its source and date.

## The EU Data Boundary

The EU Data Boundary is a specific Microsoft commitment for Azure, Dynamics 365, Power Platform, and Microsoft 365. It is not a generic definition of data residency. It has product-specific scope rules, country coverage, and log handling rules.

For the current EU Data Boundary scope, covered countries, covered services, and product-specific configuration rules, read the [European commitments and EU Data Boundary](/level-100/module-01-digital-sovereignty/european-commitments/#eu-data-boundary) page.

## Sources

- [Data controls](https://learn.microsoft.com/azure/azure-sovereign-clouds/data-controls)
- [What is the EU Data Boundary?](https://learn.microsoft.com/privacy/eudb/eu-data-boundary-learn)
- [Azure regions list](https://learn.microsoft.com/azure/reliability/regions-list)
- [Azure, Dynamics 365, Microsoft 365, and Power Platform compliance offerings](https://learn.microsoft.com/azure/compliance/offerings/)
- [Azure geographies](https://azure.microsoft.com/explore/global-infrastructure/geographies/)
