---
layout: default
title: Module 6 - Hands-On Labs
parent: Level 200 - Intermediate
nav_order: 10
has_children: true
---

# Module 6: Hands-On Labs

{: .warning }
> **🚧 Labs Under Development**  
> All lab content is complete but hands-on exercises are currently being validated and refined.  
> **Expected Release:** Q1 2026  
> You can review the lab steps and prepare your environment in advance.

## Overview

This module provides practical, hands-on labs to reinforce the concepts covered in Modules 1-5. Each lab is designed to be completed in 2-4 hours and builds progressively toward a complete sovereign cloud deployment with compliance and security controls.

### Prerequisites

- Completion of Level 200 Modules 1-5
- Azure subscription (free tier acceptable for most labs)
- Familiarity with PowerShell, Azure CLI, or Azure Portal
- Basic networking knowledge (subnets, firewalls, VPNs)

### Learning Objectives

By completing all labs, you will:

- Deploy and configure Azure Local in connected mode
- Onboard hybrid infrastructure to Azure Arc
- Implement Edge RAG with vector database and LLM inference
- Enforce governance policies at scale using Azure Policy
- Configure comprehensive monitoring and alerting

### Lab Environment Architecture

```text
HANDS-ON LAB ENVIRONMENT
═════════════════════════════════════════════════════════════

Lab Progression Flow:

Lab 1: Azure Local Foundation
├─ Simulate Azure Local deployment
├─ Configure connected mode
├─ Deploy demo application
└─ Verify connectivity

    ↓ (Lab 1 resources used in Lab 2)

Lab 2: Azure Arc Governance
├─ Onboard Lab 1 resources to Arc
├─ Create multi-resource groups
├─ Implement Arc management
└─ Enable monitoring

    ↓ (Lab 2 Arc setup used in Lab 3 & 4)

Lab 3: Edge RAG Deployment
├─ Deploy vector database (Weaviate)
├─ Configure LLM inference engine
├─ Implement RAG pipeline
└─ Test end-to-end

    ↓ (Lab 1, 2, 3 enable Lab 4)

Lab 4: Policy & Governance
├─ Create custom policies
├─ Apply compliance standards
├─ Implement enforcement
└─ Generate compliance reports

    ↓ (All labs aggregated in Lab 5)

Lab 5: Monitoring & Observability
├─ Collect metrics from Labs 1-4
├─ Configure alerting rules
├─ Create dashboards
└─ Run incident simulation

FINAL ARCHITECTURE:
┌─────────────────────────────────────────────────┐
│ Azure Local (Lab 1)                             │
│ ├─ Demo application running                     │
│ ├─ Connected to Arc (Lab 2)                     │
│ └─ Running Edge RAG inference (Lab 3)           │
└─────────────────────────────────────────────────┘
                        ↓
        ┌───────────────┴────────────────┐
        │                                │
┌───────▼──────────┐      ┌──────────────▼──────────┐
│ Azure Arc (Lab 2)│      │ Azure Monitor (Lab 5)   │
│ ├─ Policy (Lab 4)│      │ ├─ Metrics              │
│ ├─ Governance    │      │ ├─ Alerts               │
│ └─ Management    │      │ └─ Dashboards           │
└──────────────────┘      └───────────────────────┘
```

### Time Estimates

| Lab | Topic | Duration | Difficulty |
|-----|-------|----------|------------|
| 1 | Azure Local Deployment | 2-3 hours | Intermediate |
| 2 | Azure Arc Onboarding | 2-3 hours | Intermediate |
| 3 | Edge RAG Setup | 3-4 hours | Advanced |
| 4 | Policy & Governance | 2-3 hours | Intermediate |
| 5 | Monitoring & Alerts | 2-3 hours | Intermediate |
| **Total** | **All Labs** | **11-16 hours** | **Mixed** |

---

## Lab Structure & Format

### Each Lab Includes

**Pre-Lab Checklist:**

- Prerequisites and required resources
- Estimated time and difficulty level
- Learning outcomes
- Resource cost estimates

**Step-by-Step Instructions:**

- Numbered steps with detailed commands
- Expected output for verification
- Screenshots and examples
- Troubleshooting tips

**Validation Steps:**

