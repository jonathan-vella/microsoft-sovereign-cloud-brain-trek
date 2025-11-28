---
layout: default
title: "Lab 1: Azure Local Deployment"
parent: Hands-On Labs Overview
nav_order: 1
---

# Lab 1: Azure Local Deployment

{: .warning }
> **🚧 Lab Under Development**  
> This lab content is complete but hands-on exercises are currently being validated and refined.  
> **Expected Release:** Q1 2026  
> You can review the lab steps and prepare your environment in advance.

## Objective

Deploy and configure Azure Local in connected mode, including networking, storage, and a sample workload. This lab simulates the deployment process and validates connectivity.

---

## Pre-Lab Checklist

```text
PREREQUISITES
═════════════════════════════════════════════════════════════

Required:
☐ Azure subscription with Owner or Contributor role
☐ Azure CLI installed (version 2.50+)
☐ PowerShell 7+ installed
☐ kubectl installed (for Kubernetes validation)
☐ 4+ vCPUs available for VMs
☐ 50+ GB storage for demo environment

Optional but Recommended:
☐ Azure Portal familiarity
☐ Docker Desktop (for container images)
☐ VS Code with Azure extensions

Estimated Time: 2-3 hours
Difficulty: Intermediate
Cost: $5-20 Azure credits
```

---

## Lab Architecture

```text
AZURE LOCAL DEPLOYMENT ARCHITECTURE
═════════════════════════════════════════════════════════════

On-Premises (Your Lab Environment)
┌──────────────────────────────────────────────┐
│ Azure Local Cluster (Simulated)              │
│                                              │
│ ┌─────────────────────────────────────────┐ │
│ │ Arc Agent                               │ │
│ │ └─→ Connected to Azure (Management)    │ │
│ └─────────────────────────────────────────┘ │
│                                              │
│ ┌─────────────────────────────────────────┐ │
│ │ Demo Application Namespace              │ │
│ │ ├─ Web API Pod                          │ │
│ │ ├─ Database Pod                         │ │
│ │ └─ Storage PVC                          │ │
│ └─────────────────────────────────────────┘ │
│                                              │
│ ┌─────────────────────────────────────────┐ │
│ │ Azure Local Storage                     │ │
│ │ ├─ 500 GB for containers                │ │
│ │ └─ 500 GB for data                      │ │
│ └─────────────────────────────────────────┘ │
└──────────────────────────────────────────────┘
          ↓ (Connected mode)
┌──────────────────────────────────────────────┐
│ Azure (Cloud)                                │
│ ├─ Azure Arc representation                  │
│ ├─ Monitoring & management                   │
│ ├─ Backup storage                            │
│ └─ Audit logs                                │
└──────────────────────────────────────────────┘
```

---

## Lab Steps

### Step 1: Prepare Azure Environment

**Objective:** Set up Azure resources for Azure Local deployment

**Step 1.1: Create Resource Group**

```powershell
# Set variables
$resourceGroup = "rg-azure-local-lab"
$location = "eastus"

# Create resource group
az group create `
  --name $resourceGroup `
  --location $location

# Verify creation
az group show --name $resourceGroup
```

**Expected Output:**

```json
{
  "id": "/subscriptions/xxx/resourceGroups/rg-azure-local-lab",
  "location": "eastus",
  "name": "rg-azure-local-lab",
  "properties": {
    "provisioningState": "Succeeded"
  }
}
```

**Step 1.2: Create Virtual Network**

```powershell
# Create virtual network for Azure Local cluster
az network vnet create `
  --resource-group $resourceGroup `
  --name "vnet-azure-local" `
  --address-prefix "10.0.0.0/16" `
  --subnet-name "subnet-nodes" `
  --subnet-prefix "10.0.1.0/24"

# Verify creation
az network vnet show `
  --resource-group $resourceGroup `
  --name "vnet-azure-local"
```

**Expected Output:** Virtual network created with CIDR 10.0.0.0/16

**Step 1.3: Create Storage Account**

```powershell
# Create storage account for Azure Local backups
$storageAccount = "stazurelocallab$([DateTime]::UtcNow.Ticks % 1000000)"

