---
layout: default
title: Industry Verticals - Knowledge Check
parent: Level 300 - Advanced
nav_order: 14
description: "Assessment covering healthcare, financial services, government, and critical infrastructure sovereign patterns"
---

# Industry Verticals - Knowledge Check

{: .no_toc }

Test your expertise in industry-specific sovereign cloud implementations for healthcare, financial services, government, and critical infrastructure sectors.

---

## Quiz Instructions

**Total Questions:** 15  
**Passing Score:** 12/15 (80%)  
**Time Estimate:** 25-35 minutes  
**Format:** Expert-level scenario-based questions

This assessment covers:

- Healthcare sovereignty patterns (HIPAA, PHI protection)
- Financial services compliance (PCI DSS, SOX)
- Government cloud requirements (FedRAMP, ITAR)
- Critical infrastructure protection (NERC CIP, ICS/SCADA)

---

### Question 1: Healthcare — PHI Storage Requirements

A healthcare provider is deploying Azure Local for their sovereign environment. Where should PHI (Protected Health Information) be stored?

A) Azure public cloud with encryption at rest  
B) Azure Local with HIPAA BAA and encryption  
C) Any location with strong passwords  
D) Third-party SaaS with HIPAA compliance badge

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Azure Local with HIPAA BAA provides maximum control:

**Requirements for PHI:**

| Requirement | Azure Local Solution |
|-------------|---------------------|
| Data residency | On-premises storage |
| Access control | Local identity + Entra ID |
| Encryption | BitLocker + network encryption |
| Business Associate Agreement | Microsoft HIPAA BAA covers Azure Local |
| Audit trail | Local logs + Azure Monitor |

**Why Not Others:**

- **A:** Public cloud may not meet organizational residency requirements
- **C:** Passwords alone don't meet HIPAA technical safeguards
- **D:** Third-party SaaS requires careful BAA review and may not provide data control

**Reference:** [Healthcare Sovereign](healthcare-sovereign.md)
</details>

---

### Question 2: Financial Services — PCI DSS Scope

A bank is implementing Edge RAG for customer service automation. The RAG system will access customer account data. What is the PCI DSS consideration?

A) RAG systems are exempt from PCI DSS  
B) Only the vector database is in scope  
C) The entire RAG system (inference, vector DB, knowledge base) is in scope  
D) Only network connections to payment systems are in scope

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: C**

**Explanation:**
Any system that stores, processes, or transmits cardholder data is in scope:

**PCI DSS Scope for RAG:**

| Component | In Scope? | Reason |
|-----------|-----------|--------|
| LLM inference | Yes | Processes queries that may contain card data |
| Vector database | Yes | May store embeddings of card data |
| Knowledge base | Yes | Source documents may contain card data |
| Network path | Yes | Data traverses these connections |

**Scope Reduction Options:**

- Tokenize cardholder data before RAG ingestion
- Use data masking in knowledge base
- Segment RAG system from CDE (Cardholder Data Environment)

**Reference:** [Financial Services](financial-services.md)
</details>

---

### Question 3: Government — FedRAMP Authorization Levels

A government agency needs to deploy a sovereign cloud solution for "Secret" classified data. What is required?

A) FedRAMP Low authorization  
B) FedRAMP Moderate authorization  
C) FedRAMP High authorization  
D) FedRAMP does not apply to classified data

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: D**

**Explanation:**
FedRAMP is for unclassified government data:

**Classification Levels:**

| Data Type | Framework | Environment |
|-----------|-----------|-------------|
| Public | FedRAMP Low | Commercial cloud |
| CUI (Controlled Unclassified) | FedRAMP Moderate/High | Gov cloud |
| Secret | ICD 503 / CNSSI 1253 | Air-gapped/classified cloud |
| Top Secret | ICD 503 / CNSSI 1253 | Air-gapped/classified cloud |

**Classified Data Requirements:**

- Air-gapped infrastructure
- DISA STIG compliance
- Physical security controls
- Personnel clearances
- Azure Government Secret / Top Secret regions

**Reference:** [Government Cloud](government-cloud.md)
</details>

---

### Question 4: Critical Infrastructure — NERC CIP Compliance

An energy utility is deploying Azure Local for operational technology (OT) network monitoring. Which NERC CIP standard is MOST relevant for access control?

A) CIP-002 (BES Cyber System Categorization)  
B) CIP-004 (Personnel & Training)  
C) CIP-005 (Electronic Security Perimeters)  
D) CIP-007 (System Security Management)

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: C**

**Explanation:**
CIP-005 governs Electronic Security Perimeters (ESPs):

