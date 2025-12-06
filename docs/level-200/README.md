---
layout: default
title: Level 200 - Intermediate
nav_order: 5
has_children: true
description: "Intermediate architecture and pre-sales skills for Microsoft Sovereign Cloud solutions"
---

# Level 200: Intermediate - Architecture & Pre-Sales

## Overview

Develop the ability to design solutions, plan deployments, and address customer-specific requirements for sovereign cloud architectures.

---

## Learning Objectives

By the end of Level 200, you will be able to:

### Sales & Pre-Sales Track

- ✅ Map customer requirements to appropriate sovereign cloud models
- ✅ Conduct TCO and ROI analysis for Azure Local deployments
- ✅ Position solutions against competitive offerings
- ✅ Qualify Edge RAG opportunities
- ✅ Present complete business cases to customers

### Technical Track

- ✅ Design Sovereign Landing Zone architectures
- ✅ Plan Azure Local deployments (connected and disconnected)
- ✅ Understand Edge RAG deployment prerequisites
- ✅ Architect hybrid connectivity solutions
- ✅ Implement governance and compliance controls

---

## Prerequisites

Before starting Level 200, ensure you have:

- [x] Completed Level 100 learning objectives
- [ ] Recommended: AZ-900 (Azure Fundamentals) certification or equivalent knowledge
- [ ] Access to an Azure subscription (for technical track)
- [ ] Access to lab environment or Azure Local hardware for hands-on exercises

**Estimated Time Commitment:** 2-3 hours per week  
**Total Program Duration:** 2-3 weeks (to complete all modules)  
**Total Planned Hours:** 6-10 hours core content

---

## Learning Modules

### Module 1: Azure Local Architecture Deep Dive

**Duration:** 1.5-2 hours | **Status:** ✅ Complete

Explore advanced Azure Local deployment patterns, hardware planning, high-availability architectures, and advanced networking scenarios for enterprise edge deployments.

**Core Topics:**

- [Main Page: Azure Local Architecture Deep Dive](azure-local-architecture-deep-dive.md)
- [Hardware Planning & Sizing](azure-local-hardware-planning.md)
- [High-Availability Patterns](azure-local-ha-patterns.md)
- [Advanced Networking Configurations](azure-local-advanced-networking.md)
- [Knowledge Check](azure-local-deep-dive-knowledge-check.md)

---

### Module 2: Arc Advanced Management

**Duration:** 2-2.5 hours | **Status:** ✅ Complete

Master enterprise-scale governance, cost optimization, and security hardening for Azure Arc across hybrid and multi-cloud environments.

**Core Topics:**

- [Main Page: Arc Advanced Management](arc-advanced-management.md)
- [Policy & Governance at Scale](arc-policy-and-governance.md)
- [Cost Optimization Strategies](arc-cost-optimization.md)
- [Enterprise Deployment Patterns](arc-enterprise-patterns.md)
- [Knowledge Check](arc-advanced-knowledge-check.md)

---

### Module 3: Edge RAG Implementation

**Duration:** 2-2.5 hours | **Status:** ✅ Complete

Master production-ready Retrieval-Augmented Generation deployment patterns, LLM optimization, vector database tuning, and operational excellence for enterprise edge deployments.

**Core Topics:**

- [Main Page: Edge RAG Implementation](edge-rag-implementation.md)
- [LLM Inference Optimization](llm-inference-optimization.md)
- [Vector Databases for Edge](vector-databases-edge.md)
- [RAG Deployment Strategies](rag-deployment-strategies.md)
- [RAG Operations & Monitoring](rag-operations-monitoring.md)
- [Knowledge Check](rag-implementation-knowledge-check.md)

---

### Module 4: Pre-Sales & Solution Design

**Duration:** 1.5-2 hours | **Status:** ✅ Complete

Master customer discovery, solution architecture, sizing methodologies, and business case development for sovereign cloud implementations.

**Core Topics:**

- [Main Page: Pre-Sales Solution Design](presales-solution-design.md)
- [Customer Discovery Framework](customer-discovery.md)
- [Solution Sizing Methodologies](solution-sizing.md)
- [TCO & Cost Estimation](cost-estimation.md)
- [Knowledge Check](presales-knowledge-check.md)

---

### Module 5: Compliance & Security Patterns

**Duration:** 1.5-2 hours | **Status:** ✅ Complete