az storage account create `
  --name $storageAccount `
  --resource-group $resourceGroup `
  --location $location `
  --sku "Standard_GRS" `
  --kind "StorageV2"

# Create container for backups
az storage container create `
  --name "azure-local-backups" `
  --account-name $storageAccount

# Verify creation
az storage account show `
  --name $storageAccount `
  --resource-group $resourceGroup
```

**Expected Output:** Storage account created with GRS replication

---

### Step 2: Deploy Azure Local Simulation

**Objective:** Set up simulated Azure Local environment (AKS cluster representing Azure Local)

**Step 2.1: Create AKS Cluster (Simulating Azure Local)**

```powershell
# Note: In production, this would be actual Azure Local hardware
# For this lab, we simulate with AKS cluster

$clusterName = "aks-azure-local-lab"
$nodeCount = 3

# Create AKS cluster
az aks create `
  --resource-group $resourceGroup `
  --name $clusterName `
  --node-count $nodeCount `
  --vm-set-type VirtualMachineScaleSets `
  --load-balancer-sku standard `
  --enable-managed-identity `
  --network-plugin azure `
  --vnet-subnet-id "/subscriptions/$(az account show --query id -o tsv)/resourceGroups/$resourceGroup/providers/Microsoft.Network/virtualNetworks/vnet-azure-local/subnets/subnet-nodes" `
  --docker-bridge-address 172.17.0.1/16 `
  --service-cidr 10.1.0.0/16 `
  --dns-service-ip 10.1.0.10 `
  --enable-addons monitoring `
  --workspace-resource-id "/subscriptions/$(az account show --query id -o tsv)/resourceGroups/$resourceGroup/providers/microsoft.operationalinsights/workspaces/..." `
  --generate-ssh-keys

# This takes ~5-10 minutes
# Meanwhile, continue with other preparations
```

**Expected Output:** AKS cluster creation started (wait for completion)

**Step 2.2: Get Cluster Credentials**

```powershell
# Get cluster credentials for kubectl access
az aks get-credentials `
  --resource-group $resourceGroup `
  --name $clusterName `
  --overwrite-existing

# Verify connectivity
kubectl cluster-info
kubectl get nodes
```

**Expected Output:**

```text
NAME                       STATUS   ROLES   AGE
aks-nodepool1-xxxxx-vmss-000000   Ready    agent   2m
aks-nodepool1-xxxxx-vmss-000001   Ready    agent   2m
aks-nodepool1-xxxxx-vmss-000002   Ready    agent   2m
```

---

### Step 3: Deploy Sample Application

**Objective:** Deploy a sample application to validate Azure Local functionality

**Step 3.1: Create Application Namespace**

```powershell
# Create namespace for demo application
kubectl create namespace demo-app

# Verify namespace creation
kubectl get namespaces
```

**Expected Output:** Namespace "demo-app" created

**Step 3.2: Create ConfigMap with Application Configuration**

```powershell
# Create ConfigMap for application settings
@"
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
  namespace: demo-app
data:
  app.properties: |
    DATABASE_HOST=postgres-db.demo-app.svc.cluster.local
    DATABASE_PORT=5432
    DATABASE_NAME=demodb
    LOG_LEVEL=INFO
"@ | kubectl apply -f -

# Verify
kubectl get configmap -n demo-app
```

**Expected Output:** ConfigMap "app-config" created

**Step 3.3: Deploy PostgreSQL Database**

```powershell
# Create persistent volume claim for database
@"
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: postgres-pvc
  namespace: demo-app
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
"@ | kubectl apply -f -

# Deploy PostgreSQL
@"
apiVersion: apps/v1
kind: Deployment
metadata:
  name: postgres-db
  namespace: demo-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
      - name: postgres
        image: postgres:15-alpine
        ports:
        - containerPort: 5432
        env:
        - name: POSTGRES_DB
          value: demodb
        - name: POSTGRES_USER
          value: demouser
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: postgres-secret
              key: password
        volumeMounts:
        - name: postgres-storage
          mountPath: /var/lib/postgresql/data
      volumes:
      - name: postgres-storage
        persistentVolumeClaim:
          claimName: postgres-pvc
---
apiVersion: v1
kind: Service
metadata:
  name: postgres-db
  namespace: demo-app
spec:
  ports:
  - port: 5432
    targetPort: 5432
  selector:
    app: postgres
"@ | kubectl apply -f -

