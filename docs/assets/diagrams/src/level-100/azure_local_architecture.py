#!/usr/bin/env python3
"""
Generate Azure Local Architecture Stack diagram.
Shows the full Azure Local infrastructure stack.
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.azure.compute import VM, KubernetesServices
from diagrams.azure.general import Resourcegroups
from diagrams.azure.storage import StorageAccounts
from diagrams.azure.network import VirtualNetworks
from diagrams.azure.identity import ActiveDirectory
from diagrams.azure.security import KeyVaults
from diagrams.azure.devops import Repos
from diagrams.azure.integration import AzureStackEdge
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "images" / "level-100"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

graph_attr = {
    "fontsize": "14",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "ortho",
}

node_attr = {
    "fontsize": "11",
}

def create_diagram():
    output_file = str(OUTPUT_DIR / "azure-local-architecture")

    with Diagram(
        "Azure Local Architecture Stack",
        filename=output_file,
        show=False,
        direction="TB",
        graph_attr=graph_attr,
        node_attr=node_attr,
        outformat=["svg", "png"],
    ):
        with Cluster("Azure Cloud"):
            arc = Repos("Azure Arc")
            portal = Resourcegroups("Azure Portal")
            entra = ActiveDirectory("Entra ID")

        with Cluster("On-Premises - Azure Local Cluster"):
            with Cluster("Management Layer"):
                wac = Resourcegroups("Windows Admin\nCenter")
                arc_agent = Repos("Arc Agent")

            with Cluster("Workload Layer"):
                with Cluster("Virtual Machines"):
                    vm1 = VM("VM 1")
                    vm2 = VM("VM 2")

                with Cluster("Kubernetes"):
                    aks = KubernetesServices("AKS Hybrid")

            with Cluster("Platform Layer"):
                hv = Resourcegroups("Hyper-V")
                sdn = VirtualNetworks("SDN")
                s2d = StorageAccounts("Storage Spaces\nDirect")

            with Cluster("Hardware Layer"):
                node1 = AzureStackEdge("Node 1")
                node2 = AzureStackEdge("Node 2")
                node3 = AzureStackEdge("Node 3")

        # Connections
        portal >> Edge(label="Management") >> arc
        arc >> Edge(label="Policies") >> arc_agent
        entra >> Edge(label="Identity") >> arc_agent

        arc_agent >> wac
        wac >> [vm1, vm2, aks]

        vm1 >> hv
        vm2 >> hv
        aks >> hv

        hv >> [node1, node2, node3]
        sdn >> [node1, node2, node3]
        s2d >> [node1, node2, node3]

    print(f"✅ Generated: {output_file}.svg")

if __name__ == "__main__":
    create_diagram()
