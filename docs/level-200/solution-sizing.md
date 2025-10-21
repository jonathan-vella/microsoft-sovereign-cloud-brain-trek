---
layout: default
title: Solution Sizing & Planning
parent: Level 200 - Intermediate
nav_order: 4
---

# Solution Sizing & Planning

> **📊 Visual Reference: Asset 33 - Solution Sizing Framework**  
> *Placeholder - See docs/assets/images/README.md#asset-33*  
> Interactive sizing process showing input variables (workload type, user count, data volume, growth), calculation layers (compute/storage/network sizing), decision points for HA/redundancy, and output configurations with cost estimates and confidence ranges.

## Overview

Solution sizing translates customer requirements into specific hardware configurations, software components, and deployment architectures. This page covers workload assessment, sizing calculators, capacity planning, and validation techniques.

---

## Solution Sizing Methodology

### Three-Phase Sizing Process

```
PHASE 1: REQUIREMENTS EXTRACTION (1-2 weeks)
├─ Workload characterization
├─ Performance requirements
├─ Scale and growth projections
└─ Operational constraints

PHASE 2: CAPACITY CALCULATION (1 week)
├─ CPU/Memory sizing
├─ Storage sizing
├─ Network requirements
└─ GPU/accelerator needs

PHASE 3: VALIDATION & OPTIMIZATION (1 week)
├─ Benchmark against requirements
├─ Cost optimization analysis
├─ Risk mitigation planning
└─ Final recommendation & presentation
```

---

## Workload Classification & Profiling

### Workload Categories

```
CATEGORY 1: Inference (AI/ML prediction)
├─ Characteristics:
│  ├─ High throughput (100-10000 QPS)
│  ├─ Low latency requirement (<500ms)
│  ├─ GPU-intensive
│  └─ Stateless operations
├─ Sizing Focus:
│  ├─ GPU count and memory
│  ├─ Batch processing capability
│  └─ Network throughput

CATEGORY 2: Analytics/Reporting
├─ Characteristics:
│  ├─ Batch processing
│  ├─ High data volume (TB-PB)
│  ├─ Flexible timing
│  └─ CPU-intensive
├─ Sizing Focus:
│  ├─ Storage capacity
│  ├─ CPU cores
│  └─ Network bandwidth

CATEGORY 3: Transactional Database
├─ Characteristics:
│  ├─ Consistent throughput (1000-100K TPS)
│  ├─ Low latency (<10ms)
│  ├─ High availability
│  └─ ACID compliance
├─ Sizing Focus:
│  ├─ Memory (cache efficiency)
│  ├─ IOPS (disk speed)
│  └─ Network latency

CATEGORY 4: Vector Search (RAG)
├─ Characteristics:
│  ├─ Moderate throughput (100-10000 QPS)
│  ├─ Similarity search
│  ├─ Memory-resident indexes
│  └─ GPU-optional
├─ Sizing Focus:
│  ├─ Memory (index size)
│  ├─ Network I/O
│  └─ CPU cores for search
```

### Workload Profile Template

```
WORKLOAD NAME: [Name]
WORKLOAD TYPE: [Classification]
BUSINESS CONTEXT: [Why this matters]

SCALE CHARACTERISTICS:
├─ Concurrent Users: [Number]
├─ Queries/Transactions per Second:
│  ├─ Average: [X QPS]
│  ├─ Peak: [Y QPS, Z% of time]
│  └─ 99th percentile: [W QPS]
├─ Data Volume:
│  ├─ Current: [Size]
│  ├─ Year 1: [Size]
│  ├─ Year 3: [Size]
│  └─ Growth Rate: [% per year]

PERFORMANCE REQUIREMENTS:
├─ Latency:
│  ├─ p50: [ms]
│  ├─ p95: [ms]
│  └─ p99: [ms]
├─ Throughput: [Transactions/sec]
├─ Availability: [SLA %]
└─ Error Rate: [Target %]

INFRASTRUCTURE CONSTRAINTS:
├─ Hardware Available: [Description]
├─ Power Budget: [kW]
├─ Network Bandwidth: [Mbps]
├─ Physical Space: [sq ft]
└─ Environmental: [Temperature, humidity, etc.]

OPERATIONAL CONSTRAINTS:
├─ Maintenance Windows: [Frequency]
├─ Failover Requirements: [RPO/RTO]
├─ Compliance Audits: [Frequency]
└─ Support Model: [24/7, business hours, etc.]
```

---

## Hardware Sizing Calculators

### CPU Sizing Calculator

