---
layout: default
title: Security Hardening Patterns
parent: Module 5 - Compliance & Security
nav_order: 8
---

# Security Hardening Patterns

## Overview

Security hardening is the process of minimizing attack surface and protecting systems through defense-in-depth strategies. This page covers network segmentation, least privilege access, vulnerability management, patch policies, and incident response procedures for Microsoft Sovereign Cloud deployments.

---

## Defense-in-Depth Strategy

### Layered Security Model

```text
DEFENSE-IN-DEPTH ARCHITECTURE
═════════════════════════════════════════════════════════════

CONCEPT: Multiple security layers (don't rely on single defense)

If one layer fails, others protect system

Layer 1: Physical Security
┌─────────────────────────────────────┐
│ Microsoft Data Center (Secure)      │
│ ├─ Armed guards (24/7)              │
│ ├─ Multi-factor authentication      │
│ ├─ Biometric scanners               │
│ ├─ Surveillance cameras (recorded)  │
│ ├─ Perimeter fencing                │
│ └─ All media physically encrypted   │
└─────────────────────────────────────┘
        ↓

Layer 2: Network Perimeter
┌─────────────────────────────────────┐
│ Internet-facing Protection          │
│ ├─ DDoS protection                  │
│ ├─ Web Application Firewall (WAF)   │
│ ├─ Network security groups (NSG)    │
│ ├─ Threat detection                 │
│ └─ Intrusion prevention              │
└─────────────────────────────────────┘
        ↓

Layer 3: Network Segmentation
┌─────────────────────────────────────┐
│ Internal Network Isolation          │
│ ├─ DMZ: Public-facing services      │
│ ├─ App Tier: Application servers    │
│ ├─ Data Tier: Databases             │
│ ├─ Mgmt Tier: Administration        │
│ └─ Firewalls between each tier      │
└─────────────────────────────────────┘
        ↓

Layer 4: Application Security
┌─────────────────────────────────────┐
│ Software & Code Protection          │
│ ├─ Input validation                 │
│ ├─ SQL injection prevention         │
│ ├─ Cross-site scripting (XSS) prep  │
│ ├─ Authentication enforcement       │
│ └─ Secure error handling            │
└─────────────────────────────────────┘
        ↓

Layer 5: Data Protection
┌─────────────────────────────────────┐
│ Information Security                │
│ ├─ Encryption at rest (AES-256)     │
│ ├─ Encryption in transit (TLS 1.3)  │
│ ├─ Key management                   │
│ ├─ Access control to data           │
│ └─ Data classification              │
└─────────────────────────────────────┘
        ↓

Layer 6: Monitoring & Response
┌─────────────────────────────────────┐
│ Detection & Response                │
│ ├─ Security monitoring (SIEM)       │
│ ├─ Log aggregation                  │
│ ├─ Threat intelligence              │
│ ├─ Incident response team           │
│ └─ Forensics capability             │
└─────────────────────────────────────┘

EXAMPLE ATTACK SCENARIO
──────────────────────

Attack: Ransomware from internet

Layer 1 Defense: DDoS Protection
├─ Attack: Large volume of requests
├─ Defense: Automatically rate-limited
├─ Result: Blocked before reaching servers
└─ Status: Attack didn't get past Layer 1

If Attack Continues...

Layer 2 Defense: WAF (Web Application Firewall)
├─ Attack: Attempts SQL injection
├─ Defense: WAF detects and blocks
├─ Result: Malicious SQL rejected
└─ Status: Attack blocked at Layer 2

If Attack Continues (Rare)...

Layer 3 Defense: Network Segmentation
├─ Attack: Compromise web server
├─ Defense: Web tier isolated from data tier
├─ Result: Attacker can't reach databases
└─ Status: Blast radius limited to web tier

Layer 4 Defense: Application Security
├─ Attack: Attempt privilege escalation
├─ Defense: Application only has minimal permissions
├─ Result: Attacker gains user access, not admin
└─ Status: Cannot execute critical operations

Layer 5 Defense: Data Encryption
├─ Attack: Access encrypted database files
├─ Defense: Data encrypted with unknown key
├─ Result: Data unreadable (worthless to attacker)
└─ Status: Data protected even if accessed

Layer 6 Defense: Monitoring & Response
├─ Detection: Unusual activity detected
├─ Response: Incident team notified automatically
├─ Action: Suspicious accounts disabled
├─ Recovery: System restored from backup
└─ Status: Incident contained and resolved

RESULT: Multiple layers provide redundancy
If one fails, others protect system
```

