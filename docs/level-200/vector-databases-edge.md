---
layout: default
title: Vector Databases for Edge
parent: Module 3 - Edge RAG Implementation
nav_order: 3
---

# Vector Databases for Edge

## Overview

Vector databases are the foundation of RAG systems, enabling fast similarity search across millions of embeddings. This page explores vector database selection, indexing strategies, and optimization techniques for enterprise edge deployments where performance and resource efficiency are critical.

---

## Vector Database Selection Matrix

### Evaluation Criteria

1. **Performance**
   - Query latency: <50ms for 1M+ vectors
   - Throughput: 1,000+ queries per second
   - Recall accuracy: >95% for top-k results

2. **Scalability**
   - Support for 100M+ vectors
   - Horizontal sharding
   - Memory efficiency (< 5KB per vector)

3. **Enterprise Features**
   - RBAC & authentication
   - Encryption at rest/transit
   - Replication & failover
   - Backup & recovery

4. **Kubernetes Integration**
   - Container-native deployment
   - Helm charts available
   - Persistent volumes support
   - StatefulSet ready

### Edge-Ready Vector Databases

#### Weaviate

**Profile:**

- Language: Go
- Model: Modular (pluggable ML modules)
- Scaling: Horizontal sharding
- Enterprise: ✅ Full support

**Characteristics:**

```text
Vector Capacity:     <50M vectors (single), <500M (sharded)
Query Latency:       <20ms (1M vectors)
Memory per Vector:   ~2KB
Deployment Size:     ~500MB container
GPU Support:         Yes (CUDA/ROCm)
ML Framework:        Pluggable (Hugging Face, Cohere)
```

**Best For:**

- Hybrid search (vector + keyword)
- Rapid prototyping
- Multi-tenant deployments

**Kubernetes Example:**

```yaml
helm install weaviate weaviate/weaviate \
  --values values.yaml \
  --set persistence.enabled=true \
  --set persistence.size=100Gi
```

#### Qdrant

**Profile:**

- Language: Rust
- Model: High-performance, optimized
- Scaling: Distributed clusters
- Enterprise: ✅ Strong

**Characteristics:**

```text
Vector Capacity:     <100M vectors (single), >1B (distributed)
Query Latency:       <30ms (1M vectors)
Memory per Vector:   ~1.5KB
Deployment Size:     ~150MB container
GPU Support:         Limited (CPU optimized)
Index Type:          HNSW, IVF
```

**Best For:**

- Large-scale deployments
- High throughput requirements
- Cost-sensitive environments

**Performance Comparison:**

```text
1M Vectors:   <30ms latency
10M Vectors:  <50ms latency
100M Vectors: <200ms latency (distributed)
```

#### Milvus

**Profile:**

- Language: C++
- Model: Distributed, cloud-native
- Scaling: Kubernetes-first design
- Enterprise: ✅ Strong

**Characteristics:**

```text
Vector Capacity:     >1B vectors (distributed)
Query Latency:       <50ms (100M vectors)
Memory per Vector:   ~2KB
Deployment Size:     ~400MB container
GPU Support:         Full (CUDA)
Cloud Native:        Kubernetes operator available
```

**Best For:**

- Massive scale (>100M vectors)
- Cloud-native deployments
- Complex filtering requirements

#### Chroma

**Profile:**

- Language: Python
- Model: Simple, developer-friendly
- Scaling: Single machine or basic clustering
- Enterprise: ⚠️ Limited

**Characteristics:**

```text
Vector Capacity:     <10M vectors
Query Latency:       <15ms (1M vectors)
Memory per Vector:   ~2KB
Deployment Size:     ~100MB container
GPU Support:         No
Best Use:            Development, small scale
```

#### Comparison Table

| Database | Scale | Latency | Memory | Enterprise | Edge-Ready |
|----------|-------|---------|--------|-----------|-----------|
| Weaviate | 500M | <20ms | 2KB | ✅ Strong | ✅ Optimal |
| Qdrant | >1B | <30ms | 1.5KB | ✅ Strong | ✅ Optimal |
| Milvus | >1B | <50ms | 2KB | ✅ Strong | ✅ Good |
| Chroma | 10M | <15ms | 2KB | ⚠️ Limited | ✅ Dev |

---

## Vector Indexing Strategies

### Index Types & Trade-offs

#### HNSW (Hierarchical Navigable Small World)