**NERC CIP Access Control Standards:**

| Standard | Focus |
|----------|-------|
| **CIP-005** | Network segmentation, ESP boundaries, remote access |
| CIP-004 | Personnel vetting, training requirements |
| CIP-007 | Ports/services, patch management, malware |

**CIP-005 Requirements:**

- Define Electronic Security Perimeter boundaries
- Restrict inbound/outbound traffic
- Monitor and log all access
- Multi-factor authentication for remote access

**Azure Local Alignment:**

- Network isolation between IT/OT
- SDN-based micro-segmentation
- Azure Arc for monitoring (controlled connectivity)

**Reference:** [Critical Infrastructure](critical-infrastructure.md)
</details>

---

### Question 5: Healthcare — Breach Notification

A hospital experiences a ransomware attack affecting 50,000 patient records. What are the HIPAA notification requirements?

A) Notify HHS within 72 hours  
B) Notify HHS within 60 days, individuals within 60 days, media immediately  
C) Notify HHS within 60 days, individuals within 60 days, media within 60 days  
D) No notification required if data was encrypted

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: C**

**Explanation:**
HIPAA Breach Notification Rule requirements:

**Notification Timelines:**

| Recipient | Timeline | Threshold |
|-----------|----------|-----------|
| HHS | Within 60 days of discovery | All breaches |
| Individuals | Within 60 days | All affected individuals |
| Media | Within 60 days | Breaches affecting 500+ in a state |

**50,000 Records:**

- Exceeds 500 threshold → media notification required
- Annual HHS breach report due within 60 days
- Individual notification via mail or substitute notice

**Encryption Exception:**

Encrypted data is a "safe harbor" ONLY if the encryption key was not compromised.

**Reference:** [Healthcare Sovereign](healthcare-sovereign.md)
</details>

---

### Question 6: Financial Services — Cross-Border Data Transfer

A European bank needs to share transaction data with their US subsidiary for fraud analysis. What is required under GDPR?

A) No restrictions — internal company transfers are exempt  
B) Standard Contractual Clauses (SCCs) or Binding Corporate Rules (BCRs)  
C) Data can be transferred if encrypted  
D) Only aggregated data can be transferred

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
GDPR Chapter V governs international data transfers:

**Transfer Mechanisms:**

| Mechanism | Description |
|-----------|-------------|
| **Adequacy decision** | US is not adequate (post-Schrems II) |
| **SCCs** | Contractual clauses approved by EU Commission |
| **BCRs** | Internal corporate rules approved by DPA |
| **Derogations** | Explicit consent, contract necessity, legal claims |

**US Transfers (Post-Schrems II):**

- SCCs required with supplementary measures
- Transfer Impact Assessment recommended
- Consider data localization if transfer risks are high

**Why Not Others:**

- **A:** Intra-company transfers still cross borders
- **C:** Encryption alone doesn't satisfy transfer requirements
- **D:** Personal data transfer restrictions apply regardless of aggregation

**Reference:** [Financial Services](financial-services.md)
</details>

---

### Question 7: Government — ITAR Compliance

A defense contractor is implementing Azure Local for engineering data. The data includes technical specifications for military equipment. What is the PRIMARY compliance concern?

A) FedRAMP authorization  
B) ITAR export control — data must not be accessible to foreign nationals  
C) HIPAA for employee health data  
D) PCI DSS for payment processing

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
ITAR (International Traffic in Arms Regulations) controls defense-related technical data:

**ITAR Requirements:**

| Requirement | Implementation |
|-------------|----------------|
| Access control | US persons only |
| Data location | US territory or approved locations |
| Cloud provider | US-controlled facilities, US persons |
| Encryption | End-to-end with US-controlled keys |

**Azure Local for ITAR:**

- On-premises deployment in US facility
- No foreign national access to systems
- Air-gapped or strictly controlled connectivity
- Customer-managed encryption keys

**Penalties:**

- Civil penalties up to $1M per violation
- Criminal penalties up to $1M and 20 years imprisonment

**Reference:** [Government Cloud](government-cloud.md)
</details>

---

### Question 8: Critical Infrastructure — ICS/SCADA Integration

A water utility wants to connect their SCADA system to Azure for analytics. What is the SAFEST integration pattern?

A) Direct internet connection from SCADA to Azure  
B) VPN tunnel from SCADA network to Azure  
C) Unidirectional data diode from OT to IT, then to Azure  
D) Bidirectional API gateway in DMZ

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: C**

**Explanation:**
Unidirectional data diodes provide physical one-way data flow:

**Data Diode Architecture:**

