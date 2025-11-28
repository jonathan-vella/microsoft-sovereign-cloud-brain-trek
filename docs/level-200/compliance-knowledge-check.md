---
layout: default
title: Compliance & Security Knowledge Check
parent: Compliance & Security Patterns
nav_order: 5.3
---

# Compliance & Security Patterns - Assessment Quiz

{: .no_toc }

Test your understanding of compliance frameworks, security patterns, encryption, and hardening techniques for Microsoft Sovereign Cloud deployments.

---

## Quiz Instructions

- **Total Questions:** 15
- **Passing Score:** 70% (11 of 15 correct)
- **Time Estimate:** 25-30 minutes
- **Format:** Scenario-based multiple choice (A/B/C/D)
- **Note:** Focus on real-world compliance and security scenarios for sovereign cloud deployments.

---

## Questions

### Question 1: GDPR Data Residency

**Scenario:** A German healthcare organization processes patient medical records under GDPR. Where must their data be stored to comply with the EU data boundary requirement?

A) Azure Public Cloud (US East region)  
B) Azure EU Data Boundary (West Europe or North Europe)  
C) Azure Local deployed on-premises in Germany  
D) Both B and C are compliant  

**Correct Answer: D**

**Explanation:**
GDPR compliance allows for multiple architectures:

- **Option B (EU Data Boundary)**: Azure West Europe or North Europe keeps data within EU, satisfying GDPR data residency. Microsoft handles all operations.
- **Option C (Azure Local)**: Physical on-premises deployment in Germany provides maximum sovereignty and meets strictest data residency requirements, especially for German data protection laws.

Both satisfy GDPR's data residency requirement through different operational models. German healthcare organizations often choose Azure Local for maximum control and sovereignty, but EU regions are also compliant. Organizations should consider their specific risk tolerance and operational capabilities when choosing between these options.

**Business Context:** Healthcare organizations often face the choice between operational simplicity (cloud) and maximum data sovereignty (on-premises). Azure Local addresses concerns about data leaving the country while maintaining Microsoft's managed services.

---

### Question 2: Data Subject Rights

**Scenario:** A customer requests their personal data under the GDPR "right to access." Your organization must provide this data within a specific timeframe. What is the legal deadline?

A) 7 days  
B) 14 days  
C) 30 days  
D) 90 days  

**Correct Answer: C**

**Explanation:**
GDPR Article 12 specifies a **30-day deadline** for responding to data subject access requests. This deadline starts when the request is received.

**Timeline Breakdown:**

- Days 1-5: Locate all personal data across systems
- Days 6-10: Compile and format data
- Days 11-20: Verify data accuracy and organize by type
- Days 21-28: Package for secure delivery
- Days 29-30: Deliver to data subject

**Best Practice:** Organizations typically respond within 7-10 days to exceed regulatory requirements and build customer trust.

**Non-Compliance Risk:** Failing to meet the 30-day deadline can result in fines up to €10 million or 2% of global annual revenue.

---

### Question 3: FedRAMP Authorization Levels

**Scenario:** A U.S. federal agency needs to store PII (personally identifiable information) in Azure. Which FedRAMP authorization level is typically required?

A) Level 1 (Low Impact)  
B) Level 2 (Moderate Impact)  
C) Level 3 (High Impact)  
D) Government Secret only  

**Correct Answer: B**

**Explanation:**
PII is classified as **Moderate Impact** data under NIST 800-53. FedRAMP Level 2 (Moderate Authorization) is the appropriate authorization level because:

**Moderate Impact Definition:**

- Significant harm if confidentiality breached
- Examples: Citizen PII, financial data, healthcare information
- Controls required: ~110 baseline controls
- Continuous monitoring: Monthly
- Authorization time: 6-12 months
- Cost: $300K-750K

**Why not Level 1?** Level 1 is only for public or unclassified low-sensitivity data.

**Why not Level 3?** Level 3 is reserved for classified (Secret/Top Secret) data and has much stricter requirements, higher cost, and longer authorization timeline.

**Business Impact:** Choosing the correct FedRAMP level affects authorization timeline, cost, and operational requirements. Overestimating (Level 3) wastes budget; underestimating (Level 1) creates compliance risk.

---

