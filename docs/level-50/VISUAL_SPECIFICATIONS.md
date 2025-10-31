---
layout: default
title: Level 50 Visual Asset Specifications
nav_exclude: true
---

# Level 50 Visual Asset Specifications

Purpose: Detailed design briefs for all Level 50 visual assets (Assets 21–23)
Created: October 31, 2025
Asset Registry: See `docs/assets/images/README.md` for short specs and usage

---

## Module 1: Cloud Computing Fundamentals

### Asset 21: Cloud Service Models Pyramid

Context:
This diagram introduces the foundational concept of cloud service models (IaaS, PaaS, SaaS) showing the layers of responsibility and abstraction. Essential for all learners to understand the differences between service models and when to use each.

Design Constraints:
- Canvas 800x600 px, 50px margins
- Use Microsoft color palette: Blue gradient from light (SaaS) to dark (IaaS)
- Minimum font size 14pt for readability at 600px width
- Maintain WCAG AA color contrast ratios

Content Requirements:
- Pyramid or stack diagram with 3 layers
- Top layer: SaaS (Software as a Service)
  - Examples: Microsoft 365, Salesforce, Slack
  - Customer manages: Data, Access
  - Provider manages: Applications, Runtime, Middleware, OS, Virtualization, Servers, Storage, Networking
- Middle layer: PaaS (Platform as a Service)
  - Examples: Azure App Service, Google App Engine, Heroku
  - Customer manages: Data, Access, Applications
  - Provider manages: Runtime, Middleware, OS, Virtualization, Servers, Storage, Networking
- Bottom layer: IaaS (Infrastructure as a Service)
  - Examples: Azure VMs, Amazon EC2, Google Compute Engine
  - Customer manages: Data, Access, Applications, Runtime, Middleware, OS
  - Provider manages: Virtualization, Servers, Storage, Networking

Visual Elements:
- Clear layer separation with distinct colors
- Icons representing each service type
- Responsibility matrix on the right side
- Customer vs Provider responsibility indicators

Typography:
- Headers: Segoe UI Bold, 18pt
- Body text: Segoe UI Regular, 14pt
- Examples: Segoe UI Italic, 12pt

Reference Materials:
- Microsoft Azure service model documentation
- AWS shared responsibility model diagrams
- Google Cloud service comparison charts

---

## Module 2: Security & Compliance Fundamentals

### Asset 22: CIA Triad Security Model

Context:
This diagram illustrates the three foundational pillars of information security. Critical for understanding how all security controls and compliance requirements map back to these core principles.

Design Constraints:
- Canvas 700x700 px (square format), 50px margins
- Use security-themed color palette: Red (Confidentiality), Green (Integrity), Blue (Availability)
- Minimum font size 12pt for readability
- Maintain WCAG AA color contrast ratios

Content Requirements:
- Triangle or three interconnected circles showing CIA relationship
- Confidentiality (Red):
  - Definition: "Ensuring information is accessible only to authorized individuals"
  - Examples: Encryption, Access controls, Authentication
  - Threats: Data breaches, Unauthorized access, Social engineering
- Integrity (Green):
  - Definition: "Ensuring information remains accurate and unaltered"
  - Examples: Digital signatures, Checksums, Version control
  - Threats: Data corruption, Unauthorized modification, Malware
- Availability (Blue):
  - Definition: "Ensuring information is accessible when needed"
  - Examples: Redundancy, Backups, Load balancing
  - Threats: DoS attacks, Hardware failures, Natural disasters

Visual Elements:
- Central intersection showing interdependence
- Icons for each pillar (lock, shield, uptime symbol)
- Examples and threats in smaller text around each pillar
- Clean, professional security-focused design

Typography:
- Headers: Segoe UI Bold, 16pt
- Definitions: Segoe UI Regular, 14pt
- Examples/Threats: Segoe UI Regular, 11pt

Reference Materials:
- NIST cybersecurity framework
- ISO 27001 security principles
- Microsoft security fundamentals documentation

---

## Module 3: Microsoft Azure Introduction

