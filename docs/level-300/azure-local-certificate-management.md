---
layout: default
title: Certificate Management in Disconnected Environments
parent: Azure Local at Scale - Disconnected Mode
nav_order: 2
---

# Certificate Management in Disconnected Environments

## Overview

Manage certificates manually in air-gapped environments without cloud certificate services or automated renewal capabilities.

---

## Manual Certificate Lifecycle

> **📊 Visual Reference Needed** *(Optional)*  
> *Certificate Lifecycle Management (Asset 51)*  
> Timeline showing certificate issue, validity periods, renewal windows, key procedures, and decision points for manual management.  
> **Specification Reference:** See `docs/level-300/VISUAL_SPECIFICATIONS.md` → Asset 51  
> **Source to adapt:** [Certificate lifecycle in Azure Local](https://learn.microsoft.com/en-us/azure/azure-local/manage/certificate-management?view=azloc-2509)

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
