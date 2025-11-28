"""
Financial Services Sovereign Architecture
PCI-DSS and regulatory compliant financial deployment
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.azure.network import VirtualNetworks, Firewall, ApplicationGateway, PrivateEndpoint, FrontDoors
from diagrams.azure.compute import KubernetesServices, VM
from diagrams.azure.storage import StorageAccounts
from diagrams.azure.database import SQLDatabases
from diagrams.azure.security import KeyVaults, Sentinel
from diagrams.azure.identity import ActiveDirectory, ConditionalAccess
from diagrams.azure.integration import APIManagement, EventGridDomains
from diagrams.azure.analytics import Databricks

graph_attr = {
    "fontsize": "14",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "ortho",
    "nodesep": "0.8",
    "ranksep": "1.0"
}

with Diagram(
    "Financial Services Sovereign Architecture",
    filename="/workspaces/sov-cloud-brain-trek/docs/assets/images/level-300/financial-services",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    outformat=["svg"]
):
    # Entry Point
    front_door = FrontDoors("Azure Front Door\n(DDoS Protection)")

    # Security Layer
    with Cluster("Security & Compliance", graph_attr={"bgcolor": "#F3E8FF"}):
        entra = ActiveDirectory("Microsoft Entra\n(PIM Enabled)")
        cond_access = ConditionalAccess("Conditional Access\n(Risk-based)")
        sentinel = Sentinel("Sentinel\n(SOC Integration)")
        kv = KeyVaults("Managed HSM\n(FIPS 140-2 L3)")

    # PCI Zone (Cardholder Data)
    with Cluster("PCI Zone - Cardholder Data Environment", graph_attr={"bgcolor": "#FFE4E1"}):
        pci_vnet = VirtualNetworks("PCI VNet\n(Isolated)")
        firewall = Firewall("Firewall\n(IDS/IPS)")
        app_gw = ApplicationGateway("WAF\n(OWASP Rules)")

        with Cluster("Payment Processing"):
            payment_aks = KubernetesServices("Payment AKS\n(Hardened)")
            apim = APIManagement("Payment API")

        with Cluster("Card Data Storage"):
            pci_sql = SQLDatabases("Card Data SQL\n(TDE + Always Encrypted)")
            pci_storage = StorageAccounts("Tokenized\nStorage")

    # Non-PCI Zone
    with Cluster("General Workload Zone", graph_attr={"bgcolor": "#E8F4FD"}):
        gen_vnet = VirtualNetworks("General VNet")

        with Cluster("Analytics"):
            databricks = Databricks("Databricks\n(Fraud Detection)")
            event_grid = EventGridDomains("Event Grid")

        with Cluster("Applications"):
            gen_aks = KubernetesServices("App AKS")
            gen_sql = SQLDatabases("App SQL")

    # Connections
    front_door >> app_gw
    entra >> cond_access >> app_gw
    app_gw >> firewall >> pci_vnet

    pci_vnet >> payment_aks >> apim
    apim >> [pci_sql, pci_storage]
    kv >> Edge(label="HSM Keys", style="dashed") >> [pci_sql, pci_storage]

    pci_vnet >> Edge(label="Peering", style="dotted") >> gen_vnet
    gen_vnet >> gen_aks
    event_grid >> databricks

    sentinel >> Edge(label="SIEM", style="dotted") >> [pci_vnet, gen_vnet]
