---
layout: default
title: "Lab 3: Edge RAG Setup"
parent: Hands-On Labs Overview
nav_order: 3
---

# Lab 3: Edge RAG Setup

{: .warning }
> **🚧 Lab Under Development**  
> This lab content is complete but hands-on exercises are currently being validated and refined.  
> **Expected Release:** Q1 2026  
> You can review the lab steps and prepare your environment in advance.

{: .warning }
> **🚧 Lab Under Development**  
> This lab content is complete but hands-on exercises are currently being validated and refined.  
> **Expected Release:** Q1 2026  
> You can review the lab steps and prepare your environment in advance.

{: .warning }
> **🚧 Lab Under Development**  
> This lab content is complete but hands-on exercises are currently being validated and refined.  
> **Expected Release:** Q1 2026  
> You can review the lab steps and prepare your environment in advance.

## Objective

Deploy a complete Edge RAG (Retrieval-Augmented Generation) solution on Azure Local, including vector database, embedding models, LLM inference engine, and RAG pipeline. This is the most comprehensive lab demonstrating AI at the edge.

---

## Pre-Lab Checklist

```text
PREREQUISITES
═════════════════════════════════════════════════════════════

Required:
☐ Completion of Lab 1 (Azure Local) and Lab 2 (Arc)
☐ Azure subscription with resources from prior labs
☐ 8+ GB RAM available for containers
☐ 50+ GB disk space for models
☐ Docker/Podman installed locally
☐ Python 3.10+ (for RAG script)
☐ curl or Postman for API testing

Optional but Recommended:
☐ GPU (NVIDIA/AMD) for model acceleration
☐ LLM model experience
☐ Vector database knowledge (Weaviate/Qdrant)
☐ REST API debugging tools

Estimated Time: 3-4 hours
Difficulty: Advanced
Cost: $50-100 Azure credits (GPU usage)
```

---

## Lab Architecture

```text
EDGE RAG SYSTEM ARCHITECTURE
═════════════════════════════════════════════════════════════

Azure Local (On-Premises)
┌─────────────────────────────────────────────────────────┐
│ Edge RAG Solution                                       │
│                                                         │
│ ┌────────────────────────────────────────────────────┐ │
│ │ RAG Application Layer                              │ │
│ │ ├─ FastAPI/Flask RAG Endpoint (:8000)             │ │
│ │ ├─ Document Ingestion Service                      │ │
│ │ └─ Query Processing Pipeline                       │ │
│ └────────────────────────────────────────────────────┘ │
│          ↓           ↓           ↓                      │
│ ┌─────────────┬───────────────┬──────────────┐        │
│ │ Embedding   │ Vector Store  │ LLM Inference│        │
│ │ Model       │ (Weaviate)    │ Engine       │        │
│ │ (LLaMA-    │ (:8080)       │ (Ollama:11434)       │
│ │ Embeddings) │               │              │        │
│ └─────────────┴───────────────┴──────────────┘        │
│                                                         │
│ ┌────────────────────────────────────────────────────┐ │
│ │ Storage & Persistence                              │ │
│ │ ├─ Volume: /data/weaviate (vector store)          │ │
│ │ ├─ Volume: /data/ollama (model cache)             │ │
│ │ └─ Volume: /data/documents (ingested docs)        │ │
│ └────────────────────────────────────────────────────┘ │
│                                                         │
│ ┌────────────────────────────────────────────────────┐ │
│ │ Monitoring & Logging                               │ │
│ │ ├─ Prometheus metrics (:9090)                      │ │
│ │ ├─ Loki logs aggregation (:3100)                   │ │
│ │ └─ Grafana dashboards (:3000)                      │ │
│ └────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
          ↓ (Arc Integration)
┌─────────────────────────────────────────────────────────┐
│ Azure (Monitoring & Backup)                             │
│ ├─ Azure Monitor ingests metrics                        │
│ ├─ Log Analytics receives logs                          │
│ └─ Storage Account backs up embeddings                  │
└─────────────────────────────────────────────────────────┘
```

