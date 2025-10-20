---
layout: default
title: Cloud Models Knowledge Check
parent: Level 100 - Foundation
nav_order: 2.4
---

# Cloud Models Knowledge Check
{: .no_toc }

Test your understanding of Microsoft's three sovereign cloud models with this comprehensive knowledge check.

---

## Instructions

- Answer all 15 questions
- No time limit - take as long as you need
- Answers are provided at the bottom of the page
- Aim for 80% (12/15) or higher to demonstrate mastery
- Review related content for any questions you miss

---

## Questions

### Question 1: Sovereign Cloud Models Overview

Which of the following is one of Microsoft's three sovereign cloud models?

A) Sovereign Hybrid Cloud  
B) Sovereign Private Cloud  
C) Sovereign Multi-Cloud  
D) Sovereign Edge Cloud

---

### Question 2: Model Selection Criteria

A European financial services company requires GDPR compliance, elastic scalability, and access to the latest Azure AI services. Which model is MOST appropriate?

A) Sovereign Public Cloud (Microsoft Cloud for Sovereignty)  
B) Sovereign Private Cloud (Azure Local Disconnected)  
C) National Partner Clouds (Azure Government)  
D) Traditional on-premises infrastructure

---

### Question 3: Microsoft Cloud for Sovereignty

What is the primary purpose of Microsoft Cloud for Sovereignty?

A) To provide physically isolated data centers in each country  
B) To enforce sovereignty requirements through policy-driven controls in Azure public cloud  
C) To replace Azure with a new sovereign-only cloud platform  
D) To eliminate the need for compliance certifications

---

### Question 4: Customer Lockbox

A healthcare organization wants to ensure that no Microsoft support engineer can access their patient data without explicit approval. Which feature should they enable?

A) Azure Policy  
B) Azure Firewall  
C) Customer Lockbox  
D) Azure Key Vault

---

### Question 5: Azure Local Operating Modes

What is the PRIMARY difference between Azure Local Connected Mode and Disconnected Mode?

A) Connected mode costs more  
B) Connected mode requires internet connectivity and uses cloud control plane; Disconnected mode operates independently  
C) Disconnected mode has better performance  
D) Connected mode supports more VMs

---

### Question 6: Air-Gapped Requirements

A defense contractor needs to run Azure services in a completely air-gapped environment with no internet connectivity. Which solution should they use?

A) Azure Government with ExpressRoute  
B) Sovereign Public Cloud with Azure Policy  
C) Azure Local Connected Mode  
D) Azure Local Disconnected Mode

---

### Question 7: National Partner Clouds - Azure Government

Which of the following is TRUE about Azure Government?

A) It is operated by a third-party partner, not Microsoft  
B) It is physically and logically separated from commercial Azure  
C) It has fewer compliance certifications than commercial Azure  
D) It is available to any organization worldwide

---

### Question 8: Azure China (21Vianet)

Why is Azure China operated by 21Vianet instead of Microsoft directly?

A) To reduce costs  
B) To meet Chinese regulatory requirements for local cloud operators  
C) Because Microsoft is not authorized to operate in China  
D) To improve performance

---

### Question 9: Confidential Computing

What does Azure Confidential Computing protect?

A) Data at rest only  
B) Data in transit only  
C) Data in use (during processing)  
D) Data after deletion

---

### Question 10: Model Comparison - Infrastructure

Which model provides dedicated, single-tenant physical infrastructure?

A) Sovereign Public Cloud  
B) Sovereign Private Cloud (Azure Local)  
C) National Partner Clouds  
D) All three models provide dedicated infrastructure

---

### Question 11: Azure Policy for Sovereignty

A company wants to automatically prevent any resources from being created outside the EU. What should they implement?

A) Azure Firewall rules  
B) Network Security Groups (NSGs)  
C) Azure Policy with deny effect for non-EU regions  
D) Customer Lockbox

---

### Question 12: FedRAMP High Authorization

A US federal agency requires FedRAMP High authorization for their cloud infrastructure. Which option is appropriate?

A) Azure commercial cloud (global)  
B) Azure Government  
C) Azure China  
D) Any Azure region with Policy enforcement

---

### Question 13: Use Case Identification

Which scenario is BEST suited for Sovereign Private Cloud (Azure Local Disconnected Mode)?