# Monitor deployment
kubectl get deployment -n demo-app
kubectl get pods -n demo-app
```

**Expected Output:** PostgreSQL pod running

**Step 3.4: Deploy Web Application**

```powershell
# Deploy sample web API
@"
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-api
  namespace: demo-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web-api
  template:
    metadata:
      labels:
        app: web-api
    spec:
      containers:
      - name: web-api
        image: nginx:latest
        ports:
        - containerPort: 80
        resources:
          requests:
            memory: "128Mi"
            cpu: "100m"
          limits:
            memory: "256Mi"
            cpu: "500m"
        envFrom:
        - configMapRef:
            name: app-config
---
apiVersion: v1
kind: Service
metadata:
  name: web-api
  namespace: demo-app
spec:
  type: LoadBalancer
  ports:
  - port: 80
    targetPort: 80
  selector:
    app: web-api
"@ | kubectl apply -f -

# Monitor deployment
kubectl get deployment -n demo-app
kubectl get service -n demo-app
```

**Expected Output:** Web API pods running with load balancer service

---

### Step 4: Validate Deployment

**Objective:** Verify all components deployed successfully

**Step 4.1: Check Pod Status**

```powershell
# Get all pods in demo-app namespace
kubectl get pods -n demo-app -o wide

# Check for any issues
kubectl get events -n demo-app
```

**Expected Output:**

```text
NAME                        READY   STATUS    RESTARTS   AGE
postgres-db-xxxxx-xxxxx     1/1     Running   0          2m
web-api-xxxxx-xxxxx-xxxxx   1/1     Running   0          1m
web-api-xxxxx-xxxxx-yyyyy   1/1     Running   0          1m
web-api-xxxxx-xxxxx-zzzzz   1/1     Running   0          1m
```

**Step 4.2: Check Storage Usage**

```powershell
# Get persistent volume status
kubectl get pv
kubectl get pvc -n demo-app

# Check storage class
kubectl get storageclass
```

**Expected Output:** PVC showing "Bound" status with correct storage size

**Step 4.3: Test Application Connectivity**

```powershell
# Get external IP of web service
kubectl get service web-api -n demo-app

# Test connectivity (replace with actual IP)
$webApiIP = kubectl get service web-api -n demo-app -o jsonpath='{.status.loadBalancer.ingress[0].ip}'
Invoke-WebRequest "http://$webApiIP" -ErrorAction SilentlyContinue
```

**Expected Output:** HTTP 200 OK response

**Step 4.4: Check Resource Utilization**

```powershell
# Get node status
kubectl get nodes -o wide

# Get cluster metrics (if metrics-server installed)
kubectl top nodes
kubectl top pods -n demo-app
```

**Expected Output:** Nodes showing Ready status with CPU/Memory usage

---

### Step 5: Connected Mode Configuration

**Objective:** Configure Azure Local connectivity to Azure (via Arc)

**Step 5.1: Install Azure Arc Agent**

```powershell
# Add Helm repository for Azure Arc
helm repo add azurearc https://raw.githubusercontent.com/Azure/azure-arc-for-kubernetes/main/helm

# Install Azure Arc extension
az k8s-configuration flux create `
  --cluster-name $clusterName `
  --resource-group $resourceGroup `
  --cluster-type managedClusters `
  --name arc-demo-config `
  --scope cluster

# Verify Arc connectivity
kubectl get pods -n azure-arc
```

**Expected Output:** Azure Arc pods running in azure-arc namespace

**Step 5.2: Enable Monitoring**

```powershell
# Enable Container Insights (monitoring)
# Get cluster resource ID
$clusterId = az aks show `
  --resource-group $resourceGroup `
  --name $clusterName `
  --query id `
  -o tsv

# Enable monitoring
az aks enable-addons `
  --addons monitoring `
  --name $clusterName `
  --resource-group $resourceGroup

# Verify monitoring is enabled
kubectl get daemonset -n kube-system | grep -i omsagent
```

**Expected Output:** OMS Agent daemonset running for monitoring

**Step 5.3: Verify Azure Connectivity**

```powershell
# Check Arc connection status via Azure CLI
az connectedk8s show `
  --name $clusterName `
  --resource-group $resourceGroup