---

## Lab Steps

### Step 1: Prepare Edge RAG Environment

**Objective:** Set up prerequisites and namespace for RAG system

**Step 1.1: Create Namespace**

```powershell
# Create dedicated namespace for RAG
kubectl create namespace edge-rag

# Label namespace for monitoring
kubectl label namespace edge-rag monitoring=enabled

# Verify namespace
kubectl get namespace edge-rag
```

**Expected Output:** Namespace "edge-rag" created

**Step 1.2: Create Storage for Models and Data**

```powershell
# Create PVC for persistent storage
@"
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: rag-data-pvc
  namespace: edge-rag
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 50Gi
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: weaviate-pvc
  namespace: edge-rag
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 30Gi
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: ollama-pvc
  namespace: edge-rag
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 20Gi
"@ | kubectl apply -f -

# Verify PVCs
kubectl get pvc -n edge-rag
```

**Expected Output:** Three PVCs created and bound

**Step 1.3: Create ConfigMap for RAG Configuration**

```powershell
# Create configuration for RAG pipeline
@"
apiVersion: v1
kind: ConfigMap
metadata:
  name: rag-config
  namespace: edge-rag
data:
  rag-settings.yaml: |
    vector_store:
      type: weaviate
      url: http://weaviate:8080
      batch_size: 50
      consistency_level: ALL

    embeddings:
      model: sentence-transformers/all-MiniLM-L6-v2
      device: cpu
      batch_size: 32

    llm:
      engine: ollama
      url: http://ollama:11434
      model: mistral
      temperature: 0.7
      max_tokens: 512

    retrieval:
      top_k: 5
      similarity_threshold: 0.7

    ingestion:
      chunk_size: 512
      chunk_overlap: 50
      document_path: /data/documents
"@ | kubectl apply -f -

# Verify ConfigMap
kubectl get configmap -n edge-rag
```

**Expected Output:** ConfigMap "rag-config" created

---

### Step 2: Deploy Vector Database (Weaviate)

**Objective:** Set up Weaviate vector database for embedding storage

**Step 2.1: Deploy Weaviate Service**

```powershell
# Deploy Weaviate vector database
@"
apiVersion: apps/v1
kind: Deployment
metadata:
  name: weaviate
  namespace: edge-rag
spec:
  replicas: 1
  selector:
    matchLabels:
      app: weaviate
  template:
    metadata:
      labels:
        app: weaviate
    spec:
      containers:
      - name: weaviate
        image: semitechnologies/weaviate:1.18.0
        ports:
        - containerPort: 8080
          name: graphql
        - containerPort: 50051
          name: grpc
        env:
        - name: AUTHENTICATION_APIKEY_ENABLED
          value: "false"
        - name: PERSISTENCE_DATA_PATH
          value: /var/lib/weaviate
        - name: ENABLE_MODULES
          value: "text2vec-transformers,text2vec-openai"
        resources:
          requests:
            memory: "2Gi"
            cpu: "1000m"
          limits:
            memory: "4Gi"
            cpu: "2000m"
        livenessProbe:
          httpGet:
            path: /v1/.well-known/ready
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /v1/.well-known/ready
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 5
        volumeMounts:
        - name: weaviate-storage
          mountPath: /var/lib/weaviate
      volumes:
      - name: weaviate-storage
        persistentVolumeClaim:
          claimName: weaviate-pvc
---
apiVersion: v1
kind: Service
metadata:
  name: weaviate
  namespace: edge-rag
spec:
  type: ClusterIP
  ports:
  - port: 8080
    targetPort: 8080
    name: graphql
  - port: 50051
    targetPort: 50051
    name: grpc
  selector:
    app: weaviate
"@ | kubectl apply -f -

# Wait for deployment
Write-Host "Weaviate deploying (2-3 minutes)..."
kubectl wait --for=condition=ready pod -l app=weaviate -n edge-rag --timeout=300s

# Verify service
kubectl get svc -n edge-rag
kubectl get pods -n edge-rag
```

