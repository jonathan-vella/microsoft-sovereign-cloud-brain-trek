---
layout: default
title: Edge RAG Production - Knowledge Check
parent: Level 300 - Advanced
nav_order: 12
---

# Edge RAG Production - Knowledge Check
{: .no_toc }

Test your expertise in production Edge RAG deployment, MLOps workflows, performance optimization, and enterprise operations.

---

## Quiz Instructions

**Total Questions:** 18  
**Passing Score:** 14/18 (78%)  
**Time Estimate:** 30-40 minutes  
**Format:** Expert-level scenario-based questions

This assessment covers:
- Production RAG architecture and deployment patterns
- MLOps workflows for edge AI models
- Performance optimization techniques
- Knowledge base management at scale
- Enterprise operations and SLA management

---

### Question 1: Production RAG Architecture

Designing production RAG for financial services with strict latency requirements (< 500ms). What architecture provides BEST balance of performance and cost?

A) Cloud-only RAG with GPU instances  
B) Hybrid: Edge inference + cloud knowledge base  
C) Full edge deployment: Local inference + local vector database  
D) Edge inference with on-demand cloud retrieval

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: C**

**Explanation:**
**Full edge deployment** meets latency requirements and regulatory needs:

**Architecture Components:**

**1. Edge Inference Engine:**
- ✅ Local LLM (quantized for edge)
- ✅ < 100ms inference time
- ✅ No cloud dependency
- ✅ Data sovereignty maintained

**2. Local Vector Database:**
- ✅ Embeddings stored locally
- ✅ < 50ms retrieval time
- ✅ No network latency
- ✅ Works in disconnected scenarios

**3. Knowledge Base:**
- ✅ Financial documents locally indexed
- ✅ Regular updates via batch sync
- ✅ Version control
- ✅ Audit trail maintained

**Latency Breakdown:**
```
Retrieval: 30-50ms (local vector DB)
Inference: 80-120ms (quantized model)
Processing: 20-30ms (app logic)
Total: 130-200ms ✅ (well under 500ms target)
```

**Why NOT Others:**
- **A:** Cloud latency variable; data sovereignty issues
- **B:** Retrieval latency adds 50-150ms; sovereignty risk
- **D:** On-demand cloud calls add unpredictable latency

**Reference:** [Production Architecture](edge-rag-architecture-production)
</details>

---

### Question 2: Model Selection for Edge

Choosing LLM for edge RAG with 64GB RAM constraint. Which model type is MOST appropriate?

A) Full-precision 70B parameter model  
B) INT8 quantized 13B parameter model  
C) INT4 quantized 7B parameter model  
D) Cloud API calls (no local model)

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
**INT8 quantized 13B model** provides best quality/resource balance:

**Model Sizing Analysis:**

**Full-Precision 70B (Option A):**
- Memory: 140GB+ (FP16) ❌
- Cannot fit in 64GB constraint

**INT8 Quantized 13B (Option B):**
- Memory: ~13-16GB ✅
- Quality: Minimal degradation (< 3%)
- Inference: 80-150ms
- Supports 4-8 concurrent requests

**INT4 Quantized 7B (Option C):**
- Memory: ~4-7GB ✅
- Quality: Moderate degradation (5-10%)
- Inference: 50-100ms
- May lack reasoning capability

**Cloud API (Option D):**
- Memory: Minimal
- Latency: High and variable
- Data sovereignty violated

**Recommendation: INT8 13B**
- Optimal quality for RAG tasks
- Fits constraint with room for vector DB
- Production-grade performance
- Good cost/performance ratio

**Memory Budget:**
```
Model: 16GB
Vector DB: 8GB
OS + Apps: 12GB
Buffer: 28GB
Total: 64GB ✅
```

**Reference:** [Performance Optimization](edge-rag-optimization#model-selection)
</details>

---

### Question 3: Vector Database Selection

Selecting vector database for 10M document enterprise knowledge base. What is the PRIMARY consideration?

A) Maximum query throughput  
B) Balance of retrieval accuracy, latency, and memory footprint  
C) Lowest cost per query  
D) Easiest to configure

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
**Balanced trade-offs** are critical for production success:

**Key Evaluation Criteria:**

**1. Retrieval Accuracy:**
- ✅ Recall@10: > 95% (find relevant docs)
- ✅ Precision: > 90% (avoid false positives)
- ✅ Supports approximate nearest neighbor (ANN)

**2. Query Latency:**
- ✅ P50: < 30ms
- ✅ P99: < 100ms
- ✅ Consistent performance under load

