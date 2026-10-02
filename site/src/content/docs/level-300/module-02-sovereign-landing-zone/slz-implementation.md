---
title: "SLZ implementation"
description: "Compare Sovereign Landing Zone implementation paths, including Bicep, Terraform, Azure Landing Zones Library, and Microsoft.Sovereign resources."
lastVerified: 2026-10-02
sidebar:
  order: 3
---

SLZ implementation has two meanings. The first is the accelerator path that layers SLZ assets onto an Azure landing zone implementation. The second is the native `Microsoft.Sovereign` resource provider, which exposes preview ARM resource types for landing zone accounts and configurations. Treat them as distinct mechanisms until Microsoft documents a unified production path.

The term "Azure sovereign clouds" also has two meanings in Microsoft documentation. In Azure Architecture Center deployment guidance, it refers to isolated Azure clouds such as Azure Government and Azure operated by 21Vianet. In the Microsoft Sovereign Cloud documentation under `/azure/azure-sovereign-clouds/`, it refers to the current portfolio of Sovereign Public Cloud, Sovereign Private Cloud, and National Partner Clouds. State which meaning you use in architecture documents.

## Implementation options

Microsoft Learn says there is no single mandated SLZ deployment path. You can adopt SLZ controls incrementally or deploy the full variant.

| Path | Current Microsoft guidance | Best fit |
| --- | --- | --- |
| Bicep accelerator | Uses a compact SLZ package from `Azure/alz-bicep-accelerator` to overlay SLZ configuration during bootstrap. | Teams using Bicep and the Azure landing zone accelerator pattern. |
| Terraform accelerator | Uses Terraform Azure Verified Modules for the platform landing zone, deployed manually or through the Azure landing zone accelerator. | Teams standardizing ALZ on Terraform and AVM. |
| Azure Landing Zones Library | SLZ assets live under `platform/slz` and depend on `platform/alz`. | Teams building or extending accelerator content, policy assets, and library-driven platform definitions. |
| `Microsoft.Sovereign` resource provider | `landingZoneAccounts` and `landingZoneAccounts/landingZoneConfigurations` use API version `2025-02-27-preview`. | Early evaluation of native ARM resource types. Treat as preview. |

The Azure Landing Zones Library release page showed a `platform/slz/2026.08.1` tag during this update. Check the latest GitHub release before you pin a library version, because library assets and policy definitions change.

## Bicep accelerator path

The Bicep path follows the Azure landing zone accelerator deployment pattern. It uses the `examples/slz/.config` and `examples/slz/templates` folders from the `Azure/alz-bicep-accelerator` repository. The accelerator copies those folders into the accelerator configuration before bootstrap, then deploys the platform landing zone through the generated continuous delivery workflow.

Use this path when the platform team already runs Bicep or wants readable Azure-native templates in source control. Keep the SLZ overlay small. The landing zone should still be parameterized by region, management group, policy assignment, and subscription vending decisions rather than hard-coded for one customer environment.

For Azure Government or Azure operated by 21Vianet, the Azure Architecture Center says the portal-based ALZ deployment is not supported. Bicep can still be used as a starting point, but the platform team must remove unsupported policies, adjust unavailable API versions, and remove resources that are not available in that cloud.

## Terraform accelerator path

The Terraform path uses Terraform Azure Verified Modules for the platform landing zone. Microsoft Learn recommends the Azure landing zone accelerator for guided setup. The high-level flow chooses Terraform as the infrastructure as code tool, chooses GitHub or Azure DevOps as version control, selects a scenario, enables the SLZ controls step, checks prerequisites, deploys bootstrap, and runs continuous delivery for the platform landing zone.

Use this path when Terraform is the enterprise standard or when policy and platform teams already manage module versions through a Terraform registry and pull request workflow. As with Bicep, do not assume public Azure settings work unchanged in Azure Government or 21Vianet.

## Azure Landing Zones Library