**Expected Output:** Weaviate pod running, service created

**Step 2.2: Verify Weaviate Health**

```powershell
# Port-forward to test locally (optional)
# kubectl port-forward -n edge-rag svc/weaviate 8080:8080 &

# Get Weaviate pod IP for testing
$weaviatePod = kubectl get pods -n edge-rag -l app=weaviate -o jsonpath='{.items[0].metadata.name}'
$weaviateIP = kubectl get pod $weaviatePod -n edge-rag -o jsonpath='{.status.podIP}'

Write-Host "Weaviate Pod: $weaviatePod"
Write-Host "Weaviate IP: $weaviateIP"

# Test connectivity from another pod
kubectl run -it --rm debug --image=curlimages/curl -n edge-rag -- sh
# Inside pod: curl http://weaviate:8080/v1/.well-known/ready
```

**Expected Output:** Weaviate is ready and accessible

---

### Step 3: Deploy LLM Inference Engine (Ollama)

**Objective:** Set up Ollama for local LLM inference

**Step 3.1: Deploy Ollama Service**

```powershell
# Deploy Ollama for LLM inference
@"
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ollama
  namespace: edge-rag
spec:
  replicas: 1
  selector:
    matchLabels:
      app: ollama
  template:
    metadata:
      labels:
        app: ollama
    spec:
      containers:
      - name: ollama
        image: ollama/ollama:latest
        ports:
        - containerPort: 11434
          name: api
        env:
        - name: OLLAMA_MODELS_DIR
          value: /root/.ollama/models
        resources:
          requests:
            memory: "4Gi"
            cpu: "2000m"
          limits:
            memory: "8Gi"
            cpu: "4000m"
        livenessProbe:
          exec:
            command: ["sh", "-c", "curl -f http://localhost:11434/api/tags || exit 1"]
          initialDelaySeconds: 60
          periodSeconds: 30
        readinessProbe:
          exec:
            command: ["sh", "-c", "curl -f http://localhost:11434/api/tags || exit 1"]
          initialDelaySeconds: 30
          periodSeconds: 10
        volumeMounts:
        - name: ollama-storage
          mountPath: /root/.ollama
      volumes:
      - name: ollama-storage
        persistentVolumeClaim:
          claimName: ollama-pvc
---
apiVersion: v1
kind: Service
metadata:
  name: ollama
  namespace: edge-rag
spec:
  type: ClusterIP
  ports:
  - port: 11434
    targetPort: 11434
    name: api
  selector:
    app: ollama
"@ | kubectl apply -f -

# Wait for deployment
Write-Host "Ollama deploying (1-2 minutes)..."
kubectl wait --for=condition=ready pod -l app=ollama -n edge-rag --timeout=300s
```

**Expected Output:** Ollama pod running, service created

**Step 3.2: Pull and Verify Model**

```powershell
# Get Ollama pod name
$ollamaPod = kubectl get pods -n edge-rag -l app=ollama -o jsonpath='{.items[0].metadata.name}'

# Pull lightweight model (Mistral 7B)
# Note: First time takes 5-10 minutes for download
Write-Host "Pulling Mistral model (this may take several minutes)..."
kubectl exec -it $ollamaPod -n edge-rag -- ollama pull mistral

# Verify model is available
kubectl exec $ollamaPod -n edge-rag -- ollama list

# Test model responsiveness
kubectl exec $ollamaPod -n edge-rag -- ollama generate --model mistral "Hello, what is retrieval augmented generation?" | head -20
```

**Expected Output:** Model pulled and responding to queries

---

### Step 4: Deploy RAG Application

