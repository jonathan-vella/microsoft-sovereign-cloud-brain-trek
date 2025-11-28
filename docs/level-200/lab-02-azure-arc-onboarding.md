---
layout: default
title: "Lab 2: Azure Arc Onboarding"
parent: Hands-On Labs Overview
nav_order: 2
---

# Lab 2: Azure Arc Onboarding

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

Onboard hybrid resources (Azure Local from Lab 1) to Azure Arc for centralized management, governance, and monitoring across hybrid environments.

---

## Pre-Lab Checklist

```text
PREREQUISITES
═════════════════════════════════════════════════════════════

Required:
☐ Completion of Lab 1 (Azure Local deployment)
☐ Azure subscription with Owner role
☐ Azure CLI installed (version 2.50+)
☐ PowerShell 7+ installed
☐ kubectl access to Lab 1 cluster
☐ Service Principal creation rights

Optional but Recommended:
☐ Azure Arc experience
☐ Kubernetes onboarding knowledge
☐ Hybrid management concepts

Estimated Time: 2-3 hours
Difficulty: Intermediate
Cost: $0-10 Azure credits (Arc is free)
```

---

## Lab Architecture

```text
AZURE ARC ONBOARDING ARCHITECTURE
═════════════════════════════════════════════════════════════

On-Premises (Lab 1 Azure Local)
┌─────────────────────────────────────────────┐
│ AKS Cluster (Kubernetes)                    │
│                                             │
│ ┌────────────────────────────────────────┐  │
│ │ azure-arc Namespace                    │  │
│ │ ├─ Azure Arc Agent Pods                │  │
│ │ ├─ Service Principal Credentials       │  │
│ │ └─ Connected State Validation          │  │
│ └────────────────────────────────────────┘  │
│                                             │
│ ┌────────────────────────────────────────┐  │
│ │ demo-app Namespace (Lab 1)             │  │
│ │ ├─ Web API (Now managed by Arc)        │  │
│ │ ├─ Database (Arc policies applied)     │  │
│ │ └─ Storage (Monitored via Arc)         │  │
│ └────────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
          ↓ (Bidirectional Arc Agent Communication)
┌─────────────────────────────────────────────┐
│ Azure (Cloud Control Plane)                 │
│                                             │
│ ┌────────────────────────────────────────┐  │
│ │ Azure Arc Enabled Kubernetes Cluster   │  │
│ │ ├─ Representation of on-prem cluster   │  │
│ │ ├─ Unified management                  │  │
│ │ └─ Single pane of glass                │  │
│ └────────────────────────────────────────┘  │
│                                             │
│ ┌────────────────────────────────────────┐  │
│ │ Arc Configuration Management           │  │
│ │ ├─ GitOps for declarative config       │  │
│ │ ├─ Policy enforcement                  │  │
│ │ └─ Compliance monitoring               │  │
│ └────────────────────────────────────────┘  │
│                                             │
│ ┌────────────────────────────────────────┐  │
│ │ Monitoring & Observability             │  │
│ │ ├─ Metrics collection                  │  │
│ │ ├─ Audit logging                       │  │
│ │ └─ Integration with Azure Monitor      │  │
│ └────────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

---

## Lab Steps

### Step 1: Prepare for Arc Onboarding

**Objective:** Set up prerequisites for Arc registration

**Step 1.1: Create Service Principal**

```powershell
# Variables
$subscriptionId = az account show --query id -o tsv
$tenantId = az account show --query tenantId -o tsv
$appName = "arc-lab-sp"

# Create service principal for Arc onboarding
$sp = az ad sp create-for-rbac `
  --name $appName `
  --role "Kubernetes Cluster - Azure Arc Onboarding" `
  --scopes "/subscriptions/$subscriptionId" | ConvertFrom-Json

# Store credentials securely
$spAppId = $sp.appId
$spPassword = $sp.password
$spTenantId = $sp.tenant

Write-Host "Service Principal Created:"
Write-Host "App ID: $spAppId"
Write-Host "Tenant ID: $spTenantId"

# Note: Save credentials - you'll need them next
```

