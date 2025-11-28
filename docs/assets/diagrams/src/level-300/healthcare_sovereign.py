"""
Healthcare Sovereign Cloud Architecture
HIPAA-compliant healthcare deployment with data sovereignty
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.azure.network import VirtualNetworks, Firewall, ApplicationGateway, PrivateEndpoint
from diagrams.azure.compute import KubernetesServices, VM
from diagrams.azure.storage import StorageAccounts
from diagrams.azure.database import SQLDatabases, CosmosDb
from diagrams.azure.security import KeyVaults, Sentinel
from diagrams.azure.identity import ActiveDirectory
from diagrams.azure.ml import MachineLearningServiceWorkspaces
from diagrams.azure.integration import APIManagement

graph_attr = {
    "fontsize": "14",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "ortho",
    "nodesep": "0.8",
    "ranksep": "1.0"
}

with Diagram(
    "Healthcare Sovereign Cloud Architecture",
    filename="/workspaces/sov-cloud-brain-trek/docs/assets/images/level-300/healthcare-sovereign",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    outformat=["svg"]
):
    # Security & Identity Layer
    with Cluster("Security & Identity", graph_attr={"bgcolor": "#F3E8FF"}):
        entra = ActiveDirectory("Microsoft Entra\n(MFA Required)")
        sentinel = Sentinel("Microsoft Sentinel\nHIPAA Workbook")
        kv = KeyVaults("Key Vault\n(HSM-backed)")

    # Network Security
    with Cluster("Network Security Layer", graph_attr={"bgcolor": "#FFE4E1"}):
        app_gw = ApplicationGateway("WAF v2")
        firewall = Firewall("Azure Firewall\nPremium")

    # Application Layer
    with Cluster("HIPAA Workload Zone", graph_attr={"bgcolor": "#E8F4FD"}):
        vnet = VirtualNetworks("Isolated VNet\n(No Internet)")

        with Cluster("Compute"):
            aks = KubernetesServices("AKS\n(Private Cluster)")
            ehr_app = VM("EHR Application")

        with Cluster("Integration"):
            apim = APIManagement("FHIR API\nManagement")

        with Cluster("AI/ML"):
            ml = MachineLearningServiceWorkspaces("Azure ML\n(PHI Processing)")

    # Data Layer
    with Cluster("PHI Data Layer (Encrypted)", graph_attr={"bgcolor": "#D4E9D7"}):
        private_ep = PrivateEndpoint("Private\nEndpoints")

        with Cluster("Databases"):
            sql = SQLDatabases("SQL Server\n(TDE + CMK)")
            cosmos = CosmosDb("Cosmos DB\n(PHI Documents)")

        with Cluster("Storage"):
            storage = StorageAccounts("Blob Storage\n(CMK Encrypted)")

    # Connections
    entra >> Edge(label="Zero Trust") >> app_gw
    app_gw >> firewall >> vnet
    sentinel >> Edge(label="Audit Logs", style="dotted") >> vnet

    vnet >> [aks, ehr_app]
    aks >> apim
    apim >> ml

    kv >> Edge(label="CMK", style="dashed") >> [sql, cosmos, storage]
    vnet >> private_ep >> [sql, cosmos, storage]
