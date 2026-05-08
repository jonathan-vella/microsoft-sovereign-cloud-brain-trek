#!/usr/bin/env python3
"""Phase 3.4 — L300 description manifest. Same shape as add_descriptions.py."""
from __future__ import annotations

import re
import sys
from pathlib import Path

DOCS = Path("docs")

DESCRIPTIONS: dict[str, str] = {
    # === L300 Module 1: Zero Trust ===
    "level-300/zero-trust.md": (
        "Module 1: Zero Trust security for sovereign cloud — Zero Trust "
        "principles applied to Azure Local, Arc, and Edge RAG; identity, "
        "device, network, and data pillars."
    ),
    "level-300/zero-trust-architecture.md": (
        "Zero Trust architecture for sovereign cloud — segmentation "
        "patterns, identity perimeters, conditional access, and "
        "verification mechanisms across Azure Arc-enabled resources."
    ),
    "level-300/zero-trust-monitoring.md": (
        "Zero Trust monitoring — telemetry collection, Microsoft Sentinel "
        "queries, GDPR-aware logging, and continuous verification across "
        "Arc-enabled estate."
    ),
    "level-300/zero-trust-lab.md": (
        "Lab: Zero Trust security controls — implement Conditional Access, "
        "device compliance, risk-based policies, and audit logging in a "
        "sovereign Azure environment."
    ),
    "level-300/zero-trust-troubleshooting-knowledge-check.md": (
        "Knowledge check covering Zero Trust troubleshooting — common "
        "Conditional Access issues, audit-log analysis, and incident "
        "response patterns."
    ),
    # === L300 Module 2: Azure Local at scale (connected) ===
    "level-300/azure-local-advanced-connected.md": (
        "Module 2: Azure Local at scale (connected mode) — multi-site "
        "topologies, advanced storage and network optimizations, update "
        "ring strategies, and capacity planning at enterprise scale."
    ),
    "level-300/azure-local-multi-site.md": (
        "Azure Local multi-site deployments — stretched clusters, Site "
        "Recovery, fault domains across data centers, and quorum "
        "configurations for geo-resilient sovereign infrastructure."
    ),
    "level-300/azure-local-networking-advanced.md": (
        "Azure Local advanced networking — SDN deep-dive, Network "
        "Controller, multi-path RDMA, segmentation patterns, and "
        "troubleshooting connectivity at scale."
    ),
    "level-300/azure-local-certificate-management.md": (
        "Azure Local certificate management — PKI integration, automated "
        "rotation, and certificate strategies for control-plane and data-"
        "plane communications."
    ),
    "level-300/azure-local-connected-lab.md": (
        "Lab: Azure Local connected-mode multi-site deployment — set up a "
        "stretched cluster, configure replication, and validate failover "
        "scenarios."
    ),
    # === L300 Module 3: Azure Local disconnected / air-gapped ===
    "level-300/azure-local-advanced-disconnected.md": (
        "Module 3: Azure Local in disconnected mode — offline registration, "
        "local control plane, periodic sync, and operational patterns for "
        "air-gapped sovereign deployments."
    ),
    "level-300/azure-local-air-gapped.md": (
        "Air-gapped Azure Local deployments — fully isolated environments, "
        "physical and logical air-gap patterns, and compliance with "
        "stringent sovereignty requirements."
    ),
    "level-300/azure-local-disconnected-lab.md": (
        "Lab: Azure Local disconnected-mode deployment — provision, "
        "register, and operate a cluster without continuous Azure "
        "connectivity."
    ),
    "level-300/azure-local-advanced-knowledge-check.md": (
        "Knowledge check covering advanced Azure Local — multi-site "
        "deployments, networking deep-dive, certificate management, and "
        "disconnected operations."
    ),
    # === L300 Module 4: Production Edge RAG ===
    "level-300/edge-rag-production.md": (
        "Module 4: Production Edge RAG (preview) — moving from pilot to "
        "production, MLOps, optimization, and operations for on-premises "
        "RAG systems."
    ),
    "level-300/edge-rag-architecture-production.md": (
        "Production Edge RAG (preview) architecture — multi-model serving, "
        "high-availability vector stores, ingestion at scale, and "
        "integration with enterprise data governance."
    ),
    "level-300/edge-rag-optimization.md": (
        "Edge RAG (preview) optimization — retrieval quality tuning, model "
        "quantization, hardware acceleration, and latency / throughput "
        "trade-offs."
    ),
    "level-300/edge-rag-mlops.md": (
        "Edge RAG (preview) MLOps — model lifecycle on Arc-enabled "
        "Kubernetes, CI/CD for prompts and embeddings, evaluation "
        "harnesses, and rollback patterns."
    ),
    "level-300/edge-rag-production-lab.md": (
        "Lab: Production Edge RAG (preview) deployment — set up a multi-"
        "tenant RAG service with high availability, observability, and "
        "compliance controls."
    ),
    "level-300/edge-rag-production-knowledge-check.md": (
        "Knowledge check covering production Edge RAG (preview) — "
        "architecture, optimization, MLOps, and operational patterns."
    ),
    # === L300 Module 5: Troubleshooting ===
    "level-300/troubleshooting.md": (
        "Module 5: Troubleshooting sovereign cloud deployments — diagnostic "
        "tools, common issues, and escalation patterns for Azure Local, "
        "Arc, and Edge RAG."
    ),
    "level-300/troubleshooting-common-issues.md": (
        "Common troubleshooting scenarios — agent connectivity, policy "
        "evaluation, certificate expiry, and storage performance issues "
        "in Azure Local + Arc deployments."
    ),
    "level-300/troubleshooting-tools.md": (
        "Troubleshooting tools and telemetry — log collection, Azure "
        "Monitor queries, Network Watcher, and partner support tooling "
        "for sovereign deployments."
    ),
    "level-300/troubleshooting-escalation.md": (
        "Escalation patterns and Microsoft support engagement — preparing "
        "support requests, Customer Lockbox workflow, and escalation "
        "paths for production sovereign incidents."
    ),
    # === L300 Internal ===
    "level-300/VISUAL_SPECIFICATIONS.md": (
        "Internal Level 300 visual asset specifications (excluded from nav)."
    ),
}

FRONTMATTER_RE = re.compile(r"^(---\s*\n)(.*?)(\n---\s*\n)", re.DOTALL)


def add_description(path: Path, description: str) -> bool:
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        print(f"SKIP (no frontmatter): {path}")
        return False
    fm_body = m.group(2)
    if re.search(r"^\s*description\s*:", fm_body, re.MULTILINE):
        return False
    new_fm_body = fm_body + f'\ndescription: "{description}"'
    new_text = m.group(1) + new_fm_body + m.group(3) + text[m.end():]
    path.write_text(new_text, encoding="utf-8")
    print(f"FIXED {path.relative_to(DOCS)}")
    return True


def main() -> int:
    fixed = 0
    skipped = 0
    for relpath, desc in DESCRIPTIONS.items():
        path = DOCS / relpath
        if not path.exists():
            print(f"MISSING: {relpath}")
            continue
        if add_description(path, desc):
            fixed += 1
        else:
            skipped += 1
    print(f"\nfixed={fixed} skipped={skipped} total_manifest={len(DESCRIPTIONS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
