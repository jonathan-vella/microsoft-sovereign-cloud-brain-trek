#!/usr/bin/env python3
"""Phase 3 — Bulk-add `description` to front-matter from a manifest.

Reads a manifest dict {path: description}, finds each file's frontmatter,
and inserts the description if missing. Skips files where description
already exists (idempotent). Verifies that a `---\n` close delimiter
is present and that the description doesn't already exist inside the
front-matter block.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

DOCS = Path("docs")

# Phase 3 description manifest.  Add entries here as Phase 3 progresses.
DESCRIPTIONS: dict[str, str] = {
    # === L200 Module overviews ===
    "level-200/module-01-azure-local.md": (
        "Module 1: Azure Local deep-dive — architecture-deep-dive, advanced "
        "networking, hardware planning, and HA patterns for production "
        "deployments."
    ),
    "level-200/module-02-arc.md": (
        "Module 2: Azure Arc advanced management — multi-cluster patterns, "
        "GitOps at scale, policy and governance, cost optimization, and "
        "enterprise deployment patterns."
    ),
    "level-200/module-03-edge-rag.md": (
        "Module 3: Edge RAG (preview) implementation — vector databases on "
        "the edge, deployment strategies, LLM inference optimization, and "
        "operations / monitoring."
    ),
    "level-200/module-04-presales.md": (
        "Module 4: Pre-sales and solution design — customer discovery, "
        "solution sizing, cost estimation / TCO, and presales solution "
        "design patterns for sovereign cloud opportunities."
    ),
    "level-200/module-05-compliance.md": (
        "Module 5: Compliance and security implementation — GDPR, FedRAMP, "
        "encryption key management, security hardening, and compliance / "
        "security patterns."
    ),
    "level-200/labs-overview.md": (
        "Module 6: Hands-on labs overview — five validated lab exercises "
        "covering Azure Local deployment, Arc onboarding, Edge RAG setup, "
        "policy governance, and monitoring."
    ),
    # === L200 Arc Advanced Management ===
    "level-200/arc-advanced-management.md": (
        "Arc advanced management — multi-cluster operations, custom "
        "locations, Arc Resource Bridge, and integrating Arc with VMware "
        "vSphere / SCVMM / Azure Local."
    ),
    "level-200/arc-policy-and-governance.md": (
        "Azure Policy and governance for Arc-enabled resources — policy "
        "authoring, Initiative scope, audit-then-enforce rollout patterns, "
        "and compliance reporting."
    ),
    "level-200/arc-cost-optimization.md": (
        "Arc cost optimization — RBAC and tagging strategies, billing "
        "patterns for Arc-enabled services, and reducing operational "
        "overhead at scale."
    ),
    "level-200/arc-enterprise-patterns.md": (
        "Enterprise Arc deployment patterns — landing-zone alignment, "
        "multi-subscription topology, identity integration, and rollout "
        "patterns for thousands of Arc-enabled resources."
    ),
    "level-200/arc-advanced-knowledge-check.md": (
        "Knowledge check covering advanced Azure Arc management — multi-"
        "cluster GitOps, custom locations, Arc-enabled SQL Server, and "
        "enterprise-scale governance patterns."
    ),
    # === L200 Azure Local deep dive ===
    "level-200/azure-local-architecture-deep-dive.md": (
        "Azure Local architecture deep dive — Cluster Aware Updating, "
        "Storage Spaces Direct internals, RDMA networking, and Hyper-V "
        "virtualization details for production planning."
    ),
    "level-200/azure-local-advanced-networking.md": (
        "Azure Local advanced networking — SDN, Network Controller, "
        "Software Load Balancer, multi-site topologies, and integration "
        "with Azure ExpressRoute and Network Adapters."
    ),
    "level-200/azure-local-ha-patterns.md": (
        "Azure Local high-availability patterns — fault domains, witness "
        "configurations, stretched clusters, and disaster-recovery "
        "options including Azure Site Recovery."
    ),
    "level-200/azure-local-hardware-planning.md": (
        "Azure Local hardware planning — workload-driven sizing, validated "
        "hardware tiers, network and storage minimums, and worked examples "
        "for common deployment sizes."
    ),
    "level-200/azure-local-deep-dive-knowledge-check.md": (
        "Knowledge check covering Azure Local deep-dive concepts — "
        "architecture internals, HA patterns, hardware planning, and "
        "advanced networking."
    ),
    # === L200 Edge RAG implementation ===
    "level-200/edge-rag-implementation.md": (
        "Edge RAG (preview) implementation overview — deployment topology, "
        "Azure Arc-enabled Kubernetes prerequisites, and end-to-end RAG "
        "pipeline configuration."
    ),
    "level-200/vector-databases-edge.md": (
        "Vector databases on the edge — Weaviate, Qdrant, and pgvector "
        "deployed on Azure Arc-enabled Kubernetes; sizing, persistence, "
        "and backup considerations for sovereign deployments."
    ),
    "level-200/rag-implementation-knowledge-check.md": (
        "Knowledge check covering Edge RAG (preview) implementation — "
        "deployment strategies, vector databases, LLM inference "
        "optimization, and operations / monitoring."
    ),
    # === L200 Pre-sales ===
    "level-200/solution-sizing.md": (
        "Solution sizing for sovereign cloud opportunities — workload "
        "intake, capacity calculators for Azure Local, and translation "
        "from customer requirements to validated hardware SKUs."
    ),
    "level-200/presales-knowledge-check.md": (
        "Knowledge check covering pre-sales and solution design — "
        "customer discovery, sizing, cost estimation, and proposal "
        "patterns for sovereign cloud opportunities."
    ),
    # === L200 Compliance & security ===
    "level-200/gdpr-implementation.md": (
        "GDPR implementation patterns for sovereign cloud — controller / "
        "processor responsibilities, data subject rights workflows, and "
        "Azure features that support GDPR compliance."
    ),
    "level-200/fedramp-compliance.md": (
        "FedRAMP compliance patterns for sovereign cloud — Azure "
        "Government boundaries, FedRAMP Moderate vs High, and how Azure "
        "Local fits into FedRAMP authorization scope."
    ),
    "level-200/encryption-key-management.md": (
        "Encryption and key management — customer-managed keys, Azure "
        "Key Vault Managed HSM, BYOK / HYOK patterns, and key-rotation "
        "automation for sovereign workloads."
    ),
    "level-200/security-hardening.md": (
        "Security hardening for Azure Local and Arc-enabled resources — "
        "Defender for Cloud, Microsoft Sentinel integration, OS-level "
        "baselines, and reducing attack surface."
    ),
    "level-200/compliance-security-patterns.md": (
        "Compliance and security architecture patterns — segmentation, "
        "audit logging, key management, and policy as code patterns "
        "applied across sovereign deployments."
    ),
    "level-200/compliance-knowledge-check.md": (
        "Knowledge check covering compliance and security implementation "
        "— GDPR, FedRAMP, encryption / key management, and security "
        "hardening."
    ),
    # === L200 Labs ===
    "level-200/lab-01-azure-local-deployment.md": (
        "Lab 1: Azure Local connected-mode deployment — networking, "
        "storage, sample workload, and validating the cluster against "
        "Azure Arc."
    ),
    "level-200/lab-02-azure-arc-onboarding.md": (
        "Lab 2: Azure Arc onboarding — connecting servers and Kubernetes "
        "clusters to Arc, applying Azure Policy, and validating the "
        "control plane."
    ),
    "level-200/lab-03-edge-rag-setup.md": (
        "Lab 3: Edge RAG (preview) setup — deploying vector database, "
        "ingestion pipeline, and LLM inference components on Azure Arc-"
        "enabled Kubernetes."
    ),
    "level-200/lab-04-policy-governance.md": (
        "Lab 4: Policy and governance — authoring custom Azure Policy "
        "definitions, applying initiatives across Arc-enabled scope, "
        "and validating compliance reporting."
    ),
    "level-200/lab-05-monitoring-observability.md": (
        "Lab 5: Monitoring and observability — Azure Monitor for "
        "containers, Container Insights for Arc-enabled Kubernetes, "
        "and Defender for Cloud alerting."
    ),
    # === L200 Internal ===
    "level-200/VISUAL_SPECIFICATIONS.md": (
        "Internal Level 200 visual asset specifications (excluded from nav)."
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
        return False  # already has description
    # Insert before the closing ---
    new_fm_body = fm_body + f'\ndescription: "{description}"'
    new_text = m.group(1) + new_fm_body + m.group(3) + text[m.end():]
    path.write_text(new_text, encoding="utf-8")
    print(f"FIXED {path.relative_to(DOCS)}")
    return True


def main() -> int:
    if not DOCS.exists():
        print("docs/ not found", file=sys.stderr)
        return 2
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