---

## Network Segmentation

### Segmented Architecture

```text
NETWORK SEGMENTATION DESIGN
═════════════════════════════════════════════════════════════

CONCEPT: Divide network into isolated security zones

Benefits:
├─ Blast radius: Breach in one zone doesn't compromise all
├─ Least privilege: Each zone has minimal permissions
├─ Monitoring: Traffic between zones more visible
├─ Compliance: Easier to meet regulatory requirements
└─ Flexibility: Scale each zone independently

EXAMPLE: Healthcare Organization Network

┌────────────────────────────────────────────────────────┐
│                  INTERNET (Untrusted)                  │
└────────────────────┬─────────────────────────────────┘
                     │
            ┌────────▼────────┐
            │  AZURE FIREWALL │
            │  ├─ DDoS protect│
            │  ├─ WAF rules   │
            │  └─ Rate limit  │
            └────────┬────────┘
                     │
        ┌────────────────────────────┐
        │    DMZ / Public Zone       │
        │    (Exposed services)      │
        │  ┌──────────────────────┐  │
        │  │ Web Application      │  │
        │  │ (App Gateway)        │  │
        │  │ ├─ SSL/TLS encrypt   │  │
        │  │ ├─ Public IP         │  │
        │  │ └─ DDoS mitigated    │  │
        │  └──────────────────────┘  │
        │           │                │
        │  ┌────────▼────────┐       │
        │  │  NSG Rules:     │       │
        │  │  ├─ HTTPS: ✓    │       │
        │  │  ├─ HTTP: Block │       │
        │  │  └─ SSH: Deny   │       │
        │  └─────────────────┘       │
        └────────────────────────────┘
                     │
        ┌────────────▼────────────┐
        │  Internal Firewall      │
        │  (App Tier ↔ Data Tier) │
        └────────────┬────────────┘
                     │
    ┌────────────────────────────────┐
    │   Application Tier             │
    │   (Private services)           │
    │  ┌──────────────────────────┐  │
    │  │ Web/API Servers          │  │
    │  │ ├─ Private IPs only      │  │
    │  │ ├─ No internet access    │  │
    │  │ └─ Inbound: Port 443     │  │
    │  └──────────────────────────┘  │
    │           │                    │
    │  ┌────────▼─────────┐          │
    │  │  NSG Rules:      │          │
    │  │  ├─ HTTP: ✓      │          │
    │  │  ├─ DB: ✓        │          │
    │  │  └─ SSH: Deny    │          │
    │  └──────────────────┘          │
    └────────────────────────────────┘
                     │
        ┌────────────▼────────────┐
        │  Data Access Firewall   │
        │  (App Tier ↔ DB)        │
        └────────────┬────────────┘
                     │
    ┌────────────────────────────────┐
    │   Data Tier (Highly Protected) │
    │  ┌──────────────────────────┐  │
    │  │ Azure SQL Database       │  │
    │  │ ├─ Private endpoint      │  │
    │  │ ├─ Encryption: AES-256   │  │
    │  │ ├─ Only app tier access  │  │
    │  │ └─ Audit: Every query    │  │
    │  └──────────────────────────┘  │
    │           │                    │
    │  ┌────────▼─────────┐          │
    │  │  NSG Rules:      │          │
    │  │  ├─ SQL: ✓       │          │
    │  │  ├─ HTTPS: Deny  │          │
    │  │  └─ SSH: Deny    │          │
    │  └──────────────────┘          │
    └────────────────────────────────┘
                     │
        ┌────────────▼────────────┐
        │  Backup Firewall        │
        │  (Data ↔ Backup Vault)  │
        └────────────┬────────────┘
                     │
    ┌────────────────────────────────┐
    │   Backup Tier (Read-Only)      │
    │  ┌──────────────────────────┐  │
    │  │ Recovery Services Vault  │  │
    │  │ ├─ Daily backups         │  │
    │  │ ├─ Geo-replicated        │  │
    │  │ └─ Access restricted     │  │
    │  └──────────────────────────┘  │
    │           │                    │
    │  ┌────────▼─────────┐          │
    │  │  NSG Rules:      │          │
    │  │  ├─ Backup: ✓    │          │
    │  │  └─ All else: ✗  │          │
    │  └──────────────────┘          │
    └────────────────────────────────┘

NETWORK SECURITY GROUP (NSG) RULES
──────────────────────────────────

Example: Web tier NSG

Rule Priority | Direction | Source  | Dest Port | Action
─────────────────────────────────────────────────────
100           | Inbound   | 0.0.0.0 | 443       | Allow  (Internet users)
101           | Inbound   | 0.0.0.0 | 80        | Deny   (Force HTTPS)
102           | Inbound   | 0.0.0.0 | 22        | Deny   (No SSH)
103           | Inbound   | 0.0.0.0 | 3389      | Deny   (No RDP)
110           | Inbound   | *       | *         | Deny   (Default: block all)
─────────────────────────────────────────────────────

Example: Database tier NSG

Rule Priority | Direction | Source            | Port | Action
──────────────────────────────────────────────────────
100           | Inbound   | 10.0.1.0/24       | 1433 | Allow  (App tier only)
101           | Inbound   | 0.0.0.0           | 1433 | Deny   (Anyone else)
102           | Inbound   | *                 | 22   | Deny   (No SSH)
110           | Inbound   | *                 | *    | Deny   (Default: block all)
120           | Outbound  | *                 | *    | Deny   (No outbound)
──────────────────────────────────────────────────────
```

