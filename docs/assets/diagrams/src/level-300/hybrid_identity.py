"""
Hybrid Identity Architecture
On-premises AD with Microsoft Entra ID for sovereign scenarios
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.azure.identity import ActiveDirectory, ConditionalAccess, ManagedIdentities
from diagrams.azure.security import KeyVaults
from diagrams.azure.compute import VM
from diagrams.azure.network import VirtualNetworks, VirtualNetworkGateways
from diagrams.onprem.identity import Dex
from diagrams.onprem.network import Internet
from diagrams.generic.device import Mobile, Tablet
from diagrams.generic.compute import Rack

graph_attr = {
    "fontsize": "14",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "ortho",
    "nodesep": "0.8",
    "ranksep": "1.0"
}

with Diagram(
    "Hybrid Identity Architecture",
    filename="/workspaces/sov-cloud-brain-trek/docs/assets/images/level-300/hybrid-identity",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    outformat=["svg"]
):
    # Users
    with Cluster("End Users"):
        mobile = Mobile("Mobile\nUsers")
        devices = Tablet("Corporate\nDevices")

    internet = Internet("Internet")

    # Cloud Identity
    with Cluster("Microsoft Entra ID", graph_attr={"bgcolor": "#E8F4FD"}):
        entra = ActiveDirectory("Microsoft\nEntra ID")
        cond_access = ConditionalAccess("Conditional\nAccess")
        managed_id = ManagedIdentities("Managed\nIdentities")

    # Azure Resources
    with Cluster("Azure Sovereign Cloud", graph_attr={"bgcolor": "#D4E9D7"}):
        vnet = VirtualNetworks("Azure VNet")
        kv = KeyVaults("Key Vault")
        workloads = VM("Workloads")

    # Hybrid Connectivity
    vpn = VirtualNetworkGateways("VPN/ExpressRoute")

    # On-Premises
    with Cluster("On-Premises Data Center", graph_attr={"bgcolor": "#FFF4E6"}):
        ad_connect = Rack("Entra Connect\nSync Server")
        ad_ds = Dex("Active Directory\nDomain Services")
        dc = Rack("Domain\nControllers")

    # Authentication Flow
    [mobile, devices] >> internet >> entra
    entra >> cond_access
    cond_access >> Edge(label="MFA + Device") >> vnet

    # Sync Flow
    ad_ds >> Edge(label="Password Hash\nSync", style="dashed") >> ad_connect
    ad_connect >> Edge(label="Sync", color="blue") >> entra
    dc >> ad_ds

    # Resource Access
    managed_id >> kv
    vnet >> workloads
    vnet >> Edge(label="S2S VPN") >> vpn >> ad_ds