**Best for:** Most edge deployments

```text
Characteristics:
  - Search: O(log n) complexity
  - Insert: O(log n) complexity
  - Memory: ~2KB per vector
  - Latency: <10ms for 1M vectors
  - Accuracy: 99%+

Configuration:
  - ef_construction: 200-400 (higher = better quality, slower build)
  - max_connections: 16-64 (higher = better search, more memory)
  - ef_search: 100-200 (higher = better accuracy, slower search)
```

**Use When:**

- Sub-100ms latency required
- Memory is constrained
- Real-time indexing needed

**Example:**

```json
{
  "indexType": "hnsw",
  "hnsw": {
    "m": 32,
    "efConstruction": 200,
    "efSearch": 200
  }
}
```

#### IVF (Inverted File)

**Best for:** Large-scale deployments (>100M vectors)

```text
Characteristics:
  - Search: O(k log n) complexity (faster for large n)
  - Insert: O(log n) complexity
  - Memory: ~1KB per vector
  - Latency: <50ms for 100M vectors
  - Accuracy: 95-98%

Configuration:
  - nlist: 100-1000 (number of partitions)
  - nprobe: 10-100 (partitions to search)
  - trainable: Training vectors (>100K)
```

**Use When:**

- Scale >100M vectors
- Memory constraints
- Batch indexing acceptable

**Trade-offs:**

- Slower search than HNSW
- Better memory efficiency
- Requires training phase

#### Flat Search

**Best for:** Small datasets or maximum accuracy

```text
Characteristics:
  - Search: O(n) complexity (linear)
  - Insert: O(1) complexity (instant)
  - Memory: No index overhead
  - Latency: Proportional to dataset size
  - Accuracy: 100%

Use When:
  - <1M vectors
  - Accuracy critical
  - Preprocessing acceptable
```

### Multi-Index Strategy for Edge

**Optimize for your workload:**

```text
Dataset Size    | Primary Index | Secondary | Rationale
────────────────────────────────────────────────────────────
<1M vectors     | Flat Search   | -         | Fast, accurate
1-10M vectors   | HNSW          | Flat      | Balance speed/memory
10-100M vectors | HNSW+IVF      | -         | Distributed search
>100M vectors   | IVF+Sharding  | HNSW      | Partition by shard
```

---

## Embedding Model Selection

### Embedding Model Characteristics

```text
Model              | Dimensions | Size   | Speed    | Quality | Edge-Ready
────────────────────────────────────────────────────────────────────────────
all-minilm-l6-v2  | 384        | 90MB   | Fast     | Good    | ✅ Best
bge-base-en        | 768        | 440MB  | Medium   | Optimal | ✅ Good
multilingual-e5-m  | 384        | 120MB  | Fast     | Good    | ✅ Good
OpenAI text-embed  | 1536       | API    | Slow     | Optimal | ❌ Cloud
Cohere embed-en    | 1024       | API    | Slow     | Optimal | ❌ Cloud
```

### Embedding Generation Pipeline

```text
Raw Text
  │
  ├─ Tokenization (text → token IDs)
  │   • BPE, WordPiece, or SentencePiece
  │   • Token limit: 512 typical
  │
  ├─ Embedding Computation (tokens → vector)
  │   • Transformer model inference
  │   • Output: Float32 vector (384-1536 dims)
  │
  └─ Vector Normalization
      • L2 normalization (improve similarity comparison)
      • Output: Normalized vector [-1, 1]

Performance:
  - Single embedding: 5-50ms (CPU), 1-5ms (GPU)
  - Batch 100: 100-200ms (CPU), 10-20ms (GPU)
  - Batch 1000: 500-1000ms (CPU), 50-100ms (GPU)
```

### Embedding Storage & Retrieval

**Vector Format Optimization:**

```text
Standard (Float32):
  - Size: 384 dims × 4 bytes = 1.5 KB per vector
  - Accuracy: 100%
  - Recommended: Production

Half-Precision (Float16):
  - Size: 384 dims × 2 bytes = 768 B per vector
  - Accuracy: 99.5% (minimal impact)
  - Recommended: When memory constrained
  - Savings: 50% storage, 2x faster search

Quantized (Int8):
  - Size: 384 dims × 1 byte = 384 B per vector
  - Accuracy: 98% (acceptable)
  - Recommended: Extreme memory constraints
  - Savings: 75% storage, 4x faster search
```

---