**3. Memory Footprint:**
- ✅ 10M vectors × 1536 dimensions × 4 bytes = 60GB base
- ✅ Index overhead: 1.2-2x multiplier
- ✅ Total: 72-120GB depending on algorithm

**4. Update Performance:**
- ✅ Incremental updates supported
- ✅ No full reindex for new documents
- ✅ < 100ms per document ingestion

**Vector DB Options:**

**FAISS (Facebook AI):**
- Accuracy: Excellent (configurable)
- Latency: 20-50ms
- Memory: Efficient with compression
- ✅ Good balance for edge

**Milvus:**
- Accuracy: Excellent
- Latency: 30-80ms
- Memory: Higher overhead
- Better for distributed/cloud

**Pinecone/Weaviate:**
- Cloud-native; not ideal for edge

**Why NOT Others:**
- **A:** Throughput important but accuracy is critical
- **C:** Cost secondary to performance/accuracy in production
- **D:** Configuration ease tertiary concern

**Reference:** [Production Architecture](edge-rag-architecture-production#vector-database)
</details>

---

### Question 4: RAG Retrieval Strategy

Production RAG returns irrelevant results 15% of the time. What is the FIRST optimization to try?

A) Increase number of retrieved chunks (k) from 5 to 20  
B) Implement hybrid retrieval: Dense vectors + keyword search  
C) Switch to larger embedding model  
D) Add reranking model after initial retrieval

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: D**

**Explanation:**
**Reranking** is the most effective single improvement for retrieval quality:

**Retrieval Pipeline with Reranking:**

**Stage 1: Initial Retrieval (Fast & Broad)**
- Retrieve k=20 documents (over-retrieve)
- Vector similarity search
- Latency: 30-50ms

**Stage 2: Reranking (Accurate & Focused)**
- Apply cross-encoder reranker model
- Compare query to each retrieved doc
- Score and re-rank
- Select top 5 for LLM context
- Latency: 50-100ms

**Stage 3: LLM Generation**
- Use top 5 reranked documents
- Generate response
- Latency: 80-150ms

**Why Reranking Works:**
- ✅ **Dense vectors miss semantic nuance:** Reranker adds precision
- ✅ **Cross-encoder models more accurate:** See full query-doc interaction
- ✅ **Reduces false positives dramatically:** 15% → 3-5% error rate
- ✅ **Latency acceptable:** 50-100ms overhead worth accuracy gain

**Reranker Options:**
- `ms-marco-MiniLM-L-12-v2` (Fast, 12-layer)
- `cross-encoder/ms-marco-TinyBERT` (Faster, less accurate)
- Custom fine-tuned on domain data (Best)

**Why NOT Others:**
- **A:** More chunks = more noise; makes problem worse
- **B:** Hybrid helps but reranking more impactful as first step
- **C:** Larger embedding expensive; marginal gain

**Reference:** [Performance Optimization](edge-rag-optimization#retrieval-optimization)
</details>

---

### Question 5: Knowledge Base Chunking Strategy

Ingesting technical documentation with complex tables and diagrams. What chunking strategy is BEST?

A) Fixed 512-token chunks with 50-token overlap  
B) Semantic chunking based on document structure (sections, tables)  
C) Sentence-level chunks (one sentence per chunk)  
D) Full document as single chunk

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
**Semantic/structural chunking** preserves context and meaning:

**Chunking Strategy:**

**1. Respect Document Structure:**
- ✅ Sections/headings as natural boundaries
- ✅ Tables kept intact (don't split mid-table)
- ✅ Code blocks preserved
- ✅ Lists maintained

**2. Target Chunk Size:**
- 256-512 tokens (LLM context window consideration)
- Flexible based on content boundaries
- Overlap: 10-20% with adjacent chunks

**3. Metadata Enrichment:**
- ✅ Document title
- ✅ Section heading
- ✅ Page number
- ✅ Content type (text, table, code)
- ✅ Last updated date

**Example: Technical Doc**
```
Chunk 1: Section "Architecture Overview"
  - Full section text
  - Includes architecture diagram reference
  - Metadata: {section: "Architecture", type: "overview"}

Chunk 2: Section "Component Details" + Table
  - Section text + full component table
  - Table NOT split across chunks
  - Metadata: {section: "Components", type: "table"}
```

**Why NOT Others:**
- **A:** Fixed chunks split tables, code blocks; loses context
- **C:** Sentence-level too granular; loses paragraph context
- **D:** Full doc too large; LLM cannot focus on relevant part

**Benefits:**
- Better retrieval relevance
- Preserved context
- Easier to cite sources
- Better LLM reasoning

**Reference:** [Knowledge Base Management](edge-rag-architecture-production#knowledge-base)
</details>

---

### Question 6: MLOps - Model Deployment Strategy

Deploying new RAG model version. What deployment pattern minimizes risk?

A) Replace all edge instances simultaneously  
B) Blue-green deployment with instant cutover  
C) Canary deployment: 5% → 25% → 100% with validation gates  
D) A/B testing with random 50/50 split

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: C**