### Firewall Policies

```text
AZURE FIREWALL POLICY IMPLEMENTATION
═════════════════════════════════════════════════════════════

POLICY LAYERS
──────────────────────────────────────────────────────────

Layer 1: Network Rules (IP/Protocol/Port)
├─ Purpose: Block traffic at network layer
├─ Speed: Fast (no payload inspection)
├─ Example: "Block all traffic from 192.168.1.0/24"
└─ Use case: Known bad IPs, internal firewalls

Layer 2: Application Rules (HTTP/HTTPS URLs)
├─ Purpose: Block based on domain/URL
├─ Speed: Moderate (inspects HTTP headers)
├─ Example: "Block access to facebook.com"
└─ Use case: Prevent data exfiltration

Layer 3: HTTPS Inspection (SSL/TLS Decryption)
├─ Purpose: Inspect encrypted HTTPS traffic
├─ Speed: Slow (CPU-intensive decryption)
├─ Example: "Block malicious domains in encrypted traffic"
├─ Requirement: Enterprise option (additional cost)
└─ Use case: High-security environments

EXAMPLE FIREWALL POLICIES
──────────────────────────

Policy Set: "Secure Healthcare Organization"

Collection 1: Deny Malicious Destinations
├─ Action: Deny
├─ Type: Application rule
├─ Rules:
│  ├─ Deny: *.torrentdownload.com (malware source)
│  ├─ Deny: *.ransomwareC2.ru (command & control)
│  ├─ Deny: *.bitcoinminer.io (cryptomining)
│  └─ Deny: *.sextortion-scam.com (phishing)
└─ Priority: 100 (evaluated first)

Collection 2: Require HTTPS Only
├─ Action: Deny
├─ Type: Network rule
├─ Rules:
│  ├─ Deny: * → * port 80 (all HTTP blocked)
│  ├─ Allow: * → * port 443 (HTTPS allowed)
│  └─ Deny: * → * port 21 (FTP not allowed)
└─ Priority: 101

Collection 3: Allow Required Services
├─ Action: Allow
├─ Type: Application rule
├─ Rules:
│  ├─ Allow: Internal servers → Windows Update (patching)
│  ├─ Allow: Internal servers → Office 365 (email)
│  ├─ Allow: Developers → GitHub (code repositories)
│  └─ Allow: Operations → ServiceNow (ticketing)
└─ Priority: 1000 (evaluated last)

Collection 4: Block Personal Services
├─ Action: Deny
├─ Type: Application rule
├─ Rules:
│  ├─ Deny: facebook.com (social media)
│  ├─ Deny: youtube.com (video streaming)
│  ├─ Deny: netflix.com (personal entertainment)
│  └─ Deny: *.torrent (file sharing)
└─ Priority: 200
```

