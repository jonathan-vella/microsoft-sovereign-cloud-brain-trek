---
layout: default
title: Edge RAG Knowledge Check
parent: Module 5 - Edge RAG Concepts
nav_order: 5.4
---

# Edge RAG Knowledge Check

{: .no_toc }

Test your understanding of Edge RAG concepts, architecture, and implementation.

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

### Question 1: RAG Fundamentals

**What is the primary advantage of RAG over a traditional LLM?**

A) RAG is always faster than LLMs  
B) RAG grounds responses in retrieved documents, reducing hallucinations and enabling citations  
C) RAG doesn't require any LLM  
D) RAG uses smaller models

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
RAG's primary advantage is grounding LLM responses in retrieved documents, which reduces hallucinations (false information), enables source citations, and provides answers based on current, relevant information. Speed varies, RAG still uses an LLM (just augments it), and model size is independent of using RAG.

**Reference:** [Traditional LLMs vs. RAG](edge-rag-concepts#traditional-llms-vs-rag-augmented-systems)
</details>

---

### Question 2: Knowledge Cutoff

**How does RAG address the knowledge cutoff problem of LLMs?**

A) By retraining the LLM daily  
B) By retrieving current documents from a knowledge base that can be updated without retraining  
C) By using a larger model  
D) It doesn't address this problem

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
RAG solves the knowledge cutoff problem by retrieving information from a knowledge base that can be updated at any time without retraining the LLM. The LLM generates answers based on these retrieved, current documents. Retraining is expensive and impractical for daily updates, model size doesn't affect knowledge cutoff, and RAG specifically addresses this problem.

**Reference:** [RAG Fundamentals](rag-fundamentals#traditional-llms-and-their-limitations)
</details>

---

### Question 3: Edge Deployment

**Why deploy RAG "at the edge" rather than in the cloud?**

A) Edge deployment is always cheaper  
B) To maintain data sovereignty, reduce latency, and enable offline operation  
C) Edge hardware is more powerful  
D) Cloud deployment is not technically possible

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Edge deployment maintains data sovereignty (sensitive data stays on-premises), reduces latency (no internet round-trip), and enables offline operation (works during internet outages). Cost varies by scenario, cloud hardware is often more powerful, and cloud RAG deployment is certainly possible - edge is chosen for sovereignty and latency reasons.

**Reference:** [Edge RAG Benefits](edge-rag-concepts#edge-rag-definition-and-benefits)
</details>

---

### Question 4: Vector Embeddings

**What are embeddings in the context of RAG?**

A) Images embedded in documents  
B) Dense numerical vector representations of text that capture semantic meaning  
C) Hyperlinks between documents  
D) Document metadata

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Embeddings are dense numerical vectors (e.g., 384 or 1536 dimensions) that represent text in a way that captures semantic meaning. Similar meanings result in similar vectors, enabling semantic search. They're not images, hyperlinks, or metadata, though embeddings can be generated from any of these.

**Reference:** [Embedding Models](rag-fundamentals#embedding-models-and-representation-learning)
</details>

---

### Question 5: Vector Databases

**What is the primary function of a vector database in a RAG system?**

A) To store the LLM model weights  
B) To store document embeddings and enable fast similarity search  
C) To generate text responses  
D) To parse documents

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
A vector database stores document embeddings (vector representations) and enables fast similarity search to find documents most relevant to a query. It doesn't store LLM weights (those are in the model file), generate responses (LLM does that), or parse documents (done in ingestion pipeline).

**Reference:** [Vector Databases](rag-fundamentals#vector-databases-and-similarity-search)
</details>

---

### Question 6: Data Sovereignty

**In Edge RAG, what type of data stays on-premises?**

A) Only query logs  
B) Documents, embeddings, queries, and generated responses - all data  
C) Only the LLM model  
D) Nothing - all data is sent to cloud

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
In Edge RAG, ALL data stays on-premises: the documents/knowledge base, embeddings, user queries, and generated responses. This ensures complete data sovereignty and compliance with data residency requirements. The LLM model also runs locally.

**Reference:** [Data Sovereignty](edge-rag-concepts#connection-to-sovereign-cloud-strategies)
</details>

---

### Question 7: Chunking

**Why is document chunking necessary in RAG systems?**

A) To reduce storage costs  
B) To fit within LLM context window limits and improve retrieval precision  
C) To make documents load faster  
D) Chunking is not necessary

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Chunking breaks documents into smaller pieces to: 1) Fit within LLM context windows (typically 4K-32K tokens), and 2) Improve retrieval precision (retrieve only relevant sections, not entire documents). While it may help with storage and loading, those aren't the primary reasons.