**Explanation:**
**Canary deployment with gates** provides safest rollout with early issue detection:

**Canary Deployment Process:**

**Phase 1: Canary (5% - 2 hours)**
- ✅ Deploy to 5% of edge nodes
- ✅ Monitor key metrics:
  - Response quality (human eval sample)
  - Latency (P50, P99)
  - Error rate
  - Resource utilization
- ✅ **Gate:** Manual approval after 2 hours if green

**Phase 2: Expanded Canary (25% - 24 hours)**
- Deploy to 25% of nodes
- Monitor same metrics at scale
- Check for edge cases/rare issues
- **Gate:** Auto-proceed if metrics within 5% of baseline

**Phase 3: Full Rollout (100% - 48 hours)**
- Deploy to remaining 75%
- Continue monitoring
- Rollback plan ready

**Validation Gates:**
```
Gate Criteria:
- Error rate < 1%
- P99 latency < baseline + 20%
- Quality score > 95% of baseline
- No critical issues reported
```

**Rollback Procedure:**
- Keep previous model version
- One-command rollback
- < 5 minute rollback time

**Why NOT Others:**
- **A:** All-at-once risks widespread outage if issues
- **B:** Blue-green good but canary provides more gradual validation
- **D:** A/B testing for experimentation, not deployment

**Reference:** [MLOps Workflows](edge-rag-mlops#deployment)
</details>

---

### Question 7: Model Monitoring - Data Drift Detection

Detecting when RAG model needs retraining. Which metric is the PRIMARY indicator of data drift?

A) Inference latency increasing  
B) User query distribution shifting significantly from training data  
C) Memory usage increasing  
D) Error logs growing

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
**Query distribution shift** indicates model sees data it wasn't trained for:

**Data Drift Detection:**

**1. Query Embedding Drift:**
- ✅ Cluster user queries in embedding space
- ✅ Compare to training data distribution
- ✅ Measure: KL divergence, Wasserstein distance
- ✅ **Threshold:** > 0.3 KL divergence = significant drift

**2. Topic Drift:**
- Track query topics over time
- New topics emerging
- Old topics declining
- Example: Sudden surge in regulatory questions after law change

**3. Vocabulary Drift:**
- New terminology appearing
- Out-of-vocabulary rate increasing

**Monitoring Approach:**
```python
# Collect query embeddings
current_embeddings = embed(queries_last_week)
training_embeddings = load(training_set_embeddings)

# Calculate drift
drift_score = kl_divergence(current_embeddings, training_embeddings)

if drift_score > 0.3:
    alert("Significant data drift detected")
    trigger_retraining_evaluation()
```

**Retraining Triggers:**
- Drift score > threshold
- User satisfaction < 85%
- Manual reports of poor quality
- New data domain added

**Why NOT Others:**
- **A:** Latency drift indicates system issues, not data drift
- **C:** Memory usage not related to data distribution
- **D:** Errors indicate bugs, not drift

**Reference:** [MLOps Workflows](edge-rag-mlops#monitoring)
</details>

---

### Question 8: Knowledge Base Update Strategy

Knowledge base has 10M documents. 50K documents updated monthly. What is the MOST efficient update approach?

A) Full reindex of entire 10M documents  
B) Incremental update: Re-embed and re-index only changed documents  
C) Create separate index for new docs; query both  
D) Manual merge of vectors

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
**Incremental updates** provide efficiency and minimal disruption:

**Incremental Update Process:**

**1. Identify Changed Documents:**
- ✅ Track document modification timestamps
- ✅ Checksum/hash comparison
- ✅ 50K changed docs out of 10M = 0.5%

**2. Re-embed Changed Documents:**
- Run embedding model on 50K docs
- Generate new vectors
- Time: ~1-2 hours (depending on hardware)

**3. Update Vector Index:**
- Modern vector DBs support incremental updates
- Delete old vectors for changed docs
- Insert new vectors
- Update index structure
- Time: ~15-30 minutes

