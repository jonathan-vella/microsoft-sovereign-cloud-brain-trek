---
title: "Visual Assets Index"
description: "Complete index of Brain Trek visual assets with regeneration instructions"
lastVerified: 2026-10-02
sidebar:
  order: 3
---

Complete catalog of 53 Python-generated SVG diagrams organized by learning level, with descriptions and regeneration instructions.

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

## Level 50: Foundational (21 diagrams)

### Cloud Computing Concepts

| Diagram | Description | Used In |
|---------|-------------|---------|
| [cloud-computing-mindmap.svg](/images/level-50/cloud-computing-mindmap.svg) | Cloud computing essential characteristics mindmap | [Cloud computing primer](/level-50/module-01-cloud-computing/cloud-computing-primer/) |
| [traditional-vs-cloud.svg](/images/level-50/traditional-vs-cloud.svg) | Traditional IT vs cloud infrastructure comparison | [Cloud computing primer](/level-50/module-01-cloud-computing/cloud-computing-primer/) |
| [cloud-tco-comparison.svg](/images/level-50/cloud-tco-comparison.svg) | CapEx vs OpEx total cost of ownership | [Cloud computing primer](/level-50/module-01-cloud-computing/cloud-computing-primer/) |
| [cloud-scalability-patterns.svg](/images/level-50/cloud-scalability-patterns.svg) | Horizontal vs vertical scaling patterns | [Cloud computing primer](/level-50/module-01-cloud-computing/cloud-computing-primer/) |

### Service & Deployment Models

| Diagram | Description | Used In |
|---------|-------------|---------|
| [shared-responsibility-matrix.svg](/images/level-50/shared-responsibility-matrix.svg) | IaaS/PaaS/SaaS responsibility matrix | [Cloud service models](/level-50/module-01-cloud-computing/cloud-service-models/) |
| [shared-responsibility-shift.svg](/images/level-50/shared-responsibility-shift.svg) | Responsibility shift across service models | [Cloud service models](/level-50/module-01-cloud-computing/cloud-service-models/) |
| [cloud-deployment-models.svg](/images/level-50/cloud-deployment-models.svg) | Public/private/hybrid deployment comparison | [Cloud deployment models](/level-50/module-01-cloud-computing/cloud-deployment-models/) |
| [cloud-deployment-models-overview.svg](/images/level-50/cloud-deployment-models-overview.svg) | Deployment model decision tree | [Cloud deployment models](/level-50/module-01-cloud-computing/cloud-deployment-models/) |
| [hypervisor-types.svg](/images/level-50/hypervisor-types.svg) | Type 1 vs Type 2 hypervisors | [Cloud computing primer](/level-50/module-01-cloud-computing/cloud-computing-primer/) |

### Security & Compliance

| Diagram | Description | Used In |
|---------|-------------|---------|
| [cia-triad.svg](/images/level-50/cia-triad.svg) | Confidentiality, Integrity, Availability triangle | [Security compliance basics](/level-50/module-02-security-compliance/security-compliance-basics/) |
| [defense-in-depth.svg](/images/level-50/defense-in-depth.svg) | Multi-layer security model | [Security compliance basics](/level-50/module-02-security-compliance/security-compliance-basics/) |
| [authentication-authorization-flow.svg](/images/level-50/authentication-authorization-flow.svg) | AuthN vs AuthZ flow comparison | [Security compliance basics](/level-50/module-02-security-compliance/security-compliance-basics/) |
| [data-classification-pyramid.svg](/images/level-50/data-classification-pyramid.svg) | Data sensitivity classification levels | [Security compliance basics](/level-50/module-02-security-compliance/security-compliance-basics/) |
| [compliance-frameworks-comparison.svg](/images/level-50/compliance-frameworks-comparison.svg) | GDPR, HIPAA, FedRAMP comparison | [Compliance frameworks](/level-50/module-02-security-compliance/compliance-frameworks/) |

### Azure Fundamentals

