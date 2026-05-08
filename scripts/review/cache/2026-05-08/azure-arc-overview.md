# MS Learn snapshot — 2026-05-08

**Source:** <https://learn.microsoft.com/en-us/azure/azure-arc/overview>
**Cache date:** 2026-05-08
**Used by:** Phase 0.5 pilot (L100 Module 4 — Azure Arc verification)

## Excerpts (verbatim)

### Resource types Azure Arc manages

> Currently, Azure Arc allows you to manage the following resource types
> hosted outside of Azure:
>
> - **Servers** and virtual machines: Manage Windows and Linux physical
>   servers and virtual machines hosted outside of Azure. Provision, resize,
>   delete, and manage virtual machines based on Azure Local and on VMware
>   vCenter or System Center Virtual Machine Manager managed on-premises
>   environments.
> - **Kubernetes clusters**: Attach and configure Kubernetes clusters
>   running anywhere, with multiple supported distributions.
> - **Azure data services**: Run SQL Managed Instance on-premises, at the
>   edge, and in public clouds using Kubernetes and the infrastructure of
>   your choice.
> - **SQL Server**: Extend Azure services to SQL Server instances hosted
>   outside of Azure.

→ **Authoritative count: 4 Arc resource types** (Servers, Kubernetes,
data services, SQL Server). Project docs that claim "three Arc services"
must be updated.

### Indirectly connected mode

> As of September, 2025 indirectly connected mode is retired.

→ Material change. Any project content describing "indirectly connected
mode" as a current option must be updated to reflect retirement.

### Adaptive cloud framing

> Azure Arc is a key part of Microsoft's adaptive cloud approach. This
> approach helps organizations run and manage apps and services across
> many environments, including Azure, other cloud providers, on-premises
> datacenters, and edge locations.

## Verification entries (claim list)

| # | Project doc claim (verbatim) | File:line | Outcome | Notes |
|---|---|---|---|---|
| ARC-1 | "Hybrid management, multi-cloud governance, three Arc services" | level-100/azure-arc-intro.md:21 | **MISMATCH** | Authoritative: four resource types (Servers, Kubernetes, data services, SQL Server) |
| ARC-2 | "Hybrid management, multi-cloud governance, Arc-enabled services" (general framing) | level-100/azure-arc-intro.md:81+ | MATCH | Confirmed hybrid/multi-cloud framing |
| ARC-3 | Indirect / disconnected Arc options availability | (search needed) | NEEDS-CHECK | If "indirectly connected mode" is mentioned anywhere, must update per Sep 2025 retirement |