**Expected Output:**

```json
{
  "appId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "displayName": "arc-lab-sp",
  "password": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "tenant": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

**Step 1.2: Create Resource Group for Arc**

```powershell
# Variables from Lab 1
$resourceGroup = "rg-azure-local-lab"
$clusterName = "aks-azure-local-lab"
$arcResourceGroup = "rg-arc-lab"
$location = "eastus"

# Create new resource group for Arc resources
az group create `
  --name $arcResourceGroup `
  --location $location

# Verify creation
az group show --name $arcResourceGroup
```

**Expected Output:** Resource group created successfully

**Step 1.3: Register Azure Arc Provider**

```powershell
# Register Microsoft.Kubernetes provider
az provider register --namespace Microsoft.Kubernetes
az provider register --namespace Microsoft.KubernetesConfiguration
az provider register --namespace Microsoft.ExtendedLocation

# Wait for registration to complete (typically 1-5 minutes)
Write-Host "Providers registering... please wait"
Start-Sleep -Seconds 10

# Check registration status
az provider show --namespace Microsoft.Kubernetes --query registrationState
az provider show --namespace Microsoft.KubernetesConfiguration --query registrationState
az provider show --namespace Microsoft.ExtendedLocation --query registrationState
```

**Expected Output:** All providers showing "Registered" state

**Step 1.4: Verify Lab 1 Connectivity**

```powershell
# Get credentials from Lab 1 cluster
az aks get-credentials `
  --resource-group $resourceGroup `
  --name $clusterName `
  --overwrite-existing

# Verify access
kubectl cluster-info
kubectl get nodes
kubectl get namespaces
```

**Expected Output:** Cluster accessible via kubectl with all namespaces visible

---

### Step 2: Register Kubernetes Cluster with Arc

**Objective:** Connect the Lab 1 cluster to Azure Arc

**Step 2.1: Install Azure CLI Extensions**

```powershell
# Install required extensions
az extension add --name connectedk8s
az extension add --name k8s-configuration
az extension add --name k8s-extension

# Verify installations
az extension list | grep -E "connectedk8s|k8s-configuration|k8s-extension"
```

**Expected Output:** All three extensions installed

**Step 2.2: Register Cluster with Arc**

```powershell
# Variables
$arcClusterName = "arc-kubernetes-lab"
$arcResourceGroup = "rg-arc-lab"

# Register cluster with Azure Arc
az connectedk8s connect `
  --name $arcClusterName `
  --resource-group $arcResourceGroup `
  --location $location `
  --tags environment=lab purpose=training

# This takes 2-5 minutes
Write-Host "Cluster onboarding in progress..."
Start-Sleep -Seconds 10
```

**Expected Output:** Cluster successfully connected to Arc

**Step 2.3: Verify Arc Connection**

```powershell
# Check Arc resource in Azure
az connectedk8s show `
  --name $arcClusterName `
  --resource-group $arcResourceGroup

# Check Arc agent pods in cluster
kubectl get pods -n azure-arc
kubectl get pods -n azure-arc-data
```

**Expected Output:**

```text
NAME                              READY   STATUS    RESTARTS   AGE
clusteridentityoperator-xxxxx     1/1     Running   0          2m
config-agent-xxxxx                1/1     Running   0          2m
controller-manager-xxxxx          1/1     Running   0          2m
metrics-agent-xxxxx               1/1     Running   0          2m
resource-sync-agent-xxxxx         1/1     Running   0          2m
```

**Step 2.4: Check Agent Health**

```powershell
# Get detailed Arc connection status
kubectl describe configmap azure-clusterconfig -n azure-arc

# Check connectivity logs
kubectl logs -n azure-arc -l app=config-agent -f --tail=20
```

**Expected Output:** Agent successfully communicating with Azure

---

### Step 3: Configure Arc Extensions

**Objective:** Deploy Azure Arc extensions for enhanced management

**Step 3.1: Deploy Container Insights Extension**

