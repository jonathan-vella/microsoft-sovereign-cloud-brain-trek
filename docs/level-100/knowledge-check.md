---
layout: default
title: Knowledge Check
parent: Module 1 - Digital Sovereignty
nav_order: 6
---

# Level 100 Knowledge Check

{: .no_toc }

Test your understanding of Digital Sovereignty fundamentals with this knowledge check. This assessment covers concepts from all Level 100 modules.

---

## Instructions

- Answer all 15 questions
- No time limit - take as long as you need
- Answers are provided at the bottom of the page
- Aim for 80% (12/15) or higher to demonstrate mastery
- Review related content for any questions you miss

---

## Questions

### Question 1: Digital Sovereignty Basics

What is digital sovereignty?

A) The requirement to store data in a specific country  
B) The ability to control and govern digital assets within jurisdictional boundaries  
C) A type of cloud security certification  
D) A regulation specific to the European Union

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Digital sovereignty is broader than just data location. It encompasses control, governance, and independence over digital infrastructure and data within specific jurisdictional boundaries.

**Reference:** [Digital Sovereignty Overview](digital-sovereignty)
</details>

---

### Question 2: Microsoft Sovereign Cloud Models

Which of the following is NOT one of Microsoft's three sovereign cloud models?

A) Sovereign Public Cloud  
B) Sovereign Private Cloud  
C) Sovereign Regional Cloud  
D) National Partner Clouds

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: C**

**Explanation:**
Microsoft offers three sovereign cloud models: Sovereign Public Cloud (enhanced Azure with sovereignty controls), Sovereign Private Cloud (dedicated infrastructure), and National Partner Clouds (country-specific clouds operated by local partners). There is no "Sovereign Regional Cloud" model.

**Reference:** [Digital Sovereignty Overview](digital-sovereignty#sovereignty-spectrum)
</details>

---

### Question 3: Data Residency vs. Sovereignty

What is the difference between data residency and data sovereignty?

A) They mean the same thing  
B) Data residency is where data is stored; data sovereignty includes residency plus operational and legal control  
C) Data sovereignty is only about location; data residency includes access controls  
D) Data residency applies to public cloud; data sovereignty applies to private cloud

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Data residency focuses specifically on the geographic location where data is stored. Data sovereignty is broader, encompassing residency requirements plus who can access the data, how it's governed, operational controls, and legal jurisdiction.

**Reference:** [Data Residency Concepts](data-residency-concepts#key-definitions)
</details>

---

### Question 4: GDPR Requirements

Which of the following is TRUE about GDPR and data residency?

A) GDPR requires all data to be stored in the EU  
B) GDPR prohibits any data transfers outside the EU  
C) GDPR requires data minimization and allows international transfers with appropriate safeguards  
D) GDPR only applies to government organizations

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: C**

**Explanation:**
GDPR does not require data to be stored in the EU, but it does regulate how personal data can be transferred outside the EU/EEA. Transfers are allowed with appropriate safeguards such as adequacy decisions or Standard Contractual Clauses.

**Reference:** [Regulatory Overview - GDPR](regulatory-overview#gdpr-general-data-protection-regulation)
</details>

---

### Question 5: EU Data Boundary

What does Microsoft's EU Data Boundary commitment ensure?

A) No data ever leaves the EU under any circumstances  
B) Customer data is stored and processed within the EU with documented, limited exceptions  
C) All Microsoft employees must be based in the EU  
D) Only applies to Azure, not Microsoft 365

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
The EU Data Boundary commitment ensures customer data is stored and processed within the EU. There are some documented exceptions (like customer-initiated transfers or certain support scenarios with Customer Lockbox), but these are transparent and often under customer control.

**Reference:** [European Digital Commitments](european-commitments#eu-data-boundary-for-the-microsoft-cloud)
</details>

---

### Question 6: FedRAMP Impact Levels

What is the difference between FedRAMP Moderate and FedRAMP High?

A) Moderate is for public data; High is for internal government data  
B) Moderate is for internal government data; High is for national security information  
C) There is no difference in security requirements  
D) High requires more documentation but same security controls

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
FedRAMP has three impact levels based on the sensitivity of data:

