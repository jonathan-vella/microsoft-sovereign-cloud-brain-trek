---
title: "Module 6: Operations"
description: "Operate Azure Local, Arc-enabled resources, and Sovereign Public Cloud workloads with verified observability, response, and support patterns."
lastVerified: 2026-10-02
module:
  duration: "60-90 minutes"
  objectives:
    - Design telemetry collection that respects residency boundaries and support workflows.
    - Use Azure Local, Azure Monitor, Arc, Sentinel, and Service Health signals during operations.
    - Triage Azure Local, Arc, and AKS on Azure Local issues with verified diagnostic tools.
    - Plan incident response and support escalation without weakening sovereignty controls.
  prerequisites:
    - /level-300/module-05-zero-trust/
---

Operating a sovereign estate is a control problem as much as a reliability problem. Architects must decide where telemetry lands, who can see it, which disconnected mode changes the support model, and when an incident becomes a regulatory or support escalation.

This module covers the operations layer for Azure Local, Arc-enabled resources, and Sovereign Public Cloud workloads. It focuses on Azure Monitor, Insights for Azure Local, Microsoft Sentinel incidents, Azure support access controls, Customer Lockbox, Data Guardian, Service Health, Resource Health, and the verified troubleshooting commands that operators can run before they open a support request.

## Operations map

| Operations decision | Primary Microsoft service | Sovereignty checkpoint |
| --- | --- | --- |
| Telemetry collection | Azure Monitor Agent, data collection rules, Log Analytics workspaces | Place workspaces and data collection endpoints in the intended geography. |
| Azure Local health | Insights for Azure Local, Health Service events, Azure Local metrics | Check what is sent to Azure and what remains local or goes to Microsoft support. |
| Security incidents | Microsoft Sentinel, Microsoft Defender XDR, incident response playbooks | Preserve evidence in the approved region and document notification triggers. |
| Support escalation | Azure support requests, Customer Lockbox, Data Guardian, Azure Local Remote Support | Approve only the access level, scope, and duration needed for the case. |

## Sources

- [Azure Monitor Agent overview](https://learn.microsoft.com/azure/azure-monitor/agents/azure-monitor-agent-overview)
- [Monitor a single Azure Local system with Insights](https://learn.microsoft.com/azure/azure-local/manage/monitor-single-23h2)
- [Incident response overview](https://learn.microsoft.com/security/operations/incident-response-overview)
- [Customer Lockbox for Microsoft Azure](https://learn.microsoft.com/azure/security/fundamentals/customer-lockbox-overview)
- [What is Data Guardian?](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/data-guardian)
