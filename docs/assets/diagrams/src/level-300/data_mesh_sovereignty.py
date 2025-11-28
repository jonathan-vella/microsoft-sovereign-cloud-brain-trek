"""
Data Mesh for Sovereignty
Domain-oriented data ownership with sovereignty controls
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.azure.database import SQLDatabases, CosmosDb, DataLake
from diagrams.azure.analytics import Databricks, SynapseAnalytics
from diagrams.azure.integration import AzureDataCatalog
from diagrams.azure.integration import APIManagement
from diagrams.azure.security import KeyVaults
from diagrams.azure.network import VirtualNetworks
from diagrams.azure.general import Tags

graph_attr = {
    "fontsize": "14",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "ortho",
    "nodesep": "0.8",
    "ranksep": "1.0"
}

with Diagram(
    "Data Mesh for Sovereignty",
    filename="/workspaces/sov-cloud-brain-trek/docs/assets/images/level-300/data-mesh-sovereignty",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    outformat=["svg"]
):
    # Governance Layer
    with Cluster("Federated Governance", graph_attr={"bgcolor": "#F3E8FF"}):
        purview = AzureDataCatalog("Microsoft Purview\n(Data Catalog)")
        policy = Tags("Data Policies\n(Residency)")
        kv = KeyVaults("Key Vault\n(CMK)")

    # Data Products Layer
    with Cluster("Domain Data Products"):

        # Sales Domain
        with Cluster("Sales Domain (EU)", graph_attr={"bgcolor": "#E8F4FD"}):
            sales_vnet = VirtualNetworks("EU VNet")
            sales_sql = SQLDatabases("Sales DB")
            sales_api = APIManagement("Sales API")

        # Customer Domain
        with Cluster("Customer Domain (EU)", graph_attr={"bgcolor": "#FFF4E6"}):
            cust_vnet = VirtualNetworks("EU VNet")
            cust_cosmos = CosmosDb("Customer DB")
            cust_api = APIManagement("Customer API")

        # Analytics Domain
        with Cluster("Analytics Domain (EU)", graph_attr={"bgcolor": "#D4E9D7"}):
            analytics_vnet = VirtualNetworks("EU VNet")
            lake = DataLake("Data Lake\n(Aggregated)")
            databricks = Databricks("Databricks")
            synapse = SynapseAnalytics("Synapse")

    # Cross-Domain Data Sharing
    data_mesh_api = APIManagement("Data Mesh\nData Products API")

    # Connections
    purview >> Edge(label="Catalog", style="dotted") >> [sales_sql, cust_cosmos, lake]
    policy >> Edge(label="Policies", style="dotted") >> [sales_vnet, cust_vnet, analytics_vnet]
    kv >> Edge(label="CMK", style="dashed") >> [sales_sql, cust_cosmos, lake]

    sales_sql >> sales_api
    cust_cosmos >> cust_api

    [sales_api, cust_api] >> data_mesh_api
    data_mesh_api >> lake

    lake >> databricks >> synapse
