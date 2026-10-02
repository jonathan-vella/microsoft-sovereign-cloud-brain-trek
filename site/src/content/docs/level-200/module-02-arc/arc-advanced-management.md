---
title: "Arc advanced management"
description: "Plan advanced Azure Arc management with Arc gateway, resource bridge, Windows Server benefits, Update Manager, and Arc data services."
lastVerified: 2026-10-02
sidebar:
  order: 1
---

Advanced Azure Arc management is about reducing operational variance. At scale, the hard parts are outbound connectivity, version support, entitlement boundaries, patch cadence, and removing retired management paths before they become design debt.

## Use Arc gateway to reduce outbound allowlists

Azure Arc gateway reduces the network allowlist for Arc-enabled servers to seven required FQDNs while still letting teams view and audit Arc traffic ([Learn](https://learn.microsoft.com/azure/azure-arc/servers/arc-gateway)). Arc-enabled Kubernetes uses nine FQDNs for the base gateway path ([Learn](https://learn.microsoft.com/azure/azure-arc/kubernetes/arc-gateway-simplify-networking)). Azure Local still has deployment endpoints outside the gateway path, but the endpoint list is much smaller than the more than 200 endpoints represented by full Arc feature coverage ([Learn](https://learn.microsoft.com/azure/azure-local/deploy/deployment-azure-arc-gateway-overview)).

Arc gateway has two parts:

| Part | Role |
| --- | --- |
| Arc gateway resource | An Azure resource with a gateway URL, such as `<prefix>.gw.arc.azure.com`, that acts as a shared front end for Azure Arc traffic. |
| Arc proxy | A local proxy component that Arc agents and extensions use to send traffic through the gateway. On servers it runs with the Connected Machine agent. On Kubernetes it runs as an `arc-proxy` pod. |

Use Arc gateway when a customer needs a smaller public endpoint list and traffic auditability. Do not treat it as a private connectivity substitute. Arc gateway uses public cloud connectivity and the server documentation states a subscription limit of five gateway resources ([Learn](https://learn.microsoft.com/azure/azure-arc/servers/arc-gateway#current-limitations)). For capacity planning, one gateway resource can handle about 2,000 Arc-enabled server resources per Azure region, and Kubernetes-only planning uses about 1,000 clusters per gateway resource per region ([Learn](https://learn.microsoft.com/azure/azure-arc/servers/arc-gateway#plan-your-azure-arc-gateway-setup), [Learn](https://learn.microsoft.com/azure/azure-arc/kubernetes/arc-gateway-simplify-networking#plan-your-azure-arc-gateway-setup)).

Arc gateway is not recommended where a proxy must terminate or inspect TLS. Microsoft recommends skipping TLS inspection for the gateway endpoint because Arc gateway establishes a TLS session between the local proxy and the Azure gateway, then can establish a nested end-to-end TLS session to the target service ([Learn](https://learn.microsoft.com/azure/azure-arc/servers/arc-gateway#azure-arc-gateway-and-tls-inspection)).

:::caution[Check status by workload]
Arc gateway for Azure Local infrastructure and Azure Local VMs is generally available, but Arc gateway for AKS on Azure Local is still in preview ([Learn](https://learn.microsoft.com/azure/azure-local/deploy/deployment-azure-arc-gateway-overview)).
:::

## Plan resource bridge as a managed appliance

Azure Arc resource bridge is a prepackaged, Kubernetes-based virtual appliance that runs in a private cloud and lets Azure project on-premises resources as Azure resources. It supports Azure Local, VMware vSphere 7.0 and 8.0, and System Center Virtual Machine Manager (SCVMM) ([Learn](https://learn.microsoft.com/azure/azure-arc/resource-bridge/overview)).

Resource bridge is required for VM lifecycle management from Azure for supported private clouds. For example, Azure can create, resize, start, stop, and delete VMs through custom locations that map Azure requests to Azure Local, vCenter, or SCVMM targets. If the resource bridge is unavailable, local VMs keep running, but Azure management operations and status projection are affected.

Plan operations around these constraints:

| Design area | Planning point |
| --- | --- |
| Region support | Arc resource bridge is supported in 21 named Azure regions. The resource bridge and the Arc-enabled private cloud must both support the target region ([Learn](https://learn.microsoft.com/azure/azure-arc/resource-bridge/overview#version-and-region-support)). |
| Upgrade cadence | Keep the appliance within the last six months of releases or within the latest n-3 versions, whichever is more recent. Microsoft says you must still upgrade at least once every six months ([Learn](https://learn.microsoft.com/azure/azure-arc/resource-bridge/overview#supported-versions)). |
| Resiliency | Arc resource bridge does not support cross-region failover. Local workloads continue, but Azure management can be unavailable during an outage ([Learn](https://learn.microsoft.com/azure/azure-arc/resource-bridge/overview#regional-resiliency)). |
| Private connectivity | Arc resource bridge currently does not support Private Link ([Learn](https://learn.microsoft.com/azure/azure-arc/resource-bridge/overview#private-link-support)). |

Use resource bridge for self-service VM operations and consistent Azure governance. Do not use it as a general disaster recovery layer.

## Use Windows Server benefits through Arc deliberately

Windows Server pay-as-you-go through Azure Arc is available for Windows Server 2025 and later. It bills the operating system license per core and per hour through Azure, supports Standard and Datacenter at the same price, and does not require product keys or client access licenses for base functionality ([Learn](https://learn.microsoft.com/azure/azure-arc/servers/cloud-native/licensing-cost-management#windows-server-pay-as-you-go)).

Windows Server Management enabled by Azure Arc adds a benefits bundle for eligible attested servers or servers enrolled in Windows Server pay-as-you-go. Benefits include Azure Update Manager, Change Tracking and Inventory, Azure Machine Configuration, Windows Admin Center in Azure for Arc, Remote Support, Network HUD, Best Practices Assessment, Azure Site Recovery configuration, and Azure File Sync benefits ([Learn](https://learn.microsoft.com/azure/azure-arc/servers/windows-server-management-overview)).

Network HUD is Windows Server 2025 only, so do not include it in a Windows Server 2019 or 2022 benefits story ([Learn](https://learn.microsoft.com/azure/azure-arc/servers/windows-server-management-overview)). Also remember that some benefits can still generate linked costs. For example, Change Tracking and Inventory and Best Practices Assessment can require Log Analytics ingestion, and Azure Site Recovery still incurs its own service costs.

## Standardize update and configuration operations

Azure Update Manager assesses update status and deploys one-time or recurring updates to Arc-enabled Windows Server 2012 and later as part of the Windows Server Management enabled by Azure Arc benefits table ([Learn](https://learn.microsoft.com/azure/azure-arc/servers/windows-server-management-overview)). Use maintenance windows, rings, and resource tags to separate production and non-production patch behavior.

Machine configuration is the Azure Policy feature that audits or configures operating system settings as code on Azure and Arc-enabled machines. Microsoft describes it as Azure Policy's machine configuration feature, formerly Azure Policy Guest Configuration, and lists enforcement modes for audit, apply and monitor, and apply and autocorrect ([Learn](https://learn.microsoft.com/azure/governance/machine-configuration/overview)). Use it for operating system baselines, local security settings, service state, and application presence checks that need Azure Policy reporting.

When combining Update Manager and machine configuration, separate patch compliance from configuration compliance. Patch compliance answers whether required updates are missing. Machine configuration answers whether the machine matches the desired operating system or application state.

## Keep Arc-enabled data services current

SQL Managed Instance enabled by Azure Arc is generally available in selected regions, but it must be planned with the current connectivity model ([Learn](https://learn.microsoft.com/azure/azure-arc/data/validation-program)). Azure Arc-enabled data services now support direct connectivity mode. Indirectly connected mode is retired as of September 2025 for SQL Managed Instance enabled by Azure Arc ([Learn](https://learn.microsoft.com/azure/azure-arc/data/connectivity), [Learn](https://learn.microsoft.com/azure/azure-arc/data/release-notes#september-2025)).

Remove these old design assumptions from proposals and runbooks:

| Retired or removed item | Current planning action |
| --- | --- |
| Indirectly connected mode for SQL Managed Instance enabled by Azure Arc | Plan direct connectivity to Azure for portal, Azure Resource Manager, Azure CLI, inventory, and billing. |
| Azure Arc-enabled PostgreSQL server | It retired in July 2025. Use Azure Database for PostgreSQL Flexible Server when that service fits the workload ([Learn](https://learn.microsoft.com/azure/azure-arc/data/what-is-azure-arc-enabled-postgresql)). |
| Grafana and OpenSearch dashboards for Arc-enabled SQL Managed Instance | They were removed for Arc-enabled SQL Managed Instance. Use supported monitoring paths instead ([Learn](https://learn.microsoft.com/azure/azure-arc/data/release-notes#august-2025)). |

## Sources

- [Simplify network configuration requirements with Azure Arc gateway](https://learn.microsoft.com/azure/azure-arc/servers/arc-gateway)
- [Simplify network configuration requirements with Azure Arc Gateway](https://learn.microsoft.com/azure/azure-arc/kubernetes/arc-gateway-simplify-networking)
- [About Azure Arc gateway for Azure Local](https://learn.microsoft.com/azure/azure-local/deploy/deployment-azure-arc-gateway-overview)
- [What is Azure Arc resource bridge?](https://learn.microsoft.com/azure/azure-arc/resource-bridge/overview)
- [Cloud-native licensing and cost management with Arc-enabled servers](https://learn.microsoft.com/azure/azure-arc/servers/cloud-native/licensing-cost-management)
- [Windows Server Management enabled by Azure Arc](https://learn.microsoft.com/azure/azure-arc/servers/windows-server-management-overview)
- [What is Azure Machine Configuration?](https://learn.microsoft.com/azure/governance/machine-configuration/overview)
- [Azure Arc-enabled data services Kubernetes validation](https://learn.microsoft.com/azure/azure-arc/data/validation-program)
- [Connectivity mode and requirements](https://learn.microsoft.com/azure/azure-arc/data/connectivity)
- [Release notes - Azure Arc-enabled data services](https://learn.microsoft.com/azure/azure-arc/data/release-notes)
- [Azure Arc-enabled PostgreSQL server](https://learn.microsoft.com/azure/azure-arc/data/what-is-azure-arc-enabled-postgresql)