- **Low:** Public information
- **Moderate:** Internal government information (most common)
- **High:** National security information (most stringent requirements)

**Reference:** [Regulatory Overview - FedRAMP](regulatory-overview#fedramp-federal-risk-and-authorization-management-program)
</details>

---

### Question 7: Azure Regions

How many Azure regions does Microsoft operate globally?

A) 20+  
B) 40+  
C) 60+  
D) 80+

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: C**

**Explanation:**
Microsoft Azure operates more than 60 regions globally, more than any other major cloud provider. This extensive footprint provides customers with more options for data residency and low-latency access.

**Reference:** [Data Residency Concepts](data-residency-concepts#azure-regions-and-data-residency)
</details>

---

### Question 8: Operational Sovereignty

What is operational sovereignty primarily concerned with?

A) Where data is stored geographically  
B) The cost of cloud operations  
C) Who can access and manage infrastructure and under what conditions  
D) The speed of data processing

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: C**

**Explanation:**
Operational sovereignty focuses on control over operations: who can access systems, where personnel are located, operational independence, and the ability to maintain control under various circumstances.

**Reference:** [Operational Sovereignty](operational-sovereignty#what-is-operational-sovereignty)
</details>

---

### Question 9: Azure Local Operating Modes

What is the key difference between Azure Local Connected and Disconnected modes?

A) Connected mode is faster  
B) Connected mode uses cloud control plane; Disconnected mode uses local control plane  
C) Disconnected mode is cheaper  
D) Connected mode doesn't support virtualization

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
The fundamental difference is the control plane location:

- **Connected Mode:** Managed via Azure portal and Azure Arc (cloud control plane)
- **Disconnected Mode:** Managed via local portal/Windows Admin Center (local control plane)

**Reference:** [Operational Sovereignty - Control Plane](operational-sovereignty#control-plane-connected-vs-disconnected)
</details>

---

### Question 10: Customer Lockbox

What is the purpose of Azure Customer Lockbox?

A) To encrypt customer data automatically  
B) To require customer approval before Microsoft support can access customer data  
C) To lock customer resources from accidental deletion  
D) To store encryption keys securely

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Customer Lockbox provides customers with explicit control over Microsoft support access to their data. Support personnel can only access customer data after the customer approves the request.

**Reference:** [Operational Sovereignty - Access Controls](operational-sovereignty#access-control-mechanisms)
</details>

---

### Question 11: Standard Contractual Clauses (SCCs)

What are Standard Contractual Clauses used for?

A) Pricing agreements with Microsoft  
B) Legally compliant data transfers from the EU to countries without adequacy decisions  
C) Defining service level agreements  
D) Contract templates for employee agreements

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Standard Contractual Clauses (SCCs) are EU Commission-approved contract templates that provide appropriate safeguards for international data transfers when transferring personal data from the EU to countries that don't have an adequacy decision.

**Reference:** [Data Residency Concepts - Data Transfers](data-residency-concepts#legal-mechanisms-for-transfers)
</details>

---

### Question 12: HIPAA Business Associate Agreement

What is required when using Azure for healthcare applications with PHI?

A) FedRAMP authorization  
B) A Business Associate Agreement (BAA) with Microsoft  
C) ITAR compliance  
D) PCI DSS certification

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
HIPAA requires that "Business Associates" (including cloud service providers) handling Protected Health Information (PHI) on behalf of covered entities sign a Business Associate Agreement. Microsoft provides BAAs for Azure services used with PHI.

**Reference:** [Regulatory Overview - HIPAA](regulatory-overview#hipaa-health-insurance-portability-and-accountability-act)
</details>

---

### Question 13: Azure Arc

What is the primary function of Azure Arc?

A) To provide network connectivity between on-premises and Azure  
B) To enable management of on-premises and multi-cloud resources from Azure control plane  
C) To encrypt data in transit  
D) To replace traditional VPNs

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Azure Arc extends the Azure control plane to enable unified management of resources regardless of where they're located—on-premises, at the edge, or in other clouds.

