---
layout: default
title: Cloud Service Models
parent: Module 1 - Cloud Computing Fundamentals
grand_parent: Level 50 - Prerequisites
nav_order: 2
description: "Understanding IaaS, PaaS, and SaaS with practical examples"
---

# Cloud Service Models

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

Cloud service models define the level of control and responsibility between cloud providers and customers. Understanding these models is crucial for selecting appropriate cloud solutions and understanding shared responsibility boundaries.

## The Three Primary Service Models

### Infrastructure as a Service (IaaS)

**Definition:** Provides virtualized computing infrastructure over the internet, including servers, storage, and networking resources.

**What You Get:**
- Virtual machines
- Storage volumes
- Network infrastructure
- Load balancers
- Firewalls and security groups

**What You Manage:**
- Operating systems
- Middleware
- Runtime environments
- Applications
- Data
- Security configurations

**Examples:**
- **Microsoft Azure:** Virtual Machines, Azure Storage, Virtual Networks
- **Amazon Web Services:** EC2, S3, VPC
- **Google Cloud:** Compute Engine, Cloud Storage

**Use Cases:**
- Hosting websites and web applications
- Development and testing environments
- Big data analysis
- Backup and disaster recovery

**Business Scenario:**
A software development company needs flexible computing resources for their development teams. Instead of purchasing physical servers, they use Azure Virtual Machines to spin up development environments on-demand, paying only for resources used.

### Platform as a Service (PaaS)

**Definition:** Provides a platform allowing customers to develop, run, and manage applications without dealing with underlying infrastructure complexity.

**What You Get:**
- Development frameworks
- Database management systems
- Web servers
- Operating system maintenance
- Infrastructure scaling
- Development tools

**What You Manage:**
- Applications
- Data
- Application configurations
- User access management

**Examples:**
- **Microsoft Azure:** App Service, Azure SQL Database, Azure Functions
- **Google Cloud:** Cloud Run, Cloud SQL
- **Heroku:** Application hosting platform

**Use Cases:**
- Web application development
- API development and hosting
- Database applications
- Microservices architecture

**Business Scenario:**
An e-commerce startup wants to focus on building their application, not managing servers. They use Azure App Service to deploy their web application, letting Microsoft handle server maintenance, scaling, and security updates.

### Software as a Service (SaaS)

**Definition:** Delivers software applications over the internet, on a subscription basis, fully managed by the service provider.

**What You Get:**
- Complete applications
- Automatic updates
- Multi-device access
- Data backup and recovery
- 24/7 availability
- Built-in security

**What You Manage:**
- User data and content
- User access permissions
- Application configuration settings
- Integration with other systems

**Examples:**
- **Microsoft 365:** Word, Excel, PowerPoint, Teams, SharePoint
- **Salesforce:** CRM applications
- **ServiceNow:** IT service management
- **Slack:** Team collaboration

**Use Cases:**
- Email and collaboration
- Customer relationship management
- Human resources management
- Accounting and finance

**Business Scenario:**
A consulting firm needs professional email and collaboration tools. They subscribe to Microsoft 365, giving all employees access to Outlook, Teams, and SharePoint without needing to install or maintain any servers.

## Service Model Comparison

| Aspect | IaaS | PaaS | SaaS |
|--------|------|------|------|
| **Control** | High | Medium | Low |
| **Flexibility** | Maximum | Moderate | Limited |
| **Management Overhead** | High | Medium | Low |
| **Time to Deploy** | Days/Weeks | Hours/Days | Minutes |
| **Scalability Control** | Manual | Automatic | Automatic |
| **Customization** | Full | Moderate | Limited |
| **Cost Predictability** | Variable | Moderate | Predictable |

## Shared Responsibility Model

Understanding who is responsible for what in each service model:

### IaaS Responsibilities

**Customer Responsible For:**
- Operating system updates and patches
- Application security
- Network configuration
- Access management
- Data encryption
- Backup and recovery

**Provider Responsible For:**
- Physical security
- Hardware maintenance
- Network infrastructure
- Hypervisor security
- Power and cooling

### PaaS Responsibilities

**Customer Responsible For:**
- Application code security
- Data protection
- User access management
- Application configuration
- Identity management

**Provider Responsible For:**
- Operating system maintenance
- Runtime environment security
- Platform scaling
- Infrastructure security
- Network security

### SaaS Responsibilities

**Customer Responsible For:**
- Data classification
- User access management
- Device management
- Account management

**Provider Responsible For:**
- Application security
- Infrastructure security
- Platform maintenance
- Data backup
- Network security

## Choosing the Right Service Model

### Decision Framework

**Choose IaaS When:**
- You need maximum control over the environment
- You have existing applications that require specific configurations
- You have specialized networking or security requirements
- You want to migrate existing on-premises workloads with minimal changes

**Choose PaaS When:**
- You want to focus on application development, not infrastructure
- You need rapid application deployment and scaling
- You're building cloud-native applications
- You want to leverage managed databases and services

