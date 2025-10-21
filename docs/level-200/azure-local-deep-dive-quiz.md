---
layout: default
title: Knowledge Check - Azure Local Deep Dive
parent: Azure Local Architecture Deep Dive
grand_parent: Level 200 - Intermediate
nav_order: 4
---

# Knowledge Check - Azure Local Architecture Deep Dive

> **📊 Visual References:**
> - **Asset 21** - Advanced Networking Architecture (referenced in networking questions)
> - **Asset 22** - High-Availability Architecture (referenced in HA/failover questions)
> - **Asset 23** - Hardware Planning Decision Tree (referenced in hardware selection questions)
> 
> See docs/assets/images/README.md for complete asset specifications.

Test your understanding of advanced Azure Local architecture concepts. These scenario-based questions help verify your readiness for production deployments.

## Questions

### Question 1: System Architecture
**A large enterprise is designing a 3-node Azure Local cluster for production use. They need to understand the complete architecture layers. Which statement best describes the relationship between the four architecture layers?**

A) The management layer sits above the virtualization layer, which sits above the software layer, which sits above the hardware layer, creating a complete stack where all layers must be healthy for any workload to function.

B) The hardware layer provides the foundation, virtualization runs on hardware, the software layer orchestrates virtualization, and the management layer provides operational tools - each layer is somewhat independent and can fail separately without affecting other layers.

C) The management layer is most critical, followed by software layer, then virtualization, then hardware - they form a hierarchy of importance rather than technical layers.

D) All layers are integrated into a single unified system with no distinct separation between hardware, virtualization, software, and management.

**Correct Answer: B**

**Explanation:** Azure Local uses a layered architecture where each layer provides specific functions. The hardware layer provides CPU, memory, storage, and network. The virtualization layer (Hyper-V) runs on hardware and provides VM isolation. The software layer (Azure Local system services) orchestrates storage and compute. The management layer provides operational tools. While all layers need to work together for optimal function, they can fail independently - for example, Azure Local services can be restarted without requiring hardware replacement.

---

### Question 2: Network Design
**You're configuring networking for a 3-node cluster with 25 Gbps adapters using converged networking. What is the primary advantage of using VLANs with converged networking instead of separate physical adapters for each network type?**

A) VLANs eliminate network latency entirely, making all networks perform like dedicated physical connections.

B) VLANs allow logical network segmentation on fewer physical adapters, reducing hardware costs and complexity while maintaining traffic isolation through priority policies.

C) VLANs provide automatic redundancy, so if one physical adapter fails, all networks automatically switch to a backup adapter.

D) VLANs guarantee that storage traffic always has higher performance than customer workload traffic without additional configuration.

**Correct Answer: B**

**Explanation:** Converged networking uses VLANs to separate multiple logical networks over fewer physical adapters. This reduces hardware costs, rack space, and cable complexity. However, VLAN isolation is logical, not physical - QoS policies must be configured to ensure storage traffic priority. A single physical adapter failure can affect all networks if not properly teamed.

---

### Question 3: Storage Architecture
**In your 3-node Azure Local cluster with 3-way mirroring, a single SSD drive fails. The cluster begins automatic rebuild. During the rebuild process, what is the status of data redundancy and how should you respond?**

A) Data redundancy is maintained at 3-way mirror level because two other copies exist - continue normal operations and monitor the rebuild progress.

B) Data redundancy is degraded to 2-way mirror - the cluster can only tolerate one more failure, so you should stop all workloads until rebuild completes.

C) Data redundancy is completely lost because one drive failed - you must restore from backup immediately.

D) Data redundancy cycles between 3-way and 2-way during rebuild, so you cannot determine the true resilience until rebuild completes.

**Correct Answer: B**

**Explanation:** With 3-way mirroring and one drive failed, data exists on exactly 2 copies (the rebuild is happening in real-time, but the third copy is not yet complete). This means the cluster can only tolerate one more failure before data loss. This is a degraded mode and requires monitoring. You should avoid performing maintenance on other nodes during this period, but normal operations can continue.

---

### Question 4: Hardware Planning
**You're sizing hardware for a cluster that will run database workloads with high memory requirements. The customer has a 2-node cluster and wants to maximize usable memory per node. What is the most important consideration when selecting memory configuration?**

A) Choose the highest frequency DDR5 memory available to ensure maximum speed.

B) Populate all DIMM slots symmetrically with identical memory to ensure NUMA performance and proper quorum witness configuration for 2-node clusters.

C) Use a mix of DDR4 and DDR5 memory to provide redundancy - if one type fails, you have the other.

D) Maximize memory size by using the largest capacity DIMMs available, even if they don't fill all slots symmetrically.

**Correct Answer: B**

**Explanation:** Symmetric memory population ensures optimal NUMA performance (local memory access is faster than remote). DDR4 and DDR5 shouldn't be mixed (different speeds and timing). Larger capacity DIMMs are fine, but they must be populated symmetrically. For 2-node clusters, this also simplifies witness configuration and management.

---

### Question 5: Deployment Patterns
**Your company has two locations 500 miles apart connected by a 1 Gbps link. They want high availability for critical workloads. Which deployment pattern best balances resilience with bandwidth efficiency?**

A) Single 3-node cluster at location A, with location B as a POC-sized single-node cluster for testing only.

B) Two 2-node clusters (one at each location) with asynchronous replication between sites and file share witness at a third location.

C) One large 6-node cluster distributed across both locations (3 nodes each) with synchronous storage replication.