Both Bicep and Terraform SLZ implementations use the Azure Landing Zones Library. The library contains Azure Policy assets and constructs that produce deployable landing zone architecture. Microsoft Learn states that the SLZ library assets are in the `platform/slz` directory and that SLZ depends on the `platform/alz` directory.

This dependency is important for upgrades. An SLZ change can depend on ALZ changes, and ALZ policy changes can affect sovereign controls. Pin versions, read release notes, and test policy effects in a non-production tenant before updating production assignments.

## Microsoft.Sovereign resource provider

The `Microsoft.Sovereign` resource provider is not the same thing as the accelerator path. The ARM template reference lists these resource types at API version `2025-02-27-preview`:

| Resource type | Use |
| --- | --- |
| `Microsoft.Sovereign/landingZoneAccounts` | Defines a landing zone account resource and the storage account that hosts generated infrastructure as code. |
| `Microsoft.Sovereign/landingZoneAccounts/landingZoneConfigurations` | Defines configuration for management groups, policies, connectivity, logging, and related platform resources. |
| `Microsoft.Sovereign/landingZoneAccounts/landingZoneRegistrations` | Listed as part of the provider version set. |

Because the API version includes `preview`, do not treat this provider as a replacement for the documented accelerator path without a product decision, support review, and non-production validation. It is useful to track because it shows where Microsoft is moving native resource modeling for SLZ.

## Architect-level deployment sequence

Use this sequence for a new or major SLZ deployment.

1. Plan the control model. Confirm data classifications, sovereign boundaries, allowed regions, service restrictions, platform dependencies, and non-regional service exceptions.
2. Bootstrap the platform. Create or update the ALZ management group structure, identity model, platform subscriptions, version control repository, pipeline identity, and state storage.
3. Configure SLZ assets. Add Public, Confidential Online, and Confidential Corp under Landing Zones. Add or confirm the Security platform subscription for Managed HSM and other sovereign security services.
4. Deploy the platform landing zone. Run the Bicep or Terraform accelerator pipeline. Keep policy assignment parameters in source control.
5. Vend workload subscriptions. Place each subscription in Public, Online, Corp, Confidential Online, or Confidential Corp based on data classification and network exposure.
6. Operate and improve. Review Azure Policy compliance, Sovereign Control Panel posture, Defender for Cloud findings, exemptions, and policy drift. Promote audit controls to deny after templates and teams can deploy compliant resources.

## Brownfield adoption

Microsoft Learn says you do not need to replace your Azure landing zone implementation to adopt SLZ. Start from the existing landing zone unless critical structural gaps exist. This is the safest pattern for brownfield estates.

For brownfield subscriptions, avoid moving every subscription at once. First, discover each workload's data classification, network exposure, region footprint, customer-managed key support, private endpoint posture, and confidential compute readiness. Assign audit policies at the candidate management group, then remediate or exempt before you switch high-impact policies to deny.

Subscription movement also needs operational cleanup. The CAF FAQ explains that subscription reuse should remove resource groups, role assignments, custom RBAC definitions, policy definitions, assignments, exemptions, deployments, tags, locks, budgets, diagnostics settings, Lighthouse delegations, and hidden resources before reassignment. Apply the same discipline when a brownfield subscription moves into Confidential Corp or Confidential Online.

## Sources

- [Sovereign Landing Zone implementation options](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/implementation-options)
- [Sovereign Landing Zone](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/overview-sovereign-landing-zone)
- [Microsoft.Sovereign landingZoneAccounts](https://learn.microsoft.com/azure/templates/microsoft.sovereign/landingzoneaccounts)
- [Microsoft.Sovereign resource types](https://learn.microsoft.com/azure/templates/microsoft.sovereign/allversions)
- [Deploy Azure landing zones](https://learn.microsoft.com/azure/architecture/landing-zones/landing-zone-deploy)
- [Azure landing zone frequently asked questions](https://learn.microsoft.com/azure/cloud-adoption-framework/ready/enterprise-scale/faq)
- [Releases for Azure Landing Zones Library](https://github.com/Azure/Azure-Landing-Zones-Library/releases)