### Asset 23: Azure Global Infrastructure Map

Context:
This diagram shows Azure's global reach and infrastructure components. Important for understanding data residency, compliance options, and performance optimization through geographic distribution.

Design Constraints:
- Canvas 1200x700 px (wide format for world map), 50px margins
- Use Azure brand colors: Azure Blue (#0078D4) as primary
- Minimum font size 10pt for map labels, 12pt for legends
- Maintain WCAG AA color contrast ratios

Content Requirements:
- World map as background (simplified, professional style)
- Azure Regions marked with blue circles
  - Major regions: US East/West, Europe North/West, Asia Southeast/East
  - 60+ regions total (representative sampling, not all)
- Availability Zones shown as smaller circles within regions
  - Indicate 3+ zones per region where applicable
- Edge Locations/CDN marked with smaller dots
  - 100+ locations globally (representative sampling)
- Paired Regions connected with dotted lines
  - Show disaster recovery relationships

Visual Elements:
- Legend explaining region types and symbols
- Callout boxes highlighting key regional features:
  - "Data Residency & Compliance"
  - "Low Latency & High Performance"
  - "Disaster Recovery & High Availability"
- Statistics box: "60+ Regions, 3+ Availability Zones, 100+ Edge Locations"

Typography:
- Title: Segoe UI Bold, 18pt
- Region labels: Segoe UI Regular, 10pt
- Legend: Segoe UI Regular, 12pt
- Callouts: Segoe UI Semibold, 11pt

Reference Materials:
- Azure global infrastructure documentation
- Azure regions and availability zones maps
- Microsoft data center location information

---

## Asset Creation Guidelines

### Design Standards
- All assets follow Microsoft Design Language principles
- Consistent color palette across all Level 50 assets
- Accessibility compliance (WCAG AA)
- Scalable vector format (SVG) preferred
- Fallback PNG at 2x resolution for compatibility

### File Naming Convention
- `level-50-asset-[number]-[descriptive-name].svg`
- Examples:
  - `level-50-asset-21-cloud-service-models.svg`
  - `level-50-asset-22-cia-triad.svg`
  - `level-50-asset-23-azure-global-infrastructure.svg`

### Integration Requirements
- Assets must integrate with Jekyll markdown
- Responsive design for mobile viewing
- Alt text provided for accessibility
- Caption support for additional context

### Quality Assurance
- Review by subject matter experts
- Accessibility testing with screen readers
- Mobile responsiveness validation
- Print-friendly versions when applicable

---

## Asset Usage in Content

### Cloud Service Models Pyramid (Asset 21)
- Used in: `cloud-computing-primer.md`
- Context: Service models explanation section
- Purpose: Visual comparison of IaaS, PaaS, SaaS responsibilities

### CIA Triad Security Model (Asset 22)
- Used in: `security-compliance-basics.md`
- Context: CIA triad principles section
- Purpose: Foundational security concepts visualization

### Azure Global Infrastructure Map (Asset 23)
- Used in: `microsoft-azure-overview.md`
- Context: Azure global infrastructure section
- Purpose: Geographic distribution and compliance visualization

---

## Designer Handoff Package

### Deliverables Required
1. **Source Files:** Editable format (AI, Sketch, Figma)
2. **Production Files:** SVG and PNG formats
3. **Asset Documentation:** Specifications and usage guidelines
4. **Style Guide:** Color codes, fonts, spacing specifications

### Review Process
1. **Technical Review:** Accuracy of content and terminology
2. **Design Review:** Adherence to Microsoft design standards
3. **Accessibility Review:** WCAG compliance validation
4. **Integration Testing:** Jekyll and markdown compatibility

### Timeline
- **Design Phase:** 1-2 weeks per asset
- **Review Phase:** 3-5 days per asset
- **Revision Phase:** 2-3 days per asset
- **Total Estimated:** 3-4 weeks for all Level 50 assets

---

**Specifications Last Updated:** October 31, 2025
**Designer Handoff:** Ready for external design team
**Integration Target:** November 2025
