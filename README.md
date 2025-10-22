# Microsoft Sovereign Cloud Brain Trek

Master Sovereign Cloud, Azure Local, and Edge AI Technologies

A comprehensive learning journey for architects and solutions professionals

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Microsoft Azure](https://img.shields.io/badge/Microsoft%20Azure-0078D4?logo=microsoftazure&logoColor=white)](https://azure.microsoft.com/)
[![Microsoft Learn](https://img.shields.io/badge/Microsoft%20Learn-258ffa?logo=microsoft&logoColor=white)](https://learn.microsoft.com/)
[![GitHub Copilot](https://img.shields.io/badge/GitHub%20Copilot-000000?logo=githubcopilot&logoColor=white)](https://github.com/features/copilot)

[![Azure Arc](https://img.shields.io/badge/Azure%20Arc-0078D4?logo=microsoftazure&logoColor=white)](https://azure.microsoft.com/en-us/products/azure-arc/)
[![Azure Local](https://img.shields.io/badge/Azure%20Local-0078D4?logo=microsoftazure&logoColor=white)](https://learn.microsoft.com/en-us/azure/azure-local/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?logo=kubernetes&logoColor=white)](https://kubernetes.io/)
[![Claude Haiku](https://img.shields.io/badge/Claude%20Haiku-191919?logo=anthropic&logoColor=white)](https://www.anthropic.com/claude)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Documentation](https://img.shields.io/badge/Documentation-Complete-brightgreen.svg)](docs/README.md)

## Overview

Welcome to the **Microsoft Sovereign Cloud Brain Trek** – your comprehensive skilling platform for mastering sovereign cloud technologies, hybrid infrastructure, and edge AI. This repository contains structured learning modules for sales and technical professionals to develop deep expertise in:

- **Microsoft Sovereign Cloud** (Sovereign Public, Private, and National Partner Clouds)
- **Azure Local** (Connected and Disconnected Operations)
- **Azure Arc** (Hybrid and Multi-Cloud Management)
- **Retrieval-Augmented Generation (RAG)** on Azure Arc for Edge

## Target Audience

- **Sales & Pre-Sales:** Account Executives, Solution Specialists, and Technical Sales Professionals
- **Technical Professionals:** Cloud Architects, Field Engineers, and AI Developers

## Learning Path Structure

The skilling plan is organized into three progressive levels:

| Level | Objective | Duration |
|-------|-----------|----------|
| **100** | **Foundational:** Understand the "what" and "why" | 2-4 weeks |
| **200** | **Intermediate:** Design solutions and handle objections | 4-6 weeks |
| **300** | **Advanced:** Lead deployments and provide expert guidance | 8-12 weeks |

### Learning Journey Map

```mermaid
graph TD
    Start([Start Your Journey]) --> L100[Level 100: Foundations]
    
    L100 --> M1[Module 1: Digital Sovereignty]
    L100 --> M2[Module 2: Cloud Models]
    L100 --> M3[Module 3: Azure Local]
    L100 --> M4[Module 4: Azure Arc]
    L100 --> M5[Module 5: Edge RAG]
    
    M1 --> Q1{Quiz 1}
    M2 --> Q2{Quiz 2}
    M3 --> Q3{Quiz 3}
    M4 --> Q4{Quiz 4}
    M5 --> Q5{Quiz 5}
    
    Q1 & Q2 & Q3 & Q4 & Q5 --> L200[Level 200: Intermediate]
    
    L200 --> M6[Module 6: Presales & Discovery]
    L200 --> M7[Module 7: Compliance & Security]
    L200 --> M8[Module 8: Azure Local Deep Dive]
    L200 --> M9[Module 9: Arc Management]
    L200 --> M10[Module 10: RAG Implementation]
    L200 --> M11[Module 11: Hands-on Labs]
    
    M6 & M7 --> Q6{Quiz 6}
    M8 --> Q7{Quiz 7}
    M9 --> Q8{Quiz 8}
    M10 --> Q9{Quiz 9}
    
    Q6 & Q7 & Q8 & Q9 & M11 --> L300[Level 300: Advanced]
    
    L300 --> M12[Module 12: Azure Local Advanced]
    L300 --> M13[Module 13: Arc Advanced]
    L300 --> M14[Module 14: RAG Optimization]
    L300 --> M15[Module 15: Advanced Labs]
    L300 --> M16[Module 16: Capstone Project]
    
    M12 --> Q10{Quiz 10}
    M13 --> Q11{Quiz 11}
    M14 --> Q12{Quiz 12}
    
    Q10 & Q11 & Q12 & M15 & M16 --> Cert([Certification Ready])
    
    style Start fill:#00C853,stroke:#00C853,stroke-width:3px,color:#000
    style L100 fill:#0091EA,stroke:#0091EA,stroke-width:3px,color:#fff
    style L200 fill:#FF6D00,stroke:#FF6D00,stroke-width:3px,color:#fff
    style L300 fill:#AA00FF,stroke:#AA00FF,stroke-width:3px,color:#fff
    style Cert fill:#00C853,stroke:#00C853,stroke-width:3px,color:#000
    
    style M1 fill:#fff,stroke:#0091EA,stroke-width:2px,color:#000
    style M2 fill:#fff,stroke:#0091EA,stroke-width:2px,color:#000
    style M3 fill:#fff,stroke:#0091EA,stroke-width:2px,color:#000
    style M4 fill:#fff,stroke:#0091EA,stroke-width:2px,color:#000
    style M5 fill:#fff,stroke:#0091EA,stroke-width:2px,color:#000
    
    style M6 fill:#fff,stroke:#FF6D00,stroke-width:2px,color:#000
    style M7 fill:#fff,stroke:#FF6D00,stroke-width:2px,color:#000
    style M8 fill:#fff,stroke:#FF6D00,stroke-width:2px,color:#000
    style M9 fill:#fff,stroke:#FF6D00,stroke-width:2px,color:#000
    style M10 fill:#fff,stroke:#FF6D00,stroke-width:2px,color:#000
    style M11 fill:#fff,stroke:#FF6D00,stroke-width:2px,color:#000
    
    style M12 fill:#fff,stroke:#AA00FF,stroke-width:2px,color:#000
    style M13 fill:#fff,stroke:#AA00FF,stroke-width:2px,color:#000
    style M14 fill:#fff,stroke:#AA00FF,stroke-width:2px,color:#000
    style M15 fill:#fff,stroke:#AA00FF,stroke-width:2px,color:#000
    style M16 fill:#fff,stroke:#AA00FF,stroke-width:2px,color:#000
    
    style Q1 fill:#FFD600,stroke:#FFD600,stroke-width:2px,color:#000
    style Q2 fill:#FFD600,stroke:#FFD600,stroke-width:2px,color:#000
    style Q3 fill:#FFD600,stroke:#FFD600,stroke-width:2px,color:#000
    style Q4 fill:#FFD600,stroke:#FFD600,stroke-width:2px,color:#000
    style Q5 fill:#FFD600,stroke:#FFD600,stroke-width:2px,color:#000
    style Q6 fill:#FFD600,stroke:#FFD600,stroke-width:2px,color:#000
    style Q7 fill:#FFD600,stroke:#FFD600,stroke-width:2px,color:#000
    style Q8 fill:#FFD600,stroke:#FFD600,stroke-width:2px,color:#000
    style Q9 fill:#FFD600,stroke:#FFD600,stroke-width:2px,color:#000
    style Q10 fill:#FFD600,stroke:#FFD600,stroke-width:2px,color:#000
    style Q11 fill:#FFD600,stroke:#FFD600,stroke-width:2px,color:#000
    style Q12 fill:#FFD600,stroke:#FFD600,stroke-width:2px,color:#000
```

**Legend:**
- 🔵 **Level 100 (Blue)**: Foundational concepts - white boxes with blue borders
- 🟠 **Level 200 (Orange)**: Intermediate skills - white boxes with orange borders
- 🟣 **Level 300 (Purple)**: Advanced expertise - white boxes with purple borders
- 🟡 **Quizzes (Yellow)**: Knowledge validation checkpoints - bright yellow diamonds
- 🟢 **Start/End (Green)**: Journey milestones - bright green rounded boxes

## Documentation Structure

```text
docs/
├── index.md                    # Home page
├── introduction.md             # Project introduction
├── level-100/                  # Foundational concepts
├── level-200/                  # Intermediate skills
├── level-300/                  # Advanced expertise
├── resources/                  # Additional resources
└── assets/                     # Images and diagrams
```

## Getting Started

### For Learners
1. **Start with Level 100** in `/docs/level-100/README.md` - Foundational concepts
2. **Progress to Level 200** for intermediate skills and solution design
3. **Complete Level 300** for advanced expertise and deployment leadership

### For Content Contributors
1. **Review** [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines
2. **Check** [.github/PROJECT_FILES.md](.github/PROJECT_FILES.md) for current project status
3. **Reference** [docs/README.md](docs/README.md) for content structure

### For Deploying the Site
1. **See** [docs/README.md](docs/README.md) for content organization
2. **Review** Jekyll configuration (coming soon)
3. **Test locally** before GitHub Pages deployment

## Key Technologies Covered

- Microsoft Sovereign Cloud
- Azure Local (formerly Azure Stack HCI)
- Azure Arc
- Azure Kubernetes Service (AKS)
- Edge RAG (Retrieval-Augmented Generation)
- Sovereign Landing Zones (SLZ)
- Zero Trust Security

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Content Contributions

New content should follow:
1. Level/module structure in `docs/level-XXX/`
2. YAML frontmatter template (see existing files)
3. Markdown formatting standards
4. Visual asset placeholder format (see examples in existing files)

### Jekyll Deployment

Site deployment preparation is underway for late November 2025. See [deployment status](#deployment-status) below.

## Resources

- [Microsoft Sovereign Cloud Documentation](https://learn.microsoft.com/en-us/industry/sovereign-cloud/)
- [Azure Local Documentation](https://learn.microsoft.com/en-us/azure/azure-local/)
- [Azure Arc Documentation](https://learn.microsoft.com/en-us/azure/azure-arc/overview)
- [Microsoft Learn Training](https://learn.microsoft.com/en-us/training/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This skilling plan is based on Microsoft's official documentation and best practices for Sovereign Cloud, Azure Local, and Edge AI solutions.

---

**Status:** ✅ Content Complete | Ready for Designer Engagement & Jekyll Deployment  
**Last Updated:** October 21, 2025  
**Repository:** [microsoft-sovereign-cloud-brain-trek](https://github.com/jonathan-vella/microsoft-sovereign-cloud-brain-trek)
