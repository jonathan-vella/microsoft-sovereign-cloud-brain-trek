---
title: Sovereign Public Cloud
description: "Learn how Sovereign Public Cloud uses Azure public regions, policy, key control, access oversight, and posture tools for regulated workloads."
lastVerified: 2026-10-02
sidebar:
  order: 2
---

Sovereign Public Cloud is the Microsoft Sovereign Cloud model for workloads that can use Azure public regions while adding sovereignty controls. It runs in Microsoft-operated datacenters within defined geopolitical boundaries, such as the EU Data Boundary.

The model does not create a separate cloud for each customer. Instead, it uses Azure public-cloud services with controls for data location, key ownership, operator access, confidential computing, policy enforcement, and posture management. For EU workloads, read the [European commitments page](/level-100/module-01-digital-sovereignty/european-commitments/) before treating the EU Data Boundary as a blanket rule. Scope differs by product and configuration.

## Main capabilities

Microsoft Learn lists four named Sovereign Public Cloud capabilities.

**Data Guardian.** Data Guardian applies to Microsoft personnel remote access for EU and European Free Trade Association customers. Access is monitored by authorized European-resident staff and logged in a tamper-evident ledger built on Azure Confidential Ledger.

**External Key Management.** The name covers two related key-control patterns. [Managed HSM key sovereignty is generally available](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/external-key-management) and gives customers a single-tenant FIPS 140-3 Level 3 HSM with customer-controlled security domains. Managed HSM External Key Management is a separate [preview capability](https://learn.microsoft.com/azure/key-vault/managed-hsm/external-key-management-overview) where the key-encryption key stays outside Microsoft through a customer-run EKM Proxy.

**Azure confidential computing.** Confidential computing protects data in use by running workloads in hardware-based trusted execution environments. Current Azure offerings include generally available confidential VM families, confidential AKS worker nodes, and confidential containers on Azure Container Instances.

**Sovereign Control Panel.** Sovereign Control Panel is the current name for Regulated Environment Management. [Microsoft Learn states that REM is now SCP](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/sovereign-control-panel). SCP uses a Discover, Control, Act operating model and combines Azure Policy evaluation with direct resource configuration reads.

## Customer Lockbox

Customer Lockbox gives the customer an approval workflow before Microsoft engineers can access customer content during support. It covers many Azure services, including services such as App Service, Azure Kubernetes Service, Storage, SQL, Azure OpenAI, Functions, and Logic Apps. [Coverage is broad, but it is not universal](https://learn.microsoft.com/azure/security/fundamentals/customer-lockbox-overview). Microsoft Learn lists [preview status for Azure Data Box Lockbox](https://learn.microsoft.com/azure/databox/data-box-customer-lockbox) and carve-outs for [Power Platform and Dynamics 365 Lockbox](https://learn.microsoft.com/power-platform/admin/about-lockbox).

Use Customer Lockbox when the requirement is approval and auditability for support access. It is not a data residency control, an encryption control, or a substitute for least-privilege administration.

## Azure Policy sovereignty initiatives

Azure Policy provides the enforcement layer for many public-cloud sovereignty requirements. Current Microsoft Learn pages show two sovereignty surfaces.

The mature Regulatory Compliance category includes these initiatives:

- "Sovereignty Baseline - Global Policies"
- "Sovereignty Baseline - Confidential Policies"

The newer "Sovereignty" category contains preview initiatives for granular controls such as data residency, encryption at rest with customer-managed keys, encryption in transit, encryption in use, private endpoints, and restricted public network access.

The confidential-computing controls are in "Sovereignty Baseline - Confidential Policies" and the preview encryption-in-use initiative. Azure Policy has no initiative named "Sovereignty Confidential Computing".

## Sovereign Landing Zone

Sovereign Landing Zone is a variant of Azure Landing Zone, not a separate product. It keeps the standard landing-zone design areas and adds sovereignty-focused policy and management-group patterns, especially for compliance controls.

At Level 100, treat Sovereign Landing Zone as the starting environment for governed Azure subscriptions. It helps place workloads into management groups that match control levels for data residency, encryption, and confidential computing.

## When this model fits

Use Sovereign Public Cloud when the workload needs Azure public-cloud scale or service breadth, and the sovereignty requirement can be met with region choice, policy, encryption, key control, confidential computing, access oversight, and posture management.

Do not choose this model if a requirement says the customer must operate the infrastructure, or if the workload must keep running when the Azure control plane is unavailable for long periods. Those requirements point to [Sovereign Private Cloud](/level-100/module-02-cloud-models/sovereign-private-cloud/).

## Sources

- [What is Sovereign Public Cloud?](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/overview-sovereign-public-cloud)
- [Capabilities of Sovereign Public Cloud](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/sovereign-public-cloud-capabilities)
- [What is Data Guardian?](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/data-guardian)
- [What is External Key Management?](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/external-key-management)
- [What is Managed HSM external key management?](https://learn.microsoft.com/azure/key-vault/managed-hsm/external-key-management-overview)
- [Azure confidential computing offerings](https://learn.microsoft.com/azure/confidential-computing/overview-azure-products)
- [Sovereign Control Panel](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/sovereign-control-panel)
- [Customer Lockbox for Microsoft Azure](https://learn.microsoft.com/azure/security/fundamentals/customer-lockbox-overview)
- [Azure Policy built-in initiative definitions](https://learn.microsoft.com/azure/governance/policy/samples/built-in-initiatives)
- [Sovereign Landing Zone](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/overview-sovereign-landing-zone)