```powershell
# Create Log Analytics workspace for monitoring
$workspaceName = "log-arc-lab-$([DateTime]::UtcNow.Ticks % 1000000)"
$workspaceResourceGroup = $arcResourceGroup

az monitor log-analytics workspace create `
  --resource-group $workspaceResourceGroup `
  --workspace-name $workspaceName

# Get workspace ID and key
$workspaceId = az monitor log-analytics workspace show `
  --resource-group $workspaceResourceGroup `
  --workspace-name $workspaceName `
  --query id `
  -o tsv

# Deploy Container Insights extension
az k8s-extension create `
  --cluster-name $arcClusterName `
  --cluster-type connectedClusters `
  --name azuremonitor-containers `
  --extension-type Microsoft.AzureMonitor.Containers `
  --resource-group $arcResourceGroup `
  --configuration-settings logAnalyticsWorkspaceResourceID=$workspaceId

# Wait for deployment
Write-Host "Container Insights deploying..."
Start-Sleep -Seconds 30

# Verify extension
az k8s-extension list `
  --cluster-name $arcClusterName `
  --cluster-type connectedClusters `
  --resource-group $arcResourceGroup
```

**Expected Output:** Extension status showing "Provisioned"

**Step 3.2: Deploy Azure Policy Extension**

```powershell
# Deploy Azure Policy for Kubernetes
az k8s-extension create `
  --cluster-name $arcClusterName `
  --cluster-type connectedClusters `
  --name azure-policy `
  --extension-type Microsoft.PolicyInsights.PolicyAgentForKubernetes `
  --resource-group $arcResourceGroup

# Wait for deployment
Write-Host "Azure Policy deploying..."
Start-Sleep -Seconds 30

# Verify policy engine pods
kubectl get pods -n gatekeeper-system
```

**Expected Output:** Gatekeeper and policy engine pods running

**Step 3.3: Deploy GitOps Extension**

```powershell
# Deploy Azure Arc GitOps extension
az k8s-extension create `
  --cluster-name $arcClusterName `
  --cluster-type connectedClusters `
  --name flux `
  --extension-type microsoft.flux `
  --resource-group $arcResourceGroup `
  --scope cluster

# Wait for deployment
Write-Host "GitOps deploying..."
Start-Sleep -Seconds 30

# Verify flux controller pods
kubectl get pods -n flux-system
```

**Expected Output:** Flux operator and controller running

---

### Step 4: Create Arc Configuration (GitOps)

**Objective:** Deploy applications declaratively using GitOps

**Step 4.1: Create Flux Configuration**

```powershell
# This example uses a public repository (or local)
# In production, use your private repo

$configName = "demo-app-config"
$gitRepository = "https://github.com/fluxcd/flux2-kustomize-helm-example.git"
$branch = "main"
$namespace = "flux-system"

# Create flux configuration for demo-app
az k8s-configuration flux create `
  --cluster-name $arcClusterName `
  --cluster-type connectedClusters `
  --name $configName `
  --resource-group $arcResourceGroup `
  --namespace $namespace `
  --source-kind GitRepository `
  --url $gitRepository `
  --branch $branch `
  --sync-interval 5m

# Verify configuration
az k8s-configuration flux list `
  --cluster-name $arcClusterName `
  --cluster-type connectedClusters `
  --resource-group $arcResourceGroup
```

**Expected Output:** Flux configuration created and syncing

**Step 4.2: Monitor GitOps Sync**

```powershell
# Check GitRepository source
kubectl get gitrepository -n flux-system -o wide

# Check Kustomization sync status
kubectl get kustomization -n flux-system -o wide

# Check events
kubectl get events -n flux-system --sort-by='.lastTimestamp'
```

**Expected Output:** GitRepository and Kustomization in "Ready" state

---

### Step 5: Configure Azure Policies

**Objective:** Enforce governance policies on Arc cluster

**Step 5.1: Define Custom Policy**

```powershell
# Create policy definition for image registry enforcement
$policyDefinition = @"
{
  "mode": "Indexed",
  "policyRule": {
    "if": {
      "allOf": [
        {
          "field": "type",
          "equals": "Microsoft.Kubernetes/connectedClusters"
        }
      ]
    },
    "then": {
      "effect": "audit"
    }
  },
  "parameters": {}
}
"@

# Save policy definition
$policyDefinition | Out-File -Path policy-definition.json

Write-Host "Policy definition created"
```