- How to verify each step succeeded
- Common errors and solutions
- Checkpoint verification

**Post-Lab Review:**

- What you accomplished
- Key learning points
- How this applies to production
- Next steps

### Labs at a Glance

```text
LAB 1: Azure Local Deployment (2-3 hours)
────────────────────────────────────────
Objective: Deploy and configure Azure Local

Topics covered:
├─ Azure Local architecture
├─ Connected mode setup
├─ Networking and connectivity
├─ Demo workload deployment
└─ Validation and testing

Skills gained:
✓ Understand Azure Local deployment model
✓ Configure network connectivity
✓ Deploy applications on Azure Local
✓ Monitor Azure Local health

Estimated cost: $0-20 (Azure credits / free tier)

LAB 2: Azure Arc Onboarding (2-3 hours)
────────────────────────────────────────
Objective: Onboard resources to Azure Arc

Topics covered:
├─ Arc agent deployment
├─ Machine onboarding
├─ Kubernetes cluster registration
├─ Arc server management
└─ Governance enablement

Skills gained:
✓ Deploy Arc agents
✓ Onboard hybrid infrastructure
✓ Use Arc for centralized management
✓ Apply policies across infrastructure

Estimated cost: $0-30 (Azure credits / free tier)

LAB 3: Edge RAG Implementation (3-4 hours)
───────────────────────────────────────────
Objective: Deploy complete Edge RAG solution

Topics covered:
├─ Vector database setup (Weaviate)
├─ Embedding model deployment
├─ LLM inference configuration
├─ RAG pipeline implementation
└─ Performance optimization

Skills gained:
✓ Deploy vector databases
✓ Configure LLM inference
✓ Implement RAG patterns
✓ Optimize inference performance

Estimated cost: $50-100 (GPU resources if using)

LAB 4: Policy & Governance (2-3 hours)
────────────────────────────────────────
Objective: Implement compliance policies

Topics covered:
├─ Azure Policy basics
├─ Custom policy definition
├─ Policy assignment and scope
├─ Compliance monitoring
└─ Remediation automation

Skills gained:
✓ Create custom policies
✓ Enforce compliance at scale
✓ Monitor policy compliance
✓ Generate compliance reports

Estimated cost: $0-10 (Policy evaluation free)

LAB 5: Monitoring & Observability (2-3 hours)
──────────────────────────────────────────────
Objective: Configure comprehensive monitoring

Topics covered:
├─ Azure Monitor setup
├─ Metrics and logging
├─ Alert configuration
├─ Dashboard creation
└─ Incident response simulation

Skills gained:
✓ Configure monitoring
✓ Create effective alerts
✓ Build operational dashboards
✓ Respond to incidents

Estimated cost: $20-50 (Log Analytics ingestion)
```

---

## Resource Requirements

### Azure Subscription

- Azure subscription (free tier acceptable for testing)
- Owner or Contributor role on subscription
- Resource quota for:
  - Virtual Machines (2-4)
  - Azure Container Registry (1)
  - Virtual Networks (1)
  - Storage Accounts (1)

### Local Tools Required

```text
Required:
├─ Azure CLI (latest version)
├─ PowerShell 7+
├─ kubectl (Kubernetes CLI)
├─ Docker (for container images)
└─ Text editor (VS Code recommended)

Optional:
├─ Azure Portal access
├─ Postman (API testing)
├─ Git (for script version control)
└─ Azure Storage Explorer
```

### Estimated Costs

