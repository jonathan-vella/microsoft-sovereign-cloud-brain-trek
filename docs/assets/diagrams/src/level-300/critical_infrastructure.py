"""
Critical Infrastructure Architecture
OT/IT convergence for critical infrastructure protection
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.azure.network import VirtualNetworks, Firewall, VirtualNetworkGateways
from diagrams.azure.compute import VM, KubernetesServices
from diagrams.azure.iot import IotHub, TimeSeriesInsightsEnvironments
from diagrams.azure.storage import StorageAccounts
from diagrams.azure.database import SQLDatabases
from diagrams.azure.security import KeyVaults, Sentinel
from diagrams.azure.analytics import StreamAnalyticsJobs
from diagrams.generic.compute import Rack
from diagrams.generic.device import Tablet

graph_attr = {
    "fontsize": "14",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "ortho",
    "nodesep": "0.8",
    "ranksep": "1.0"
}

with Diagram(
    "Critical Infrastructure Architecture",
    filename="/workspaces/sov-cloud-brain-trek/docs/assets/images/level-300/critical-infrastructure",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    outformat=["svg"]
):
    # OT Environment (Air-Gapped)
    with Cluster("OT Environment (Purdue Model)", graph_attr={"bgcolor": "#FFE4E1"}):
        with Cluster("Level 0-2: Process Control"):
            plc = Rack("PLCs/RTUs")
            scada = Tablet("SCADA/HMI")
            historian = Rack("Local Historian")

        with Cluster("Level 3: Site Operations"):
            dmz = Rack("OT DMZ")
            edge_gw = Rack("Edge Gateway\n(Azure IoT Edge)")

    # IT/OT Boundary
    with Cluster("IT/OT Convergence Zone", graph_attr={"bgcolor": "#FFF4E6"}):
        firewall = Firewall("Industrial\nFirewall")
        vpn = VirtualNetworkGateways("Secure VPN")
        bastion = VM("Azure Bastion")

    # Azure Cloud
    with Cluster("Azure Sovereign Cloud", graph_attr={"bgcolor": "#E8F4FD"}):
        vnet = VirtualNetworks("Industrial VNet")

        with Cluster("IoT & Analytics"):
            iot_hub = IotHub("IoT Hub\n(Device Twin)")
            stream = StreamAnalyticsJobs("Stream\nAnalytics")
            tsi = TimeSeriesInsightsEnvironments("Time Series\\nInsights")

        with Cluster("Applications"):
            aks = KubernetesServices("AKS\n(Analytics)")
            apps = VM("Industrial\nApps")

        with Cluster("Data & Security"):
            storage = StorageAccounts("Cold Storage\n(Telemetry)")
            sql = SQLDatabases("SQL DB")
            kv = KeyVaults("Key Vault")
            sentinel = Sentinel("Sentinel\n(OT Workbooks)")

    # Connections
    plc >> scada >> historian
    historian >> dmz >> edge_gw

    edge_gw >> firewall >> vpn >> vnet
    bastion >> Edge(label="Secure Access", style="dotted") >> [scada, apps]

    vnet >> iot_hub >> stream >> [tsi, storage]
    stream >> aks
    aks >> sql

    kv >> Edge(label="Secrets", style="dashed") >> edge_gw
    sentinel >> Edge(label="OT Threat Detection", style="dotted") >> vnet
