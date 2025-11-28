#!/usr/bin/env python3
"""
SDN (Software-Defined Networking) Architecture
L200-41: SDN architecture for Azure Local
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.azure.network import VirtualNetworks, LoadBalancers, Firewall
from diagrams.onprem.compute import Server
from diagrams.onprem.network import Internet
from diagrams.generic.network import Switch, Router, Firewall as GenFirewall
from diagrams.generic.virtualization import Vmware
import os

# Output path
output_dir = "/workspaces/sov-cloud-brain-trek/docs/assets/images/level-200"
os.makedirs(output_dir, exist_ok=True)

graph_attr = {
    "fontsize": "11",
    "bgcolor": "white",
    "pad": "0.4",
    "splines": "spline",
    "nodesep": "0.5",
    "ranksep": "0.7"
}

with Diagram(
    "Software-Defined Networking (SDN) Architecture",
    filename=f"{output_dir}/sdn-architecture",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    outformat="svg"
):

    # External
    inet = Internet("External\nNetwork")

    # SDN Control Plane
    with Cluster("SDN Control Plane", graph_attr={"bgcolor": "#E8F4FD", "style": "rounded,bold"}):
        nc = Server("Network\nController")
        slb_mux = LoadBalancers("SLB MUX")
        gw = Router("SDN\nGateway")

    # Physical Network
    with Cluster("Physical Network", graph_attr={"bgcolor": "#FFF4E6", "style": "rounded"}):
        tor1 = Switch("ToR Switch 1")
        tor2 = Switch("ToR Switch 2")

    # Hyper-V Hosts with Virtual Switch
    with Cluster("Hyper-V Hosts", graph_attr={"bgcolor": "#F3E8FF", "style": "rounded"}):

        with Cluster("Host 1"):
            vswitch1 = Switch("vSwitch")
            h1_vms = [Vmware("VM"), Vmware("VM")]

        with Cluster("Host 2"):
            vswitch2 = Switch("vSwitch")
            h2_vms = [Vmware("VM"), Vmware("VM")]

        with Cluster("Host 3"):
            vswitch3 = Switch("vSwitch")
            h3_vms = [Vmware("VM"), Vmware("VM")]

    # Virtual Networks
    with Cluster("Virtual Networks (Overlay)", graph_attr={"bgcolor": "#D4E9D7", "style": "rounded"}):
        vnet1 = VirtualNetworks("Tenant 1\nVNet")
        vnet2 = VirtualNetworks("Tenant 2\nVNet")
        vnet3 = VirtualNetworks("Shared\nServices")

    # Security
    with Cluster("Network Security", graph_attr={"bgcolor": "#FFE6E6", "style": "rounded"}):
        fw = GenFirewall("Distributed\nFirewall")
        acl = GenFirewall("Network\nACLs")

    # Connections
    inet >> gw
    gw >> slb_mux
    slb_mux >> nc

    nc >> Edge(label="Control", style="dashed", color="blue") >> vswitch1
    nc >> Edge(style="dashed", color="blue") >> vswitch2
    nc >> Edge(style="dashed", color="blue") >> vswitch3

    tor1 >> vswitch1
    tor1 >> vswitch2
    tor2 >> vswitch2
    tor2 >> vswitch3

    vswitch1 >> Edge(label="VXLAN") >> vnet1
    vswitch2 >> vnet1
    vswitch2 >> vnet2
    vswitch3 >> vnet3

    vnet1 >> fw
    vnet2 >> acl

print(f"✅ Generated: {output_dir}/sdn-architecture.svg")
