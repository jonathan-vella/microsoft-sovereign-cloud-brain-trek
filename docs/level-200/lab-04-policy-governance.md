---
layout: default
title: "Lab 4: Policy & Governance"
parent: Hands-On Labs Overview
nav_order: 4
---

# Lab 4: Policy & Governance

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

Configure Azure Policy and governance controls across hybrid resources deployed in previous labs (Azure Local, Arc, Edge RAG). Implement compliance requirements and enforce organizational standards at scale.

---

## Pre-Lab Checklist

```text
PREREQUISITES
═════════════════════════════════════════════════════════════

Required:
☐ Completion of Labs 1-3 (Azure Local, Arc, Edge RAG)
☐ Azure subscription with Owner role
☐ Azure CLI installed (version 2.50+)
☐ PowerShell 7+ installed
☐ kubectl access to all labs' clusters
☐ Azure Policy experience

Optional but Recommended:
☐ Understanding of RBAC and IAM
☐ Compliance framework knowledge (GDPR, FedRAMP)
☐ Audit logging concepts

Estimated Time: 2-3 hours
Difficulty: Intermediate
Cost: $0-10 Azure credits (Policy is free)
```

---

## Lab Architecture

```text
POLICY AND GOVERNANCE ARCHITECTURE
═════════════════════════════════════════════════════════════

Azure Management Plane
┌─────────────────────────────────────────────────────────┐
│ Azure Policy Engine                                     │
│                                                         │
│ ┌────────────────────────────────────────────────────┐ │
│ │ Policy Definitions                                 │ │
│ │ ├─ Enforce tagging requirements                    │ │
│ │ ├─ Require encryption at rest                      │ │
│ │ ├─ Enforce network security                        │ │
│ │ ├─ Mandate compliance monitoring                   │ │
│ │ └─ Restrict resource types/locations               │ │
│ └────────────────────────────────────────────────────┘ │
│              ↓                   ↓                       │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ Policy Assignments (Scopes)                        │ │
│ │ ├─ Subscription-level (all resources)              │ │
│ │ ├─ Resource group-level (specific workloads)       │ │
│ │ └─ Resource-level (exceptions/exclusions)          │ │
│ └─────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
              ↓                   ↓                   ↓
     ┌──────────────┐    ┌─────────────────┐ ┌──────────────┐
     │ Arc Cluster  │    │ Edge RAG        │ │ Azure Local  │
     │ (Lab 2)      │    │ (Lab 3)         │ │ (Lab 1)      │
     │              │    │                 │ │              │
     │ ├─ Policies  │    │ ├─ Policies    │ │ ├─ Policies  │
     │ │  enforced  │    │ │  enforced    │ │ │  enforced  │
     │ │  via agents│    │ │  via agents  │ │ │  via agents│
     │ ├─ Compliance│    │ ├─ Compliance │ │ ├─ Compliance│
     │ │  monitored │    │ │  monitored  │ │ │  monitored │
     │ └─ Audit logs│    │ └─ Audit logs │ │ └─ Audit logs│
     └──────────────┘    └─────────────────┘ └──────────────┘

┌─────────────────────────────────────────────────────────┐
│ Compliance & Audit Plane                                │
│                                                         │
│ ├─ Compliance Dashboard                                 │
│ ├─ Audit Trail (Activity Logs)                         │
│ ├─ Remediation Tracking                                │
│ └─ Incident Response                                   │
└─────────────────────────────────────────────────────────┘
```

---

## Lab Steps

### Step 1: Understand Governance Requirements

**Objective:** Define organizational compliance and governance policies

**Step 1.1: Define Policy Categories**

