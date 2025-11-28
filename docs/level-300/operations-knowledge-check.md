---
layout: default
title: Operations - Knowledge Check
parent: Level 300 - Advanced
nav_order: 16
description: "Assessment covering observability, DevSecOps, and disaster recovery for sovereign clouds"
---

# Operations - Knowledge Check

{: .no_toc }

Test your expertise in sovereign cloud operations including observability architecture, DevSecOps pipelines, and disaster recovery strategies.

---

## Quiz Instructions

**Total Questions:** 15  
**Passing Score:** 12/15 (80%)  
**Time Estimate:** 25-35 minutes  
**Format:** Expert-level scenario-based questions

This assessment covers:

- Observability architecture and sovereign monitoring
- DevSecOps pipelines with security automation
- Disaster recovery planning and execution
- Operational resilience patterns

---

### Question 1: Observability — Log Data Sovereignty

A multinational organization has Azure Local clusters in EU and US. Where should logs be stored for GDPR compliance?

A) Central global Log Analytics workspace  
B) Regional Log Analytics workspaces per geography  
C) Only on-premises log storage  
D) Logs don't contain personal data, no restrictions

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Regional workspaces maintain data residency:

**Log Architecture:**

| Region | Log Analytics | Data Residency |
|--------|---------------|----------------|
| EU | West Europe workspace | EU Data Boundary |
| US | East US workspace | US territory |

**GDPR Considerations:**

- Logs may contain IP addresses, usernames, error messages with PII
- IP addresses are personal data under GDPR
- Logs must remain in-region by default
- Cross-region aggregation requires legal basis

**Implementation:**

- Separate workspace per sovereignty boundary
- Azure Monitor Agent configured per region
- Dashboards can query across workspaces (no data movement)

**Reference:** [Observability Stack](observability-stack.md)
</details>

---

### Question 2: DevSecOps — Shift Left Security

At which pipeline stage should container image vulnerability scanning occur?

A) Only in production  
B) At build time, before images are pushed to registry  
C) Only during annual security audits  
D) After deployment to staging

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Shift-left means finding vulnerabilities as early as possible:

**Pipeline Security Stages:**

| Stage | Security Activity |
|-------|-------------------|
| Commit | SAST, secrets scanning |
| **Build** | Container scanning, SBOM generation |
| Test | DAST, integration security tests |
| Deploy | Policy validation, admission control |
| Runtime | Continuous monitoring, anomaly detection |

**Build-Time Scanning Benefits:**

- Blocks vulnerable images from reaching registry
- Immediate feedback to developers
- Lower cost to fix than production
- Prevents supply chain attacks

**Tools:**

- Microsoft Defender for Containers
- Trivy, Grype, Snyk
- Azure Container Registry scanning

**Reference:** [DevSecOps Pipeline](devsecops-pipeline.md)
</details>

---

### Question 3: Disaster Recovery — RPO vs RTO

A financial services application requires RPO of 1 hour and RTO of 15 minutes. Which DR strategy meets these requirements?

A) Daily backup to tape  
B) Asynchronous replication with hot standby  
C) Synchronous replication with automatic failover  
D) Weekly full backups with daily incrementals

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: C**

**Explanation:**
Synchronous replication with auto-failover meets strict requirements:

**DR Strategy Comparison:**

| Strategy | Typical RPO | Typical RTO | Cost |
|----------|-------------|-------------|------|
| Tape backup | 24 hours | Days | $ |
| Async replication | 15-60 min | Hours | $$ |
| **Sync replication** | Near-zero | Minutes | $$$ |
| Active-Active | Zero | Zero | $$$$ |

**Requirements Analysis:**

- RPO 1 hour: Sync or async replication works
- RTO 15 minutes: Requires hot standby + auto-failover
- Combination: Synchronous replication ensures near-zero data loss, hot standby enables fast recovery

**Implementation:**

- Storage Replica with synchronous mode
- Always On availability groups
- Automated failover triggers
- Pre-staged compute in DR site

**Reference:** [Disaster Recovery](disaster-recovery.md)
</details>

---

### Question 4: Observability — Metrics Aggregation

How should metrics be aggregated across multiple Azure Local clusters for a unified dashboard?

A) Export raw metrics to central location  
B) Use Azure Monitor with multi-workspace queries  
C) Aggregate only on-premises, no cloud visibility  
D) Create separate dashboards per cluster

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Multi-workspace queries provide unified view without data movement:

**Architecture:**

