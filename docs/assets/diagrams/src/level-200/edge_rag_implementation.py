#!/usr/bin/env python3
"""
Edge RAG Implementation Architecture
L200-45: Detailed implementation architecture for Edge RAG
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.azure.compute import KubernetesServices, ContainerInstances
from diagrams.azure.storage import BlobStorage
from diagrams.azure.database import CosmosDb
from diagrams.azure.network import LoadBalancers
from diagrams.azure.security import KeyVaults
from diagrams.azure.ml import MachineLearningServiceWorkspaces
from diagrams.onprem.compute import Server
from diagrams.onprem.container import Docker
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.queue import Kafka
from diagrams.generic.storage import Storage
from diagrams.programming.framework import React
import os

# Output path
output_dir = "/workspaces/sov-cloud-brain-trek/docs/assets/images/level-200"
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
    "Edge RAG Implementation Architecture",
    filename=f"{output_dir}/edge-rag-implementation",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    outformat="svg"
):

    # User Interface Layer
    with Cluster("Client Layer", graph_attr={"bgcolor": "#F5F5F5", "style": "rounded"}):
        ui = React("Web UI")
        api_client = React("API Client")

    # API Gateway
    lb = LoadBalancers("API Gateway\n(Kong/NGINX)")

    # Application Layer
    with Cluster("Application Services (AKS-HCI)", graph_attr={"bgcolor": "#E8F4FD", "style": "rounded"}):

        with Cluster("Query Pipeline"):
            query_svc = Docker("Query\nService")
            reranker = Docker("Reranker\nService")
            cache = Kafka("Redis\nCache")

        with Cluster("Ingestion Pipeline"):
            ingest = Docker("Document\nLoader")
            chunker = Docker("Text\nChunker")
            embedder = Docker("Embedding\nService")

    # AI/ML Layer
    with Cluster("AI/ML Layer (GPU Nodes)", graph_attr={"bgcolor": "#FFF4E6", "style": "rounded"}):
        llm = MachineLearningServiceWorkspaces("LLM\nPhi-3 / Mistral")
        embed_model = MachineLearningServiceWorkspaces("Embedding\nE5-large")

    # Data Layer
    with Cluster("Data Layer", graph_attr={"bgcolor": "#D4E9D7", "style": "rounded"}):
        vector_db = Storage("Vector DB\n(Qdrant)")
        doc_store = BlobStorage("Document\nStore")
        metadata = PostgreSQL("Metadata\nDB")

    # Security
    vault = KeyVaults("Local\nKey Vault")

    # Monitoring
    with Cluster("Observability", graph_attr={"bgcolor": "#FFE6E6", "style": "rounded"}):
        logs = Server("Prometheus\n+ Grafana")
        traces = Server("Jaeger\nTracing")

    # Flow connections
    ui >> lb
    api_client >> lb

    lb >> query_svc
    query_svc >> cache
    query_svc >> embed_model
    embed_model >> vector_db
    vector_db >> reranker
    reranker >> llm
    llm >> query_svc

    lb >> ingest
    ingest >> chunker
    chunker >> embedder
    embedder >> embed_model
    embed_model >> vector_db
    ingest >> doc_store
    ingest >> metadata

    # Security connections
    llm >> Edge(style="dotted", color="red") >> vault
    query_svc >> Edge(style="dotted", color="red") >> vault

    # Monitoring connections
    query_svc >> Edge(style="dotted", color="gray") >> logs
    llm >> Edge(style="dotted", color="gray") >> traces

print(f"✅ Generated: {output_dir}/edge-rag-implementation.svg")
