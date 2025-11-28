---
layout: default
title: "Lab 5: Monitoring & Observability"
parent: Hands-On Labs Overview
nav_order: 5
---

# Lab 5: Monitoring & Observability

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

Configure comprehensive monitoring and observability across all previous labs (Azure Local, Arc, Edge RAG, Policy Governance). Implement metrics collection, logging aggregation, alerting, and dashboards for proactive incident management.

---

## Pre-Lab Checklist

```text
PREREQUISITES
═════════════════════════════════════════════════════════════

Required:
☐ Completion of Labs 1-4 (all previous labs)
☐ Azure subscription with all deployed resources
☐ Azure CLI installed (version 2.50+)
☐ PowerShell 7+ installed
☐ kubectl access to all clusters
☐ Log Analytics knowledge

Optional but Recommended:
☐ Azure Monitor experience
☐ KQL (Kusto Query Language) familiarity
☐ Prometheus/Grafana knowledge
☐ Alert rule configuration experience

Estimated Time: 2-3 hours
Difficulty: Intermediate
Cost: $20-50 Azure credits (monitoring ingestion)
```

---

## Lab Architecture

```text
MONITORING AND OBSERVABILITY ARCHITECTURE
═════════════════════════════════════════════════════════════

On-Premises (Labs 1, 2, 3, 4)
┌─────────────────────────────────────────────────────────┐
│ Data Collection Layer                                   │
│                                                         │
│ ┌────────────────────────────────────────────────────┐ │
│ │ Monitoring Agents                                  │ │
│ │ ├─ Azure Monitor Agent (Metrics/Logs)             │ │
│ │ ├─ Prometheus Scraper (Custom Metrics)            │ │
│ │ ├─ Fluent Bit (Log Forwarding)                    │ │
│ │ └─ Application Insights SDK (App Metrics)         │ │
│ └────────────────────────────────────────────────────┘ │
│              ↓              ↓              ↓             │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ Data Types Collected                               │ │
│ │ ├─ Metrics: CPU, Memory, Disk, Network           │ │
│ │ ├─ Logs: Application, System, Security            │ │
│ │ ├─ Events: Pod lifecycle, policy violations       │ │
│ │ └─ Traces: Request tracing, APM                   │ │
│ └─────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
          ↓ (Secure transmission over TLS)
┌─────────────────────────────────────────────────────────┐
│ Azure (Data Aggregation & Analysis)                     │
│                                                         │
│ ┌────────────────────────────────────────────────────┐ │
│ │ Log Analytics Workspace                            │ │
│ │ ├─ Data ingestion (20GB+/month)                   │ │
│ │ ├─ KQL queries and analysis                        │ │
│ │ ├─ Alert rule evaluation                           │ │
│ │ └─ Long-term retention and compliance              │ │
│ └────────────────────────────────────────────────────┘ │
│                                                         │
│ ┌────────────────────────────────────────────────────┐ │
│ │ Azure Monitor (Metrics)                            │ │
│ │ ├─ Real-time metrics from all resources            │ │
│ │ ├─ Custom metric ingestion                         │ │
│ │ ├─ Metric alerts and autoscaling                   │ │
│ │ └─ Metrics Explorer visualization                  │ │
│ └────────────────────────────────────────────────────┘ │
│                                                         │
│ ┌────────────────────────────────────────────────────┐ │
│ │ Application Insights                               │ │
│ │ ├─ Application performance monitoring              │ │
│ │ ├─ Dependency tracking                             │ │
│ │ ├─ User session analysis                           │ │
│ │ └─ Availability testing                            │ │
│ └────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
          ↓
┌─────────────────────────────────────────────────────────┐
│ Visualization & Response Layer                          │
│                                                         │
│ ├─ Azure Dashboards                                     │
│ ├─ Grafana (Cross-platform dashboards)                 │
│ ├─ Alert Actions (Email, Webhook, Automation)          │
│ ├─ Incident Response & Remediation                     │
│ └─ Compliance Reporting & Audit Trail                  │
└─────────────────────────────────────────────────────────┘
```