| Diagram | Description | Used In |
|---------|-------------|---------|
| [azure-infrastructure-hierarchy.svg](/images/level-50/azure-infrastructure-hierarchy.svg) | Regions, zones, datacenters hierarchy | [Azure global infrastructure](/level-50/module-03-azure-intro/azure-global-infrastructure/) |
| [azure-service-categories.svg](/images/level-50/azure-service-categories.svg) | Azure service taxonomy | [Azure service categories](/level-50/module-03-azure-intro/azure-service-categories/) |
| [azure-compute-options.svg](/images/level-50/azure-compute-options.svg) | VMs, containers, serverless comparison | [Azure service categories](/level-50/module-03-azure-intro/azure-service-categories/) |
| [azure-storage-tiers.svg](/images/level-50/azure-storage-tiers.svg) | Hot, cool, archive storage tiers | [Azure service categories](/level-50/module-03-azure-intro/azure-service-categories/) |
| [azure-networking-fundamentals.svg](/images/level-50/azure-networking-fundamentals.svg) | VNet, subnet, NSG basics | [Azure service categories](/level-50/module-03-azure-intro/azure-service-categories/) |

---

## Level 100: Foundational sovereignty (9 diagrams)

### Sovereignty Concepts

| Diagram | Description | Used In |
|---------|-------------|---------|
| [azure-regions-map.svg](/images/level-100/azure-regions-map.svg) | Global Azure region distribution | [Azure global infrastructure](/level-50/module-03-azure-intro/azure-global-infrastructure/) |
| [regulatory-timeline.svg](/images/level-100/regulatory-timeline.svg) | Key regulatory framework timeline | [Compliance frameworks](/level-50/module-02-security-compliance/compliance-frameworks/) |
| [eu-data-boundary.svg](/images/level-100/eu-data-boundary.svg) | EU Data Boundary scope | [European commitments](/level-100/module-01-digital-sovereignty/european-commitments/) |
| [sovereign-cloud-models-comparison.svg](/images/level-100/sovereign-cloud-models-comparison.svg) | Sovereign cloud model comparison matrix | [Sovereign cloud models](/level-100/module-02-cloud-models/sovereign-cloud-models/) |
| [data-classification-pyramid.svg](/images/level-100/data-classification-pyramid.svg) | Sovereignty-focused data classification | [Data residency concepts](/level-100/module-01-digital-sovereignty/data-residency-concepts/) |

### Azure Local

| Diagram | Description | Used In |
|---------|-------------|---------|
| [azure-local-architecture.svg](/images/level-100/azure-local-architecture.svg) | Azure Local cluster architecture overview | [Azure Local overview](/level-100/module-03-azure-local/azure-local-overview/) |
| [capex-opex-comparison.svg](/images/level-100/capex-opex-comparison.svg) | Azure Local economics comparison | [Cloud computing primer](/level-50/module-01-cloud-computing/cloud-computing-primer/) |

### Edge AI

| Diagram | Description | Used In |
|---------|-------------|---------|
| [vector-embedding-process.svg](/images/level-100/vector-embedding-process.svg) | RAG vector embedding workflow | [RAG fundamentals](/level-100/module-05-edge-rag/rag-fundamentals/) |
| [nist-cloud-characteristics.svg](/images/level-100/nist-cloud-characteristics.svg) | NIST cloud characteristics | [Cloud computing primer](/level-50/module-01-cloud-computing/cloud-computing-primer/) |

---

## Level 200: Intermediate (7 diagrams)

### Azure Local Deep Dive

| Diagram | Description | Used In |
|---------|-------------|---------|
| [storage-spaces-direct.svg](/images/level-200/storage-spaces-direct.svg) | S2D architecture and data flow | [Azure Local architecture deep dive](/level-200/module-01-azure-local/azure-local-architecture-deep-dive/) |
| [sdn-architecture.svg](/images/level-200/sdn-architecture.svg) | Software-defined networking stack | [Azure Local advanced networking](/level-200/azure-local-advanced-networking/) |

### Azure Arc

| Diagram | Description | Used In |
|---------|-------------|---------|
| [enterprise-arc-topology.svg](/images/level-200/enterprise-arc-topology.svg) | Enterprise Arc deployment patterns | [Arc enterprise patterns](/level-200/arc-enterprise-patterns/) |

### Edge RAG

| Diagram | Description | Used In |
|---------|-------------|---------|
| [edge-rag-implementation.svg](/images/level-200/edge-rag-implementation.svg) | RAG implementation architecture | [Edge RAG implementation](/level-200/edge-rag-implementation/) |

### Compliance & Security

| Diagram | Description | Used In |
|---------|-------------|---------|
| [security-patterns-matrix.svg](/images/level-200/security-patterns-matrix.svg) | Security pattern decision matrix | [Compliance security patterns](/level-200/compliance-security-patterns/) |
| [encryption-key-hierarchy.svg](/images/level-200/encryption-key-hierarchy.svg) | Key management hierarchy | [Encryption key management](/level-200/encryption-key-management/) |
| [fedramp-control-families.svg](/images/level-200/fedramp-control-families.svg) | FedRAMP control family overview | [FedRAMP compliance](/level-200/fedramp-compliance/) |