```text
SCADA Network → [Data Diode] → IT Network → Azure
   (OT Zone)                    (IT Zone)
```

**Why Data Diodes:**

| Benefit | Description |
|---------|-------------|
| Physical isolation | Hardware enforces one-way flow |
| No remote access | OT network cannot receive inbound traffic |
| Regulatory compliance | Meets NERC CIP, IEC 62443 |
| Reduced attack surface | No pathway for remote exploitation |

**Why Not Others:**

- **A:** Direct internet connection exposes SCADA to attacks
- **B:** VPN allows bidirectional traffic
- **D:** Bidirectional gateway creates attack path

**Reference:** [Critical Infrastructure](critical-infrastructure.md)
</details>

---

### Question 9: Healthcare — Edge RAG for Clinical Decision Support

A hospital is implementing Edge RAG for clinical decision support. Which data handling approach is CORRECT?

A) Send patient symptoms to cloud RAG for diagnosis  
B) Use local RAG with de-identified clinical guidelines only  
C) Use local RAG with PHI but no logging  
D) Store all RAG queries in cloud analytics

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Local RAG with de-identified data provides clinical value while maintaining compliance:

**Recommended Architecture:**

| Component | Location | Data Type |
|-----------|----------|-----------|
| LLM inference | Edge (Azure Local) | Processes queries locally |
| Vector database | Edge | De-identified clinical guidelines |
| Knowledge base | Edge | Medical literature, protocols |
| Audit logs | Edge + optional secure cloud | De-identified usage metrics |

**PHI Handling:**

- Queries may contain PHI → process locally
- Knowledge base uses de-identified reference data
- Responses must not persist PHI
- Audit trails required but must protect PHI

**Why Not Others:**

- **A:** Sending PHI to cloud violates data residency
- **C:** Logging is required for HIPAA accountability
- **D:** Query logs containing PHI cannot go to cloud

**Reference:** [Healthcare Sovereign](healthcare-sovereign.md)
</details>

---

### Question 10: Financial Services — Algorithmic Trading Sovereignty

A trading firm needs to ensure their AI trading algorithms and associated data remain within their control. What is the PRIMARY concern?

A) Algorithm IP protection and preventing cloud provider access  
B) Minimizing cloud costs  
C) Maximizing algorithm speed  
D) Using the latest GPU models

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: A**

**Explanation:**
Operational sovereignty for trading algorithms is critical:

**Sovereignty Concerns:**

| Concern | Solution |
|---------|----------|
| Algorithm IP | Customer-managed encryption, confidential computing |
| Data access | No cloud provider access to trading data |
| Audit trail | Complete logging of all data access |
| Key management | Customer Lockbox, HSM-backed keys |

**Azure Local Benefits:**

- On-premises execution — algorithm never leaves facility
- No cloud provider access to running workloads
- Customer controls all encryption keys
- Air-gapped option for maximum isolation

**Regulatory Driver:**

SEC Rule 15c3-5 and MiFID II require firms to maintain control over trading systems.

**Reference:** [Financial Services](financial-services.md)
</details>

---

### Question 11: Government — Continuous Monitoring (ConMon)

For FedRAMP High systems, what is the continuous monitoring requirement?

A) Annual security assessment  
B) Quarterly vulnerability scans  
C) Monthly vulnerability scans, annual penetration test, continuous logging  
D) Real-time monitoring only during business hours

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: C**

**Explanation:**
FedRAMP High requires rigorous continuous monitoring:

**ConMon Requirements:**

| Activity | Frequency |
|----------|-----------|
| Vulnerability scanning | Monthly (High), Quarterly (Moderate) |
| Penetration testing | Annual |
| POA&M updates | Monthly |
| Security control assessment | Annual (subset) |
| Continuous logging | 24/7 with 90-day retention |

**Azure Local Alignment:**

- Microsoft Defender for Cloud for vulnerability scanning
- Azure Monitor for continuous logging
- Regular POA&M reporting to sponsoring agency
- Third-party annual assessments

**Reference:** [Government Cloud](government-cloud.md)
</details>

---

### Question 12: Critical Infrastructure — Incident Response

A power grid operator detects a cyberattack on their control systems. In addition to internal response, who must they notify?

A) Only their insurance provider  
B) CISA (Cybersecurity and Infrastructure Security Agency)  
C) Local law enforcement only  
D) No external notification required

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Critical infrastructure operators must report to CISA:

**Reporting Requirements:**

| Requirement | Source |
|-------------|--------|
| CISA reporting | CIRCIA (Cyber Incident Reporting for Critical Infrastructure Act) |
| NERC reporting | CIP-008 (Incident Reporting) |
| FBI reporting | Recommended for criminal activity |