---

## Least Privilege Access

### Role-Based Access Control (RBAC)

```text
LEAST PRIVILEGE IMPLEMENTATION
═════════════════════════════════════════════════════════════

CONCEPT: Grant minimum permissions needed to do job

Principles:
├─ Default: Deny all access
├─ Explicit: Grant only what's needed
├─ Temporary: Access expires (time-limited)
├─ Audited: Every access logged
└─ Reviewed: Quarterly access review

RBAC ROLE HIERARCHY
───────────────────

Owner (Full Control)
├─ Can: Create resources, manage access, delete resources
├─ Count: 1-2 per subscription (CTO, CISO)
├─ Duration: Permanent (executive role)
└─ Approval: Board level required
        │
        ├─ Contributor (Create/Modify)
        │   ├─ Can: Deploy resources, modify configuration
        │   ├─ Count: 5-10 per subscription (architects, admins)
        │   ├─ Duration: 1-year review cycle
        │   └─ Approval: CTO approval
        │           │
        │           ├─ Reader (View only)
        │           │   ├─ Can: View resources, no changes
        │           │   ├─ Count: 30-50 (managers, auditors)
        │           │   ├─ Duration: Annual review
        │           │   └─ Approval: Department manager
        │           │
        │           ├─ Virtual Machine Admin
        │           │   ├─ Can: Manage VMs, restart, patch
        │           │   ├─ Count: 5-10 (DevOps, operations)
        │           │   ├─ Duration: Temporary (1-month max)
        │           │   └─ Approval: Change management
        │           │
        │           ├─ SQL Admin
        │           │   ├─ Can: Manage SQL servers, backups
        │           │   ├─ Count: 2-3 (DBAs)
        │           │   ├─ Duration: 1-year review
        │           │   └─ Approval: CTO approval
        │           │
        │           └─ Managed Identity (Service Account)
        │               ├─ Can: Specific resource access
        │               ├─ Count: 50+ (one per application)
        │               ├─ Duration: Permanent (tied to app)
        │               └─ Approval: Application owner


EXAMPLE: Finance Team Permissions
──────────────────────────────────

Employee: Alice (Finance Manager)

Current Role: Contributor
├─ Permissions: Can modify all resources (TOO MUCH)
├─ Risk: Can delete databases, compromise security
└─ Status: NEEDS REDUCTION

Recommended Roles: Finance-specific RBAC
├─ Role 1: "Cost Management Analyst"
│  ├─ Permissions: View resource costs, generate reports
│  ├─ Resources: Can access cost management APIs
│  ├─ Duration: Permanent
│  └─ Cannot: Modify resources, delete resources
│
├─ Role 2: "Cost Optimization Reviewer"
│  ├─ Permissions: View resource configuration for cost
│  ├─ Resources: Can query resource properties
│  ├─ Duration: Temporary (3 months for special project)
│  └─ Cannot: Modify or delete anything
│
└─ Role 3: "Billing Reader"
   ├─ Permissions: View invoices, payment history
   ├─ Resources: Can access billing APIs
   ├─ Duration: Permanent
   └─ Cannot: Modify billing, create resources

Result: Alice can do her job (finance reporting)
But cannot compromise security

ROLE REVIEW PROCESS
──────────────────

Quarterly Access Review (Every 90 days):

Step 1: Gather Access Data
├─ Report: All users and their roles
├─ Query: Last 90 days of access/usage
├─ Analysis: Who actually used their permissions?
└─ Example:
   ├─ Alice (Finance Manager): Used 45 times
   ├─ Bob (Engineer): Used 1,247 times (very active)
   ├─ Charlie (On leave): Used 0 times (7 months on leave)
   └─ Diana (Contractor): Used 234 times (contract ending)

Step 2: Manager Review
├─ Reviewer: Direct manager confirms
├─ Questions:
│  ├─ "Does Alice still need Contributor role?"
│  ├─ "Should Charlie's access be removed (on leave)?"
│  ├─ "Should Diana's access expire (contract ending)?"
│  └─ "Is anyone requesting new permissions?"
├─ Time: 15 minutes per team member
└─ Deadline: Review completed within 5 days

Step 3: Update Access
├─ Remove: Access for employees on leave
├─ Reduce: Excessive permissions to least privilege
├─ Extend: Needed access gets extended
├─ Add: New team members get appropriate roles
└─ Document: Change log for audit trail

Step 4: Remediation
├─ Auto-remove: Access removal (if approved)
├─ Notify: Affected employees
├─ Log: Evidence for auditors
└─ Verify: Confirm removal took effect

COMPLIANCE EVIDENCE
──────────────────

Access Review Report:

┌────────────────────────────────────┐
│ Q4 2025 Access Review Report       │
│ Finance Department                 │
│                                    │
│ Review Period: Oct 1 - Oct 31      │
│ Reviewer: Sarah Kim (Manager)      │
│ Date Completed: Oct 31, 2025       │
│                                    │
│ FINDINGS:                          │
│                                    │
│ Total Employees: 15                │
│ ├─ Permissions Appropriate: 12     │
│ ├─ Permissions Reduced: 2          │
│ ├─ Permissions Added: 0            │
│ └─ Permissions Removed: 1          │
│                                    │
│ CHANGES MADE:                      │
│                                    │
│ 1. Alice Johnson                   │
│    Before: Contributor             │
│    After: Cost Analyst              │
│    Reason: Role changed for better │
│            least privilege         │
│                                    │
│ 2. Charlie Davis                   │
│    Before: Contributor             │
│    After: REMOVED                  │
│    Reason: 7 months on leave       │
│                                    │
│ COMPLIANCE STATUS: ✓ PASS          │
│ All access verified and audited    │
└────────────────────────────────────┘
```