```
STEP 1: Estimate CPU Requirements
─────────────────────────────────
Per-Query CPU Time: [ms]
  (from benchmarking or vendor data)

Queries per Second (peak): [QPS]

Cores Needed = (QPS × CPU_time_ms × num_threads) / (core_time_per_sec × efficiency)

Example:
  - 500 QPS peak
  - 50ms CPU time per query
  - 4 threads per query
  - 85% CPU efficiency
  
  Cores = (500 × 50 × 4) / (1000 × 0.85) = 117 cores needed
  
  → Recommend: 4 nodes × 32 cores = 128 cores
  → Provides 9% headroom

STEP 2: Add Overhead for System Services
────────────────────────────────────
  - Operating system: 15% of cores
  - Monitoring/logging: 10% of cores
  - Cache/buffers: 5% of cores
  - Headroom for peaks: 10% of cores
  
  Total Overhead: ~40% of cores
  
  Adjusted cores needed = 117 / 0.6 = 195 cores

STEP 3: Select Hardware
──────────────────────
  - Dual-socket servers, 32 cores each = 64 cores/server
  - 195 / 64 = 3.05 → Recommend 4 servers
  
RESULT: 4 servers with dual 32-core processors
```

### Memory Sizing Calculator

```
STEP 1: Identify Memory Components
──────────────────────────────────
Working Set Size:
  - Active data in use: [GB]
  - Example: LLM model (7B params in INT4) = 2GB

Cache Layers:
  - Application cache: [GB]
  - Database buffer pool: [GB]
  - OS page cache: [GB]
  - Total cache: [GB]

Index Structures:
  - Vector index (HNSW for 1M vecs): 2KB per vector = 2GB
  - B-tree indexes: varies
  - Hash tables: varies
  - Total: [GB]

Temporary Allocations:
  - Query processing: [GB]
  - Sort buffers: [GB]
  - Join buffers: [GB]
  - Total: [GB]

STEP 2: Calculate Total Memory
──────────────────────────────
Total = Working Set + Cache + Indexes + Temp + Headroom (25%)

Example:
  - Working Set (LLM): 2GB
  - Cache: 64GB
  - Indexes (1M vectors): 2GB
  - Temp buffers: 10GB
  - Headroom (25%): 19.5GB
  
  Total: ~98GB → Round to 128GB per server

STEP 3: Memory Layout per Server
─────────────────────────────────
With 384GB server (enterprise hardware):
  - LLM model: 2GB (40% GPU VRAM, 60% host)
  - Vector index: 2GB
  - Buffer pool: 256GB
  - OS + overhead: 124GB
  
  Utilization: ~340/384 = 88.5%
```

### GPU Sizing Calculator

```
STEP 1: Assess GPU Requirements
───────────────────────────────
Model Requirements:
  - Llama 2 7B in INT4: ~2GB VRAM
  - Mistral 7B in INT8: ~8GB VRAM
  - Llama 2 13B in INT8: ~14GB VRAM

Inference Requirements:
  - QPS: 500 peak
  - Model latency: 200ms per query
  - Batch size: 4 (256ms latency, 2000 QPS capacity)
  
GPU Memory Needed:
  - Model: 2GB (INT4 quantized)
  - Batch buffers: 1GB (4x batch size)
  - Embeddings: 0.5GB
  - Total per GPU: 3.5GB
  
  Utilization per GPU: 3.5GB / 16GB = 22%
  
STEP 2: Calculate GPU Count
───────────────────────────
With Batch Processing:
  - Batching 4 queries: 2000 QPS theoretical
  - Need 500 QPS: 1 GPU sufficient mathematically
  - Add redundancy: 2 GPUs
  - Add failure headroom: 3 GPUs
  
  → 3x T4 GPUs (16GB each)

STEP 3: Validate Load Distribution
──────────────────────────────────
  - 500 QPS across 3 GPUs = 167 QPS per GPU
  - Batch size 4 = 42 batches/second per GPU
  - Processing time: 200ms + overhead = 250ms per batch
  - Capacity: 1000/250ms × 4 = 16,000 QPS per GPU ✓
  
  Result: 3 GPUs provides 10x headroom

STEP 4: CPU Support for GPU Operations
──────────────────────────────────
  - 1 CPU core per GPU for host processing
  - 2-4 CPU cores for driver and utilities
  - With 3 GPUs: allocate 6 cores minimum
```

### Storage Sizing Calculator

