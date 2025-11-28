#!/usr/bin/env python3
"""
Air-Gapped Azure Local Architecture
L300-61: Complete air-gapped deployment architecture
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server
from diagrams.onprem.network import Internet
from diagrams.onprem.security import Vault
from diagrams.onprem.client import Users
from diagrams.generic.storage import Storage
from diagrams.generic.network import Switch, Firewall
from diagrams.generic.virtualization import Vmware
import os

# Output path
output_dir = "/workspaces/sov-cloud-brain-trek/docs/assets/images/level-300"
os.makedirs(output_dir, exist_ok=True)

graph_attr = {
    "fontsize": "11",
    "bgcolor": "white",
    "pad": "0.4",
    "splines": "spline",
    "nodesep": "0.6",
    "ranksep": "0.8"
}

with Diagram(
    "Air-Gapped Azure Local Architecture",
    filename=f"{output_dir}/air-gapped-architecture",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    outformat="svg"
):

    # External World (Disconnected)
    with Cluster("External (NO CONNECTIVITY)", graph_attr={"bgcolor": "#FFE6E6", "style": "rounded,dashed"}):
        inet = Internet("Internet\n❌ Blocked")
        azure = Server("Azure Cloud\n❌ No Access")

    # Air Gap Boundary
    airgap = Firewall("AIR GAP\n🔒 Physical Isolation")

    # Secure Facility
    with Cluster("Secure Facility (SCIF/Air-Gapped)", graph_attr={"bgcolor": "#E8F4FD", "style": "rounded,bold"}):

        # Management Zone
        with Cluster("Management Zone", graph_attr={"bgcolor": "#FFF4E6", "style": "rounded"}):
            wac = Server("Windows\nAdmin Center")
            pki = Vault("Internal\nPKI/CA")
            ntp = Server("Local NTP\nServer")
            dns = Server("Local DNS")
            admin = Users("Administrators")

        # Compute Zone
        with Cluster("Compute Zone (Azure Local)", graph_attr={"bgcolor": "#D4E9D7", "style": "rounded"}):
            with Cluster("Cluster Nodes"):
                nodes = [Server("Node 1"), Server("Node 2"), Server("Node 3"), Server("Node 4")]

            with Cluster("Storage"):
                s2d = Storage("Storage Spaces\nDirect")

            with Cluster("Workloads"):
                vms = [Vmware("Classified\nVM"), Vmware("Classified\nVM"), Vmware("Classified\nVM")]

        # Security Zone
        with Cluster("Security Zone", graph_attr={"bgcolor": "#F3E8FF", "style": "rounded"}):
            siem = Server("Local SIEM")
            backup = Storage("Local Backup\n(Tape/Disk)")
            hsm = Vault("HSM\n(Key Storage)")

        # Network
        with Cluster("Isolated Network"):
            core_sw = Switch("Core Switch\n(Isolated)")
            mgmt_sw = Switch("Mgmt Switch")

    # Update Station (Sneakernet)
    with Cluster("Update Station (Offline Transfer)", graph_attr={"bgcolor": "#FFF9C4", "style": "rounded"}):
        update_pc = Server("Staging PC\n(Malware Scan)")
        usb = Storage("USB/DVD\nMedia")

    # Connections within secure facility
    admin >> wac
    wac >> mgmt_sw
    mgmt_sw >> nodes[0]

    for node in nodes:
        node >> core_sw

    core_sw >> s2d
    s2d >> vms[0]

    nodes[0] >> Edge(style="dotted", label="Certs") >> pki
    nodes[0] >> Edge(style="dotted") >> ntp
    nodes[0] >> Edge(style="dotted") >> dns

    core_sw >> siem
    s2d >> backup
    pki >> hsm

    # Air gap - NO connection
    inet >> Edge(style="dashed", color="red", label="❌ BLOCKED") >> airgap

    # Sneakernet flow
    usb >> Edge(label="Manual\nTransfer", color="orange") >> update_pc
    update_pc >> Edge(label="Scanned\nUpdates", color="green") >> wac

print(f"✅ Generated: {output_dir}/air-gapped-architecture.svg")
