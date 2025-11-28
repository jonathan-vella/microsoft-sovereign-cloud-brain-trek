---
layout: default
title: Sovereign Public Cloud
parent: Module 2 - Sovereign Cloud Models
nav_order: 2.1
---

# Sovereign Public Cloud

{: .no_toc }

Azure public cloud with enhanced sovereignty controls, data residency guarantees, and compliance automation.

---

## Table of Contents

{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What is Sovereign Public Cloud?

**Sovereign Public Cloud** represents Microsoft's approach to delivering cloud services with enhanced sovereignty controls while maintaining the full benefits of public cloud infrastructure. It combines the **scalability, innovation, and cost-efficiency** of Azure public cloud with **data residency guarantees, operational transparency, and compliance automation** required for sovereign workloads.

### Core Concept

Unlike traditional public cloud where resources are shared with minimal control over data location and access, Sovereign Public Cloud provides:

- **Enhanced Data Controls:** Granular control over data location, processing, and access
- **Compliance Automation:** Policy-driven guardrails that enforce sovereignty requirements
- **Operational Transparency:** Clear visibility into who can access data and under what circumstances
- **Customer Lockbox:** Customer approval required for Microsoft support access
- **Confidential Computing:** Hardware-based encryption for data in use

**Key Principle:** "Sovereignty controls in the cloud, not sovereignty without the cloud"

---

## Microsoft Cloud for Sovereignty

Microsoft Cloud for Sovereignty is the primary solution for implementing Sovereign Public Cloud. It provides a **policy-driven framework** that enables organizations to meet sovereignty requirements while leveraging Azure's global infrastructure.

### What is Microsoft Cloud for Sovereignty?

**Microsoft Cloud for Sovereignty** is a set of capabilities, policies, and configurations built on top of Azure that:

1. **Enforces Data Residency:** Ensures data stays in specified regions
2. **Implements Access Controls:** Restricts who can access customer data
3. **Provides Transparency:** Logs and audits all access and operations
4. **Automates Compliance:** Continuously monitors and remediates policy violations
5. **Enables Confidentiality:** Protects data with hardware-based encryption

**Official Definition from Microsoft:**
> "Microsoft Cloud for Sovereignty is a solution that provides sovereignty controls and capabilities to help organizations meet their specific sovereignty, compliance, security, and policy requirements on the Microsoft Cloud." - [Microsoft Learn](https://learn.microsoft.com/en-us/industry/sovereign-cloud/)

---

## Key Capabilities and Features

### 1. Data Residency and Boundary Controls

**Data Residency Guarantees:**

- Customer data stored in specified Azure regions
- Data processing occurs within defined boundaries
- Backup and replication respect geographic constraints
- Metadata residency controls available

**EU Data Boundary Implementation:**

- Customer data and metadata stay within EU/EEA
- Documented exceptions with customer control
- Applies to Azure, Microsoft 365, Dynamics 365, Power Platform
- Ongoing expansion of boundary coverage

**Implementation:**

```text
Azure Policy → Deny resource creation outside allowed regions
Azure Monitor → Alert on data transfer outside boundaries
Azure Policy → Audit compliance continuously
Customer Lockbox → Control exceptions to data boundary
```

**[Learn More: EU Data Boundary](european-commitments#eu-data-boundary)**

---

### 2. Customer Lockbox

**What is Customer Lockbox?**

Customer Lockbox provides **customer approval** for Microsoft support engineers to access customer data. Without explicit approval, Microsoft cannot access customer content.

**How It Works:**

1. Microsoft support engineer needs access to customer data
2. Engineer initiates Customer Lockbox request
3. Customer receives notification and request details
4. Customer reviews request and approves or denies
5. Access is granted only if approved, and all access is logged
6. Access automatically expires after specified duration

**Key Benefits:**

- ✅ Customer control over support access
- ✅ Audit trail of all access requests and approvals
- ✅ Time-limited access with automatic expiration
- ✅ Integration with Azure AD for approver management

**Use Cases:**

- Regulatory requirements for data access approval
- High-security environments (financial, healthcare, government)
- Demonstrating control to auditors and customers
- Meeting contractual obligations for data access

**[Official Documentation: Customer Lockbox for Azure](https://learn.microsoft.com/en-us/azure/security/fundamentals/customer-lockbox-overview)**

---

### 3. Azure Policy for Compliance Automation

**Policy-Driven Sovereignty:**

Azure Policy enables organizations to **enforce sovereignty requirements automatically** rather than relying on manual processes or trust.

**Key Policy Capabilities:**

**Deny Policies:** Prevent non-compliant configurations

- Deny resource creation in non-allowed regions
- Deny public endpoint exposure
- Deny data export to non-compliant destinations

**Audit Policies:** Monitor compliance status

- Report on resource locations
- Track policy violations
- Generate compliance reports for auditors

**DeployIfNotExists Policies:** Auto-remediate violations

- Automatically enable encryption
- Deploy monitoring agents
- Configure diagnostic settings

**Example Sovereignty Policies:**

```json
// Deny resource creation outside EU regions
{
  "mode": "All",
  "policyRule": {
    "if": {
      "not": {
        "field": "location",
        "in": [
          "westeurope",
          "northeurope",
          "francecentral",
          "germanywestcentral",
          "swedencentral"
        ]
      }
    },
    "then": {
      "effect": "deny"
    }
  }
}
```

**Built-in Policy Initiatives for Sovereignty:**

- Microsoft Cloud for Sovereignty Baseline
- EU Data Boundary Policy Set
- Industry-specific compliance (GDPR, HIPAA, PCI DSS)
- Regional regulatory frameworks

**[Official Documentation: Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/overview)**

---

### 4. Confidential Computing

**What is Confidential Computing?**

Confidential Computing protects **data in use** by performing computation in a hardware-based trusted execution environment (TEE). This ensures data is encrypted even while being processed, protecting against:

- Cloud provider access
- Privileged administrator access
- Malicious insiders
- Hardware attacks

**Azure Confidential Computing Offerings:**

**Confidential VMs:**

- AMD SEV-SNP or Intel TDX enabled virtual machines
- Full VM memory encryption
- Attestation to verify encryption
- Use cases: High-value data processing, multi-party computation

**Azure Kubernetes Service (AKS) with Confidential Containers:**

- Container-level confidential computing
- Pod-to-pod encryption
- Attestation for container integrity

**Always Encrypted with Secure Enclaves (SQL Database):**

- Queries on encrypted data using Intel SGX
- Protects against database administrators
- Client-side encryption with server-side computation

**Azure Key Vault Managed HSM:**

- FIPS 140-2 Level 3 validated HSMs
- Customer-controlled key hierarchy
- Bring Your Own Key (BYOK) support

**When to Use Confidential Computing:**

- Processing sensitive data (PII, PHI, financial)
- Multi-party data collaboration (encrypted data sharing)
- Blockchain and distributed ledger scenarios
- Protecting intellectual property in the cloud
- Meeting specific regulatory requirements (GDPR Article 32)

**[Official Documentation: Azure Confidential Computing](https://learn.microsoft.com/en-us/azure/confidential-computing/overview)**

---

### 5. Encryption and Key Management

**Comprehensive Encryption Strategy:**

**Data at Rest:**

- Azure Storage Service Encryption (SSE) - enabled by default
- Azure Disk Encryption (ADE) for VM disks
- Transparent Data Encryption (TDE) for databases
- Customer-managed keys (CMK) in Azure Key Vault

**Data in Transit:**

- TLS 1.2+ for all Azure services
- ExpressRoute with private peering for dedicated connectivity
- VPN Gateway for site-to-site encryption
- Private Link for private connectivity to Azure services

**Data in Use:**

- Confidential Computing with TEEs (see above)
- Always Encrypted for SQL databases
- Client-side encryption for applications

**Key Management Options:**

| Option | Description | Sovereignty Level | Use Case |
|--------|-------------|-------------------|----------|
| **Microsoft-Managed Keys** | Microsoft manages encryption keys | Low | Standard workloads |
| **Customer-Managed Keys (CMK)** | Customer controls keys in Azure Key Vault | Medium | Regulated workloads |
| **Bring Your Own Key (BYOK)** | Customer imports keys from on-premises HSM | High | Compliance requirements |
| **Hold Your Own Key (HYOK)** | Customer retains keys on-premises | Maximum | Highest sovereignty needs |

**Key Vault Managed HSM:**

- Single-tenant HSM service
- FIPS 140-2 Level 3 validated
- Customer exclusive access
- Supports BYOK from on-premises HSMs

**[Official Documentation: Azure encryption overview](https://learn.microsoft.com/en-us/azure/security/fundamentals/encryption-overview)**

---

## Use Cases and Customer Scenarios

### Scenario 1: European Financial Services

**Customer:** Pan-European investment bank with operations in 15 EU countries

**Requirements:**

- GDPR compliance for customer financial data
- MiFID II and local banking regulations (BaFin, ACPR, ECB)
- Data residency within EU boundaries
- PCI DSS for payment processing
- Demonstrate sovereignty to regulators

**Solution Implementation:**

**Data Residency:**

- Deploy all workloads in Azure West Europe and North Europe regions
- Use Azure Policy to deny resource creation outside EU
- Configure geo-redundancy within EU (West Europe ↔ North Europe)
- Enable EU Data Boundary for all Microsoft 365 integration

**Compliance Automation:**

- Deploy Microsoft Cloud for Sovereignty Baseline policies
- Enable PCI DSS policy initiative for payment systems
- Configure continuous compliance monitoring via Azure Security Center
- Implement Azure Sentinel for security operations

**Access Controls:**

- Enable Customer Lockbox for all production subscriptions
- Configure Azure AD Privileged Identity Management (PIM)
- Implement Just-In-Time (JIT) VM access
- Require MFA for all administrative access

**Encryption:**

- Enable Azure Storage encryption with customer-managed keys
- Deploy Azure SQL with Always Encrypted for sensitive columns
- Use Azure Key Vault Managed HSM for key storage
- Enable Azure Disk Encryption on all VMs

**Outcomes:**

- ✅ Passed ECB regulatory audit with zero findings
- ✅ Reduced compliance reporting time by 70% with automated policies
- ✅ Demonstrated data sovereignty to all 15 national regulators
- ✅ Achieved PCI DSS certification in 6 months (vs. 12 months traditional)
- ✅ Reduced infrastructure costs by 40% vs. on-premises

---

### Scenario 2: Healthcare Provider Network

**Customer:** US regional hospital system with 20 hospitals across 5 states

**Requirements:**

- HIPAA compliance for Protected Health Information (PHI)
- State-specific privacy regulations
- Business Associate Agreement (BAA) with Microsoft
- Data must remain in United States
- Integration with health information exchanges (HIE)

**Solution Implementation:**

**Data Residency:**

- Deploy in Azure East US and Central US regions
- Use Azure Policy to restrict resource creation to US regions
- Configure backup and disaster recovery within US

**HIPAA Compliance:**

- Sign HIPAA Business Associate Agreement with Microsoft
- Deploy HIPAA-compliant Azure services (see [HIPAA compliance offerings](https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-hipaa-us))
- Enable Azure Policy for HIPAA compliance initiative
- Configure audit logging for all PHI access

**Security Controls:**

- Enable Customer Lockbox for PHI-containing subscriptions
- Deploy Azure Private Link for all PaaS services
- Use Azure Firewall for network traffic inspection
- Implement Azure DDoS Protection Standard

**Application Architecture:**

- Deploy Epic EHR integration via Azure API for FHIR
- Use Azure Functions for HL7 message processing
- Deploy Power BI for population health analytics (PHI-compliant)
- Implement Azure Logic Apps for HIE integration

**Outcomes:**

- ✅ Achieved HIPAA compliance across all facilities
- ✅ Integrated with 3 state HIEs for care coordination
- ✅ Reduced time to access patient records by 80%
- ✅ Enabled telehealth during COVID-19 within 2 weeks
- ✅ Improved population health outcomes with AI-powered analytics

---

### Scenario 3: Energy Sector Critical Infrastructure

**Customer:** European energy company operating power generation and distribution

**Requirements:**

- NIS2 Directive (EU Network and Information Security)
- Critical infrastructure protection requirements
- Data sovereignty for operational technology (OT) data
- SCADA and industrial control system integration
- Cyber resilience for critical national infrastructure

**Solution Implementation:**

**Data Sovereignty:**

- Deploy in Azure Sweden Central and Germany West Central
- Separate OT and IT networks with Azure Firewall
- Use Azure Policy to enforce data residency for OT data
- Configure Private Link for all industrial connections

**Critical Infrastructure Protection:**

- Deploy Microsoft Defender for IoT for OT security monitoring
- Use Azure Sentinel for security operations center (SOC)
- Implement Azure DDoS Protection for internet-facing services
- Enable Azure Confidential Computing for sensitive SCADA data analysis

**Operational Technology Integration:**

- Deploy Azure Arc-enabled servers for on-premises SCADA servers
- Use Azure IoT Edge for edge analytics at substations
- Implement Azure Digital Twins for power grid modeling
- Deploy Azure Time Series Insights for grid monitoring

**Compliance Automation:**

- Deploy NIS2 compliance policy initiative (custom)
- Automate security baseline for all resources
- Continuous compliance monitoring and reporting
- Integration with European cybersecurity authorities

**Outcomes:**

- ✅ Met NIS2 Directive requirements ahead of enforcement date
- ✅ Detected and prevented cyberattacks on OT systems
- ✅ Improved grid reliability by 15% with predictive analytics
- ✅ Maintained data sovereignty for critical infrastructure
- ✅ Passed national energy regulator security audit

---

## Implementation Best Practices

### Planning and Design Phase

**1. Data Discovery and Classification**

Before implementing Sovereign Public Cloud, understand what data you have:

✅ **Identify all data types:**

- Customer data (PII, financial, health)
- System data (logs, metrics, diagnostic)
- Organizational data (HR, financial, operational)

✅ **Classify by sensitivity:**

- Public (no controls needed)
- Internal (standard controls)
- Confidential (enhanced controls)
- Restricted (maximum controls)

✅ **Map data flows:**

- Where is data created?
- Where is data stored?
- Where is data processed?
- Where is data archived or deleted?

**Tool:** [Microsoft Purview Data Map](https://learn.microsoft.com/en-us/purview/concept-elastic-data-map) for automated data discovery

---

**2. Define Sovereignty Requirements**

Document clear sovereignty requirements:

✅ **Regulatory requirements:**

- Which regulations apply? (GDPR, HIPAA, sector-specific)
- What are data residency requirements?
- What compliance certifications are needed?

✅ **Operational requirements:**

- Where can data be stored?
- Where can data be processed?
- Who can access data?
- What audit and logging is required?

✅ **Technical requirements:**

- What encryption is required?
- What key management approach?
- What network isolation is needed?

**Output:** Sovereignty Requirements Document (SRD) that guides all implementation decisions

---

**3. Design Landing Zones**

Implement [Azure Landing Zones](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/) with sovereignty controls:

✅ **Management Groups hierarchy:**

```text
Root Management Group
├── Sovereign Workloads (MG)
│   ├── Production (MG) ← Strict policies
│   ├── Development (MG) ← Relaxed policies
│   └── Sandbox (MG) ← Testing policies
└── Non-Sovereign Workloads (MG)
```

✅ **Subscription design:**

- Separate subscriptions by sovereignty level
- Separate subscriptions by environment (prod/dev/test)
- Separate subscriptions by workload type

✅ **Network topology:**

- Hub-and-spoke with Azure Firewall
- Private Link for PaaS services
- ExpressRoute for hybrid connectivity
- Network Security Groups (NSGs) for micro-segmentation

**Reference:** [Microsoft Cloud for Sovereignty landing zone](https://learn.microsoft.com/en-us/industry/sovereign-cloud/sovereign-public-cloud/sovereign-landing-zone/overview-slz)

---

### Deployment Phase

**1. Deploy Core Infrastructure**

✅ **Identity and Access:**

- Deploy Azure AD tenant (or use existing)
- Configure Azure AD Privileged Identity Management
- Enable Azure AD Conditional Access
- Configure MFA for all users

✅ **Network Foundation:**

- Deploy hub VNet with Azure Firewall
- Deploy spoke VNets for workloads
- Configure VNet peering
- Deploy Azure Bastion for secure VM access
- Configure ExpressRoute (if needed)

✅ **Governance:**

- Apply Azure Policy at Management Group level
- Deploy Azure Blueprints for repeatable deployments
- Configure Azure Monitor and Log Analytics
- Enable Azure Security Center

---

**2. Implement Sovereignty Controls**

✅ **Data Residency Policies:**

```text
Deploy-AzPolicy -Name "Deny-Non-EU-Regions" -PolicyDefinition $policyDef
```

✅ **Customer Lockbox:**

- Enable at subscription level
- Configure approver groups in Azure AD
- Set up notifications via Azure Logic Apps
- Document approval process

✅ **Encryption:**

- Deploy Azure Key Vault in each region
- Configure customer-managed keys
- Enable Azure Disk Encryption on all VMs
- Configure Always Encrypted for SQL databases

✅ **Monitoring and Auditing:**

- Enable Azure Activity Log for all subscriptions
- Configure diagnostic settings for all resources
- Deploy Azure Sentinel for SIEM
- Set up compliance dashboards

---

**3. Migrate Workloads**

Follow a phased migration approach:

**Phase 1: Non-Production (2-4 weeks)**

- Migrate dev/test workloads first
- Validate sovereignty controls work as expected
- Test disaster recovery procedures
- Train operations team

**Phase 2: Low-Risk Production (4-6 weeks)**

- Migrate non-critical production workloads
- Monitor compliance and performance
- Refine policies based on learnings
- Document runbooks

**Phase 3: High-Risk Production (6-12 weeks)**

- Migrate critical sovereign workloads
- Extensive testing and validation
- Customer communication and change management
- Post-migration compliance validation

---

### Operational Phase

**1. Continuous Compliance Monitoring**

✅ **Daily Tasks:**

- Review Azure Policy compliance dashboard
- Respond to policy violation alerts
- Review Customer Lockbox requests

✅ **Weekly Tasks:**

- Review security recommendations from Azure Security Center
- Analyze Azure Sentinel security incidents
- Review cost and optimization recommendations

✅ **Monthly Tasks:**

- Generate compliance reports for auditors
- Review and update Azure Policy definitions
- Conduct access reviews for privileged accounts
- Update disaster recovery documentation

**Tool:** [Azure Compliance Manager](https://learn.microsoft.com/en-us/microsoft-365/compliance/compliance-manager)

---

**2. Change Management**

✅ **Policy Changes:**

- Test policy changes in dev/test subscriptions first
- Document reason for policy changes
- Communicate changes to affected teams
- Monitor for unintended impacts

✅ **Infrastructure Changes:**

- Use Infrastructure as Code (ARM templates, Bicep, Terraform)
- Implement CI/CD for infrastructure changes
- Require approvals for production changes
- Maintain change log for audits

---

## Sales Talking Points

### Value Propositions

**1. "Cloud Innovation with Sovereignty Assurance"**

- Get all Azure services (200+) while meeting sovereignty requirements
- Continuous innovation from Microsoft without compromising compliance
- New AI, ML, and analytics capabilities with data sovereignty
- **ROI:** Innovation velocity 3x faster than on-premises

**2. "Automated Compliance, Reduced Risk"**

- Policy-driven compliance enforcement (not manual processes)
- Continuous monitoring and automated remediation
- Reduces audit preparation time by 60-70%
- **ROI:** Compliance cost reduction 40-50%

**3. "Pay for What You Use"**

- OpEx model vs. CapEx for on-premises
- Elastic scale up/down based on demand
- Reserved instances and savings plans for predictable workloads
- **ROI:** 40-50% cost reduction vs. on-premises typical

**4. "Enterprise-Grade Security"**

- More security features than any other cloud provider
- Microsoft invests $1B+ annually in security
- 8,500+ security experts worldwide
- **Differentiator:** Security at cloud scale

---

### Discovery Questions

**Data and Compliance:**

1. "What types of data do you handle, and what are the sensitivity levels?"
2. "What regulatory frameworks apply to your organization?"
3. "Do you have specific data residency requirements from regulators or customers?"
4. "How do you currently demonstrate compliance to auditors?"

**Current Infrastructure:**
5. "What percentage of workloads are currently in the cloud vs. on-premises?"
6. "What cloud services are you currently using (Azure, AWS, GCP)?"
7. "What are your biggest challenges with your current infrastructure?"
8. "How do you handle disaster recovery and business continuity today?"

**Security and Access:**
9. "Who currently has access to your sensitive data?"
10. "Do you have requirements for customer approval of support access?"
11. "What encryption standards are you required to meet?"
12. "How do you manage encryption keys today?"

**Business Drivers:**
13. "What are your top 3 business priorities for the next 12 months?"
14. "What is driving your interest in sovereign cloud solutions?"
15. "What would success look like for a cloud sovereignty initiative?"
16. "What is your timeline for implementing sovereignty controls?"

---

## Competitive Differentiation

### vs. AWS

**Microsoft Advantages:**

1. **Policy-Driven Sovereignty:**
   - ✅ Microsoft: Microsoft Cloud for Sovereignty with automated compliance
   - ⚠️ AWS: Manual configuration of controls, no sovereignty-specific offering

2. **EU Data Boundary:**
   - ✅ Microsoft: Comprehensive EU Data Boundary across Azure, Microsoft 365, Dynamics
   - ❌ AWS: No equivalent data boundary commitment

3. **Customer Lockbox:**
   - ✅ Microsoft: Customer approval required for support access
   - ❌ AWS: No equivalent capability

4. **Confidential Computing:**
   - ✅ Microsoft: Confidential VMs, AKS with confidential containers, Always Encrypted
   - ⚠️ AWS: Limited confidential computing options (Nitro Enclaves)

**When to Emphasize:**

- Customer requires EU Data Boundary
- Customer needs policy-driven compliance automation
- Customer requires customer approval for support access
- Customer has Microsoft enterprise agreement

---

### vs. Google Cloud

**Microsoft Advantages:**

1. **Sovereign Cloud Portfolio:**
   - ✅ Microsoft: Three sovereign models (Public, Private, Partner)
   - ⚠️ Google: Limited sovereignty offerings

2. **Compliance Certifications:**
   - ✅ Microsoft: 100+ compliance certifications
   - ⚠️ Google: ~60 certifications

3. **Enterprise Integration:**
   - ✅ Microsoft: Seamless integration with Microsoft 365, Dynamics, Power Platform
   - ⚠️ Google: Limited enterprise suite

4. **Government Cloud:**
   - ✅ Microsoft: Azure Government with FedRAMP High, DoD IL6
   - ⚠️ Google: Limited government cloud capabilities

**When to Emphasize:**

- Customer has Microsoft enterprise footprint
- Customer requires extensive compliance certifications
- Customer needs government-specific cloud
- Customer wants integrated cloud platform

---

## Common Challenges and Solutions

### Challenge 1: Performance Concerns with Encryption

**Concern:** "Won't encryption and sovereignty controls slow down our applications?"

**Solution:**

- Azure Storage encryption has negligible performance impact (<5%)
- Confidential Computing VMs have ~10-15% performance overhead (acceptable for most workloads)
- Network encryption (TLS) overhead minimal with modern processors
- Use Premium SSD or Ultra Disk for I/O-intensive workloads
- **Proof Point:** Banking customers report no noticeable performance degradation

---

### Challenge 2: Cost Concerns

**Concern:** "Sovereign Public Cloud sounds expensive. Will we pay a premium?"

**Solution:**

- Sovereign Public Cloud uses same pricing as standard Azure
- Customer Lockbox: No additional cost
- Azure Policy: No additional cost
- Customer-managed keys: Small additional cost for Key Vault operations
- Confidential Computing: ~10-20% premium for specialized VMs
- **ROI:** Total cost typically 40-50% lower than on-premises due to OpEx model

---

### Challenge 3: Complexity

**Concern:** "This sounds complex. Do we need specialized skills?"

**Solution:**

- Microsoft Cloud for Sovereignty provides pre-built policies and blueprints
- Azure Policy enforces compliance automatically
- Microsoft FastTrack available for guidance
- Training available via Microsoft Learn
- **Support:** Assign Customer Success Manager for large deployments

---

### Challenge 4: Lock-In Fears

**Concern:** "Will we be locked into Microsoft if we use sovereignty controls?"

**Solution:**

- Sovereignty controls use standard Azure features (not proprietary)
- Applications remain portable (containers, VMs)
- Data export capabilities maintained
- Multi-cloud strategies possible with Azure Arc
- **Differentiation:** More portable than AWS or Google Cloud Platform

---

## Next Steps and Learning Resources

### Continue Learning

- **[← Back to Sovereign Cloud Models Overview](sovereign-cloud-models)**
- **[→ Next: Sovereign Private Cloud](sovereign-private-cloud)**
- **[Explore: National Partner Clouds](national-partner-clouds)**

### Hands-On Learning

1. **[Microsoft Cloud for Sovereignty quickstart](https://learn.microsoft.com/en-us/industry/sovereign-cloud/sovereign-public-cloud/sovereign-landing-zone/overview-slz)**
2. **[Deploy Azure Policy for compliance](https://learn.microsoft.com/en-us/azure/governance/policy/tutorials/create-and-manage)**
3. **[Configure Customer Lockbox](https://learn.microsoft.com/en-us/azure/security/fundamentals/customer-lockbox-overview)**
4. **[Set up Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/quick-create-portal)**

### Additional Resources

- **[Microsoft Cloud for Sovereignty documentation](https://learn.microsoft.com/en-us/industry/sovereign-cloud/)** - Official hub
- **[Azure compliance documentation](https://learn.microsoft.com/en-us/azure/compliance/)** - Compliance offerings
- **[EU Data Boundary](https://aka.ms/eudb)** - EU commitment details
- **[Azure confidential computing](https://learn.microsoft.com/en-us/azure/confidential-computing/)** - Confidential computing guide

---

**Last Updated:** October 2025