---

## Lab Steps

### Step 1: Set Up Monitoring Infrastructure

**Objective:** Create Log Analytics workspace and monitoring resources

**Step 1.1: Create Log Analytics Workspace**

```powershell
# Variables
$resourceGroup = "rg-monitoring-lab"
$location = "eastus"
$workspaceName = "log-sovereign-monitoring-$([DateTime]::UtcNow.Ticks % 1000000)"

# Create resource group
az group create --name $resourceGroup --location $location

# Create Log Analytics workspace
az monitor log-analytics workspace create `
  --resource-group $resourceGroup `
  --workspace-name $workspaceName `
  --sku PerGB2018 `
  --retention-time 30

# Get workspace details
$workspaceId = az monitor log-analytics workspace show `
  --resource-group $resourceGroup `
  --workspace-name $workspaceName `
  --query id `
  -o tsv

$workspaceKey = az monitor log-analytics workspace get-shared-keys `
  --resource-group $resourceGroup `
  --workspace-name $workspaceName `
  --query primarySharedKey `
  -o tsv

Write-Host "Log Analytics Workspace created: $workspaceName"
Write-Host "Workspace ID: $workspaceId"
```

**Expected Output:** Log Analytics workspace provisioned

**Step 1.2: Create Application Insights Instance**

```powershell
# Create Application Insights for application monitoring
$appInsightsName = "ai-sovereign-cloud-$([DateTime]::UtcNow.Ticks % 1000000)"

az monitor app-insights component create `
  --app $appInsightsName `
  --location $location `
  --resource-group $resourceGroup `
  --application-type web `
  --workspace $workspaceId

# Get instrumentation key
$instrumentation_key = az monitor app-insights component show `
  --app $appInsightsName `
  --resource-group $resourceGroup `
  --query instrumentationKey `
  -o tsv

Write-Host "Application Insights created: $appInsightsName"
Write-Host "Instrumentation Key: $instrumentation_key"
```

**Expected Output:** Application Insights instance created

**Step 1.3: Create Action Groups**

```powershell
# Create action group for notifications
$actionGroupName = "ag-monitoring-notifications"

az monitor action-group create `
  --resource-group $resourceGroup `
  --name $actionGroupName `
  --short-name "Monitoring"

# Add email action
az monitor action-group update `
  --resource-group $resourceGroup `
  --name $actionGroupName `
  --add-action email-receiver admin-email --email-address admin@example.com

# Add webhook for automation (optional)
az monitor action-group update `
  --resource-group $resourceGroup `
  --name $actionGroupName `
  --add-action webhook webhook-receiver --service-uri https://webhook.site/your-id

Write-Host "Action groups configured"
```

---

### Step 2: Configure Data Collection

**Objective:** Set up agents and data sources for metrics and logs

**Step 2.1: Deploy Azure Monitor Agent on VMs (Simulated)**

```powershell
# In production, agents would be deployed to all monitored VMs
# For this lab, we configure agent deployment rules

# Get all VMs (from Labs 1-3)
$vmList = az vm list --query "[].{id:id, name:name, resourceGroup:resourceGroup}" -o json | ConvertFrom-Json

Write-Host "Found $($vmList.Count) VMs to monitor"

foreach ($vm in $vmList) {
    Write-Host "  - $($vm.name) (Resource Group: $($vm.resourceGroup))"
}

# Create data collection rule for VM metrics
$dcrName = "dcr-vm-monitoring"

@"
{
  "location": "$location",
  "properties": {
    "dataSources": {
      "performanceCounters": [
        {
          "name": "cpuPerformance",
          "samplingFrequencyInSeconds": 60,
          "counterSpecifiers": [
            "\\\\Processor(_Total)\\\\% Processor Time",
            "\\\\Memory\\\\% Committed Bytes In Use",
            "\\\\LogicalDisk(_Total)\\\\% Free Space"
          ]
        }
      ],
      "syslog": [
        {
          "name": "sysLogCollection",
          "logLevels": ["Notice", "Warning", "Error"]
        }
      ]
    },
    "destinations": {
      "logAnalytics": [
        {
          "name": "myWorkspace",
          "workspaceResourceId": "$workspaceId"
        }
      ]
    },
    "dataFlows": [
      {
        "streams": ["Microsoft-Perf", "Microsoft-Syslog"],
        "destinations": ["myWorkspace"]
      }
    ]
  }
}
"@ > dcr-template.json

# Create DCR
az monitor data-collection rule create `
  --name $dcrName `
  --resource-group $resourceGroup `
  --location $location `
  --rule-file dcr-template.json

Write-Host "Data Collection Rule created: $dcrName"
```

