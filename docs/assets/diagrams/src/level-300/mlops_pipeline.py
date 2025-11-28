#!/usr/bin/env python3
"""
MLOps Pipeline for Edge RAG
L300-64: Complete MLOps workflow for model management
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.azure.devops import Repos, Pipelines
from diagrams.azure.ml import MachineLearningServiceWorkspaces
from diagrams.azure.storage import BlobStorage
from diagrams.azure.compute import KubernetesServices
from diagrams.onprem.container import Docker
from diagrams.onprem.ci import GitlabCI
from diagrams.onprem.vcs import Git
from diagrams.onprem.monitoring import Prometheus, Grafana
from diagrams.generic.storage import Storage
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
    "MLOps Pipeline for Edge RAG",
    filename=f"{output_dir}/mlops-pipeline",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    outformat="svg"
):

    # Source Control
    with Cluster("Version Control", graph_attr={"bgcolor": "#F5F5F5", "style": "rounded"}):
        git = Git("Model Code\n& Config")
        data_version = Storage("Data Version\n(DVC)")

    # CI/CD Pipeline
    with Cluster("CI/CD Pipeline", graph_attr={"bgcolor": "#E8F4FD", "style": "rounded"}):
        pipeline = Pipelines("Build\nPipeline")
        test = GitlabCI("Model\nValidation")
        registry = Docker("Model\nRegistry")

    # Model Training (Cloud or Local)
    with Cluster("Model Training", graph_attr={"bgcolor": "#FFF4E6", "style": "rounded"}):
        train = MachineLearningServiceWorkspaces("Fine-Tuning\nPhi-3 / Mistral")
        eval_stage = MachineLearningServiceWorkspaces("Evaluation\n& Benchmarks")
        artifacts = BlobStorage("Model\nArtifacts")

    # Model Serving (Edge)
    with Cluster("Edge Deployment (AKS-HCI)", graph_attr={"bgcolor": "#D4E9D7", "style": "rounded"}):
        k8s = KubernetesServices("Kubernetes")

        with Cluster("Canary Deployment"):
            prod = Docker("Production\n(90%)")
            canary = Docker("Canary\n(10%)")

        with Cluster("Model Serving"):
            llm_svc = Docker("LLM\nService")
            embed_svc = Docker("Embedding\nService")

    # Monitoring & Feedback
    with Cluster("Monitoring & Feedback", graph_attr={"bgcolor": "#F3E8FF", "style": "rounded"}):
        prom = Prometheus("Metrics")
        grafana = Grafana("Dashboards")
        feedback = Storage("User\nFeedback")

    # Data Pipeline
    with Cluster("Data Pipeline", graph_attr={"bgcolor": "#FFE6E6", "style": "rounded"}):
        new_data = Storage("New\nDocuments")
        preprocess = Docker("Preprocessing")
        vectorize = Docker("Vectorization")

    # Flow: Development
    git >> pipeline
    data_version >> pipeline
    pipeline >> test
    test >> registry

    # Flow: Training
    registry >> train
    train >> eval_stage
    eval_stage >> artifacts

    # Flow: Deployment
    artifacts >> Edge(label="Deploy", color="green") >> k8s
    k8s >> prod
    k8s >> canary
    prod >> llm_svc
    canary >> llm_svc
    prod >> embed_svc

    # Flow: Monitoring
    llm_svc >> Edge(style="dotted") >> prom
    embed_svc >> Edge(style="dotted") >> prom
    prom >> grafana

    # Feedback loop
    llm_svc >> Edge(label="Logs", style="dashed") >> feedback
    feedback >> Edge(label="Retrain", color="orange", style="dashed") >> data_version

    # Data pipeline
    new_data >> preprocess
    preprocess >> vectorize
    vectorize >> embed_svc

print(f"✅ Generated: {output_dir}/mlops-pipeline.svg")