A) A retail company needing elastic scalability for seasonal traffic  
B) A startup building a mobile app  
C) An aerospace company with classified defense data requiring air-gap  
D) A SaaS provider serving global customers

---

### Question 14: Hybrid Sovereignty

A manufacturing company wants some workloads in Azure public cloud and others on-premises with unified management. What should they use?

A) Separate management tools for each environment  
B) Azure Arc to manage hybrid resources from Azure control plane  
C) Azure ExpressRoute only  
D) Two separate clouds with no integration

---

### Question 15: TCO Considerations

For which workload pattern is Sovereign Private Cloud (Azure Local) typically MOST cost-effective compared to public cloud?

A) Highly variable, unpredictable workloads  
B) Short-term projects (3-6 months)  
C) Steady-state workloads with consistent resource utilization  
D) Development and testing environments

---

## Answers

<details markdown="1">
<summary><strong>Click to reveal answers</strong></summary>

### Answer 1: B
**Correct:** Sovereign Private Cloud

**Explanation:** Microsoft's three sovereign cloud models are:
1. **Sovereign Public Cloud** - Azure with enhanced sovereignty controls
2. **Sovereign Private Cloud** - Dedicated infrastructure via Azure Local
3. **National Partner Clouds** - Partner-operated clouds (Azure Government, Azure China)

Sovereign Hybrid Cloud, Multi-Cloud, and Edge Cloud are not official Microsoft sovereign cloud model names.