---

## Level 300: Advanced (16 diagrams)

### Zero Trust

| Diagram | Description | Used In |
|---------|-------------|---------|
| [zero-trust-architecture.svg](/images/level-300/zero-trust-architecture.svg) | Complete Zero Trust implementation | [Zero Trust](/level-300/module-05-zero-trust/) |
| [security-monitoring-flow.svg](/images/level-300/security-monitoring-flow.svg) | Security monitoring and alerting | [Zero Trust monitoring](/level-300/module-05-zero-trust/zero-trust-monitoring/) |
| [hybrid-identity.svg](/images/level-300/hybrid-identity.svg) | Hybrid identity architecture | [Zero Trust](/level-300/module-05-zero-trust/) |

### Azure Local at Scale

| Diagram | Description | Used In |
|---------|-------------|---------|
| [azure-local-multisite.svg](/images/level-300/azure-local-multisite.svg) | Multi-site deployment topology | [Azure Local multi-site](/level-300/module-01-azure-local-advanced/azure-local-multi-site/) |
| [air-gapped-architecture.svg](/images/level-300/air-gapped-architecture.svg) | Air-gapped environment design | [Azure Local disconnected operations](/level-300/module-01-azure-local-advanced/azure-local-disconnected-operations/) |
| [disaster-recovery-topology.svg](/images/level-300/disaster-recovery-topology.svg) | DR site configuration | [Disaster recovery](/level-300/module-03-architecture-patterns/disaster-recovery/) |
| [multi-region-sovereign.svg](/images/level-300/multi-region-sovereign.svg) | Multi-region sovereign architecture | [SLZ architecture](/level-300/module-02-sovereign-landing-zone/slz-architecture/) |

### Production Edge RAG

| Diagram | Description | Used In |
|---------|-------------|---------|
| [edge-rag-production.svg](/images/level-300/edge-rag-production.svg) | Production RAG deployment | [Foundry Local in production](/level-300/module-04-foundry-local-production/) |
| [mlops-pipeline.svg](/images/level-300/mlops-pipeline.svg) | MLOps continuous improvement | [Model lifecycle](/level-300/module-04-foundry-local-production/model-lifecycle/) |

### Industry Verticals

| Diagram | Description | Used In |
|---------|-------------|---------|
| [healthcare-sovereign.svg](/images/level-300/healthcare-sovereign.svg) | Healthcare sovereignty patterns | [Healthcare sovereign](/level-300/module-07-industry-solutions/healthcare-sovereign/) |
| [financial-services.svg](/images/level-300/financial-services.svg) | Financial services architecture | [Financial services](/level-300/module-07-industry-solutions/financial-services/) |
| [government-cloud.svg](/images/level-300/government-cloud.svg) | Government cloud design | [Government cloud](/level-300/module-07-industry-solutions/government-cloud/) |
| [critical-infrastructure.svg](/images/level-300/critical-infrastructure.svg) | Critical infrastructure patterns | [Critical infrastructure](/level-300/module-07-industry-solutions/critical-infrastructure/) |

### Architecture Patterns

| Diagram | Description | Used In |
|---------|-------------|---------|
| [sovereign-landing-zone.svg](/images/level-300/sovereign-landing-zone.svg) | Sovereign Landing Zone structure | [SLZ architecture](/level-300/module-02-sovereign-landing-zone/slz-architecture/) |
| [api-gateway-patterns.svg](/images/level-300/api-gateway-patterns.svg) | API gateway architectures | [API gateway patterns](/level-300/module-03-architecture-patterns/api-gateway-patterns/) |
| [event-driven-architecture.svg](/images/level-300/event-driven-architecture.svg) | Event-driven patterns | [Event-driven architecture](/level-300/module-03-architecture-patterns/event-driven-architecture/) |
| [data-mesh-sovereignty.svg](/images/level-300/data-mesh-sovereignty.svg) | Data mesh with sovereignty | [Data mesh sovereignty](/level-300/module-03-architecture-patterns/data-mesh-sovereignty/) |
| [observability-stack.svg](/images/level-300/observability-stack.svg) | Observability architecture | [Observability stack](/level-300/module-06-operations/observability-stack/) |

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

## Sources

- [Azure Architecture Icons](https://learn.microsoft.com/azure/architecture/icons/)