## Similarity Search Tuning

### Search Quality vs. Performance

```text
Search Strategy     | Accuracy | Speed  | Memory | Use Case
─────────────────────────────────────────────────────────────
Exact (Flat)        | 100%     | Slow   | Low    | Small data
HNSW (ef=200)       | 99%      | Medium | Medium | Balanced
HNSW (ef=500)       | 99.5%    | Slower | Medium | High quality
IVF (nprobe=10)     | 95%      | Fast   | Low    | Large scale
IVF (nprobe=100)    | 98%      | Medium | Low    | Balanced
```

### Query Optimization

**Retrieve most relevant context:**

```text
Basic Query:
  SELECT * FROM vectors
  WHERE distance(query_vec, embedding) < threshold
  ORDER BY distance ASC
  LIMIT 5

Result: 5 closest vectors, ~50ms

Optimized Query (with reranking):
  1. BM25 keyword search (100 results) → 10ms
  2. Vector search (top 50) → 30ms
  3. LLM-based reranking (top 5) → 100ms
  4. Return top 5 results

Result: More relevant results, ~140ms total
```

### Metadata Filtering

**Efficient filtering strategies:**

```text
High-Quality Filtering:
  SELECT * FROM vectors
  WHERE date_updated > '2024-01-01'
    AND source = 'internal_docs'
    AND status = 'approved'
  ORDER BY distance(query_vec, embedding) ASC
  LIMIT 10

Optimization:
  - Create indexes on date_updated, source, status
  - Filter first (reduce vector search space)
  - Then similarity search on filtered subset
  - Impact: 10x faster queries with specific metadata
```

---

## Scaling Vector Databases

### Horizontal Scaling (Sharding)

**Distribution strategy:**

```text
Logical Shards (by hash):
  Vectors 0-333M:   Shard 1 (Server 1)
  Vectors 333M-666M: Shard 2 (Server 2)
  Vectors 666M-1B:   Shard 3 (Server 3)

Query Flow:
  1. Parse query vector
  2. Send to all 3 shards in parallel
  3. Collect top-10 from each shard (30 candidates)
  4. Re-rank globally
  5. Return top-10

Performance:
  - Single shard latency: 50ms × 3 shards (parallel) = 50ms
  - vs. single server: 200ms
  - Improvement: 4x faster
```

### Replication for High Availability

```text
Master-Replica Setup:
  ┌──────────────┐
  │ Master Node  │ (Write operations)
  │ (Primary)    │
  └─────┬────────┘
        │
    ┌───┴───┐
    │       │
  ┌─▼───┐ ┌▼───┐
  │Rep 1 │ │Rep 2│ (Read operations)
  │      │ │     │
  └──────┘ └─────┘

Redundancy:
  - Replica 1: Full copy
  - Replica 2: Full copy
  - Any node down: No impact
  - RPO: 0 (no data loss)
  - RTO: <5s (automatic failover)
```

---

## Vector Database Operations

### Backup & Recovery

**Enterprise backup strategy:**

```text
Backup Schedule:
  - Snapshots: Every 6 hours
  - Full export: Daily (off-peak)
  - WAL (Write-Ahead Logs): Continuous

Recovery Options:
  1. Point-in-time restore (< 5 minutes)
  2. Full restore from backup (< 30 minutes)
  3. Incremental restore (< 10 minutes)

Storage:
  - Local: For rapid recovery
  - Remote: For disaster recovery
  - Cloud storage: Long-term retention
```

### Monitoring & Health

**Key metrics to track:**

```text
Search Performance:
  - Query latency (p50, p95, p99)
  - Throughput (queries/second)
  - Cache hit rate

Resource Utilization:
  - CPU usage
  - Memory consumption
  - Disk I/O
  - Network bandwidth

Data Health:
  - Total vectors indexed
  - Index fragmentation
  - Missing or corrupt entries
```

---

## Related Topics

- **Main Page:** [Edge RAG Implementation](./edge-rag-implementation.md)
- **Deployment:** [RAG Deployment Strategies](./rag-deployment-strategies.md)
- **LLM Optimization:** [LLM Inference Optimization](./llm-inference-optimization.md)
- **Operations:** [RAG Operations & Monitoring](./rag-operations-monitoring.md)
- **Assessment:** [RAG Implementation Knowledge Check](./rag-implementation-knowledge-check.md)

---

_Last Updated: October 21, 2025_
