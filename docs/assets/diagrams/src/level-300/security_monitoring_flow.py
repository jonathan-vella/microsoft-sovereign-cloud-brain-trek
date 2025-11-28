#!/usr/bin/env python3
"""
Security Monitoring Flow
L300-66: Security monitoring and threat detection flow
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.azure.security import Sentinel, SecurityCenter
from diagrams.azure.analytics import LogAnalyticsWorkspaces, EventHubs
from diagrams.azure.integration import LogicApps
from diagrams.azure.devops import Boards
from diagrams.onprem.compute import Server
from diagrams.onprem.security import Vault
from diagrams.onprem.monitoring import Prometheus, Grafana
from diagrams.onprem.network import Internet
from diagrams.generic.network import Firewall
import os

# Output path
output_dir = "/workspaces/sov-cloud-brain-trek/docs/assets/images/level-300"
os.makedirs(output_dir, exist_ok=True)

graph_attr = {
    "fontsize": "11",
    "bgcolor": "white",
    "pad": "0.4",
    "splines": "spline",
    "nodesep": "0.5",
    "ranksep": "0.7"
}

with Diagram(
    "Security Monitoring Flow for Sovereign Cloud",
    filename=f"{output_dir}/security-monitoring-flow",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    outformat="svg"
):

    # Data Sources
    with Cluster("Security Data Sources", graph_attr={"bgcolor": "#F5F5F5", "style": "rounded"}):
        with Cluster("Azure Local"):
            hci_logs = Server("System Logs")
            hci_events = Server("Security Events")
            hci_metrics = Server("Performance")

        with Cluster("Network"):
            fw_logs = Firewall("Firewall Logs")
            flow_logs = Server("Flow Logs")

        with Cluster("Identity"):
            auth_logs = Vault("Auth Logs")
            priv_logs = Vault("Privileged\nAccess")

    # Collection Layer
    with Cluster("Log Collection", graph_attr={"bgcolor": "#E8F4FD", "style": "rounded"}):
        event_hub = EventHubs("Event Hub\n(Streaming)")
        log_analytics = LogAnalyticsWorkspaces("Log Analytics\nWorkspace")

    # Analysis Layer
    with Cluster("Threat Detection & Analysis", graph_attr={"bgcolor": "#FFF4E6", "style": "rounded"}):
        sentinel = Sentinel("Microsoft\nSentinel")
        defender = SecurityCenter("Defender\nfor Cloud")

        with Cluster("Detection Rules"):
            ml_rules = Server("ML-Based\nDetection")
            custom_rules = Server("Custom\nAnalytics")
            scheduled = Server("Scheduled\nQueries")

    # Response Layer
    with Cluster("Automated Response", graph_attr={"bgcolor": "#FFE6E6", "style": "rounded"}):
        playbooks = LogicApps("SOAR\nPlaybooks")
        automation = LogicApps("Auto\nRemediation")
        ticketing = Boards("Incident\nTickets")

    # Visualization
    with Cluster("Dashboards & Reporting", graph_attr={"bgcolor": "#D4E9D7", "style": "rounded"}):
        workbooks = Grafana("Azure\nWorkbooks")
        reports = Server("Compliance\nReports")
        alerts = Server("Alert\nNotifications")

    # External Integration
    with Cluster("External", graph_attr={"bgcolor": "#F3E8FF", "style": "rounded"}):
        soc = Server("SOC Team")
        threat_intel = Internet("Threat\nIntelligence")

    # Connections - Data Flow
    hci_logs >> event_hub
    hci_events >> event_hub
    hci_metrics >> log_analytics
    fw_logs >> event_hub
    flow_logs >> log_analytics
    auth_logs >> event_hub
    priv_logs >> event_hub

    event_hub >> log_analytics
    log_analytics >> sentinel
    log_analytics >> defender

    # Analysis connections
    sentinel >> ml_rules
    sentinel >> custom_rules
    sentinel >> scheduled

    threat_intel >> Edge(label="Enrichment", style="dashed") >> sentinel

    # Response connections
    ml_rules >> Edge(label="Trigger", color="red") >> playbooks
    custom_rules >> playbooks
    playbooks >> automation
    playbooks >> ticketing
    ticketing >> soc

    # Visualization connections
    sentinel >> workbooks
    defender >> reports
    sentinel >> alerts
    alerts >> soc

print(f"✅ Generated: {output_dir}/security-monitoring-flow.svg")
