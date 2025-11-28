#!/usr/bin/env python3
"""
Azure Local Multi-Site Replication Topology
L300-60: Advanced multi-site deployment with replication
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.azure.compute import VM, VMScaleSet
from diagrams.azure.network import VirtualNetworks, ExpressrouteCircuits
from diagrams.azure.storage import BlobStorage
from diagrams.azure.identity import ActiveDirectory
from diagrams.azure.integration import EventGridDomains
from diagrams.onprem.compute import Server
from diagrams.onprem.network import Internet
from diagrams.generic.storage import Storage
from diagrams.generic.network import Switch
import os

# Output path
output_dir = "/workspaces/sov-cloud-brain-trek/docs/assets/images/level-300"
os.makedirs(output_dir, exist_ok=True)

graph_attr = {
    "fontsize": "12",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "spline",
    "nodesep": "0.6",
    "ranksep": "0.8"
}

with Diagram(
    "Azure Local Multi-Site Replication Topology",
    filename=f"{output_dir}/azure-local-multisite",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    outformat="svg"
):

    # Azure Control Plane
    with Cluster("Azure Cloud Control Plane", graph_attr={"bgcolor": "#E6F3FF", "style": "rounded,bold"}):
        azure_ad = ActiveDirectory("Entra ID")
        arc = EventGridDomains("Azure Arc")
        blob = BlobStorage("Witness Storage")

    # Site 1 - Primary
    with Cluster("Site 1: Primary Datacenter\n(Active)", graph_attr={"bgcolor": "#E6FFE6", "style": "rounded"}):
        with Cluster("Azure Local Cluster"):
            s1_nodes = [Server("Node 1"), Server("Node 2"), Server("Node 3")]
            s1_storage = Storage("S2D Storage")
            s1_switch = Switch("25GbE ToR")
        s1_vms = VMScaleSet("Production VMs")

    # Site 2 - DR
    with Cluster("Site 2: DR Datacenter\n(Standby)", graph_attr={"bgcolor": "#FFF3E6", "style": "rounded"}):
        with Cluster("Azure Local Cluster"):
            s2_nodes = [Server("Node 1"), Server("Node 2"), Server("Node 3")]
            s2_storage = Storage("S2D Storage")
            s2_switch = Switch("25GbE ToR")
        s2_vms = VMScaleSet("Replica VMs")

    # Site 3 - Edge
    with Cluster("Site 3: Edge Location\n(Branch)", graph_attr={"bgcolor": "#F3E6FF", "style": "rounded"}):
        with Cluster("Azure Local (2-node)"):
            s3_nodes = [Server("Node 1"), Server("Node 2")]
            s3_storage = Storage("Storage")
        s3_vms = VM("Edge Workloads")

    # Connectivity
    express = ExpressrouteCircuits("ExpressRoute\nGlobal Reach")

    # Replication flows
    s1_storage >> Edge(label="Sync Replication\n<5ms RTT", color="green", style="bold") >> s2_storage
    s1_storage >> Edge(label="Async Replication", color="orange", style="dashed") >> s3_storage

    # Arc management
    arc >> Edge(color="blue", style="dashed") >> s1_switch
    arc >> Edge(color="blue", style="dashed") >> s2_switch
    arc >> Edge(color="blue", style="dashed") >> s3_nodes[0]

    # Cloud witness
    s1_nodes[1] >> Edge(label="Witness", style="dotted") >> blob
    s2_nodes[1] >> Edge(label="Witness", style="dotted") >> blob

    # Express route
    s1_switch >> express
    s2_switch >> express
    express >> s3_nodes[0]

print(f"✅ Generated: {output_dir}/azure-local-multisite.svg")