---

## Patch Management & Vulnerability

### Patching Strategy

```text
PATCH MANAGEMENT LIFECYCLE
═════════════════════════════════════════════════════════════

CLASSIFICATION: Security Updates vs. Others

Critical Security Patch
├─ Severity: High (0-day exploit)
├─ Urgency: IMMEDIATE (within 24-48 hours)
├─ Example: Windows RDP vulnerability
├─ Rollback plan: Required (may have issues)
└─ Approval: Expedited (CTO approval only)

Important Security Patch
├─ Severity: Medium (known vulnerability)
├─ Urgency: Monthly (within 30 days)
├─ Example: Regular Windows/Linux patches
├─ Rollback plan: Tested before deployment
└─ Approval: Change management process

Minor/Compatibility Update
├─ Severity: Low (bug fixes, performance)
├─ Urgency: Quarterly (within 90 days)
├─ Example: Optimization improvements
├─ Rollback plan: Optional
└─ Approval: Operations team

PATCH DEPLOYMENT TIMELINE
──────────────────────────

Week 1: Assessment Phase
├─ Day 1: Vulnerability announced
├─ Day 2: Severity assessment
├─ Day 3: Impact analysis
│  ├─ How many systems affected?
│  ├─ What applications running?
│  └─ What's the risk if not patched?
└─ Decision: Approve for deployment?

Week 2: Testing Phase
├─ Dev Environment: Apply patch, test
├─ QA Environment: Full testing (1-2 days)
│  ├─ Functional testing: "Does app work?"
│  ├─ Performance testing: "Is it faster/slower?"
│  ├─ Security testing: "Did patch break anything?"
│  └─ Sign-off: QA lead approval
└─ Decision: Ready for production?

Week 3-4: Phased Rollout
├─ Phase 1: Dev systems only (Day 21)
│  ├─ Count: 2-3 systems
│  ├─ Monitoring: 24 hours for issues
│  └─ Decision: Proceed to Phase 2?
│
├─ Phase 2: Test/QA systems (Day 22-24)
│  ├─ Count: 5-10 systems
│  ├─ Monitoring: 3 days for issues
│  └─ Decision: Proceed to Phase 3?
│
├─ Phase 3: Production tier 1 (Day 25-28)
│  ├─ Count: 20-30% of production
│  ├─ Monitoring: 48 hours for issues
│  └─ Decision: Proceed to Phase 4?
│
└─ Phase 4: Production tier 2 (Day 29-30)
   ├─ Count: Remaining production systems
   ├─ Monitoring: 72 hours post-deployment
   └─ Status: Fully deployed

Example Timeline (Critical Patch):
────────────────────────────────────
Jan 10 (Day 0): Vulnerability announced
│              Risk: Data breach possible
│              System: Azure Virtual Machines
│
Jan 11 (Day 1): Severity: CRITICAL
│              Decision: Expedited deployment
│              Plan: 48-hour deployment
│
Jan 12 (Day 2): Testing complete
│              Status: Approved for production
│
Jan 13 (Day 3): Production deployment starts
│              Phase 1 (Tier 1): 30% of VMs
│              Monitoring: Active
│
Jan 14 (Day 4): Phase 2 (Tier 2): Remaining 70%
│              Monitoring: 24/7 on-call
│
Jan 15 (Day 5): Patch verification complete
│              Status: 100% of systems patched
│              Risk: MITIGATED

AUTOMATED PATCHING
───────────────────

Azure Update Management (fully automated):

┌──────────────────┐
│ Vulnerability    │
│ Announced        │
│ (Microsoft)      │
└────────┬─────────┘
         │
         ├─→ [Auto-assess impact]
         │
         ├─→ [Create patch group]
         │
         ├─→ [Run pre-patch tests]
         │
         ├─→ [Schedule patch window]
         │    ├─ Saturday 2 AM UTC
         │    ├─ 4-hour window
         │    └─ Maintenance schedule
         │
         ├─→ [Deploy patches]
         │    ├─ Batch 1: 10% systems
         │    ├─ Wait 1 hour
         │    ├─ Batch 2: 50% systems
         │    ├─ Wait 2 hours
         │    └─ Batch 3: Remaining
         │
         ├─→ [Monitor results]
         │    ├─ Success rate: 99%+
         │    ├─ Failures: Auto-rollback
         │    └─ Alerts: If issues detected
         │
         └─→ [Report completion]
              └─ Dashboard: Patch status

COMPLIANCE EVIDENCE
──────────────────

Patch Compliance Report:

┌────────────────────────────────────┐
│ Q4 2025 Patch Management Report    │
│                                    │
│ CRITICAL PATCHES:                  │
│ ├─ Released: 3 patches              │
│ ├─ Applied within 48h: 3 ✓         │
│ ├─ Compliance: 100% ✓              │
│ └─ Status: PASS (exceeds FedRAMP)  │
│                                    │
│ IMPORTANT PATCHES:                 │
│ ├─ Released: 45 patches            │
│ ├─ Applied within 30d: 45 ✓        │
│ ├─ Compliance: 100% ✓              │
│ └─ Status: PASS (compliant)        │
│                                    │
│ PATCH FAILURES:                    │
│ ├─ Total: 0 (100% success rate)    │
│ ├─ Rolled back: 0                  │
│ └─ Status: EXCELLENT ✓             │
│                                    │
│ COMPLIANCE VERDICT: ✓ PASS         │
│ Organization exceeds patch policy  │
│ requirements for FedRAMP/GDPR      │
└────────────────────────────────────┘
```

