"""
Multi-Region Sovereign Deployment Architecture
Geographic distribution with data residency compliance
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.azure.network import VirtualNetworks, Firewall, TrafficManagerProfiles, FrontDoors
from diagrams.azure.compute import VM, KubernetesServices
from diagrams.azure.storage import StorageAccounts
from diagrams.azure.database import SQLDatabases, CosmosDb
from diagrams.azure.security import KeyVaults
from diagrams.azure.integration import EventGridDomains

graph_attr = {
    "fontsize": "14",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "ortho",
    "nodesep": "0.8",
    "ranksep": "1.0"
}

with Diagram(
    "Multi-Region Sovereign Deployment",
    filename="/workspaces/sov-cloud-brain-trek/docs/assets/images/level-300/multi-region-sovereign",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    outformat=["svg"]
):
    # Global Layer
    front_door = FrontDoors("Azure Front Door\nGlobal Load Balancer")
    traffic_mgr = TrafficManagerProfiles("Traffic Manager\nDNS-based Routing")

    # Region 1 - EU West
    with Cluster("Region 1: EU West (Primary)", graph_attr={"bgcolor": "#E8F4FD"}):
        with Cluster("Hub VNet EU"):
            fw_eu = Firewall("Firewall EU")

        with Cluster("Workload VNet EU"):
            aks_eu = KubernetesServices("AKS EU")
            vm_eu = VM("VMs EU")

        with Cluster("Data Layer EU"):
            kv_eu = KeyVaults("Key Vault EU")
            storage_eu = StorageAccounts("Storage EU")
            sql_eu = SQLDatabases("SQL EU\n(Primary)")
            cosmos_eu = CosmosDb("Cosmos DB EU")

    # Region 2 - EU North
    with Cluster("Region 2: EU North (Secondary)", graph_attr={"bgcolor": "#FFF4E6"}):
        with Cluster("Hub VNet EU North"):
            fw_eun = Firewall("Firewall EU-N")

        with Cluster("Workload VNet EU North"):
            aks_eun = KubernetesServices("AKS EU-N")
            vm_eun = VM("VMs EU-N")

        with Cluster("Data Layer EU North"):
            kv_eun = KeyVaults("Key Vault EU-N")
            storage_eun = StorageAccounts("Storage EU-N\n(GRS)")
            sql_eun = SQLDatabases("SQL EU-N\n(Replica)")
            cosmos_eun = CosmosDb("Cosmos DB EU-N")

    # Replication
    replication = EventGridDomains("Async\nReplication")

    # Connections
    front_door >> traffic_mgr
    traffic_mgr >> [fw_eu, fw_eun]

    fw_eu >> aks_eu
    fw_eu >> vm_eu
    fw_eun >> aks_eun
    fw_eun >> vm_eun

    # Data replication
    sql_eu >> Edge(label="Geo-Replication", style="dashed", color="blue") >> sql_eun
    storage_eu >> Edge(label="GRS", style="dashed", color="green") >> storage_eun
    cosmos_eu >> Edge(label="Multi-region", style="dashed", color="purple") >> cosmos_eun
