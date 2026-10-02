---
title: "Azure management tools"
description: "The Azure portal, Cloud Shell, Azure CLI, Azure PowerShell, ARM templates and Bicep, and Azure Copilot: what each tool is for and where it's available."
lastVerified: 2026-10-02
sidebar:
  order: 4
---

You can manage Azure through a browser, a command line, code, or a chat assistant. Every tool sends its requests to Azure Resource Manager, which checks your identity and permissions before it acts. So the tools differ in how you work, not in what you're allowed to do.

## Azure portal

The **Azure portal** is a web console for managing Azure through a graphical interface. You can create and manage resources, build custom dashboards, and monitor what you've deployed. The portal is a good place to start learning, because you can see each setting.

The portal runs in every Azure datacenter and updates without maintenance downtime.

## Azure Cloud Shell

**Azure Cloud Shell** is a terminal in your browser, already signed in with your Azure account. You choose Bash or PowerShell. It has the Azure CLI, Azure PowerShell, and other common tools preinstalled, so there's nothing to install on your machine.

Open it from the Cloud Shell icon in the portal or at shell.azure.com. A session times out after 20 minutes without activity. Your files persist in a 5-GB file share in an Azure storage account, which you pay for at normal storage rates ([Microsoft Learn](https://learn.microsoft.com/azure/cloud-shell/overview)).

## Azure CLI and Azure PowerShell

Both tools run commands against Azure from a terminal or a script. They can do the same things. Pick the one whose syntax you prefer.

| | Azure CLI | Azure PowerShell |
|---|---|---|
| Command style | `az` commands, for example `az group create` | PowerShell cmdlets, for example `New-AzResourceGroup` |
| Runs on | Windows, Linux, macOS, and Cloud Shell | Windows, Linux, macOS, and Cloud Shell |
| Suits | People used to Bash and Linux tools | People used to PowerShell and Windows administration |

Put commands in a script and you can repeat a deployment or a routine task the same way every time.

## Infrastructure as code: ARM templates and Bicep

**Infrastructure as code** means you describe your environment in files instead of clicking through the portal. You store the files in source control and deploy the same environment as often as you need.

- **ARM templates** are JSON files that declare the resources you want. Azure Resource Manager validates the template, works out the order of dependencies, and creates resources in parallel where it can.
- **Bicep** is a simpler language for the same thing. A Bicep file is shorter and easier to read than the equivalent JSON, and Azure converts it to an ARM template when you deploy. Bicep supports every Azure resource type and API version as soon as it's released, and it's free and open source ([Microsoft Learn](https://learn.microsoft.com/azure/azure-resource-manager/bicep/overview)).

Both are declarative: you describe the end state, not the steps. Deploying the same file twice gives the same result. Many sovereign landing zone accelerators in Level 300 use Bicep or Terraform.

## Azure Copilot

**Azure Copilot** is an AI assistant in the Azure portal and the Azure mobile app ([Microsoft Learn](https://learn.microsoft.com/azure/copilot/overview)). You ask questions or describe a goal in natural language, and it answers, writes queries and scripts, or carries out tasks for you.

- It can only see the resources you have permission to see, and only do what you're allowed to do. It asks you to confirm before it takes any action.
- Agents in Azure Copilot extend it to multistep, agent-style tasks.
- Today's capabilities are included at no extra cost, except the Observability Agent, which has usage-based charges.
- It's available in 19 languages.
- **It isn't available in Azure Government or Azure operated by 21Vianet.**

Some older pages and training call it "Microsoft Copilot in Azure" or "Copilot in Azure." It's the same product. Treat its suggestions like a colleague's: check them, and review changes before you apply them to production.

## Azure Arc

**Azure Arc** brings resources outside Azure, such as servers, Kubernetes clusters, and databases in your datacenter or another cloud, into Azure Resource Manager. You then manage them with the same portal, CLI, PowerShell, policies, and role-based access control as your Azure resources. Azure Arc is central to the hybrid and sovereign scenarios in this course, and Level 100 has a module about it.

## Which tool when

| Task | Good choice |
|---|---|
| Explore a service and see its settings | Azure portal |
| Run a quick command without installing anything | Cloud Shell |
| Automate a routine task | Azure CLI or Azure PowerShell script |
| Deploy the same environment many times | Bicep or ARM templates |
| Ask how to do something, or get a draft query | Azure Copilot (global Azure only) |
| Manage servers and clusters outside Azure | Azure Arc |

## Sources

- [Describe tools for interacting with Azure (Microsoft Learn training)](https://learn.microsoft.com/training/modules/describe-features-tools-manage-deploy-azure-resources/2-describe-interacting-azure)
- [Describe Azure Resource Manager and ARM templates (Microsoft Learn training)](https://learn.microsoft.com/training/modules/describe-features-tools-manage-deploy-azure-resources/4-describe-azure-resource-manager-azure-arm-templates)
- [What is Azure Cloud Shell?](https://learn.microsoft.com/azure/cloud-shell/overview)
- [Azure CLI documentation](https://learn.microsoft.com/cli/azure/)
- [What is Azure PowerShell?](https://learn.microsoft.com/powershell/azure/what-is-azure-powershell)
- [What is Bicep?](https://learn.microsoft.com/azure/azure-resource-manager/bicep/overview)
- [What is Azure Copilot?](https://learn.microsoft.com/azure/copilot/overview)
- [Azure Arc overview](https://learn.microsoft.com/azure/azure-arc/overview)
