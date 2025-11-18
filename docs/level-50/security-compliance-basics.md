---
layout: default
title: Security & Compliance Basics
parent: Level 50 - Prerequisites
nav_order: 6
description: "Essential security principles and compliance frameworks for cloud computing"
---

# Security & Compliance Basics

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

Security and compliance are fundamental considerations in cloud computing. Understanding basic security principles and compliance frameworks is essential for making informed decisions about cloud adoption and ensuring appropriate protection of organizational assets and data.

## Core Security Principles

### The CIA Triad

The foundation of information security rests on three core principles:

**Confidentiality**
- Ensures information is accessible only to authorized individuals
- Protects sensitive data from unauthorized disclosure
- Implemented through access controls, encryption, and authentication

**Integrity**
- Ensures information remains accurate, complete, and unaltered
- Protects against unauthorized modification or destruction
- Implemented through checksums, digital signatures, and version control

**Availability**
- Ensures information and systems are accessible when needed
- Protects against disruption of service or access
- Implemented through redundancy, backup systems, and disaster recovery

### Defense in Depth

**Layered Security Approach**
Multiple layers of security controls provide better protection than any single control:

```text
Defense in Depth Layers:
├── Physical Security (Data centers, access controls)
├── Network Security (Firewalls, VPNs, segmentation)
├── Endpoint Security (Antivirus, device management)
├── Application Security (Secure coding, testing)
├── Data Security (Encryption, classification)
├── Identity Security (Authentication, authorization)
└── Administrative Security (Policies, procedures, training)
```

### Principle of Least Privilege

**Minimum Required Access**
- Users receive only the minimum permissions necessary for their role
- Reduces risk of unauthorized access or accidental damage
- Regular review and adjustment of permissions
- Time-bound access for temporary requirements

### Zero Trust Security Model

**Never Trust, Always Verify**
- Assumes no user or device is inherently trustworthy
- Continuous verification of identity and device state
- Micro-segmentation of network resources
- Conditional access based on risk assessment

## Identity and Access Management (IAM)

### Authentication vs. Authorization

**Authentication (Who are you?)**
- Verifies the identity of a user, device, or system
- Methods include passwords, multi-factor authentication, biometrics
- Ensures only legitimate users can access systems

**Authorization (What can you do?)**
- Determines what authenticated users are allowed to access
- Based on roles, permissions, and policies
- Controls actions users can perform on resources

### Multi-Factor Authentication (MFA)

**Something You Know + Something You Have + Something You Are**

**Knowledge Factors (Something You Know):**
- Passwords
- PINs
- Security questions

**Possession Factors (Something You Have):**
- Mobile phones
- Hardware tokens
- Smart cards

**Inherence Factors (Something You Are):**
- Fingerprints
- Facial recognition
- Voice patterns

### Role-Based Access Control (RBAC)

**Permissions Based on Job Function**
- Users assigned to roles based on responsibilities
- Roles have predefined permissions
- Simplifies access management at scale
- Easier compliance and audit processes

**Example RBAC Structure:**

```text
Healthcare Organization:
├── Doctor Role
│   ├── Read patient records
│   ├── Update patient records
│   └── Prescribe medications
├── Nurse Role
│   ├── Read patient records
│   ├── Update vitals
│   └── View medication schedules
└── Administrator Role
    ├── Manage user accounts
    ├── System configuration
    └── Audit log access
```

## Data Protection Fundamentals

### Data Classification

**Organizing Data by Sensitivity Level**

**Public Data**
- No harm if disclosed
- Marketing materials, published reports
- No special protection required

**Internal Data**
- Meant for internal use only
- Business processes, internal communications
- Basic access controls required

**Confidential Data**
- Could cause harm if disclosed
- Financial information, strategic plans
- Enhanced protection and access controls

**Restricted Data**
- Severe damage if disclosed
- Personal information, trade secrets
- Highest level of protection required

### Data Encryption

**Encryption In Transit**
- Protects data while moving between systems
- Uses protocols like TLS/SSL, IPsec
- Prevents interception during transmission

**Encryption At Rest**
- Protects stored data
- Encrypts files, databases, backups
- Protects against physical theft or unauthorized access

**Key Management**
- Secure generation, storage, and rotation of encryption keys
- Separation of keys from encrypted data
- Hardware security modules (HSMs) for high-value keys

