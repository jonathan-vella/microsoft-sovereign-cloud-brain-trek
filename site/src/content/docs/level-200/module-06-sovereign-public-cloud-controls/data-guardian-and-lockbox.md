---
title: "Data Guardian and Customer Lockbox"
description: "Compare Data Guardian and Customer Lockbox for Microsoft remote access oversight, approval, logging, and service coverage."
lastVerified: 2026-10-02
sidebar:
  order: 2
---

Data Guardian and Customer Lockbox both address Microsoft access to customer environments, but they solve different problems. Data Guardian adds regional oversight and tamper-evident logging for Microsoft remote access. Customer Lockbox gives customer approvers a workflow to approve or deny eligible customer data access requests.

Use them together when the requirement includes both provider-operation oversight and customer approval of direct customer data access. Do not treat one as a replacement for the other.

## Data Guardian

Data Guardian is a Sovereign Public Cloud capability for operational sovereignty. Microsoft states that remote access by Microsoft personnel to systems in defined regions such as EU and EFTA is monitored by authorized European-resident personnel, and access is logged in a tamper-evident ledger ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/data-guardian)).

The ledger uses Azure Confidential Ledger to write entries in a tamper-evident manner ([Learn](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/data-guardian)). That matters for audit review because the control is not only a process statement. It produces evidence that a session occurred under monitored conditions.

The conceptual flow has three steps:

1. A Microsoft engineer requests just-in-time access to a production resource in a sovereign region.
2. Designated personnel monitor the approved session in real time.
3. The session is logged to the ledger for transparency and compliance review.

Data Guardian is useful when an organization must show that provider operations in the region have local human oversight. It does not ask the customer to approve each session. It is about Microsoft-side regional oversight and auditable provider operations.

## Customer Lockbox

Customer Lockbox for Microsoft Azure applies when Microsoft requires access to customer data in rare support or service scenarios. Microsoft states that the organization must have an Azure support plan with a minimum level of Developer to use Customer Lockbox for Microsoft Azure ([Learn](https://learn.microsoft.com/azure/security/fundamentals/customer-lockbox-overview)).

The normal Azure workflow is:

1. A customer opens a support ticket, or Microsoft identifies an issue.
2. The support engineer tries standard tools and service-generated data first.
3. If direct customer data access is required, Microsoft starts internal just-in-time access approval.
4. Customer Lockbox creates a request in the Customer Notified state.
5. The customer's approver approves or denies the request.
6. Azure writes request activity to activity logs for subscription-scoped requests and to Microsoft Entra audit logs for tenant-scoped requests.

Microsoft Learn lists more than 40 supported Azure services, including Azure API Management, Azure App Service, Azure AI Search, Azure Kubernetes Service, Azure Storage, Azure SQL Database, Azure SQL Managed Instance, Azure OpenAI, Azure Synapse Analytics, Azure Functions, Azure Logic Apps, and Virtual Machines in Azure ([Learn](https://learn.microsoft.com/azure/security/fundamentals/customer-lockbox-overview)). The list changes over time, so treat it as a service-by-service planning input.

Customer Lockbox is not universal. Customer Lockbox for Azure Data Box is an opt-in preview for Data Box and Data Box Heavy orders ([Learn](https://learn.microsoft.com/azure/databox/data-box-customer-lockbox)). Power Platform and Dynamics 365 Customer Lockbox has product carve-outs, including Cards for Power Apps, data sent from Copilot Studio as part of Agent 365 security audit logging, some Azure OpenAI-powered features unless documentation says Lockbox applies, Nuance Conversational IVR unless documentation says Lockbox applies, Maker Welcome Content, and Power Platform environment settings ([Learn](https://learn.microsoft.com/power-platform/admin/about-lockbox)).

:::caution[Check service scope before committing]
Do not promise Customer Lockbox coverage at platform level. Confirm that the exact service and feature are in scope, and record any carve-outs in the workload design record.
:::

## How they complement each other

| Design question | Data Guardian | Customer Lockbox |
|---|---|---|
| Who is the approver? | Authorized regional Microsoft personnel monitor Microsoft access. | Customer-designated approvers approve or reject eligible requests. |
| What access problem does it address? | Regional oversight of Microsoft personnel remote access to sovereign systems. | Customer consent for eligible Microsoft access to customer data. |
| What evidence does it produce? | Tamper-evident ledger entries for monitored sessions. | Customer Lockbox request logs, activity logs, Microsoft Entra audit logs, and support ticket context. |
| Is it service-specific? | It applies to the defined Sovereign Public Cloud regions and systems Microsoft documents for the capability. | Yes. Microsoft publishes supported service lists and carve-outs. |
| Does it cover emergency scenarios? | Review the Data Guardian documentation and contract scope for applicability. | Customer Lockbox excludes break-glass emergency scenarios and some platform troubleshooting paths. |

The strongest design uses both controls with a clear escalation path. For example, a European regulated workload might use the EU Data Boundary and Azure Policy for residency, Data Guardian for European-resident oversight of Microsoft access, Customer Lockbox for eligible customer data access approval, Managed HSM for key control, and confidential computing for Level 3 workloads.

## Planning checklist

Use this checklist before including either control in a customer design:

- Identify the service and feature set. Customer Lockbox support is not a blanket property of Azure.
- Confirm support plan prerequisites. Azure Customer Lockbox requires at least the Developer support plan.
- Name the approver group. For Azure subscription-scoped requests, use subscription Owner or Azure Customer Lockbox Approver for Subscription. For tenant-scoped requests, use Global Administrator.
- Define response ownership. Lockbox requests expire if customer approvers do not act in time, so the support process needs coverage.
- Map evidence to the audit requirement. Data Guardian logs, Customer Lockbox logs, support tickets, and policy evidence answer different audit questions.
- Record exclusions. Emergency access, legal demands, preview services, and product carve-outs need explicit treatment.

## Worked example

A ministry runs a case management system in West Europe and must prove that Microsoft operational access has regional oversight and that direct customer data access needs customer approval.

Use Data Guardian for the regional oversight requirement because it addresses Microsoft remote access monitoring by European-resident personnel and ledger logging. Use Customer Lockbox for customer approval of eligible customer data access requests. Add Azure Policy to enforce approved regions and customer-managed keys, and use Sovereign Control Panel to review posture evidence.

The evidence pack should include the support plan, Lockbox configuration, approver roles, activity log export, Data Guardian ledger access process, Azure Policy compliance report, and exception handling process.

## Sources

- [What is Data Guardian?](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/data-guardian)
- [Azure confidential ledger overview](https://learn.microsoft.com/azure/confidential-ledger/overview)
- [Customer Lockbox for Microsoft Azure](https://learn.microsoft.com/azure/security/fundamentals/customer-lockbox-overview)
- [Use Customer Lockbox for Azure Data Box (Preview)](https://learn.microsoft.com/azure/databox/data-box-customer-lockbox)
- [Securely access customer data by using Customer Lockbox in Power Platform and Dynamics 365](https://learn.microsoft.com/power-platform/admin/about-lockbox)
