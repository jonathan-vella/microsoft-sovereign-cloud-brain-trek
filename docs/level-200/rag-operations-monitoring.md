---
layout: default
title: RAG Operations & Monitoring
parent: Edge RAG Implementation
nav_order: 3
---

# RAG Operations & Monitoring

## Overview

Production RAG systems require robust operational patterns, comprehensive monitoring, and continuous quality assessment. This page covers monitoring strategies, operational excellence practices, observability patterns, and incident response for enterprise edge RAG deployments.

---

## Operational Patterns

### RAG System Health Model

```text
Healthy RAG System
─────────────────────
Queries      Vector Search    LLM Generation    User Feedback
    │              │                │                 │
    ├─→ <50ms      ├─→ >95% recall  ├─→ <500ms      ├─→ 4.5/5.0
    ├─→ <1% errors ├─→ <1% failures ├─→ <2% errors  ├─→ Factual
    └─→ 100% avail └─→ 100% data    └─→ Coherent    └─→ Relevant

Monitoring Alert Thresholds:
  - Query latency p95 > 200ms → Warning
  - Query latency p95 > 500ms → Critical
  - Vector recall < 90% → Warning
  - LLM generation errors > 5% → Critical
  - Vector search failures > 1% → Critical
```

### Deployment Topology Patterns

#### Pattern 1: Active-Active (Multi-Region)

```text
Region 1 (Primary)          Region 2 (Secondary)
┌─────────────────────┐     ┌─────────────────────┐
│ LLM Service (3x)    │     │ LLM Service (3x)    │
│ Vector DB (3x)      │◄───►│ Vector DB (3x)      │
│ Data Connectors     │     │ Data Connectors     │
└─────────────────────┘     └─────────────────────┘
       ↑                              ↑
    80% users                    20% users
       (local latency)           (cross-region fallback)
```

**Characteristics:**

- Active in both regions
- Users served locally
- Automatic failover
- Async replication

#### Pattern 2: Active-Passive (Standby)

```text
Active (Primary)            Passive (Standby)
┌──────────────────┐       ┌──────────────────┐
│ Full deployment  │       │ Scaled down      │
│ 100% serving     │◄─────►│ 25% capacity     │
│ Traffic: 100%    │ Sync  │ Traffic: 0%      │
└──────────────────┘       └──────────────────┘
     Real Users            Standby Ready

Failover (Automatic):
  1. Primary health check fails (3 consecutive)
  2. DNS updated to Standby
  3. Standby scales to 100%
  4. Users reconnected
  5. Time: <10 seconds
```

**Characteristics:**

- Cost-efficient standby
- Reduced primary load
- RPO: Minutes (async replication)
- RTO: <10 seconds

---

## Monitoring Strategy

### Key Metrics Framework

```text
System Health Dashboard
════════════════════════════════════════════════════════════

SERVICE METRICS (What users experience)
  Query Latency:           150ms (p50), 350ms (p95), 1.2s (p99)
  Success Rate:            99.8%
  Availability:            99.95%
  User Satisfaction:       4.6/5.0

VECTOR SEARCH METRICS (Retrieval quality)
  Search Latency:          45ms avg
  Recall Accuracy:         96.5% (mean reciprocal rank)
  Result Relevance:        94%
  Reranking Success:       87%

LLM INFERENCE METRICS (Generation quality)
  Generation Latency:      200ms avg
  Error Rate:              0.3%
  Hallucination Rate:      2.1%
  Output Length:           150 tokens avg
  GPU Utilization:         72%

RESOURCE METRICS (Infrastructure)
  GPU Memory:              24/32 GB (75%)
  CPU Usage:               45%
  Network I/O:             200 Mbps
  Disk I/O:                150 Mbps

DATA METRICS (Ground truth)
  Embeddings Updated:      2 hours ago
  Index Status:            Healthy
  Total Vectors:           1,234,567
  Data Freshness:          100%
```

### Prometheus Metrics

**Key metrics to expose:**

```yaml
# Query metrics
rag_queries_total{status="success"}           # Total queries
rag_query_duration_seconds{quantile="0.95"}   # Latency p95
rag_query_errors_total{type="timeout"}        # Error types

# Vector search metrics
vector_search_duration_seconds                # Search latency
vector_search_recall@k{k="10"}                # Recall accuracy
vector_retrieval_failures_total               # Failures

# LLM inference metrics
llm_generation_duration_seconds               # Generation time
llm_tokens_generated_total                    # Token count
llm_errors_total{type="cuda_oom"}             # Error types
llm_gpu_memory_usage_bytes                    # GPU memory

# Resource metrics
process_resident_memory_bytes                 # Process memory
process_cpu_seconds_total                     # CPU time
system_disk_io_reads_total                    # Disk I/O
```

### Grafana Dashboards

**Key views:**