```powershell
# Policy categories for this lab:
# 1. Tagging & Resource Management
# 2. Security & Encryption
# 3. Compliance & Audit
# 4. Resource Restrictions
# 5. Network & Connectivity

$policyCategories = @{
    "Tagging" = @{
        "Description" = "Ensure all resources properly tagged"
        "Impact" = "Resource identification and cost allocation"
        "Enforcement" = "Deny resource creation without tags"
    }
    "Security" = @{
        "Description" = "Enforce encryption and security standards"
        "Impact" = "Data protection and compliance"
        "Enforcement" = "Audit/Deny encryption violations"
    }
    "Compliance" = @{
        "Description" = "Meet regulatory requirements"
        "Impact" = "Legal and governance compliance"
        "Enforcement" = "Audit logging and monitoring"
    }
    "Resources" = @{
        "Description" = "Control resource types and locations"
        "Impact" = "Cost optimization and governance"
        "Enforcement" = "Deny non-compliant resource types"
    }
}

Write-Host "Policy Categories Defined:"
foreach ($category in $policyCategories.Keys) {
    Write-Host "  ✓ $category"
}
```

**Step 1.2: Document Compliance Requirements**

```powershell
# Compliance requirements based on Modules covered
$complianceRequirements = @{
    "DataResidency" = @{
        "Description" = "Data must remain within sovereign cloud boundaries"
        "Source" = "Module 2: Sovereign Cloud Models"
        "Implementation" = "Resource location policies"
    }
    "Encryption" = @{
        "Description" = "All data encrypted at rest (AES-256) and in transit (TLS 1.2+)"
        "Source" = "Module 5: Compliance & Security"
        "Implementation" = "Encryption enforcement policies"
    }
    "Audit" = @{
        "Description" = "All access and modifications logged and monitored"
        "Source" = "Module 5: Compliance & Security"
        "Implementation" = "Audit logging policies"
    }
    "AccessControl" = @{
        "Description" = "Zero-trust access with RBAC and MFA"
        "Source" = "Module 5: Security Hardening"
        "Implementation" = "Identity-based access policies"
    }
}

Write-Host "`nCompliance Requirements:"
foreach ($req in $complianceRequirements.GetEnumerator()) {
    Write-Host "  ✓ $($req.Key): $($req.Value.Description)"
}
```

---

### Step 2: Create Custom Policy Definitions

**Objective:** Define custom policies for organizational standards

**Step 2.1: Policy Definition - Require Tagging**

```powershell
# Variables
$subscriptionId = az account show --query id -o tsv
$resourceGroup = "rg-policy-lab"

# Create resource group for policy work
az group create --name $resourceGroup --location eastus

# Policy definition: Require environment tag
$tagPolicy = @{
    mode = "Indexed"
    policyRule = @{
        if = @{
            field = "tags['environment']"
            exists = "false"
        }
        then = @{
            effect = "audit"
        }
    }
    parameters = @{}
}

# Save policy definition
$tagPolicy | ConvertTo-Json -Depth 5 | Out-File -Path policy-require-env-tag.json

# Create policy definition
az policy definition create `
  --name "require-environment-tag" `
  --display-name "Require Environment Tag" `
  --description "Enforces that all resources have an environment tag" `
  --rules policy-require-env-tag.json `
  --mode Indexed

Write-Host "Policy 'require-environment-tag' created"
```

**Step 2.2: Policy Definition - Require Encryption**

```powershell
# Policy definition: Enforce encryption on storage accounts
$encryptionPolicy = @{
    mode = "Indexed"
    policyRule = @{
        if = @{
            allOf = @(
                @{
                    field = "type"
                    equals = "Microsoft.Storage/storageAccounts"
                },
                @{
                    field = "Microsoft.Storage/storageAccounts/encryption.services.blob.enabled"
                    notEquals = "true"
                }
            )
        }
        then = @{
            effect = "audit"
        }
    }
    parameters = @{}
}

$encryptionPolicy | ConvertTo-Json -Depth 5 | Out-File -Path policy-require-encryption.json

# Create policy definition
az policy definition create `
  --name "require-storage-encryption" `
  --display-name "Require Storage Account Encryption" `
  --description "Enforces encryption on all storage accounts" `
  --rules policy-require-encryption.json `
  --mode Indexed

