---
title: National Partner Clouds
description: "Learn what National Partner Clouds are and how Bleu in France and Delos Cloud in Germany use Microsoft technology with partner operations."
lastVerified: 2026-10-02
sidebar:
  order: 4
---

National Partner Clouds are Microsoft Sovereign Cloud deployments that combine Microsoft technology with partner-operated and jointly governed operations. They are for countries or regions where a local operator, shared governance model, or national compliance target is part of the sovereignty requirement.

For a comparison of all three models, see [sovereign cloud models](/level-100/module-02-cloud-models/sovereign-cloud-models/).

## What makes a National Partner Cloud different

The defining point is the operating model. Microsoft technology provides the cloud foundation, while an approved national or regional partner operates the environment and participates in governance. This differs from Sovereign Public Cloud, where Microsoft operates Azure public-cloud regions, and from Sovereign Private Cloud, where the customer operates the private environment.

Service scope, latency, rollout timing, and compliance targets [can differ from global Azure](https://learn.microsoft.com/azure/azure-sovereign-clouds/microsoft-sovereign-cloud). Microsoft Learn tells customers to review the published service matrix for each national implementation. Do not assume that every Azure service, region behavior, or release date matches global Azure.

## Bleu in France

Bleu is the National Partner Cloud for France. Microsoft Learn describes Bleu as a joint venture between Orange and Capgemini. It is designed to meet SecNumCloud requirements for French public-sector and regulated customers.

[Bleu is still being built](https://learn.microsoft.com/azure/azure-sovereign-clouds/partner/overview-national-partner-clouds) and is not a generally available global Azure region.

## Delos Cloud in Germany

Delos Cloud is the National Partner Cloud for Germany. Microsoft Learn describes Delos Cloud as operated by an SAP subsidiary and aligned to German Cloud Platform Requirements.

[Delos Cloud is still being built](https://learn.microsoft.com/azure/azure-sovereign-clouds/partner/overview-national-partner-clouds) and is not a generally available global Azure region. Its target is German public-sector and regulated requirements, not a generic replacement for every Azure region in Germany.

## How this differs from Azure Government and 21Vianet

Azure Government and Azure operated by 21Vianet are separate, isolated Azure clouds. Older material sometimes grouped them with partner clouds, but they are not part of the National Partner Clouds model. The Microsoft Sovereign Cloud documentation names Bleu and Delos Cloud for this model.

## When this model fits

Evaluate a National Partner Cloud when the customer has a national operator requirement, a procurement rule that requires local governance participation, or a compliance target that Microsoft addresses through a named partner cloud.

If the requirement is data residency in Azure public cloud without a partner operator, evaluate [Sovereign Public Cloud](/level-100/module-02-cloud-models/sovereign-public-cloud/). If the requirement is customer-operated infrastructure or disconnected operation, evaluate [Sovereign Private Cloud](/level-100/module-02-cloud-models/sovereign-private-cloud/).

## Sources

- [National Partner Clouds](https://learn.microsoft.com/azure/azure-sovereign-clouds/partner/overview-national-partner-clouds)
- [What is Microsoft Sovereign Cloud?](https://learn.microsoft.com/azure/azure-sovereign-clouds/microsoft-sovereign-cloud)
