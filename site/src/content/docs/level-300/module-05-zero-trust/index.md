---
title: "Module 5: Zero Trust"
description: "Design Zero Trust for sovereign estates that span Microsoft Sovereign Cloud, Azure Local, Azure Arc, and AI workloads."
lastVerified: 2026-10-02
module:
  duration: "60-90 minutes"
  objectives:
    - Apply the three Zero Trust principles across sovereign cloud and edge estates.
    - Map the seven Microsoft Zero Trust technology pillars to the right control planes.
    - Design identity, network, data, infrastructure, and SecOps controls for Azure, Azure Local, Arc, and AI agents.
    - Use Defender for Cloud and Microsoft Sentinel to monitor hybrid and multicloud Zero Trust controls.
  prerequisites:
    - /level-50/module-02-security-compliance/
---

Zero Trust starts from three Microsoft principles: [verify explicitly, use least privilege access, and assume breach](https://learn.microsoft.com/security/zero-trust/zero-trust-overview). In a sovereign estate, those principles must work across Sovereign Public Cloud subscriptions, Azure Local sites, Arc-enabled infrastructure, and AI workloads that may act without a human at the keyboard.

The current Microsoft adoption model organizes Zero Trust work into business scenarios, security disciplines, technology pillars, and technical solutions. The technology pillar layer now has [seven pillars](https://learn.microsoft.com/security/zero-trust/deploy/overview): Identities, Endpoints, Data, Apps, Infrastructure, Network, and SecOps. SecOps is no longer only a cross-cutting activity. It is the pillar that connects signals, investigation, and response across the other six.

## Pillars and Microsoft control planes

| Pillar | Design question | Main Microsoft products and control points |
| --- | --- | --- |
| Identities | Who or what is requesting access, and should the request continue? | Microsoft Entra ID, Conditional Access, Entra ID Protection, Entra ID Governance, Privileged Identity Management, Entra Workload ID, and Microsoft Entra Agent ID |
| Endpoints | Is the device healthy, managed, and still safe during the session? | Microsoft Intune, Microsoft Defender for Endpoint, device compliance, endpoint DLP |
| Data | Does protection stay with the asset when it moves? | Microsoft Purview, sensitivity labels, data loss prevention, Customer-Managed Keys, Managed HSM, Azure Confidential Computing |
| Apps | Are app and API sessions governed at the resource boundary? | Microsoft Entra app integration, Conditional Access app controls, Microsoft Defender for Cloud Apps, Azure API Management, app registration governance |
| Infrastructure | Are compute, containers, and management planes hardened and monitored? | Azure Arc, Azure Policy, Microsoft Defender for Cloud, Defender for Servers, Defender for Containers, Azure Local management |
| Network | Is connectivity identity-aware, segmented, encrypted, and observable? | Global Secure Access, Microsoft Entra Internet Access, Microsoft Entra Private Access, Azure Firewall, Azure Private Link, private endpoints |
| SecOps | Can the team detect, investigate, and respond across every pillar? | Microsoft Defender portal, Microsoft Defender XDR, Microsoft Defender for Cloud, Microsoft Sentinel, Security Copilot, regulatory compliance dashboard |

## Sovereign design emphasis

Zero Trust for sovereignty is not a separate model. It is the Microsoft model applied with stricter placement, key control, operator, and evidence requirements. Architects should make four decisions early.

| Decision | Sovereign design point |
| --- | --- |
| Policy authority | Use Microsoft Entra Conditional Access as the cloud policy engine when cloud identity is available. For Azure Local disconnected operations, plan the local Active Directory and AD FS integration before deployment. |
| Enforcement point | Place controls close to the protected asset. Use identity checks for every request, network segmentation for lateral movement limits, and data controls such as labels, encryption, and key release for sensitive data. |
| Evidence plane | Send security posture, workload protection, and investigation signals to Defender for Cloud, Microsoft Defender portal, and Microsoft Sentinel. Keep logs and workspaces in the required geography or local environment. |
| AI identity | Treat AI agents as nonhuman identities. Use Entra Agent ID and workload identity patterns so agent access is governed, least-privilege, and auditable. |

The rest of this module turns that model into an architecture for sovereign estates, then shows how to monitor the controls through the SecOps pillar.

## Sources

- [Zero Trust as a security foundation](https://learn.microsoft.com/security/zero-trust/zero-trust-overview)
- [Overview: Technology pillars](https://learn.microsoft.com/security/zero-trust/deploy/overview)
- [Overview: Implement Zero Trust solutions](https://learn.microsoft.com/security/zero-trust/implement-overview)
- [What is Microsoft Entra?](https://learn.microsoft.com/entra/fundamentals/what-is-entra)
- [What is Microsoft Entra Agent ID?](https://learn.microsoft.com/entra/agent-id/what-is-microsoft-entra-agent-id)
- [What is Global Secure Access?](https://learn.microsoft.com/entra/global-secure-access/overview-what-is-global-secure-access)
- [What is Conditional Access?](https://learn.microsoft.com/entra/identity/conditional-access/overview)
- [What is Microsoft Defender for Cloud?](https://learn.microsoft.com/azure/defender-for-cloud/defender-for-cloud-introduction)
- [Connect Microsoft Sentinel to the Microsoft Defender portal](https://learn.microsoft.com/azure/sentinel/microsoft-sentinel-onboard)
