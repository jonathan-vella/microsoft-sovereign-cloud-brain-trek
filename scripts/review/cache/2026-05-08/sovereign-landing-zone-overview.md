# MS Learn snapshot — 2026-05-08

**Source:** <https://learn.microsoft.com/azure/azure-sovereign-clouds/public/overview-sovereign-landing-zone>
**Cache date:** 2026-05-08
**Used by:** Phase 3.4 L300 verification (SLZ-1)

## Verbatim excerpts

### What is the Sovereign Landing Zone

> The Sovereign Landing Zone (SLZ) is a variant of the Azure landing zone
> platform landing zone architecture. It's tailored to help accelerate
> customers with sovereign requirements to meet their specific sovereign
> needs and requirements.

> The SLZ architecture is based on the Azure landing zone architecture,
> which provides a scalable and secure foundation for deploying and
> managing workloads in Azure. SLZ applies the same underlying design
> principles and design areas, while also incorporating additional
> controls and principles to address specific sovereign requirements in
> the Sovereign Public Cloud.

### Key SLZ-specific differences (Environment)

> Resource organization: Addition of the `Public`, `Confidential Corp`,
> and `Confidential Online` Management Groups beneath the `Landing Zones`
> Management Group.

→ Project content in `level-300/sovereign-landing-zone.md` should
verify that the management-group hierarchy is described with these
exact group names.

### Key SLZ-specific differences (Compliance)

> Security, Management & Governance: Additional Azure Policies either
> applied or required depending on organization sovereignty
> requirements.

### Topology options (verbatim)

The page shows 4 architecture options:

1. Hub & Spoke
2. Virtual WAN
3. Management Group Hierarchy Only
4. Management Group Hierarchy with Controls & Principles

## Verification entries (claim list)

| ID | Project doc claim | File | Outcome |
|---|---|---|---|
| SLZ-1 | SLZ scope, components, management group hierarchy | `level-300/sovereign-landing-zone.md`, `level-100/digital-sovereignty.md` | NEEDS-CHECK on next deep-content review pass — current pages are ≥ 400 words and reference SLZ correctly at high level. Specific numeric / structural claims (e.g., the 3 confidential management groups) should be cross-checked in PR-4 |
| SLZ-2 | EU Data Boundary commitments | `level-100/european-commitments.md`, `level-100/data-residency-concepts.md` | NEEDS-CHECK on next deep-content review pass |
| SLZ-3 | SLZ deployment via Bicep / Terraform | (project-wide) | INFORMATIONAL — recent SLZ release adds Terraform support (Sep 2025 GA); project content should mention both options if SLZ deployment is discussed in detail |