**Reference:** [Introduction - Azure Arc](../introduction#azure-arc)
</details>

---

### Question 14: Sovereignty Spectrum

Which scenario requires the HIGHEST level of sovereignty?

A) Public website hosting  
B) Internal business applications  
C) Regulated healthcare data  
D) Air-gapped classified defense systems

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: D**

**Explanation:**
Air-gapped classified defense systems require the maximum level of sovereignty: complete operational independence, no external connectivity, local control plane, US persons-only access, and physical isolation. This is Level 5 on the sovereignty spectrum.

**Reference:** [Operational Sovereignty - Spectrum](operational-sovereignty#level-5-air-gapped)
</details>

---

### Question 15: Schrems II Decision

What was the impact of the Schrems II decision?

A) It created GDPR  
B) It invalidated the EU-US Privacy Shield and increased scrutiny on data transfers to the US  
C) It prohibited all data transfers from the EU  
D) It eliminated the need for Standard Contractual Clauses

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
The Schrems II decision (July 2020) by the Court of Justice of the European Union invalidated the EU-US Privacy Shield framework. While Standard Contractual Clauses remain valid, the decision increased requirements for assessing and mitigating risks in international data transfers, particularly to the US.

**Reference:** [Data Residency Concepts - Schrems II](data-residency-concepts#schrems-ii-decision)
</details>

---

## Scoring Guide

**15/15 (100%):** Excellent! You have mastered Level 100 concepts.

**12-14/15 (80-93%):** Good work! You meet the success criteria for Level 100.

**9-11/15 (60-73%):** You understand the basics but should review some topics before proceeding to Level 200.

**Below 9/15 (< 60%):** Please review the Level 100 content and retake the quiz before moving to Level 200.

---

## What Did You Miss?

Review the explanations for any questions you answered incorrectly. Each answer includes a reference link to the relevant content section.

### Common Areas for Review

**If you missed questions 1-3:** Review [Digital Sovereignty fundamentals](digital-sovereignty)

**If you missed questions 4-7:** Review [Regulatory Overview](regulatory-overview) and [European Commitments](european-commitments)

**If you missed questions 8-10:** Review [Operational Sovereignty](operational-sovereignty)

**If you missed questions 11-12:** Review [Regulatory Overview](regulatory-overview)

**If you missed questions 13-15:** Review [Data Residency Concepts](data-residency-concepts)

---

## Next Steps

### If You Scored 80% or Higher ✅

**Congratulations!** You've successfully completed Level 100 - Foundational Concepts.

You're ready to proceed to:

- **[Level 200: Intermediate - Architecture & Pre-Sales](../level-200/)**

### If You Scored Below 80%

**Keep Learning!** Review the indicated sections and retake the quiz.

Focus on:

1. The explanations for questions you missed
2. Related content sections linked in each answer
3. Hands-on exploration of Azure portal and documentation

---

## Additional Practice

### Discussion Questions

Consider these questions to deepen your understanding:

1. How would you explain digital sovereignty to a non-technical executive?
2. What questions would you ask a customer to determine their sovereignty requirements?
3. How does operational sovereignty differ between healthcare and defense sectors?
4. What trade-offs exist between sovereignty and operational efficiency?
5. How would you position Azure's sovereignty capabilities against competitors?

### Hands-On Practice

To reinforce your learning:

1. **Explore Azure Regions:** Browse the [Azure geographies page](https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/) to understand regional options
2. **Review Compliance Offerings:** Visit the [Microsoft Trust Center](https://www.microsoft.com/en-us/trust-center) to explore certifications
3. **Watch Azure Local Videos:** Check out demos on the [Azure Local YouTube channel](https://www.youtube.com/@AzureStackHCI) (channel name pending rename)

---

## Feedback

How was this knowledge check? We'd love to hear your feedback:

- Were the questions clear and relevant?
- Was the difficulty appropriate for Level 100?
- Did the explanations help you understand the concepts better?
- What topics would you like more questions about?

Share your feedback through the repository's GitHub Issues.

---

## Retake the Quiz

Want to test yourself again? Refresh the page and try to answer all questions from memory before revealing the answers.

---

**Last Updated:** October 2025

---

**[Return to Level 100 Overview](README)** | **[Proceed to Level 200](../level-200/)**