**Choose SaaS When:**
- You need immediate access to proven applications
- You have limited IT resources for maintenance
- You want predictable, subscription-based pricing
- You need to enable remote work and collaboration

### Cost Considerations

**IaaS Costs:**

```text
Base VM: $100/month
+ Storage: $50/month
+ Networking: $25/month
+ Management overhead: $200/month (staff time)
Total: $375/month
```

**PaaS Costs:**

```text
App Service: $200/month
+ Database: $150/month
+ Minimal management: $50/month (staff time)
Total: $400/month
```

**SaaS Costs:**

```text
Microsoft 365 (per user): $22/month
+ No management overhead
Total: $22/month per user
```

## Hybrid and Multi-Service Approaches

### Combining Service Models

Many organizations use multiple service models simultaneously:

**Example Architecture:**
- **SaaS:** Microsoft 365 for productivity and collaboration
- **PaaS:** Azure App Service for custom web applications
- **IaaS:** Virtual machines for legacy applications

**Benefits:**
- Optimize each workload for appropriate service model
- Gradual cloud migration strategy
- Balance control and convenience

### Real-World Implementation

**Healthcare Organization Example:**

```text
SaaS Layer:
├── Microsoft 365 (Email, collaboration)
├── Salesforce (Patient CRM)
└── ServiceNow (IT service management)

PaaS Layer:
├── Azure App Service (Patient portal)
├── Azure SQL Database (Patient records)
└── Azure Functions (Data processing)

IaaS Layer:
├── Virtual Machines (Legacy applications)
├── Azure Storage (Medical imaging)
└── Virtual Networks (Secure connectivity)
```

## Service Model Evolution

### Traditional to Cloud Journey

**Phase 1: Lift and Shift (IaaS)**
- Move existing applications to cloud VMs
- Minimal application changes
- Quick migration with immediate cost benefits

**Phase 2: Modernization (PaaS)**
- Refactor applications for cloud-native services
- Leverage managed databases and platforms
- Improve scalability and operational efficiency

**Phase 3: Innovation (SaaS + Custom PaaS)**
- Adopt best-of-breed SaaS solutions
- Build differentiated capabilities on PaaS
- Focus on business value creation

## Industry-Specific Examples

### Financial Services

**IaaS:** High-performance computing for risk calculations
**PaaS:** Mobile banking applications on managed platforms
**SaaS:** Customer relationship management and compliance reporting

### Manufacturing

**IaaS:** Simulation and modeling workloads requiring specific configurations
**PaaS:** IoT data processing and analytics platforms
**SaaS:** Enterprise resource planning and supply chain management

### Education

**IaaS:** Research computing environments
**PaaS:** Learning management system platforms
**SaaS:** Student information systems and collaboration tools

## Security Considerations by Service Model

### IaaS Security Requirements

- Network security group configuration
- Operating system hardening
- Vulnerability management
- Access control implementation
- Data encryption in transit and at rest

### PaaS Security Requirements

- Application-level security
- API security and authentication
- Data protection and privacy
- Integration security
- Identity and access management

### SaaS Security Requirements

- User access management
- Data governance and classification
- Single sign-on implementation
- Device management and compliance
- Third-party risk assessment

## Common Pitfalls and Best Practices

### IaaS Pitfalls

**Common Mistakes:**
- Under-estimating management overhead
- Poor resource sizing leading to cost overruns
- Inadequate backup and disaster recovery planning

**Best Practices:**
- Implement infrastructure as code
- Use monitoring and alerting
- Plan for automatic scaling
- Regular security assessments

### PaaS Pitfalls

**Common Mistakes:**
- Vendor lock-in without exit strategy
- Insufficient application monitoring
- Poor integration architecture

**Best Practices:**
- Design for portability where possible
- Implement comprehensive logging
- Use API-first architecture
- Plan for service limits and quotas

### SaaS Pitfalls

**Common Mistakes:**
- Inadequate data governance
- Poor user training and adoption
- Insufficient integration planning

**Best Practices:**
- Establish data governance policies
- Invest in user training and change management
- Plan integrations early
- Regular security and compliance reviews

## Summary

Understanding cloud service models is fundamental to making informed decisions about cloud adoption:

- **IaaS** provides maximum control and flexibility with higher management overhead
- **PaaS** balances control and convenience, enabling rapid application development
- **SaaS** offers immediate value with minimal management requirements

Most organizations benefit from a multi-model approach, selecting the appropriate service model for each workload based on requirements, constraints, and strategic objectives.

## Next Steps

1. ✅ Review service model characteristics and use cases
2. ✅ Consider which models apply to your organization's needs
3. ✅ Continue to [Cloud Deployment Models](cloud-deployment-models.md)
4. ✅ Complete the [Knowledge Check](cloud-computing-knowledge-check.md)

---

## Additional Resources

- [Azure Service Models Overview](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/considerations/fundamental-concepts)
- [AWS Service Models Explained](https://aws.amazon.com/types-of-cloud-computing/)
- [Google Cloud Service Models](https://cloud.google.com/docs/overview/cloud-platform-services)

---

**Last Updated:** November 2025
