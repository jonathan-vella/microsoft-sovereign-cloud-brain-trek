#!/usr/bin/env python3
"""
Cloud Deployment Models Architecture Diagram
L50-05: Visual comparison of Public, Private, Hybrid, and Multi-cloud deployments
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.azure.compute import VM
from diagrams.azure.network import VirtualNetworks
from diagrams.azure.security import KeyVaults
from diagrams.onprem.compute import Server
from diagrams.onprem.network import Internet
from diagrams.generic.network import Firewall
from diagrams.generic.storage import Storage
import os

# Output path
output_dir = "/workspaces/sov-cloud-brain-trek/docs/assets/images/level-50"
os.makedirs(output_dir, exist_ok=True)

graph_attr = {
    "fontsize": "14",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "ortho",
    "nodesep": "0.8",
    "ranksep": "1.0"
}

with Diagram(
    "Cloud Deployment Models Comparison",
    filename=f"{output_dir}/cloud-deployment-models",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    outformat="svg"
):

    # Public Cloud
    with Cluster("Public Cloud\n(Azure, AWS, GCP)", graph_attr={"bgcolor": "#E6F3FF", "style": "rounded"}):
        public_vms = [VM("VM"), VM("VM"), VM("VM")]
        public_net = VirtualNetworks("VNet")

    # Private Cloud
    with Cluster("Private Cloud\n(On-Premises)", graph_attr={"bgcolor": "#E6FFE6", "style": "rounded"}):
        private_servers = [Server("Server"), Server("Server")]
        private_storage = Storage("Storage")
        private_fw = Firewall("Firewall")

    # Hybrid Cloud
    with Cluster("Hybrid Cloud", graph_attr={"bgcolor": "#FFF3E6", "style": "rounded"}):
        with Cluster("Azure"):
            hybrid_azure = VM("Azure VM")
            hybrid_vault = KeyVaults("Key Vault")
        with Cluster("On-Premises"):
            hybrid_onprem = Server("Local Server")

        hybrid_onprem >> Edge(label="VPN/ExpressRoute", style="dashed") >> hybrid_azure

    # Internet connectivity
    inet = Internet("Internet")

    inet >> public_net
    inet >> private_fw

print(f"✅ Generated: {output_dir}/cloud-deployment-models.svg")