D) Single-node clusters at each location, each operating independently with nightly backups to the other location.

**Correct Answer: B**

**Explanation:** With limited 1 Gbps bandwidth, synchronous replication (Option C) would be problematic - storage rebuild alone can saturate the link. Two 2-node clusters with asynchronous replication provides good resilience while respecting bandwidth constraints. Each site has its own quorum (via file share witness), so they can operate independently. This provides geographic redundancy without excessive WAN utilization.

---

### Question 6: HA Quorum
**A 2-node Azure Local cluster loses connectivity between nodes due to a network partition. What happens next, and why?**

A) Both nodes automatically stop all services and refuse to operate, ensuring no split-brain scenario occurs.

B) Whichever node has the file share witness connection continues operating; the other node stops. This prevents split-brain because only one partition can achieve quorum.

C) The node with more VMs continues; the other stops. This balances workload distribution.

D) Random node selection decides which continues - Azure Local automatically picks one to prevent ties.

**Correct Answer: B**

**Explanation:** In a 2-node cluster, neither node has quorum by itself (needs 2/2). The file share witness acts as tiebreaker - whichever node can reach the witness achieves quorum and continues. The isolated node stops to prevent split-brain. This is why witness placement is critical for 2-node deployments.

---

### Question 7: Failure Recovery
**You manage a 3-node cluster when node 2 suddenly fails. Based on typical failure detection and recovery, approximately how long before all VMs are running on the survivor nodes?**

A) 30 seconds - Azure Local detects failures and migrates VMs nearly instantaneously.

B) 2-5 minutes - detection, cluster decisions, VM restart, and OS boot take time, but the process is largely automatic.

C) 15-30 minutes - requires manual intervention to isolate the failed node and decide on recovery strategy.

D) 1-2 hours - the storage rebuild must complete before VMs can resume.

**Correct Answer: B**

**Explanation:** Failure detection takes 5-30 seconds, cluster decision/orchestration adds 5 seconds, VM restart/OS boot takes 2-3 minutes. The process is largely automatic. Storage rebuild happens in parallel and is not blocking for VM operation, though performance will be degraded.

---

### Question 8: Capacity Planning
**For a 3-node cluster with 2 TB usable storage capacity (3-way mirror), a customer wants to allocate storage for three tiers: critical production (1 TB required), secondary workload (500 GB), and development (remaining). What is the issue with this plan?**

A) The allocation is fine - 1 TB + 500 GB + 500 GB = 2 TB total capacity.

B) Development tier will only have 500 GB, which is too small to be useful.

C) The plan doesn't account for rebuild overheads - during a node failure, rebuild requires temporary extra capacity, so allocating all capacity leaves no safety margin.

D) Three tiers are too many for one storage pool - use multiple pools instead.

**Correct Answer: C**

**Explanation:** With 3-way mirroring at full capacity (2 TB), a node failure requires rebuild but there's no extra capacity to write the rebuilding data. This creates risk. Best practice is to allocate only 70-80% of capacity and reserve 20-30% for rebuild overhead and spike capacity needs.

---

### Question 9: Network Optimization
**You've enabled RDMA on the storage network and configured QoS policies. Testing shows storage performance is 40% lower than expected. What is the most likely cause?**

A) RDMA isn't working - reboot all nodes to reset the RDMA stack.

B) Network congestion from customer workload traffic sharing the same physical adapter - verify QoS policies are correctly configured and prioritizing storage traffic.

C) RDMA is too much overhead - disable it to get faster TCP/IP performance.

D) The physical switch doesn't support RDMA speeds - replace the switch with a higher-speed model.

**Correct Answer: B**

**Explanation:** With converged networking, storage (RDMA) and workload traffic share the same adapters. If storage is getting only 60% of expected performance, it's likely being congested by lower-priority traffic. Verify QoS policies are applied (sometimes requires verification after updates) and that priority values are correctly configured.

---

### Question 10: DR Planning
**Your customer requires an RPO of zero (no data loss) and RTO of 30 minutes. What architecture best meets these requirements?**

A) Two 3-node clusters with asynchronous replication to the secondary site.

B) Two 3-node clusters with synchronous replication, cloud witness for quorum, and automated failover scripts.

C) Single 3-node cluster at primary site only, with nightly backups.

D) One 6-node cluster split across two sites using active-active configuration.

**Correct Answer: B**

**Explanation:** RPO=0 requires synchronous replication (Option A uses asynchronous). RTO=30 minutes requires automated failover (Option C is manual). Options B and D both work, but B is simpler and more standard. D adds complexity with active-active coordination.

---

## Scoring Guide

- **9-10 Correct:** Excellent understanding of Azure Local advanced architecture. Ready for production deployment responsibilities.
- **7-8 Correct:** Good understanding with minor gaps. Recommend reviewing specific sections before lead role.
- **5-6 Correct:** Foundational understanding. Recommend additional study before independent design work.
- **< 5 Correct:** Significant gaps. Return to core sections and retake assessment.

---

## Key Concepts Covered

This assessment validates understanding of:
- System architecture layers and their independence
- Network design with VLANs and QoS
- Storage resilience and rebuild processes
- Hardware selection and capacity planning
- Deployment pattern selection based on constraints
- Quorum mechanisms and failure scenarios
- Automatic failure recovery timelines
- Capacity planning with redundancy overhead
- Network optimization and troubleshooting
- Disaster recovery architecture decisions

