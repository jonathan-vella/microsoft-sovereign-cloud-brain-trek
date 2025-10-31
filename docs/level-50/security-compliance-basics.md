---
layout: default
title: Overview
parent: Module 2 - Security & Compliance Basics
nav_order: 1
---

# Security & Compliance Basics
{: .no_toc }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What is Information Security?

**Information security** refers to the practice of protecting information and information systems from unauthorized access, use, disclosure, disruption, modification, or destruction. In today's digital world, this includes protecting data both at rest (stored data) and in transit (data being transmitted).

Information security is critical for:
- Protecting sensitive business data
- Maintaining customer trust
- Meeting regulatory requirements
- Preventing financial losses from breaches
- Ensuring business continuity

### Why Security Matters in the Cloud

Cloud computing introduces new security considerations:

**Shared Responsibility:** Security is shared between cloud provider and customer
**Data Location:** Data may be stored in multiple geographic locations
**Access Control:** Managing who can access cloud resources
**Compliance:** Meeting regulatory requirements in cloud environments
**Visibility:** Understanding what's happening in your cloud environment

---

## The CIA Triad

> **📊 Visual Reference Needed**
> *CIA Triad Security Model (Asset 22)*
> This section includes a visual diagram showing the three pillars of information security (Confidentiality, Integrity, Availability) as a triangle or three interconnected circles.
> **Specification Reference:** See `docs/level-50/VISUAL_SPECIFICATIONS.md` → Asset 22

The CIA triad forms the foundation of information security by establishing three core principles:

### Confidentiality

**Definition:** Ensuring that information is accessible only to those authorized to have access.

**Key Concepts:**
- Data should only be viewable by authorized individuals
- Unauthorized disclosure must be prevented
- Access controls and permissions management
- Encryption to protect data from unauthorized viewing

**Examples:**
- **Encryption:** Protecting data so it's unreadable without proper keys
- **Access Controls:** User permissions and role-based access
- **Authentication:** Verifying user identity before granting access
- **Data Classification:** Labeling data based on sensitivity level

**Real-World Scenario:**
> A healthcare provider encrypts patient medical records so that only authorized medical staff can view the information, even if someone gains unauthorized access to the database files.

**Common Threats to Confidentiality:**
- Data breaches and unauthorized access
- Insider threats from malicious employees
- Social engineering attacks
- Weak authentication mechanisms
- Unencrypted data transmission

### Integrity

**Definition:** Ensuring that information remains accurate and unaltered except by authorized modification.

**Key Concepts:**
- Data should not be modified without authorization
- Changes should be trackable and auditable
- Data should remain consistent and accurate
- Protection against unauthorized modifications

**Examples:**
- **Digital Signatures:** Proving that data hasn't been tampered with
- **Checksums and Hashing:** Detecting unauthorized changes
- **Version Control:** Tracking changes and maintaining history
- **Backup and Recovery:** Protecting against data corruption

**Real-World Scenario:**
> A financial institution uses digital signatures and checksums to ensure that transaction records cannot be altered without detection, maintaining trust in financial data.

**Common Threats to Integrity:**
- Malicious modification of data
- Accidental corruption or deletion
- System failures and hardware errors
- Malware that modifies files
- Man-in-the-middle attacks during transmission

### Availability

**Definition:** Ensuring that information and information systems are accessible to authorized users when needed.

**Key Concepts:**
- Systems should be operational when required
- Data should be accessible to authorized users
- Service disruptions should be minimized
- Recovery capabilities for system failures

**Examples:**
- **Redundancy:** Multiple systems to prevent single points of failure
- **Load Balancing:** Distributing traffic across multiple servers
- **Disaster Recovery:** Plans and procedures for major outages
- **Regular Backups:** Ensuring data can be restored if lost

**Real-World Scenario:**
> An e-commerce website uses load balancing and redundant servers across multiple data centers to ensure the site remains available even if one data center experiences problems.

**Common Threats to Availability:**
- Denial of Service (DoS) attacks
- Hardware failures and system crashes
- Natural disasters affecting data centers
- Network outages and connectivity issues
- Software bugs and system vulnerabilities

---

## Authentication vs. Authorization

Understanding the difference between authentication and authorization is fundamental to security:

### Authentication

**Definition:** The process of verifying the identity of a user, device, or system.

**Key Question:** "Who are you?"

