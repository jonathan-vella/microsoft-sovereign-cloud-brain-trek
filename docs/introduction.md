---
layout: default
title: Introduction
nav_order: 2
description: "Purpose, audience, and structure of the Microsoft Sovereign Cloud skilling plan"
---

# Introduction
{: .no_toc }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Purpose

This document outlines a structured learning path for sales and technical professionals to develop expertise in Microsoft's Sovereign Cloud offerings, Azure Local for edge computing, and leveraging AI at the edge with Retrieval-Augmented Generation (RAG).

The skilling plan provides:

- **Structured learning progression** from foundational to advanced concepts
- **Role-specific tracks** for sales and technical professionals
- **Hands-on lab experiences** for practical skill development
- **Clear success metrics** and completion criteria at each level
- **Curated Microsoft Learn resources** aligned with learning objectives

---

## Target Audience

### 👔 Sales & Pre-Sales Track

**Roles:**
- Account Executives
- Solution Specialists
- Technical Sales Professionals
- Pre-Sales Consultants

**Objectives:**
- Identify and qualify sovereign cloud opportunities
- Articulate business value and ROI
- Handle customer objections effectively
- Structure complex deals
- Navigate compliance discussions
- Conduct executive briefings

### 🔧 Technical Track

**Roles:**
- Cloud Architects
- Field Engineers
- AI Developers
- Solution Engineers
- Systems Administrators

**Objectives:**
- Design sovereign cloud architectures
- Plan and execute deployments
- Implement security and compliance controls
- Troubleshoot production issues
- Optimize performance and costs
- Manage hybrid environments

---

## Key Technologies

This skilling plan covers the following Microsoft technologies:

### Microsoft Sovereign Cloud