```
STEP 1: Categorize Storage Needs
────────────────────────────────

Hot Storage (SSD, <10ms latency):
  - Active vector indexes: 2GB
  - LLM model cache: 2GB
  - Database working set: 50GB
  - Total hot: 54GB

Warm Storage (NVMe/SSD, <100ms latency):
  - Full embeddings backup: 6GB
  - Model variants: 10GB
  - Query logs (1 week): 100GB
  - Total warm: 116GB

Cold Storage (HDD/Archive, <1s latency):
  - Historical query logs: 500GB
  - Data backups: 200GB
  - Total cold: 700GB

STEP 2: Calculate Total with Replication
────────────────────────────────────────
Replication Factor: 2x (high availability)

  - Hot storage: 54GB × 2 = 108GB SSD
  - Warm storage: 116GB × 2 = 232GB NVMe
  - Cold storage: 700GB × 2 = 1.4TB HDD
  
  Total: ~1.8TB raw storage

STEP 3: Add Growth Buffer (30% per year)
─────────────────────────────────────
Year 1: 1.8TB
Year 2: 1.8TB × 1.3 = 2.3TB
Year 3: 2.3TB × 1.3 = 3TB

Recommendation: Procure 3TB usable with tiering
```

### Network Sizing Calculator

```
STEP 1: Calculate Bandwidth Requirements
─────────────────────────────────────────

Ingress (Data flowing in):
  - Query traffic: 500 QPS × 2KB query = 1 MB/sec
  - Data ingestion: 100 MB/hour
  - Replication sync: 50 Mbps (peak)
  - Total ingress: ~50 Mbps average, 150 Mbps peak

Egress (Data flowing out):
  - Query responses: 500 QPS × 5KB response = 2.5 MB/sec
  - Replication egress: 50 Mbps
  - Monitoring/logging: 20 Mbps
  - Total egress: ~70 Mbps average, 200 Mbps peak

Cluster Internal:
  - Node-to-node replication: 50 Mbps
  - Storage access: 100 Mbps
  - Monitoring: 10 Mbps
  - Total internal: ~160 Mbps average, 400 Mbps peak

STEP 2: Size Network Interfaces
───────────────────────────────
External-facing (to users/services):
  - 200 Mbps peak required
  - Recommend: Dual 10Gbps uplinks (20 Gbps total)
  - Utilization: <1%

Cluster-internal (node-to-node):
  - 400 Mbps peak required
  - Recommend: 25Gbps fabric interconnect
  - Utilization: <2%

Per-server network:
  - External: 10Gbps NIC (1000x peak requirement)
  - Internal: 25Gbps interconnect

STEP 3: Network Services Configuration
──────────────────────────────────────
Load Balancer:
  - Capacity: 20 Gbps minimum
  - Connection tracking: 100K sessions
  - NAT throughput: 5 Gbps

Firewall:
  - Stateful inspection: 20 Gbps minimum
  - Connection limit: 1M concurrent

Switch Fabric:
  - Non-blocking: Full bandwidth between all ports
  - Redundancy: Dual switches, active-active

Backup Network:
  - Dedicated for replication
  - 25Gbps capacity
```

---

## Capacity Planning & Growth

### Growth Projection Framework

```
CURRENT STATE (Year 0):
├─ Users: 50 concurrent
├─ Queries: 100K/day (1.15 QPS avg)
├─ Data: 100K vectors (200MB)
└─ Hardware: 2 nodes + 1 GPU

YEAR 1 PROJECTION (30% growth):
├─ Users: 65 concurrent
├─ Queries: 130K/day (1.5 QPS avg)
├─ Data: 130K vectors (260MB)
└─ Action: Monitor, no changes needed

YEAR 2 PROJECTION (30% growth):
├─ Users: 85 concurrent
├─ Queries: 169K/day (2 QPS avg)
├─ Data: 169K vectors (338MB)
└─ Action: Prepare for expansion

YEAR 3 PROJECTION (30% growth):
├─ Users: 110 concurrent
├─ Queries: 220K/day (2.5 QPS avg)
├─ Data: 220K vectors (440MB)
└─ Action: Add additional replicas

YEAR 5 PROJECTION (Conservative, slowing growth):
├─ Users: 200 concurrent
├─ Queries: 500K/day (5.8 QPS avg)
├─ Data: 500K vectors (1GB)
└─ Action: Consider multi-cluster sharding
```

### Capacity Monitoring & Triggers