**Common Methods:**
- **Something you know:** Passwords, PINs, security questions
- **Something you have:** Smart cards, mobile devices, hardware tokens
- **Something you are:** Biometrics (fingerprints, facial recognition, retina scans)
- **Something you do:** Behavioral patterns, typing patterns

**Multi-Factor Authentication (MFA):**
- Combines two or more authentication methods
- Significantly improves security
- Example: Password (something you know) + SMS code (something you have)

**Examples:**
- Logging into your email with username and password
- Using a fingerprint to unlock your smartphone
- Entering a verification code sent to your phone

### Authorization

**Definition:** The process of determining what actions an authenticated user is allowed to perform.

**Key Question:** "What are you allowed to do?"

**Common Models:**
- **Role-Based Access Control (RBAC):** Access based on user roles
- **Attribute-Based Access Control (ABAC):** Access based on multiple attributes
- **Discretionary Access Control (DAC):** Access controlled by data owners
- **Mandatory Access Control (MAC):** Access controlled by system policies

**Examples:**
- An authenticated employee can read company documents but not financial records
- A manager can approve expenses up to $5,000 but needs higher approval for larger amounts
- A database administrator can create databases but cannot access sensitive customer data

### Identity and Access Management (IAM)

**Definition:** The framework of policies and technologies for ensuring that the right people have the right access to the right resources at the right time.

**Key Components:**
- **Identity Management:** Creating, maintaining, and deactivating user identities
- **Access Management:** Controlling what authenticated users can access
- **Single Sign-On (SSO):** One login for multiple applications
- **Privileged Access Management (PAM):** Special controls for administrative accounts

---

## Data Protection Principles

### Data Classification

**Purpose:** Categorizing data based on its sensitivity and importance to the organization.

**Common Classification Levels:**
- **Public:** Information that can be freely shared (marketing materials, press releases)
- **Internal:** Information for internal use only (policies, procedures)
- **Confidential:** Sensitive information requiring protection (customer data, financial records)
- **Restricted:** Highly sensitive information (trade secrets, classified data)

**Implementation:**
- Data labeling and tagging systems
- Automated classification tools
- Access controls based on classification
- Handling procedures for each classification level

### Data Lifecycle Management

**Stages of Data Lifecycle:**
1. **Creation:** When data is first generated or collected
2. **Storage:** How and where data is stored
3. **Use:** How data is accessed and utilized
4. **Sharing:** Controlled distribution of data
5. **Archival:** Long-term storage for compliance or historical purposes
6. **Destruction:** Secure deletion when data is no longer needed

**Security Considerations at Each Stage:**
- **Creation:** Ensure data is properly classified from the start
- **Storage:** Implement appropriate encryption and access controls
- **Use:** Monitor access and prevent unauthorized usage
- **Sharing:** Control and audit data distribution
- **Archival:** Maintain security controls for long-term storage
- **Destruction:** Ensure complete and secure deletion

### Encryption Fundamentals

**Definition:** The process of converting readable data into an encoded format that can only be read with the correct decryption key.

**Types of Encryption:**

**Encryption at Rest:**
- Protects stored data on hard drives, databases, and storage systems
- Examples: Full disk encryption, database encryption, file-level encryption

**Encryption in Transit:**
- Protects data being transmitted over networks
- Examples: HTTPS, TLS/SSL, VPN encryption

**Encryption in Use:**
- Protects data while it's being processed (advanced technique)
- Examples: Confidential computing, homomorphic encryption

**Key Management:**
- Secure generation, storage, and rotation of encryption keys
- Hardware Security Modules (HSMs) for key protection
- Key escrow and recovery procedures

---

## Compliance Frameworks Overview

### What is Compliance?

**Compliance** refers to adhering to laws, regulations, standards, and internal policies that apply to an organization's operations and data handling practices.

**Why Compliance Matters:**
- **Legal Requirements:** Avoid fines and legal penalties
- **Business Relationships:** Many contracts require compliance certifications
- **Customer Trust:** Demonstrating commitment to data protection
- **Risk Management:** Reducing security and operational risks

### Common Compliance Frameworks

#### SOC 2 (Service Organization Control 2)

**Purpose:** Auditing standard for service providers storing customer data in the cloud

**Trust Service Categories:**
- **Security:** Protection against unauthorized access
- **Availability:** System operational availability
- **Processing Integrity:** System processing is complete, valid, accurate, timely
- **Confidentiality:** Information designated as confidential is protected
- **Privacy:** Personal information is collected, used, retained, disclosed according to policy