**4. Validate:**
- Spot-check retrieval for updated docs
- Ensure no index corruption
- Monitor query performance

**Total Time: 2-3 hours (vs. 24+ hours for full reindex)**

**Why NOT Others:**
- **A:** Full reindex wasteful; 9.95M docs unchanged
- **C:** Multiple indexes complicate queries; merge complexity
- **D:** Manual merge error-prone and not scalable

**Benefits:**
- ✅ Fast updates (hours vs. days)
- ✅ No service interruption
- ✅ Resource efficient
- ✅ Scalable approach

**Reference:** [Knowledge Base Management](edge-rag-architecture-production#knowledge-base)
</details>

---

### Question 9: Inference Optimization - Quantization

Model quantization from FP16 to INT8 reduces memory by 50%. What is the expected quality impact?

A) No quality degradation  
B) 1-3% degradation in task performance  
C) 10-15% degradation  
D) Model becomes unusable

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
**INT8 quantization has minimal quality impact** with proper calibration:

**Quantization Analysis:**

**FP16 (Baseline):**
- 16 bits per weight
- Full precision
- Quality: 100% (reference)

**INT8 (Quantized):**
- 8 bits per weight
- 50% memory reduction
- Quality: 97-99% of FP16
- **Degradation: 1-3% typically**

**Quantization Process:**
1. **Calibration:** Run on representative dataset
2. **Range Finding:** Determine min/max values per layer
3. **Quantization:** Map FP16 range to INT8 range
4. **Validation:** Measure quality impact

**Quality Metrics:**
- Perplexity: +1-2% increase (acceptable)
- Task accuracy: -1-3% decrease
- User satisfaction: Negligible impact

**INT4 Comparison:**
- 4 bits per weight
- 75% memory reduction
- Quality: 90-95% of FP16
- **Degradation: 5-10%** (more noticeable)

**When to Use:**
- INT8: Production default (best balance)
- INT4: Extreme resource constraints only
- FP16: When quality is paramount

**Why NOT Others:**
- **A:** Some degradation inevitable but minimal
- **C/D:** Only with poor quantization or INT4/lower

**Reference:** [Performance Optimization](edge-rag-optimization#quantization)
</details>

---

### Question 10: Batch Processing for Throughput

RAG system needs to process 10K user queries in batch overnight. What optimization provides BEST throughput?

A) Process queries sequentially with full model  
B) Batch retrieval + batch inference with dynamic batching  
C) Scale up to larger GPU for each query  
D) Use multiple separate model instances

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
**Batch processing leverages parallelism** for maximum throughput:

**Optimized Batch Processing:**

**1. Batch Retrieval (Vectorization):**
```python
# Embed all queries at once
query_embeddings = embed_batch(queries, batch_size=128)
# Time: 10K queries / 128 per batch = 78 batches × 200ms = 16 seconds

# Batch vector search
results = vector_db.search_batch(query_embeddings, k=5)
# Time: 78 batches × 50ms = 4 seconds
```

**2. Dynamic Batch Inference:**
```python
# Group queries by similar length (for efficiency)
batches = create_dynamic_batches(queries, max_batch_size=32)

# Process batches in parallel
for batch in batches:
    responses = model.generate(batch, batch_size=32)
# Time: 10K / 32 = 313 batches × 500ms = 157 seconds
```

**Total Time: ~3 minutes** (vs. 10K × 500ms = 83 minutes sequential)

**Throughput Gain: 28x**

**Dynamic Batching Benefits:**
- ✅ Amortizes model load overhead
- ✅ Better GPU utilization (80%+ vs. 20-30%)
- ✅ Reduced memory transfers
- ✅ Optimal for batch workloads

**Why NOT Others:**
- **A:** Sequential leaves GPU idle; 28x slower
- **C:** Larger GPU helps but batching more impactful
- **D:** Multiple instances adds overhead without batching benefit

**Reference:** [Performance Optimization](edge-rag-optimization#batch-processing)
</details>

---

### Question 11: Caching Strategy

Implementing caching for RAG to reduce latency. What caching layer provides BEST performance gain?

A) Cache final LLM responses (semantic cache)  
B) Cache vector retrieval results  
C) Cache embedding computation  
D) All three layers with different TTLs

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: D**

**Explanation:**
**Multi-layer caching** provides maximum benefit with appropriate TTLs:

**Caching Strategy:**

