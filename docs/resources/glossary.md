---
layout: default
title: Glossary
nav_order: 2
parent: Resources
description: "Definitions of key terms used throughout the Microsoft Sovereign Cloud Brain Trek program"
---

# Glossary of Terms

{: .no_toc }

A comprehensive glossary of terminology used throughout the Microsoft Sovereign Cloud Brain Trek learning program.

## Table of Contents

{: .no_toc .text-delta }

1. TOC
{:toc}

---

## A

### Air-Gapped

An isolated computing environment with no external network connectivity. Air-gapped systems are physically separated from public networks and the internet, providing the highest level of security for sensitive workloads.

### Azure Arc

A set of technologies that extends Azure management capabilities to on-premises, multi-cloud, and edge environments. Azure Arc enables centralized governance, security, and management of resources regardless of where they run.

### Azure Arc-enabled Data Services

Database services (SQL Managed Instance, PostgreSQL) that can run on any Kubernetes infrastructure while being managed through Azure Arc.

### Azure Arc-enabled Kubernetes

The ability to attach and configure Kubernetes clusters running anywhere to Azure Arc for centralized management, policy enforcement, and GitOps deployments.

### Azure Arc-enabled Servers

Servers running Windows or Linux, whether on-premises or in other clouds, that are registered with Azure Arc for unified management.

### Azure Local

Microsoft's hyperconverged infrastructure (HCI) solution that extends Azure to customer premises. Formerly known as Azure Stack HCI, Azure Local enables running Azure services on-premises while maintaining cloud connectivity for management.

### Azure Policy

A service that enables you to create, assign, and manage policies that enforce rules and effects over your resources, ensuring compliance with corporate standards and service level agreements.

---

## C

### Cloud Operating Model

A framework that defines how an organization manages, governs, and operates cloud resources. It encompasses processes, tools, and organizational structures.

### Compliance Framework

A structured set of guidelines and requirements (such as GDPR, HIPAA, or FedRAMP) that organizations must follow to meet regulatory or industry standards.

### Connected Mode

An operational mode for Azure Local where the cluster maintains continuous connectivity to Azure for management, updates, monitoring, and billing.

### Customer Lockbox

A feature that provides an approval workflow for Microsoft support access to customer data, ensuring customers maintain control over who accesses their resources.

---

## D

### Data Residency

The geographic or jurisdictional location where data is stored and processed. Data residency requirements ensure that data remains within specific boundaries to comply with local regulations.

### Data Sovereignty

The concept that data is subject to the laws and governance structures of the nation or jurisdiction where it is collected or stored.

### Digital Sovereignty

The ability of organizations and nations to control their digital infrastructure, data, and technology assets according to their own governance requirements.

### Disconnected Mode

An operational mode for Azure Local where the cluster operates with limited or intermittent Azure connectivity, requiring periodic synchronization for licensing and updates.

---

## E

### Edge Computing

Computing infrastructure and services deployed at the network edge, closer to where data is generated and consumed, to reduce latency and enable local processing.

### Edge RAG

Edge Retrieval-Augmented Generation — a pattern for deploying AI systems on-premises that combine large language models with local document retrieval capabilities while maintaining data sovereignty.

### Embedding

A numerical representation of text or other data that captures semantic meaning, used in RAG systems to find relevant documents for AI queries.

---

## F

### FedRAMP

Federal Risk and Authorization Management Program — a US government program that provides a standardized approach to security assessment, authorization, and continuous monitoring for cloud products and services.

---

## G

### GDPR

General Data Protection Regulation — European Union regulation on data protection and privacy that applies to organizations handling EU citizens' data.

### GitOps

An operational framework that uses Git repositories as the single source of truth for declarative infrastructure and application configuration.

---

## H

### HIPAA

Health Insurance Portability and Accountability Act — US legislation that provides data privacy and security provisions for safeguarding medical information.

### Hybrid Cloud

A computing environment that combines on-premises infrastructure with public cloud services, allowing data and applications to be shared between them.