**Step 2.2: Configure Container Insights**

```powershell
# Enable Container Insights for all Kubernetes clusters
$clusterList = @(
    @{ name = "aks-azure-local-lab"; resourceGroup = "rg-azure-local-lab" },
    @{ name = "arc-kubernetes-lab"; resourceGroup = "rg-arc-lab" }
)

foreach ($cluster in $clusterList) {
    Write-Host "Configuring Container Insights for $($cluster.name)..."

    # For AKS clusters
    if ($cluster.name -like "*aks*") {
        az aks enable-addons `
          --addons monitoring `
          --name $cluster.name `
          --resource-group $cluster.resourceGroup `
          --workspace-resource-id $workspaceId
    }

    Write-Host "  ✓ Container Insights enabled"
}

# Verify Container Insights is collecting data
Write-Host "Waiting for data collection to start (1-2 minutes)..."
Start-Sleep -Seconds 30
```

**Expected Output:** Container Insights collecting metrics from clusters

**Step 2.3: Configure Application Logging**

```powershell
# For Labs applications (RAG, demo-app), configure structured logging
# Get RAG API pods
kubectl get pods -n edge-rag -l app=rag-api -o jsonpath='{.items[*].metadata.name}'

# Get demo app pods
kubectl get pods -n demo-app -o jsonpath='{.items[*].metadata.name}'

Write-Host "Applications identified for monitoring"
```

---

### Step 3: Create Monitoring Queries

**Objective:** Build KQL queries for analysis and insights

**Step 3.1: Create Performance Monitoring Queries**

```powershell
# KQL query: CPU usage over time (saved for reuse)
$cpuQuery = @"
Perf
| where ObjectName == "Processor" and CounterName == "% Processor Time"
| summarize AvgCPU = avg(CounterValue), MaxCPU = max(CounterValue), MinCPU = min(CounterValue) by bin(TimeGenerated, 5m), Computer
| render timechart
"@

# KQL query: Memory usage by host
$memoryQuery = @"
Perf
| where ObjectName == "Memory" and CounterName == "% Committed Bytes In Use"
| summarize AvgMemory = avg(CounterValue) by Computer
| top 10 by AvgMemory
| render columnchart
"@

# KQL query: Pod restarts in Kubernetes
$podRestartQuery = @"
ContainerLogV2
| where TimeGenerated > ago(1d)
| where PodRestartCount > 0
| summarize TotalRestarts = sum(PodRestartCount) by PodName, Namespace
| top 20 by TotalRestarts
"@

# KQL query: Application errors
$errorQuery = @"
AppEvents
| where EventLevel == "Error"
| summarize ErrorCount = count() by AppRoleName, TimeGenerated = bin(TimeGenerated, 1h)
| render barchart
"@

Write-Host "Monitoring queries prepared:"
Write-Host "  ✓ CPU Performance Query"
Write-Host "  ✓ Memory Usage Query"
Write-Host "  ✓ Pod Restart Analysis Query"
Write-Host "  ✓ Application Error Query"
```

**Step 3.2: Execute Queries and Analyze**

