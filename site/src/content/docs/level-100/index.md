---
title: "Level 100 - Foundation"
description: "Foundational concepts for Microsoft Sovereign Cloud & AI at the Edge"
sidebar:
  order: 4
---

## Overview

Build a solid understanding of the core concepts, terminology, and value propositions for Microsoft Sovereign Cloud, Azure Local, and Edge RAG.

---

## Learning Objectives

By the end of Level 100, you will be able to:

### Sales & Pre-Sales Track

- ✅ Articulate the value proposition of digital sovereignty
- ✅ Explain the three Microsoft Sovereign Cloud models
- ✅ Identify customer scenarios requiring sovereign solutions
- ✅ Differentiate between Azure Local connected and disconnected modes
- ✅ Describe the business value of Edge RAG

### Technical Track

- ✅ Understand core sovereignty architectural concepts
- ✅ Explain Azure Local architecture differences (connected vs. disconnected)
- ✅ Describe Azure Arc's role in hybrid management
- ✅ Understand Edge RAG components and architecture
- ✅ Identify validated hardware requirements

---

## Prerequisites

Before starting Level 100, ensure you have:

- [ ] Basic understanding of cloud computing concepts
- [ ] Familiarity with virtualization fundamentals
- [ ] Access to Microsoft Learn (free account) - [Sign up here](https://learn.microsoft.com)
- [ ] (Optional) Azure free account for hands-on exploration - [Get started](https://azure.microsoft.com/free)

**Estimated Time Commitment:** 1 hour per week
**Total Duration:** 1-2 weeks
**Total Hours:** 1-3 hours

---

## Learning Modules

### 1. Digital Sovereignty Fundamentals

**Duration:** 15-30 minutes

📚 **Main Content:**

- [Digital Sovereignty Overview](/level-100/module-01-digital-sovereignty/digital-sovereignty/) - Core concepts, principles, and customer scenarios

**Deep Dive Topics:**

- [Microsoft's European Digital Commitments](/level-100/module-01-digital-sovereignty/european-commitments/) - The 5 commitments and EU Data Boundary
- [Regulatory Requirements Overview](/level-100/module-01-digital-sovereignty/regulatory-overview/) - GDPR, FedRAMP, HIPAA, PCI DSS, ITAR
- [Data Residency vs. Sovereignty](/level-100/module-01-digital-sovereignty/data-residency-concepts/) - Definitions and Azure implementation
- [Operational Sovereignty](/level-100/module-01-digital-sovereignty/operational-sovereignty/) - Control plane concepts and Azure Local modes

✅ **Assessment:**

- [Knowledge Check Quiz](/level-100/module-01-digital-sovereignty/knowledge-check/) - 15 questions to test your understanding

**Key Concepts:**

- Data residency and localization
- Operational sovereignty
- Compliance and regulatory frameworks
- EU Data Boundary
- Control plane models

### 2. Microsoft Sovereign Cloud Models

**Duration:** 30-45 minutes

📚 **Main Content:**

- [Microsoft Sovereign Cloud Models Overview](/level-100/module-02-cloud-models/sovereign-cloud-models/) - Three models, comparison, and decision framework

**Deep Dive Topics:**

- [Sovereign Public Cloud](/level-100/module-02-cloud-models/sovereign-public-cloud/) - Azure with enhanced sovereignty controls and Microsoft Cloud for Sovereignty
- [Sovereign Private Cloud](/level-100/module-02-cloud-models/sovereign-private-cloud/) - Azure Local (Connected and Disconnected modes) for dedicated infrastructure
- [National Partner Clouds](/level-100/module-02-cloud-models/national-partner-clouds/) - Azure Government, Azure China, and partner-operated sovereign clouds

✅ **Assessment:**

- [Cloud Models Knowledge Check](/level-100/module-02-cloud-models/cloud-models-knowledge-check/) - 15 questions testing model selection and technical understanding

**Key Concepts:**

- Model differentiation (Public, Private, Partner)
- Microsoft Cloud for Sovereignty capabilities
- Azure Local Connected vs. Disconnected
- Customer Lockbox and Confidential Computing
- Azure Government and Azure China
- Use case mapping and decision criteria

### 3. Azure Local Overview

**Duration:** 30-45 minutes

📚 **Main Content:**

- [Azure Local Overview](/level-100/module-03-azure-local/azure-local-overview/) - Architecture, deployment modes, customer scenarios

**Deep Dive Topics:**

- [Azure Local Architecture Deep Dive](/level-100/module-03-azure-local/azure-local-architecture/) - Hardware, networking, security layers
- [Connected Mode Operations](/level-100/module-03-azure-local/azure-local-connected-mode/) - Azure integration, monitoring, update management
- [Disconnected Mode Operations](/level-100/module-03-azure-local/azure-local-disconnected-mode/) - Air-gapped deployment, periodic sync
- [Hardware Requirements & Planning](/level-100/module-03-azure-local/azure-local-hardware/) - Validated hardware, sizing, deployment checklist

✅ **Assessment:**

- [Azure Local Knowledge Check](/level-100/module-03-azure-local/azure-local-knowledge-check/) - 15 questions testing deployment modes and technical concepts

**Key Concepts:**

- Connected vs. Disconnected deployment modes
- Data sovereignty and control plane separation
- Hyper-V, Storage Spaces Direct, RDMA networking
- Azure Arc integration
- Validated hardware ecosystem
- High availability and disaster recovery

---

### 4. Azure Arc Introduction

**Duration:** 25-30 minutes

📚 **Main Content:**

- [Azure Arc Introduction](/level-100/module-04-azure-arc/azure-arc-intro/) - Hybrid management, multi-cloud governance, three Arc services

**Deep Dive Topics:**

- [Arc-enabled Servers](/level-100/module-04-azure-arc/azure-arc-servers/) - Windows/Linux management, policy, monitoring
- [Arc-enabled Kubernetes](/level-100/module-04-azure-arc/azure-arc-kubernetes/) - GitOps, multi-cluster management, policy enforcement
- [Arc-enabled Data Services](/level-100/module-04-azure-arc/azure-arc-data-services/) - SQL MI and PostgreSQL on any infrastructure

✅ **Assessment:**

- [Azure Arc Knowledge Check](/level-100/module-04-azure-arc/azure-arc-knowledge-check/) - 12 questions covering all Arc services

**Key Concepts:**

- Unified control plane for hybrid/multi-cloud
- Azure Arc Servers, Kubernetes, Data Services
- Azure Policy enforcement everywhere
- GitOps-based configuration management
- Data services with managed experience anywhere
- Multi-cloud governance and compliance

---

### 5. Edge RAG Concepts

**Duration:** 30-40 minutes

📚 **Main Content:**

- [Edge RAG Concepts](/level-100/module-05-edge-rag/edge-rag-concepts/) RAG fundamentals, edge deployment benefits, customer scenarios

**Deep Dive Topics:**

- [RAG Fundamentals](/level-100/module-05-edge-rag/rag-fundamentals/) - Embeddings, vector databases, LLM limitations
- [Edge RAG Architecture](/level-100/module-05-edge-rag/edge-rag-architecture/) - Local LLM deployment, ingestion pipeline, query processing
- [Edge RAG Use Cases and Implementation](/level-100/module-05-edge-rag/edge-rag-use-cases/) - Industry scenarios, best practices, ROI

✅ **Assessment:**

- [Edge RAG Knowledge Check](/level-100/module-05-edge-rag/edge-rag-knowledge-check/) - 15 questions testing RAG concepts and implementation

**Key Concepts:**

- RAG (Retrieval-Augmented Generation) basics
- Traditional LLMs vs. RAG-augmented systems
- Edge deployment for data sovereignty
- Vector embeddings and similarity search
- Local LLM considerations
- Privacy-preserving AI
- Healthcare, manufacturing, financial use cases

---

## Recommended Microsoft Learn Resources

Complete these Microsoft Learn paths and modules:

### Essential Learning

1. **[Get started with Microsoft Cloud for Sovereignty](https://learn.microsoft.com/en-us/training/paths/get-started-sovereignty/)**
   - 4 modules, ~3 hours
   - Covers sovereignty fundamentals, Azure Policy, key management, confidential computing

2. **[Azure fundamentals](https://learn.microsoft.com/en-us/training/paths/azure-fundamentals/)**
   - 6 modules, ~6 hours
   - Essential background for all Azure-related learning

3. **[Introduction to Azure hybrid cloud services](https://learn.microsoft.com/en-us/training/modules/intro-to-azure-hybrid-services/)**
   - 1 module, ~45 minutes
   - Understanding hybrid cloud scenarios

4. **[Introduction to Azure Arc](https://learn.microsoft.com/en-us/training/modules/intro-to-azure-arc/)**
   - 1 module, ~30 minutes
   - Azure Arc fundamentals

### Recommended Reading

- **[What is digital sovereignty?](https://learn.microsoft.com/en-us/industry/sovereign-cloud/overview/digital-sovereignty)** - Core concept documentation
- **[Azure Local overview](https://learn.microsoft.com/en-us/azure/azure-local/overview)** - Product introduction
- **[What is Edge RAG?](https://learn.microsoft.com/en-us/azure/azure-arc/edge-rag/overview)** - AI at the edge concepts
- **[Microsoft Sovereign Cloud Hub](https://learn.microsoft.com/en-us/industry/sovereign-cloud/)** - Central documentation hub

---

## Success Criteria

### Sales Track Completion ✅

You have successfully completed Level 100 (Sales Track) when you can:

- ✓ Articulate sovereign cloud value propositions in customer conversations
- ✓ Identify appropriate use cases for each sovereign model
- ✓ Explain the difference between connected and disconnected Azure Local
- ✓ Describe Edge RAG benefits for on-premises data scenarios
- ✓ Pass knowledge check quizzes with 80% or higher

### Technical Track Completion ✅

You have successfully completed Level 100 (Technical Track) when you can:

- ✓ Explain architecture differences between connected and disconnected modes
- ✓ Describe key components of Azure Local infrastructure
- ✓ Understand Azure Arc's role in hybrid management
- ✓ Identify Edge RAG architectural components
- ✓ Complete all foundational Microsoft Learn modules

---

## Knowledge Check

Test your understanding with these questions:

1. What are the three models of Microsoft Sovereign Cloud?
2. What is the primary difference between Azure Local connected and disconnected operations?
3. How does Azure Arc enable hybrid cloud management?
4. What is Retrieval-Augmented Generation (RAG)?
5. Why is data residency important for sovereign workloads?

**[Take the Level 100 Quiz →](/level-100/module-01-digital-sovereignty/knowledge-check/)**

---

## Next Steps

Once you've completed Level 100:

1. ✅ Review all module content and ensure understanding
2. ✅ Complete knowledge check with passing score
3. ✅ Document any questions for Level 200
4. 🎯 **[Proceed to Level 200: Intermediate Skills →](../level-200/)**

---

## Additional Resources

- [Microsoft Tech Community - Sovereign Cloud](https://techcommunity.microsoft.com/t5/sovereign-cloud/ct-p/SovereignCloud)
- [Azure Local YouTube Channel](https://www.youtube.com/@AzureStackHCI)
- [Azure Arc Blog](https://techcommunity.microsoft.com/t5/azure-arc-blog/bg-p/AzureArcBlog)

---

**Last Updated:** October 2025

[def]: edge-rag-concepts.md