**Layer 1: Semantic Response Cache**
- ✅ Cache final LLM responses
- ✅ Semantic similarity matching (similar queries)
- ✅ Hit: Instant response (< 5ms)
- ✅ TTL: 1-4 hours (context-dependent)
- ✅ **Benefit:** Avoids entire pipeline

**Layer 2: Retrieval Cache**
- ✅ Cache vector search results
- ✅ Key: Query embedding
- ✅ Hit: Skip retrieval (save 30-50ms)
- ✅ TTL: 15-60 minutes
- ✅ **Benefit:** Still personalizes response but skips retrieval

**Layer 3: Embedding Cache**
- ✅ Cache query embeddings
- ✅ Exact match only
- ✅ Hit: Skip embedding (save 20-50ms)
- ✅ TTL: 5-30 minutes
- ✅ **Benefit:** Useful for repeated exact queries

**Cache Hit Rates (Typical):**
- Semantic cache: 15-30% (high value)
- Retrieval cache: 20-40%
- Embedding cache: 30-50%

**Combined Latency:**
```
No cache: 200ms average
With caching: 60-100ms average (50% reduction)
```

**Cache Invalidation:**
- Knowledge base updates: Clear retrieval cache
- Model updates: Clear all caches
- Time-sensitive data: Aggressive TTLs

**Why NOT Others:**
- **A/B/C:** Single-layer caching misses optimization opportunities
- **D:** Multi-layer captures benefits at each stage

**Reference:** [Performance Optimization](edge-rag-optimization#caching)
</details>

---

### Question 12: SLA Definition for Production RAG

Defining SLA for customer-facing RAG chatbot. What metrics should be included?

A) Uptime only  
B) Uptime + average latency  
C) Uptime + P99 latency + quality score + error rate  
D) Uptime + cost per query

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: C**

**Explanation:**
**Comprehensive SLA covers availability, performance, quality, and reliability:**

**Production RAG SLA:**

**1. Availability:**
- ✅ **Uptime: 99.9%** (8.76 hours downtime/year)
- ✅ Measured: Service available and responding
- ✅ Excludes: Planned maintenance windows

**2. Latency:**
- ✅ **P50 Latency: < 300ms**
- ✅ **P95 Latency: < 800ms**
- ✅ **P99 Latency: < 1500ms**
- ✅ Measured: End-to-end query → response time

**3. Quality:**
- ✅ **Quality Score: > 90%** (human evaluation)
- ✅ **Relevance Rate: > 95%** (retrieval accuracy)
- ✅ Measured: Weekly sample evaluation (100 queries)

**4. Reliability:**
- ✅ **Error Rate: < 0.5%**
- ✅ Errors: Timeouts, failures, crashes
- ✅ Excludes: User input errors

**Example SLA:**
```
Service Level Agreement: Enterprise RAG Chatbot

Availability: 99.9% uptime
Performance:
  - P50 latency < 300ms
  - P99 latency < 1500ms
Quality:
  - Response quality > 90% satisfaction
  - Retrieval relevance > 95%
Reliability:
  - Error rate < 0.5%
  - No data loss
Reporting: Monthly SLA report
Credits: Downtime > 0.1% = 10% service credit
```

**Why NOT Others:**
- **A:** Uptime insufficient; users need performance guarantees
- **B:** Average latency misleading (hides tail latencies)
- **D:** Cost not customer-facing SLA metric

**Reference:** [Enterprise Operations](edge-rag-production#sla-management)
</details>

---

### Question 13: Disaster Recovery for Edge RAG

Production edge RAG system loses connectivity to management plane. What ensures continued operation?

A) Automatic failover to cloud RAG  
B) Local autonomy: Model + knowledge base + monitoring all edge-local  
C) Queue queries until connectivity restored  
D) Shut down gracefully

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
**Local autonomy** is core design principle for edge systems:

**Edge Autonomy Architecture:**

**1. Local Model Deployment:**
- ✅ Model files stored on edge
- ✅ No cloud dependencies for inference
- ✅ Continues operating during outage

**2. Local Knowledge Base:**
- ✅ Vector database edge-hosted
- ✅ Full index locally available
- ✅ Retrieval works offline

**3. Local Monitoring:**
- ✅ Metrics collected locally
- ✅ Local time-series database
- ✅ Alerts generated locally
- ✅ Syncs to cloud when available

**4. Local Configuration:**
- ✅ Config cached locally
- ✅ Policies enforced edge-side
- ✅ No remote dependencies

