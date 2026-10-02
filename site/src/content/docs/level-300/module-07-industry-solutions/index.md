---
title: "Module 7: Industry solutions"
description: "Apply sovereign cloud controls to regulated financial services, healthcare, government, and critical infrastructure architectures."
lastVerified: 2026-10-02
module:
  duration: "60-90 minutes"
  objectives:
    - Select the Microsoft Sovereign Cloud deployment model that matches an industry's regulatory and operational constraints.
    - Map industry drivers to Sovereign Landing Zone levels and Microsoft-documented control families.
    - Choose key, access, monitoring, and edge controls for sector-specific architectures.
    - Explain when Sovereign Public Cloud, Azure Local, Microsoft 365 Local, and National Partner Clouds fit an industry design.
  prerequisites:
    - /level-300/module-02-sovereign-landing-zone/
---

Industry designs start with obligations that change where data can live, who can operate the service, how keys are controlled, and how evidence is produced. This module applies those decisions to financial services, healthcare, government, and critical infrastructure workloads. Each pattern uses Microsoft-documented regulatory offerings and Microsoft Sovereign Cloud controls rather than sector assumptions.

Use these pages as architecture patterns, not legal advice. Your design still needs customer legal review, contract review, and a service availability check for the selected cloud environment.

```mermaid
graph TB
  A["Industry driver"] --> B["Sovereign Landing Zone level"]
  B --> C["Public cloud controls"]
  B --> D["Private cloud placement"]
  B --> E["Partner or government cloud"]
  C --> F["Evidence and operations"]
  D --> F
  E --> F
```

## Sources

- [What is Microsoft Sovereign Cloud?](https://learn.microsoft.com/azure/azure-sovereign-clouds/microsoft-sovereign-cloud)
- [What is Sovereign Public Cloud?](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/overview-sovereign-public-cloud)
- [What is Sovereign Private Cloud?](https://learn.microsoft.com/azure/azure-sovereign-clouds/private/overview/sovereign-private-cloud)
- [National Partner Clouds](https://learn.microsoft.com/azure/azure-sovereign-clouds/partner/overview-national-partner-clouds)
- [Sovereign Landing Zone](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/overview-sovereign-landing-zone)