### Question 4: FedRAMP Continuous Monitoring

**Scenario:** Your organization maintains FedRAMP Moderate authorization. What is the minimum monitoring frequency required to maintain compliance?

A) Annual  
B) Quarterly  
C) Monthly  
D) Real-time/Daily  

**Correct Answer: C**

**Explanation:**
FedRAMP Moderate authorization requires **monthly continuous monitoring** at minimum:

**Monthly Requirements:**

- Review security logs
- Verify patch status (all systems)
- Assess access control compliance
- Identify and track incidents
- Update control status
- Prepare compliance report

**Quarterly Requirements (Additional):**

- Deep-dive control assessment
- Risk assessment update
- Remediation tracking

**Annual Requirements (Additional):**

- Comprehensive reassessment
- Vulnerability scanning (external)
- Penetration testing

**Increased Monitoring for Level 3 (High):** Real-time/daily monitoring with automated alerts.

**Compliance Monitoring Failure Impact:** Failure to maintain continuous monitoring monitoring can result in loss of FedRAMP authorization, which would immediately disqualify the system from government use.

---

### Question 5: GDPR Encryption Requirements

**Scenario:** Under GDPR, if a data breach occurs but personal data was encrypted with AES-256, what is the likely outcome?

A) Notification to authorities is still required (encryption doesn't eliminate notification)  
B) No notification required (encryption provides absolute protection)  
C) Notification only required if encryption keys were compromised  
D) Notification timeline extends to 90 days  

**Correct Answer: A**

**Explanation:**
Under GDPR Article 32, encryption is a **recommended technical measure** for data protection, but it does NOT eliminate breach notification requirements.

**Encryption Helps:**

- Reduces risk assessment likelihood (data probably unreadable)
- May reduce penalties (demonstrates security effort)
- Shows "appropriate safeguards" defense

**But Notification May Still Be Required If:**

- Encryption keys were also compromised
- Attack demonstrates other security flaws
- Regulatory authority requests notification
- Customer notification would build trust

**Key GDPR Principle:** Encryption is **one control** in a layered defense, not a substitute for incident response procedures.

**Real Example:** EU regulators have noted that encryption alone doesn't guarantee exemption from breach notification, especially if combined with other attacks or if the breach indicates systematic security failures.

---

### Question 6: Encryption at Rest vs. in Transit

**Scenario:** You have a database with AES-256 encryption at rest. A hacker intercepts database traffic during replication. What protection prevents the hacker from reading the replicated data?

A) At-rest encryption (protects storage)  
B) In-transit encryption (TLS 1.3)  
C) Key Vault management  
D) RBAC permissions  

**Correct Answer: B**

**Explanation:**
Different encryption protects at different points:

**At-Rest Encryption (AES-256):**

- Protects: Data stored in databases, blobs, disks
- Prevents: Reading files on storage directly
- Fails against: Intercepting network traffic

**In-Transit Encryption (TLS 1.3):**

- Protects: Data moving between systems
- Prevents: Intercepting and reading replication traffic
- Protects: API calls, database connections, backups

**Layered Approach:**

```text
Scenario: Database Replication
┌─────────────────────┐
│ Source Database     │
│ (AES-256 at rest)   │ ← At-rest encryption
└─────────┬───────────┘
          │
    ┌─────▼──────┐
    │ TLS 1.3    │  ← In-transit encryption
    │ Encrypted  │
    │ Tunnel     │
    └─────┬──────┘
          │
┌─────────▼───────────┐
│ Target Database     │
│ (AES-256 at rest)   │ ← At-rest encryption
└─────────────────────┘
```

**Network Interception Scenario:** Without TLS 1.3 in-transit encryption, hacker intercepts the replication data stream (encrypted at-rest key is useless for transmitted data).

---

### Question 7: Azure Key Vault Disaster Recovery

**Scenario:** Your primary Azure Key Vault in West Europe becomes unavailable. You need to decrypt customer data urgently. What is the minimum RTO (Recovery Time Objective) with proper geo-replication setup?

A) 24 hours  
B) 4 hours  
C) < 5 minutes  
D) Varies; depends on backup strategy  

**Correct Answer: C**

**Explanation:**
With **proper geo-replication of Azure Key Vault**, recovery is nearly instantaneous:

**Geo-Replicated Architecture:**

- Primary: West Europe (active read/write)
- Secondary: North Europe (read-only replica, real-time sync)
- Automatic failover: When primary unavailable
- DNS switching: Automatic redirection to secondary
- RTO: < 5 minutes typical

**Process:**

1. Primary region goes down
2. Azure detects unavailability (automated)
3. Secondary vault becomes primary (auto-promotion)
4. DNS updated to point to new primary (seconds)
5. Applications retry and connect to secondary
6. Total downtime: 2-5 minutes

**Why Not 24 Hours?** That would be without proper disaster recovery; this is unacceptable for encryption keys. Organizations must have active/active or active/passive with automatic failover.

**Compliance Requirement:** FedRAMP requires RTO < 4 hours for critical systems; RTO < 5 minutes exceeds this requirement.

**Cost Trade-off:** Geo-replication adds ~50% to Key Vault costs but provides near-zero downtime for keys.

---

### Question 8: Least Privilege Access Control

**Scenario:** An IT administrator needs to temporarily manage VM scaling during a high-traffic event (1-day event). What is the best practice for granting access?

A) Permanent Contributor role (convenient, not revoked)  
B) Temporary elevated access via PIM (Privileged Identity Management) with time limit  
C) Owner role for the duration of event  
D) Shared admin account (multiple admins use same credentials)  

**Correct Answer: B**

**Explanation:**
**Temporary Privileged Access Management (PIM)** is the best practice:

**PIM Features:**

- Temporary elevation: Access automatically expires
- Just-in-time (JIT): Access granted only when needed
- Approval workflow: Requires manager/security approval
- Audit trail: Every access logged
- Accountability: Time-limited responsibility

**Timeline Example:**

```text
Event: High traffic expected Oct 15, 2 PM - 11 PM UTC

Request: Oct 14, 10 AM
├─ Admin requests: "VM Contributor role for Oct 15, 2 PM - 11 PM"
├─ Duration: 9 hours (exactly what's needed)
├─ Manager approves: Within 15 minutes
└─ Access granted: Oct 15, 2 PM

Automatic Cleanup:
└─ Oct 15, 11 PM: Access automatically revoked
   └─ No manual follow-up required
   └─ Compliant with least privilege principle
```

**Why Not Other Options?**

- A) Permanent role violates least privilege (kept too long)
- C) Owner role is excessive (gives too many permissions)
- D) Shared account violates audit requirements (no accountability)

**Compliance Impact:** Temporary, approved, audited access demonstrates GDPR and FedRAMP compliance for access control.

---

### Question 9: Network Segmentation

**Scenario:** You're designing network segmentation for a healthcare organization. A web server is compromised. How does segmentation minimize the blast radius?

A) Prevents web server from accessing databases (firewall between tiers)  
B) Prevents internet traffic from reaching internal servers  
C) Requires additional authentication for each tier  
D) All of the above  

**Correct Answer: D**

**Explanation:**
Network segmentation uses **multiple controls** to minimize blast radius:

**Segmentation Architecture:**

```text
Internet (Attacker)
    │
    ├─ DMZ Firewall (Layer 1)
    │  └─ Blocks non-HTTPS traffic
    │
Web Tier (Compromised)
    │
    ├─ Internal Firewall (Layer 2)
    │  └─ Blocks web-to-database traffic on port 22, 3389
    │
App Tier (Protected)
    │
    ├─ Data Firewall (Layer 3)
    │  └─ Blocks app-to-database access without MFA
    │
Data Tier (Highly Protected)
```

**Why Option A Works:**

- Firewall rules: "Port 1433 (SQL) blocked from web tier"
- Compromised web server cannot query databases
- Prevents data exfiltration

**Why Option B Works:**

- DMZ prevents internet from reaching internal systems
- Compromised web server cannot reach internal services directly

**Why Option C Works:**

- MFA required between tiers
- Even if firewall bypassed, additional authentication required
- Time-limited session tokens

**Combined Effect:** Blast radius reduced from "entire network" to "single web server only"

**Compliance Benefit:** Network segmentation demonstrates defense-in-depth, reducing penalty severity if breach occurs.

---

### Question 10: Patch Management Timeline