### Data Loss Prevention (DLP)

**Preventing Unauthorized Data Disclosure**
- Monitors data movement and usage
- Identifies sensitive data patterns
- Blocks or alerts on policy violations
- Protects against accidental or malicious data leaks

## Network Security Basics

### Firewalls

**Network Traffic Control**
- Controls traffic based on security rules
- Can be hardware-based or software-based
- Monitors incoming and outgoing connections
- First line of defense against network attacks

### Virtual Private Networks (VPNs)

**Secure Remote Access**
- Creates encrypted tunnel over public networks
- Enables secure remote work capabilities
- Protects data transmission from remote locations
- Site-to-site or client-to-site configurations

### Network Segmentation

**Isolating Network Resources**
- Divides network into smaller, isolated segments
- Limits lateral movement in case of breach
- Provides better control and monitoring
- Reduces blast radius of security incidents

## Common Security Threats

### Cyber Attack Categories

**Malware**
- Viruses, worms, trojans, ransomware
- Designed to damage or gain unauthorized access
- Delivered through email, websites, or removable media
- Mitigation: Antivirus, patching, user education

**Phishing**
- Fraudulent attempts to obtain sensitive information
- Often disguised as trustworthy communications
- Email, SMS, or voice-based attacks
- Mitigation: User training, email filtering, MFA

**Social Engineering**
- Manipulating people to divulge information or perform actions
- Exploits human psychology rather than technical vulnerabilities
- Can be in-person, over phone, or through digital channels
- Mitigation: Security awareness training, verification procedures

**Insider Threats**
- Security risks from people within the organization
- Can be malicious or accidental
- Access to systems and data makes detection difficult
- Mitigation: Background checks, access controls, monitoring

### Cloud-Specific Security Considerations

**Shared Responsibility Model**
- Clear understanding of who secures what
- Provider secures infrastructure, customer secures their data and applications
- Responsibilities vary by service model (IaaS, PaaS, SaaS)

**Data Location and Movement**
- Understanding where data is stored and processed
- Compliance with data residency requirements
- Control over data movement between regions

**Account and Access Management**
- Securing cloud service accounts
- Managing multiple user identities and permissions
- Integration with existing identity systems

## Compliance Frameworks Overview

### What is Compliance?

**Adherence to Rules and Regulations**
- Meeting legal, regulatory, and industry requirements
- Following established standards and best practices
- Demonstrating due diligence in risk management
- Avoiding penalties and maintaining business reputation

### Major Compliance Frameworks

**SOC 2 (Service Organization Control 2)**
- Focuses on security, availability, processing integrity, confidentiality, privacy
- Relevant for service providers handling customer data
- Annual audit process with detailed reporting
- Trust Services Criteria framework

**ISO 27001**
- International standard for information security management
- Risk-based approach to security management
- Continuous improvement methodology
- Global recognition and acceptance

**GDPR (General Data Protection Regulation)**
- European regulation for data protection and privacy
- Applies to organizations handling EU personal data
- Significant penalties for non-compliance
- Focus on individual rights and consent

**HIPAA (Health Insurance Portability and Accountability Act)**
- US regulation for healthcare data protection
- Protects patient health information (PHI)
- Administrative, physical, and technical safeguards
- Applicable to healthcare providers, payers, clearinghouses

**PCI DSS (Payment Card Industry Data Security Standard)**
- Requirements for organizations handling credit card data
- Twelve core requirements across six categories
- Regular assessment and compliance validation
- Reduces risk of data breaches in payment processing

### Compliance in Cloud Computing

**Shared Compliance Responsibility**
- Cloud providers often achieve compliance certifications
- Customers responsible for compliance of their specific use
- Understanding inherited vs. customer-managed controls
- Regular assessment and validation required

**Compliance Benefits of Cloud**
- Professional-grade security controls
- Regular third-party audits and certifications
- Automated compliance monitoring and reporting
- Cost-effective access to compliant infrastructure

## Risk Management Principles

### Risk Assessment Process

**Risk Identification**
- Identifying potential threats and vulnerabilities
- Understanding assets and their value
- Considering likelihood and impact of risks
- Documenting risk scenarios and dependencies

**Risk Analysis**
- Quantitative and qualitative risk assessment
- Calculating potential impact and probability
- Prioritizing risks based on severity
- Understanding risk interdependencies