**Step 5.2: Apply Built-in Policies**

```powershell
# Get built-in policies for Kubernetes
az policy definition list --query "[?contains(displayName, 'Kubernetes')].[id, displayName]"

# Apply policy: "Ensure container image registry is not allowed"
$policyId = "/subscriptions/$subscriptionId/providers/Microsoft.Authorization/policyDefinitions/unique-identifier"

# Create policy assignment
az policy assignment create `
  --name "arc-lab-image-policy" `
  --policy "Kubernetes cluster containers should only use allowed images" `
  --scope "/subscriptions/$subscriptionId/resourceGroups/$arcResourceGroup"

# Verify policy assignment
az policy assignment list --scope "/subscriptions/$subscriptionId/resourceGroups/$arcResourceGroup"
```

**Expected Output:** Policy assignment created successfully

**Step 5.3: Test Policy Enforcement**

```powershell
# Try to deploy container with non-compliant image
kubectl apply -f - <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: policy-test
  namespace: default
spec:
  containers:
  - name: test
    image: nginx:latest
EOF

# Check if pod is denied (if policies are strict)
kubectl get pod policy-test -o wide

# If allowed, check audit logs in Azure Policy
az policy state summarize --resource "/subscriptions/$subscriptionId/resourceGroups/$arcResourceGroup"
```

**Expected Output:** Policy evaluation logged (audit/deny depending on policy)

---

### Step 6: Configure Monitoring and Alerts

**Objective:** Set up monitoring for Arc resources

**Step 6.1: Create Action Group**

```powershell
# Create action group for alerts
$actionGroupName = "arc-lab-action-group"

az monitor action-group create `
  --resource-group $arcResourceGroup `
  --name $actionGroupName

# Add email action (replace with your email)
az monitor action-group update `
  --resource-group $arcResourceGroup `
  --name $actionGroupName `
  --add-action email-receiver admin-email --email-address your-email@example.com

# Verify action group
az monitor action-group show `
  --resource-group $arcResourceGroup `
  --name $actionGroupName
```

**Expected Output:** Action group created with email recipient

**Step 6.2: Create Alert Rule**

```powershell
# Create alert for Arc agent disconnection
az monitor metrics alert create `
  --resource-group $arcResourceGroup `
  --name "arc-agent-disconnected" `
  --description "Alert when Arc agent disconnects" `
  --scopes "/subscriptions/$subscriptionId/resourceGroups/$arcResourceGroup/providers/Microsoft.Kubernetes/connectedClusters/$arcClusterName" `
  --condition "avg Microsoft.Kubernetes/connectedClusters/connectedUnitCount < 1" `
  --window-size 5m `
  --evaluation-frequency 1m `
  --action $actionGroupName

# Verify alert rule
az monitor metrics alert list --resource-group $arcResourceGroup
```

**Expected Output:** Alert rule created successfully

**Step 6.3: View Metrics in Portal**

```powershell
# Get workspace ID for querying
$workspaceId = az monitor log-analytics workspace show `
  --resource-group $workspaceResourceGroup `
  --workspace-name $workspaceName `
  --query id `
  -o tsv

Write-Host "View metrics in Azure Portal:"
Write-Host "1. Go to Azure Monitor"
Write-Host "2. Select Metrics"
Write-Host "3. Scope: $arcResourceGroup / $arcClusterName"
Write-Host "4. Metric: connectedUnitCount, CPU, Memory"
```

---

### Step 7: Onboard Machines (Optional Extension)

**Objective:** Register individual machines to Arc (if desired)

**Step 7.1: Check Arc Server Support**

```powershell
# Arc can also manage individual servers
# For this lab, we focus on cluster-level management
# But here's how you'd add servers:

# In production, use the Arc-enabled Servers agent
# For details, see Module 2: Arc Advanced Management

Write-Host "Machine onboarding covered in Module 2"
```