Write-Host "Policy 'require-storage-encryption' created"
```

**Step 2.3: Policy Definition - Restrict Locations**

```powershell
# Policy definition: Restrict resource locations to sovereign cloud region
$locationPolicy = @{
    mode = "Indexed"
    policyRule = @{
        if = @{
            field = "location"
            notIn = @("eastus", "eastus2", "westeurope")
        }
        then = @{
            effect = "deny"
        }
    }
    parameters = @{}
}

$locationPolicy | ConvertTo-Json -Depth 5 | Out-File -Path policy-restrict-locations.json

# Create policy definition
az policy definition create `
  --name "restrict-allowed-locations" `
  --display-name "Restrict Allowed Locations" `
  --description "Restricts resources to approved regions for data residency" `
  --rules policy-restrict-locations.json `
  --mode Indexed

Write-Host "Policy 'restrict-allowed-locations' created"
```

**Step 2.4: View Created Policies**

```powershell
# List custom policies
az policy definition list --query "[].{name:name, displayName:displayName, policyType:policyType}" --output table
```

**Expected Output:**

```text
Name                           DisplayName                         PolicyType
─────────────────────────────────────────────────────────────────────────────
require-environment-tag        Require Environment Tag            Custom
require-storage-encryption     Require Storage Account Encryption Custom
restrict-allowed-locations     Restrict Allowed Locations         Custom
```

---

### Step 3: Create Policy Initiatives

**Objective:** Group related policies into initiatives for easier management

**Step 3.1: Create Governance Initiative**

```powershell
# Create policy initiative combining multiple policies
$initiativeDefinition = @{
    type = "Microsoft.Authorization/policySetDefinitions"
    apiVersion = "2021-06-01"
    name = "governance-initiative"
    properties = @{
        displayName = "Governance and Compliance Initiative"
        description = "Initiative enforcing organizational governance standards"
        policyDefinitions = @(
            @{
                policyDefinitionId = "/subscriptions/$subscriptionId/providers/Microsoft.Authorization/policyDefinitions/require-environment-tag"
                parameters = @{}
            },
            @{
                policyDefinitionId = "/subscriptions/$subscriptionId/providers/Microsoft.Authorization/policyDefinitions/require-storage-encryption"
                parameters = @{}
            },
            @{
                policyDefinitionId = "/subscriptions/$subscriptionId/providers/Microsoft.Authorization/policyDefinitions/restrict-allowed-locations"
                parameters = @{}
            }
        )
    }
}

$initiativeDefinition | ConvertTo-Json -Depth 10 | Out-File -Path initiative-definition.json

# Create initiative
az policy set-definition create `
  --name "governance-initiative" `
  --display-name "Governance and Compliance Initiative" `
  --description "Initiative for organizational governance" `
  --definitions initiative-definition.json

Write-Host "Initiative 'governance-initiative' created"
```

**Step 3.2: Verify Initiative Creation**

```powershell
# List policy initiatives
az policy set-definition list --query "[].{name:name, displayName:displayName}" --output table
```

---

### Step 4: Assign Policies

**Objective:** Apply policies to resources across hybrid environment

**Step 4.1: Assign Policies to Resource Groups**

```powershell
# Variables
$arcResourceGroup = "rg-arc-lab"
$azureLocalResourceGroup = "rg-azure-local-lab"

# Assign governance initiative to Arc resource group
az policy assignment create `
  --name "arc-governance-assignment" `
  --policy-set-definition "governance-initiative" `
  --scope "/subscriptions/$subscriptionId/resourceGroups/$arcResourceGroup" `
  --location eastus

# Assign governance initiative to Azure Local resource group
az policy assignment create `
  --name "local-governance-assignment" `
  --policy-set-definition "governance-initiative" `
  --scope "/subscriptions/$subscriptionId/resourceGroups/$azureLocalResourceGroup" `
  --location eastus

Write-Host "Policy assignments created"
```

**Step 4.2: Verify Assignments**

```powershell
# List policy assignments
az policy assignment list --query "[].{name:name, displayName:displayName, scope:scope}" --output table
```

**Expected Output:**

