---
layout: default
title: Azure Local Knowledge Check
parent: Module 3 - Azure Local Overview
nav_order: 3.5
---

# Azure Local Knowledge Check

{: .no_toc }

Test your understanding of Azure Local concepts, deployment modes, architecture, and use cases.

---

## Quiz Instructions

- **Total Questions:** 15
- **Passing Score:** 80% (12 of 15 correct)
- **Time Estimate:** 15-20 minutes
- **Format:** Multiple choice (A/B/C/D)

**Tips:**

- Read each question carefully
- Consider real-world scenarios
- Review module content if unsure
- Check your answers against explanations below

---

## Questions

### Question 1: Fundamental Concepts

**What is the primary difference between Azure Local and running workloads only in Azure public cloud?**

A) Azure Local is faster for all workloads  
B) Azure Local provides physical control and can operate without continuous cloud connectivity  
C) Azure Local is less expensive for all scenarios  
D) Azure Local does not support virtual machines

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
The primary difference is that Azure Local provides physical control over infrastructure and can operate without continuous cloud connectivity (especially in Disconnected Mode). While Azure Local may offer performance or cost benefits for specific workloads, the key differentiator is sovereignty, control, and the ability to operate independently of the cloud. Azure Local fully supports VMs and many other workloads.

**Reference:** [Azure Local Overview](azure-local-overview#what-is-azure-local)
</details>

---

### Question 2: Connected vs. Disconnected Mode

**Which scenario is the BEST fit for Azure Local in Disconnected Mode?**

A) A retail chain wanting centralized monitoring across 100 locations  
B) A defense agency processing classified information in an air-gapped environment  
C) A healthcare provider needing Azure Backup for disaster recovery  
D) A financial services company wanting to use Azure Machine Learning

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Disconnected Mode is specifically designed for air-gapped environments where data cannot leave the premises and no cloud connectivity is allowed. This is ideal for classified government work, defense agencies, and highly sensitive environments. The other scenarios would benefit from Connected Mode: retail needs centralized monitoring, healthcare wants cloud backup, and financial services wants ML integration - all requiring Azure connectivity.

**Reference:** [Disconnected Mode Operations](azure-local-disconnected-mode#when-disconnected-mode-is-necessary)
</details>

---

### Question 3: Data Sovereignty

**In Azure Local Connected Mode, what type of data is synchronized to Azure?**

A) All VM disk data and application data  
B) Only metadata, metrics, logs, and configuration - not workload data  
C) Only user credentials and passwords  
D) All data including backups is automatically sent to Azure

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Even in Connected Mode, workload data (VM disks, application data, databases) stays on-premises. Only metadata (VM names, states, sizes), performance metrics, event logs, and configuration information is synchronized to Azure. This enables cloud-based management while maintaining data sovereignty. Credentials are not sent, and backups only go to Azure if explicitly configured by the customer.

**Reference:** [Connected Mode Operations](azure-local-connected-mode#data-sovereignty-in-connected-mode)
</details>

---

### Question 4: Hardware Requirements

**What is the MINIMUM production-recommended configuration for an Azure Local cluster?**

A) 1 node with 8 cores and 128 GB RAM  
B) 2 nodes with 16+ cores and 384+ GB RAM each, RDMA-capable networking  
C) 4 nodes with 32 cores and 1 TB RAM each  
D) 8 nodes with dedicated storage array

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
The production-recommended minimum is 2 nodes (for high availability) with 16+ cores and 384+ GB RAM per node, along with RDMA-capable networking (25 GbE or faster) for Storage Spaces Direct. While 1 node can work for testing, it provides no redundancy. While 4+ nodes offer better performance and lower overhead, 2 nodes is the minimum for production HA. External storage arrays are not required as Azure Local uses Storage Spaces Direct.