### Hyperconverged Infrastructure (HCI)

A software-defined IT infrastructure that virtualizes computing, storage, and networking in a single system, typically running on commodity hardware.

---

## I

### Infrastructure as Code (IaC)

The practice of managing and provisioning infrastructure through machine-readable definition files rather than physical hardware configuration or interactive configuration tools.

### ITAR

International Traffic in Arms Regulations — US regulatory regime that controls the export and import of defense-related articles and services.

---

## K

### Kubernetes

An open-source container orchestration platform that automates deployment, scaling, and management of containerized applications.

---

## L

### Landing Zone

A pre-configured environment in the cloud that provides the foundational infrastructure, security controls, and governance needed to deploy workloads.

### Large Language Model (LLM)

An AI model trained on vast amounts of text data that can understand and generate human-like text. Examples include GPT-4 and Phi-3.

---

## M

### Managed Identity

An Azure feature that provides an automatically managed identity for applications to use when connecting to resources that support Azure Active Directory authentication.

### Microsoft Entra ID

Microsoft's cloud-based identity and access management service (formerly Azure Active Directory).

---

## N

### National/Regional Cloud

A cloud deployment that operates within specific geographic boundaries and may be operated by local partners to meet national sovereignty requirements.

---

## O

### Operational Sovereignty

Control over the operations, maintenance, and support of IT infrastructure, ensuring that operational personnel and processes meet specific jurisdictional or security requirements.

---

## P

### PCI DSS

Payment Card Industry Data Security Standard — a set of security standards designed to ensure that companies that accept, process, store, or transmit credit card information maintain a secure environment.

### Policy-as-Code

The practice of defining and managing policies through code, enabling version control, testing, and automated enforcement.

### Private Cloud

Cloud infrastructure provisioned for exclusive use by a single organization, providing greater control over data, security, and compliance.

---

## R

### RBAC

Role-Based Access Control — an approach to restricting system access based on the roles of individual users within an organization.

### Retrieval-Augmented Generation (RAG)

An AI architecture that enhances large language models by retrieving relevant information from external sources (like document stores) to provide more accurate and contextual responses.

---

## S

### Sovereign Controls

Technical and operational measures implemented to ensure that cloud resources comply with sovereignty requirements, including data residency, access controls, and encryption.

### Sovereign Landing Zone (SLZ)

An architectural pattern that extends Azure Landing Zones with additional controls and configurations specifically designed to meet sovereignty requirements.

### Sovereign Private Cloud

A cloud environment that combines private cloud isolation with sovereign controls for maximum data protection and regulatory compliance.

### Sovereign Public Cloud

Azure public cloud regions enhanced with sovereign controls, including confidential computing, customer-managed keys, and restricted operations.

---

## T

### Tenant

In cloud computing, a logical isolation unit that represents an organization's dedicated instance within a shared infrastructure.

### Trusted Launch

A security feature for Azure VMs that protects against advanced and persistent attack techniques by enabling secure boot, vTPM, and boot integrity monitoring.

---

## V

### Vector Database

A database optimized for storing and querying high-dimensional vectors (embeddings), commonly used in RAG systems for semantic search.

### Virtual Machine (VM)

An emulation of a computer system that provides the functionality of a physical computer, running on top of a hypervisor.

---

## W

### Workload

An application, service, or capability deployed in a cloud environment, along with its associated resources and configurations.

---

## Z

### Zero Trust

A security model based on the principle of "never trust, always verify" that requires strict identity verification for every person and device trying to access resources, regardless of their location.

---

## Additional Resources

- **[Microsoft Terminology Collection](https://www.microsoft.com/en-us/language)** - Official Microsoft terminology
- **[Cloud Computing Terms](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/)** - Azure glossary
- **[NIST Cloud Computing Glossary](https://csrc.nist.gov/glossary)** - Government standards terminology

---

## Next Steps

- **[Return to Resources](./)**
- **[Start Learning Path](../level-50/)**