```text
Name                              DisplayName                    Scope
──────────────────────────────────────────────────────────────────────────────
arc-governance-assignment         Governance and Compliance...   /subscriptions/.../rg-arc-lab
local-governance-assignment       Governance and Compliance...   /subscriptions/.../rg-azure-local-lab
```

---

### Step 5: Configure Arc Policy Extension

**Objective:** Extend policy enforcement to Arc-managed Kubernetes clusters

**Step 5.1: Enable Azure Policy for Kubernetes**

```powershell
# Variables
$arcClusterName = "arc-kubernetes-lab"
$arcResourceGroup = "rg-arc-lab"

# Verify Azure Policy extension is deployed (from Lab 2)
az k8s-extension list `
  --cluster-name $arcClusterName `
  --cluster-type connectedClusters `
  --resource-group $arcResourceGroup | grep -i policy

Write-Host "Azure Policy extension for Kubernetes verified"
```

**Step 5.2: Create Kubernetes Policy**

```powershell
# Get cluster credentials
az aks get-credentials `
  --resource-group "rg-azure-local-lab" `
  --name "aks-azure-local-lab" `
  --overwrite-existing

# Create constraint for pod security
@"
apiVersion: templates.gatekeeper.sh/v1
kind: ConstraintTemplate
metadata:
  name: k8srequiredlabels
spec:
  crd:
    spec:
      names:
        kind: K8sRequiredLabels
      validation:
        openAPIV3Schema:
          properties:
            labels:
              type: array
              items:
                type: string
  targets:
    - target: admission.k8s.gatekeeper.sh
      rego: |
        package k8srequiredlabels
        violation[{"msg": msg}] {
          label := input.parameters.labels[_]
          not input.review.object.metadata.labels[label]
          msg := sprintf("Missing required label: %v", [label])
        }
---
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sRequiredLabels
metadata:
  name: require-labels
spec:
  match:
    kinds:
      - apiGroups: [""]
        kinds: ["Pod"]
  parameters:
    labels: ["environment", "owner", "cost-center"]
"@ | kubectl apply -f -

Write-Host "Kubernetes policy constraints applied"
```

**Step 5.3: Test Policy Enforcement**

```powershell
# Try to create pod without required labels (should be denied)
@"
apiVersion: v1
kind: Pod
metadata:
  name: test-pod-no-labels
  namespace: default
spec:
  containers:
  - name: nginx
    image: nginx:latest
"@ | kubectl apply -f -

# Should be denied - check output
Write-Host "Pod without labels: Should be DENIED"

# Create pod with required labels (should succeed)
@"
apiVersion: v1
kind: Pod
metadata:
  name: test-pod-with-labels
  namespace: default
  labels:
    environment: production
    owner: admin
    cost-center: engineering
spec:
  containers:
  - name: nginx
    image: nginx:latest
"@ | kubectl apply -f -

Write-Host "Pod with labels: Should SUCCEED"

# Verify policy results
kubectl describe constrainttemplate k8srequiredlabels
```

---

### Step 6: Monitor Policy Compliance

**Objective:** Track compliance status across resources

**Step 6.1: Check Compliance Status**

```powershell
# Get policy compliance state
az policy state summarize `
  --subscription $subscriptionId `
  --query "value[0]" `
  -o json | ConvertFrom-Json

Write-Host "Compliance Summary:"
Write-Host "  Non-compliant resources: check dashboard"
```

**Step 6.2: Evaluate Specific Policy**

```powershell
# Evaluate compliance for require-environment-tag policy
az policy state list `
  --filter "policyDefinitionName eq 'require-environment-tag'" `
  --query "[].{resourceId:resourceId, complianceState:complianceState, timestamp:timestamp}" `
  --output table
```

**Step 6.3: Create Compliance Report**

```powershell
# Generate detailed compliance report
$complianceReport = az policy state list `
  --query "[?complianceState=='NonCompliant'].{Resource:resourceId, Policy:policyDefinitionName, State:complianceState}" `
  -o json | ConvertFrom-Json

Write-Host "Non-Compliant Resources:"
$complianceReport | Format-Table -AutoSize

# Export to CSV for audit trail
$complianceReport | Export-Csv -Path "compliance-report-$(Get-Date -Format yyyyMMdd-HHmm).csv" -NoTypeInformation

Write-Host "Report exported to CSV"
```

