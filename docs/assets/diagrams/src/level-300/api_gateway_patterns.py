"""
API Gateway Patterns for Sovereign Cloud
Secure API management with data sovereignty
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.azure.network import VirtualNetworks, Firewall, ApplicationGateway, PrivateEndpoint
from diagrams.azure.compute import KubernetesServices
from diagrams.azure.integration import APIManagement
from diagrams.azure.security import KeyVaults
from diagrams.azure.identity import ActiveDirectory
from diagrams.onprem.network import Internet
from diagrams.generic.device import Mobile

graph_attr = {
    "fontsize": "14",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "ortho",
    "nodesep": "0.8",
    "ranksep": "1.0"
}

with Diagram(
    "API Gateway Patterns for Sovereignty",
    filename="/workspaces/sov-cloud-brain-trek/docs/assets/images/level-300/api-gateway-patterns",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    outformat=["svg"]
):
    # External Clients
    with Cluster("External Clients"):
        mobile = Mobile("Mobile Apps")
        internet = Internet("Partner APIs")

    # Security Layer
    with Cluster("Security Perimeter", graph_attr={"bgcolor": "#FFE4E1"}):
        entra = ActiveDirectory("Microsoft Entra\n(OAuth 2.0)")
        app_gw = ApplicationGateway("WAF v2\n(OWASP)")
        firewall = Firewall("Azure Firewall")

    # API Management
    with Cluster("API Management Zone", graph_attr={"bgcolor": "#E8F4FD"}):
        apim = APIManagement("Azure APIM\n(Internal Mode)")
        kv = KeyVaults("Key Vault\n(Certificates)")

    # Backend Services
    with Cluster("Backend Services (Private)", graph_attr={"bgcolor": "#D4E9D7"}):
        vnet = VirtualNetworks("Private VNet")
        private_ep = PrivateEndpoint("Private\nEndpoints")

        with Cluster("Microservices"):
            aks = KubernetesServices("AKS Cluster")
            svc1 = KubernetesServices("Service A")
            svc2 = KubernetesServices("Service B")
            svc3 = KubernetesServices("Service C")

    # Connections
    [mobile, internet] >> entra
    entra >> app_gw >> firewall >> apim

    kv >> Edge(label="mTLS Certs", style="dashed") >> apim

    apim >> private_ep >> vnet
    vnet >> aks
    aks >> [svc1, svc2, svc3]