**Objective:** Deploy the RAG pipeline connecting embeddings, vector store, and LLM

**Step 4.1: Create RAG Application Image (Local Build)**

```powershell
# Create Dockerfile for RAG application
$dockerfile = @"
FROM python:3.10-slim

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir \
    fastapi==0.104.1 \
    uvicorn==0.24.0 \
    requests==2.31.0 \
    weaviate-client==3.25.0 \
    sentence-transformers==2.2.2 \
    torch==2.1.0 \
    PyYAML==6.0 \
    pydantic==2.5.0

# Copy RAG application
COPY app.py /app/
COPY rag_pipeline.py /app/
COPY config.yaml /app/

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
"@

$dockerfile | Out-File -Path Dockerfile

Write-Host "Dockerfile created"
```

**Step 4.2: Create RAG Pipeline Code**

```python
# Save as rag_pipeline.py
cat > rag_pipeline.py << 'EOF'
import requests
import json
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)

class RAGPipeline:
    def __init__(self, config: Dict):
        self.config = config
        self.weaviate_url = config['vector_store']['url']
        self.ollama_url = config['llm']['url']
        self.top_k = config['retrieval']['top_k']

    def embed_text(self, text: str) -> List[float]:
        """Generate embeddings for text"""
        try:
            # Use sentence-transformers locally
            from sentence_transformers import SentenceTransformer
            model = SentenceTransformer('all-MiniLM-L6-v2')
            embedding = model.encode(text, convert_to_tensor=True)
            return embedding.tolist()
        except Exception as e:
            logger.error(f"Embedding error: {e}")
            raise

    def store_document(self, doc_id: str, text: str, metadata: Dict) -> bool:
        """Store document in Weaviate"""
        try:
            embedding = self.embed_text(text)

            payload = {
                "class": "Document",
                "id": doc_id,
                "properties": {
                    "content": text,
                    "source": metadata.get("source", "unknown"),
                    "timestamp": metadata.get("timestamp", ""),
                },
                "vector": embedding
            }

            response = requests.post(
                f"{self.weaviate_url}/v1/objects",
                json=payload
            )
            return response.status_code == 200
        except Exception as e:
            logger.error(f"Storage error: {e}")
            raise

    def retrieve_context(self, query: str) -> List[str]:
        """Retrieve relevant documents for query"""
        try:
            query_embedding = self.embed_text(query)

            graphql_query = f"""
            {% raw %}{{
              Get {{
                Document(
                  nearVector: {{
                    vector: {query_embedding}
                  }}
                  limit: {self.top_k}
                ) {{
                  content
                  source
                }}
              }}
            }}{% endraw %}
            """

            response = requests.post(
                f"{self.weaviate_url}/v1/graphql",
                json={"query": graphql_query}
            )

            if response.status_code == 200:
                results = response.json().get("data", {}).get("Get", {}).get("Document", [])
                return [doc["content"] for doc in results]
            return []
        except Exception as e:
            logger.error(f"Retrieval error: {e}")
            raise

    def generate_answer(self, query: str, context: List[str]) -> str:
        """Generate answer using LLM with context"""
        try:
            context_text = "\n".join(context)
            prompt = f"""Context:
{context_text}

Question: {query}

Answer:"""

            response = requests.post(
                f"{self.ollama_url}/api/generate",
                json={
                    "model": "mistral",
                    "prompt": prompt,
                    "stream": False
                }
            )

            if response.status_code == 200:
                return response.json()["response"]
            raise Exception(f"Generation error: {response.status_code}")
        except Exception as e:
            logger.error(f"Generation error: {e}")
            raise

    def query(self, query: str) -> Dict:
        """Full RAG query pipeline"""
        try:
            context = self.retrieve_context(query)
            answer = self.generate_answer(query, context)
            return {
                "query": query,
                "answer": answer,
                "context_documents": len(context),
                "sources": [doc[:100] + "..." for doc in context]
            }
        except Exception as e:
            logger.error(f"Query error: {e}")
            return {
                "query": query,
                "error": str(e),
                "answer": "Unable to generate answer"
            }
EOF
```