**Review:** [Microsoft Sovereign Cloud Models Overview](sovereign-cloud-models.html#the-three-sovereign-cloud-models)

---

### Answer 2: A
**Correct:** Sovereign Public Cloud (Microsoft Cloud for Sovereignty)

**Explanation:** For GDPR compliance with needs for elastic scalability and latest Azure services, Sovereign Public Cloud is ideal because:
- ✅ Provides GDPR compliance with EU Data Boundary
- ✅ Offers full portfolio of Azure services (200+) including latest AI/ML
- ✅ Provides elastic scalability with pay-as-you-go pricing
- ✅ Uses policy-driven controls to enforce sovereignty requirements

Sovereign Private Cloud (Azure Local Disconnected) would be overkill and lack elasticity. Azure Government is for US government customers, not European financial services.

**Review:** [Sovereign Public Cloud Use Cases](sovereign-public-cloud.html#use-cases-and-customer-scenarios)

---

### Answer 3: B
**Correct:** To enforce sovereignty requirements through policy-driven controls in Azure public cloud

**Explanation:** Microsoft Cloud for Sovereignty is NOT a separate cloud platform. It's a set of capabilities, policies, and configurations that run on top of Azure public cloud to enforce sovereignty requirements automatically through Azure Policy and other controls. This allows customers to get all Azure benefits while meeting sovereignty needs.

**Review:** [Microsoft Cloud for Sovereignty](sovereign-public-cloud.html#microsoft-cloud-for-sovereignty)

---

### Answer 4: C
**Correct:** Customer Lockbox

**Explanation:** Customer Lockbox requires customer approval before Microsoft support engineers can access customer data. This provides:
- Customer control over support access
- Audit trail of all access requests
- Time-limited access with automatic expiration
- No access granted without explicit customer approval

Azure Policy enforces compliance, Azure Firewall controls network traffic, and Azure Key Vault stores encryption keys - none provide support access approval.

**Review:** [Customer Lockbox](sovereign-public-cloud.html#2-customer-lockbox)

---

### Answer 5: B
**Correct:** Connected mode requires internet connectivity and uses cloud control plane; Disconnected mode operates independently

**Explanation:** 
- **Connected Mode:** Requires ongoing internet connectivity to Azure, uses Azure portal for management, provides hybrid services
- **Disconnected Mode:** No internet required, uses local control plane (Windows Admin Center), operates independently

The key difference is the dependency on Azure connectivity and where the control plane resides (cloud vs. local).

**Review:** [Operating Modes Comparison](sovereign-private-cloud.html#operating-modes-connected-vs-disconnected)

---

### Answer 6: D
**Correct:** Azure Local Disconnected Mode

**Explanation:** For completely air-gapped environments (no internet connectivity), Azure Local Disconnected Mode is the only option that:
- ✅ Operates without any internet connectivity
- ✅ Uses local control plane (no cloud dependencies)
- ✅ Provides Azure-consistent services on-premises
- ✅ Supports completely isolated operations

Azure Government still requires internet connectivity. Connected Mode by definition needs connectivity. Sovereign Public Cloud requires cloud connection.

**Review:** [Azure Local Disconnected Mode](sovereign-private-cloud.html#disconnected-mode-air-gapped)

---

### Answer 7: B
**Correct:** It is physically and logically separated from commercial Azure

**Explanation:** Azure Government is:
- ✅ Operated by Microsoft (not a third-party partner)
- ✅ Physically separate data centers from commercial Azure
- ✅ Logically isolated network infrastructure
- ✅ Has MORE compliance certifications than commercial (FedRAMP High, DoD IL6)
- ✅ Available only to US government entities and partners (not worldwide)

**Review:** [Azure Government Overview](national-partner-clouds.html#1-azure-government-united-states)

---

### Answer 8: B
**Correct:** To meet Chinese regulatory requirements for local cloud operators

**Explanation:** China's Cybersecurity Law requires that cloud services in China be operated by Chinese companies with local data storage. 21Vianet is a licensed Chinese telecommunications provider that operates Azure China to comply with these regulations. Microsoft provides the technology and support to 21Vianet, but 21Vianet handles operations, billing, and customer support.

**Review:** [Azure China (21Vianet)](national-partner-clouds.html#2-azure-china-21vianet-operated)

---

### Answer 9: C
**Correct:** Data in use (during processing)

**Explanation:** Azure Confidential Computing protects data **while it's being processed** using hardware-based Trusted Execution Environments (TEEs). This completes the encryption story:
- **Data at Rest:** Azure Storage Encryption, Azure Disk Encryption
- **Data in Transit:** TLS/SSL encryption
- **Data in Use:** Confidential Computing (Intel SGX, AMD SEV-SNP)

This protects against cloud provider access, privileged admins, and hardware attacks.

**Review:** [Confidential Computing](sovereign-public-cloud.html#4-confidential-computing)

---

### Answer 10: B
**Correct:** Sovereign Private Cloud (Azure Local)

**Explanation:** Infrastructure types by model:
- **Sovereign Public Cloud:** Shared infrastructure with logical isolation
- **Sovereign Private Cloud (Azure Local):** Dedicated, single-tenant physical infrastructure
- **National Partner Clouds:** Shared infrastructure (partner-operated)

Only Sovereign Private Cloud provides dedicated physical hardware exclusively for one customer.

**Review:** [Model Comparison Matrix](sovereign-cloud-models.html#model-comparison-matrix)

---

### Answer 11: C
**Correct:** Azure Policy with deny effect for non-EU regions

**Explanation:** Azure Policy with a "deny" effect is the correct approach to prevent resource creation outside allowed regions. The policy evaluates resource creation requests and denies any that don't match the specified EU regions.

Example policy:
```json
{
  "if": {
    "not": {
      "field": "location",
      "in": ["westeurope", "northeurope", "francecentral"]
    }
  },
  "then": {
    "effect": "deny"
  }
}
```

Azure Firewall controls network traffic, NSGs control subnet traffic, and Customer Lockbox controls support access - none prevent resource creation in specific regions.

**Review:** [Azure Policy for Compliance](sovereign-public-cloud.html#3-azure-policy-for-compliance-automation)

---

### Answer 12: B
**Correct:** Azure Government

**Explanation:** Azure Government is specifically designed for US government workloads and is the only Microsoft cloud with:
- FedRAMP High authorization
- DoD Impact Level 5 and 6 authorization
- Physical and logical separation from commercial cloud
- US persons-only support

Azure commercial cloud (global) has FedRAMP Moderate only. Azure China is for Chinese operations. Policy enforcement alone doesn't provide FedRAMP authorization.

**Review:** [Azure Government Compliance](national-partner-clouds.html#1-azure-government-united-states)

---

### Answer 13: C
**Correct:** An aerospace company with classified defense data requiring air-gap

**Explanation:** Azure Local Disconnected Mode is specifically designed for:
- Air-gapped environments (no internet)
- Classified or highly sensitive data
- Defense and intelligence scenarios
- Complete operational independence

Scenario analysis:
- Retail with elastic needs: Sovereign Public Cloud (elasticity needed)
- Startup mobile app: Sovereign Public Cloud or commercial cloud (need scalability)
- Aerospace with classified data: Sovereign Private Cloud Disconnected (air-gap required)
- SaaS provider: Sovereign Public Cloud (global reach and scalability)

**Review:** [Use Cases - Defense Contractor](sovereign-private-cloud.html#scenario-1-defense-contractor---classified-workloads)

---

### Answer 14: B
**Correct:** Azure Arc to manage hybrid resources from Azure control plane

**Explanation:** Azure Arc provides unified management for hybrid and multi-cloud environments by:
- Projecting on-premises and multi-cloud resources into Azure Resource Manager
- Enabling Azure management tools (portal, CLI, ARM templates) for all resources
- Applying Azure Policy across hybrid resources
- Providing unified monitoring via Azure Monitor

This provides a single control plane for managing resources across cloud and on-premises, which is essential for hybrid sovereignty scenarios.

**Review:** [Hybrid Architecture Scenarios](sovereign-private-cloud.html#scenario-3-healthcare---rural-hospital-network)

---

### Answer 15: C
**Correct:** Steady-state workloads with consistent resource utilization

**Explanation:** Azure Local (Sovereign Private Cloud) TCO considerations:

**When cost-effective:**
- ✅ Steady-state workloads (consistent utilization amortizes CapEx)
- ✅ Long-term deployment (3-5 years to recover hardware investment)
- ✅ Data gravity (large datasets, high I/O, expensive to move)
- ✅ Latency requirements (can't tolerate cloud latency)

**When NOT cost-effective:**
- ❌ Variable/unpredictable workloads (cloud elasticity more economical)
- ❌ Short-term projects (can't amortize CapEx over short period)
- ❌ Dev/test environments (cloud pay-as-you-go better)

**Review:** [Total Cost of Ownership](sovereign-private-cloud.html#total-cost-of-ownership-tco)

---

## Scoring Guide

- **13-15 correct (87-100%):** Excellent! You have mastered sovereign cloud models.
- **12 correct (80%):** Good job! You meet the mastery threshold.
- **10-11 correct (67-73%):** Review the topics you missed and retake the quiz.
- **Below 10 correct (<67%):** Review all three sovereign cloud model pages before retaking.

---

## Study Recommendations Based on Score

### If you missed questions 1-3 (Overview and Model Selection)
**Review:** [Microsoft Sovereign Cloud Models Overview](sovereign-cloud-models.html)
- Focus on the three model definitions
- Study the decision framework
- Review customer scenarios

### If you missed questions 4-9 (Sovereign Public Cloud)
**Review:** [Sovereign Public Cloud](sovereign-public-cloud.html)
- Focus on Microsoft Cloud for Sovereignty
- Study Customer Lockbox, Azure Policy, Confidential Computing
- Review implementation best practices

### If you missed questions 10-13 (Sovereign Private Cloud)
**Review:** [Sovereign Private Cloud](sovereign-private-cloud.html)
- Focus on Azure Local architecture
- Study Connected vs. Disconnected modes
- Review use cases and TCO analysis

### If you missed questions 12-15 (National Partner Clouds)
**Review:** [National Partner Clouds](national-partner-clouds.html)
- Focus on Azure Government and Azure China
- Study compliance certifications
- Review onboarding processes

---

## Next Steps

After achieving mastery (80%+):

1. ✅ **Review any missed questions** - Understand why the correct answer is right
2. ✅ **Explore deep dive content** - Read the detailed pages for each model
3. 🎯 **[Proceed to Module 3: Azure Local Overview →](azure-local-overview.html)**
4. 🎯 **[Return to Level 100 Overview →](README.html)**

---

## Additional Resources

- **[Microsoft Cloud for Sovereignty](https://learn.microsoft.com/en-us/industry/sovereign-cloud/)** - Official documentation
- **[Azure Local overview](https://learn.microsoft.com/en-us/azure/azure-local/overview)** - Product documentation
- **[Azure Government documentation](https://learn.microsoft.com/en-us/azure/azure-government/)** - Government cloud guide
- **[Azure China documentation](https://learn.microsoft.com/en-us/azure/china/)** - China cloud guide

---

</details>

**Last Updated:** October 2025