**Scenario:** A critical zero-day security vulnerability is announced affecting your Azure SQL databases. Under FedRAMP requirements, what is the maximum allowed time to apply this patch?

A) 24 hours  
B) 48 hours  
C) 7 days  
D) 30 days  

**Correct Answer: B**

**Explanation:**
FedRAMP requires **critical security patches within 24-48 hours**:

**FedRAMP Patch Timeline:**

- Critical (0-day): 24-48 hours maximum
- Important: 30 days maximum
- Minor: 90 days maximum

**Critical Patch Example:**

```text
Day 0: Vulnerability announced
├─ Severity: CVSS 9.8 (critical)
├─ Impact: Affects Azure SQL Databases
└─ Action: Declare emergency

Day 1: Assessment & Deployment Start
├─ Hour 0-6: Impact assessment
├─ Hour 6-12: Test in QA environment
├─ Hour 12-24: Begin production deployment
└─ Action: Phased rollout (30%, 70% batches)

Day 2: Completion
├─ Hour 24-48: Complete remaining systems
├─ Hour 48: Verification that all systems patched
└─ Status: Compliant (within 48-hour deadline)
```

**Why So Fast?** Critical vulnerabilities can lead to data breach, which is much worse than brief downtime from patching.

**Realistic Challenge:** 48-hour timeline is aggressive and requires:

- Pre-positioned patches
- Tested procedures
- On-call team availability
- Pre-approved maintenance windows
- Automated deployment where possible

**Compliance Evidence:** Organizations must maintain patch deployment logs showing all critical patches applied within 48-hour window.

---

### Question 11: Encryption Algorithm Selection

**Scenario:** You need to select an encryption algorithm for encrypting sensitive healthcare data at rest in Azure Storage. Azure supports multiple algorithms. Which is the correct choice for GDPR/FedRAMP compliance?

A) AES-128  
B) AES-256  
C) MD5  
D) SHA-256  

**Correct Answer: B**

**Explanation:**
**AES-256** is the required standard for GDPR/FedRAMP compliance:

**Why AES-256?**

- NIST approved: FIPS 197 standard
- Key size: 256-bit (2^256 possible keys)
- Security: Unbreakable with current technology
- Military-grade: NSA Suite B approved
- Regulatory: Required by GDPR, FedRAMP, HIPAA, DoD

**Why Not Other Options?**

**AES-128 (Option A):**

- Only 128-bit key size
- Technically secure but below standards
- FedRAMP/GDPR explicitly require AES-256
- Acceptable for some use cases, not healthcare

**MD5 (Option C):**

- Hash algorithm, NOT encryption
- Cannot decrypt (one-way transformation)
- Cryptographically broken (attacks published)
- Should NEVER be used for data encryption

**SHA-256 (Option D):**

- Hash algorithm, NOT encryption
- Used for integrity checking, not data protection
- One-way function (cannot reverse)
- Complements encryption but doesn't replace it

**Correct Use of Each:**

```text
┌─────────────────────────────────────┐
│ Data Protection Strategy            │
├─────────────────────────────────────┤
│ Encryption: AES-256 (symmetric)    │
│ (Protects confidentiality)          │
│                                     │
│ + Integrity: SHA-256 (hash)        │
│   (Prevents tampering)              │
│                                     │
│ + Key Management: RSA-2048          │
│   (Protects encryption keys)        │
│                                     │
│ = Complete Data Protection          │
└─────────────────────────────────────┘
```

---

### Question 12: Incident Response Timeline

**Scenario:** Your organization detects a data breach affecting 5,000 customer records. Under GDPR, when must you notify the Data Protection Authority (DPA)?

A) Immediately (within 1 hour)  
B) Within 24 hours  
C) Within 72 hours  
D) Within 30 days  

**Correct Answer: C**

**Explanation:**
GDPR Article 33 requires notification to DPA **within 72 hours** of discovering a breach:

**GDPR Breach Notification Timeline:**

