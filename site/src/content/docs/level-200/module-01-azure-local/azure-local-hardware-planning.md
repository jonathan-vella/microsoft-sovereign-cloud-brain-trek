---
title: "Plan Azure Local hardware"
description: "Use the Azure Local catalog, system requirements, hardware categories, SBE updates, and support boundaries to plan a supported deployment."
lastVerified: 2026-10-02
sidebar:
  order: 2
---

Azure Local hardware planning starts with supportability. Microsoft Support may only be provided for Azure Local running on hardware listed in the Azure Local catalog ([Learn](https://learn.microsoft.com/azure/azure-local/concepts/system-requirements-23h2#machine-and-storage-requirements)).

## Hardware categories

Azure Local hardware is available through the Azure Local catalog in three categories: Validated Nodes, Integrated Systems, and Premier Solutions. The categories matter because they affect how much integration, update automation, and partner validation you can expect.

| Category | Use when | Planning notes |
| --- | --- | --- |
| Validated Nodes | You need a supported building block and can perform more integration work yourself. | Validate firmware, driver, BIOS, storage, and network settings with the OEM guidance before deployment. |
| Integrated Systems | You want a more complete partner-integrated system. | Newer Integrated Systems added to the catalog from Azure Local 2311.2 onward must implement Solution Builder Extension support for firmware and driver updates ([Learn](https://learn.microsoft.com/azure/azure-local/update/solution-builder-extension#identify-a-solution-builder-extension-update-for-your-hardware)). |
| Premier Solutions | You need the most integrated option or a workload that requires it. | Premier Solutions are turnkey solutions developed with hardware partners. Disconnected operations requires Premier Solution hardware and a dedicated management cluster ([Learn](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview#eligibility-criteria)). |

The current research matrix lists these Azure Local hardware partners: ASUS, Blue Chip, DataON, Dell EMC, Fujitsu, HPE, Hitachi, Lenovo, NEC, primeLine Solutions, QCT, and Supermicro. Always use the live catalog before purchase because supported models change.

## Baseline system requirements

Azure Local system requirements cover Azure, compute, memory, storage, networking, security, and update prerequisites. Use the Learn article as the authority because the values change by deployment type and release.

For hyperconverged requirements, Microsoft documents these minimums and constraints:

| Area | Requirement to check |
| --- | --- |
| Azure | Supported Azure subscription, required deployment permissions, supported Azure region, and public network access for Key Vault when used. |
| Machines | 1 to 64 machines are supported in the system requirements article because the same article covers disaggregated requirements. Hyperconverged scale remains 1 to 16 machines in deployment-type guidance. |
| CPU | 64-bit Intel Nehalem grade or AMD EPYC or later compatible processor with SLAT. Processor properties must be compatible across nodes at deployment. |
| Memory | Minimum 32 GB RAM per machine with ECC. |
| Host network adapters | At least two adapters listed in the Windows Server Catalog, or dedicated adapters per intent. A storage intent requires two separate adapters when using dedicated storage adapters. |
| Boot drive | Minimum 200 GB, with 400 GB or more recommended for large-memory instances. |
| Data drives | At least two disks per server with a minimum capacity of 500 GB. Drives should match in number, type, capacity, performance, and firmware across servers at deployment. |
| Security | TPM 2.0 and Secure Boot must be present and enabled. |

Do not mix nodes casually. Microsoft documents that each machine must use the same model, manufacturer, processor types, network adapters, and number and type of storage drives at deployment ([Learn](https://learn.microsoft.com/azure/azure-local/concepts/system-requirements-23h2#machine-and-storage-requirements)). For OEM licensing, mixed-node scenarios with different hardware, OS, or billing models within one instance are not supported in the current research matrix.

## Storage hardware choices

Storage planning depends on whether the deployment uses direct-attached storage, SAN storage, or a compact appliance.

For Storage Spaces Direct, drives must be direct-attached and physically connected to a single machine. RAID controller cards, shared SAS enclosures connected to multiple machines, SAN storage through Fibre Channel, iSCSI, FCoE, and MPIO are not supported for Storage Spaces Direct data drives, except where Microsoft documents external SAN support for Azure Local ([Learn](https://learn.microsoft.com/azure/azure-local/concepts/system-requirements-23h2#data-drive-requirements)).

For direct-attached storage, Microsoft strongly recommends all-flash, single drive type, uniform performance for multi-node clusters. Hybrid two-tier designs with HDD capacity plus flash cache are supported, but only under the documented drive rules. Use that pattern only when the workload and cost model justify the added planning.

## Solution Builder Extension updates

Solution Builder Extension, or SBE in Azure CLI, packages hardware-vendor content for Azure Local. SBE packages can include driver and firmware updates, hardware monitoring enhancements, diagnostic tools, supplemental Windows Defender Application Control policies, and validation logic for pre-update health checks ([Learn](https://learn.microsoft.com/azure/azure-local/update/solution-builder-extension#about-the-extension)).

Starting with Azure Local 2311.2, these vendor updates are packaged as Solution Builder Extension packages. For systems that support SBE, the updates integrate into Azure Local solution updates and can appear in Azure portal or through `Get-SolutionUpdate` ([Learn](https://learn.microsoft.com/azure/azure-local/update/solution-builder-extension#solution-builder-extension-package-updates)).

Plan these SBE questions before procurement:

- Does the exact hardware model implement SBE?
- Does the vendor provide automatic download support, or must you import additional content?
- Are firmware and driver updates included in combined solution updates?
- Which maintenance window covers both Azure Local updates and vendor updates?
- Does the workload require Premier Solution hardware, such as disconnected operations or Microsoft 365 Local?

## Sizing guidance

Use the Azure Local sizer tool and partner sizing guidance rather than generic CPU, memory, and storage ratios. Microsoft Learn points planners to the sizer from the deployment-type page ([Learn](https://learn.microsoft.com/azure/azure-local/plan/find-your-deployment-type#step-2-what-scale-do-you-need)). Use the sizer to test workload profiles, then validate the bill of materials with the OEM.

For intermediate planning, keep three rules in front of stakeholders:

1. Supportability beats preference. If the hardware is not in the catalog or the OEM does not validate the combination, do not treat it as a supported production design.
2. Scale and storage model drive the deployment type. Hyperconverged is not a path to 64 machines, and disaggregated is not a rack-aware direct-attached storage design.
3. Updates are part of the hardware design. If SBE support is missing, firmware and driver operations require more manual process and stronger runbook controls.

## Sources

- [System requirements for Azure Local](https://learn.microsoft.com/azure/azure-local/concepts/system-requirements-23h2)
- [Find your Azure Local deployment type](https://learn.microsoft.com/azure/azure-local/plan/find-your-deployment-type)
- [Solution Builder Extension updates for your Azure Local](https://learn.microsoft.com/azure/azure-local/update/solution-builder-extension)
- [Disconnected operations for Azure Local](https://learn.microsoft.com/azure/azure-local/manage/disconnected-operations-overview)