**Types:**
- **Type I:** Design of controls at a specific point in time
- **Type II:** Operating effectiveness of controls over a period (typically 12 months)

**Business Impact:**
- Required for most B2B cloud services
- Demonstrates commitment to security and operational excellence
- Enables trust in vendor relationships

#### ISO 27001

**Purpose:** International standard for information security management systems (ISMS)

**Key Requirements:**
- Risk assessment and treatment
- Information security policies and procedures
- Employee security training and awareness
- Incident response and business continuity planning
- Regular monitoring and improvement

**Benefits:**
- Systematic approach to information security
- International recognition and credibility
- Continuous improvement framework
- Reduced security risks and incidents

#### GDPR (General Data Protection Regulation)

**Scope:** EU regulation protecting personal data of EU residents

**Key Principles:**
- **Lawfulness, fairness, and transparency:** Clear purpose and legal basis for processing
- **Purpose limitation:** Data used only for specified purposes
- **Data minimization:** Only collect and process necessary data
- **Accuracy:** Keep personal data accurate and up to date
- **Storage limitation:** Keep data only as long as necessary
- **Integrity and confidentiality:** Protect data from unauthorized access
- **Accountability:** Demonstrate compliance with all principles

**Individual Rights:**
- Right to access personal data
- Right to rectification (correction)
- Right to erasure ("right to be forgotten")
- Right to portability
- Right to object to processing

**Penalties:** Up to €20 million or 4% of global annual turnover

#### HIPAA (Health Insurance Portability and Accountability Act)

**Scope:** US regulation protecting health information

**Key Requirements:**
- **Privacy Rule:** Standards for protecting health information
- **Security Rule:** Administrative, physical, and technical safeguards
- **Breach Notification Rule:** Requirements for reporting data breaches
- **Business Associate Agreements:** Contracts with third-party service providers

**Protected Health Information (PHI):**
- Any health information that can be linked to an individual
- Includes medical records, billing information, and health plan data
- Special protections for mental health and substance abuse records

#### PCI DSS (Payment Card Industry Data Security Standard)

**Purpose:** Security standard for organizations handling credit card information

**Requirements:**
1. Install and maintain firewall configuration
2. Do not use vendor-supplied defaults for passwords
3. Protect stored cardholder data
4. Encrypt transmission of cardholder data across public networks
5. Use and regularly update anti-virus software
6. Develop and maintain secure systems and applications
7. Restrict access to cardholder data by business need-to-know
8. Assign a unique ID to each person with computer access
9. Restrict physical access to cardholder data
10. Track and monitor access to network resources
11. Regularly test security systems and processes
12. Maintain information security policy

**Compliance Levels:**
- **Level 1:** Over 6 million transactions annually
- **Level 2:** 1-6 million transactions annually
- **Level 3:** 20,000-1 million e-commerce transactions annually
- **Level 4:** Fewer than 20,000 e-commerce transactions annually

---

## Risk Management Principles

### Understanding Risk

**Risk Definition:** The potential for loss, damage, or destruction of assets or data as a result of a threat exploiting a vulnerability.

**Risk Formula:** Risk = Threat × Vulnerability × Impact

**Key Components:**
- **Asset:** Anything of value to the organization (data, systems, reputation)
- **Threat:** Potential cause of harm (hackers, natural disasters, insider threats)
- **Vulnerability:** Weakness that could be exploited (unpatched software, weak passwords)
- **Impact:** Potential consequences if the risk materializes (financial loss, reputation damage)

### Risk Assessment Process

#### 1. Asset Identification

**Questions to Ask:**
- What data and systems are critical to business operations?
- What would happen if these assets were compromised?
- Who has access to these assets?
- Where are these assets located or stored?

**Asset Categories:**
- **Data Assets:** Customer information, financial records, intellectual property
- **System Assets:** Servers, applications, network infrastructure
- **People Assets:** Employees, contractors, business partners
- **Physical Assets:** Buildings, equipment, storage media

#### 2. Threat Identification

**External Threats:**
- **Cybercriminals:** Motivated by financial gain
- **Nation-State Actors:** Advanced persistent threats (APTs)
- **Hacktivists:** Motivated by social or political causes
- **Natural Disasters:** Floods, earthquakes, fires
- **Supply Chain Attacks:** Compromised vendors or partners

