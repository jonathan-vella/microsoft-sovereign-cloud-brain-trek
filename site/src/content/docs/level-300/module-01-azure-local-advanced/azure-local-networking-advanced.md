---
title: "Azure Local advanced networking"
description: "Plan Azure Local host networking, Network ATC intents, RDMA, SDN, logical networks, Arc gateway, and multi-rack network boundaries."
lastVerified: 2026-10-02
sidebar:
  order: 3
---

Azure Local networking is intent-based at the host layer and policy-based at the workload layer. Design the host network first. Then decide whether workload networks need simple VLAN-backed logical networks or Arc-managed SDN with network security groups.

The main traffic types are management, compute, storage, and, in disaggregated designs, cluster SMB or SAN-specific paths. Azure Local uses Network ATC to apply host network configuration from declared intents. Network ATC does not remove the need to design top-of-rack switches, VLANs, MTU, Data Center Bridging, proxy rules, and recovery paths.

## Network ATC intents

[Network ATC](https://learn.microsoft.com/azure/azure-local/deploy/network-atc?view=azloc-2609) provides an intent-based approach to host networking. You specify one or more intents for adapters, and Network ATC deploys the intended configuration. The supported intent types are management, compute, and storage.

Common patterns include:

| Pattern | Use when | Design notes |
| --- | --- | --- |
| Fully converged | A small deployment can carry management, compute, and storage on the same adapter set. | Requires switched storage. Not a fit for switchless storage. |
| Management plus compute, separate storage | Workload traffic and host management share a SET team, while storage uses dedicated adapters. | Common for switchless and switched hyperconverged designs. |
| Fully disaggregated | Each traffic type has separate adapters. | Useful when traffic isolation and predictable bandwidth matter more than port count. |
| Storage-only intent | Network ATC manages only storage adapters. | Management and compute are handled outside the storage intent. |
| Multiple compute intents | Different workload groups need different compute switches. | Requires enough symmetric adapters and clear VLAN planning. |

Adapters in the same intent must be symmetric across nodes. Physical switches must be configured before Network ATC deployment, including VLANs, MTU, and Data Center Bridging where required. Network ATC also configures default storage VLANs and automatic storage IP addressing unless you override those values.

## Switched and switchless storage

Switched storage uses top-of-rack switches for storage traffic. It fits larger node counts and most standard datacenter topologies. Switchless storage directly connects storage adapters between nodes and can reduce switch dependency for small clusters.

Microsoft documents switchless reference patterns for two-node, three-node, and four-node Azure Local deployments. In those patterns, Network ATC commonly creates one intent for management and compute traffic and another for storage traffic. RDMA adapters use SMB Multichannel for resiliency and bandwidth aggregation rather than teaming.

Switchless design does not mean unmanaged. It requires exact cabling, subnets, and adapter symmetry. For a four-node switchless pattern, Microsoft states that scaling out storage switchless systems is not supported and that the scenario is deployed by using ARM templates. Use switchless when the validated reference pattern matches the customer site. Use switched storage when the environment needs growth beyond the switchless pattern, easier operations, or standard network tooling.

## RDMA and adapter qualification

Azure Local uses RDMA for host cluster SMB traffic. RDMA reduces host CPU use by allowing SMB traffic to bypass much of the operating system network stack. Microsoft supports [iWARP and RoCE](https://learn.microsoft.com/azure/azure-local/concepts/host-network-requirements-disaggregated?view=azloc-2609#rdma), and RDMA adapters must use the same RDMA protocol when communicating.

Choose iWARP when the customer has little experience managing lossless Ethernet or does not control the top-of-rack switches. Choose RoCE when the datacenter already operates RoCE and can manage Data Center Bridging correctly. Microsoft states that DCB is required for RoCE and optional for iWARP. InfiniBand is not supported with Azure Local.

For disaggregated deployments, distinguish Ethernet cluster traffic from SAN traffic. Fibre Channel SAN storage does not use RDMA storage intent. iSCSI paths are standalone ports that Network ATC does not manage in the documented six-port pattern.

## Logical networks for Azure Local VMs

[Logical networks](https://learn.microsoft.com/azure/azure-local/manage/create-logical-networks?view=azloc-2609) are the Azure Local VM network abstraction. A logical network represents a physical network where Azure Local VMs can be provisioned and defines how VM network interfaces connect to that network. In baseline Azure Local designs, compute logical networks map to specific VLAN IDs on the physical fabric.

Plan logical networks with application routing, firewall zones, IP address ownership, and tenant separation in mind. A logical network is not a disaster recovery design by itself. If a VM can fail over to another site or another instance, the recovered VM still needs a routable network and a client redirection plan.

## SDN enabled by Azure Arc

[Software Defined Networking enabled by Azure Arc](https://learn.microsoft.com/azure/azure-local/concepts/sdn-overview?view=azloc-2609) is available with Azure Local 2506 and OS version 26100.xxxx or later. In this model, Network Controller runs as a Failover Cluster service instead of separate infrastructure VMs, and it integrates with the Azure Arc control plane.

Arc-managed SDN on Azure Local currently supports:

- Logical networks.
- Azure Local VM network interfaces.
- Network security groups.

It does not support virtual networks, software load balancers, or gateways such as VPN, L3, or GRE gateways. If workloads require the full Windows Server SDN stack, including virtual networks, software load balancers, and gateways, use the on-premises tools model or a Windows Server SDN deployment where that stack is supported.

Do not mix SDN management methods. If SDN is enabled by Arc, manage it only with Azure portal, Azure CLI, and ARM templates. If Network Controller was deployed with on-premises tools, do not attempt to run the Arc-managed method. AKS is supported on Azure Local instances configured with Arc-managed SDN, but associating NSGs with the logical network used for AKS workload deployment or with AKS workload VM NICs is not supported.

## Arc gateway, proxy, and firewalls

Connected Azure Local deployments need outbound access to Azure endpoints. [Arc gateway for Azure Local](https://learn.microsoft.com/azure/azure-local/deploy/deployment-azure-arc-gateway-overview?view=azloc-2609) can reduce the number of required endpoints. It introduces an Arc gateway resource in Azure and an Arc proxy service on Arc-enabled resources.

Arc gateway for Azure Local infrastructure and Azure Local VMs is generally available. Arc gateway for AKS on Azure Local is still preview. You can enable it on new Azure Local deployments running software version 2506 or later, but Microsoft states that you cannot enable Arc gateway after deployment.

Plan the exception list carefully. Arc gateway does not support HTTP traffic, so HTTP endpoints such as certificate revocation endpoints still need proxy or firewall access. It also does not support TLS terminating proxies. For Azure Local VMs, Arc HTTPS traffic can be sent to Arc gateway, but traffic for endpoints not managed by Arc gateway still routes through the enterprise proxy or firewall.

## Multi-rack networking

[Multi-rack deployments](https://learn.microsoft.com/azure/azure-local/multi-rack/multi-rack-overview?view=azloc-2609) include managed networking as part of the prescriptive rack design. Microsoft describes automated bootstrapping and lifecycle management of network devices using Azure APIs and ARM templates. The design includes logical Layer 2 and Layer 3 networks spanning racks.

Do not apply small-cluster switchless assumptions to multi-rack. Multi-rack has an aggregation and SAN rack, three or more compute racks, SAN storage, and managed network devices. It is a preintegrated architecture. The network design is a product boundary as much as a cabling plan.

## Design checklist

- Declare host network intents before choosing port counts.
- Use symmetric adapters for each Network ATC intent.
- Keep storage traffic nonrouted unless the reference architecture says otherwise.
- Match RDMA protocol and DCB requirements to the adapter and switch design.
- Treat logical networks as workload placement networks, not as site recovery.
- Use Arc-managed SDN only for its supported resources.
- Decide on Arc gateway during deployment, not after deployment.
- Keep proxy bypass lists, firewall rules, certificate revocation endpoints, and AKS subnet exceptions in the architecture record.

## Sources

- [Deploy host networking with Network ATC](https://learn.microsoft.com/azure/azure-local/deploy/network-atc?view=azloc-2609)
- [Network considerations for cloud deployments of Azure Local](https://learn.microsoft.com/azure/azure-local/plan/cloud-deployment-network-considerations?view=azloc-2609)
- [Azure Local storage switchless architecture](https://learn.microsoft.com/azure/architecture/hybrid/azure-local-switchless)
- [Host network requirements for Azure Local disaggregated deployments](https://learn.microsoft.com/azure/azure-local/concepts/host-network-requirements-disaggregated?view=azloc-2609)
- [Create logical networks for Azure Local VMs enabled by Azure Arc](https://learn.microsoft.com/azure/azure-local/manage/create-logical-networks?view=azloc-2609)
- [Software Defined Networking enabled by Azure Arc on Azure Local](https://learn.microsoft.com/azure/azure-local/concepts/sdn-overview?view=azloc-2609)
- [About Azure Arc gateway for Azure Local](https://learn.microsoft.com/azure/azure-local/deploy/deployment-azure-arc-gateway-overview?view=azloc-2609)
- [What are multi-rack deployments of Azure Local?](https://learn.microsoft.com/azure/azure-local/multi-rack/multi-rack-overview?view=azloc-2609)