**Reference:** [RAG Architecture](edge-rag-architecture#data-ingestion-and-indexing-pipeline)
</details>

---

### Question 8: LLM Selection

**For Edge RAG deployment, what is the trade-off with LLM model size?**

A) Larger models are always better with no downsides  
B) Larger models provide better quality but require more memory and are slower  
C) Smaller models are always preferred  
D) Model size doesn't matter

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Larger LLMs (e.g., 70B parameters) generally provide better quality responses but require significantly more GPU memory and are slower to generate responses. Smaller models (7B-13B) are faster and require less hardware but may produce lower quality outputs. The choice depends on quality requirements and available resources.

**Reference:** [Local LLM Deployment](edge-rag-architecture#local-llm-deployment-considerations)
</details>

---

### Question 9: Use Case Selection

**Which scenario is the BEST fit for Edge RAG?**

A) Public-facing website with general knowledge questions  
B) Healthcare facility needing to query patient records and clinical guidelines while maintaining HIPAA compliance  
C) Simple keyword search of public documents  
D) Real-time stock trading algorithms

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Healthcare with HIPAA requirements is ideal for Edge RAG because: 1) Sensitive patient data must stay on-premises, 2) Complex queries benefit from RAG's semantic understanding, 3) Citation of sources is important for clinical decisions. Public websites don't need edge deployment, keyword search doesn't need RAG, and trading algorithms require different technology.

**Reference:** [Customer Scenarios](edge-rag-concepts#scenario-1-healthcare-documentation-assistant-disconnected-edge)
</details>

---

### Question 10: Fine-Tuning vs. RAG

**When should you choose RAG over fine-tuning an LLM?**

A) When you need to change the model's writing style  
B) When you have frequently changing factual information that needs to be updated easily  
C) When you want to teach the model new vocabulary  
D) When you have unlimited budget and time

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
RAG is better for frequently changing factual information because you can update the knowledge base without retraining the model. Fine-tuning is better for changing style, teaching vocabulary, or task-specific behavior. RAG is actually more cost-effective than repeated fine-tuning.

**Reference:** [Fine-Tuning vs. RAG](rag-fundamentals#fine-tuning-vs-rag-trade-offs)
</details>

---

### Question 11: Retrieval Quality

**What is the most important factor for RAG system quality?**

A) The size of the LLM  
B) The speed of the vector database  
C) The quality and relevance of retrieved documents (retrieval quality)  
D) The user interface design

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: C**

**Explanation:**
Retrieval quality is the most critical factor - "garbage in, garbage out." If the system retrieves irrelevant or incorrect documents, even the best LLM will generate poor answers. While LLM size, database speed, and UI matter, retrieval quality is foundational to RAG success.

**Reference:** [RAG Fundamentals](rag-fundamentals#evaluation-metrics-for-rag-systems)
</details>

---

### Question 12: Hallucinations

**How does RAG reduce LLM hallucinations?**

A) By using a larger model  
B) By providing relevant factual context from retrieved documents that the LLM must base its answer on  
C) By training the model more  
D) RAG doesn't reduce hallucinations

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
RAG reduces hallucinations by providing the LLM with relevant, factual documents as context and instructing it to base answers only on that context. This grounds the response in real information rather than allowing the model to generate potentially false content from its training. Model size and additional training are not RAG techniques.

**Reference:** [Why RAG for Enterprise](edge-rag-concepts#why-rag-for-enterprise-applications)
</details>

---

### Question 13: Hardware Requirements

**What is the most critical hardware component for running Edge RAG?**

A) Large hard drives  
B) Fast CPU  
C) GPU with sufficient VRAM for the LLM  
D) Network card

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: C**

**Explanation:**
GPU with sufficient VRAM is most critical for running the LLM efficiently. LLMs are computationally intensive and benefit greatly from GPU acceleration. VRAM requirements vary by model size (24GB for 7B, 40-80GB for 13B-70B). While storage, CPU, and networking matter, the GPU is the bottleneck for LLM inference.