---

### Step 8: Validation and Verification

**Objective:** Confirm Arc onboarding success

**Step 8.1: Verify Cluster Registration**

```powershell
# Check cluster resource in Azure
az connectedk8s show `
  --name $arcClusterName `
  --resource-group $arcResourceGroup

# Check connectivity status
$arcStatus = az connectedk8s show `
  --name $arcClusterName `
  --resource-group $arcResourceGroup `
  --query "{name:name, agentVersion:agentVersion, connectivityStatus:connectivityStatus, lastConnectivityTime:lastConnectivityTime}" `
  -o json | ConvertFrom-Json

Write-Host "Arc Cluster Status:"
Write-Host "Name: $($arcStatus.name)"
Write-Host "Agent Version: $($arcStatus.agentVersion)"
Write-Host "Connectivity: $($arcStatus.connectivityStatus)"
Write-Host "Last Connected: $($arcStatus.lastConnectivityTime)"
```

**Expected Output:**

```text
Arc Cluster Status:
Name: arc-kubernetes-lab
Agent Version: 1.13.x
Connectivity: Connected
Last Connected: 2025-10-21T14:30:00Z
```

**Step 8.2: Verify Extensions**

```powershell
# List all installed extensions
az k8s-extension list `
  --cluster-name $arcClusterName `
  --cluster-type connectedClusters `
  --resource-group $arcResourceGroup `
  --query "[].{name:name, provisioningState:provisioningState, version:version}" `
  -o table
```

**Expected Output:**

```text
Name                         ProvisioningState    Version
azuremonitor-containers      Provisioned          1.10
azure-policy                 Provisioned          1.5
flux                         Provisioned          1.0
```

**Step 8.3: Verify Pod Deployments from Lab 1**

```powershell
# Verify Lab 1 application still running under Arc management
kubectl get pods -n demo-app -o wide

# Check Arc is managing the namespace
kubectl get pods -n azure-arc -o wide

# Verify metrics flowing
kubectl top nodes
kubectl top pods -n demo-app
```

**Expected Output:** All pods running, metrics available

**Step 8.4: Check Audit Logs**

```powershell
# View Arc activity in Azure Activity Log
az monitor activity-log list `
  --resource-group $arcResourceGroup `
  --max-events 20

# Look for Arc-related operations
az monitor activity-log list `
  --resource-group $arcResourceGroup `
  --query "[?contains(operationName.value, 'Microsoft.Kubernetes')]" `
  --max-events 10
```

**Expected Output:** Arc operations logged successfully

---

## Learning Outcomes

### What You Learned

✓ Service Principal creation for Arc onboarding
✓ Azure Arc Kubernetes cluster registration
✓ Arc extensions for monitoring, policy, and GitOps
✓ GitOps configuration with Flux
✓ Azure Policy enforcement on Arc clusters
✓ Monitoring and alerting for Arc resources
✓ Unified management across hybrid environments

### Skills Gained

✓ Onboard Kubernetes clusters to Azure Arc
✓ Deploy and configure Arc extensions
✓ Implement GitOps for declarative configuration
✓ Enforce governance policies at scale
✓ Monitor Arc cluster health and compliance
✓ Troubleshoot Arc connectivity issues
✓ Manage hybrid infrastructure from Azure

### Next Steps

- **Lab 3:** [Edge RAG Setup](./lab-03-edge-rag-setup.md) - Deploy AI workload managed by Arc
- **Lab 4:** [Policy Governance](./lab-04-policy-governance.md) - Advanced policy enforcement
- **Production:** Onboard production Kubernetes clusters to Arc for enterprise governance

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Service Principal creation fails | Check subscription permissions |
| Arc connect fails | Verify cluster has internet access for Arc agent |
| Extensions fail to deploy | Check cluster resources: `kubectl describe nodes` |
| GitOps not syncing | Verify Git repository access and credentials |
| Policies not enforcing | Check Azure Policy assignment scope |
| Monitoring shows no data | Verify Log Analytics workspace connection |

---

_Last Updated: October 21, 2025_
