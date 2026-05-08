# MS Learn snapshot — 2026-05-08

**Source:** <https://learn.microsoft.com/en-us/azure/azure-arc/servers/overview>
**Cache date:** 2026-05-08
**Used by:** Phase 0.5 pilot (L100 Module 4 — Azure Arc verification)

## Verbatim excerpts

### Connected Machine agent behaviour

> The Connected Machine agent sends a regular heartbeat message to the
> service every five minutes. If the service stops receiving these
> heartbeat messages from a machine, the service considers that machine
> offline, and the status will change to **Disconnected** within 15 to
> 30 minutes. When the service receives a subsequent heartbeat message
> from the Connected Machine agent, the status automatically changes
> back to **Connected**.
>
> If a machine remains disconnected for 45 days, its status might change
> to **Expired**. … The credential is valid for up to 90 days and
> renews every 45 days.

### Service limits

> There's no limit to the number of Arc-enabled servers and VM
> extensions you can deploy in a resource group or subscription. The
> standard 800 instance limit per resource group limit does apply to
> the Azure Arc Private Link Scope resource type.

### Data residency

> By default, customer data stays within the region the customer deploys
> the service instance in. For regions with data residency requirements,
> customer data is always kept within the same region.

### Supported environments

> Azure Arc-enabled servers supports the management of physical servers
> and virtual machines hosted _outside_ of Azure. … Azure Arc-enabled
> servers isn't designed or supported to enable management of virtual
> machines running in Azure.

### Lighthouse support

> This service supports Azure Lighthouse, which lets service providers
> sign in to their own tenant to manage subscriptions and resource
> groups that customers have delegated.