---

### Step 7: Implement Remediation

**Objective:** Automatically fix non-compliant resources

**Step 7.1: Create Remediation Tasks**

```powershell
# List non-compliant resources
$nonCompliant = az policy state list `
  --filter "complianceState eq 'NonCompliant'" `
  --query "[].resourceId" `
  -o json | ConvertFrom-Json

Write-Host "Found $($nonCompliant.Count) non-compliant resources"

# Create remediation task for non-compliant storage accounts
if ($nonCompliant.Count -gt 0) {
    az policy remediation create `
      --name "encryption-remediation" `
      --policy-assignment "storage-encryption-assignment" `
      --definition-reference-id "require-storage-encryption" `
      --resource-discovery-mode ReEvaluateCompliance

    Write-Host "Remediation task created"
}
```

**Step 7.2: Monitor Remediation**

```powershell
# Check remediation status
az policy remediation list `
  --query "[].{name:name, provisioningState:provisioningState, deploymentStatus:deploymentStatus}" `
  --output table

# Get details of specific remediation
az policy remediation show --name "encryption-remediation"
```

**Step 7.3: Verify Compliance Improvement**

```powershell
# Re-evaluate compliance after remediation
Start-Sleep -Seconds 30

$newCompliance = az policy state summarize `
  --subscription $subscriptionId `
  --query "value[0]" `
  -o json | ConvertFrom-Json

Write-Host "Updated Compliance Status:"
Write-Host "  Compliant: $($newCompliance.results.compliantResourceCount)"
Write-Host "  Non-compliant: $($newCompliance.results.nonCompliantResourceCount)"
```

---

### Step 8: Audit Logging and Monitoring

**Objective:** Set up comprehensive audit trail for governance

**Step 8.1: Enable Activity Logging**

```powershell
# Activity logs are enabled by default
# Create Log Analytics workspace for analysis
$logWorkspaceName = "log-policy-analysis-$([DateTime]::UtcNow.Ticks % 1000000)"

az monitor log-analytics workspace create `
  --resource-group $resourceGroup `
  --workspace-name $logWorkspaceName

$logWorkspaceId = az monitor log-analytics workspace show `
  --resource-group $resourceGroup `
  --workspace-name $logWorkspaceName `
  --query id `
  -o tsv

Write-Host "Log Analytics workspace created: $logWorkspaceName"
```

**Step 8.2: Create Diagnostic Settings**

```powershell
# Stream activity logs to Log Analytics
az monitor diagnostic-settings create `
  --name "policy-diagnostics" `
  --resource "/subscriptions/$subscriptionId" `
  --logs "true" `
  --workspace $logWorkspaceId

Write-Host "Diagnostic settings configured"
```

**Step 8.3: Create Alert Rules**

```powershell
# Create alert for policy violations
az monitor action-group create `
  --resource-group $resourceGroup `
  --name "policy-alerts"

# Create metric alert for compliance degradation
az monitor metrics alert create `
  --resource-group $resourceGroup `
  --name "compliance-degradation-alert" `
  --description "Alert when compliance score decreases" `
  --scopes "/subscriptions/$subscriptionId" `
  --condition "avg Microsoft.PolicyInsights/PolicyComplianceMetric/NonCompliantResourceCount > 5" `
  --window-size 1h `
  --evaluation-frequency 15m `
  --action policy-alerts

Write-Host "Alert rules configured"
```

**Step 8.4: Query Audit Logs**

```powershell
# Query recent policy-related activities
az monitor activity-log list `
  --resource-group $resourceGroup `
  --query "[?contains(operationName.value, 'Microsoft.Authorization/policyAssignments')]" `
  --max-events 20 `
  --output table

Write-Host "Audit logs retrieved"
```

---

### Step 9: Validation and Reporting

**Objective:** Verify governance implementation and create reports