---

## Incident Response

### Incident Response Plan

```text
INCIDENT RESPONSE PLAYBOOK
═════════════════════════════════════════════════════════════

PHASES: Preparation → Detection → Analysis → Containment → Recovery → Lessons

PHASE 1: PREPARATION (Before Incident)
──────────────────────────────────────────────────────────

Team Assembly:
├─ Incident Commander: Coordinates response
├─ Security Lead: Technical investigation
├─ Network Admin: Network analysis
├─ Database Admin: Data/backup recovery
├─ Communications Lead: External notifications
└─ Legal/Compliance: Regulatory requirements

Tools & Systems:
├─ SIEM: Azure Sentinel (log analysis)
├─ Forensics: Isolated systems for investigation
├─ Backups: Clean backups for recovery
├─ Runbooks: Documented procedures
└─ Contact list: Team members, stakeholders

Playbook Development:
├─ Ransomware response playbook
├─ Insider threat playbook
├─ DDoS attack playbook
├─ Data breach playbook
└─ Application outage playbook

PHASE 2: DETECTION & ALERTING
──────────────────────────────────────────────────────────

Alert Triggers:

Alert 1: Unusual Login Activity
├─ Trigger: 50+ failed logins in 5 minutes
├─ Source: Azure AD logs
├─ Response: Automatic account lockout + alert
└─ Severity: Medium

Alert 2: Data Exfiltration
├─ Trigger: > 100 GB data transferred to external IP
├─ Source: Network monitoring
├─ Response: Immediate alert + network blocking
└─ Severity: Critical

Alert 3: Ransomware Pattern
├─ Trigger: Rapid mass file encryption detected
├─ Source: File integrity monitoring
├─ Response: Isolate system + freeze backups
└─ Severity: Critical

Alert 4: Suspicious Process
├─ Trigger: Known malware signature detected
├─ Source: Endpoint security
├─ Response: Quarantine file + alert
└─ Severity: High

PHASE 3: INITIAL RESPONSE (First 30 Minutes)
──────────────────────────────────────────────────────────

Minute 0-5: Receive & Verify Alert
├─ Alert received: "Ransomware detected on 3 servers"
├─ Verify: Is this real? (Check alert source)
├─ Decision: Declare incident (YES)
└─ Action: Page incident commander (on-call rotation)

Minute 5-10: Activate Response Team
├─ IC (Incident Commander) activated
├─ Calls emergency line: "Security incident, all-hands"
├─ Team status: 8 people online within 5 minutes
└─ Communication: Video conference + chat

Minute 10-15: Initial Containment
├─ Action 1: Isolate affected systems (network)
│  ├─ Remove from network (emergency disconnect)
│  └─ Status: 3 infected servers isolated
│
├─ Action 2: Disable compromised accounts
│  ├─ Revoke: All active sessions
│  ├─ Disable: User account access
│  └─ Force: Password reset required to recover
│
├─ Action 3: Activate incident command center
│  ├─ War room: Virtual meeting active
│  ├─ Status: "Incident IN PROGRESS"
│  └─ Logs: Recording all decisions and actions
│
└─ Action 4: Preserve evidence
   ├─ Snapshots: Take memory dump of affected servers
   ├─ Logs: Copy all logs to safe location
   └─ Chain of custody: Document everything

Minute 15-30: Assess Scope
├─ Questions:
│  ├─ How many systems affected? (Answer: 3 servers)
│  ├─ How long has this been running? (Answer: 2 hours)
│  ├─ What data was accessed? (Answer: Customer database)
│  ├─ Has data left the organization? (Answer: Unknown, investigating)
│  └─ Are other systems compromised? (Answer: Scanning now)
│
└─ Findings: Ransomware active for 2+ hours
   └─ Scope: Growing (potential for more systems)

PHASE 4: INVESTIGATION (Hours 1-8)
──────────────────────────────────────────────────────────

Deep Forensic Analysis:

Step 1: Determine Entry Point
├─ Question: How did ransomware get in?
├─ Analysis:
│  ├─ Network logs: Check firewall rules for unusual access
│  ├─ VPN logs: Check for unauthorized access
│  ├─ Email logs: Check for phishing email attachment
│  └─ Result: Phishing email from external threat actor
│
└─ Finding: Employee clicked malicious link in email

Step 2: Determine Attacker Capabilities
├─ Question: What can the attacker do?
├─ Analysis:
│  ├─ Privilege analysis: What permissions did they gain?
│  ├─ Lateral movement: Did they move to other systems?
│  ├─ Data access: What data can they access?
│  └─ Result: Full domain admin privileges (bad)
│
└─ Finding: Attacker has high-privilege access

Step 3: Determine Impact
├─ Question: What happened?
├─ Analysis:
│  ├─ Files encrypted: 1.2 TB of customer data encrypted
│  ├─ Systems affected: 3 servers (100% compromised)
│  ├─ Data exfiltration: Logs show 50 GB transferred out
│  └─ Duration: Active for 2 hours before detection
│
└─ Finding: Data breach occurred (needs notification)

PHASE 5: RECOVERY (Hours 8-24)
───────────────────────────────────────────────────────────

Restoration from Clean Backup:

Step 1: Verify Clean Backup
├─ Find: Last clean backup (before infection)
├─ Date: June 20, 2025 (3 days old)
├─ Verify: Is this backup actually clean?
│  └─ Check: Scan backup files for malware (negative)
└─ Decision: Approve restoration

Step 2: Restore Systems
├─ Environment: Isolated test lab (not production)
├─ Process:
│  ├─ Restore from backup
│  ├─ Apply pending patches
│  ├─ Update antivirus definitions
│  ├─ Verify system functionality
│  └─ Security re-scan (confirm clean)
│
└─ Status: Restored system verified clean

Step 3: Restore to Production
├─ Cutover plan: Fail over to restored system
├─ Timing: Sunday 2 AM (low-traffic window)
├─ Rollback plan: Can rollback if issues
└─ Execution:
   ├─ Hour 1: Shut down infected system
   ├─ Hour 2: Start restored system
   ├─ Hour 3: Point applications to restored system
   ├─ Hour 4: Verify data integrity
   └─ Hour 5: Return to normal operations

Step 4: Data Recovery
├─ Restore: Missing data from backup (3 days lost)
├─ Notify: Customers "Data may be 3 days old"
├─ Reconcile: Compare with external sources
└─ Update: Reload any missing transactions

PHASE 6: LESSONS LEARNED (Week 1)
───────────────────────────────────────────────────────────

Post-Incident Review:

Question 1: What happened?
Answer: Phishing email led to ransomware installation
└─ Root cause: Employee clicked suspicious link

Question 2: Why did we miss it?
Answer: Endpoint detection wasn't catching this variant
└─ Gap: Antivirus definitions outdated by 1 week

Question 3: Why was the blast radius so large?
Answer: User account had domain admin privileges (too much)
└─ Gap: Least privilege not enforced

Question 4: What will we do differently?
Actions:
├─ Email security: Deploy email banner for external senders
├─ Training: Mandatory phishing awareness training
├─ Endpoint: Update antivirus + enable behavioral detection
├─ Least privilege: Remove unnecessary admin rights
├─ Detection: Improve ransomware pattern detection
└─ Backup: Ensure offline backup exists

Estimated Preventative Impact:
├─ Email banner: Would have prevented ~40% of phishing
├─ Training: Additional ~20% reduction
├─ Least privilege: Limited blast radius to 1 system instead of 3
├─ Detection: Would have caught this attack 30 minutes sooner
└─ Result: Incident severity reduced by ~70%

COMPLIANCE NOTIFICATION (72-Hour Requirement)
──────────────────────────────────────────────

Data Breach Notification Email (sent to customers):

```