```text
Hour 0: Breach detected
├─ Immediate actions (containment, evidence preservation)
└─ 72-hour clock starts

Hour 24: Initial investigation
├─ Root cause analysis underway
├─ Scope assessment: 5,000 records confirmed
└─ Risk assessment: Determine likelihood of harm

Hour 48-72: DPA notification preparation
├─ Documentation compiled
├─ Breach notification form completed
├─ Legal review completed
└─ Authority contacted

Hour 72: DPA notification sent (DEADLINE)
├─ Detailed breach report submitted
├─ Mitigation actions described
├─ Continues investigation while reporting
└─ Status: Compliant with GDPR

Hour 72+: Affected parties notification
├─ GDPR allows additional time if needed
├─ But customer notification should follow quickly
├─ Transparency builds trust
└─ Longer delays damage reputation
```

**Note on Customer Notification:** GDPR doesn't specify a deadline for notifying affected individuals, but best practice is to notify within 72 hours as well (same as DPA).

**Non-Compliance Penalties:** Failing to notify DPA within 72 hours:

- Tier 1: €10M or 2% of global revenue fine
- Reputational damage
- Regulatory scrutiny

---

### Question 13: Defense-in-Depth Security

**Scenario:** A security incident occurs where a web server is compromised. The organization has implemented defense-in-depth architecture. Which layer would prevent the attacker from accessing the database?

A) Physical security (guards)  
B) Network segmentation & firewall rules  
C) Application-level access control  
D) Data encryption  

**Correct Answer: B**

**Explanation:**
**Network segmentation** is the most effective layer for preventing database access from compromised web server:

**Defense-in-Depth Layers:**

```text
Layer 1: Physical Security
├─ Prevents: Physical theft of servers
├─ Against: This attack? No (server already in data center)
└─ Status: Already compromised (irrelevant for this scenario)

Layer 2: Network Segmentation ✓ STOPS ATTACK
├─ Rule: "Traffic from web tier to database tier blocked"
├─ Result: Database firewalled from web tier
├─ Status: Attacker cannot reach database at network level
└─ Technical: NSG rule denies port 1433/5432 traffic

Layer 3: Application Access Control
├─ Adds: Extra authentication layer
├─ Helps: But network layer already blocked traffic
└─ Status: Defense-in-depth (layers overlap)

Layer 4: Data Encryption
├─ Protects: Even if data accessed, unreadable
├─ Helps: But database never accessed
└─ Status: Defense-in-depth (layers overlap)
```

**Why Network Segmentation is First Line:**
Network segmentation blocks attack at the **network layer** before it can reach the application layer, data layer, or encryption.

**Why Other Layers Matter:**
If network segmentation failed (misconfigured rule), then:

- Application access control would require additional authentication
- Data encryption would protect even if database accessed
- Multiple failures needed before data compromised

**Compliance Benefit:** Demonstrating network segmentation shows risk management aligned with defense-in-depth principles, reducing FedRAMP/GDPR compliance risks.

---

### Question 14: Key Rotation Compliance

**Scenario:** Your organization has an encryption key protecting customer data. The compliance policy requires key rotation every 90 days. The last rotation was on August 1. Today is November 1. What is your status?

A) Compliant (within policy)  
B) Non-compliant (overdue by 2 days)  
C) Compliant (just within deadline)  
D) Non-compliant (severely overdue)  

**Correct Answer: B**

**Explanation:**
**Key age calculation:**

- Last rotation: August 1
- Today: November 1
- Time elapsed: 92 days
- Policy requirement: 90 days maximum
- Status: 2 days overdue → Non-compliant

**Timeline:**

```text
Aug 1: Key rotation performed
├─ Day 0: New key deployed
├─ Day 45: Check halfway point
├─ Day 90: Rotation policy deadline (Oct 31)
│  ├─ Status if rotated: ✓ Compliant
│  ├─ Status if NOT rotated: ✗ Non-compliant
│  └─ Action: Must schedule rotation immediately
│
Nov 1: Today
├─ Days elapsed: 92 days (2 days over deadline)
├─ Status: ✗ Non-compliant
└─ Action: Immediate rotation required + incident documentation

COMPLIANCE EVIDENCE NEEDED:
├─ Document: Why rotation was missed
├─ Approval: Exception approval from CISO/compliance
├─ Plan: Schedule rotation immediately (within 24 hours)
└─ Remediation: Process improvement to prevent recurrence
```

**Audit Finding:** Missing a key rotation deadline by even 2 days can result in:

- Compliance violation notation
- Audit finding for remediation
- Potential fine consideration
- Request for corrective action plan

**Best Practice:** Schedule rotation at 75-80 day mark (before 90-day deadline):

- Provides 10-15 day buffer
- Prevents compliance violation from scheduling delays
- Demonstrates proactive management

---

### Question 15: Zero-Trust Security Model

**Scenario:** Your organization is implementing a zero-trust security architecture for a sovereign cloud deployment. Which principle best describes zero-trust approach?

A) Trust all users on internal network  
B) Verify every access request, assume breach  
C) Trust users after initial login  
D) Security at network perimeter is sufficient  

**Correct Answer: B**

**Explanation:**
**Zero-trust principle:** "Never trust, always verify" - assume every access is potentially malicious and verify every request:

**Zero-Trust vs. Traditional (Perimeter) Security:**

```text
TRADITIONAL APPROACH (Outdated):
└─ "Trust everyone inside firewall"
   ├─ Problem: Assumes network perimeter secure
   ├─ Problem: Once inside, free access
   ├─ Problem: Insider threats undetected
   └─ Result: Large blast radius if perimeter breached

ZERO-TRUST APPROACH (Modern):
└─ "Trust nothing, verify everything"
   ├─ Verify: Identity (MFA required)
   ├─ Verify: Device health (patches current, antivirus active)
   ├─ Verify: Access context (location, time, purpose)
   ├─ Verify: Resource entitlement (has permission?)
   ├─ Verify: Session integrity (continuous monitoring)
   └─ Result: Small blast radius (limited user access only)
```

**Zero-Trust Components:**

```text
Request for Access (e.g., "Access database")
        │
        ├─ Identity: Who are you?
        │  └─ MFA required (password + phone approval)
        │
        ├─ Device: What device?
        │  └─ Must be company laptop, patches current
        │
        ├─ Location: Where are you?
        │  └─ Expected geography (not VPN from hostile country)
        │
        ├─ Context: Why now?
        │  └─ Normal business hours (not 3 AM)
        │
        ├─ Permission: Can you access?
        │  └─ RBAC: Job role permits database access
        │
        └─ Result: ALL verified = GRANT ACCESS
           ANY failed = DENY ACCESS + ALERT
```

**Sovereign Cloud Implementation:**
Zero-trust is essential for sovereign cloud deployments:

- Prevents unauthorized data exfiltration
- Meets GDPR/FedRAMP requirements for access control
- Detects insider threats early
- Complies with defense-in-depth principles

**Benefits for Compliance:**

- GDPR: Demonstrates access control security (Article 32)
- FedRAMP: Meets IA (identification & authentication) controls
- HIPAA: Meets minimum necessary access principle
- PCI-DSS: Enforces least privilege principle

---

## Answer Key Summary

| Q | Answer | Topic |
|---|--------|-------|
| 1 | D | GDPR data residency (EU boundary vs. local) |
| 2 | C | Data subject access rights (30-day deadline) |
| 3 | B | FedRAMP authorization for PII (Level 2) |
| 4 | C | FedRAMP continuous monitoring (monthly) |
| 5 | A | GDPR encryption & breach notification |
| 6 | B | Encryption in-transit protection (TLS) |
| 7 | C | Key Vault RTO with geo-replication (<5 min) |
| 8 | B | Least privilege access (PIM temporary access) |
| 9 | D | Network segmentation (all layers combined) |
| 10 | B | Critical patch timeline (24-48 hours) |
| 11 | B | Encryption algorithm selection (AES-256) |
| 12 | C | GDPR breach notification to DPA (72 hours) |
| 13 | B | Defense-in-depth against database access |
| 14 | B | Key rotation compliance (92 days overdue) |
| 15 | B | Zero-trust security principle |

---

## Scoring Guide

**Calculate your score:**

- Count the number of correct answers
- Divide by 15 and multiply by 100 for percentage

**Score Interpretation:**

**14-15 correct (93-100%):** 🏆 **Excellent - Compliance Expert**

- You have mastery-level understanding of compliance and security patterns
- Ready to lead compliance initiatives and security audits
- Qualified for security architect or compliance officer roles
- Consider pursuing security certifications (CISSP, CISM, Azure Security Engineer)