**Step 9.1: Validate Policy Enforcement**

```powershell
# Test 1: Verify tag enforcement
Write-Host "Test 1: Tag Enforcement"
Write-Host "─" * 60

# Try to create resource without tags (should be denied)
az storage account create `
  --name "test-storage-nopolicy-$([DateTime]::UtcNow.Ticks % 1000000)" `
  --resource-group $resourceGroup `
  --location eastus `
  --sku Standard_LRS 2>&1

# Create with tags (should succeed)
az storage account create `
  --name "test-storage-withtags-$([DateTime]::UtcNow.Ticks % 1000000)" `
  --resource-group $resourceGroup `
  --location eastus `
  --sku Standard_LRS `
  --tags environment=production owner=admin

Write-Host "Tag enforcement verified"
```

**Step 9.2: Generate Compliance Dashboard**

```powershell
# Get comprehensive compliance metrics
$compliance = az policy state summarize `
  --subscription $subscriptionId `
  --query "value[0].results" `
  -o json | ConvertFrom-Json

$total = $compliance.compliantResourceCount + $compliance.nonCompliantResourceCount
$compliantPercentage = ($compliance.compliantResourceCount / $total) * 100

Write-Host "═" * 60
Write-Host "GOVERNANCE COMPLIANCE DASHBOARD"
Write-Host "═" * 60
Write-Host "`nCompliance Overview:"
Write-Host "  Compliant Resources: $($compliance.compliantResourceCount)"
Write-Host "  Non-Compliant Resources: $($compliance.nonCompliantResourceCount)"
Write-Host "  Compliance Rate: $([math]::Round($compliantPercentage, 2))%"
Write-Host "`nPolicy Details:"

az policy assignment list --query "[].{name:name, scope:scope}" --output table

Write-Host "`n═" * 60
```

**Step 9.3: Export Compliance Report**

```powershell
# Create detailed report
$report = @{
    GeneratedTime = Get-Date
    SubscriptionId = $subscriptionId
    ComplianceState = @{
        CompliantResources = $compliance.compliantResourceCount
        NonCompliantResources = $compliance.nonCompliantResourceCount
        CompliancePercentage = $compliantPercentage
    }
    AppliedPolicies = $(az policy assignment list --query "length(@)" -o tsv)
    CustomPolicies = $(az policy definition list --query "length(@)" -o tsv)
}

$report | ConvertTo-Json | Out-File -Path "governance-report-$(Get-Date -Format yyyyMMdd).json"

Write-Host "Detailed report saved"
```

---

## Learning Outcomes

### What You Learned

✓ Azure Policy definition and structure
✓ Custom policy creation for organizational standards
✓ Policy initiatives for grouped enforcement
✓ Policy assignments at different scopes
✓ Kubernetes policy enforcement via Gatekeeper
✓ Compliance monitoring and reporting
✓ Automated remediation of non-compliant resources
✓ Audit logging and compliance tracking

### Skills Gained

✓ Create custom Azure Policies for governance
✓ Define and enforce organizational standards
✓ Monitor compliance across hybrid infrastructure
✓ Implement automated remediation
✓ Generate compliance reports and dashboards
✓ Troubleshoot policy enforcement issues
✓ Integrate compliance with DevOps workflows

### Applied Knowledge from Previous Modules

✓ **Module 5 (Compliance & Security):** Implement compliance requirements
✓ **Lab 1-2 (Azure Local & Arc):** Apply governance to all resources
✓ **Lab 3 (Edge RAG):** Enforce policies on AI workloads

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Policy assignment fails | Verify scope permissions and policy definition exists |
| Compliance state not updating | Wait 30 minutes or trigger re-evaluation manually |
| Kubernetes policies not enforcing | Verify Gatekeeper pods running: `kubectl get pods -n gatekeeper-system` |
| Remediation tasks stalling | Check task definition and resource permissions |
| No audit logs appearing | Verify diagnostic settings configured and Log Analytics connected |
| Policy conflicts | Review policy definitions for overlapping rules |

---

_Last Updated: October 21, 2025_
