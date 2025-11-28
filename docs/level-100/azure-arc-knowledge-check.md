---
layout: default
title: Azure Arc Knowledge Check
parent: Module 4 - Azure Arc Introduction
nav_order: 4.4
---

# Azure Arc Knowledge Check

{: .no_toc }

Test your understanding of Azure Arc concepts, services, and use cases.

---

## Quiz Instructions

- **Total Questions:** 12
- **Passing Score:** 80% (10 of 12 correct)
- **Time Estimate:** 15-20 minutes
- **Format:** Multiple choice (A/B/C/D)

**Tips:**

- Read each question carefully
- Consider real-world scenarios
- Review module content if unsure
- Check your answers against explanations below

---

## Questions

### Question 1: Azure Arc Fundamentals

**What is the primary purpose of Azure Arc?**

A) To migrate workloads from on-premises to Azure cloud  
B) To extend Azure management and services to any infrastructure  
C) To replace existing infrastructure management tools  
D) To provide backup services for on-premises servers

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Azure Arc's primary purpose is to extend Azure management, governance, and services to any infrastructure - on-premises, multi-cloud, or edge. It does not migrate workloads (that's Azure Migrate), doesn't replace tools (it complements them), and backup is just one of many capabilities.

**Reference:** [Azure Arc Introduction](azure-arc-intro#what-is-azure-arc)
</details>

---

### Question 2: Arc Services

**Which THREE services are part of Azure Arc? (Select all that apply)**

A) Arc-enabled Servers  
B) Arc-enabled Kubernetes  
C) Arc-enabled Data Services  
D) Arc-enabled Virtual Networks

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: A, B, C**

**Explanation:**
The three pillars of Azure Arc are Arc-enabled Servers (Windows/Linux machines), Arc-enabled Kubernetes (any CNCF-certified K8s), and Arc-enabled Data Services (SQL MI and PostgreSQL). Arc-enabled Virtual Networks is not an Arc service.

**Reference:** [Three Pillars of Azure Arc](azure-arc-intro#three-pillars-of-azure-arc)
</details>

---

### Question 3: Data Residency

**In Azure Arc, what type of data is sent to Azure from Arc-enabled Servers?**

A) All application data and databases  
B) Only metadata, metrics, logs, and configuration - not workload data  
C) Only credentials and passwords  
D) All data is kept 100% local with no Azure sync

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Arc synchronizes metadata (inventory, configuration), metrics, and logs to Azure for management purposes, but workload data (application data, databases, files) stays on-premises. This enables cloud-based management while maintaining data sovereignty.

**Reference:** [Arc and Sovereignty](azure-arc-intro#arc-and-sovereignty)
</details>

---

### Question 4: Arc-Enabled Servers

**What is required to onboard a Windows or Linux server to Azure Arc?**

A) The server must be migrated to Azure first  
B) Install the Connected Machine agent and provide Azure authentication  
C) The server must be domain-joined  
D) Purchase special Arc licenses

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Onboarding requires installing the Connected Machine agent on the server and authenticating to Azure (via service principal or interactive login). Servers can be anywhere (not just Azure), domain-join is optional, and Arc itself has no additional license cost.

**Reference:** [Arc Servers Onboarding](azure-arc-servers#onboarding-process-and-architecture)
</details>

---

### Question 5: GitOps

**What is the primary benefit of using GitOps with Arc-enabled Kubernetes?**

A) Faster Kubernetes cluster creation  
B) Git repository becomes the source of truth for cluster configuration with automatic synchronization  
C) Eliminates the need for kubectl  
D) Reduces Kubernetes licensing costs

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
GitOps uses Git as the source of truth for cluster configuration. Changes committed to Git automatically sync to clusters via Flux, providing version control, audit trail, and consistent deployments. It doesn't create clusters, doesn't eliminate kubectl (complements it), and Kubernetes is open source (no licensing).

