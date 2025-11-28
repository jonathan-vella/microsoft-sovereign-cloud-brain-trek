---
layout: default
title: Lab - Connected Mode Multi-Site
parent: Module 2 - Azure Local Connected
nav_order: 3
---

# Lab: Connected Mode Multi-Site Deployment

## Lab Scenario

**Company:** GlobalTech Expansion  
**Objective:** Deploy Azure Local in connected mode across two geographic sites  
**Compliance:** GDPR, data residency requirements  
**Duration:** 2-3 hours  
**Resources:** 2 Azure Local clusters, Azure connectivity services

---

## Learning Outcomes

After completing this lab, you will:

- Deploy multi-site Azure Local architecture
- Configure Azure ExpressRoute connectivity
- Implement cluster federation
- Set up multi-site monitoring
- Execute failover procedures

---

## Lab Environment

### Pre-lab Setup

- Primary site Azure Local cluster (configured, ready)
- Secondary site Azure Local cluster (pre-staged)
- Azure subscription with network infrastructure
- ExpressRoute circuit (or simulated connectivity)

### Success Criteria

- Both clusters operational and federated
- Azure connectivity validated
- Multi-site workload deployed
- Monitoring showing both sites
- Failover test completed successfully

---

## Exercises

### Exercise 1: Site Federation (90 minutes)

**Objective:** Configure cluster federation across sites

1. Validate cluster health on both sites
2. Create federation relationship
3. Synchronize configuration policies
4. Validate replication health
5. Test management operations from primary

**Deliverables:**

- Federated cluster status
- Replication metrics
- Configuration consistency check

---

### Exercise 2: Azure Connectivity (90 minutes)

**Objective:** Establish cloud connectivity

1. Configure ExpressRoute Private Peering
2. Connect primary cluster to Azure
3. Connect secondary cluster to Azure
4. Validate cross-site cloud access
5. Test failover between connectivity paths

**Deliverables:**

- Connectivity validation report
- Failover test results
- Bandwidth metrics

---

### Exercise 3: Multi-Site Workload (60 minutes)

**Objective:** Deploy applications across sites

1. Create application on primary site
2. Configure site affinity policies
3. Deploy replica workload to secondary
4. Verify data synchronization
5. Test load distribution

**Deliverables:**

- Workload deployment confirmation
- Replication status report
- Performance metrics

---

### Exercise 4: Multi-Site Monitoring (60 minutes)

**Objective:** Set up comprehensive monitoring

1. Deploy monitoring agents to both sites
2. Aggregate metrics to Azure Monitor
3. Create cross-site dashboards
4. Set up alerts for site failures
5. Verify incident response workflow

**Deliverables:**

- Dashboard screenshots
- Alert configuration
- Incident response test results

---

### Exercise 5: Failover & Recovery (60 minutes)

**Objective:** Practice failure scenarios

1. Simulate site failure
2. Execute failover procedures
3. Verify workload migration
4. Test recovery procedures
5. Return to normal operations

**Deliverables:**

- Failover execution log
- Recovery time metrics
- Lessons learned document

---

### Exercise 6: Performance Tuning (30 minutes)

**Objective:** Optimize multi-site performance

1. Collect baseline performance metrics
2. Identify optimization opportunities
3. Adjust QoS policies
4. Re-measure performance
5. Document changes

**Deliverables:**

- Baseline vs. optimized comparison
- Configuration changes applied
- Performance improvement summary

---

## Troubleshooting Guide

### Federation Issues

- Cluster network connectivity
- Certificate validation
- Policy compatibility

### Connectivity Problems

- ExpressRoute diagnostics
- Site-to-site routing
- Firewall rules

### Replication Lag

- Bandwidth constraints
- Latency issues
- Data size factors

---

## Grading Rubric

| Area | Excellent | Good | Needs Work |
|------|-----------|------|-----------|
| Cluster Federation | Federated, fully synced | Federated, minor issues | Fails to federate |
| Azure Connectivity | Redundant, failover working | Connected, no redundancy | Connection issues |
| Workload Deployment | Multi-site with replication | Single site working | Deployment failure |
| Monitoring | All metrics aggregated | Partial monitoring | No monitoring |
| Failover Response | <5 min, automatic | <15 min, manual | >30 min or incomplete |

---

**See also:** [Connected Mode Overview](azure-local-advanced-connected) | [Multi-Site Architectures](azure-local-multi-site) | [Networking Guide](azure-local-networking-advanced)