**Reference:** [Hardware Requirements](azure-local-hardware#minimum-vs-recommended-specifications)
</details>

---

### Question 5: Architecture

**In Azure Local architecture, where does the data plane operate?**

A) In Azure cloud exclusively  
B) Always locally on Azure Local hardware, even in Connected Mode  
C) Split between on-premises and Azure  
D) In Azure during backups, local otherwise

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
The data plane (VM workloads, storage I/O, network traffic) ALWAYS operates locally on Azure Local hardware, regardless of deployment mode (Connected or Disconnected). This ensures data sovereignty and low latency. Only the control plane functions (management, monitoring, policies) may leverage Azure in Connected Mode. The data plane never depends on Azure connectivity.

**Reference:** [Architecture Deep Dive](azure-local-architecture#control-plane-vs-data-plane-separation)
</details>

---

### Question 6: Networking

**Why is RDMA (Remote Direct Memory Access) critical for Azure Local storage performance?**

A) It enables internet connectivity  
B) It reduces CPU utilization and achieves sub-millisecond latency for storage traffic  
C) It's required for VM networking  
D) It encrypts data in transit

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
RDMA is critical for Storage Spaces Direct because it reduces CPU utilization for storage traffic and achieves sub-millisecond latency between nodes. This is essential for optimal storage performance in hyper-converged infrastructure. RDMA is not related to internet connectivity, VM networking uses standard networking, and encryption is handled by SMB 3.x.

**Reference:** [Network Architecture](azure-local-architecture#rdma-remote-direct-memory-access)
</details>

---

### Question 7: Deployment Modes

**What is required for Azure Local to operate in Connected Mode?**

A) Continuous 24/7 internet connectivity with zero tolerance for outages  
B) Intermittent outbound HTTPS connectivity to Azure services (resilient to temporary outages)  
C) Inbound connections from the internet  
D) A dedicated Azure ExpressRoute circuit

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Connected Mode requires intermittent outbound HTTPS (TCP 443) connectivity to Azure services, but it is resilient to temporary outages (hours to days). Continuous 24/7 connectivity is not required. No inbound connections from the internet are needed. While ExpressRoute is recommended for large deployments, it's not required - standard internet connectivity works fine.

**Reference:** [Connected Mode Prerequisites](azure-local-connected-mode#prerequisites-and-connectivity-requirements)
</details>

---

### Question 8: Use Case Selection

**A hospital network needs to run EMR systems with low latency, meet HIPAA requirements, and wants cloud-based backup for disaster recovery. Which solution is best?**

A) Pure Azure public cloud  
B) Azure Local in Disconnected Mode  
C) Azure Local in Connected Mode  
D) On-premises infrastructure without Azure

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: C**

**Explanation:**
Azure Local in Connected Mode is ideal for this scenario because it provides: 1) Low latency for EMR systems (local processing), 2) HIPAA compliance through data residency (data stays on-premises), and 3) Azure Backup integration for cloud-based DR. Pure Azure cloud wouldn't provide the same low latency, Disconnected Mode wouldn't enable cloud backup, and traditional on-premises without Azure wouldn't provide modern cloud-based DR capabilities.

**Reference:** [Customer Scenarios](azure-local-overview#scenario-2-hospital-network-with-hipaa-compliance-connected-mode)
</details>

---

### Question 9: Storage Configuration

**What resiliency option provides the best storage efficiency but still tolerates one disk/node failure in Azure Local?**

A) Three-way mirror (33% efficiency)  
B) Two-way mirror (50% efficiency)  
C) Erasure coding/Parity (50-80% efficiency)  
D) Single disk (100% efficiency, no redundancy)

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Two-way mirror provides 50% storage efficiency while tolerating one disk/node failure, making it the best balance for this requirement. Three-way mirror is more resilient (2 failures) but less efficient (33%). Erasure coding can be more efficient (50-80%) but has higher CPU overhead and more complex rebuild. Single disk provides no redundancy and would not tolerate any failures.