**Step 4.3: Create FastAPI Application**

```python
# Save as app.py
cat > app.py << 'EOF'
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import yaml
import logging
from rag_pipeline import RAGPipeline

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Edge RAG Service", version="1.0.0")

# Load configuration
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Initialize RAG pipeline
rag_pipeline = RAGPipeline(config)

class QueryRequest(BaseModel):
    query: str

class DocumentRequest(BaseModel):
    doc_id: str
    content: str
    source: str = "unknown"

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/config")
async def get_config():
    return config

@app.post("/query")
async def query_endpoint(request: QueryRequest):
    try:
        result = rag_pipeline.query(request.query)
        return result
    except Exception as e:
        logger.error(f"Query failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ingest")
async def ingest_document(request: DocumentRequest):
    try:
        success = rag_pipeline.store_document(
            request.doc_id,
            request.content,
            {"source": request.source}
        )
        return {"success": success, "doc_id": request.doc_id}
    except Exception as e:
        logger.error(f"Ingestion failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/stats")
async def get_stats():
    return {
        "vector_store": config['vector_store']['url'],
        "llm_model": config['llm']['model'],
        "embeddings_model": config['embeddings']['model'],
        "retrieval_top_k": config['retrieval']['top_k']
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
EOF
```

**Step 4.4: Deploy RAG Service**

```powershell
# Deploy RAG application
@"
apiVersion: apps/v1
kind: Deployment
metadata:
  name: rag-api
  namespace: edge-rag
spec:
  replicas: 2
  selector:
    matchLabels:
      app: rag-api
  template:
    metadata:
      labels:
        app: rag-api
    spec:
      containers:
      - name: rag-api
        image: rag-service:latest
        imagePullPolicy: Never
        ports:
        - containerPort: 8000
          name: http
        env:
        - name: WEAVIATE_URL
          value: http://weaviate:8080
        - name: OLLAMA_URL
          value: http://ollama:11434
        resources:
          requests:
            memory: "2Gi"
            cpu: "1000m"
          limits:
            memory: "4Gi"
            cpu: "2000m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 10
          periodSeconds: 5
        volumeMounts:
        - name: rag-data
          mountPath: /data
      volumes:
      - name: rag-data
        persistentVolumeClaim:
          claimName: rag-data-pvc
---
apiVersion: v1
kind: Service
metadata:
  name: rag-api
  namespace: edge-rag
spec:
  type: LoadBalancer
  ports:
  - port: 8000
    targetPort: 8000
    name: http
  selector:
    app: rag-api
"@ | kubectl apply -f -

# Wait for deployment
Write-Host "RAG API deploying..."
kubectl wait --for=condition=ready pod -l app=rag-api -n edge-rag --timeout=300s
```

**Expected Output:** RAG API pods running

---

### Step 5: Test RAG Pipeline

**Objective:** Validate end-to-end RAG functionality

**Step 5.1: Ingest Sample Documents**

