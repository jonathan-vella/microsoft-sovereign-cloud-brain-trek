---
title: "Module 1: Azure Local advanced"
description: "Design Azure Local at architect depth across connected, multi-site, network, certificate, and disconnected operation scenarios."
lastVerified: 2026-10-02
module:
  duration: "60-90 minutes"
  objectives:
    - Distinguish fleet scale from single-instance scale for Azure Local designs.
    - Choose an Azure Local deployment pattern for connected, multi-site, and disconnected requirements.
    - Plan network intents, SDN boundaries, and Arc gateway connectivity for Azure Local.
    - Plan certificate, secret, identity, and update operations for regulated Azure Local environments.
  prerequisites:
    - /level-200/module-01-azure-local/
---

Azure Local at Level 300 is an architecture exercise. You decide when one instance is large enough, when to add another instance, when to keep sites separate, and when to move the control plane into the customer boundary. This module focuses on scale limits, failure domains, network design, certificate operations, and disconnected operations.

Use the single-instance limits as sizing guardrails, not as fleet limits. Microsoft Learn describes connected operations as scaling "from one node to thousands of nodes," but that is aggregate fleet scale across a sovereign environment. A single instance still follows the deployment-type limits in the table.

| Deployment type | Single-instance maximum |
| --- | --- |
| Hyperconverged | [1 to 16 machines](https://learn.microsoft.com/azure/azure-local/overview/hyperconverged-overview?view=azloc-2609) |
| Disaggregated | [1 to 64 machines](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/azure-local/connected-operations-overview) |
| Multi-rack | [Up to 128 nodes per instance](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/azure-local/connected-operations-overview) |

## Sources

- [Connected operations overview](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/azure-local/connected-operations-overview)
- [What are hyperconverged deployments of Azure Local?](https://learn.microsoft.com/azure/azure-local/overview/hyperconverged-overview?view=azloc-2609)
- [What are multi-rack deployments of Azure Local?](https://learn.microsoft.com/azure/azure-local/multi-rack/multi-rack-overview?view=azloc-2609)
