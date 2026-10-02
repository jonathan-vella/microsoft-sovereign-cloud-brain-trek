---
title: "Azure Local at scale"
description: "Design connected Azure Local fleets by separating fleet scale, single-instance limits, update policy, Arc governance, and rack-scale patterns."
lastVerified: 2026-10-02
sidebar:
  order: 1
---

Connected Azure Local keeps workloads and data on-premises while Azure provides deployment, governance, monitoring, and lifecycle operations when connectivity is available. The design question is not only how large a cluster can become. You also decide how many Azure Local instances to operate, how to group them into fault domains, and how to keep every instance inside the supported release window.

Microsoft Learn describes connected operations as supporting environments "from one node to thousands of nodes" in a connected deployment. The [April 27, 2026 Microsoft blog](https://blogs.microsoft.com/blog/2026/04/27/microsoft-sovereign-private-cloud-scales-to-thousands-of-nodes-with-azure-local/) says Azure Local can grow from hundreds up to thousands of servers within one sovereign boundary. Treat those statements as fleet-scale statements. They describe many Azure Local instances governed together. They do not replace the single-instance limits of [16 nodes for hyperconverged deployments](https://learn.microsoft.com/azure/azure-local/overview/hyperconverged-overview?view=azloc-2609), [64 machines for disaggregated deployments](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/azure-local/connected-operations-overview), or [128 nodes for a multi-rack instance](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/azure-local/connected-operations-overview).

## Scale boundary decisions

Use three boundaries when you size Azure Local.

| Boundary | What it controls | Design decision |
| --- | --- | --- |
| Instance | Cluster membership, storage architecture, update unit, and failure domain | Grow the instance until you hit a deployment-type limit, operational limit, or failure-domain limit. |
| Site | Network, power, identity, local staff, and business continuity scope | Add instances per site when site isolation, local maintenance windows, or capacity ownership matters. |
| Fleet | Governance, inventory, policy, monitoring, and lifecycle reporting | Use Azure Arc, Azure Policy, Azure Monitor, and Azure Update Manager to manage many instances consistently. |

The first scaling decision is whether the next unit of capacity belongs inside the same instance. Keep one instance when the workload needs local failover inside the same failure domain, when the storage design supports the growth path, and when the maintenance window can absorb the larger update unit. Add another instance when you need a separate blast radius, a separate site, a separate hardware generation, a separate support team boundary, or a workload-specific maintenance cadence.

For very large datacenter footprints, multi-rack deployments change the unit of design. A [multi-rack deployment](https://learn.microsoft.com/azure/azure-local/multi-rack/multi-rack-overview?view=azloc-2609) is delivered as preintegrated racks with one aggregation and SAN rack plus three or more compute racks. The minimum footprint is four racks, and the control plane is currently available in East US, Australia East, and South Central US. Multi-rack instances require Azure Local 2511 or later and support up to 128 nodes per instance.

## Connected operations and the 30-day tolerance

Connected operations require periodic outbound connectivity to Azure. Azure Local can tolerate intermittent disconnection for [up to 30 days without affecting running workloads](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/azure-local/connected-operations-overview). Hyperconverged deployment guidance also states that Azure Local requires HTTPS outbound access to Azure endpoints at least every 30 days.

Design this tolerance as an operational buffer, not as a planned offline mode. If a customer expects routine operation without Azure connectivity, use [disconnected operations](/level-300/module-01-azure-local-advanced/azure-local-disconnected-operations/) instead of stretching the connected model. The connected model still depends on Azure for cloud-based management, policy, monitoring, deployment workflows, and update orchestration when those actions are needed.

## Release and update governance

Azure Local follows the [Modern Lifecycle policy](https://learn.microsoft.com/azure/azure-local/update/about-updates-23h2?view=azloc-2609#lifecycle-cadence). Systems must stay within six months of the most recent release to remain supported. The update model includes monthly cumulative updates, semiannual feature updates, hotfixes as needed, and Solution Builder Extension updates as needed.

For architects, the six-month support window turns update planning into capacity planning. Every instance needs:

1. A ring assignment that defines when it receives updates.
2. A maintenance window large enough for the instance size and workload placement.
3. A rollback and support path that includes OEM firmware and driver updates when the hardware uses Solution Builder Extension.
4. A record of the Arc resource bridge lifecycle.

The Arc resource bridge is part of Azure Local VM management. Microsoft warns that [solution updates must be applied within one year](https://learn.microsoft.com/azure/azure-local/update/about-updates-23h2?view=azloc-2609#lifecycle-cadence) to keep Arc resource bridge certificates valid and Azure Local VM functionality working. That one-year certificate pressure is a separate clock from the six-month Azure Local support window. Track both.

Systems with more than 16 nodes can have longer update runtimes. Microsoft recommends considering a separate Solution Builder Extension update from the solution update for systems of that size. If your platform has dozens of instances, update governance should be fleet-level, but execution remains per instance.

## Fleet operations with Arc and Azure services

Azure Local uses Azure as the control plane in connected mode. The connected operations overview lists Azure Monitor, Entra ID, Key Vault, and Update Manager as management and security services available for connected environments. Azure Arc is the bridge that makes on-premises infrastructure visible to those services.

Use Azure Arc and Azure Policy to standardize tags, locations, security baselines, and resource configuration. Use Azure Monitor and Log Analytics for telemetry and alerts. Use Azure Update Manager for Azure Local infrastructure updates and for guest operating system update compliance where supported. Keep workload update governance separate from platform update governance because Microsoft states that Azure Local solution updates do not cover customer workloads.

Arc gateway helps when a connected deployment has strict egress controls. For Azure Local, [Arc gateway is generally available for Azure Local infrastructure and Azure Local VMs, while Arc gateway for AKS on Azure Local is still preview](https://learn.microsoft.com/azure/azure-local/deploy/deployment-azure-arc-gateway-overview?view=azloc-2609). It reduces endpoint allowlists by routing supported Arc HTTPS traffic through an Arc gateway resource and Arc proxy. It does not eliminate every endpoint, and it does not support TLS terminating proxies.

## Rack-aware and multi-rack designs

Rack-aware clustering and multi-rack deployments solve different problems.

| Pattern | Use it when | Main limits |
| --- | --- | --- |
| Rack-aware clustering | You need a single Azure Local instance across two racks in a campus or same-site design. | Azure Local 2510 or later, two racks, 2+2 expandable to 3+3 and 4+4, 1 ms or less round-trip latency, no external SAN. |
| Multi-rack deployment | You need a large single instance with preintegrated racks, SAN storage, managed networking, and up to 128 nodes. | Azure Local 2511 or later, four-rack minimum, control-plane region availability currently limited to East US, Australia East, and South Central US. |
| Multiple instances | You need site, operational, tenant, hardware, or lifecycle separation. | Requires fleet governance and cross-instance workload recovery planning. |

[Rack-aware clustering](https://learn.microsoft.com/azure/azure-local/concepts/rack-aware-cluster-overview?view=azloc-2609) is a same-site availability pattern. It supports a single storage pool and distributes data copies evenly between two racks. It is not a substitute for multi-site disaster recovery.

[Multi-rack deployments](https://learn.microsoft.com/azure/azure-local/multi-rack/multi-rack-overview?view=azloc-2609) are a scale pattern. They include SAN storage, managed networking, and Arc-enabled services at a larger footprint. Use them when one large instance is the right operational boundary. Do not use them to avoid governance design. A 128-node instance still has one instance lifecycle, one large update unit, and one local control-plane dependency set.

## When to add instances instead of growing one

Add another Azure Local instance when any of these conditions apply:

- The workload needs a separate site or a disaster recovery target.
- The business requires a separate maintenance calendar.
- The hardware generation, OEM, or storage architecture differs.
- Update runtime would exceed the available maintenance window.
- A tenant, application group, or regulator needs a separate operational boundary.
- You need to place capacity closer to users or data sources.

Grow an existing instance when the workload benefits from local resource pooling, local failover, and one operational boundary, and when the deployment type still supports the node count. For example, adding nodes inside a rack-aware cluster may be right for a campus facility that needs rack-level tolerance. Adding another instance is a better fit for a second site, a separate disaster recovery boundary, or a regulated tenant that must have isolated operations.

## Sources

- [Connected operations overview](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/azure-local/connected-operations-overview)
- [Microsoft Sovereign Private Cloud scales to thousands of nodes with Azure Local](https://blogs.microsoft.com/blog/2026/04/27/microsoft-sovereign-private-cloud-scales-to-thousands-of-nodes-with-azure-local/)
- [What are hyperconverged deployments of Azure Local?](https://learn.microsoft.com/azure/azure-local/overview/hyperconverged-overview?view=azloc-2609)
- [What are multi-rack deployments of Azure Local?](https://learn.microsoft.com/azure/azure-local/multi-rack/multi-rack-overview?view=azloc-2609)
- [Azure Local rack aware clustering overview](https://learn.microsoft.com/azure/azure-local/concepts/rack-aware-cluster-overview?view=azloc-2609)
- [About updates for Azure Local](https://learn.microsoft.com/azure/azure-local/update/about-updates-23h2?view=azloc-2609)
- [About Azure Arc gateway for Azure Local](https://learn.microsoft.com/azure/azure-local/deploy/deployment-azure-arc-gateway-overview?view=azloc-2609)