**Reference:** [Storage Resiliency](azure-local-architecture#storage-resiliency)
</details>

---

### Question 10: Updates and Patching

**How does Cluster-Aware Updating (CAU) work in Azure Local?**

A) All nodes are updated simultaneously for speed  
B) Nodes are updated one at a time with VM migration, validation after each node  
C) Updates require complete cluster downtime  
D) Updates can only be applied monthly

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Cluster-Aware Updating (CAU) updates nodes one at a time: it drains VMs from a node (live migrating them to other nodes), applies updates, reboots the node, validates health, and then moves to the next node. This approach provides zero VM downtime (with 2+ nodes) and validates each step. Simultaneous updates would cause downtime, and updates can be applied on any schedule (though monthly is common).

**Reference:** [Update Procedures](azure-local-connected-mode#cluster-aware-updating-cau)
</details>

---

### Question 11: Security

**Which security feature in Azure Local is enabled by default to protect data at rest?**

A) Azure Security Center  
B) BitLocker drive encryption  
C) Network encryption with IPsec  
D) Azure Policy enforcement

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
BitLocker drive encryption is enabled by default on all Azure Local volumes, providing encryption at rest using AES-256 with TPM-protected keys. Azure Security Center is available in Connected Mode but requires configuration. IPsec is optional (not default) for network encryption. Azure Policy is only available in Connected Mode and requires setup.

**Reference:** [Security Layers](azure-local-architecture#encryption-at-rest)
</details>

---

### Question 12: Cost Considerations

**For which type of workload does Azure Local typically provide the fastest ROI vs. public cloud?**

A) Short-term development and testing (1-2 months)  
B) Sporadic batch processing (few hours per month)  
C) 24/7 production workloads running continuously for years  
D) Unpredictable bursting workloads

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: C**

**Explanation:**
Azure Local provides fastest ROI for 24/7 production workloads running continuously, typically breaking even in 2-3 years. For short-term or sporadic workloads, public cloud's OpEx model is more cost-effective. For bursting workloads, cloud provides better elasticity. Azure Local's CapEx investment is amortized best over consistent, long-running workloads with predictable capacity needs.

**Reference:** [Cost Considerations](azure-local-overview#cost-considerations)
</details>

---

### Question 13: Management in Disconnected Mode

**What is the primary management tool for Azure Local in Disconnected Mode?**

A) Azure portal  
B) Azure Arc  
C) Windows Admin Center (local)  
D) Azure Monitor

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: C**

**Explanation:**
Windows Admin Center (installed locally) is the primary management tool for Disconnected Mode since there is no Azure connectivity. Azure portal and Azure Arc require cloud connectivity and are not available in Disconnected Mode. Azure Monitor is also not available without cloud connectivity. PowerShell is also available for automation in Disconnected Mode.

**Reference:** [Management Without Cloud Connection](azure-local-disconnected-mode#windows-admin-center)
</details>

---

### Question 14: Hardware Topology

**For a 4-node Azure Local cluster using two-way mirroring, what percentage of capacity is available for use?**

A) 100% (all capacity usable)  
B) 75% (25% overhead)  
C) 50% (two copies of data)  
D) 33% (three copies of data)

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: C**

**Explanation:**
Two-way mirroring stores two copies of all data for redundancy, resulting in 50% storage efficiency. If you have 160 TB of raw storage, you get 80 TB usable. The number of nodes doesn't directly affect this efficiency - it's determined by the resiliency setting. Three-way mirror would give 33% efficiency (three copies), and erasure coding could provide better efficiency (50-80%) with some performance tradeoffs.

**Reference:** [Storage Sizing](azure-local-hardware#storage-sizing-formula)
</details>

---

### Question 15: High Availability

**A 3-node Azure Local cluster experiences a complete failure of one node. What happens to the VMs running on that node?**

A) VMs are permanently lost and must be restored from backup  
B) VMs automatically restart on the remaining 2 healthy nodes  
C) The entire cluster shuts down  
D) VMs remain offline until the failed node is replaced

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
When a node fails, the cluster's high availability mechanisms automatically restart the VMs from that node on the remaining healthy nodes. No data is lost because Storage Spaces Direct maintains replicas on other nodes (with two-way or three-way mirroring). The cluster continues operating with reduced capacity until the failed node is replaced. This is a core benefit of multi-node clusters with proper resiliency settings.

