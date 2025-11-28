"""
Disaster Recovery Topology for Sovereign Cloud
Multi-region DR with data sovereignty compliance
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.azure.network import VirtualNetworks, TrafficManagerProfiles, ExpressrouteCircuits
from diagrams.azure.compute import KubernetesServices, VM
from diagrams.azure.storage import StorageAccounts
from diagrams.azure.database import SQLDatabases
from diagrams.azure.security import KeyVaults
from diagrams.azure.integration import EventGridDomains
from diagrams.azure.devops import Repos as ASR

graph_attr = {
    "fontsize": "14",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "ortho",
    "nodesep": "0.8",
    "ranksep": "1.0"
}

with Diagram(
    "Disaster Recovery Topology",
    filename="/workspaces/sov-cloud-brain-trek/docs/assets/images/level-300/disaster-recovery-topology",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    outformat=["svg"]
):
    # Traffic Manager
    traffic_mgr = TrafficManagerProfiles("Traffic Manager\n(Priority Routing)")

    # Primary Region
    with Cluster("Primary Region: EU West", graph_attr={"bgcolor": "#D4E9D7"}):
        with Cluster("Production Workloads"):
            primary_vnet = VirtualNetworks("Primary VNet")
            primary_aks = KubernetesServices("AKS\n(Active)")
            primary_vms = VM("VMs\n(Active)")

        with Cluster("Primary Data"):
            primary_sql = SQLDatabases("SQL Primary\n(Read-Write)")
            primary_storage = StorageAccounts("Storage Primary\n(RA-GRS)")
            primary_kv = KeyVaults("Key Vault\n(Primary)")

    # Azure Site Recovery
    asr = ASR("Azure Site\nRecovery")

    # Secondary Region
    with Cluster("Secondary Region: EU North", graph_attr={"bgcolor": "#FFF4E6"}):
        with Cluster("DR Workloads"):
            dr_vnet = VirtualNetworks("DR VNet")
            dr_aks = KubernetesServices("AKS\n(Standby)")
            dr_vms = VM("VMs\n(Replicated)")

        with Cluster("DR Data"):
            dr_sql = SQLDatabases("SQL Secondary\n(Read-Only)")
            dr_storage = StorageAccounts("Storage Secondary\n(GRS Target)")
            dr_kv = KeyVaults("Key Vault\n(Secondary)")

    # On-Premises
    with Cluster("On-Premises (Optional)", graph_attr={"bgcolor": "#E8F4FD"}):
        expressroute = ExpressrouteCircuits("ExpressRoute")

    # Connections - Normal Operation
    traffic_mgr >> Edge(label="Active", color="green") >> primary_vnet
    traffic_mgr >> Edge(label="Standby", style="dashed", color="orange") >> dr_vnet

    primary_vnet >> primary_aks
    primary_vnet >> primary_vms

    # Replication
    primary_sql >> Edge(label="Geo-Replication", style="dashed", color="blue") >> dr_sql
    primary_storage >> Edge(label="RA-GRS", style="dashed", color="blue") >> dr_storage
    primary_kv >> Edge(label="Backup", style="dotted") >> dr_kv

    asr >> Edge(label="VM Replication", style="dashed", color="purple") >> [primary_vms, dr_vms]

    # On-prem connectivity
    expressroute >> [primary_vnet, dr_vnet]