**Risk Treatment Options**
- **Accept**: Acknowledge and monitor low-impact risks
- **Avoid**: Eliminate activities that create unacceptable risks
- **Mitigate**: Implement controls to reduce risk
- **Transfer**: Use insurance or third-party services

### Business Continuity and Disaster Recovery

**Business Impact Analysis**
- Identifying critical business processes
- Understanding recovery time objectives (RTO)
- Defining recovery point objectives (RPO)
- Calculating costs of downtime

**Disaster Recovery Planning**
- Backup and recovery procedures
- Alternative processing sites
- Communication plans and procedures
- Regular testing and plan updates

**High Availability Design**
- Redundant systems and components
- Load balancing and failover mechanisms
- Geographic distribution of resources
- Monitoring and automated response

## Security Governance

### Policies and Procedures

**Security Policies**
- High-level statements of management intent
- Define acceptable use and behavior
- Establish accountability and responsibilities
- Regular review and updates required

**Procedures and Standards**
- Detailed step-by-step instructions
- Technical implementation guidelines
- Specific requirements and configurations
- Support consistent implementation

### Security Awareness and Training

**User Education Programs**
- Regular security awareness training
- Phishing simulation exercises
- Incident reporting procedures
- Role-specific security training

**Continuous Improvement**
- Regular assessment of security posture
- Lessons learned from incidents
- Updates based on threat landscape changes
- Feedback from audits and assessments

## Cloud Security Best Practices

### Account Security

**Strong Authentication**
- Complex passwords or passphrases
- Multi-factor authentication enabled
- Regular password updates
- Secure password storage

**Access Management**
- Regular review of user accounts and permissions
- Prompt removal of access for departed employees
- Time-bound access for temporary requirements
- Separation of administrative and user accounts

### Data Protection

**Encryption Strategy**
- Encrypt sensitive data at rest and in transit
- Proper key management and rotation
- Use of customer-managed keys where required
- Regular testing of decryption procedures

**Backup and Recovery**
- Regular automated backups
- Geographically distributed backup storage
- Regular testing of recovery procedures
- Documentation of backup and recovery processes

### Monitoring and Incident Response

**Security Monitoring**
- Continuous monitoring of security events
- Automated alerting for suspicious activities
- Log collection and analysis
- Regular security assessments and penetration testing

**Incident Response Planning**
- Defined incident response procedures
- Clear roles and responsibilities
- Communication plans and escalation procedures
- Post-incident review and improvement processes

## Industry-Specific Security Considerations

### Healthcare

**HIPAA Compliance Requirements:**
- Administrative safeguards (policies, training)
- Physical safeguards (facility access, workstation use)
- Technical safeguards (access control, audit controls, integrity)
- Business associate agreements for third parties

### Financial Services

**Regulatory Requirements:**
- SOX compliance for public companies
- PCI DSS for payment processing
- GLBA for financial privacy
- Basel III for risk management

### Government

**Security Clearance Levels:**
- FedRAMP compliance for cloud services
- FISMA requirements for federal systems
- ITAR compliance for defense-related data
- State and local government requirements

## Summary

Security and compliance are foundational to successful cloud adoption. Key principles include:

- **CIA Triad**: Confidentiality, Integrity, Availability
- **Defense in Depth**: Multiple layers of security controls
- **Identity and Access Management**: Authentication and authorization
- **Data Protection**: Classification, encryption, and loss prevention
- **Compliance Frameworks**: Understanding regulatory requirements
- **Risk Management**: Assessment, treatment, and continuous monitoring

Understanding these basics prepares you for more advanced security topics and helps ensure appropriate protection in cloud environments.

## Next Steps

1. ✅ Review security principles and their applications
2. ✅ Consider how these concepts apply to your organization
3. ✅ Continue to [Data Protection Principles](data-protection-principles.md)
4. ✅ Study [Compliance Frameworks](compliance-frameworks.md)
5. ✅ Review [Identity and Access Basics](identity-access-basics.md)
6. ✅ Complete [Module 2 Knowledge Check](security-compliance-knowledge-check.md)

---

## Additional Resources

- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [Cloud Security Alliance (CSA)](https://cloudsecurityalliance.org/)
- [Microsoft Security Documentation](https://learn.microsoft.com/en-us/security/)
- [AWS Security Best Practices](https://aws.amazon.com/security/security-resources/)

---

**Last Updated:** November 2025