**Internal Threats:**
- **Malicious Insiders:** Employees with harmful intent
- **Negligent Insiders:** Accidental security incidents
- **Privileged Users:** Administrators with excessive access
- **Contractors and Partners:** Third-party access risks

#### 3. Vulnerability Assessment

**Technical Vulnerabilities:**
- Unpatched software and operating systems
- Misconfigured security settings
- Weak encryption or authentication
- Insecure network protocols

**Process Vulnerabilities:**
- Inadequate security policies
- Lack of employee training
- Poor incident response procedures
- Insufficient access controls

**Physical Vulnerabilities:**
- Unsecured facilities
- Unprotected network equipment
- Lack of surveillance systems
- Poor visitor access controls

#### 4. Impact Analysis

**Impact Categories:**
- **Financial:** Direct costs, lost revenue, fines and penalties
- **Operational:** Business disruption, lost productivity
- **Reputational:** Customer trust, brand damage, media attention
- **Legal:** Regulatory violations, litigation, compliance failures

**Impact Scales:**
- **Low:** Minimal impact on business operations
- **Medium:** Moderate impact requiring recovery efforts
- **High:** Significant impact affecting core business functions
- **Critical:** Severe impact threatening business survival

### Risk Treatment Strategies

#### 1. Risk Mitigation (Reduce)

**Approach:** Implement controls to reduce the likelihood or impact of risks

**Examples:**
- Installing firewalls and intrusion detection systems
- Implementing multi-factor authentication
- Regular security training for employees
- Encryption of sensitive data

**When to Use:** When the cost of controls is less than the potential impact

#### 2. Risk Transfer (Share)

**Approach:** Transfer risk to another party through insurance or contracts

**Examples:**
- Cyber insurance policies
- Cloud service provider agreements
- Outsourcing to specialized security providers
- Business partner indemnification clauses

**When to Use:** When specialized expertise or resources are needed

#### 3. Risk Avoidance (Eliminate)

**Approach:** Eliminate the risk by avoiding the activity that creates it

**Examples:**
- Not collecting sensitive data that isn't essential
- Avoiding high-risk technologies or vendors
- Restricting certain types of business activities
- Geographic limitations on operations

**When to Use:** When the risk is too high or the activity isn't essential

#### 4. Risk Acceptance (Accept)

**Approach:** Accept the risk and its potential consequences

**Examples:**
- Self-insuring against certain types of losses
- Accepting residual risk after implementing controls
- Operating with known vulnerabilities when fixes aren't available
- Budget allocation for potential security incidents

**When to Use:** When the cost of mitigation exceeds the potential impact

---

## Security in Cloud Computing

### Shared Responsibility Model

Cloud security operates on a shared responsibility model where both the cloud provider and customer have important security responsibilities.

#### Cloud Provider Responsibilities

**Infrastructure Security:**
- Physical security of data centers
- Hardware maintenance and replacement
- Network infrastructure protection
- Host operating system patching

**Service Security:**
- Platform security and updates
- Service availability and redundancy
- Built-in security features and tools
- Compliance certifications and audits

#### Customer Responsibilities

**Data Security:**
- Data classification and protection
- Encryption key management
- Access control configuration
- Data backup and recovery

**Application Security:**
- Application code security
- User access management
- Operating system updates (for IaaS)
- Network traffic protection

### Cloud Security Best Practices

#### 1. Identity and Access Management

**Implement Strong Authentication:**
- Multi-factor authentication for all users
- Strong password policies and requirements
- Regular review and rotation of credentials
- Privileged access management for administrators

**Principle of Least Privilege:**
- Grant minimum necessary permissions
- Regular access reviews and cleanup
- Role-based access control implementation
- Just-in-time access for administrative tasks

#### 2. Data Protection

**Encryption Strategy:**
- Encrypt data at rest and in transit
- Proper key management and rotation
- Use of hardware security modules (HSMs)
- Consider encryption in use for sensitive workloads

**Data Classification:**
- Classify data based on sensitivity
- Apply appropriate protection levels
- Monitor and audit data access
- Implement data loss prevention (DLP) tools

#### 3. Network Security

**Network Segmentation:**
- Isolate different environments (production, development, testing)
- Use virtual private networks (VPNs) for remote access
- Implement micro-segmentation for granular control
- Monitor network traffic for anomalies