**Reference:** [GitOps Configuration Management](azure-arc-kubernetes#gitops-based-configuration-management)
</details>

---

### Question 6: Azure Policy

**Which of the following can Azure Policy do for Arc-enabled Servers?**

A) Automatically migrate servers to Azure  
B) Audit compliance and optionally remediate configuration drift  
C) Replace the server operating system  
D) Increase server hardware resources

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Azure Policy can audit server configurations for compliance and optionally remediate drift (deploy missing extensions, configure settings, etc.). It doesn't migrate servers, change OS, or modify hardware - those require different tools/processes.

**Reference:** [Applying Azure Policy](azure-arc-servers#applying-azure-policy)
</details>

---

### Question 7: Multi-Cloud Support

**Azure Arc supports managing resources in which of the following?**

A) Only Microsoft Azure  
B) Only on-premises  
C) Azure, AWS, GCP, and any infrastructure  
D) Only Microsoft technologies

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: C**

**Explanation:**
Azure Arc supports any infrastructure - Microsoft Azure, AWS, Google Cloud, on-premises, edge, and any other cloud. It's designed for multi-cloud and hybrid scenarios and supports non-Microsoft technologies (Linux, any K8s distribution, PostgreSQL, etc.).

**Reference:** [Multi-Cloud Governance](azure-arc-intro#multi-cloud-governance-capabilities)
</details>

---

### Question 8: Use Case Selection

**A retail company has 200 stores with local Kubernetes clusters running POS applications. They want consistent deployment and security policies. Which Arc service is best?**

A) Arc-enabled Servers  
B) Arc-enabled Kubernetes  
C) Arc-enabled Data Services  
D) Azure Migrate

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Arc-enabled Kubernetes is designed for managing multiple Kubernetes clusters with consistent GitOps deployment and Azure Policy enforcement. Arc Servers is for individual machines, Data Services is for databases, and Azure Migrate is for migrations (not management).

**Reference:** [Arc Kubernetes Scenarios](azure-arc-kubernetes#use-case-scenarios)
</details>

---

### Question 9: Arc Data Services Licensing

**Which licensing models are available for Azure SQL Managed Instance on Arc?**

A) Only pay-as-you-go  
B) Only bring-your-own-license (BYOL)  
C) Both pay-as-you-go and BYOL with Azure Hybrid Benefit  
D) Free (no licensing cost)

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: C**

**Explanation:**
Arc SQL MI supports both pay-as-you-go (Azure consumption billing) and BYOL where you can bring existing SQL Server licenses and leverage Azure Hybrid Benefit for up to 55% savings. It's not free - either model incurs costs.

**Reference:** [Data Services Billing](azure-arc-data-services#billing-model)
</details>

---

### Question 10: High Availability

**How does Azure SQL Managed Instance on Arc provide high availability?**

A) By replicating to Azure SQL Database  
B) Using Always-On Availability Groups with automatic failover  
C) By creating manual backups every hour  
D) High availability is not supported on Arc

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Arc SQL MI uses Always-On Availability Groups (AG) with synchronous replication and automatic failover, providing 99.95% SLA. It doesn't replicate to Azure SQL Database, hourly backups don't provide HA, and HA is a core feature.

**Reference:** [Elastic Scale and HA](azure-arc-data-services#elastic-scale-and-high-availability)
</details>

---

### Question 11: Deployment Modes

{: .note }
> **📝 Updated November 2025:** Indirectly Connected mode was retired in September 2025.

**Which statement about Azure Arc Data Services connectivity is correct as of November 2025?**

A) Indirectly Connected mode is recommended for maximum security  
B) Only Directly Connected mode is supported; Indirect mode was retired in September 2025  
C) Indirectly Connected mode offers better performance  
D) Both modes are fully supported with identical features

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
As of September 2025, **Indirectly Connected mode has been retired**. Azure Arc-enabled Data Services now only supports Directly Connected mode, which requires continuous Azure connectivity for billing, monitoring, and management through the Azure portal.

For disconnected/air-gapped scenarios, organizations should use **Azure Local with Disconnected Operations** (Preview), which provides a local Azure portal experience and supports Arc-enabled data services without public cloud connectivity.

