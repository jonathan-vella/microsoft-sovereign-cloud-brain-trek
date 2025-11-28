#!/usr/bin/env python3
"""
Storage Spaces Direct (S2D) Architecture
L200-40: Detailed S2D architecture for Azure Local
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.azure.storage import BlobStorage
from diagrams.onprem.compute import Server
from diagrams.onprem.network import Internet
from diagrams.generic.storage import Storage
from diagrams.generic.network import Switch
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
    "Storage Spaces Direct (S2D) Architecture",
    filename=f"{output_dir}/storage-spaces-direct",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    outformat="svg"
):

    # Physical Layer
    with Cluster("Physical Storage Layer", graph_attr={"bgcolor": "#FFF4E6", "style": "rounded"}):
        with Cluster("Node 1"):
            n1_nvme = [Storage("NVMe\nCache"), Storage("NVMe\nCache")]
            n1_ssd = [Storage("SSD\nCapacity"), Storage("SSD\nCapacity")]

        with Cluster("Node 2"):
            n2_nvme = [Storage("NVMe\nCache"), Storage("NVMe\nCache")]
            n2_ssd = [Storage("SSD\nCapacity"), Storage("SSD\nCapacity")]

        with Cluster("Node 3"):
            n3_nvme = [Storage("NVMe\nCache"), Storage("NVMe\nCache")]
            n3_ssd = [Storage("SSD\nCapacity"), Storage("SSD\nCapacity")]

    # Storage Bus Layer
    with Cluster("Storage Bus Layer (SBL)", graph_attr={"bgcolor": "#E8F4FD", "style": "rounded"}):
        sbl = Switch("Software\nStorage Bus")

    # Pool Layer
    with Cluster("Storage Pool", graph_attr={"bgcolor": "#F3E8FF", "style": "rounded"}):
        pool = Storage("Unified\nStorage Pool")

    # Virtual Disk Layer
    with Cluster("Virtual Disks (Resiliency)", graph_attr={"bgcolor": "#D4E9D7", "style": "rounded"}):
        mirror = Storage("2-Way\nMirror")
        three_mirror = Storage("3-Way\nMirror")
        parity = Storage("Parity\n(Erasure)")

    # CSV Layer
    with Cluster("Cluster Shared Volumes", graph_attr={"bgcolor": "#FFE6E6", "style": "rounded"}):
        csv1 = BlobStorage("CSV1\nVMs")
        csv2 = BlobStorage("CSV2\nData")
        csv3 = BlobStorage("CSV3\nBackup")

    # VM Layer
    with Cluster("Virtual Machines", graph_attr={"bgcolor": "#E6E6E6", "style": "rounded"}):
        vms = [Vmware("VM 1"), Vmware("VM 2"), Vmware("VM 3")]

    # Connections
    for nvme in n1_nvme + n2_nvme + n3_nvme:
        nvme >> Edge(style="dashed") >> sbl

    sbl >> pool

    pool >> mirror
    pool >> three_mirror
    pool >> parity

    mirror >> csv1
    three_mirror >> csv2
    parity >> csv3

    csv1 >> vms[0]
    csv2 >> vms[1]
    csv3 >> vms[2]

print(f"✅ Generated: {output_dir}/storage-spaces-direct.svg")