```powershell
# Get RAG API service IP
$ragApiIP = kubectl get service rag-api -n edge-rag -o jsonpath='{.status.loadBalancer.ingress[0].ip}'

Write-Host "RAG API available at: http://$ragApiIP:8000"

# Create sample documents
$doc1 = @{
    doc_id = "doc-001"
    content = "Azure Local is Microsoft's edge computing platform for sovereign cloud deployments. It enables organizations to run cloud services on-premises with guaranteed data residency and compliance."
    source = "Azure Local Overview"
}

$doc2 = @{
    doc_id = "doc-002"
    content = "Retrieval-Augmented Generation (RAG) combines the power of large language models with targeted document retrieval. This approach improves accuracy and reduces hallucinations by grounding responses in actual data."
    source = "RAG Fundamentals"
}

$doc3 = @{
    doc_id = "doc-003"
    content = "Azure Arc enables unified management of resources across on-premises, edge, and cloud environments. It provides policy enforcement, monitoring, and governance at scale for hybrid infrastructure."
    source = "Azure Arc Overview"
}

# Ingest documents
foreach ($doc in @($doc1, $doc2, $doc3)) {
    $response = Invoke-RestMethod -Uri "http://$ragApiIP:8000/ingest" `
        -Method Post `
        -ContentType "application/json" `
        -Body ($doc | ConvertTo-Json)

    Write-Host "Ingested: $($doc.doc_id) - $($response.success)"
}
```

**Expected Output:** Documents ingested successfully

**Step 5.2: Query RAG System**

```powershell
# Test RAG queries
$queries = @(
    "What is Azure Local?",
    "How does RAG work?",
    "Tell me about Azure Arc"
)

foreach ($query in $queries) {
    Write-Host "`nQuery: $query"
    Write-Host "─" * 60

    $response = Invoke-RestMethod -Uri "http://$ragApiIP:8000/query" `
        -Method Post `
        -ContentType "application/json" `
        -Body (@{ query = $query } | ConvertTo-Json)

    Write-Host "Answer: $($response.answer)"
    Write-Host "Sources: $($response.context_documents) documents"
}
```

**Expected Output:** RAG system returning contextual answers

**Step 5.3: Monitor Performance**

```powershell
# Check pod logs
kubectl logs -n edge-rag -l app=rag-api --tail=50

# Monitor resource usage
kubectl top nodes
kubectl top pods -n edge-rag

# Get RAG API stats
$stats = Invoke-RestMethod -Uri "http://$ragApiIP:8000/stats" -Method Get
Write-Host "RAG System Configuration:"
Write-Host ($stats | ConvertTo-Json -Depth 3)
```

**Expected Output:** All services healthy with reasonable resource usage

---

### Step 6: Configure Monitoring

**Objective:** Set up observability for RAG system

**Step 6.1: Add Prometheus Metrics**

```powershell
# Deploy Prometheus for metrics collection
@"
apiVersion: v1
kind: ConfigMap
metadata:
  name: prometheus-config
  namespace: edge-rag
data:
  prometheus.yml: |
    global:
      scrape_interval: 30s
    scrape_configs:
    - job_name: 'rag-api'
      static_configs:
      - targets: ['rag-api:8000']
    - job_name: 'weaviate'
      static_configs:
      - targets: ['weaviate:8080']
    - job_name: 'kubernetes'
      kubernetes_sd_configs:
      - role: pod
        namespaces:
          names:
          - edge-rag
"@ | kubectl apply -f -

Write-Host "Prometheus ConfigMap created"
```

**Step 6.2: Deploy Observability Stack**

```powershell
# Deploy Prometheus, Loki, and Grafana
Write-Host "In production, use Helm for full monitoring stack"
Write-Host "For this lab, monitoring is simplified via Kubernetes metrics"

# Verify metrics are available
kubectl top pods -n edge-rag
```

---

### Step 7: Validation and Performance Testing

**Objective:** Verify RAG system meets performance requirements

**Step 7.1: Load Testing**

```powershell
# Simple performance test
$queries = @(
    "What is sovereign cloud?",
    "Explain data residency",
    "What is edge computing?",
    "How does AI inference work?",
    "What is vector similarity?"
)

Write-Host "Running performance test..."
Write-Host "─" * 60

$results = @()

foreach ($query in $queries) {
    $start = Get-Date

    $response = Invoke-RestMethod -Uri "http://$ragApiIP:8000/query" `
        -Method Post `
        -ContentType "application/json" `
        -Body (@{ query = $query } | ConvertTo-Json)

    $duration = ((Get-Date) - $start).TotalMilliseconds

    $results += [PSCustomObject]@{
        Query = $query
        DurationMs = [math]::Round($duration, 2)
        Success = -not $response.error
    }
}

