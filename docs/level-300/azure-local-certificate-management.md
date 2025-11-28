---
layout: default
title: Certificate Management in Disconnected Environments
parent: Module 3 - Azure Local Disconnected
nav_order: 2
---

# Certificate Management in Disconnected Environments

## Overview

<details class="diagram-container">
<summary>View Diagram: PKI Hierarchy for Air-Gapped Environments</summary>
<div class="diagram-content" markdown="1">

```mermaid
graph TB
    subgraph Offline["Offline Root CA"]
        ROOT[Root CA<br/>10+ Year Validity<br/>HSM Protected]
    end

    subgraph Issuing["Issuing CAs"]
        ROOT --> ICA1[Issuing CA 1<br/>Infrastructure]
        ROOT --> ICA2[Issuing CA 2<br/>User Auth]
        ROOT --> ICA3[Issuing CA 3<br/>Code Signing]
    end

    subgraph Certs["End Certificates"]
        ICA1 --> CERT1[Server Certs]
        ICA1 --> CERT2[Client Certs]
        ICA2 --> CERT3[User Certs]
        ICA2 --> CERT4[Smart Card]
        ICA3 --> CERT5[Code Sign]
    end

    subgraph Lifecycle["Lifecycle Management"]
        GEN[Generation]
        DIST[Distribution]
        MON[Monitoring]
        RENEW[Renewal]
        REV[Revocation]
        GEN --> DIST --> MON --> RENEW
        MON --> REV
    end

    style Offline fill:#D13438,stroke:#A4262C,stroke-width:3px,color:#fff
    style Issuing fill:#FFF4E6,stroke:#FF8C00,stroke-width:2px,color:#000
    style Certs fill:#D4E9D7,stroke:#107C10,stroke-width:2px,color:#000
    style Lifecycle fill:#E8F4FD,stroke:#0078D4,stroke-width:2px,color:#000
```

_Figure 1: PKI hierarchy for air-gapped Azure Local environments_

</div>
</details>

Manage certificates manually in air-gapped environments without cloud certificate services or automated renewal capabilities.

---

## Manual Certificate Lifecycle


---

## Key Management

- Certificate generation offline
- Key storage in HSM or secure vaults
- Backup and recovery procedures
- Expiration tracking
- Renewal planning

---

## Renewal Procedures

- Pre-renewal validation
- Certificate generation
- Testing on staging system
- Manual deployment
- Verification procedures

---

## Emergency Procedures

- Certificate revocation
- Emergency renewal
- Disaster recovery
- Recertification after incidents

---

**See also:** [Air-Gapped Architecture](azure-local-air-gapped) | [Disconnected Lab](azure-local-disconnected-lab)