SUBJECT: Important Notice - Your Data May Have Been Affected

Dear Valued Customer,

We are writing to inform you of a security incident that may have
affected your data stored with us.

WHAT HAPPENED:
On June 23, 2025, we detected unauthorized access to our systems
caused by ransomware. An attacker gained access and may have accessed
the following data:
├─ Your account information
├─ Transaction history (30 days)
└─ Partial contact information

WHAT WE'RE DOING:
├─ We have contained the incident and isolated affected systems
├─ We have restored from clean backups and verified no active threats
├─ We have enhanced our security controls to prevent recurrence
├─ We are offering 2 years of complimentary credit monitoring
└─ We have notified law enforcement and regulators

WHAT YOU SHOULD DO:
├─ Change your password (especially if used elsewhere)
├─ Monitor your accounts for unauthorized activity
├─ Enable 2FA/MFA on your account
├─ Contact us with any questions: <security@company.com>
└─ More details: <https://security.company.com/breach-2025>

We sincerely apologize for this incident and appreciate your trust.

Sincerely,
The Security Team

```text
```

---

## Related Topics

- **Main Page:** [Compliance & Security Patterns](./compliance-security-patterns.md)
- **GDPR:** [GDPR Implementation & Data Residency](./gdpr-implementation.md)
- **FedRAMP:** [FedRAMP Compliance Path](./fedramp-compliance.md)
- **Encryption:** [Encryption & Key Management](./encryption-key-management.md)
- **Assessment:** [Compliance & Security Knowledge Check](./compliance-knowledge-check.md)

---

_Last Updated: October 21, 2025_
