#!/usr/bin/env python3
"""
Zero Trust Architecture Implementation
L300-68: Comprehensive Zero Trust security model for sovereign cloud
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.azure.identity import ActiveDirectory, ConditionalAccess, ManagedIdentities
from diagrams.azure.security import KeyVaults, Sentinel, SecurityCenter
from diagrams.azure.network import Firewall, ApplicationGateway, VirtualNetworks
from diagrams.azure.compute import VM, KubernetesServices
from diagrams.azure.database import SQLDatabases
from diagrams.azure.storage import BlobStorage
from diagrams.azure.integration import APIManagement
from diagrams.azure.devops import Repos
from diagrams.onprem.client import Users, Client
from diagrams.onprem.network import Internet
from diagrams.generic.device import Mobile, Tablet
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
    "Zero Trust Architecture - Sovereign Cloud",
    filename=f"{output_dir}/zero-trust-architecture",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    outformat="svg"
):

    # Users and Devices (Untrusted)
    with Cluster("Identity & Devices\n(Never Trust)", graph_attr={"bgcolor": "#FFE6E6", "style": "rounded"}):
        users = Users("Users")
        devices = [Client("Managed\nDevice"), Mobile("BYOD"), Tablet("Partner\nDevice")]

    # Identity Verification Layer
    with Cluster("Verify Explicitly\n(Identity Provider)", graph_attr={"bgcolor": "#E6F3FF", "style": "rounded,bold"}):
        entra = ActiveDirectory("Microsoft\nEntra ID")
        conditional = ConditionalAccess("Conditional\nAccess")
        mfa = ManagedIdentities("MFA /\nPasswordless")

    # Network Security Layer
    with Cluster("Assume Breach\n(Network Security)", graph_attr={"bgcolor": "#FFF3E6", "style": "rounded"}):
        waf = ApplicationGateway("WAF / DDoS")
        fw = Firewall("Azure Firewall\n(L7 Filtering)")
        vnet = VirtualNetworks("Micro-\nSegmentation")

    # Application Layer
    with Cluster("Least Privilege Access\n(Applications)", graph_attr={"bgcolor": "#E6FFE6", "style": "rounded"}):
        apim = APIManagement("API Gateway\n(Token Validation)")
        aks = KubernetesServices("AKS\n(Workload ID)")
        vms = VM("VMs\n(JIT Access)")

    # Data Layer
    with Cluster("Data Protection\n(Encrypt Everything)", graph_attr={"bgcolor": "#F3E6FF", "style": "rounded"}):
        vault = KeyVaults("Key Vault\n(CMK/BYOK)")
        sql = SQLDatabases("SQL\n(TDE + AE)")
        blob = BlobStorage("Storage\n(Encryption)")

    # Security Operations
    with Cluster("Continuous Monitoring\n(SecOps)", graph_attr={"bgcolor": "#E6E6E6", "style": "rounded"}):
        sentinel = Sentinel("Microsoft\nSentinel")
        defender = SecurityCenter("Defender\nfor Cloud")

    # Flow: Users -> Identity
    users >> Edge(label="1. Authenticate", color="blue") >> entra
    for device in devices:
        device >> Edge(style="dashed") >> conditional
    entra >> conditional
    conditional >> mfa

    # Flow: Identity -> Network
    mfa >> Edge(label="2. Token", color="green") >> waf
    waf >> fw
    fw >> vnet

    # Flow: Network -> Apps
    vnet >> Edge(label="3. Authorized\nRequest", color="purple") >> apim
    apim >> aks
    apim >> vms

    # Flow: Apps -> Data
    aks >> Edge(label="4. Least\nPrivilege", color="orange") >> vault
    vault >> sql
    vault >> blob

    # Monitoring flows
    entra >> Edge(style="dotted", color="red") >> sentinel
    fw >> Edge(style="dotted", color="red") >> sentinel
    aks >> Edge(style="dotted", color="red") >> defender
    defender >> sentinel

print(f"✅ Generated: {output_dir}/zero-trust-architecture.svg")