**11-13 correct (73-87%):** ✅ **Good - Competent**

- You have solid understanding of compliance frameworks
- Ready for most compliance implementation projects
- Review areas where you missed questions
- Focus on specific compliance deadlines and requirements

**8-10 correct (53-67%):** ⚠️ **Fair - Needs Review**

- You have foundational understanding but gaps exist
- Additional study needed before compliance implementation
- Review GDPR timelines, FedRAMP requirements, and encryption standards
- Practice with scenario-based questions
- Retake quiz after comprehensive review

**Below 8 correct (<53%):** ❌ **Needs Significant Review**

- Significant knowledge gaps in compliance and security
- Thoroughly review all module content
- Focus on fundamentals: GDPR, FedRAMP, encryption, zero-trust
- Consider starting with compliance framework documentation
- Seek additional training resources
- Retake quiz only after thorough study

---

## Study Recommendations by Topic

**If you missed questions on GDPR (Q1, Q2, Q5, Q12):**

- Review [GDPR Implementation](gdpr-implementation)
- Master key timelines: 30-day access, 72-hour breach notification
- Study EU Data Boundary requirements
- Focus on data subject rights and breach notification procedures

**If you missed questions on FedRAMP (Q3, Q4):**

- Review [FedRAMP Compliance](fedramp-compliance)
- Study authorization levels (Low, Moderate, High)
- Focus on continuous monitoring requirements
- Review control baselines (NIST 800-53)

**If you missed questions on Encryption (Q5, Q6, Q7, Q11):**

- Review [Encryption & Key Management](encryption-key-management)
- Study encryption standards: AES-256 (at-rest), TLS 1.3 (in-transit)
- Focus on Azure Key Vault architecture and geo-replication
- Review key rotation policies

**If you missed questions on Security Patterns (Q8, Q9, Q13, Q15):**

- Review [Compliance & Security Patterns](compliance-security-patterns)
- Study defense-in-depth architecture
- Focus on least privilege and zero-trust principles
- Review network segmentation strategies

**If you missed questions on Operations (Q10, Q14):**

- Review security operations best practices
- Study patch management timelines for critical vulnerabilities
- Focus on key rotation compliance and remediation

---

## Next Steps

**After completing this assessment:**

1. **✅ Celebrate your achievement!** You've mastered compliance and security patterns.

2. **📚 Continue learning:**
   - Complete other Level 200 modules
   - Explore Level 300 advanced content

3. **🔗 Review related content:**
   - [Compliance & Security Patterns](compliance-security-patterns)
   - [GDPR Implementation](gdpr-implementation)
   - [FedRAMP Compliance](fedramp-compliance)
   - [Encryption & Key Management](encryption-key-management)

4. **🌐 Explore external resources:**
   - [GDPR Official Text](https://gdpr-info.eu/)
   - [FedRAMP Documentation](https://www.fedramp.gov/)
   - [NIST 800-53 Controls](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
   - [Azure Security Documentation](https://learn.microsoft.com/azure/security/)
   - [Azure Compliance Documentation](https://learn.microsoft.com/azure/compliance/)

5. **💡 Consider hands-on practice:**
   - Implement GDPR-compliant data processing
   - Configure Azure Policy for compliance
   - Set up Azure Key Vault with geo-replication
   - Practice zero-trust architecture design

---

## Master These Key Concepts

**GDPR Timeline Deadlines:**

- 30 days: Data subject access requests
- 72 hours: DPA breach notification
- 3 years: Log retention minimum

**FedRAMP Requirements:**

- Level 2 (Moderate) for PII
- Monthly continuous monitoring
- 110+ baseline controls

**Encryption Standards:**

- At-rest: AES-256
- In-transit: TLS 1.3
- Key management: Azure Key Vault with HSM

**Security Principles:**

- Defense-in-depth: Multiple layers
- Least privilege: Minimum permissions
- Zero-trust: Verify everything
- Network segmentation: Limit blast radius

---

**Quiz Version:** 1.0  
**Last Updated:** October 2025  
**Questions:** 15  
**Passing Score:** 70% (11 of 15 correct)

---

**[← Back to Compliance & Security Patterns](compliance-security-patterns)**