**Reference:** [Hardware Requirements](edge-rag-architecture#hardware-requirements)
</details>

---

### Question 14: Hybrid Deployment

**What is a "hybrid" Edge RAG deployment?**

A) Using both GPUs and CPUs  
B) Combining local Edge RAG for sensitive data with cloud services for general queries  
C) Using multiple LLMs  
D) Mixing different document types

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Hybrid Edge RAG deploys RAG locally for sensitive data that must stay on-premises while optionally using cloud services (like Azure OpenAI) for general, non-sensitive queries. This balances sovereignty requirements with the convenience of cloud AI. Using both GPUs and CPUs is standard, not "hybrid deployment."

**Reference:** [Scenario 4: Research Lab](edge-rag-concepts#scenario-4-research-lab-data-analysis-hybrid)
</details>

---

### Question 15: ROI

**What is typically the largest source of ROI for Edge RAG implementations?**

A) Hardware cost savings  
B) Reduced cloud API costs  
C) Time savings from faster access to information and improved productivity  
D) Reduced training costs

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: C**

**Explanation:**
The largest ROI typically comes from time savings - employees finding information 50-80% faster, making better decisions, and being more productive. While reduced cloud costs and training costs contribute, the productivity gains from instant access to organizational knowledge usually provide the largest financial benefit.

**Reference:** [ROI and Business Value](edge-rag-use-cases#roi-and-business-value)
</details>

---

## Scoring Guide

**Calculate your score:**

- Count the number of correct answers
- Divide by 15 and multiply by 100 for percentage

**Score Interpretation:**

**12-15 correct (80-100%):** ✅ **Excellent!** You have a strong understanding of Edge RAG concepts.

- Ready to proceed to next level or module
- Consider reviewing missed questions for completeness

**10-11 correct (67-79%):** ⚠️ **Good progress, but review needed**

- Review the module content, especially areas where you missed questions
- Pay attention to RAG architecture and deployment patterns
- Revisit fundamentals like embeddings and vector databases
- Retake quiz after review

**7-9 correct (47-66%):** ❌ **More study required**

- Thoroughly review all module content
- Focus on core concepts: RAG fundamentals, edge deployment benefits, architecture
- Review customer scenarios to understand real-world applications
- Consider hands-on practice if available
- Retake quiz after comprehensive review

**0-6 correct (0-46%):** ❌ **Significant review needed**

- Start from the beginning with [Edge RAG Concepts](edge-rag-concepts)
- Read each sub-page carefully: RAG Fundamentals, Architecture, Use Cases
- Take notes on key concepts
- Review all scenarios
- Consider additional resources on RAG and LLMs
- Retake quiz only after thorough review

---

## Study Recommendations

**If you missed questions on RAG fundamentals (Q1, Q2, Q4, Q12):**

- Review [Edge RAG Concepts](edge-rag-concepts)
- Review [RAG Fundamentals](rag-fundamentals)

**If you missed questions on deployment (Q3, Q6, Q13, Q14):**

- Review [Edge RAG Architecture](edge-rag-architecture)

**If you missed questions on implementation (Q7, Q8, Q10, Q11):**

- Review [RAG Fundamentals](rag-fundamentals)
- Review [Edge RAG Architecture](edge-rag-architecture)

**If you missed questions on use cases (Q9, Q15):**

- Review [Edge RAG Use Cases](edge-rag-use-cases)
- Review customer scenarios in [Edge RAG Concepts](edge-rag-concepts)

---

## Next Steps

**After completing this assessment:**

1. **✅ Congratulations!** You've completed all Level 100 foundation modules!

2. **📚 Review other Level 100 modules if needed:**
   - [Digital Sovereignty](digital-sovereignty)
   - [Sovereign Cloud Models](sovereign-cloud-models)
   - [Azure Local Overview](azure-local-overview)
   - [Azure Arc Introduction](azure-arc-intro)

3. **🎯 Prepare for Level 200:**
   - Level 200 provides intermediate deep dives into architecture and implementation

4. **🌐 Explore external resources:**
   - [LangChain Documentation](https://python.langchain.com/)
   - [LlamaIndex Documentation](https://gpt-index.readthedocs.io/)
   - [Hugging Face](https://huggingface.co/)
   - [Azure AI Documentation](https://learn.microsoft.com/azure/ai-services/)

5. **💡 Consider hands-on practice:**
   - Build a simple RAG system locally
   - Experiment with different embedding models
   - Explore vector database options

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

**[← Back to Edge RAG Concepts](edge-rag-concepts)**