```text
Cluster EU → Azure Monitor (EU workspace)
Cluster US → Azure Monitor (US workspace)
                    ↓
         Multi-workspace dashboard
         (queries cross workspaces,
          data stays in place)
```

**Benefits:**

- Data residency maintained
- Single pane of glass for operations
- Alerts can span workspaces
- No bulk data transfer required

**Query Example:**

```kusto
union
    workspace('eu-workspace').Perf,
    workspace('us-workspace').Perf
| summarize avg(CounterValue) by Computer
```

**Reference:** [Observability Stack](observability-stack.md)
</details>

---

### Question 5: DevSecOps — Secrets Management

Where should application secrets (API keys, passwords) be stored in a DevSecOps pipeline?

A) In source code repository  
B) In CI/CD pipeline variables (unencrypted)  
C) Azure Key Vault with pipeline integration  
D) Environment variables in deployment manifests

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: C**

**Explanation:**
Key Vault provides secure, audited secrets management:

**Secrets Management Hierarchy:**

| Approach | Security Level | Audit | Rotation |
|----------|----------------|-------|----------|
| Source code | ❌ None | ❌ | ❌ |
| Pipeline vars | ⚠️ Limited | ⚠️ | ❌ |
| **Key Vault** | ✅ High | ✅ | ✅ |
| Hardware HSM | ✅✅ Highest | ✅ | ✅ |

**Key Vault Integration:**

- Pipeline retrieves secrets at deploy time
- Secrets never stored in repo or logs
- RBAC controls who can access
- Full audit trail of access
- Automatic rotation capabilities

**Why Not Others:**

- **A:** Secrets in code = security breach waiting to happen
- **B:** Pipeline vars may appear in logs
- **D:** Manifests often committed to source control

**Reference:** [DevSecOps Pipeline](devsecops-pipeline.md)
</details>

---

### Question 6: Disaster Recovery — Failover Testing

How frequently should disaster recovery failover be tested for production sovereign systems?

A) Only after major changes  
B) Annually  
C) Quarterly at minimum, with tabletop exercises monthly  
D) Never — testing is too risky for production

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: C**

**Explanation:**
Regular testing ensures DR readiness:

**Testing Cadence:**

| Test Type | Frequency | Scope |
|-----------|-----------|-------|
| Tabletop exercise | Monthly | Walkthrough, no actual failover |
| Partial failover | Quarterly | Subset of systems, controlled |
| Full failover | Annually | Complete DR activation |
| Chaos engineering | Continuous | Random failure injection |

**Why Quarterly+:**

- Systems change constantly
- Staff turnover requires retraining
- Dependencies may have changed
- Regulatory requirements (many require annual testing)

**Testing Best Practices:**

- Document and review results
- Update runbooks based on findings
- Track recovery time metrics
- Involve all stakeholders

**Reference:** [Disaster Recovery](disaster-recovery.md)
</details>

---

### Question 7: Observability — Distributed Tracing

A request fails in a microservices architecture. How can the root cause be identified?

A) Check each service's logs manually  
B) Use distributed tracing with correlation IDs  
C) Restart all services  
D) Wait for user complaints to identify pattern

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Distributed tracing correlates requests across services:

**Tracing Components:**

| Component | Purpose |
|-----------|---------|
| Trace ID | Unique identifier for entire request |
| Span ID | Identifier for each service hop |
| Parent Span | Links child to parent operation |
| Context propagation | Passes IDs across service boundaries |

**Example Trace:**

```text
Trace: abc123
├── API Gateway (span: 1)
│   ├── Auth Service (span: 2)
│   └── Order Service (span: 3) ← ERROR
│       ├── Inventory Service (span: 4)
│       └── Payment Service (span: 5)
```

**Tools:**

- Azure Monitor Application Insights
- Jaeger, Zipkin
- OpenTelemetry standard

**Reference:** [Observability Stack](observability-stack.md)
</details>

---

### Question 8: DevSecOps — Infrastructure as Code Security

How should Terraform/ARM templates be secured in a DevSecOps pipeline?

A) No scanning needed — IaC is just configuration  
B) Static analysis for security misconfigurations before deployment  
C) Only review in production  
D) Manual review of all templates

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
IaC security scanning prevents misconfigurations:

**IaC Security Scanning:**

| Check | Example Issue |
|-------|---------------|
| Public access | Storage account with public blob access |
| Encryption | Disk without encryption at rest |
| Network exposure | NSG allowing 0.0.0.0/0 inbound |
| IAM | Overly permissive role assignments |
| Secrets | Hardcoded passwords in templates |

