#!/usr/bin/env python3
"""
Production Edge RAG Architecture with High Availability
L300-63: Enterprise-grade RAG deployment pattern
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.azure.compute import KubernetesServices, ContainerInstances
from diagrams.azure.ml import MachineLearningServiceWorkspaces
from diagrams.azure.database import CosmosDb
from diagrams.azure.storage import BlobStorage
from diagrams.azure.network import LoadBalancers, ApplicationGateway
from diagrams.azure.security import KeyVaults
from diagrams.azure.analytics import EventHubs
from diagrams.azure.integration import APIManagement
from diagrams.onprem.compute import Server
from diagrams.onprem.container import Docker
from diagrams.onprem.queue import Kafka
from diagrams.generic.storage import Storage
from diagrams.programming.framework import React
import os

# Output path
output_dir = "/workspaces/sov-cloud-brain-trek/docs/assets/images/level-300"
os.makedirs(output_dir, exist_ok=True)

graph_attr = {
    "fontsize": "11",
    "bgcolor": "white",
    "pad": "0.3",
    "splines": "spline",
    "nodesep": "0.5",
    "ranksep": "0.7",
    "compound": "true"
}

with Diagram(
    "Production Edge RAG Architecture",
    filename=f"{output_dir}/edge-rag-production",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    outformat="svg"
):

    # Client Layer
    with Cluster("Client Applications", graph_attr={"bgcolor": "#F5F5F5"}):
        clients = [React("Web App"), React("Mobile"), React("API Client")]

    # Gateway Layer
    apim = APIManagement("API Gateway\n(Rate Limiting)")

    # Azure Local Edge Infrastructure
    with Cluster("Azure Local Edge Infrastructure", graph_attr={"bgcolor": "#E6F3FF", "style": "rounded,bold"}):

        lb = LoadBalancers("Load Balancer\n(HA Proxy)")

        # RAG Processing Cluster
        with Cluster("RAG Processing Cluster (AKS-HCI)", graph_attr={"bgcolor": "#CCE5FF"}):

            # Inference Layer
            with Cluster("LLM Inference (GPU Nodes)"):
                llm_pods = [
                    ContainerInstances("Phi-3\nPrimary"),
                    ContainerInstances("Phi-3\nReplica"),
                    ContainerInstances("Mistral\n(Fallback)")
                ]

            # Embedding Layer
            with Cluster("Embedding Service"):
                embed_pods = [
                    Docker("E5-Large\n#1"),
                    Docker("E5-Large\n#2")
                ]

            # Retrieval Layer
            with Cluster("Vector Store (HA)"):
                vector_primary = Storage("Qdrant\nPrimary")
                vector_replica = Storage("Qdrant\nReplica")

        # Data Layer
        with Cluster("Data Tier", graph_attr={"bgcolor": "#E6FFE6"}):
            doc_store = Storage("Document\nStorage")
            cache = Kafka("Redis Cache\n(Sessions)")
            queue = Kafka("Message Queue")

        # Security
        vault = KeyVaults("Local Vault\n(Keys/Secrets)")

    # Monitoring (Azure)
    with Cluster("Azure Monitoring", graph_attr={"bgcolor": "#FFF3E6"}):
        events = EventHubs("Event Hub")
        logs = MachineLearningServiceWorkspaces("Log Analytics")

    # Flows
    for client in clients:
        client >> apim

    apim >> lb
    lb >> llm_pods[0]
    lb >> llm_pods[1]

    # RAG flow
    llm_pods[0] >> Edge(label="query", style="dashed") >> embed_pods[0]
    embed_pods[0] >> Edge(label="vector search") >> vector_primary
    vector_primary >> Edge(label="sync", color="green") >> vector_replica
    vector_primary >> Edge(label="docs") >> doc_store

    # Cache flow
    llm_pods[0] >> cache

    # Security
    llm_pods[0] >> Edge(style="dotted", color="red") >> vault

    # Monitoring
    llm_pods[0] >> Edge(style="dotted", color="orange") >> events
    events >> logs

print(f"✅ Generated: {output_dir}/edge-rag-production.svg")