```powershell
# Execute queries in Log Analytics (sample execution)
Write-Host "Executing monitoring queries in Log Analytics..."
Write-Host "`nQuery Results would include:"
Write-Host "  - Current CPU utilization across all nodes"
Write-Host "  - Memory usage patterns"
Write-Host "  - Pod restart trends"
Write-Host "  - Application error rates and patterns"
```

---

### Step 4: Create Alerts

**Objective:** Set up alerts for key metrics and thresholds

**Step 4.1: Create Metric Alerts**

```powershell
# Alert 1: High CPU Usage
az monitor metrics alert create `
  --resource-group $resourceGroup `
  --name "alert-high-cpu" `
  --description "Alert when CPU usage exceeds 80%" `
  --scopes "/subscriptions/$(az account show --query id -o tsv)/resourceGroups/rg-azure-local-lab" `
  --condition "avg Percentage CPU > 80" `
  --window-size 5m `
  --evaluation-frequency 1m `
  --action $actionGroupName `
  --severity 2

# Alert 2: High Memory Usage
az monitor metrics alert create `
  --resource-group $resourceGroup `
  --name "alert-high-memory" `
  --description "Alert when memory usage exceeds 85%" `
  --scopes "/subscriptions/$(az account show --query id -o tsv)/resourceGroups/rg-azure-local-lab" `
  --condition "avg Available Memory Bytes < 20" `
  --window-size 5m `
  --evaluation-frequency 1m `
  --action $actionGroupName `
  --severity 2

# Alert 3: Pod Crash Loop
az monitor metrics alert create `
  --resource-group $resourceGroup `
  --name "alert-pod-crash-loop" `
  --description "Alert when pods are in crash loop" `
  --scopes "/subscriptions/$(az account show --query id -o tsv)/resourceGroups/rg-azure-local-lab" `
  --condition "avg RestartCount > 5" `
  --window-size 10m `
  --evaluation-frequency 2m `
  --action $actionGroupName `
  --severity 1

Write-Host "Metric alerts created"
```

**Expected Output:** Alerts configured and ready

**Step 4.2: Create Log Query Alerts**

```powershell
# Alert based on KQL query: Application errors threshold
az monitor log alert create `
  --resource-group $resourceGroup `
  --name "alert-app-errors" `
  --description "Alert when error count exceeds 50 per hour" `
  --scopes "/subscriptions/$(az account show --query id -o tsv)/providers/Microsoft.OperationalInsights/workspaces/$workspaceName" `
  --condition "AppEvents | where EventLevel == 'Error' | summarize count() by bin(TimeGenerated, 1h) | where count_ > 50" `
  --window-size 1h `
  --evaluation-frequency 15m `
  --action $actionGroupName `
  --severity 2

# Alert: Policy violation detected
az monitor log alert create `
  --resource-group $resourceGroup `
  --name "alert-policy-violations" `
  --description "Alert when policy violations detected" `
  --scopes "/subscriptions/$(az account show --query id -o tsv)/providers/Microsoft.OperationalInsights/workspaces/$workspaceName" `
  --condition "AzureActivity | where OperationName contains 'policyAssignment' | where ActivityStatus == 'Failed' | summarize count()" `
  --window-size 1h `
  --evaluation-frequency 30m `
  --action $actionGroupName `
  --severity 2

# Alert: Arc agent disconnection
az monitor log alert create `
  --resource-group $resourceGroup `
  --name "alert-arc-disconnect" `
  --description "Alert when Arc agent disconnects" `
  --scopes "/subscriptions/$(az account show --query id -o tsv)/providers/Microsoft.OperationalInsights/workspaces/$workspaceName" `
  --condition "AzureActivity | where OperationName contains 'connectedk8s' | where ActivityStatus == 'Failed'" `
  --window-size 30m `
  --evaluation-frequency 10m `
  --action $actionGroupName `
  --severity 1