**Pipeline Integration:**

```yaml
steps:
  - task: tfsec
    displayName: 'Terraform Security Scan'
  - task: checkov
    displayName: 'IaC Policy Check'
  - task: terraform-plan
    condition: and(succeeded(), eq(variables['Build.Reason'], 'PullRequest'))
```

**Tools:**

- tfsec, Checkov, Terrascan
- Microsoft Defender for DevOps
- OPA/Gatekeeper policies

**Reference:** [DevSecOps Pipeline](devsecops-pipeline.md)
</details>

---

### Question 9: Disaster Recovery — Data Consistency

During failover, how can data consistency be verified between primary and DR sites?

A) Assume consistency if replication was active  
B) Compare checksums/hashes of critical datasets  
C) User acceptance testing only  
D) Consistency isn't important in DR scenarios

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Checksums verify data integrity:

**Consistency Verification:**

| Method | Purpose |
|--------|---------|
| **Checksums** | Verify file/block integrity |
| Record counts | Verify transaction completeness |
| Hash comparison | Detect silent corruption |
| Application validation | Business logic verification |

**Verification Process:**

1. Identify critical datasets
2. Calculate checksums on primary (pre-failover)
3. Calculate checksums on DR (post-failover)
4. Compare and document discrepancies
5. Remediate gaps before production cutover

**Why Important:**

- Replication can fail silently
- Corruption can propagate
- Business continuity requires trusted data

**Reference:** [Disaster Recovery](disaster-recovery.md)
</details>

---

### Question 10: Observability — Alert Fatigue

An operations team receives 500+ alerts daily. What is the BEST approach to reduce alert fatigue?

A) Disable all alerts  
B) Implement alert tiering, aggregation, and intelligent suppression  
C) Hire more operations staff  
D) Only alert on complete system outages

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Intelligent alerting reduces noise while maintaining visibility:

**Alert Management Strategies:**

| Strategy | Description |
|----------|-------------|
| **Tiering** | P1 (page), P2 (ticket), P3 (log) |
| **Aggregation** | Group related alerts into incidents |
| **Suppression** | Suppress during maintenance windows |
| **Correlation** | Identify root cause, suppress symptoms |
| **Auto-remediation** | Resolve known issues automatically |

**Implementation:**

- Define alert severity based on business impact
- Use AIOps for pattern detection
- Implement runbooks for common alerts
- Track alert-to-incident ratio as metric

**Target:**

< 10 actionable alerts per on-call shift

**Reference:** [Observability Stack](observability-stack.md)
</details>

---

### Question 11: DevSecOps — Compliance as Code

How should regulatory compliance requirements be enforced in a DevSecOps pipeline?

A) Manual compliance review before each release  
B) Automated policy checks with Azure Policy and OPA  
C) Annual compliance audits only  
D) Trust developers to follow guidelines

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Automated policy enforcement ensures continuous compliance:

**Compliance as Code:**

| Layer | Tool | Example |
|-------|------|---------|
| Code | SAST | No hardcoded secrets |
| Config | OPA/Gatekeeper | Required encryption |
| Infrastructure | Azure Policy | Allowed regions only |
| Runtime | Defender for Cloud | Continuous posture assessment |

**Pipeline Example:**

```yaml
- stage: Compliance
  jobs:
    - job: PolicyCheck
      steps:
        - task: opa-eval
          inputs:
            policy: 'sovereignty-policies/'
            input: 'deployment.yaml'
        - task: azure-policy
          inputs:
            scope: 'subscription'
```

**Benefits:**

- Every deployment validated
- Immediate feedback on violations
- Audit trail of compliance checks
- Scales without additional headcount

**Reference:** [DevSecOps Pipeline](devsecops-pipeline.md)
</details>

---

### Question 12: Disaster Recovery — Communication Plan

During a disaster, who should be notified and in what order?

A) Customers first, then internal teams  
B) Incident commander activates defined communication tree  
C) No communication until issue is fully resolved  
D) Post on social media immediately

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Structured communication prevents chaos:

**Communication Tree:**

| Order | Stakeholder | Responsibility |
|-------|-------------|----------------|
| 1 | Incident Commander | Overall coordination |
| 2 | Technical Team | Investigation and recovery |
| 3 | Leadership | Business decisions |
| 4 | Legal/Compliance | Regulatory notification |
| 5 | Communications | Customer/public messaging |
| 6 | Customers | Status updates |

