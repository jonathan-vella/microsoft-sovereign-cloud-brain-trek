---
title: Azure Arc data services
description: "Understand current Azure Arc data services facts, including SQL Managed Instance direct connectivity and retired PostgreSQL and indirect modes."
lastVerified: 2026-10-02
sidebar:
  order: 4
---

Azure Arc data services bring selected Azure data service patterns to Kubernetes infrastructure outside Azure. Today that means one service: Azure Arc-enabled SQL Managed Instance, generally available in select regions and supported only in direct connectivity mode.

Arc data services used to include two services and two connectivity modes. Azure Arc-enabled PostgreSQL server was retired on July 14, 2025, and indirectly connected mode for Azure Arc-enabled data services retired in September 2025 ([release notes](https://learn.microsoft.com/azure/azure-arc/data/release-notes), [connectivity mode and requirements](https://learn.microsoft.com/azure/azure-arc/data/connectivity)).

## What remains current

| Area | Current status | What to remember |
|---|---|---|
| Azure Arc-enabled SQL Managed Instance | Generally available in select regions ([validation program](https://learn.microsoft.com/azure/azure-arc/data/validation-program)) | Runs on Kubernetes infrastructure and is managed through Azure Arc |
| Direct connectivity mode | Required for Arc-enabled data services ([connectivity](https://learn.microsoft.com/azure/azure-arc/data/connectivity)) | The data controller has direct Azure connectivity for management, monitoring, and billing flows |
| Indirect connectivity mode | Retired in September 2025 ([release notes](https://learn.microsoft.com/azure/azure-arc/data/release-notes#september-2025)) | Do not design new deployments around manual upload or disconnected indirect mode |
| Azure Arc-enabled PostgreSQL server | Retired on July 14, 2025 ([release notes](https://learn.microsoft.com/azure/azure-arc/data/release-notes)) | Remove it from current solution options |
| Grafana and OpenSearch dashboards for Arc SQL MI | Removed in August 2025 ([release notes](https://learn.microsoft.com/azure/azure-arc/data/release-notes)) | Do not include those dashboards in current operating models |

## SQL Managed Instance enabled by Azure Arc

SQL Managed Instance enabled by Azure Arc is a managed SQL service that runs on Kubernetes infrastructure and is exposed through Azure Arc. It targets cases where an organization wants a managed SQL experience while the database runs outside Azure.

At L100 depth, focus on these points:

- The service is not retired. Microsoft lists SQL Managed Instance enabled by Azure Arc as generally available in select regions on the Arc-enabled data services Kubernetes validation page.
- It now uses direct connectivity mode only. Indirect mode is retired.
- Database files and query processing run on the target infrastructure, while Azure connectivity supports management, monitoring, and billing.
- The service is distinct from SQL Server enabled by Azure Arc, which connects existing SQL Server instances running on Windows or Linux machines.

## Direct connectivity mode

Direct connectivity mode connects the Arc data controller directly to Azure. Microsoft states that direct mode is now the only supported connectivity mode for Azure Arc-enabled data services ([connectivity mode and requirements](https://learn.microsoft.com/azure/azure-arc/data/connectivity)).

Direct connectivity supports Azure portal inventory and management flows, Azure billing, usage reporting, and Azure-side monitoring integrations. Because those flows require connectivity, a design that cannot allow direct Azure connectivity should not assume that Arc-enabled SQL Managed Instance can use the old indirect model.

For sovereign cloud architecture, separate two questions:

1. Where do the database files and query processing run?
2. Which management, billing, monitoring, and diagnostic data flows go to Azure?

The first answer may be "local infrastructure." The second answer depends on direct mode configuration and any services you attach.

## Retired PostgreSQL service

Azure Arc-enabled PostgreSQL server was a separate Arc data service. It was retired on July 14, 2025 ([release notes](https://learn.microsoft.com/azure/azure-arc/data/release-notes)) and is no longer an option, including the PostgreSQL Hyperscale on Arc name that appears in older diagrams.

For existing PostgreSQL needs, choose a current PostgreSQL platform outside this module's scope. Options might include self-managed PostgreSQL, Azure Database for PostgreSQL in Azure, or another supported database platform, depending on sovereignty and connectivity requirements. Check the target platform against current Microsoft documentation before you commit to it.

## What the retirements mean

If an existing environment still refers to indirect mode or Arc-enabled PostgreSQL, treat it as a migration and risk review topic.

- Remove indirect mode from new designs.
- Check existing Arc data services deployments for their connectivity mode.
- Plan SQL Managed Instance enabled by Azure Arc around direct mode.
- Remove Arc-enabled PostgreSQL server from current reference architectures.
- Replace old Grafana and OpenSearch dashboard guidance for Arc SQL MI with current monitoring guidance.

These retirements also affect sovereignty messaging. A design can still keep database files local, but it cannot claim an Arc data services deployment is supported without direct Azure connectivity unless a separate, current Microsoft pattern says so.

## SQL Server enabled by Azure Arc

SQL Server enabled by Azure Arc is related, but it is not the same thing as Azure Arc-enabled SQL Managed Instance. SQL Server enabled by Azure Arc connects existing SQL Server instances on Windows or Linux machines to Azure by using the Connected Machine agent and the Azure Extension for SQL Server ([SQL Server enabled by Azure Arc](https://learn.microsoft.com/sql/sql-server/azure-arc/overview?view=sql-server-ver17)).

Use SQL Server enabled by Azure Arc when you need inventory and management for existing SQL Server instances. Use SQL Managed Instance enabled by Azure Arc when the design calls for the Arc data services managed instance pattern on Kubernetes. The names are similar, so state the distinction in architecture reviews.

## Sources

- [Connectivity mode and requirements](https://learn.microsoft.com/azure/azure-arc/data/connectivity)
- [Release notes, Azure Arc-enabled data services](https://learn.microsoft.com/azure/azure-arc/data/release-notes)
- [Azure Arc-enabled data services Kubernetes validation](https://learn.microsoft.com/azure/azure-arc/data/validation-program)
- [SQL Server enabled by Azure Arc](https://learn.microsoft.com/sql/sql-server/azure-arc/overview?view=sql-server-ver17)
