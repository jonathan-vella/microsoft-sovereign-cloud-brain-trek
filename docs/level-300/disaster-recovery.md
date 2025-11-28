---
layout: default
title: Disaster Recovery
nav_order: 32
parent: Level 300 - Advanced
nav_exclude: true
description: "Multi-region disaster recovery patterns"
---

# Disaster Recovery Topology


{: .no_toc }

Multi-region disaster recovery patterns with data sovereignty compliance.


## Table of Contents

{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

Disaster recovery for sovereign cloud environments requires careful balance between resilience and data residency. This module covers DR patterns that maintain sovereignty while providing business continuity.

## Learning Objectives

After completing this section, you will be able to:

- ✅ Design multi-region DR with sovereignty constraints
- ✅ Implement geo-replication within sovereignty boundaries
- ✅ Configure failover procedures
- ✅ Test DR without violating data residency

---


## Disaster Recovery Architecture


| Strategy | RTO | RPO | Sovereignty Impact |
|----------|-----|-----|-------------------|
| **Backup/Restore** | Hours | Hours | Low (data stays in region) |
| **Pilot Light** | Minutes | Minutes | Medium (standby in paired region) |
| **Warm Standby** | Minutes | Near-zero | Medium (active replication) |
| **Hot/Active** | Seconds | Zero | High (multi-region active) |

---

## Sovereign Region Pairs

### Azure Region Pairing

| Primary Region | Paired Region | Sovereignty Zone |
|----------------|---------------|------------------|
| West Europe | North Europe | EU |
| Germany West Central | Germany North | Germany |
| France Central | France South | France |
| Switzerland North | Switzerland West | Switzerland |
| US Gov Virginia | US Gov Texas | US Government |

### Cross-Sovereignty Considerations

{: .warning }
> **⚠️ Cross-Sovereignty Failover**
> Some regulations prohibit data leaving the sovereignty boundary even during disasters. Verify with legal/compliance before implementing cross-region DR.

---

## Replication Patterns

### SQL Database Geo-Replication

```powershell
# Configure geo-replication within EU
$primaryDatabase = Get-AzSqlDatabase `
    -ResourceGroupName "primary-rg" `
    -ServerName "eu-west-sql" `
    -DatabaseName "appdb"

# Create secondary in EU North
New-AzSqlDatabaseSecondary `
    -ResourceGroupName "primary-rg" `
    -ServerName "eu-west-sql" `
    -DatabaseName "appdb" `
    -PartnerResourceGroupName "dr-rg" `
    -PartnerServerName "eu-north-sql" `
    -PartnerDatabaseName "appdb" `
    -AllowConnections "All"
```

### Storage Account Replication

```yaml
# GRS replication within sovereignty zone
storageReplication:
  primary:
    region: "westeurope"
    account: "primary-storage"

  replicationType: "GRS"  # Geo-redundant

  # Note: GRS replicates to paired region (North Europe)
  # This keeps data within EU sovereignty zone

  accessTier:
    primary: "Hot"
    secondary: "Cool"  # Cost optimization for DR

  failover:
    automaticFailover: false  # Manual for compliance
    minimumRPO: "PT15M"  # 15 minutes
```

### Cosmos DB Multi-Region

```powershell
# Configure Cosmos DB with EU regions only
$cosmosAccount = New-AzCosmosDBAccount `
    -ResourceGroupName "data-rg" `
    -Name "eu-cosmos" `
    -Location @(
        @{ LocationName = "West Europe"; FailoverPriority = 0 },
        @{ LocationName = "North Europe"; FailoverPriority = 1 }
    ) `
    -DefaultConsistencyLevel "BoundedStaleness" `
    -EnableAutomaticFailover $true `
    -EnableMultipleWriteLocations $false  # Single write region
```

---

## Failover Procedures

### Traffic Manager Configuration

```yaml
# Traffic Manager for regional failover
trafficManager:
  name: "sovereign-app-tm"
  routingMethod: "Priority"

  endpoints:
    - name: "primary-eu-west"
      type: "Azure"
      targetResourceId: "/subscriptions/{sub}/resourceGroups/app-rg/providers/Microsoft.Web/sites/app-west"
      priority: 1
      weight: 1

    - name: "secondary-eu-north"
      type: "Azure"
      targetResourceId: "/subscriptions/{sub}/resourceGroups/dr-rg/providers/Microsoft.Web/sites/app-north"
      priority: 2
      weight: 1

  healthProbe:
    path: "/health"
    protocol: "HTTPS"
    intervalInSeconds: 30
    toleratedNumberOfFailures: 3
```

### Failover Runbook

```powershell
# Failover runbook for sovereign applications
workflow Invoke-SovereignFailover {
    param(
        [string]$TargetRegion = "northeurope",
        [string]$FailoverReason
    )

    # 1. Validate sovereignty compliance
    $approvedRegions = @("westeurope", "northeurope")
    if ($TargetRegion -notin $approvedRegions) {
        throw "Cannot failover to non-sovereign region: $TargetRegion"
    }

    # 2. Log compliance event
    Write-Output "Initiating failover to $TargetRegion"
    Send-ComplianceNotification -Event "DR-Failover" -Details @{
        TargetRegion = $TargetRegion
        Reason = $FailoverReason
        Timestamp = Get-Date -Format "o"
    }

    # 3. Execute failover in parallel
    InlineScript {
        # Database failover
        Invoke-AzSqlDatabaseFailover `
            -ResourceGroupName "dr-rg" `
            -ServerName "eu-north-sql" `
            -DatabaseName "appdb" `
            -ReadableSecondary "Enabled"
    }

    InlineScript {
        # Storage failover
        Invoke-AzStorageAccountFailover `
            -ResourceGroupName "dr-rg" `
            -Name "primary-storage"
    }

    # 4. Update Traffic Manager
    InlineScript {
        $profile = Get-AzTrafficManagerProfile -Name "sovereign-app-tm" -ResourceGroupName "network-rg"
        $profile.Endpoints[0].Priority = 2
        $profile.Endpoints[1].Priority = 1
        Set-AzTrafficManagerProfile -TrafficManagerProfile $profile
    }

    Write-Output "Failover complete. Active region: $TargetRegion"
}
```

---

## DR Testing

### Test Without Data Movement

```yaml
# DR test configuration - no actual data movement
drTest:
  type: "Simulation"
  frequency: "Quarterly"

  testScenarios:
    - name: "Primary Region Outage"
      simulation: "Block traffic to primary"
      expectedRTO: "PT15M"

    - name: "Database Failover"
      simulation: "Readonly primary"
      expectedRPO: "PT5M"

  complianceChecks:
    - name: "Data Location Verification"
      validation: "All data remains in EU regions"

    - name: "Access Log Review"
      validation: "No cross-region data transfer"
```

### Chaos Engineering

```powershell
# Azure Chaos Studio experiment
$experiment = @{
    identity = @{
        type = "SystemAssigned"
    }
    properties = @{
        selectors = @(
            @{
                type = "List"
                id = "Selector1"
                targets = @(
                    @{
                        type = "ChaosTarget"
                        id = "/subscriptions/{sub}/resourceGroups/app-rg/providers/Microsoft.Web/sites/app-west/providers/Microsoft.Chaos/targets/microsoft-app-service"
                    }
                )
            }
        )
        steps = @(
            @{
                name = "SimulateOutage"
                branches = @(
                    @{
                        name = "Branch1"
                        actions = @(
                            @{
                                type = "discrete"
                                name = "urn:csci:microsoft:appService:stop/1.0"
                                parameters = @(
                                    @{
                                        key = "abruptShutdown"
                                        value = "true"
                                    }
                                )
                                selectorId = "Selector1"
                            }
                        )
                    }
                )
            }
        )
    }
}
```

---

## Recovery Metrics

### RTO/RPO Monitoring

```kusto
// DR metrics dashboard query
let drEvents = AzureActivity
| where TimeGenerated > ago(30d)
| where OperationNameValue contains "failover";

let recoveryTimes = drEvents
| summarize
    FailoverStart = min(TimeGenerated),
    FailoverEnd = max(TimeGenerated)
    by CorrelationId
| extend RecoveryTime = FailoverEnd - FailoverStart;

recoveryTimes
| summarize
    AvgRTO = avg(RecoveryTime),
    MaxRTO = max(RecoveryTime),
    FailoverCount = count()
```

---

## Implementation Checklist

- [ ] Identify sovereign region pairs
- [ ] Configure geo-replication for databases
- [ ] Set up storage GRS replication
- [ ] Deploy Traffic Manager
- [ ] Create failover runbooks
- [ ] Configure health probes
- [ ] Set up DR monitoring
- [ ] Document failover procedures
- [ ] Schedule DR tests
- [ ] Train operations team

---

## Next Steps

- **[Incident Response →](incident-response.md)** — Handle DR-related incidents
- **[Observability Stack →](observability-stack.md)** — Monitor DR health

---

**Reference:** [Azure Site Recovery](https://learn.microsoft.com/en-us/azure/site-recovery/) — Microsoft Learn