**Degraded Mode Operations:**
```
Cloud Connected:
✅ Full functionality
✅ Telemetry streaming
✅ Remote updates

Cloud Disconnected:
✅ Inference continues
✅ Retrieval continues
✅ Local monitoring active
⚠️ No model updates (acceptable)
⚠️ Telemetry queued (acceptable)
```

**Why NOT Others:**
- **A:** Failover defeats edge purpose; adds cloud dependency
- **C:** Queueing degrades user experience unacceptably
- **D:** Shutting down violates availability SLA

**Edge First Principle:** Design for disconnected operation as default.

**Reference:** [Production Architecture](edge-rag-architecture-production#resilience)
</details>

---

### Question 14: Cost Optimization

Edge RAG deployment costs $10K/month. What provides BEST cost reduction without sacrificing quality?

A) Use smaller model (70% cost reduction, 20% quality loss)  
B) Implement model quantization + caching (40% cost reduction, 2% quality loss)  
C) Reduce knowledge base size by 50%  
D) Increase query latency limits

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
**Quantization + caching** provides best cost/quality trade-off:

**Cost Optimization Strategy:**

**1. Model Quantization (INT8):**
- ✅ **Cost Impact:** -25% (smaller hardware, less memory)
- ✅ **Quality Impact:** -1-3%
- ✅ Memory: 50% reduction
- ✅ Inference: 20-30% faster
- ✅ Can use smaller/cheaper edge hardware

**2. Response Caching:**
- ✅ **Cost Impact:** -15% (reduced inference load)
- ✅ **Quality Impact:** None (same responses)
- ✅ Cache hit rate: 20-30%
- ✅ Reduced compute cycles

**3. Batch Processing for Updates:**
- ✅ **Cost Impact:** -5% (efficient resource use)
- ✅ Process knowledge base updates in off-peak
- ✅ Amortize embedding costs

**Total Cost Reduction: 40%**
**Total Quality Impact: -2%**

**Cost Breakdown:**
```
Before Optimization:
- Hardware: $4K/month
- Inference compute: $3K/month
- Storage: $2K/month
- Networking: $1K/month
Total: $10K/month

After Optimization:
- Hardware: $3K (-25% from quantization)
- Inference compute: $2K (-33% from caching + quantization)
- Storage: $2K (unchanged)
- Networking: $1K (unchanged)
Total: $6K/month (40% reduction)
```

**Why NOT Others:**
- **A:** 20% quality loss unacceptable for production
- **C:** Reducing knowledge base impacts usefulness
- **D:** Latency increases hurt user experience

**Reference:** [Cost Optimization](edge-rag-production#cost-management)
</details>

---

### Question 15: MLOps - Retraining Triggers

RAG model should be retrained. Which combination of signals indicates retraining is needed?

A) Query volume increased 20%  
B) Data drift > 0.3 + quality score < 85% + user complaints  
C) New hardware available  
D) Monthly schedule reached

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
**Multiple converging signals** indicate genuine need for retraining:

**Retraining Decision Matrix:**

**Signal 1: Data Drift (Quantitative)**
- ✅ KL divergence > 0.3 threshold
- ✅ Query distribution shifted from training data
- ✅ New topics/vocabulary emerging

**Signal 2: Quality Degradation (Quantitative)**
- ✅ Quality score < 85% (from baseline 92%)
- ✅ P95 latency increasing
- ✅ Retrieval relevance declining

**Signal 3: User Feedback (Qualitative)**
- ✅ Complaint volume increased 2x
- ✅ Negative sentiment in feedback
- ✅ Specific quality issues reported

**Decision Logic:**
```
if (data_drift > 0.3 AND quality_score < 85%) OR user_complaints > threshold:
    evaluate_retraining_benefit()
    if benefit > cost:
        initiate_retraining()
```

**Retraining Cost-Benefit:**
- **Cost:** Compute, data collection, validation, deployment (1-2 weeks)
- **Benefit:** Quality improvement, user satisfaction, reduced complaints

**Why NOT Others:**
- **A:** Volume increase doesn't indicate model issues
- **C:** Hardware availability not a retraining driver
- **D:** Schedule-based retraining may be wasteful or insufficient

**Avoid Over-Retraining:**
- Retraining has costs (time, compute, validation)
- Only retrain when clear benefit
- Typical frequency: Quarterly or trigger-based

**Reference:** [MLOps Workflows](edge-rag-mlops#retraining)
</details>

---

### Question 16: Knowledge Base Version Control

Managing multiple knowledge base versions across edge sites. What versioning strategy is BEST?

A) Single latest version deployed everywhere  
B) Semantic versioning with controlled rollout and rollback capability  
C) Each site maintains its own version independently  
D) No versioning; continuous updates

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
**Semantic versioning with rollout control** provides safety and consistency:

