---
layout: default
title: Azure Arc-Enabled Servers
parent: Module 4 - Azure Arc Introduction
nav_order: 4.1
---

# Azure Arc-Enabled Servers

{: .no_toc }

## Table of Contents

{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What is Arc-Enabled Servers?

Azure Arc-enabled Servers extends Azure management to Windows and Linux machines hosted outside of Azure - in your datacenter, at the edge, or in other clouds.

<details class="diagram-container">
<summary>View Diagram: Arc-Enabled Servers Architecture</summary>
<div class="diagram-content" markdown="1">

```mermaid
graph LR
    subgraph Azure["☁️ Azure"]
        ARM[Azure Resource Manager]
        POL[Azure Policy]
        MON[Azure Monitor]
        DEF[Microsoft Defender]
    end

    subgraph OnPrem["🏢 On-Premises / Other Clouds"]
        AG[Arc Agent]
        SRV1[Windows Server]
        SRV2[Linux Server]
    end

    ARM <--> AG
    AG --> SRV1
    AG --> SRV2
    POL --> AG
    MON --> AG
    DEF --> AG

    style Azure fill:#e3f2fd,stroke:#0078d4
    style OnPrem fill:#fff3e0,stroke:#ef6c00
```

</div>
</details>

**Key Capabilities:**

- Organize and inventory servers using Azure Resource Manager
- Apply Azure Policy for compliance and configuration
- Monitor with Azure Monitor and Log Analytics
- Protect with Microsoft Defender for Cloud
- Manage updates with Azure Update Management
- Automate with Azure Automation runbooks

**[← Back to Azure Arc Introduction](azure-arc-intro)**

---

## Prerequisites

**Server Requirements:**

- **Windows:** Server 2012 R2 or newer
- **Linux:** Various distributions (Ubuntu 16.04+, RHEL 7+, SUSE 12+, etc.)
- Internet connectivity (outbound HTTPS/443)
- Minimum 2 GB RAM

**Agent Requirements:**

- Connected Machine agent installation
- Outbound connectivity to Azure endpoints
- Local administrator/root privileges for installation

**Azure Requirements:**

- Azure subscription
- Permissions to create resources
- Resource group for Arc servers

---

## Onboarding Process and Architecture

### Installation Methods

**1. Interactive Installation (Single Server):**

```bash
# Linux example
wget https://aka.ms/azcmagent -O ~/install_linux_azcmagent.sh
bash ~/install_linux_azcmagent.sh

# Connect to Azure
azcmagent connect --resource-group "myResourceGroup"   --tenant-id "tenant-id"   --location "eastus"   --subscription-id "subscription-id"
```

**2. Service Principal (Scale Deployment):**

```powershell
# Windows PowerShell example
& "$env:ProgramW6432\AzureConnectedMachineAgentzcmagent.exe" connect `
  --service-principal-id "app-id" `
  --service-principal-secret "secret" `
  --resource-group "myResourceGroup" `
  --tenant-id "tenant-id" `
  --location "eastus" `
  --subscription-id "subscription-id"
```

**3. At-Scale Deployment:**

- Configuration Manager for Windows
- Ansible/Puppet for Linux
- Group Policy for domain-joined Windows

### Architecture

**Components:**

- **Connected Machine Agent:** Runs on each server
- **Instance Metadata Service:** Local endpoint (localhost:40342)
- **Extension Manager:** Manages VM extensions
- **Guest Configuration Agent:** Policy enforcement

**Communication Flow:**

1. Agent authenticates to Azure AD
2. Receives managed identity
3. Reports status and inventory
4. Receives configurations and policies
5. Executes extensions and scripts

---

## Security and Authentication

**Managed Identity:**

- System-assigned managed identity per server
- No stored credentials
- Automatic token rotation
- Least-privilege access

**Certificate-Based Authentication:**

- X.509 certificate for authentication
- Stored securely in OS keystore
- Automatic renewal

**Network Security:**

- Outbound HTTPS only (no inbound)
- Proxy support available
- Private Link support for isolated networks

---

## Applying Azure Policy

**Policy Capabilities:**

- Audit configuration compliance
- Deploy missing extensions
- Enforce security baselines
- Tag management
- Location restrictions

**Example Policies:**

- Require anti-malware extension
- Enforce disk encryption
- Audit password policies
- Require monitoring agent
- Enforce naming conventions

**Implementation:**

```text
1. Create policy assignment
2. Assign to resource group or subscription
3. Policy evaluates every 24 hours
4. Non-compliant resources reported
5. Optional auto-remediation
```

---

## Monitoring and Compliance Reporting

**Azure Monitor Integration:**

- Performance metrics (CPU, memory, disk, network)
- Event logs and syslog
- Custom metrics and logs
- Alert rules and action groups

**Log Analytics:**

- Centralized log collection
- KQL queries for analysis
- Cross-server correlation
- Long-term retention

**Compliance Dashboard:**

- Real-time compliance status
- Policy compliance reporting
- Remediation recommendations
- Historical compliance trends

---

## Update Management Capabilities

**Azure Update Manager:**

- Assess update compliance
- Schedule update deployments
- Pre and post-update scripts
- Update exclusions
- Reporting and auditing

**Update Assessment:**

- Automatic scanning for missing updates
- Security vs. non-security classification
- CVSS scoring for vulnerabilities

**Update Deployment:**

- Maintenance windows
- Phased rollout
- Reboot control
- Rollback capability

---

## Cost Model and Licensing

**Arc-Enabled Servers:**

- **No charge** for Azure Arc itself
- Charges for Azure services consumed:
  - Azure Monitor: ~$2.30/GB ingested
  - Microsoft Defender: ~$15/server/month
  - Azure Automation: ~$0.002/minute
  - Update Management: Included with Azure Automation

**Licensing:**

- Windows Server: Requires valid license
- Linux: Follows distribution license
- Azure Hybrid Benefit: Available for Windows

---

## Use Case Scenarios

### Scenario 1: Data Center Server Management

**Challenge:** 500 Windows/Linux servers across 3 data centers with inconsistent management.

**Solution:**

- Onboard all servers to Azure Arc
- Apply Azure Policy for security baseline
- Centralized monitoring with Azure Monitor
- Unified update management

**Results:**

- 100% visibility across all servers
- 60% faster patch deployment
- Unified compliance reporting
- Reduced management overhead by 40%

### Scenario 2: Multi-Cloud Governance

**Challenge:** Servers in Azure, AWS, and on-premises with fragmented governance.

**Solution:**

- Arc-enable servers in all environments
- Apply consistent Azure policies everywhere
- Deploy Microsoft Defender uniformly
- Centralized security dashboard

**Results:**

- Unified security posture across all clouds
- Consistent compliance reporting
- Reduced tool sprawl
- Single pane of glass management

### Scenario 3: Compliance for Regulated Industry

**Challenge:** Healthcare provider needs HIPAA compliance for 200+ servers.

**Solution:**

- Azure Arc with HIPAA initiative policies
- Microsoft Defender for vulnerability scanning
- Log Analytics for audit logging
- Automated compliance reporting

**Results:**

- 95% compliance score
- Passed HIPAA audit with zero findings
- Automated monthly compliance reports
- Reduced audit preparation time by 70%

---

## Best Practices

**1. Use Service Principals for Scale**

- Automate onboarding with service principals
- Store secrets securely (Azure Key Vault)
- Rotate credentials regularly

**2. Organize with Resource Groups**

- Group by environment (prod, dev, test)
- Group by location or business unit
- Use tags for additional metadata

**3. Implement Gradual Rollout**

- Pilot with small group first
- Validate monitoring and policies
- Gradually expand to production

**4. Monitor Agent Health**

- Alert on agent disconnection
- Regular connectivity validation
- Document troubleshooting procedures

**5. Leverage Automation**

- Use ARM templates for consistency
- Automate policy assignments
- Script repetitive tasks

---

## Troubleshooting

**Agent Won't Connect:**

- Verify internet connectivity to Azure endpoints
- Check firewall rules
- Validate Azure subscription and permissions
- Review agent logs

**Policy Not Applying:**

- Wait for evaluation cycle (24 hours)
- Force policy scan: `Start-GuestConfigurationAssessment`
- Check for policy conflicts
- Verify resource group assignment

**Monitoring Data Missing:**

- Verify Log Analytics agent extension installed
- Check workspace configuration
- Validate network connectivity
- Review data collection rules

---

## Next Steps

- [Arc-Enabled Kubernetes →](azure-arc-kubernetes)
- [Arc Data Services →](azure-arc-data-services)
- [Azure Arc Quiz →](azure-arc-quiz)
- [Back to Arc Overview →](azure-arc-intro)

**External Resources:**

- [Azure Arc-enabled servers documentation](https://learn.microsoft.com/en-us/azure/azure-arc/servers/)
- [Onboarding guide](https://learn.microsoft.com/en-us/azure/azure-arc/servers/onboard-portal)

---

**Last Updated:** October 2025
