"""
Government Cloud Architecture
FedRAMP High / IL4-IL5 compliant government deployment
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.azure.network import VirtualNetworks, Firewall, ExpressrouteCircuits, PrivateEndpoint
from diagrams.azure.compute import KubernetesServices, VM
from diagrams.azure.storage import StorageAccounts
from diagrams.azure.database import SQLDatabases
from diagrams.azure.security import KeyVaults, Sentinel
from diagrams.azure.identity import ActiveDirectory
from diagrams.azure.general import Tags
from diagrams.generic.compute import Rack
from diagrams.onprem.network import Internet

graph_attr = {
    "fontsize": "14",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "ortho",
    "nodesep": "0.8",
    "ranksep": "1.0"
}

with Diagram(
    "Government Cloud Architecture (FedRAMP High)",
    filename="/workspaces/sov-cloud-brain-trek/docs/assets/images/level-300/government-cloud",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    outformat=["svg"]
):
    # Boundary
    internet = Internet("Internet\n(Blocked)")

    # Azure Government Region
    with Cluster("Azure Government (US Gov Virginia)", graph_attr={"bgcolor": "#E8F4FD"}):

        # Security & Governance
        with Cluster("Security & Governance", graph_attr={"bgcolor": "#F3E8FF"}):
            entra = ActiveDirectory("Entra ID\n(Gov Tenant)")
            sentinel = Sentinel("Sentinel\n(NIST 800-53)")
            policy = Tags("Azure Policy\n(FedRAMP High)")
            kv = KeyVaults("Key Vault\n(FIPS 140-2)")

        # Network Security
        with Cluster("Network Security Boundary"):
            expressroute = ExpressrouteCircuits("ExpressRoute\n(Dedicated)")
            firewall = Firewall("Firewall\n(Threat Intel)")
            hub_vnet = VirtualNetworks("Hub VNet")

        # IL4 Workload Zone
        with Cluster("IL4 Workload Zone", graph_attr={"bgcolor": "#FFF4E6"}):
            il4_vnet = VirtualNetworks("IL4 VNet")
            il4_aks = KubernetesServices("IL4 AKS\n(CUI Data)")
            il4_sql = SQLDatabases("IL4 SQL\n(Encrypted)")
            il4_storage = StorageAccounts("IL4 Storage")

        # IL5 Workload Zone (Higher Classification)
        with Cluster("IL5 Workload Zone", graph_attr={"bgcolor": "#FFE4E1"}):
            il5_vnet = VirtualNetworks("IL5 VNet\n(Isolated)")
            il5_vm = VM("IL5 VMs\n(National Security)")
            il5_sql = SQLDatabases("IL5 SQL\n(CMK + HSM)")
            private_ep = PrivateEndpoint("Private\nEndpoints")

    # On-Premises Government DC
    with Cluster("Government Data Center", graph_attr={"bgcolor": "#D4E9D7"}):
        gov_dc = Rack("Agency\nData Center")
        classified = Rack("Classified\nNetwork")

    # Connections
    internet >> Edge(label="❌ Blocked", color="red", style="dashed") >> hub_vnet
    gov_dc >> expressroute >> firewall >> hub_vnet

    hub_vnet >> il4_vnet
    hub_vnet >> Edge(label="Isolated", style="dashed") >> il5_vnet

    il4_vnet >> il4_aks
    il4_aks >> [il4_sql, il4_storage]

    il5_vnet >> il5_vm
    private_ep >> il5_sql
    kv >> Edge(label="HSM Keys", style="dotted") >> [il4_sql, il5_sql]

    policy >> Edge(label="Compliance", style="dotted") >> [il4_vnet, il5_vnet]
    sentinel >> Edge(label="Audit", style="dotted") >> [il4_vnet, il5_vnet]