**Versioning Strategy:**

**Semantic Versioning (SemVer):**
```
Version Format: MAJOR.MINOR.PATCH
Example: 2.3.1

MAJOR (2): Breaking changes (schema change, major content restructure)
MINOR (3): New content added (new documents, sections)
PATCH (1): Corrections/updates (fixes, small updates)
```

**Version Metadata:**
```json
{
  "version": "2.3.1",
  "created": "2025-10-15",
  "documents": 10483,
  "vectors": 10483000,
  "size_gb": 87.5,
  "changelog": "Added Q4 2025 regulatory updates",
  "compatible_models": ["v1.2.x", "v1.3.x"]
}
```

**Controlled Rollout:**

**Phase 1: Staging (1 site, 48 hours)**
- Deploy to staging environment
- Validate quality
- Check compatibility

**Phase 2: Canary (5% sites, 1 week)**
- Deploy to 5% of edge sites
- Monitor query quality
- Check for issues

**Phase 3: Production (100%, 2 weeks)**
- Gradual rollout
- Per-site validation
- Automated rollback on failure

**Rollback Capability:**
- Keep previous 2 versions on edge
- One-command rollback
- < 10 minute rollback time

**Why NOT Others:**
- **A:** No rollback; risky for quality issues
- **C:** Version fragmentation; inconsistent experience
- **D:** Continuous updates lack validation gates

**Reference:** [Knowledge Base Management](edge-rag-architecture-production#versioning)
</details>

---

### Question 17: Performance Troubleshooting

Production RAG P99 latency increased from 800ms to 2500ms. What is the FIRST diagnostic step?

A) Restart all edge services  
B) Review monitoring dashboards for component-level latency breakdown  
C) Scale up edge hardware immediately  
D) Switch to smaller model

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
**Component-level analysis** identifies the bottleneck before taking action:

**Latency Breakdown Analysis:**

**Healthy Baseline:**
```
Query → Embedding: 50ms
Embedding → Retrieval: 80ms
Retrieval → LLM: 30ms
LLM Inference: 500ms
Response Processing: 40ms
Total: 700ms ✅
```

**Current (Degraded):**
```
Query → Embedding: 50ms (unchanged)
Embedding → Retrieval: 80ms (unchanged)
Retrieval → LLM: 30ms (unchanged)
LLM Inference: 2200ms ❌ (4.4x increase!)
Response Processing: 40ms (unchanged)
Total: 2400ms
```

**Root Cause Identified: LLM Inference**

**Next Steps:**
1. Check GPU/CPU utilization (thermal throttling?)
2. Check concurrent requests (resource contention?)
3. Review recent model changes
4. Check system logs for errors

**Common Causes:**
- ✅ Resource contention (too many concurrent queries)
- ✅ Hardware degradation (thermal throttling, memory issues)
- ✅ Model change (accidental switch to larger model)
- ✅ Batch size misconfiguration

**Why NOT Others:**
- **A:** Restart doesn't address root cause; may hide symptoms temporarily
- **C:** Scale up expensive; may not solve problem if software issue
- **D:** Model change too drastic without diagnosis

**Monitoring Best Practice:** Always instrument each pipeline stage separately.

**Reference:** [Performance Monitoring](edge-rag-production#monitoring)
</details>

---

### Question 18: Enterprise Governance

Multi-tenant RAG system must ensure data isolation. What architecture enforces STRONGEST isolation?

A) Logical isolation: Single model + vector DB, filter by tenant ID  
B) Physical isolation: Separate model instance + vector DB per tenant  
C) Shared model + separate vector DB per tenant  
D) Separate models + shared vector DB with encryption

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
**Physical isolation** provides strongest security and compliance:

**Multi-Tenant Isolation Options:**

**Option A: Logical Isolation**
```
Architecture:
- Single model instance
- Single vector database
- Row-level security (tenant_id filter)

Pros: Cost-efficient, easy management
Cons:
❌ Risk of query/response leakage (bug/misconfiguration)
❌ Noisy neighbor problem
❌ Difficult to prove isolation for compliance
```

**Option B: Physical Isolation (RECOMMENDED)**
```
Architecture:
- Separate model instance per tenant
- Separate vector database per tenant
- Separate compute/memory/storage

Pros:
✅ Complete isolation (bug cannot leak data)
✅ Independent scaling per tenant
✅ Clear compliance story
✅ Tenant-specific customization

Cons: Higher cost, more complex management
```