Master regulatory compliance frameworks (GDPR, FedRAMP), encryption strategies, key management, security hardening, and incident response for sovereign cloud deployments.

**Core Topics:**

- [Main Page: Compliance & Security Patterns](compliance-security-patterns.md)
- [GDPR Implementation Guide](gdpr-implementation.md)
- [FedRAMP Compliance](fedramp-compliance.md)
- [Encryption & Key Management](encryption-key-management.md)
- [Security Hardening Practices](security-hardening.md)
- [Knowledge Check](compliance-knowledge-check.md)

---

### Module 6: Hands-On Labs

**Status:** ✅ Complete

Five progressive hands-on labs reinforcing Modules 1-5 through practical implementation of Azure Local, Azure Arc, Edge RAG, policy governance, and monitoring in a complete sovereign cloud environment.

{: .note }
> **💡 Note:** Lab exercises are provided for hands-on practice. Time to complete labs varies based on environment setup and individual experience.

**Lab Overview:**

1. [Lab 1: Azure Local Deployment](lab-01-azure-local-deployment.md)
   - Deploy Azure Local in connected mode with sample applications
2. [Lab 2: Azure Arc Onboarding](lab-02-azure-arc-onboarding.md)
   - Register and manage resources with Arc, GitOps, extensions
3. [Lab 3: Edge RAG Setup](lab-03-edge-rag-setup.md)
   - Complete RAG system with Weaviate, Ollama, and FastAPI
4. [Lab 4: Policy & Governance](lab-04-policy-governance.md)
   - Custom policies, Kubernetes enforcement, compliance monitoring
5. [Lab 5: Monitoring & Observability](lab-05-monitoring-observability.md)
   - End-to-end monitoring with Log Analytics, alerts, and dashboards

**[Module 6 Overview & Navigation](../level-200/README)**

---

## Recommended Microsoft Learn Resources

### Essential Learning