**[Learn More →](https://learn.microsoft.com/en-us/industry/sovereign-cloud/)**

Microsoft Sovereign Cloud addresses digital sovereignty requirements through three models:

- **Sovereign Public Cloud:** Enhanced Azure regions with additional sovereignty controls
- **Sovereign Private Cloud:** Dedicated infrastructure for sovereign workloads
- **National Partner Clouds:** Country-specific clouds operated by trusted local partners

**Key Capabilities:**
- Data residency and sovereignty
- Operational sovereignty
- Regulatory compliance (FedRAMP, ITAR, GDPR, etc.)
- Enhanced security and isolation

### Azure Local

**[Learn More →](https://learn.microsoft.com/en-us/azure/azure-local/)**

Azure Local (formerly Azure Stack HCI) extends Azure to customer-owned infrastructure for edge computing scenarios.

**Operating Modes:**

1. **Connected Operations**
   - Seamless Azure integration
   - Cloud-managed control plane via Azure Arc
   - Hybrid Azure services (Monitor, Backup, Defender)
   - Continuous updates from Azure

2. **Disconnected Operations**
   - Air-gapped environments
   - Local control plane
   - Highest operational sovereignty
   - Manual update delivery

**Common Use Cases:**
- Branch office infrastructure
- Data center modernization
- Latency-sensitive workloads
- Data residency requirements
- Virtual Desktop Infrastructure (VDI)
- Kubernetes at the edge

### Azure Arc

**[Learn More →](https://learn.microsoft.com/en-us/azure/azure-arc/)**

Azure Arc enables management of resources across hybrid and multi-cloud environments from a unified Azure control plane.

**Capabilities:**
- Server management (Windows/Linux)
- Kubernetes cluster management
- Data services (SQL, PostgreSQL)
- Azure services anywhere
- Unified governance and compliance

### Retrieval-Augmented Generation (RAG) on Azure Arc for Edge

**[Learn More →](https://learn.microsoft.com/en-us/azure/azure-arc/edge-rag/)**

Edge RAG enables generative AI solutions on on-premises data without moving data to the cloud.

**Key Features:**
- Search on-premises data with generative AI
- Data privacy and sovereignty
- Low-latency AI inference
- Custom model support (BYOM)
- Integration with Azure AI services

**Architecture Components:**
- AKS Arc cluster for compute
- NFS server for data storage
- Language models (Microsoft-provided or custom)
- Local portal for management
- Vector database for embeddings

---

## Learning Path Overview

The skilling plan is divided into three progressive levels, each building upon the previous one.

### 📊 Level Comparison

| Level | Objective | Sales Focus | Technical Focus | Duration |
|-------|-----------|-------------|-----------------|----------|
| **100** | **Foundational:** Understand the "what" and "why" | Articulate value propositions and identify customer scenarios | Grasp core architectural concepts and technology components | 2-4 weeks (4-12 hours) |
| **200** | **Intermediate:** Design solutions and handle objections | Develop proposals, conduct TCO/ROI analysis, position against competitors | Plan deployments, understand prerequisites, design solution architectures | 4-6 weeks (16-36 hours) |
| **300** | **Advanced:** Lead deployments and provide expert guidance | Structure complex deals and navigate deep compliance discussions | Execute end-to-end deployments, troubleshoot, and optimize for production | 8-12 weeks (48-120 hours) |

### 🎯 Level 100: Foundational Concepts

**[Start Level 100 →](level-100/)**

**Goal:** Build a solid understanding of core concepts, terminology, and value propositions.

**What You'll Learn:**
- Digital sovereignty principles
- Sovereign cloud models and use cases
- Azure Local architecture (connected vs. disconnected)
- Azure Arc fundamentals
- Edge RAG concepts

**Prerequisites:**
- Basic cloud computing knowledge
- Familiarity with virtualization
- Microsoft Learn account (free)

**Time Commitment:** 2-3 hours per week

### 🏗️ Level 200: Intermediate Skills

**[Start Level 200 →](level-200/)**

**Goal:** Develop the ability to design solutions, plan deployments, and address customer-specific requirements.

**What You'll Learn:**
- Sovereign Landing Zone architecture
- Azure Local deployment planning
- Edge RAG prerequisites and setup
- TCO/ROI modeling
- Competitive positioning

**Prerequisites:**
- Completion of Level 100
- Recommended: AZ-900 certification or equivalent
- Access to Azure subscription (technical track)

**Time Commitment:** 4-6 hours per week

### 🚀 Level 300: Advanced Expertise

**[Start Level 300 →](level-300/)**

**Goal:** Achieve expert-level proficiency to lead complex deployments, manage production environments, and drive strategic engagements.

**What You'll Learn:**
- Zero Trust security implementation
- Air-gapped deployment procedures
- Production Edge RAG optimization
- Advanced networking architectures
- MLOps at the edge

**Prerequisites:**
- Completion of Level 200
- Recommended: AZ-104 or AZ-305 certification
- Production or lab environment access
- PowerShell and IaC experience

**Time Commitment:** 6-10 hours per week

---

## Timeline Estimates

### Program Duration

**Total Program:** 14-22 weeks (approximately 3.5-5.5 months)

```
Level 100: ████ (2-4 weeks)
Level 200: ████████ (4-6 weeks)
Level 300: ████████████████ (8-12 weeks)
```

### Weekly Time Commitment

- **Level 100:** 2-3 hours per week
- **Level 200:** 4-6 hours per week
- **Level 300:** 6-10 hours per week

### Total Learning Hours

- **Level 100:** 4-12 hours total
- **Level 200:** 16-36 hours total
- **Level 300:** 48-120 hours total
- **Complete Program:** 68-168 hours total

---

## Success Metrics & Completion Criteria

Each level has clear success metrics to validate learning outcomes:

### Level 100 Completion ✅

**Sales Track:**
- ✓ Successfully articulate sovereign cloud value propositions in customer conversations
- ✓ Pass knowledge check quizzes
- ✓ Identify appropriate use cases for each sovereign model

**Technical Track:**
- ✓ Demonstrate understanding of architecture differences between connected and disconnected modes
- ✓ Complete foundational Microsoft Learn modules
- ✓ Explain key components and their interactions

### Level 200 Completion ✅

**Sales Track:**
- ✓ Develop and present a complete business case (TCO/ROI) for Azure Local deployment
- ✓ Handle common customer objections confidently
- ✓ Position solutions against competitive offerings

**Technical Track:**
- ✓ Successfully plan and document a deployment architecture for a test environment
- ✓ Complete lab exercises for Azure Local deployment planning
- ✓ Deploy a basic Edge RAG test environment

### Level 300 Completion ✅

**Sales Track:**
- ✓ Lead a customer engagement from discovery through contract signature
- ✓ Conduct executive-level briefings on sovereign cloud strategy
- ✓ Structure complex multi-component deals

**Technical Track:**
- ✓ Execute an end-to-end deployment in a production or production-like environment
- ✓ Troubleshoot and resolve deployment issues independently
- ✓ Optimize a production Edge RAG solution

---

## How to Use This Skilling Plan

### 1. Assess Your Starting Point

- Review the prerequisites for Level 100
- Determine which professional track (Sales or Technical) aligns with your role
- Evaluate your current knowledge level

### 2. Follow the Learning Path

- Start with Level 100 even if you have some experience
- Complete each level sequentially
- Use the provided checklists to track progress
- Allocate dedicated time each week

### 3. Engage with Hands-On Labs

- Technical track: Set up lab environments
- Complete practical exercises
- Document your learnings
- Share experiences with peers

### 4. Leverage Microsoft Resources

- Complete recommended Microsoft Learn modules
- Access official documentation
- Join Microsoft Tech Community
- Attend webinars and events

### 5. Validate Your Learning

- Complete knowledge checks
- Meet success criteria for each level
- Consider pursuing relevant Microsoft certifications
- Apply skills in real customer scenarios

---

## Additional Resources

### Microsoft Official Documentation

- **[Microsoft Sovereign Cloud Hub](https://learn.microsoft.com/en-us/industry/sovereign-cloud/)** - Central resource for all sovereign cloud documentation
- **[Azure Local Documentation](https://learn.microsoft.com/en-us/azure/azure-local/)** - Complete technical reference
- **[Edge RAG Documentation](https://learn.microsoft.com/en-us/azure/azure-arc/edge-rag/)** - Deployment guides and requirements

### Microsoft Learn Training Paths

- **[Get started with Microsoft Cloud for Sovereignty](https://learn.microsoft.com/en-us/training/paths/get-started-sovereignty/)**
- **[Manage hybrid workloads with Azure Arc](https://learn.microsoft.com/en-us/training/paths/manage-hybrid-infrastructure-with-azure-arc/)**

### Community & Support

- **[Microsoft Tech Community](https://techcommunity.microsoft.com/)** - Forums and blogs
- **[Azure Local Supportability GitHub](https://github.com/Azure/AzureLocal-Supportability)** - Troubleshooting guides

---

## Next Steps

Ready to begin? Start your learning journey:

1. **[Review Level 100 Prerequisites](level-100/prerequisites.html)**
2. **[Begin Level 100: Foundational Concepts](level-100/)**
3. **[Explore Additional Resources](resources/)**

---

<div class="note">
  <strong>💡 Tip:</strong> Bookmark this page and return regularly to track your progress through the learning path.
</div>
