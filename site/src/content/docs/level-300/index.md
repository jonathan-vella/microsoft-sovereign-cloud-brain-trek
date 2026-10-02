---
title: "Level 300: Advanced"
description: "Architect-level design for Microsoft Sovereign Cloud: Azure Local at scale, Sovereign Landing Zone, Foundry Local in production, Zero Trust, operations, and industry patterns."
lastVerified: 2026-10-02
sidebar:
  label: Overview
  order: 6
---

Level 300 is for architects who design and run sovereign estates. Each module starts from a design decision, shows
the Microsoft services that implement it, and states the limits and preview features you have to plan around. The
modules above can be taken in any order after Level 200, but the Sovereign Landing Zone module is the base that the
patterns and industry modules build on.

## Before you start

Complete Level 200 and its knowledge checks, or have equivalent experience. You should be comfortable with Azure
landing zones, Azure Policy, Azure Arc, and at least one Azure Local deployment. Some modules include PowerShell and
Kubernetes resources, so read access to a lab helps but is not required.

## What to expect at this level

| Topic | What you design | Status to plan around |
|---|---|---|
| Azure Local | Fleets of instances, multi-site, networking, certificates, disconnected operations | Disconnected operations are GA from 2602; AKS under disconnected operations is preview ([Learn](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview)) |
| Sovereign Landing Zone | Management groups, Level 1 to 3 controls, accelerators | The `Microsoft.Sovereign` resource provider is at API version 2025-02-27-preview ([Learn](https://learn.microsoft.com/azure/templates/microsoft.sovereign/landingzoneaccounts)) |
| Foundry Local | Multi-node inference, routing, model lifecycle | Foundry Local on Azure Local and Agentic Retrieval (formerly Edge RAG) are preview ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/overview)) |
| Zero Trust | Seven technology pillars, including SecOps | Current adoption model ([Learn](https://learn.microsoft.com/security/zero-trust/deploy/overview)) |
| Operations and industries | Telemetry with residency, incident response, DORA and government clouds | Microsoft Ireland Operations Limited is a DORA critical ICT third-party provider ([Learn](https://learn.microsoft.com/compliance/dora/dora-what-is-dora)) |

:::note[Fleet scale and instance size]
Azure Local connected operations scale from one node to thousands of nodes across many instances. A single instance
still has a maximum of 16 machines (hyperconverged), 64 (disaggregated), or 128 nodes (multi-rack)
([connected operations overview](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/azure-local/connected-operations-overview)).
:::

## Sources

- [What is Microsoft Sovereign Cloud?](https://learn.microsoft.com/azure/azure-sovereign-clouds/microsoft-sovereign-cloud)
- [Connected operations for Azure Local](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/azure-local/connected-operations-overview)
- [Disconnected operations for Azure Local](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview)
- [Sovereign Landing Zone overview](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/overview-sovereign-landing-zone)
- [Microsoft.Sovereign landingZoneAccounts template reference](https://learn.microsoft.com/azure/templates/microsoft.sovereign/landingzoneaccounts)
- [What is Foundry Local on Azure Local?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/foundry-local/overview)
- [Zero Trust deployment overview](https://learn.microsoft.com/security/zero-trust/deploy/overview)
- [What is DORA?](https://learn.microsoft.com/compliance/dora/dora-what-is-dora)