**Communication Principles:**

- Single source of truth (incident commander)
- Regular status updates (every 30-60 min)
- Prepared templates for common scenarios
- Clear escalation paths

**Regulatory Requirements:**

- GDPR: 72-hour breach notification
- HIPAA: 60-day breach notification
- Financial services: Regulator notification

**Reference:** [Disaster Recovery](disaster-recovery.md)
</details>

---

### Question 13: Observability — Synthetic Monitoring

What is the purpose of synthetic monitoring for sovereign cloud applications?

A) Monitor real user traffic only  
B) Proactively detect issues before users are affected  
C) Replace all other monitoring  
D) Synthetic monitoring is not applicable to sovereign environments

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Synthetic monitoring provides proactive detection:

**Synthetic vs Real User Monitoring:**

| Aspect | Synthetic | Real User (RUM) |
|--------|-----------|-----------------|
| Timing | Continuous, scheduled | When users are active |
| Coverage | All endpoints, 24/7 | Only visited paths |
| Baseline | Consistent | Varies by user |
| Detection | Proactive | Reactive |

**Synthetic Monitoring Use Cases:**

- API health checks every minute
- Critical user journey testing
- Baseline performance tracking
- Early warning before business hours

**Sovereignty Consideration:**

- Synthetic probes should run from within sovereignty boundary
- Results stored in regional workspace
- Probe traffic may contain test credentials

**Reference:** [Observability Stack](observability-stack.md)
</details>

---

### Question 14: DevSecOps — Software Bill of Materials (SBOM)

Why is SBOM important for sovereign cloud deployments?

A) Only required for open source projects  
B) Enables vulnerability tracking, license compliance, and supply chain transparency  
C) Replaces all other security scanning  
D) SBOMs are only for marketing purposes

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
SBOM provides transparency into software composition:

**SBOM Benefits:**

| Benefit | Description |
|---------|-------------|
| **Vulnerability tracking** | When CVE announced, identify affected deployments |
| **License compliance** | Ensure no prohibited licenses in sovereign apps |
| **Supply chain** | Know exactly what's in your software |
| **Audit** | Provide evidence for compliance audits |

**SBOM Standards:**

- SPDX (Linux Foundation)
- CycloneDX (OWASP)
- SWID Tags (ISO/IEC 19770-2)

**Regulatory Drivers:**

- US Executive Order 14028 requires SBOM
- EU Cyber Resilience Act will require SBOM
- FedRAMP increasingly expects SBOM

**Reference:** [DevSecOps Pipeline](devsecops-pipeline.md)
</details>

---

### Question 15: Disaster Recovery — Recovery Prioritization

During recovery from a major outage, which systems should be restored first?

A) All systems simultaneously  
B) Systems based on defined recovery tiers aligned with business impact  
C) Alphabetically by system name  
D) Newest systems first

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Recovery tiers ensure critical systems are restored first:

**Recovery Tier Model:**

| Tier | RTO | Systems | Priority |
|------|-----|---------|----------|
| **Tier 0** | < 1 hour | Identity, DNS, core infrastructure | First |
| **Tier 1** | < 4 hours | Critical business apps, databases | Second |
| **Tier 2** | < 24 hours | Supporting systems, analytics | Third |
| **Tier 3** | < 72 hours | Dev/test, non-critical apps | Last |

**Dependency Mapping:**

```text
Tier 0: Active Directory, DNS
    ↓
Tier 1: ERP, Customer DB
    ↓
Tier 2: Reporting, Email
    ↓
Tier 3: Dev environments
```

**Why Tiering:**

- Limited recovery resources
- Dependencies prevent parallel recovery
- Business impact varies by system
- Regulatory requirements for critical systems

**Reference:** [Disaster Recovery](disaster-recovery.md)
</details>

---

## Assessment Complete

**Scoring Guide:**

| Score | Result |
|-------|--------|
| 15/15 | Expert — Ready for production operations management |
| 12-14/15 | Proficient — Minor review recommended |
| 9-11/15 | Developing — Review highlighted topics |
| < 9/15 | Needs Improvement — Complete module review |

---

## Next Steps

- **Review:** [Observability Stack](observability-stack.md)
- **Review:** [DevSecOps Pipeline](devsecops-pipeline.md)
- **Review:** [Disaster Recovery](disaster-recovery.md)
- **Complete:** [Level 300 Summary](README.md)