```
METRIC: CPU Utilization
├─ Yellow (75%): Plan upgrade timeline
├─ Red (90%): Implement optimization or upgrade
├─ Critical (95%): Escalate immediately

METRIC: Memory Utilization
├─ Yellow (80%): Monitor swap activity
├─ Red (90%): Plan hardware upgrade
├─ Critical (95%): Implement emergency measures

METRIC: Storage I/O (IOPS)
├─ Yellow (70% of limit): Monitor workload patterns
├─ Red (85% of limit): Add storage or optimize queries
├─ Critical (95% of limit): Escalate, may impact SLA

METRIC: Network Bandwidth
├─ Yellow (60% of capacity): Monitor usage patterns
├─ Red (80% of capacity): Consider network upgrade
├─ Critical (95% of capacity): Escalate immediately

TRIGGER ACTIONS:
├─ Yellow State: Send notification to ops team
├─ Red State: Create upgrade planning ticket
├─ Critical State: Execute emergency response playbook
```

---

## Sizing Validation Techniques

### Benchmark-Based Validation

```
STEP 1: Identify Reference Workload
───────────────────────────────────
Similar customer workload:
  - 500 QPS peak load
  - 1M vector embeddings
  - Llama 2 7B model

Benchmark Results from Reference:
  - 3x T4 GPUs: 2000 QPS capacity
  - 4x CPU nodes: 4000 req/sec processing
  - Total storage: 2TB with HA

STEP 2: Scale to Your Requirements
──────────────────────────────────
Your Peak Load: 500 QPS
Reference Benchmark: 2000 QPS capacity
Scaling Factor: 500 / 2000 = 0.25x

Your Hardware Needs:
  - GPUs: 3 × 0.25 = 0.75 → round up to 1 GPU
  - But add redundancy: use 2 GPUs
  - CPU nodes: scale similarly
  - Storage: scale proportionally

STEP 3: Validation
──────────────────
Performance Model Prediction:
  - 2 T4 GPUs: 1333 QPS capacity
  - Expected latency: 180ms p95
  - Storage needs: 500GB

Customer Requirement Alignment:
  - Required QPS: 500 ✓ (67% headroom)
  - Required latency: <200ms ✓ (meets p95)
  - Required storage: <500GB ✓ (meets requirement)

VERDICT: Sizing meets requirements with 50% headroom
```

### Load Testing Validation

```
PHASE 1: Baseline Testing (Week 1)
──────────────────────────────────
Deploy proposed hardware
Run representative workload:
  - Ramp up from 10% to 100% of expected load
  - Measure latency, throughput, CPU, memory
  - Collect performance data for 6 hours

Expected Results:
  - p50 latency: <100ms
  - p95 latency: <200ms
  - CPU utilization: <70%
  - Memory utilization: <80%

PHASE 2: Peak Load Testing (Week 2)
──────────────────────────────────
Run spike tests to peak expected load:
  - Instantaneous ramp to 100% load
  - Sustain for 30 minutes
  - Measure recovery time

Expected Results:
  - Latency degradation <20%
  - No request timeouts
  - Recovery to baseline within 2 minutes

PHASE 3: Stress Testing (Week 3)
───────────────────────────────
Run 150% of peak expected load:
  - Identify breaking point
  - Test failover and recovery
  - Verify graceful degradation

Expected Results:
  - System remains responsive
  - Graceful throttling below peak at 150%
  - No data loss during failover

PASS/FAIL CRITERIA:
✓ PASS if all phases meet expected results
✗ FAIL if any metric significantly misses
  → If failed: Re-size and re-test
```

---

## Sizing Output Document

### Executive Summary Section

```
PROPOSED SOLUTION SUMMARY
─────────────────────────
Deployment Model: [Single/Multi-region Hub-Spoke, etc.]
Hardware: [Component list]
Software: [Platform and tools]
Estimated Cost: [$ figure]
Implementation Timeline: [Weeks/months]

CAPACITY PROFILE
────────────────
Peak Throughput: [X QPS or TPS]
Concurrent Users: [N users]
Data Volume: [Size]
Storage Capacity: [Size]
Network Bandwidth: [Mbps]

PERFORMANCE TARGETS
───────────────────
Latency p95: [ms]
Availability: [SLA %]
Throughput: [ops/sec]
Cost per Transaction: [$]

VALIDATION
──────────
Benchmark Match: [Yes/No]
Load Test Results: [Pass/Fail]
Risk Assessment: [Low/Medium/High]
Confidence Level: [%]
```

---

## Related Topics

- **Main Page:** [Pre-Sales & Solution Design](./presales-solution-design.md)
- **Discovery:** [Customer Discovery](./customer-discovery.md)
- **Cost Analysis:** [Cost Estimation & TCO](./cost-estimation.md)
- **Proposals:** [Proposal Development](./proposal-development.md)
- **Quiz:** [Pre-Sales Quiz](./presales-quiz.md)

---

*Last Updated: October 21, 2025*
