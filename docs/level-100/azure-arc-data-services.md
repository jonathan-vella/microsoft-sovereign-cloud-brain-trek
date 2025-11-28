---
layout: default
title: Azure Arc Data Services
parent: Module 4 - Azure Arc Introduction
nav_order: 4.3
---

# Azure Arc-Enabled Data Services

{: .no_toc }

## Table of Contents

{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What are Arc Data Services?

Azure Arc-enabled Data Services bring Azure database services to any infrastructure - on-premises, edge, or any public cloud. Get a managed database experience with evergreen updates, elastic scale, and Azure-consistent management while keeping data on-premises.

**Available Services:**

- **Azure SQL Managed Instance:** Fully compatible SQL Server with PaaS benefits
- **PostgreSQL Hyperscale:** Scalable PostgreSQL with Citus extension

**[← Back to Azure Arc Introduction](azure-arc-intro)**

---

## Available Services

### Azure SQL Managed Instance

**What It Is:**

- SQL Server compatibility (99%+)
- Managed instance with automatic backups
- Built-in high availability
- Evergreen (always up-to-date)
- Running on your infrastructure

**Key Features:**

- T-SQL compatibility
- Linked servers
- CLR, SQL Agent, Database Mail
- Full-text search
- Elastic scale (Enterprise tier)
- Point-in-time restore

**Licensing:**

- Pay-as-you-go (Azure meter)
- Bring-your-own-license (BYOL)
- Azure Hybrid Benefit

### PostgreSQL Hyperscale

**What It Is:**

- PostgreSQL with Citus extension
- Horizontal scaling (sharding)
- Distributed tables and queries
- Managed service experience

**Key Features:**

- Scale out reads and writes
- Parallel query execution
- Real-time analytics
- Multi-tenant applications
- High throughput ingestion

**Use Cases:**

- Multi-tenant SaaS applications
- Real-time analytics dashboards
- Time-series data
- High-throughput OLTP

---

## Deployment Modes

### Directly Connected Mode

**Characteristics:**

- Continuous or regular connection to Azure
- Billing and usage data uploaded to Azure
- Azure portal management available
- Automatic updates

**Requirements:**

- Outbound HTTPS to Azure
- Azure subscription
- Upload to Azure every 24 hours

**Benefits:**

- Simplest to manage
- Full Azure portal experience
- Automated billing
- Latest features first

### Indirectly Connected Mode (Retired)

{: .warning }
> **⚠️ Retired Feature**
> Indirectly Connected mode was retired in September 2025. For disconnected scenarios requiring Arc-enabled data services, use [Azure Local with Disconnected Operations](azure-local-disconnected-mode.md) which provides a local control plane with Azure portal experience.

**Historical Context:**

This mode previously supported air-gapped environments with manual data export/import. Organizations requiring disconnected database services should now evaluate:

- **Azure Local Disconnected Operations** — Local Azure portal and management
- **Traditional SQL Server/PostgreSQL** — Self-managed databases on disconnected infrastructure

---

## Managed Database Experience Anywhere

### What "Managed" Means

**Automated Operations:**

- Backups and restore
- High availability and failover
- Patch management and updates
- Performance monitoring
- Resource scaling

**Reduced Admin Overhead:**

- No OS patching
- No infrastructure management
- Simplified disaster recovery
- Built-in monitoring

### Elastic Scale and High Availability

**Scale Up/Down:**

- Adjust CPU and memory dynamically
- No downtime for scaling
- Pay only for what you use

**Scale Out (Hyperscale):**

- Add read replicas
- Shard data across nodes
- Parallel query execution

**High Availability:**

- Always-On Availability Groups (SQL MI)
- Synchronous replication
- Automatic failover (< 30 seconds)
- Built-in health monitoring

---

## Billing Model

### Pay-As-You-Go

**How It Works:**

- Billed based on vCore-hours consumed
- Separate pricing for General Purpose and Business Critical tiers
- Storage charged separately

**Pricing Example (SQL MI):**

- General Purpose: ~$0.40/vCore/hour
- Business Critical: ~$1.00/vCore/hour
- Storage: ~$0.11/GB/month

### Bring Your Own License (BYOL)

**Requirements:**

- Active SQL Server license with Software Assurance
- Azure Hybrid Benefit enrollment

**Savings:**

- Up to 55% savings vs. pay-as-you-go
- License mobility (move between environments)

**Combined with Azure Hybrid Benefit:**

- Use existing on-premises licenses
- Add free 180 days of Software Assurance
- Further cost reduction

---

## Migration from Traditional Databases

### Assessment

**Tools:**

- Azure Migrate for database assessment
- Data Migration Assistant (DMA)
- Azure SQL Migration extension

**Assessment Output:**

- Compatibility issues
- Feature parity analysis
- Performance baseline
- Sizing recommendations

### Migration Methods

**1. Backup and Restore:**

- For offline migrations
- Full/diff/log backups
- Point-in-time recovery
- Minimal downtime: Hours

**2. Log Shipping:**

- For near-zero downtime migrations
- Continuous log replay
- Manual cutover
- Minimal downtime: Minutes

**3. Distributed Availability Group (SQL MI):**

- Replicate from on-premises SQL Server
- Bidirectional replication
- Minimal downtime migration
- Rollback capability

**4. Azure Database Migration Service:**

- Online migrations
- Minimal downtime
- Automated process
- Change data capture (CDC)

### Post-Migration Validation

**Performance:**

- Benchmark queries
- Compare execution plans
- Validate throughput

**Functionality:**

- Test all application features
- Validate integrations
- Confirm backup/restore

**Compliance:**

- Security controls
- Audit logging
- Encryption validation

---

## Security and Encryption

**Encryption at Rest:**

- Transparent Data Encryption (TDE) enabled by default
- AES-256 encryption
- Customer-managed keys (CMK) option

**Encryption in Transit:**

- TLS 1.2+ for all connections
- Force encryption option
- Certificate validation

**Access Control:**

- Azure AD authentication
- SQL authentication
- Role-based access control (RBAC)
- Row-level security (RLS)
- Dynamic data masking (DDM)

**Auditing:**

- SQL audit to local storage or Azure
- Threat detection
- Vulnerability assessment
- Compliance reporting (PCI-DSS, HIPAA, etc.)

---

## Data Residency Guarantees

**Data Stays On-Premises:**

- Database files remain on your infrastructure
- Backups stored locally (or where you choose)
- Query processing happens locally
- No automatic replication to cloud

**Metadata Sent to Azure (Direct Mode):**

- Billing and usage data
- Performance metrics (aggregate)
- Diagnostic logs (optional)
- Configuration metadata

**Compliance:**

- Meets GDPR requirements
- HIPAA compliant
- PCI-DSS ready
- FedRAMP compatible

**Audit Trail:**

- All data movement logged
- Compliance reports available
- Demonstrates data residency

---

## Use Case Scenarios

### Scenario 1: Financial Services Database Modernization

**Challenge:** 100+ SQL Server 2012 databases end of support, but data must stay on-premises.

**Solution:**

- Deploy Arc SQL Managed Instance
- Migrate databases using DMA
- Implement Always-On AG for HA
- Enable TDE and auditing

**Results:**

- Modernized databases without cloud migration
- Pay-as-you-go reduced costs by 40%
- 99.95% availability SLA
- Passed compliance audits
- Reduced admin overhead by 50%

### Scenario 2: Healthcare SaaS Multi-Tenant Application

**Challenge:** SaaS app needs to scale to 1000s of tenants with high performance.

**Solution:**

- Deploy PostgreSQL Hyperscale
- Shard by tenant ID
- Scale to 10+ worker nodes
- Parallel query execution

**Results:**

- 10x query performance improvement
- Seamless scaling to 5000+ tenants
- Sub-second query response times
- Reduced infrastructure costs (better utilization)

### Scenario 3: Retail Point-of-Sale System

**Challenge:** Chain of 500 stores needs local database at each store with central reporting.

**Solution:**

- Deploy SQL MI at each store location
- Local transactions (no cloud dependency)
- Nightly replication to central data warehouse
- Azure portal for monitoring all 500 instances

**Results:**

- Zero downtime from internet outages
- Real-time POS transactions
- Centralized reporting and analytics
- Managed from single pane of glass

---

## Best Practices

**1. Right-Size from the Start:**

- Use assessment tools
- Start with actual workload metrics
- Monitor and adjust

**2. Implement HA from Day 1:**

- Always-On AG for SQL MI
- Multiple coordinator nodes for Hyperscale
- Test failover procedures

**3. Plan for Growth:**

- Size for 2-3 year growth
- Consider scaling options
- Budget for storage growth

**4. Backup Strategy:**

- Define RPO and RTO
- Test restores regularly
- Implement offsite backups

**5. Monitor Proactively:**

- Set up alerts
- Review performance metrics weekly
- Capacity planning

**6. Leverage Azure Hybrid Benefit:**

- Use existing SQL licenses
- Significant cost savings
- License mobility

---

## Cost Considerations

**Total Cost of Ownership:**

**Arc Data Services:**

- Lower than Azure SQL Database for sustained workloads
- Lower than self-managed on-premises (reduced admin)
- Flexible with BYOL

**Example Monthly Cost (SQL MI, 16 vCores):**

**Pay-as-you-go:**

- General Purpose: ~$4,600/month
- Business Critical: ~$11,500/month

**With Azure Hybrid Benefit:**

- General Purpose: ~$2,100/month
- Business Critical: ~$5,200/month

**Break-Even vs. Azure SQL Database:**

- Typically 6-12 months for sustained workloads
- Faster for 24/7 production databases

---

## Troubleshooting

**Deployment Failures:**

- Verify Kubernetes resource availability
- Check storage class configuration
- Validate network connectivity
- Review controller logs

**Performance Issues:**

- Check resource allocation (CPU, memory)
- Review query execution plans
- Validate storage IOPS
- Monitor network latency

**Connectivity Problems:**

- Verify service endpoint configuration
- Check firewall rules
- Validate DNS resolution
- Test from application server

---

## Next Steps

- [Arc Servers →](azure-arc-servers)
- [Arc Kubernetes →](azure-arc-kubernetes)
- [Azure Arc Quiz →](azure-arc-quiz)
- [Back to Arc Overview →](azure-arc-intro)

**External Resources:**

- [Azure Arc-enabled data services docs](https://learn.microsoft.com/en-us/azure/azure-arc/data/)
- [SQL Managed Instance on Arc](https://learn.microsoft.com/en-us/azure/azure-arc/data/managed-instance-overview)
- [PostgreSQL Hyperscale on Arc](https://learn.microsoft.com/en-us/azure/azure-arc/data/overview)

---

**Last Updated:** October 2025
