# MS Learn snapshot — 2026-05-08

**Source:** <https://learn.microsoft.com/en-us/azure/azure-local/manage/disconnected-operations-overview>
**Cache date:** 2026-05-08
**Used by:** Phase 3.3 L200 verification (LOCAL-2 disconnected operations claims)

## Status snapshot (verbatim excerpts)

### Sovereign requirements

> In sectors like government, healthcare, and finance, you have data
> residency and sovereign requirements that are hard to meet using
> public sovereign cloud controls. When you run disconnected, data,
> operations, and control remain within your organization's boundaries.

### Service availability matrix (preview indicators)

> Arc-enabled Kubernetes clusters (**Preview**) | Connect and manage
> CNCF Kubernetes clusters deployed on Azure Local VMs.
>
> Azure Kubernetes Service (AKS) enabled by Arc for Azure Local
> (**Preview**) | Set up and manage AKS on Azure Local.

### Business prerequisites

> Disconnected operations are for organizations that can't connect to
> Azure because of connectivity issues or regulatory restrictions. To
> be able to procure disconnected operations, you need a valid business
> need for running and operating in a disconnected environment.

### Hardware minimums (per-node example)

> Number of nodes: 3 nodes
> Memory per node: 96 GB
> Cores per node: 24 physical cores
> Storage per node: 2 TB SSD/NVME

→ Project content in `level-100/azure-local-disconnected-mode.md` and
`level-300/azure-local-air-gapped.md` should reference the
"3-node minimum" anchor; do not cite specific RAM/CPU per-node numbers
unless they appear verbatim from this page.

## Verification entries (claim list)

| ID | Project doc claim | File | Outcome |
|---|---|---|---|
| LOCAL-2 | Disconnected operations support and minimums | `level-100/azure-local-disconnected-mode.md` | NEEDS-CHECK Phase 3.4 — review specific numeric claims against this snapshot |
| LOCAL-3 | Arc-enabled Kubernetes / AKS on disconnected = Preview | `level-200/edge-rag-implementation.md` | **MATCH** — note "(Preview)" |
| LOCAL-4 | Sovereign use cases (government, healthcare, finance) | `level-300/azure-local-air-gapped.md`, `level-300/financial-services.md`, `level-300/healthcare-sovereign.md` | **MATCH** — Microsoft explicitly cites these sectors |
