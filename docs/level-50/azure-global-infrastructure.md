---
layout: default
title: Azure Global Infrastructure
parent: Module 3 - Microsoft Azure Introduction
grand_parent: Level 50 - Prerequisites
nav_order: 3
description: "Azure regions, availability zones, and global infrastructure overview"
---

# Azure Global Infrastructure

## Overview

Azure's global infrastructure enables worldwide deployment with data residency compliance and high availability. This section provides key concepts with references to official documentation.

<details class="diagram-container">
<summary>View Diagram: Azure Global Regions Map</summary>
<div class="diagram-content" markdown="1">

![Azure Global Regions Map](../assets/images/level-100/azure-regions-map.svg)
_Figure: Azure global datacenter regions with EU Data Boundary highlighted_

</div>
</details>

<details class="diagram-container">
<summary>View Diagram: Azure Infrastructure Hierarchy</summary>
<div class="diagram-content" markdown="1">

![Azure Infrastructure Hierarchy](../assets/images/level-50/azure-infrastructure-hierarchy.svg)
_Figure: Azure global infrastructure hierarchy from Geographies to Data Centers_

</div>
</details>

## Key Concepts

### Regions

Geographic areas containing one or more data centers.

**Important Facts:**

- 60+ regions worldwide
- Data residency compliance
- Region-specific service availability
- Disaster recovery pairing

### Availability Zones

Physically separate locations within an Azure region.

**Key Benefits:**

- High availability (99.99% SLA)
- Fault tolerance
- Automatic failover
- Zone-redundant services

### Edge Locations

Points of presence for content delivery and edge computing.

**Use Cases:**

- Content delivery networks (CDN)
- Edge computing scenarios
- Reduced latency for users

## Sovereignty Considerations

### Data Residency

- Choose regions based on compliance requirements
- Understand data replication policies
- Consider cross-border data transfer restrictions

### Government Clouds

- Azure Government (US)
- Azure China
- Regional compliance variations

## Official Resources

### Documentation

- [Azure Global Infrastructure](https://azure.microsoft.com/en-us/explore/global-infrastructure/)
- [Azure Regions](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview)
- [Azure Geographies](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview#azure-regions-with-availability-zones)

### Interactive Tools

- [Azure Region Map](https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/)
- [Azure Speed Test](https://azurespeedtest.azurewebsites.net/)

## Next Steps

Review [Azure Management Tools](azure-management-tools.md) to understand how to manage Azure resources.

---

**Last Updated:** November 2025
