---
title: "Security hardening"
description: "Plan Azure Local, Arc-connected workload, Defender for Cloud, Zero Trust, and Microsoft Entra hardening controls."
lastVerified: 2026-10-02
sidebar:
  order: 2
---

Security hardening for sovereign solutions combines platform defaults, workload configuration, identity governance, and evidence collection. Start with Azure Local security defaults for private cloud hosts, then extend monitoring and threat protection through Azure Arc and Defender for Cloud.

## Harden Azure Local hosts first

Azure Local includes default security settings that start the instance in a known good state. The security defaults page in the Azure portal lets you view system security, drift control, and Secured-core settings. The same Learn guidance explains that Azure Local host machines can reach an expected compliance score of 99% of rules when Secured-core hardware requirements are met ([Learn](https://learn.microsoft.com/azure/azure-local/manage/manage-secure-baseline)).

Use this baseline as the host control layer:

| Control | What to plan |
| --- | --- |
| Secured-core | Confirm hardware supports the required Secured-core capabilities before procurement. Do not wait until deployment to find unsupported firmware or TPM behavior. |
| Security baseline | Keep the Microsoft security baseline applied, then document approved deviations. |
| Drift control | Enable drift control for protected settings. If a protected setting must change, disable drift control, apply the change, document the exception, and re-enable drift control. |
| BitLocker | Enable BitLocker for OS boot volumes and data volumes. Include recovery-key handling in the backup and break-glass plan. |
| Windows Defender Application Control | Use WDAC to restrict which drivers and applications can run on Azure Local nodes. Test operational tooling before broad enforcement. |
| SMB signing and encryption | Review SMB signing for external SMB traffic and SMB encryption for in-cluster traffic. These settings protect management and storage traffic paths. |

Security defaults do not replace operational hygiene. You still need patch management, credential rotation, privileged access review, and incident-response runbooks.

## Forward local security events

Azure Local supports forwarding security events to a customer-managed SIEM by using syslog. Syslog forwarding agents are deployed on every Azure Local host by default, and each agent forwards host security events in syslog format after configuration ([Learn](https://learn.microsoft.com/azure/azure-local/manage/manage-syslog-forwarding)).

Prefer encrypted forwarding for production:

| Forwarding mode | Use |
| --- | --- |
| TCP with mutual authentication and TLS | Use when the SIEM supports client and server certificates. This gives both endpoint authentication and encryption. |
| TCP with server authentication and TLS | Use when the Azure Local hosts only need to validate the SIEM server certificate. |
| TCP or UDP without encryption | Use only for lab validation or networks where another approved encryption layer protects the path. |

Document the syslog server name, port, certificate authority, certificate rotation owner, retention target, and alert routing. Sovereign designs often require local log retention even when a subset of telemetry also flows to Azure.

## Use Trusted launch for Azure Local VMs

Trusted launch for Azure Local VMs enabled by Azure Arc supports secure boot, a virtual Trusted Platform Module, vTPM state transfer during migration or failover, and boot integrity verification. Boot integrity verification is preview ([Learn](https://learn.microsoft.com/azure/azure-local/manage/trusted-launch-vm-overview)).

Plan these details before enabling it:

- VM backup must include all VM files and the VM guest state protection key.
- Restoring a Trusted launch VM to a different Azure Local instance can prevent management through the Azure Arc control plane.
- Azure Site Recovery replication from Azure Local to Azure is not supported for these VMs.
- Automatic backup of system-level secrets to Azure Key Vault is preview.
- VM live migration network traffic is not encrypted by default, so use a network-layer encryption technology such as IPsec for that path.

Use Trusted launch for workloads that benefit from secure boot, vTPM-backed guest protection, or boot attestation evidence. If you bring custom images, confirm whether guest attestation remains available for your image path.

## Protect servers with Defender for Cloud through Arc

Defender for Servers protects Azure, multicloud, and on-premises machines. For on-premises machines, Microsoft recommends onboarding them as Azure Arc VMs. Direct onboarding to Defender for Cloud is possible, but it does not provide full access to Defender for Servers Plan 2 features ([Learn](https://learn.microsoft.com/azure/defender-for-cloud/defender-for-servers-introduction)).

For sovereign or hybrid environments, plan these steps:

1. Onboard non-Azure servers to Azure Arc.
2. Enable the Defender for Servers plan at the right scope.
3. Install required extensions, including machine configuration for operating-system baseline assessment.
4. Configure file integrity monitoring with a Log Analytics workspace when Plan 2 is enabled.
5. Decide which data stays local, which data is forwarded to a SIEM, and which data is sent to Azure.

Several Plan 2 capabilities depend on Arc onboarding for non-Azure resources. For example, the Defender for Servers planning guide says on-premises direct onboarding does not give full access to Plan 2 features. The feature table for Defender for Servers also marks file integrity monitoring and some OS baseline capabilities as Plan 2 features for Arc-onboarded AWS and GCP machines.

## Protect container workloads

Defender for Containers covers Kubernetes clusters, nodes, workloads, registries, and images across multicloud and on-premises environments. It provides posture management, vulnerability assessment, runtime threat protection, software supply chain protection, and deployment monitoring ([Learn](https://learn.microsoft.com/azure/defender-for-cloud/defender-for-containers-introduction)).

Use it with sovereign design constraints:

| Area | Design question |
| --- | --- |
| Cluster discovery | Which Kubernetes clusters must be visible to Defender for Cloud, and which must remain locally monitored only? |
| Vulnerability assessment | Which registries and running containers must be scanned, and how will findings block deployment? |
| Runtime protection | Which environments support the Defender sensor and Kubernetes audit log collection? |
| Supply chain | Which image policies stop vulnerable or unapproved images from reaching production? |
| Evidence | Which recommendations, alerts, and gated deployment records support compliance evidence? |

For disconnected or intermittently connected Azure Local deployments, validate support and data-flow requirements before promising Defender for Containers coverage.

## Apply Zero Trust principles

Microsoft defines Zero Trust with three principles: verify explicitly, use least privilege access, and assume breach ([Learn](https://learn.microsoft.com/security/zero-trust/zero-trust-overview)). Current adoption guidance organizes implementation through business scenarios, security disciplines, technology pillars, and technical solutions.

Use the seven technology pillars as a checklist:

| Pillar | Sovereign design focus |
| --- | --- |
| Identities | Require strong authentication, Conditional Access, privileged access workflows, and separate identities for public and government tenants where needed. |
| Endpoints | Enforce device compliance, endpoint detection, patching, and local host hardening. |
| Data | Classify data, apply encryption, manage retention, and implement data subject or agency request workflows. |
| Apps | Require modern authentication, least privilege app permissions, secure configuration, and dependency scanning. |
| Infrastructure | Use Azure Policy, Defender for Cloud, Arc, secure baselines, and confidential computing where justified. |
| Network | Restrict public access, use private endpoints, segment management paths, and log allowed flows. |
| SecOps | Centralize detection, incident response, control testing, and remediation tracking. |

Avoid treating Zero Trust as a product deployment. It is an operating model that must be reflected in architecture, configuration, monitoring, and response.

## Use Microsoft Entra as the identity control plane

Microsoft Entra is a family of identity and network access products for Zero Trust. It includes Microsoft Entra ID, Domain Services, Private Access, Internet Access, ID Governance, ID Protection, Verified ID, External ID, Workload ID, and Agent ID for AI agents ([Learn](https://learn.microsoft.com/entra/fundamentals/whatis)).

For sovereign solutions, define identity boundaries explicitly:

- Use Microsoft Entra ID and Conditional Access for cloud control-plane access.
- Use Microsoft Entra ID Governance for access packages, lifecycle automation, and reviews.
- Use Privileged Identity Management for just-in-time administrative elevation.
- Use Workload ID for applications, services, containers, and automation.
- Use Agent ID when AI agents need governed nonhuman identities.
- Use separate Azure Government identity planning when workloads run in Azure Government.

For compliance evidence, retain access review records, privileged activation logs, Conditional Access policy changes, and workload identity ownership records.

## Hardening checklist

Use this checklist before design approval:

| Layer | Minimum decision |
| --- | --- |
| Host | Azure Local baseline, Secured-core, BitLocker, WDAC, drift control, and syslog path are defined. |
| VM | Trusted launch use, backup constraints, guest attestation status, and migration limitations are documented. |
| Server | Arc onboarding and Defender for Servers plan scope are defined. |
| Container | Defender for Containers coverage, image scanning, and runtime monitoring are defined. |
| Identity | Human, workload, external, and agent identities have separate governance paths. |
| Network | Public access, private endpoints, management segmentation, and live migration encryption are defined. |
| Evidence | Defender for Cloud, Azure Policy, SIEM, access review, and exception evidence are assigned to owners. |

## Sources

- [Manage security defaults for Azure Local](https://learn.microsoft.com/azure/azure-local/manage/manage-secure-baseline)
- [Manage syslog forwarding for Azure Local](https://learn.microsoft.com/azure/azure-local/manage/manage-syslog-forwarding)
- [Introduction to Trusted launch for Azure Local VMs enabled by Azure Arc](https://learn.microsoft.com/azure/azure-local/manage/trusted-launch-vm-overview)
- [Plan Defender for Servers deployment](https://learn.microsoft.com/azure/defender-for-cloud/defender-for-servers-introduction)
- [Introduction to Microsoft Defender for Containers](https://learn.microsoft.com/azure/defender-for-cloud/defender-for-containers-introduction)
- [Zero Trust as a security foundation](https://learn.microsoft.com/security/zero-trust/zero-trust-overview)
- [What is Microsoft Entra?](https://learn.microsoft.com/entra/fundamentals/whatis)