```text
LAB COST ESTIMATION (Azure Resources)
═════════════════════════════════════════════════════════════

Per Lab Breakdown:

Lab 1 (Azure Local Simulation):
├─ Compute: Standard_B2s VM × 2 (4 hours) = ~$1
├─ Storage: 100 GB LRS = ~$2
└─ Total: ~$3-5

Lab 2 (Azure Arc):
├─ Arc agents: Free (agent software)
├─ Extension costs: ~$0-5 (optional extensions)
└─ Total: ~$0-5

Lab 3 (Edge RAG):
├─ GPU compute: Standard_NC6s_v3 (optional) = $0.90/hour
├─ Storage: 50 GB = ~$1
└─ Total: ~$10-50 (depends on GPU usage)

Lab 4 (Policy & Governance):
├─ Azure Policy: Free (included in subscription)
├─ Policy evaluations: No additional cost
└─ Total: ~$0

Lab 5 (Monitoring):
├─ Azure Monitor: Free (basic)
├─ Log Analytics: ~0.03 per GB ingested
├─ Estimated logs: 100 GB = ~$3
└─ Total: ~$3-10

TOTAL ESTIMATED COST: $16-70 USD
(Highly dependent on Lab 3 GPU usage and duration)

COST OPTIMIZATION TIPS:
├─ Use free tier resources where possible
├─ Shut down VMs between lab sessions
├─ Use spot instances for non-critical workloads
├─ Clean up resources immediately after labs
└─ Set up budget alerts in Azure
```

---

## Success Criteria

### Lab Completion Checklist

```text
✓ All 5 labs completed
✓ All validation steps passed
✓ All expected outputs confirmed
✓ Post-lab review completed
✓ Screenshots/evidence captured
✓ Lessons documented

GRADING SCALE:
└─ Beginner: 1-2 labs completed
└─ Intermediate: 3-4 labs completed
└─ Advanced: All 5 labs completed ← Target
└─ Expert: All labs + additional challenges
```

### Learning Validation

After completing all labs, you should be able to:

**Technical Skills:**
✓ Deploy and configure Azure Local in connected mode
✓ Onboard hybrid resources to Azure Arc
✓ Implement Edge RAG with LLM inference
✓ Create and enforce Azure Policy for governance
✓ Configure comprehensive monitoring and alerting
✓ Generate compliance reports and dashboards
✓ Respond to security incidents

**Business Skills:**
✓ Explain sovereign cloud deployment architecture
✓ Articulate compliance and data residency requirements
✓ Discuss cost-benefit of edge vs. cloud deployment
✓ Plan governance strategy for hybrid infrastructure
✓ Present monitoring and security dashboards to stakeholders

---

## Lab Navigation

### Quick Links

- **[Lab 1: Azure Local Deployment](./lab-01-azure-local-deployment.md)** - Deploy and configure Azure Local
- **[Lab 2: Azure Arc Onboarding](./lab-02-azure-arc-onboarding.md)** - Onboard infrastructure to Arc
- **[Lab 3: Edge RAG Setup](./lab-03-edge-rag-setup.md)** - Deploy complete Edge RAG solution
- **[Lab 4: Policy & Governance](./lab-04-policy-governance.md)** - Implement compliance policies
- **[Lab 5: Monitoring & Observability](./lab-05-monitoring-observability.md)** - Configure monitoring and alerts

### Module Navigation

- **[Module 1: Azure Local Architecture](./azure-local-architecture-deep-dive.md)**
- **[Module 2: Arc Advanced Management](./arc-advanced-management.md)**
- **[Module 3: Edge RAG Implementation](./edge-rag-implementation.md)**
- **[Module 4: Pre-Sales & Solution Design](./presales-solution-design.md)**
- **[Module 5: Compliance & Security Patterns](./compliance-security-patterns.md)**

---

## Troubleshooting & Support

### Common Issues

**Issue: "Subscription quota exceeded"**

- Solution: Check resource usage in Azure Portal
- Action: Delete unused resources or request quota increase

**Issue: "Command not found (Azure CLI)"**

- Solution: Azure CLI not installed or not in PATH
- Action: Reinstall Azure CLI from <https://docs.microsoft.com/cli/azure/install-azure-cli>

**Issue: "Authentication failed"**

- Solution: Not authenticated with Azure
- Action: Run `az login` and follow prompts

**Issue: "Resource group not found"**

- Solution: Wrong subscription or resource group name
- Action: Run `az group list` to see available groups

### Getting Help

**Documentation:**

- Azure Documentation: <https://docs.microsoft.com/azure>
- Azure CLI Reference: <https://docs.microsoft.com/cli/azure>
- kubectl Documentation: <https://kubernetes.io/docs>

**Support Options:**

- Azure Support Portal (paid support plans)
- Azure Community Forums
- Stack Overflow (tag: azure)
- GitHub Issues (for tool-specific issues)

---

_Last Updated: October 21, 2025_