**Reference:** [Azure Arc Data Services Connectivity](https://learn.microsoft.com/en-us/azure/azure-arc/data/connectivity)
</details>

---

### Question 12: Cost and Licensing

**What is included in the cost of using Azure Arc itself?**

A) High per-server licensing fees  
B) Azure Arc has no additional charge - you pay only for Azure services consumed  
C) Requires Enterprise Agreement  
D) Monthly subscription per cluster

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Azure Arc itself is free - there's no charge to connect servers, Kubernetes clusters, or deploy the data controller. You only pay for Azure services you consume (Azure Monitor, Defender, Update Management, etc.). No EA required, no per-server fees, no subscriptions for Arc itself.

**Reference:** [Arc Servers Cost Model](azure-arc-servers#cost-model-and-licensing)
</details>

---

## Scoring Guide

**Calculate your score:**

- Count the number of correct answers
- Divide by 12 and multiply by 100 for percentage

**Score Interpretation:**

**10-12 correct (83-100%):** ✅ **Excellent!** You have a strong understanding of Azure Arc concepts.

- Ready to proceed to next module
- Consider reviewing missed questions for completeness

**8-9 correct (67-82%):** ⚠️ **Good progress, but review needed**

- Review the module content, especially areas where you missed questions
- Pay attention to differences between Arc services
- Revisit Azure Arc fundamentals and data sovereignty concepts
- Retake quiz after review

**6-7 correct (50-66%):** ❌ **More study required**

- Thoroughly review all module content
- Focus on core concepts: Arc services, data residency, multi-cloud management
- Review customer scenarios to understand real-world applications
- Consider hands-on practice if available
- Retake quiz after comprehensive review

**0-5 correct (0-49%):** ❌ **Significant review needed**

- Start from the beginning with [Azure Arc Introduction](azure-arc-intro)
- Read each sub-page carefully
- Take notes on key concepts
- Review all use case scenarios
- Consider additional Microsoft Learn resources
- Retake quiz only after thorough review

---

## Study Recommendations

**If you missed questions on Arc fundamentals (Q1, Q3, Q7):**

- Review [Azure Arc Introduction](azure-arc-intro)
- Focus on what Arc does and doesn't do

**If you missed questions on specific services (Q2, Q4, Q5, Q8):**

- Review [Arc Servers](azure-arc-servers)
- Review [Arc Kubernetes](azure-arc-kubernetes)

**If you missed questions on Data Services (Q9, Q10, Q11):**

- Review [Arc Data Services](azure-arc-data-services)

**If you missed questions on policy and governance (Q6):**

- Review [Azure Policy for Arc](azure-arc-servers#applying-azure-policy)

---

## Next Steps

**After completing this assessment:**

1. **✅ Celebrate your achievement!** You've completed Azure Arc foundational concepts.

2. **📚 Continue to next module:**
   - [Edge RAG Concepts →](edge-rag-concepts)

3. **� Review related concepts:**
   - [Azure Local Overview](azure-local-overview)
   - [Digital Sovereignty Fundamentals](digital-sovereignty)

4. **🌐 Explore external resources:**
   - [Azure Arc Documentation](https://learn.microsoft.com/azure/azure-arc/)
   - [Azure Arc Jumpstart](https://azurearcjumpstart.io/)
   - [Azure Arc Tech Community](https://techcommunity.microsoft.com/t5/azure-arc/bd-p/AzureArc)

5. **💡 Consider hands-on practice:**
   - Set up Arc-enabled servers in a lab
   - Deploy Arc-enabled Kubernetes cluster
   - Explore Arc Data Services

---

## Retake Policy

You may retake this assessment as many times as needed. We recommend:

- Reviewing missed topics before retaking
- Waiting at least 1 hour between attempts
- Reading explanations for all questions, not just missed ones
- Taking notes on key concepts

---

**Quiz Version:** 1.0  
**Last Updated:** October 2025  
**Questions:** 12  
**Passing Score:** 80%

---

**[← Back to Azure Arc Introduction](azure-arc-intro)**