**Firewall and Access Controls:**
- Configure firewalls with minimal necessary access
- Regular review and updating of firewall rules
- Intrusion detection and prevention systems
- DDoS protection services

#### 4. Monitoring and Incident Response

**Security Monitoring:**
- Centralized logging and monitoring
- Security information and event management (SIEM)
- Real-time alerting for security events
- Regular security assessments and penetration testing

**Incident Response Planning:**
- Documented incident response procedures
- Regular testing and updating of plans
- Clear roles and responsibilities
- Communication protocols for incidents

---

## Governance vs. Compliance

### Understanding the Difference

**Governance:**
- Internal framework for managing and controlling IT operations
- Policies, procedures, and standards set by the organization
- Ongoing oversight and decision-making processes
- Aligned with business objectives and risk tolerance

**Compliance:**
- Adherence to external laws, regulations, and standards
- Mandatory requirements with legal or contractual obligations
- Formal audits and certifications
- Penalties for non-compliance

### IT Governance Framework

#### 1. Policies and Standards

**Information Security Policy:**
- High-level security objectives and principles
- Management commitment and responsibilities
- Compliance requirements and enforcement
- Regular review and update procedures

**Technical Standards:**
- Specific technical requirements and configurations
- Security controls and implementation guidelines
- Technology selection criteria
- Performance and security metrics

#### 2. Processes and Procedures

**Change Management:**
- Controlled process for implementing changes
- Risk assessment and approval workflows
- Testing and rollback procedures
- Documentation and communication requirements

**Access Management:**
- User provisioning and deprovisioning
- Access request and approval processes
- Regular access reviews and certification
- Privileged access management procedures

#### 3. Oversight and Monitoring

**Risk Management:**
- Regular risk assessments and updates
- Risk register maintenance
- Key risk indicator (KRI) monitoring
- Escalation procedures for high-risk situations

**Performance Monitoring:**
- Key performance indicators (KPIs) for security
- Service level agreements (SLAs) and metrics
- Regular reporting to management
- Continuous improvement initiatives

---

## Common Security Threats and Vulnerabilities

### Cyber Threats

#### Malware

**Types:**
- **Viruses:** Self-replicating programs that attach to other files
- **Worms:** Self-replicating programs that spread across networks
- **Trojans:** Malicious programs disguised as legitimate software
- **Ransomware:** Encrypts data and demands payment for decryption
- **Spyware:** Secretly monitors and collects information

**Protection Strategies:**
- Anti-malware software with real-time protection
- Regular software updates and patches
- Email filtering and attachment scanning
- User education and awareness training

#### Phishing and Social Engineering

**Common Techniques:**
- **Email Phishing:** Fraudulent emails requesting sensitive information
- **Spear Phishing:** Targeted attacks against specific individuals
- **Vishing:** Voice-based phishing using phone calls
- **Smishing:** SMS-based phishing attacks
- **Pretexting:** Creating false scenarios to gather information

**Protection Strategies:**
- Security awareness training for employees
- Email filtering and threat detection
- Multi-factor authentication
- Verification procedures for sensitive requests

#### Advanced Persistent Threats (APTs)

**Characteristics:**
- Long-term, targeted attacks
- Advanced techniques and tools
- Often state-sponsored or organized crime
- Focus on high-value targets and data

**Protection Strategies:**
- Advanced threat detection and response
- Network segmentation and monitoring
- Regular security assessments
- Threat intelligence and information sharing

### Vulnerability Management

#### Common Vulnerabilities

**Software Vulnerabilities:**
- Unpatched operating systems and applications
- Misconfigured services and applications
- Weak default passwords and configurations
- Outdated encryption and security protocols

**Process Vulnerabilities:**
- Inadequate change management procedures
- Lack of security testing in development
- Insufficient access controls
- Poor incident response capabilities

#### Vulnerability Management Process

**1. Discovery:**
- Regular vulnerability scanning
- Penetration testing and security assessments
- Threat intelligence monitoring
- Security research and vendor notifications

**2. Assessment:**
- Risk rating based on severity and exploitability
- Business impact analysis
- Asset criticality evaluation
- Threat landscape consideration

**3. Remediation:**
- Patching and software updates
- Configuration changes and hardening
- Compensating controls implementation
- Risk acceptance for low-impact vulnerabilities

**4. Verification:**
- Testing of remediation efforts
- Follow-up scanning and assessment
- Documentation of actions taken
- Lessons learned and process improvement

---

