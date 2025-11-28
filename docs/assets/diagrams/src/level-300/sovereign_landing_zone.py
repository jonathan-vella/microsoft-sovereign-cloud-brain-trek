"""
Sovereign Landing Zone Architecture
Complete enterprise landing zone for sovereign cloud deployments
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.azure.general import Subscriptions, Managementgroups, Resourcegroups
from diagrams.azure.identity import ActiveDirectory, ConditionalAccess
from diagrams.azure.security import KeyVaults, Sentinel
from diagrams.azure.network import VirtualNetworks, Firewall, ApplicationGateway, ExpressrouteCircuits
from diagrams.azure.compute import VM, KubernetesServices
from diagrams.azure.storage import StorageAccounts
from diagrams.azure.database import SQLDatabases
from diagrams.azure.devops import Repos
from diagrams.azure.integration import LogicApps
from diagrams.generic.blank import Blank

graph_attr = {
    "fontsize": "14",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "ortho",
    "nodesep": "0.8",
    "ranksep": "1.0"
}

with Diagram(
    "Sovereign Landing Zone Architecture",
    filename="/workspaces/sov-cloud-brain-trek/docs/assets/images/level-300/sovereign-landing-zone",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    outformat=["svg"]
):
    # Management Group Hierarchy
    with Cluster("Management Group Hierarchy"):
        root_mg = Managementgroups("Root\nManagement Group")

        with Cluster("Platform"):
            identity_mg = Managementgroups("Identity")
            mgmt_mg = Managementgroups("Management")
            connectivity_mg = Managementgroups("Connectivity")

        with Cluster("Landing Zones"):
            corp_mg = Managementgroups("Corp")
            online_mg = Managementgroups("Online")
            sovereign_mg = Managementgroups("Sovereign")

    # Identity Subscription
    with Cluster("Identity Subscription", graph_attr={"bgcolor": "#E8F4FD"}):
        entra = ActiveDirectory("Microsoft\nEntra ID")
        cond_access = ConditionalAccess("Conditional\nAccess")

    # Management Subscription
    with Cluster("Management Subscription", graph_attr={"bgcolor": "#FFF4E6"}):
        sentinel = Sentinel("Microsoft\nSentinel")
        policy = Blank("Azure\nPolicy")
        automation = LogicApps("Automation")

    # Connectivity Subscription
    with Cluster("Connectivity Subscription", graph_attr={"bgcolor": "#F3E8FF"}):
        hub_vnet = VirtualNetworks("Hub VNet")
        firewall = Firewall("Azure\nFirewall")
        expressroute = ExpressrouteCircuits("ExpressRoute")
        app_gw = ApplicationGateway("Application\nGateway")

    # Sovereign Workload Subscription
    with Cluster("Sovereign Workload Subscription", graph_attr={"bgcolor": "#D4E9D7"}):
        spoke_vnet = VirtualNetworks("Spoke VNet")
        kv = KeyVaults("Key Vault\n(CMK)")
        vms = VM("Workload\nVMs")
        aks = KubernetesServices("AKS")
        storage = StorageAccounts("Encrypted\nStorage")
        sql = SQLDatabases("SQL DB")

    # Connections
    root_mg >> Edge(style="dashed") >> [identity_mg, mgmt_mg, connectivity_mg]
    root_mg >> Edge(style="dashed") >> [corp_mg, online_mg, sovereign_mg]

    identity_mg >> entra
    mgmt_mg >> sentinel
    connectivity_mg >> hub_vnet
    sovereign_mg >> spoke_vnet

    entra >> cond_access
    policy >> Edge(label="Governance", style="dotted") >> spoke_vnet
    hub_vnet >> firewall >> spoke_vnet
    expressroute >> hub_vnet

    spoke_vnet >> [vms, aks]
    kv >> Edge(label="CMK", style="dotted") >> [storage, sql]
    sentinel >> Edge(label="Monitor", style="dotted") >> spoke_vnet