```text
1. High-Level Overview
   - Uptime SLO (99.9% target)
   - Query volume (trend)
   - Error rate (target <1%)
   - User satisfaction (target 4.5+)

2. Latency Analysis
   - Query latency distribution (p50, p95, p99)
   - Breakdown by component (vector search, LLM, overhead)
   - Latency trends (hourly/daily)

3. Quality Metrics
   - Hallucination rate
   - Factual accuracy
   - User feedback score
   - Retrieval quality

4. Resource Utilization
   - GPU/CPU usage patterns
   - Memory consumption
   - Network bandwidth
   - Disk I/O

5. Error Analysis
   - Error rate by type
   - Error trends
   - Top failing queries
   - Stack traces
```

---

## Quality Metrics & Evaluation

### RAG Quality Assessment

#### 1. Retrieval Quality

**Metric: Mean Reciprocal Rank (MRR)**

```text
Query: "What is the current Azure Local pricing?"
Retrieved documents:
  1. "Azure Local pricing as of Oct 2025: $..."    ✓ Relevant
  2. "Azure Stack HCI pricing history"              ⚠ Partially
  3. "Azure VM pricing comparison"                  ✗ Not relevant

MRR = 1/1 = 1.0 (perfect, found relevant at position 1)

Typical Goals:
  MRR > 0.90 (excellent)
  MRR > 0.75 (good)
  MRR > 0.50 (acceptable)
```

**Metric: Normalized Discounted Cumulative Gain (NDCG)**

```text
Relevance scores (0-2):
  Position 1: Score 2 (perfect)   DCG₁ = 2 / log₂(2) = 2
  Position 2: Score 1 (partial)   DCG₂ = 1 / log₂(3) = 0.63
  Position 3: Score 0 (irrelevant) DCG₃ = 0

NDCG@5 = (2 + 0.63) / IdealDCG = 0.88

Typical Goals:
  NDCG > 0.85 (excellent)
  NDCG > 0.70 (acceptable)
```

#### 2. Generation Quality

**Hallucination Detection:**

```text
Query: "What's the latest Azure Local hardware spec?"
Retrieved Context: "Azure Local hardware: 2x Intel Xeon, 384GB RAM, 10x NVMe"
Generated Response: "Azure Local requires 4x Intel Xeon, 768GB RAM, 20x NVMe"

Issues:
  - Doubles CPU cores (not in context)
  - Doubles memory (not in context)
  - Doubles storage (not in context)

Hallucination Rate: 100% of response details

Detection Method:
  1. Extract facts from response
  2. Check if facts appear in context
  3. Calculate % not supported by context

Metric: Hallucination Rate
  Target: <2% of responses
  Alert: >5% triggers investigation
```

**Factual Accuracy:**

```text
Human Evaluation:
  - Does response answer the question? Yes/No
  - Are facts grounded in context? Yes/No
  - Is response logically coherent? Yes/No
  - Would user be satisfied? Yes/No

Score: 0-4 (number of yes answers)
Target: 3.5+ average score
Evaluation: Random sampling (100/1000 queries weekly)
```

#### 3. User Satisfaction

**CSAT (Customer Satisfaction):**

```text
Post-query feedback:
  1. Helpful (5 ⭐)
  2. Somewhat helpful (4 ⭐)
  3. Neutral (3 ⭐)
  4. Not helpful (2 ⭐)
  5. Misleading (1 ⭐)

CSAT = (# of 4-5 ratings / # of responses) × 100

Targets by use case:
  - General Q&A: >85% CSAT
  - Technical docs: >90% CSAT
  - Customer support: >95% CSAT
```

---

## Observability & Logging

### Distributed Tracing

**Trace a single query through the system:**

```text
User Query: "What's the best Azure Arc practice?"
Trace ID: abc-123-xyz

Timeline:
  00ms: Query arrives
  05ms: Tokenization + Embedding generation
       [Vector Service] 50ms latency
  55ms: Vector search (retrieve top 10 documents)
       [Vector DB] 50ms latency
       Result: 10 docs, recall=0.96
  105ms: LLM context assembly
         Input: 8 docs (900 tokens)
  120ms: LLM inference
         [LLM Service] 350ms latency
         Output: 150 tokens
  470ms: Post-processing
  480ms: Total response time

Visualization (Jaeger/Zipkin):
  Query
    ├─ Embedding (5ms)
    ├─ Vector Search (50ms)
    │  └─ Reranking (15ms)
    ├─ LLM Inference (350ms)
    │  ├─ Tokenization (5ms)
    │  ├─ Forward Pass (330ms)
    │  └─ De-tokenization (15ms)
    └─ Formatting (10ms)
```

### Centralized Logging

**Log aggregation and analysis:**

```text
Log Levels:
  DEBUG:   Low-level details (100+ logs/sec)
  INFO:    Normal operations (10 logs/sec)
  WARNING: Unexpected but recoverable (1 log/min)
  ERROR:   Failures requiring attention (1 log/hour)
  CRITICAL: System-threatening issues (alert immediately)

Log Format:
  timestamp=2024-10-21T10:30:45.123Z
  level=INFO
  service=llm-inference
  trace_id=abc-123-xyz
  query_id=q-456
  duration_ms=350
  event="LLM inference completed"
  tokens_generated=150
  model_version=llama-7b-v1.2

Aggregation:
  - Elasticsearch + Logstash + Kibana (ELK)
  - Loki (lightweight, log-based metrics)
  - Splunk (enterprise)

Analysis:
  - Search: "duration_ms > 1000" (slow queries)
  - Alert: "error_count > 10/minute"
  - Dashboard: Error trends over time
```