## Key Takeaways

- **Security is everyone's responsibility:** Both technical and non-technical staff play important roles
- **CIA triad provides foundation:** Confidentiality, Integrity, and Availability guide all security decisions
- **Authentication confirms identity:** "Who are you?" - verify before granting access
- **Authorization controls access:** "What can you do?" - limit access to necessary resources
- **Data classification drives protection:** Different data types require different security controls
- **Compliance is mandatory:** Legal and regulatory requirements must be met
- **Risk management is ongoing:** Continuous assessment and treatment of security risks
- **Shared responsibility in cloud:** Both provider and customer have security responsibilities

---

## Sales & Pre-Sales Talking Points

### Value Proposition

"Security and compliance aren't just technical requirements - they're business enablers. By implementing proper security controls and meeting compliance requirements, you can build customer trust, enter new markets, and reduce business risks."

### Discovery Questions

1. What types of data does your organization handle? (Personal, financial, health, etc.)
2. What compliance requirements do you need to meet? (GDPR, HIPAA, SOX, etc.)
3. How do you currently manage user access to systems and data?
4. Have you experienced any security incidents in the past?
5. What is your biggest security concern when considering cloud adoption?

### Objection Handling

**Objection:** "Cloud can't be as secure as our on-premises systems."
**Response:** "Major cloud providers invest billions in security expertise and infrastructure that most organizations can't match. The key is understanding the shared responsibility model and properly configuring your security controls."

**Objection:** "Compliance requirements prevent us from using cloud services."
**Response:** "Cloud providers offer extensive compliance certifications and specialized services designed for regulated industries. Many organizations find cloud helps them meet compliance requirements more easily and cost-effectively."

**Objection:** "We don't have the expertise to secure our cloud environment."
**Response:** "Cloud platforms provide built-in security tools and extensive documentation. Additionally, there are many training resources and professional services available to help you build the necessary expertise."

---

## Technical Considerations

### Security Architecture

**Defense in Depth:**
- Multiple layers of security controls
- Redundancy to prevent single points of failure
- Comprehensive coverage across all attack vectors
- Integration between security tools and processes

**Zero Trust Model:**
- Never trust, always verify
- Least privilege access principles
- Continuous monitoring and validation
- Assume breach mentality

### Monitoring and Detection

**Key Metrics:**
- Failed login attempts and authentication events
- Privileged access and administrative actions
- Data access and file modifications
- Network traffic anomalies and suspicious patterns

**Tools and Technologies:**
- Security Information and Event Management (SIEM)
- User and Entity Behavior Analytics (UEBA)
- Endpoint Detection and Response (EDR)
- Cloud Security Posture Management (CSPM)

---

## Deep Dive Topics

This module provides a foundational overview of security and compliance. For detailed exploration of specific topics, continue to these pages:

### 📘 Data Protection Principles
**[Read Full Article →](data-protection-principles)**

Comprehensive guide to data protection:
- Data classification methodologies
- Encryption implementation strategies
- Data lifecycle management
- Privacy by design principles

### 📘 Compliance Frameworks Deep Dive
**[Read Full Article →](compliance-frameworks)**

Detailed analysis of major frameworks:
- GDPR implementation requirements
- HIPAA security and privacy rules
- SOC 2 audit preparation
- ISO 27001 certification process

### 📘 Identity and Access Management
**[Read Full Article →](identity-access-basics)**

Complete IAM implementation guide:
- Authentication method comparison
- Role-based access control design
- Single sign-on architecture
- Privileged access management

### ✅ Test Your Knowledge
**[Take the Security & Compliance Knowledge Check →](security-compliance-knowledge-check)**

10 questions covering all security and compliance fundamentals.

---

## Next Steps

- **[Learn About Microsoft Azure Introduction →](../module-03-azure-intro/)**
- **[Review Cloud Computing Primer →](../module-01-cloud-computing/)**
- **[Take the Comprehensive Level 50 Assessment →](../comprehensive-knowledge-check/)**

---

## Additional Resources

- **[Microsoft Security Documentation](https://learn.microsoft.com/en-us/security/)** - Comprehensive security guidance
- **[NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)** - Industry standard framework
- **[SANS Institute Resources](https://www.sans.org/resources/)** - Security training and resources
- **[Microsoft Trust Center](https://www.microsoft.com/en-us/trust-center)** - Compliance and certifications

---

**Last Updated:** October 2025
