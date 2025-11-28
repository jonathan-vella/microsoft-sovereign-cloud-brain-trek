"""
Observability Stack for Sovereign Cloud
Complete monitoring and observability with data residency
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.azure.security import Sentinel
from diagrams.azure.devops import ApplicationInsights
from diagrams.azure.analytics import LogAnalyticsWorkspaces, Databricks
from diagrams.azure.compute import KubernetesServices, VM, FunctionApps
from diagrams.azure.network import VirtualNetworks
from diagrams.azure.integration import EventGridDomains
from diagrams.azure.storage import StorageAccounts

graph_attr = {
    "fontsize": "14",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "ortho",
    "nodesep": "0.8",
    "ranksep": "1.0"
}

with Diagram(
    "Observability Stack for Sovereign Cloud",
    filename="/workspaces/sov-cloud-brain-trek/docs/assets/images/level-300/observability-stack",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    outformat=["svg"]
):
    # Data Sources
    with Cluster("Telemetry Sources", graph_attr={"bgcolor": "#E8F4FD"}):
        aks = KubernetesServices("AKS\nContainers")
        vms = VM("Virtual\nMachines")
        functions = FunctionApps("Azure\nFunctions")
        vnet = VirtualNetworks("Network\nFlow Logs")

    # Collection Layer
    with Cluster("Collection & Ingestion", graph_attr={"bgcolor": "#FFF4E6"}):
        app_insights = ApplicationInsights("Application\nInsights")
        event_grid = EventGridDomains("Event Grid\n(Alerts)")

    # Central Analytics
    with Cluster("Central Analytics (Regional)", graph_attr={"bgcolor": "#F3E8FF"}):
        log_analytics = LogAnalyticsWorkspaces("Log Analytics\nWorkspace (EU)")
        sentinel = Sentinel("Microsoft\nSentinel")

    # Storage & Archive
    with Cluster("Long-term Storage (Regional)", graph_attr={"bgcolor": "#D4E9D7"}):
        storage = StorageAccounts("Blob Storage\n(7+ Years)")
        databricks = Databricks("Databricks\n(Analysis)")

    # Connections
    [aks, vms, functions] >> app_insights
    vnet >> log_analytics

    app_insights >> log_analytics
    log_analytics >> sentinel

    event_grid >> Edge(label="Alerts", style="dotted") >> sentinel

    log_analytics >> Edge(label="Export", style="dashed") >> storage
    storage >> databricks