# Display results
$results | Format-Table -AutoSize
$avgTime = ($results.DurationMs | Measure-Object -Average).Average
Write-Host "`nAverage Response Time: $([math]::Round($avgTime, 2))ms"
```

**Expected Output:** Response times under 5 seconds, high success rate

**Step 7.2: Resource Efficiency Check**

```powershell
# Check resource efficiency
$podMetrics = kubectl top pods -n edge-rag

Write-Host "Resource Usage Summary:"
Write-Host "─" * 60

$podMetrics | ForEach-Object {
    $cpu = $_.CPU
    $mem = $_.MEMORY
    Write-Host "$($_.NAME): CPU=$cpu, Memory=$mem"
}

# Check storage usage
kubectl exec -it $(kubectl get pods -n edge-rag -l app=rag-api -o jsonpath='{.items[0].metadata.name}') -n edge-rag -- df -h /data
```

**Expected Output:** Efficient resource utilization

---

### Step 8: Next Steps and Scaling

**Objective:** Plan for production deployment

**Step 8.1: Document System Capacity**

```powershell
# Get current deployment info
Write-Host "Current RAG System Configuration:"
Write-Host "═" * 60

$deploymentInfo = kubectl get deployment -n edge-rag -o jsonpath='{.items[*].spec.replicas}' | Measure-Object -Sum
Write-Host "Total Replicas: $($deploymentInfo.Sum)"

$serviceInfo = kubectl get service -n edge-rag
Write-Host "Services: $($serviceInfo.Count - 1)"

$pvcInfo = kubectl get pvc -n edge-rag
Write-Host "Storage Allocated: $(($pvcInfo | Measure-Object).Count) PVCs"

Write-Host "`nScaling Recommendations:"
Write-Host "- RAG API: Current 2 replicas, can scale to 5+"
Write-Host "- Weaviate: Requires persistent storage, single instance optimal"
Write-Host "- Ollama: Consider GPU-enabled node for better performance"
```

**Step 8.2: Export Configuration for Lab 4**

```powershell
# Export current RAG setup for reference in Lab 4
kubectl get all -n edge-rag -o yaml > edge-rag-backup.yaml

Write-Host "Configuration exported to edge-rag-backup.yaml"
Write-Host "This will be referenced in Lab 4 for policy governance"
```

---

## Learning Outcomes

### What You Learned

✓ Edge RAG architecture and components
✓ Vector database deployment (Weaviate)
✓ LLM inference at the edge (Ollama)
✓ Embedding generation and vector search
✓ RAG pipeline implementation
✓ API endpoint design for ML workloads
✓ Performance monitoring for AI applications
✓ Resource optimization for inference

### Skills Gained

✓ Deploy production-grade vector databases
✓ Configure local LLM inference engines
✓ Build RAG applications with Python/FastAPI
✓ Manage AI model lifecycle at the edge
✓ Monitor and optimize ML workload performance
✓ Design scalable inference architectures
✓ Integrate AI with existing infrastructure

### Knowledge Applied From Previous Modules

✓ **Module 1 (Azure Local):** Deployed on Azure Local compute
✓ **Module 2 (Arc):** Integrated with Arc management in Lab 2
✓ **Module 3 (Edge RAG):** Core content for this lab

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Ollama model pull timeout | Increase timeout or use smaller model (tinyllama) |
| Weaviate connection errors | Check Pod IP: `kubectl get pods -n edge-rag -o wide` |
| RAG API pods crashing | Check logs: `kubectl logs <pod> -n edge-rag` |
| Out of memory errors | Reduce model size or increase Pod limits |
| Embedding generation slow | Consider GPU or batch processing |
| Vector search returning no results | Verify documents were ingested: check Weaviate logs |

---

_Last Updated: October 21, 2025_