**Reference:** [High Availability Design](azure-local-architecture#high-availability-design)
</details>

---

## Scoring Guide

**Calculate your score:**

- Count the number of correct answers
- Divide by 15 and multiply by 100 for percentage

**Score Interpretation:**

**12-15 correct (80-100%):** ✅ **Excellent!** You have a strong understanding of Azure Local concepts.

- Ready to proceed to next module
- Consider reviewing missed questions for completeness

**9-11 correct (60-79%):** ⚠️ **Good progress, but review needed**

- Review the module content, especially areas where you missed questions
- Pay attention to differences between Connected and Disconnected modes
- Revisit hardware requirements and architecture concepts
- Retake quiz after review

**6-8 correct (40-59%):** ❌ **More study required**

- Thoroughly review all module content
- Focus on core concepts: deployment modes, data sovereignty, architecture
- Review customer scenarios to understand real-world applications
- Consider hands-on lab work if available
- Retake quiz after comprehensive review

**0-5 correct (0-39%):** ❌ **Significant review needed**

- Start from the beginning with [Azure Local Overview](azure-local-overview)
- Read each sub-page carefully
- Take notes on key concepts
- Review all customer scenarios
- Consider additional Microsoft Learn resources
- Retake quiz only after thorough review

---

## Study Recommendations by Topic

**If you missed questions on deployment modes (Q2, Q7):**

- Review [Connected Mode Operations](azure-local-connected-mode)
- Review [Disconnected Mode Operations](azure-local-disconnected-mode)
- Focus on when to use each mode

**If you missed questions on data sovereignty (Q3, Q5):**

- Review [Data Sovereignty in Connected Mode](azure-local-connected-mode#data-sovereignty-in-connected-mode)
- Review [Control Plane vs Data Plane](azure-local-architecture#control-plane-vs-data-plane-separation)

**If you missed questions on hardware (Q4, Q6, Q14):**

- Review [Hardware Requirements](azure-local-hardware)
- Review [Network Architecture](azure-local-architecture#network-architecture)
- Review [Storage Resiliency](azure-local-architecture#storage-resiliency)

**If you missed questions on use cases (Q8):**

- Review all [Customer Scenarios](azure-local-overview#customer-scenarios)
- Consider real-world business requirements

**If you missed questions on operations (Q10, Q11, Q13, Q15):**

- Review [Update Procedures](azure-local-connected-mode#update-and-patching-procedures)
- Review [Security Layers](azure-local-architecture#security-layers-and-encryption)
- Review [High Availability](azure-local-architecture#high-availability-design)

---

## Next Steps

**After completing this assessment:**

1. **✅ Celebrate your achievement!** You've completed Azure Local foundational concepts.

2. **📚 Continue to next module:**
   - [Azure Arc Introduction →](azure-arc-intro)

3. **🔗 Review related concepts:**
   - [Digital Sovereignty Fundamentals](digital-sovereignty)
   - [Microsoft Sovereign Cloud Models](sovereign-cloud-models)

4. **🌐 Explore external resources:**
   - [Azure Local Documentation](https://learn.microsoft.com/en-us/azure/azure-local/?view=azloc-2509)
   - [Azure Local Tech Community](https://techcommunity.microsoft.com/t5/azure-local/ct-p/AzureLocal)

5. **💡 Consider hands-on practice:**
   - Set up Azure Local in a lab environment
   - Explore Windows Admin Center
   - Practice cluster operations

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
**Questions:** 15  
**Passing Score:** 80%

---

**[← Back to Azure Local Overview](azure-local-overview)**