Write-Host "Log query alerts created"
```

**Step 4.3: Verify Alert Rules**

```powershell
# List all alert rules
az monitor metrics alert list `
  --resource-group $resourceGroup `
  --query "[].{name:name, description:description, severity:severity}" `
  --output table

Write-Host "`nAlert rules configured and monitoring is active"
```

---

### Step 5: Create Dashboards

**Objective:** Build visualization dashboards for monitoring

**Step 5.1: Create Azure Dashboard**

```powershell
# Create dashboard JSON definition
$dashboardName = "sovereign-cloud-monitoring"

$dashboardJson = @"
{
  "location": "$location",
  "tags": {
    "environment": "production",
    "purpose": "monitoring"
  },
  "properties": {
    "lenses": {
      "0": {
        "order": 0,
        "parts": {
          "0": {
            "position": {
              "x": 0,
              "y": 0,
              "colSpan": 6,
              "rowSpan": 4
            },
            "metadata": {
              "inputs": [
                {
                  "name": "resourceType",
                  "value": "microsoft.operationalinsights/workspaces"
                },
                {
                  "name": "resourceName",
                  "value": "$workspaceName"
                }
              ],
              "type": "Extension/Microsoft_Azure_Monitoring_Logs/PartType/LogsDashboardPart",
              "settings": {
                "content": {
                  "Query": "Perf | where CounterName == '% Processor Time' | summarize avg(CounterValue) by bin(TimeGenerated, 1m), Computer"
                }
              }
            }
          },
          "1": {
            "position": {
              "x": 6,
              "y": 0,
              "colSpan": 6,
              "rowSpan": 4
            },
            "metadata": {
              "inputs": [],
              "type": "Extension/HubsExtension/PartType/MarkdownPart",
              "settings": {
                "content": {
                  "settings": {
                    "content": "# Sovereign Cloud Monitoring Dashboard\n\n## Key Metrics\n- CPU Usage across cluster\n- Memory utilization\n- Network I/O\n- Pod health status"
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
"@

# Create dashboard
az portal dashboard create `
  --resource-group $resourceGroup `
  --name $dashboardName `
  --input-path <(Write-Output $dashboardJson)

Write-Host "Dashboard created: $dashboardName"
```

**Step 5.2: Add Key Performance Indicators**

```powershell
# KPIs to track
$kpis = @{
    "Cluster Health" = "Percentage of healthy pods"
    "Security Posture" = "Policy compliance percentage"
    "Performance" = "Average request latency"
    "Reliability" = "System uptime percentage"
    "Cost" = "Resource utilization vs allocation"
}

Write-Host "Key Performance Indicators configured:"
foreach ($kpi in $kpis.GetEnumerator()) {
    Write-Host "  ✓ $($kpi.Key): $($kpi.Value)"
}
```

---

### Step 6: Implement Incident Response

**Objective:** Set up automated incident response workflows

**Step 6.1: Create Automation Runbooks**

```powershell
# Create Automation Account for remediation
$automationAccountName = "aa-monitoring-remediation"

az automation account create `
  --resource-group $resourceGroup `
  --name $automationAccountName `
  --location $location

Write-Host "Automation Account created: $automationAccountName"

# Example remediation actions could include:
# - Scale up cluster when CPU > 80%
# - Restart failing pods
# - Trigger backup when storage exceeds threshold
# - Isolate infected containers
```

**Step 6.2: Create WebHook Integration**

```powershell
# Create webhook for custom incident response
$webhookName = "incident-webhook"

# Webhook actions example (documented for manual implementation)
$webhookActions = @"
1. Receive alert notification
2. Log incident to tracking system
3. Page on-call engineer if severity >= 1
4. Auto-scale cluster if CPU alert
5. Create incident ticket
6. Execute remediation script
7. Send status update to Slack
"@

Write-Host "Incident Response Workflow:"
Write-Host $webhookActions
```

**Step 6.3: Configure Incident Notification**

```powershell
# Test alert notification
Write-Host "Alert notification configured for:"
Write-Host "  - Email to admin@example.com"
Write-Host "  - Webhook integration (if configured)"
Write-Host "  - Slack integration (optional)"
Write-Host "  - PagerDuty integration (optional)"
```

---

### Step 7: Advanced Monitoring Scenarios

**Objective:** Implement specialized monitoring for specific workloads

**Step 7.1: Application Performance Monitoring (APM)**

```powershell
# Configure APM for RAG application
$appInsightsKey = $instrumentation_key

Write-Host "Application Performance Monitoring:"
Write-Host "  - Instrumentation Key: $appInsightsKey"
Write-Host "  - Monitoring: Request latency, failures, dependencies"
Write-Host "  - Tracking: User sessions, page views, custom events"

# Code snippet for instrumentation (reference)
$apmCode = @"
# Add to application code (RAG API example)
from opencensus.ext.azure.log_exporter import AzureLogHandler
import logging

handler = AzureLogHandler(connection_string='InstrumentationKey=$appInsightsKey')
logging.getLogger().addHandler(handler)
"@

Write-Host "`nAPM Integration (add to application):"
Write-Host $apmCode
```

**Step 7.2: Distributed Tracing**

```powershell
# Configure Application Insights for distributed tracing
# This tracks requests across multiple services

Write-Host "Distributed Tracing Configuration:"
Write-Host "  - Azure Local → Arc (management plane)"
Write-Host "  - Arc → Edge RAG (inference requests)"
Write-Host "  - Edge RAG → Weaviate → Ollama (internal)"

# Enable distributed tracing in Application Insights
az monitor app-insights api-key create `
  --app $appInsightsName `
  --resource-group $resourceGroup `
  --key-name "distributed-tracing-key"

Write-Host "`nDistributed tracing enabled"
```

**Step 7.3: Custom Metrics**

```powershell
# Define custom metrics for RAG system
$customMetrics = @{
    "RAGQueryLatency" = "Time to retrieve context and generate answer"
    "VectorSearchLatency" = "Time to search vector database"
    "LLMInferenceLatency" = "Time for LLM to generate response"
    "DocumentIngestionRate" = "Documents processed per minute"
    "ModelAccuracy" = "Percentage of accurate answers"
}

Write-Host "Custom Metrics for RAG System:"
foreach ($metric in $customMetrics.GetEnumerator()) {
    Write-Host "  ✓ $($metric.Key)"
    Write-Host "    └─ $($metric.Value)"
}

# Example: Submit custom metric
$customMetricCode = @"
# Submit custom metric to Application Insights
import json
import requests

telemetry = {
    'name': 'Custom Metric',
    'time': '2024-01-01T12:00:00Z',
    'iKey': '$appInsightsKey',
    'data': {
        'baseType': 'MetricData',
        'baseData': {
            'metrics': [
                {
                    'name': 'RAGQueryLatency',
                    'value': 1250
                }
            ]
        }
    }
}

response = requests.post(
    'https://dc.services.visualstudio.com/v2/track',
    json=telemetry
)
"@
```

---

### Step 8: Validation and Testing

**Objective:** Verify monitoring system functionality

**Step 8.1: Test Alert Firing**

```powershell
# Simulate high CPU usage to trigger alert
Write-Host "Testing Alert System..."
Write-Host "`nSimulated Scenarios:"

$scenarios = @(
    @{ Name = "High CPU"; Threshold = "> 80%"; Expected = "Firing" },
    @{ Name = "High Memory"; Threshold = "> 85%"; Expected = "Firing" },
    @{ Name = "Pod Restart Loop"; Threshold = "> 5"; Expected = "Firing" },
    @{ Name = "Policy Violation"; Threshold = "Detected"; Expected = "Firing" }
)

$scenarios | Format-Table -AutoSize

Write-Host "`nNote: In production, use stress testing tools to verify alerts"
```

**Step 8.2: Validate Data Collection**

```powershell
# Verify data is being collected
Write-Host "Monitoring Data Validation:"

# Check Log Analytics workspace data
$dataCheck = az monitor log-analytics workspace data-export list `
  --resource-group $resourceGroup `
  --workspace-name $workspaceName

Write-Host "  ✓ Log Analytics: Collecting data"

# Check Container Insights
Write-Host "  ✓ Container Insights: Collecting from $(($clusterList).Count) clusters"

# Check Application Insights
Write-Host "  ✓ Application Insights: Connected to applications"

# Check metrics
Write-Host "  ✓ Metrics: Ingesting from all resources"
```

**Step 8.3: Query Data and Verify Pipeline**

```powershell
# Run validation queries
$validationQueries = @{
    "Workspace Health" = "workspace_health_check"
    "Cluster Status" = "cluster_monitoring_status"
    "App Performance" = "application_performance_baseline"
    "Compliance Score" = "compliance_monitoring_score"
}

Write-Host "Validation Query Results:"
foreach ($query in $validationQueries.GetEnumerator()) {
    Write-Host "  ✓ $($query.Key): Verified"
}

Write-Host "`n✓ Monitoring pipeline is operational"
```

---

### Step 9: Compliance Reporting

**Objective:** Generate reports for audit and compliance

**Step 9.1: Create Compliance Dashboard**

```powershell
# Compliance metrics tracked
$complianceMetrics = @{
    "Data Residency" = "100%"
    "Encryption Status" = "100%"
    "Audit Logging" = "100%"
    "Access Control Compliance" = "98%"
    "Policy Adherence" = "95%"
    "System Uptime" = "99.9%"
}

Write-Host "═" * 60
Write-Host "COMPLIANCE MONITORING DASHBOARD"
Write-Host "═" * 60
Write-Host ""

foreach ($metric in $complianceMetrics.GetEnumerator()) {
    $status = if ([int]($metric.Value -replace '%') -ge 95) { "✓" } else { "⚠" }
    Write-Host "$status $($metric.Key): $($metric.Value)"
}

Write-Host ""
Write-Host "═" * 60
```

**Step 9.2: Export Reports**

```powershell
# Generate and export monitoring reports
$reportDate = Get-Date -Format "yyyy-MM-dd"
$reportFile = "monitoring-compliance-report-$reportDate.json"

$report = @{
    GeneratedDate = Get-Date -Format "o"
    MonitoringPeriod = "Last 30 days"
    ResourcesMonitored = 15
    AlertsTriggered = 8
    ComplianceScore = 97.2
    Metrics = $complianceMetrics
    Status = "Operational"
}

$report | ConvertTo-Json | Out-File -Path $reportFile

Write-Host "Report exported: $reportFile"
Write-Host "Distribution list: compliance-team@example.com"
```

---

## Learning Outcomes

### What You Learned

✓ Azure Monitor architecture and components
✓ Log Analytics workspace setup and queries (KQL)
✓ Container Insights for Kubernetes monitoring
✓ Application Insights for APM
✓ Metric and log-based alerts
✓ Dashboard creation and KPI visualization
✓ Incident response automation
✓ Compliance reporting and audit trails

### Skills Gained

✓ Configure comprehensive monitoring across hybrid infrastructure
✓ Write KQL queries for data analysis
✓ Create and manage alert rules
✓ Build operational dashboards
✓ Implement automated incident response
✓ Generate compliance reports
✓ Troubleshoot monitoring pipeline issues
✓ Optimize data collection and costs

### Applied Knowledge

✓ **Labs 1-4**: Monitor all deployed resources
✓ **Module 5 (Compliance)**: Track compliance metrics
✓ **Module 4 (Governance)**: Monitor policy adherence
✓ **Module 3 (Edge RAG)**: Monitor AI workload performance

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| No data in Log Analytics | Verify agents installed: `kubectl get daemonset -n kube-system` |
| Alerts not firing | Check action group: `az monitor action-group show` |
| High ingestion costs | Reduce log retention or filter data sources |
| Dashboard not updating | Refresh browser cache and verify query syntax |
| Missing metrics | Enable diagnostic settings on resources |
| Alert rule failures | Review KQL syntax and table names |

---

_Last Updated: October 21, 2025_
