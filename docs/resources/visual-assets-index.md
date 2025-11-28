---
layout: default
title: Visual Assets Index
nav_order: 3
parent: Resources
description: "Complete index of Brain Trek visual assets with regeneration instructions"
---

# Visual Assets Index

{: .no_toc }

Complete catalog of 53 Python-generated SVG diagrams organized by learning level, with descriptions and regeneration instructions.

## Table of Contents

{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

All visual assets in Brain Trek are generated from Python scripts using matplotlib, enabling consistent styling and easy updates. Each SVG follows the Microsoft Azure color palette for brand consistency.

### Azure Color Palette

| Color | Hex | Usage |
|-------|-----|-------|
| Azure Blue | `#0078D4` | Primary elements, headers |
| Azure Dark Blue | `#004578` | Borders, strokes |
| Azure Green | `#107C10` | Success, on-premises |
| Azure Orange | `#FF8C00` | Warnings, cautions |
| Azure Red | `#D13438` | Errors, critical items |
| Azure Light Blue | `#50E6FF` | Highlights, accents |
| Azure Gray | `#6B6B6B` | Secondary text |

---

## Regeneration Instructions

### Prerequisites

```bash
# Ensure Python dependencies are installed
pip install -r requirements.txt
```

### Regenerate All Diagrams

```bash
npm run diagrams
```

### Regenerate by Level

```bash
npm run diagrams:level50
npm run diagrams:level100
npm run diagrams:level200
npm run diagrams:level300
```

### Regenerate Single Diagram

```bash
python scripts/regenerate-diagrams.py --level 100 --name azure-local-architecture
```

---

## Level 50 — Foundational (21 diagrams)

### Cloud Computing Concepts

| Diagram | Description | Used In |
|---------|-------------|---------|
| [cloud-computing-mindmap.svg](../assets/images/level-50/cloud-computing-mindmap.svg) | Cloud computing essential characteristics mindmap | `cloud-computing-primer.md` |
| [traditional-vs-cloud.svg](../assets/images/level-50/traditional-vs-cloud.svg) | Traditional IT vs cloud infrastructure comparison | `cloud-computing-primer.md` |
| [cloud-tco-comparison.svg](../assets/images/level-50/cloud-tco-comparison.svg) | CapEx vs OpEx total cost of ownership | `cloud-computing-primer.md` |
| [cloud-scalability-patterns.svg](../assets/images/level-50/cloud-scalability-patterns.svg) | Horizontal vs vertical scaling patterns | `cloud-computing-primer.md` |

### Service & Deployment Models

| Diagram | Description | Used In |
|---------|-------------|---------|
| [shared-responsibility-matrix.svg](../assets/images/level-50/shared-responsibility-matrix.svg) | IaaS/PaaS/SaaS responsibility matrix | `cloud-service-models.md` |
| [shared-responsibility-shift.svg](../assets/images/level-50/shared-responsibility-shift.svg) | Responsibility shift across service models | `cloud-service-models.md` |
| [cloud-deployment-models.svg](../assets/images/level-50/cloud-deployment-models.svg) | Public/private/hybrid deployment comparison | `cloud-deployment-models.md` |
| [cloud-deployment-models-overview.svg](../assets/images/level-50/cloud-deployment-models-overview.svg) | Deployment model decision tree | `cloud-deployment-models.md` |
| [hypervisor-types.svg](../assets/images/level-50/hypervisor-types.svg) | Type 1 vs Type 2 hypervisors | `cloud-computing-primer.md` |

### Security & Compliance

| Diagram | Description | Used In |
|---------|-------------|---------|
| [cia-triad.svg](../assets/images/level-50/cia-triad.svg) | Confidentiality, Integrity, Availability triangle | `security-compliance-basics.md` |
| [defense-in-depth.svg](../assets/images/level-50/defense-in-depth.svg) | Multi-layer security model | `security-compliance-basics.md` |
| [authentication-authorization-flow.svg](../assets/images/level-50/authentication-authorization-flow.svg) | AuthN vs AuthZ flow comparison | `security-compliance-basics.md` |
| [data-classification-pyramid.svg](../assets/images/level-50/data-classification-pyramid.svg) | Data sensitivity classification levels | `security-compliance-basics.md` |
| [compliance-frameworks-comparison.svg](../assets/images/level-50/compliance-frameworks-comparison.svg) | GDPR, HIPAA, FedRAMP comparison | `compliance-frameworks.md` |

### Azure Fundamentals

| Diagram | Description | Used In |
|---------|-------------|---------|
| [azure-infrastructure-hierarchy.svg](../assets/images/level-50/azure-infrastructure-hierarchy.svg) | Regions, zones, datacenters hierarchy | `azure-global-infrastructure.md` |
| [azure-service-categories.svg](../assets/images/level-50/azure-service-categories.svg) | Azure service taxonomy | `azure-core-services.md` |
| [azure-compute-options.svg](../assets/images/level-50/azure-compute-options.svg) | VMs, containers, serverless comparison | `azure-core-services.md` |
| [azure-storage-tiers.svg](../assets/images/level-50/azure-storage-tiers.svg) | Hot, cool, archive storage tiers | `azure-core-services.md` |
| [azure-networking-fundamentals.svg](../assets/images/level-50/azure-networking-fundamentals.svg) | VNet, subnet, NSG basics | `azure-core-services.md` |

---

## Level 100 — Foundational Sovereignty (9 diagrams)

### Sovereignty Concepts

| Diagram | Description | Used In |
|---------|-------------|---------|
| [azure-regions-map.svg](../assets/images/level-100/azure-regions-map.svg) | Global Azure region distribution | `azure-global-infrastructure.md` |
| [regulatory-timeline.svg](../assets/images/level-100/regulatory-timeline.svg) | Key regulatory framework timeline | `compliance-frameworks.md` |
| [eu-data-boundary.svg](../assets/images/level-100/eu-data-boundary.svg) | EU Data Boundary scope | `european-commitments.md` |
| [sovereign-cloud-models-comparison.svg](../assets/images/level-100/sovereign-cloud-models-comparison.svg) | Sovereign cloud model comparison matrix | `sovereign-cloud-models.md` |
| [data-classification-pyramid.svg](../assets/images/level-100/data-classification-pyramid.svg) | Sovereignty-focused data classification | `data-residency-concepts.md` |

### Azure Local

| Diagram | Description | Used In |
|---------|-------------|---------|
| [azure-local-architecture.svg](../assets/images/level-100/azure-local-architecture.svg) | Azure Local cluster architecture overview | `azure-local-overview.md` |
| [capex-opex-comparison.svg](../assets/images/level-100/capex-opex-comparison.svg) | Azure Local economics comparison | `cloud-computing-primer.md` |

### Edge AI

| Diagram | Description | Used In |
|---------|-------------|---------|
| [vector-embedding-process.svg](../assets/images/level-100/vector-embedding-process.svg) | RAG vector embedding workflow | `rag-fundamentals.md` |
| [nist-cloud-characteristics.svg](../assets/images/level-100/nist-cloud-characteristics.svg) | NIST cloud characteristics | `cloud-computing-primer.md` |

---

## Level 200 — Intermediate (7 diagrams)

### Azure Local Deep Dive

| Diagram | Description | Used In |
|---------|-------------|---------|
| [storage-spaces-direct.svg](../assets/images/level-200/storage-spaces-direct.svg) | S2D architecture and data flow | `azure-local-architecture-deep-dive.md` |
| [sdn-architecture.svg](../assets/images/level-200/sdn-architecture.svg) | Software-defined networking stack | `azure-local-advanced-networking.md` |

### Azure Arc

| Diagram | Description | Used In |
|---------|-------------|---------|
| [enterprise-arc-topology.svg](../assets/images/level-200/enterprise-arc-topology.svg) | Enterprise Arc deployment patterns | `arc-enterprise-patterns.md` |

### Edge RAG

| Diagram | Description | Used In |
|---------|-------------|---------|
| [edge-rag-implementation.svg](../assets/images/level-200/edge-rag-implementation.svg) | RAG implementation architecture | `edge-rag-implementation.md` |

### Compliance & Security

| Diagram | Description | Used In |
|---------|-------------|---------|
| [security-patterns-matrix.svg](../assets/images/level-200/security-patterns-matrix.svg) | Security pattern decision matrix | `compliance-security-patterns.md` |
| [encryption-key-hierarchy.svg](../assets/images/level-200/encryption-key-hierarchy.svg) | Key management hierarchy | `encryption-key-management.md` |
| [fedramp-control-families.svg](../assets/images/level-200/fedramp-control-families.svg) | FedRAMP control family overview | `fedramp-compliance.md` |

---

## Level 300 — Advanced (16 diagrams)

### Zero Trust

| Diagram | Description | Used In |
|---------|-------------|---------|
| [zero-trust-architecture.svg](../assets/images/level-300/zero-trust-architecture.svg) | Complete Zero Trust implementation | `zero-trust.md` |
| [security-monitoring-flow.svg](../assets/images/level-300/security-monitoring-flow.svg) | Security monitoring and alerting | `zero-trust-monitoring.md` |
| [hybrid-identity.svg](../assets/images/level-300/hybrid-identity.svg) | Hybrid identity architecture | `zero-trust.md` |

### Azure Local at Scale

| Diagram | Description | Used In |
|---------|-------------|---------|
| [azure-local-multisite.svg](../assets/images/level-300/azure-local-multisite.svg) | Multi-site deployment topology | `azure-local-multi-site.md` |
| [air-gapped-architecture.svg](../assets/images/level-300/air-gapped-architecture.svg) | Air-gapped environment design | `azure-local-air-gapped.md` |
| [disaster-recovery-topology.svg](../assets/images/level-300/disaster-recovery-topology.svg) | DR site configuration | `disaster-recovery.md` |
| [multi-region-sovereign.svg](../assets/images/level-300/multi-region-sovereign.svg) | Multi-region sovereign architecture | `sovereign-landing-zone.md` |

### Production Edge RAG

| Diagram | Description | Used In |
|---------|-------------|---------|
| [edge-rag-production.svg](../assets/images/level-300/edge-rag-production.svg) | Production RAG deployment | `edge-rag-production.md` |
| [mlops-pipeline.svg](../assets/images/level-300/mlops-pipeline.svg) | MLOps continuous improvement | `edge-rag-mlops.md` |

### Industry Verticals

| Diagram | Description | Used In |
|---------|-------------|---------|
| [healthcare-sovereign.svg](../assets/images/level-300/healthcare-sovereign.svg) | Healthcare sovereignty patterns | `healthcare-sovereign.md` |
| [financial-services.svg](../assets/images/level-300/financial-services.svg) | Financial services architecture | `financial-services.md` |
| [government-cloud.svg](../assets/images/level-300/government-cloud.svg) | Government cloud design | `government-cloud.md` |
| [critical-infrastructure.svg](../assets/images/level-300/critical-infrastructure.svg) | Critical infrastructure patterns | `critical-infrastructure.md` |

### Architecture Patterns

| Diagram | Description | Used In |
|---------|-------------|---------|
| [sovereign-landing-zone.svg](../assets/images/level-300/sovereign-landing-zone.svg) | Sovereign Landing Zone structure | `sovereign-landing-zone.md` |
| [api-gateway-patterns.svg](../assets/images/level-300/api-gateway-patterns.svg) | API gateway architectures | `api-gateway-patterns.md` |
| [event-driven-architecture.svg](../assets/images/level-300/event-driven-architecture.svg) | Event-driven patterns | `event-driven-architecture.md` |
| [data-mesh-sovereignty.svg](../assets/images/level-300/data-mesh-sovereignty.svg) | Data mesh with sovereignty | `data-mesh-sovereignty.md` |
| [observability-stack.svg](../assets/images/level-300/observability-stack.svg) | Observability architecture | `observability-stack.md` |

---

## Python Source Scripts

All diagram sources are located in `docs/assets/diagrams/src/`:

```text
docs/assets/diagrams/src/
├── level-50/     (21 scripts)
├── level-100/    (9 scripts)
├── level-200/    (7 scripts)
└── level-300/    (16 scripts)
```

### Script Naming Convention

- Script: `{diagram-name}.py`
- Output: `docs/assets/images/level-{N}/{diagram-name}.svg`

### Common Script Structure

```python
import matplotlib.pyplot as plt

# Azure color palette
AZURE_BLUE = '#0078D4'
AZURE_DARK = '#004578'
AZURE_GREEN = '#107C10'

def create_diagram():
    fig, ax = plt.subplots(figsize=(12, 8))
    # ... diagram logic ...
    plt.savefig('output.svg', format='svg', bbox_inches='tight')

if __name__ == '__main__':
    create_diagram()
```

---

## Adding New Diagrams

1. Create Python script in appropriate `src/level-{N}/` folder
2. Follow existing naming and color conventions
3. Run regeneration: `npm run diagrams:level{N}`
4. Embed in target Markdown file
5. Update this index

---

**Last Updated:** January 2025
