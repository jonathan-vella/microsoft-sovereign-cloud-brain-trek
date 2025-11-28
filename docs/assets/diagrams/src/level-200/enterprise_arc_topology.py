#!/usr/bin/env python3
"""
Enterprise Azure Arc Topology
L200-43: Enterprise-scale Arc deployment patterns
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.azure.compute import VM, KubernetesServices
from diagrams.azure.database import SQLDatabases
from diagrams.azure.integration import EventGridDomains
from diagrams.azure.security import SecurityCenter, KeyVaults
from diagrams.azure.devops import Repos
from diagrams.onprem.compute import Server
from diagrams.onprem.container import Docker
from diagrams.aws.compute import EC2
from diagrams.gcp.compute import GCE
import os

# Output path
output_dir = "/workspaces/sov-cloud-brain-trek/docs/assets/images/level-200"
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
    "Enterprise Azure Arc Topology",
    filename=f"{output_dir}/enterprise-arc-topology",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    outformat="svg"
):

    # Azure Control Plane
    with Cluster("Azure Control Plane", graph_attr={"bgcolor": "#E8F4FD", "style": "rounded,bold"}):
        arc = EventGridDomains("Azure Arc\nResource Bridge")
        policy = SecurityCenter("Azure Policy\n(Governance)")
        defender = SecurityCenter("Defender\nfor Cloud")
        monitor = EventGridDomains("Azure Monitor")
        vault = KeyVaults("Key Vault")

    # Management Groups
    with Cluster("Management Hierarchy", graph_attr={"bgcolor": "#FFF9E6", "style": "rounded"}):
        mg_root = Repos("Root MG")
        mg_prod = Repos("Production")
        mg_dev = Repos("Development")
        mg_sovereign = Repos("Sovereign")

    # On-Premises
    with Cluster("On-Premises Datacenter", graph_attr={"bgcolor": "#FFF4E6", "style": "rounded"}):
        with Cluster("Azure Local Cluster"):
            hci_nodes = [Server("Node 1"), Server("Node 2"), Server("Node 3")]

        with Cluster("Legacy Servers"):
            legacy = [Server("Windows"), Server("Linux"), Server("SQL")]

        with Cluster("Kubernetes"):
            k8s = KubernetesServices("OpenShift")
            apps = [Docker("App 1"), Docker("App 2")]

    # AWS
    with Cluster("AWS (Multi-Cloud)", graph_attr={"bgcolor": "#FF9900", "style": "rounded"}):
        aws_servers = [EC2("EC2"), EC2("EC2")]
        aws_k8s = KubernetesServices("EKS")

    # GCP
    with Cluster("Google Cloud", graph_attr={"bgcolor": "#4285F4", "style": "rounded"}):
        gcp_servers = [GCE("GCE"), GCE("GCE")]
        gcp_k8s = KubernetesServices("GKE")

    # Edge Sites
    with Cluster("Edge Locations", graph_attr={"bgcolor": "#D4E9D7", "style": "rounded"}):
        edge1 = Server("Branch 1")
        edge2 = Server("Branch 2")
        edge3 = Server("Factory")

    # Connections - Arc managing everything
    arc >> Edge(label="Govern", color="blue") >> policy
    arc >> defender
    arc >> monitor

    policy >> Edge(style="dashed") >> mg_root
    mg_root >> mg_prod
    mg_root >> mg_dev
    mg_root >> mg_sovereign

    # Arc connections to resources
    arc >> Edge(label="Arc Agent", color="green") >> hci_nodes[0]
    arc >> Edge(color="green") >> legacy[0]
    arc >> Edge(color="green") >> k8s

    arc >> Edge(label="Multi-cloud", color="orange") >> aws_servers[0]
    arc >> Edge(color="orange") >> aws_k8s
    arc >> Edge(color="orange") >> gcp_servers[0]
    arc >> Edge(color="orange") >> gcp_k8s

    arc >> Edge(label="Edge", color="purple") >> edge1
    arc >> Edge(color="purple") >> edge2
    arc >> Edge(color="purple") >> edge3

print(f"✅ Generated: {output_dir}/enterprise-arc-topology.svg")