# Verify agent connectivity
kubectl get deploy -n azure-arc
```

**Expected Output:** Connected status showing "Connected"

---

### Step 6: Backup Configuration

**Objective:** Configure backup for disaster recovery

**Step 6.1: Create Backup Policy**

```powershell
# In production, use Azure Backup
# For this lab, we configure snapshot strategy

# Create snapshot schedule
@"
apiVersion: v1
kind: ConfigMap
metadata:
  name: backup-schedule
  namespace: demo-app
data:
  schedule.json: |
    {
      "frequency": "daily",
      "time": "02:00Z",
      "retention_days": 30,
      "backup_location": "$storageAccount"
    }
"@ | kubectl apply -f -

# Verify backup configuration
kubectl get configmap -n demo-app
```

**Expected Output:** Backup schedule configured

**Step 6.2: Test Backup**

```powershell
# Create test backup
$backupName = "backup-$(Get-Date -Format yyyyMMdd-HHmm)"

# Export current state to Azure Storage
kubectl get all --all-namespaces -o yaml | `
  Out-String | `
  az storage blob upload `
    --account-name $storageAccount `
    --container-name azure-local-backups `
    --name "$backupName.yaml" `
    --file -

# Verify backup created
az storage blob list `
  --account-name $storageAccount `
  --container-name azure-local-backups
```

**Expected Output:** Backup file uploaded successfully

---

### Step 7: Post-Lab Validation

**Objective:** Confirm all lab objectives completed

**Step 7.1: Collect Evidence**

```powershell
# Document cluster state
kubectl cluster-info > cluster-info.txt
kubectl get all --all-namespaces > all-resources.txt
kubectl get nodes -o wide > nodes-status.txt
kubectl top nodes > resource-usage.txt

# Document Azure resources
az group show --name $resourceGroup > resource-group-info.json
az aks show --name $clusterName --resource-group $resourceGroup > cluster-details.json

Write-Host "Lab evidence collected in current directory"
```

**Step 7.2: Summary Report**

```powershell
# Generate summary
Write-Host "=== LAB 1 COMPLETION SUMMARY ===" -ForegroundColor Green

Write-Host "`nResource Group: $resourceGroup"
Write-Host "Cluster Name: $clusterName"
Write-Host "Node Count: $nodeCount"
Write-Host "Storage Account: $storageAccount"

Write-Host "`nDeployments:"
kubectl get deployment --all-namespaces

Write-Host "`nServices:"
kubectl get service --all-namespaces

Write-Host "`nStorage:"
kubectl get pvc --all-namespaces

Write-Host "`n=== LAB 1 COMPLETE ===" -ForegroundColor Green
```

---

## Cleanup (Optional)

```powershell
# Delete all resources to avoid unnecessary charges
az group delete `
  --name $resourceGroup `
  --yes `
  --no-wait

Write-Host "Resource group deletion initiated"
```

---

## Learning Outcomes

### What You Learned

✓ Azure Local architecture and deployment model
✓ Connected mode configuration for hybrid connectivity
✓ Kubernetes deployment on Azure Local/AKS
✓ Persistent storage configuration
✓ Application deployment and validation
✓ Monitoring integration with Azure
✓ Backup strategy for disaster recovery

### Skills Gained

✓ Use Azure CLI for infrastructure provisioning
✓ Deploy and manage Kubernetes resources
✓ Configure networking for hybrid deployments
✓ Implement persistent storage for stateful applications
✓ Monitor cluster health and performance
✓ Backup and recovery procedures

### Next Steps

- **Lab 2:** [Azure Arc Onboarding](./lab-02-azure-arc-onboarding.md) - Register Azure Local resources with Arc
- **Lab 3:** [Edge RAG Setup](./lab-03-edge-rag-setup.md) - Deploy AI workload on Azure Local
- **Production:** Deploy Azure Local on actual hardware in production datacenter

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| AKS cluster creation timeout | Increase timeout or check Azure quota |
| Pods in CrashLoopBackOff | Check logs: `kubectl logs <pod> -n <namespace>` |
| PVC not binding | Verify storage class: `kubectl get storageclass` |
| LoadBalancer IP pending | Add ingress controller or use NodePort |
| Low disk space | Clean up images: `kubectl clean` or scale down |

---

_Last Updated: October 21, 2025_
