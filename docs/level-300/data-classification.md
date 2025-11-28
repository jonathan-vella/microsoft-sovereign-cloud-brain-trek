---
layout: default
title: Data Classification
nav_order: 21
parent: Level 300 - Advanced
nav_exclude: true
description: "Data classification workflows for sovereign cloud environments"
---

# Data Classification and Protection


{: .no_toc }

Implementing data classification workflows to identify, categorize, and protect sensitive information in sovereign cloud environments.


## Table of Contents

{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

Data classification is the foundation of data sovereignty. Before you can protect sensitive data, you must first understand what data you have, where it resides, and its sensitivity level. This module covers automated and manual classification approaches.

## Learning Objectives

After completing this section, you will be able to:

- ✅ Design a data classification taxonomy
- ✅ Implement automated classification with Microsoft Purview
- ✅ Apply protection policies based on classification
- ✅ Monitor classification compliance across the organization

---

## Data Classification Flow

The following diagram illustrates the complete data classification workflow from discovery to protection:

```mermaid
flowchart TB
    subgraph Discovery ["1️⃣ Discovery Phase"]
        A[Data Sources] --> B[Microsoft Purview<br/>Data Map]
        B --> C[Automated Scanning]
        C --> D[Content Inspection]
    end

    subgraph Classification ["2️⃣ Classification Phase"]
        D --> E{Classification<br/>Engine}
        E -->|PII Detected| F[Personal Data]
        E -->|Financial| G[Confidential]
        E -->|Health| H[PHI/HIPAA]
        E -->|Public| I[Non-Sensitive]
    end

    subgraph Labeling ["3️⃣ Labeling Phase"]
        F --> J[Apply Sensitivity<br/>Label]
        G --> J
        H --> J
        I --> J
        J --> K[Encryption Policy]
        J --> L[Access Policy]
        J --> M[Retention Policy]
    end

    subgraph Protection ["4️⃣ Protection Phase"]
        K --> N[Azure RMS<br/>Encryption]
        L --> O[Conditional<br/>Access]
        M --> P[Data Lifecycle<br/>Management]
    end

    subgraph Monitoring ["5️⃣ Monitoring Phase"]
        N --> Q[Activity Logs]
        O --> Q
        P --> Q
        Q --> R[Compliance<br/>Dashboard]
        R --> S{Compliant?}
        S -->|No| T[Alert &<br/>Remediate]
        S -->|Yes| U[Audit Report]
    end

    style Discovery fill:#E8F4FD,stroke:#0078D4
    style Classification fill:#FFF4E6,stroke:#FF8C00
    style Labeling fill:#F3E8FF,stroke:#5C2D91
    style Protection fill:#FFE4E1,stroke:#D13438

    style Monitoring fill:#D4E9D7,stroke:#107C10_
```

*Figure 1: Data classification workflow from discovery to continuous monitoring_

---

## Classification Taxonomy

### Sensitivity Levels

| Level | Description | Examples | Protection |
|-------|-------------|----------|------------|
| **Public** | No confidentiality requirements | Marketing materials, public docs | None required |
| **Internal** | Business-only information | Policies, procedures | Basic access control |
| **Confidential** | Business-sensitive data | Financial data, contracts | Encryption + access control |
| **Highly Confidential** | Restricted access | Trade secrets, M&A data | CMK encryption + MFA |
| **Regulated** | Legal/compliance requirements | PII, PHI, PCI data | Full DLP + audit |

### Regulatory Classifications

For sovereignty compliance, additional regulatory labels may apply:

- **GDPR Personal Data** — EU data subject information
- **HIPAA PHI** — Protected health information
- **PCI DSS** — Payment card data
- **ITAR/EAR** — Export controlled data
- **Classified** — Government security classifications

---

## Microsoft Purview Integration

### Data Map Configuration

```powershell
# Register data sources with Microsoft Purview
Register-AzPurviewDataSource `
    -AccountName "contoso-purview" `
    -DataSourceType "AzureBlob" `
    -ResourceId "/subscriptions/{sub-id}/resourceGroups/data-rg/providers/Microsoft.Storage/storageAccounts/sensitivedata"

# Configure scanning rule set for PII detection
New-AzPurviewScanRuleSet `
    -AccountName "contoso-purview" `
    -Name "EU-PII-Ruleset" `
    -Kind "AzureBlob" `
    -SystemClassificationRuleName @("GDPR", "EU.SSN", "EU.Passport")
```

### Automated Classification Rules

| Rule Type | Detection Method | Examples |
|-----------|-----------------|----------|
| Built-in | Regex + ML | Credit cards, SSN, email |
| Custom | Regex patterns | Employee IDs, custom codes |
| Trainable | Machine learning | Document types, contracts |
| Dictionary | Word lists | Project names, locations |

---

## Protection Policies

### Label-Based Protection

When a sensitivity label is applied, automatic protection policies activate:

```yaml
# Example: Confidential Label Policy
label:
  name: "Confidential"
  tooltip: "Business-sensitive information"
protection:
  encryption:
    enabled: true
    keySource: "customer-managed"
    keyVault: "/subscriptions/{sub}/resourceGroups/keys-rg/..."
  access:
    requireMFA: true
    allowedLocations: ["EU West", "EU North"]
  watermark:
    enabled: true
    text: "CONFIDENTIAL - ${user.name}"
  dlp:
    blockExternalSharing: true
    preventCopy: true
```

---

## Implementation Checklist

- [ ] Define classification taxonomy
- [ ] Deploy Microsoft Purview account
- [ ] Register all data sources
- [ ] Configure scanning schedules
- [ ] Create custom classification rules
- [ ] Define sensitivity labels
- [ ] Assign protection policies
- [ ] Enable continuous monitoring
- [ ] Train users on classification

---

## Next Steps

- **[Incident Response Workflow →](incident-response.md)** — Handle security incidents
- **[Encryption & Key Management →](../level-200/encryption-key-management.md)** — Protect classified data

---

**Reference:** [Microsoft Purview Data Classification](https://learn.microsoft.com/en-us/microsoft-365/compliance/data-classification-overview) — Microsoft Learn