**CIRCIA Timelines (2024+):**

- Significant cyber incidents: 72 hours
- Ransomware payments: 24 hours
- Supplemental reports as new information emerges

**NERC CIP-008:**

- Report to E-ISAC (Electricity ISAC)
- Document incident and response
- Share lessons learned with sector

**Reference:** [Critical Infrastructure](critical-infrastructure.md)
</details>

---

### Question 13: Healthcare — Telehealth Sovereignty

A hospital is deploying telehealth services using Azure Local. What is the KEY sovereignty consideration for video consultations?

A) Video quality must be 4K  
B) Video streams must be encrypted and not traverse foreign networks  
C) Patients must provide verbal consent  
D) Consultations must be limited to 30 minutes

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Telehealth video contains PHI and must be protected:

**Sovereignty Requirements:**

| Requirement | Implementation |
|-------------|----------------|
| Encryption | End-to-end encryption (TLS 1.3 minimum) |
| Data path | Video must not route through foreign servers |
| Recording storage | On-premises or sovereign cloud storage |
| Access control | Provider and patient authentication |

**Azure Local Telehealth:**

- Local media servers for video processing
- ExpressRoute for reliable connectivity
- Recordings stored on local storage with encryption
- Integration with EHR for documentation

**Why Routing Matters:**

Video streams contain patient images and audio discussing health conditions — both PHI under HIPAA.

**Reference:** [Healthcare Sovereign](healthcare-sovereign.md)
</details>

---

### Question 14: Financial Services — Disaster Recovery

A bank's primary Azure Local deployment is in Frankfurt. For disaster recovery, where should the secondary site be located?

A) US East region for maximum geographic separation  
B) Another EU region (e.g., Netherlands) maintaining data residency  
C) On-premises tape backup only  
D) Cloud-based backup in any region with encryption

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
DR must maintain data residency:

**DR Site Selection:**

| Factor | Requirement |
|--------|-------------|
| Data residency | Must remain in EU (GDPR, EBA guidelines) |
| Geographic separation | 200+ km for disaster resilience |
| Network latency | < 10ms for synchronous replication |
| Regulatory equivalence | Same compliance certifications |

**EU DR Options:**

| Primary | Secondary | Distance |
|---------|-----------|----------|
| Frankfurt | Amsterdam | ~365 km |
| Frankfurt | Paris | ~450 km |
| Frankfurt | Dublin | ~1,100 km |

**Why Not Others:**

- **A:** US location violates EU data residency
- **C:** Tape backup doesn't provide RTO for modern banking
- **D:** "Any region" may violate regulatory requirements

**Reference:** [Financial Services](financial-services.md)
</details>

---

### Question 15: Government — Zero Trust for Classified Networks

A defense agency is implementing Zero Trust on their classified network. What is the UNIQUE requirement compared to unclassified Zero Trust?

A) No unique requirements — Zero Trust is the same everywhere  
B) Physical access controls, personnel clearances, and air-gapped architecture  
C) Only biometric authentication is required  
D) Encryption is not required on classified networks

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Classified Zero Trust includes additional physical and personnel controls:

**Classified Network Requirements:**

| Layer | Standard Zero Trust | Classified Addition |
|-------|---------------------|---------------------|
| Identity | MFA, conditional access | Personnel clearances, NDA |
| Device | Device health attestation | Accredited hardware, TEMPEST |
| Network | Micro-segmentation | Air-gap, SIPR/JWICS networks |
| Data | Encryption, classification | Cross-domain guards, SCG |
| Physical | Building access | SCIFs, SAPF, intrusion detection |

**Air-Gap Implications:**

- No internet connectivity
- Manual update processes
- Physical media transfer procedures
- Increased operational complexity

**Reference:** [Government Cloud](government-cloud.md)
</details>

---

## Assessment Complete

**Scoring Guide:**

| Score | Result |
|-------|--------|
| 15/15 | Expert — Ready for complex industry engagements |
| 12-14/15 | Proficient — Minor review recommended |
| 9-11/15 | Developing — Review highlighted industries |
| < 9/15 | Needs Improvement — Complete module review |

---

## Next Steps

- **Review:** [Healthcare Sovereign](healthcare-sovereign.md)
- **Review:** [Financial Services](financial-services.md)
- **Review:** [Government Cloud](government-cloud.md)
- **Review:** [Critical Infrastructure](critical-infrastructure.md)
- **Next Assessment:** [Architecture Patterns Knowledge Check](patterns-knowledge-check.md)