1. **[Implement Azure Landing Zones](https://learn.microsoft.com/en-us/training/modules/enterprise-scale-introduction/)**
   - Foundation for sovereign landing zones

2. **[Configure Azure Arc-enabled Kubernetes](https://learn.microsoft.com/en-us/training/modules/intro-to-arc-enabled-kubernetes/)**
   - Essential for Azure Local management

3. **[Manage hybrid workloads with Azure Arc](https://learn.microsoft.com/en-us/training/paths/manage-hybrid-infrastructure-with-azure-arc/)**
   - Complete learning path for hybrid scenarios

### Recommended Reading

- **[Sovereign Landing Zone architecture](https://learn.microsoft.com/en-us/industry/sovereign-cloud/sovereign-public-cloud/sovereign-landing-zone/overview-slz)** - SLZ design principles
- **[Azure Local deployment overview](https://learn.microsoft.com/en-us/azure/azure-local/deploy/deployment-introduction)** - Deployment planning guide
- **[Disconnected operations overview](https://learn.microsoft.com/en-us/azure/azure-local/manage/disconnected-operations-overview)** - Air-gapped deployment guidance
- **[Edge RAG deployment prerequisites](https://learn.microsoft.com/en-us/azure/azure-arc/edge-rag/complete-prerequisites)** - Complete prerequisites checklist

---

## Hands-On Labs

### Lab 1: Azure Local Architecture & Hardware Sizing

**Objective:** Plan and document an advanced Azure Local deployment scenario with proper hardware sizing

**Module:** Azure Local Architecture Deep Dive  
**Prerequisites:**

- Completion of Module 1: Azure Local Architecture Deep Dive
- Access to Azure Local sizing tool
- Understanding of customer requirements

**Topics Covered:**

- Hardware planning and capacity calculations
- High-availability pattern design
- Network configuration for edge scenarios

---

### Lab 2: Arc Advanced Governance & Cost Analysis

**Objective:** Design an enterprise Arc governance framework with policy enforcement and cost optimization strategies

**Module:** Arc Advanced Management  
**Prerequisites:**

- Completion of Module 2: Arc Advanced Management
- Access to an Azure subscription
- Understanding of Azure Policy

**Topics Covered:**

- Azure Policy implementation at scale
- Cost optimization strategies
- Enterprise governance patterns

---

### Lab 3: Edge RAG Infrastructure Preparation

**Objective:** Set up and optimize infrastructure for Edge RAG production deployment

**Module:** Edge RAG Implementation  
**Prerequisites:**

- Completion of Module 3: Edge RAG Implementation
- AKS Arc cluster or ability to create one
- Linux VM or container environment

**Topics Covered:**

- Vector database setup and indexing
- LLM model deployment and optimization
- RAG system monitoring and operations

---

## Success Criteria

### Module 1: Azure Local Architecture Deep Dive ✅

You have successfully completed Module 1 when you can:

- ✓ Design advanced Azure Local architectures for enterprise deployments
- ✓ Plan hardware sizing and capacity management
- ✓ Architect high-availability patterns for edge scenarios
- ✓ Configure advanced networking for hybrid environments
- ✓ Successfully complete the deep-dive quiz

### Module 2: Arc Advanced Management ✅

You have successfully completed Module 2 when you can:

- ✓ Implement enterprise-scale governance policies across Arc resources
- ✓ Design cost optimization strategies for hybrid environments
- ✓ Develop enterprise governance patterns (hub-spoke, federation, zero-trust)
- ✓ Analyze TCO and ROI for multi-cloud Arc deployments
- ✓ Successfully complete the advanced quiz

### Module 3: Edge RAG Implementation ✅

You have successfully completed Module 3 when you can:

- ✓ Design production-ready RAG deployment architectures
- ✓ Optimize LLM inference for edge environments
- ✓ Select and tune vector databases for enterprise use
- ✓ Implement RAG deployment patterns and strategies
- ✓ Monitor and operate RAG systems in production
- ✓ Successfully complete the implementation quiz

---

## Next Steps

### Current Progress

**✅ Completed:** Modules 1, 2, 3, 4, 5, and 6 (All Level 200 modules!)  
**Duration:** 10-11 hours of comprehensive intermediate content  
**Status:** Level 200 is 100% complete with all hands-on labs

---

## Module Roadmap

| Module | Status | Topics | Duration | Files |
|--------|--------|--------|----------|-------|
| **Module 1** | ✅ Complete | Azure Local Architecture, Hardware Planning, HA Patterns, Advanced Networking | 1.5-2 hrs | 5 |
| **Module 2** | ✅ Complete | Arc Governance, Cost Optimization, Enterprise Patterns | 2-2.5 hrs | 5 |
| **Module 3** | ✅ Complete | RAG Deployment, LLM Optimization, Vector Databases, Operations | 2-2.5 hrs | 6 |
| **Module 4** | ✅ Complete | Pre-Sales, Discovery, Sizing, Cost Estimation | 1.5-2 hrs | 5 |
| **Module 5** | ✅ Complete | Compliance, GDPR, FedRAMP, Encryption, Security Hardening | 1.5-2 hrs | 6 |
| **Module 6** | ✅ Complete | Hands-On Labs (5 progressive labs with Azure Local, Arc, RAG, Policy, Monitoring) | Varies by experience | 6 |
| **Level 200 Total** | ✅ Complete | **All intermediate topics with practical labs** | **10-11 hrs** | **33 files** |

---

## Module Success Criteria

### Module 4: Pre-Sales & Solution Design ✅

You have successfully completed Module 4 when you can:

- ✓ Conduct customer discovery and requirements gathering
- ✓ Analyze competitive positioning and market differentiation
- ✓ Perform TCO and ROI calculations for sovereign cloud solutions
- ✓ Design complete customer proposals with business cases
- ✓ Successfully complete the pre-sales quiz

### Module 5: Compliance & Security Patterns ✅

You have successfully completed Module 5 when you can:

- ✓ Implement GDPR compliance requirements for data processing
- ✓ Meet FedRAMP compliance for government cloud deployments
- ✓ Design encryption strategies (at-rest and in-transit)
- ✓ Manage cryptographic keys with Azure Key Vault
- ✓ Implement zero-trust security architecture
- ✓ Design incident response procedures
- ✓ Successfully complete the compliance quiz

### Module 6: Hands-On Labs ✅

You have successfully completed Module 6 when you can:

- ✓ Deploy and configure Azure Local in connected mode (Lab 1)
- ✓ Register Kubernetes clusters with Azure Arc (Lab 2)
- ✓ Implement complete Edge RAG solution (Lab 3)
- ✓ Enforce governance policies across hybrid infrastructure (Lab 4)
- ✓ Configure comprehensive monitoring and alerting (Lab 5)
- ✓ All validation steps passing on 5 labs

**Last Updated:** October 2025