---

## Incident Response

### SLO & Error Budgets

```text
Service Level Objective (SLO):
  Availability: 99.9% (43 minutes downtime/month)
  Latency p95: <200ms
  Error rate: <0.5%

Error Budget:
  Total: 100% - 99.9% = 0.1% (43 minutes/month)

  Week 1: Error budget used = 0.06% (used 26 min)
  Week 2: Error budget used = 0.02% (used 8 min)
  Week 3: Available = 0.02% (9 minutes remaining)
  Week 4: Cannot deploy (no buffer for failures)

Decision:
  Week 1-2: Deploy confidently
  Week 3:   Deploy only critical fixes
  Week 4:   Freeze deployments, focus on stability
```

### Incident Severity Levels

```text
Level 1 (Critical):
  - Service completely unavailable
  - Affecting >50% of users
  - Data loss or corruption
  - Response time: 5 minutes
  - Resolution time: 1 hour

Level 2 (High):
  - Significant degradation (>2s latency)
  - Affecting 10-50% of users
  - Incorrect responses
  - Response time: 15 minutes
  - Resolution time: 4 hours

Level 3 (Medium):
  - Minor issues, workarounds exist
  - Affecting <10% of users
  - Response time: 1 hour
  - Resolution time: 8 hours

Level 4 (Low):
  - Documentation, cosmetic issues
  - No user impact
  - Response time: 24 hours
  - Resolution time: 1 week
```

### Incident Playbook

**Example: High Latency Incident**

```text
Trigger: Latency p95 > 500ms for 5 minutes

Step 1: Immediate Assessment (2 minutes)
  □ Confirm alert via dashboard
  □ Check affected regions/services
  □ Verify not scheduled maintenance

Step 2: Triage (3 minutes)
  □ Is it LLM service? Check GPU memory, queue
  □ Is it vector search? Check memory, load
  □ Is it network? Check latency between services

Step 3: Investigation (5-10 minutes)
  Sample Findings:
    - GPU memory 95% (high)
    - LLM service has 50 queued requests
    - Vector search is healthy

Step 4: Mitigation (2 minutes)
  Option A: Scale up LLM service
    kubectl scale deployment llm-service --replicas=5
    Expected improvement: 20-30% latency reduction

  Option B: Clear queue, reject new requests temporarily
    kubectl set env deployment/ingress QUEUE_LIMIT=50

  Option C: Switch to smaller model
    kubectl set env deployment/llm-service MODEL=phi-3-3b

Step 5: Verification (2 minutes)
  □ Latency p95 returning to baseline
  □ Error rate remains normal
  □ No user complaints

Step 6: Root Cause Analysis (Post-incident)
  □ Why did load spike?
  □ Should autoscaling have kicked in?
  □ Need to adjust scaling thresholds?
```

---

## Best Practices

### Operational Checklist

```text
Daily:
  ☐ Review error rate and latency trends
  ☐ Check data freshness (embeddings, indices)
  ☐ Monitor resource utilization
  ☐ Review critical logs

Weekly:
  ☐ Analyze quality metrics (CSAT, accuracy)
  ☐ Review incident reports
  ☐ Test failover procedures
  ☐ Capacity planning analysis

Monthly:
  ☐ Performance optimization review
  ☐ Cost analysis and optimization
  ☐ Model update readiness check
  ☐ Security and compliance audit

Quarterly:
  ☐ Disaster recovery drill
  ☐ Scaling capacity review
  ☐ Technology refresh assessment
  ☐ Customer feedback review
```

### Alerting Strategy

```text
Alert Fatigue Prevention:
  - Don't alert on every single metric
  - Focus on user-impacting metrics
  - Use derived conditions (e.g., latency + errors)

Sample Alert Rules:
  ✓ DO alert: Availability < 99.5%
  ✓ DO alert: Error rate > 2%
  ✓ DO alert: p95 latency > 500ms for 10 min
  ✗ DON'T: CPU > 50% (might be normal)
  ✗ DON'T: Any single error (false positives)
```

---

## Related Topics

- **Main Page:** [Edge RAG Implementation](./edge-rag-implementation.md)
- **Deployment:** [RAG Deployment Strategies](./rag-deployment-strategies.md)
- **Vector Databases:** [Vector Databases for Edge](./vector-databases-edge.md)
- **LLM Optimization:** [LLM Inference Optimization](./llm-inference-optimization.md)
- **Assessment:** [RAG Implementation Knowledge Check](./rag-implementation-knowledge-check.md)

---

_Last Updated: October 21, 2025_
