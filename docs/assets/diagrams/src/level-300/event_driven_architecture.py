"""
Event-Driven Architecture for Sovereignty
Async processing with data residency compliance
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.azure.integration import EventGridDomains, ServiceBus, LogicApps
from diagrams.azure.compute import FunctionApps, KubernetesServices
from diagrams.azure.storage import StorageAccounts, QueuesStorage
from diagrams.azure.database import CosmosDb
from diagrams.azure.analytics import EventHubs, StreamAnalyticsJobs

graph_attr = {
    "fontsize": "14",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "ortho",
    "nodesep": "0.8",
    "ranksep": "1.0"
}

with Diagram(
    "Event-Driven Architecture for Sovereignty",
    filename="/workspaces/sov-cloud-brain-trek/docs/assets/images/level-300/event-driven-architecture",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    outformat=["svg"]
):
    # Event Sources
    with Cluster("Event Sources", graph_attr={"bgcolor": "#E8F4FD"}):
        iot = EventHubs("IoT Events")
        app_events = EventGridDomains("Application\nEvents")
        storage_events = StorageAccounts("Storage\nEvents")

    # Event Routing
    with Cluster("Event Routing", graph_attr={"bgcolor": "#FFF4E6"}):
        event_grid = EventGridDomains("Event Grid\n(Regional)")
        service_bus = ServiceBus("Service Bus\n(Ordered)")
        queues = QueuesStorage("Storage\nQueues")

    # Event Processing
    with Cluster("Event Processing", graph_attr={"bgcolor": "#F3E8FF"}):
        functions = FunctionApps("Azure Functions\n(Serverless)")
        stream = StreamAnalyticsJobs("Stream\nAnalytics")
        logic = LogicApps("Logic Apps\n(Workflows)")
        aks = KubernetesServices("AKS\n(Complex Processing)")

    # Data Stores
    with Cluster("Event Stores (Regional)", graph_attr={"bgcolor": "#D4E9D7"}):
        cosmos = CosmosDb("Cosmos DB\n(Event Store)")
        cold_storage = StorageAccounts("Blob Storage\n(Archive)")

    # Connections
    [iot, app_events, storage_events] >> event_grid

    event_grid >> service_bus
    event_grid >> queues

    service_bus >> functions
    service_bus >> aks
    queues >> logic
    iot >> stream

    functions >> cosmos
    stream >> cosmos
    logic >> cosmos
    aks >> cosmos

    cosmos >> Edge(label="Archive", style="dashed") >> cold_storage