**Option C: Hybrid**
```
Architecture:
- Shared model (reasonable)
- Separate vector DB per tenant (good)

Pros: Balanced
Cons:
⚠️ Model could theoretically leak between tenants
⚠️ Moderate compliance risk
```

**Option D: Inverted Hybrid**
```
Architecture:
- Separate models (good)
- Shared vector DB (bad)

Cons:
❌ Defeats purpose; vector DB leakage risk highest
```

**Recommendation for Sovereign/Regulated:**
- Use **Option B** for high-security environments
- Accept higher cost for compliance assurance
- Use containerization/K8s for management at scale

**Cost Management:**
- Use quantized models (lower memory)
- Schedule model unloading for inactive tenants
- Optimize vector DB storage

**Reference:** [Enterprise Governance](edge-rag-production#multi-tenancy)
</details>

---

## Scoring Guide

### Score Interpretation

🏆 **17-18 correct (94-100%):** Expert! Production RAG mastery
- You can architect enterprise RAG systems
- You understand MLOps best practices for edge AI
- You're ready to lead production deployments
- Ready for principal architect/engineering roles

✅ **14-16 correct (78-89%):** Strong! Advanced proficiency
- You have solid production RAG knowledge
- Review missed topics to achieve expert level
- Ready for senior engineering roles

⚠️ **12-13 correct (67-72%):** Good - Additional practice recommended
- Solid foundation but gaps in advanced operations
- Review MLOps and optimization sections
- Complete hands-on labs

❌ **Below 12 correct (<67%):** Needs Improvement - Comprehensive review required
- Revisit production RAG and MLOps modules
- Complete all hands-on labs
- Consider additional real-world practice

---

## Study Recommendations

### If you missed questions on Architecture & Design (Q1-3)

**Focus Areas:**
- Review [Production Architecture](edge-rag-architecture-production)
- Study model selection criteria
- Understand vector database trade-offs
- Practice architecture design exercises

### If you missed questions on Retrieval & Optimization (Q4-5, Q11)

**Focus Areas:**
- Review [Performance Optimization](edge-rag-optimization)
- Study reranking techniques
- Learn chunking strategies
- Understand caching patterns

### If you missed questions on MLOps (Q6-7, Q15-16)

**Focus Areas:**
- Review [MLOps Workflows](edge-rag-mlops)
- Study deployment patterns
- Understand monitoring strategies
- Learn versioning best practices

### If you missed questions on Operations (Q8-10, Q12-14)

**Focus Areas:**
- Review [Enterprise Operations](edge-rag-production)
- Study SLA definitions
- Learn cost optimization
- Practice performance tuning

### If you missed questions on Troubleshooting & Governance (Q13, Q17-18)

**Focus Areas:**
- Review disaster recovery patterns
- Study multi-tenancy architectures
- Learn troubleshooting methodologies
- Understand compliance requirements

---

## Next Steps

After completing this assessment:

### 1. 🎯 Course Completion
- **Congratulations!** You've completed all Level 300 assessments
- **Previous Quiz:** [Zero Trust & Troubleshooting Quiz](zero-trust-troubleshooting-quiz)
- **Back to Start:** [Level 300 Overview](README)

### 2. 📚 Deep Dive Content
- [Production Architecture](edge-rag-architecture-production)
- [Performance Optimization](edge-rag-optimization)
- [MLOps Workflows](edge-rag-mlops)
- [Production Lab](edge-rag-production-lab)

### 3. 🔗 Related Content
- [Level 200 RAG Implementation](../level-200/edge-rag-implementation)
- [Troubleshooting](troubleshooting)
- [Zero Trust Architecture](zero-trust-architecture)

### 4. 🌐 External Resources
- [Azure Machine Learning MLOps](https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment)
- [RAG Best Practices](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview)
- [Vector Search Optimization](https://learn.microsoft.com/en-us/azure/search/vector-search-overview)
- [Edge AI Deployment](https://learn.microsoft.com/en-us/azure/azure-local/manage/edge-inference-optimization)

### 5. ✋ Need Help?
- Review [CONTRIBUTING.md](../../CONTRIBUTING.md)
- Check [README](../../README) for overall program
- Share feedback on course content

---

**Quiz Version:** 1.0  
**Last Updated:** November 2025  
**Total Questions:** 18  
**Passing Score:** 14/18 (78%)  
**Level:** 300 - Advanced/Expert
