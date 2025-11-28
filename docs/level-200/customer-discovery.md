---
layout: default
title: Customer Discovery
parent: Pre-Sales & Solution Design
nav_order: 4
---

# Customer Discovery Framework

## Overview

Effective customer discovery is the foundation of successful solution design. This page covers discovery interview techniques, questionnaire frameworks, stakeholder mapping, and requirements documentation for Microsoft Sovereign Cloud and Edge AI solutions.

---

## Discovery Interview Methodology

### Pre-Interview Preparation (1 hour)

**Research the Customer**

- Company background and financials
- Industry and regulatory environment
- Recent press releases and announcements
- Existing Microsoft relationships
- Competitive landscape

**Prepare Questions & Agenda**

- Customize questions for their industry
- Prepare use-case examples
- Create interview agenda (share with customer)
- Arrange for technical and business stakeholders
- Set expectations for follow-up activities

**Arrange Environment**

- Schedule 2.5-3 hours across multiple sessions if needed
- Arrange video conference with screen sharing
- Have whiteboard/collaboration tool ready
- Prepare to take detailed notes
- Have backup contact if attendee drops

### Interview Structure

#### Phase 1: Opening (10-15 minutes)

```text
Agenda Setting:
1. Confirm purpose of discovery
2. Outline topics to cover
3. Set expectations for outcomes
4. Confirm time and next steps

Example Opening:
"Thanks for taking time today. Our goal is to understand your
environment, challenges, and success criteria so we can design
a solution that truly meets your needs. We'll cover:
- Your business drivers and goals
- Current infrastructure and pain points
- Technical requirements and constraints
- Timeline, budget, and decision criteria

This should take about 2.5 hours total. I'll be taking notes,
and we'll follow up with a written summary. Does this work?"
```

#### Phase 2: Strategic Level (30-45 minutes)

**Business Context Questions**

```text
1. Business Drivers
   Q: "What's driving your interest in edge AI/sovereignty?"
   Listen for: Compliance, cost, latency, competitive pressure

2. Strategic Alignment
   Q: "How does this align with your organization's strategy?"
   Listen for: Cloud adoption plans, data strategy, transformation

3. Current State Pain Points
   Q: "What's not working well in your current environment?"
   Listen for: Latency, cost, security, compliance, vendor lock-in

4. Success Metrics
   Q: "How will we know this project was successful?"
   Listen for: Quantifiable metrics (latency, cost, throughput, etc.)

5. Executive Sponsorship
   Q: "Who are the executive sponsors for this initiative?"
   Listen for: Budget authority, commitment level, decision power
```

**Key Insight Questions**

```text
6. Competitor Pressure
   Q: "Are any of your competitors doing similar initiatives?"
   Listen for: Urgency, competitive threat, market trends

7. Regulatory Requirements
   Q: "What regulatory compliance is mandatory?"
   Listen for: GDPR, FedRAMP, HIPAA, data residency, audit needs

8. Time to Value
   Q: "When do you need this capability operational?"
   Listen for: Timeline urgency, go-live date, pilot expectations

9. Budget Availability
   Q: "What investment level have you secured?"
   Listen for: CapEx vs. OpEx, budget cycles, funding constraints
```

#### Phase 3: Operational Level (45-60 minutes)

**Current Infrastructure**

```text
1. IT Infrastructure Overview
   Q: "Can you describe your current data center/cloud setup?"
   Listen for:
   - On-premises data centers
   - Cloud adoption level (single cloud vs. multi-cloud)
   - Server count and types
   - Storage and network architecture
   - Geographic distribution

2. Applications & Workloads
   Q: "What applications are critical to your business?"
   Listen for:
   - ERP, CRM, databases
   - AI/ML investments
   - Custom applications
   - Planned decommissions or modernizations

3. Data Environment
   Q: "How much data do you store and where?"
   Listen for:
   - Data volume growth rate
   - Data types (structured, unstructured, streaming)
   - Data residency requirements
   - Data governance policies

4. Current Operations Model
   Q: "How do you currently manage your infrastructure?"
   Listen for:
   - Operations team size and skills
   - Monitoring and logging tools
   - Incident response processes
   - Support model (in-house vs. outsourced)
```

**Skills & Capabilities**

```text
5. Technical Team Maturity
   Q: "What's your team's experience with cloud and containers?"
   Listen for:
   - Kubernetes/container experience
   - Azure or other cloud platform maturity
   - DevOps practices (CI/CD, IaC)
   - Machine learning expertise

6. Organization Readiness
   Q: "How mature is your DevOps/agile process?"
   Listen for:
   - Agile transformation stage
   - Change management maturity
   - Deployment frequency
   - Incident response capability

7. Training & Support Needs
   Q: "What support and training would be most valuable?"
   Listen for:
   - Hands-on labs vs. documentation
   - On-site vs. remote training
   - Certification requirements
   - Ongoing support model preference
```

#### Phase 4: Tactical Level (30-45 minutes)

**Specific Workload Details**

```text
1. Workload Characteristics
   Q: "Can you describe the specific workloads you want to run?"
   Listen for:
   - Transaction volume and frequency
   - Data access patterns
   - Peak vs. average load
   - Performance requirements (latency, throughput)
   - Consistency requirements

2. Data Sovereignty & Security
   Q: "What are your data residency and security requirements?"
   Listen for:
   - Data location restrictions
   - Encryption requirements
   - Access control policies
   - Audit and compliance needs
   - Industry-specific regulations

3. Integration Requirements
   Q: "What systems must this integrate with?"
   Listen for:
   - Existing databases and applications
   - Identity and authentication systems
   - API requirements
   - Data flow patterns
   - Third-party integrations

4. Deployment Model
   Q: "How many locations would deploy this solution?"
   Listen for:
   - Single site vs. multiple sites
   - Geographic distribution
   - Autonomous vs. centralized operations
   - Disaster recovery requirements
```

**Technical Constraints**

```text
5. Infrastructure Constraints
   Q: "What are your infrastructure constraints?"
   Listen for:
   - Network bandwidth limitations
   - Power and cooling capacity
   - Physical space constraints
   - Hardware refresh cycles
   - Procurement restrictions

6. Compliance & Audit
   Q: "What compliance audits do you undergo?"
   Listen for:
   - Annual compliance audits
   - Specific frameworks (ISO 27001, SOC 2, FedRAMP)
   - Audit access requirements
   - Documentation needs
   - Third-party audit readiness
```

#### Phase 5: Closing (15-20 minutes)

```text
1. Validate Understanding
   "Let me summarize what I heard to make sure I understand correctly..."

2. Identify Next Steps
   "Based on this conversation, here's what I propose:"
   - Detailed solution design (2-3 weeks)
   - Cost modeling and ROI analysis
   - Proof of concept proposal
   - Executive presentation

3. Confirm Timeline
   "If we move forward, when would you want to see the proposal?"

4. Establish Ongoing Communication
   "Who should be my primary contact for follow-up questions?"

5. Schedule Next Meeting
   "Let's schedule a 30-minute follow-up for next week to discuss
    any questions that come up. Does [date/time] work?"
```

---

## Stakeholder Mapping

### Stakeholder Identification

```text
EXECUTIVE STAKEHOLDERS (Influence: High, Interest: Medium)
├── CIO/Chief Technology Officer
│   ├─ Concerns: Strategic alignment, total cost of ownership
│   ├─ Priorities: Risk mitigation, capability modernization
│   └─ Best approach: Executive summary, ROI analysis
│
├── VP Operations
│   ├─ Concerns: Operational impact, support requirements
│   ├─ Priorities: Efficiency, cost control, team readiness
│   └─ Best approach: Operations model, support plan
│
└── Chief Information Security Officer
    ├─ Concerns: Security, compliance, data protection
    ├─ Priorities: Risk reduction, audit readiness
    └─ Best approach: Security architecture, compliance roadmap

TECHNICAL STAKEHOLDERS (Influence: High, Interest: High)
├── Infrastructure Lead
│   ├─ Concerns: Integration, operational complexity
│   ├─ Priorities: Manageability, uptime, standardization
│   └─ Best approach: Architecture details, runbooks
│
├── Database Administrator
│   ├─ Concerns: Data consistency, performance, backup/recovery
│   ├─ Priorities: Data integrity, availability, cost
│   └─ Best approach: Technical specifications, performance analysis
│
├── Application Owner(s)
│   ├─ Concerns: Feature completeness, performance
│   ├─ Priorities: Functionality, user experience, time to value
│   └─ Best approach: Use cases, performance targets, timeline
│
└── Security Team
    ├─ Concerns: Vulnerabilities, compliance gaps
    ├─ Priorities: Security posture, audit trail, access control
    └─ Best approach: Security features, compliance controls

BUSINESS STAKEHOLDERS (Influence: Medium, Interest: High)
├── Business Unit Owner
│   ├─ Concerns: Business value, ROI, time to market
│   ├─ Priorities: Revenue impact, competitive advantage
│   └─ Best approach: Use cases, business outcomes, success metrics
│
└── Finance Lead
    ├─ Concerns: Cost, budget impact, approval process
    ├─ Priorities: Financial feasibility, cost control
    └─ Best approach: Cost model, ROI analysis, financing options

INFLUENCERS (Influence: Medium, Interest: Medium)
├── Project Manager
├── System Integrator/Partner
└── Industry Analyst/Advisor
```

### Stakeholder Engagement Strategy

```text
For Executive Stakeholders:
- Schedule 30-45 minute executive briefing
- Prepare 1-page executive summary
- Focus on business value and risk mitigation
- Show ROI and competitive advantage
- Include industry benchmarks and case studies

For Technical Stakeholders:
- Schedule 1-2 hour technical deep-dive sessions
- Prepare detailed architecture diagrams
- Show performance benchmarks
- Discuss integration points and dependencies
- Address concerns about operational complexity

For Business Stakeholders:
- Schedule 30-minute business impact sessions
- Focus on revenue, cost, and competitive benefits
- Show time to value and phased approach
- Address budget and resource concerns
- Share customer success stories
```

---

## Requirements Documentation Template

### Workload Requirements Document

```text
PROJECT NAME: [Customer Name] - Edge RAG Implementation
DATE: [Date]
PREPARED BY: [Your Name]

SECTION 1: WORKLOAD OVERVIEW
─────────────────────────────
Workload Name: [Description]
Primary Use Case: [What problem does it solve?]
Business Owner: [Name, Title, Contact]
Technical Owner: [Name, Title, Contact]
Go-Live Target: [Date]
Expected Users: [Number]
Geographic Scope: [Single location, Multi-location, etc.]

SECTION 2: FUNCTIONAL REQUIREMENTS
──────────────────────────────────
[List specific capabilities needed]

Example:
- Process natural language queries
- Retrieve context from 100K+ documents
- Generate responses <500ms
- Support 100 concurrent users
- Integrate with existing authentication system

SECTION 3: TECHNICAL REQUIREMENTS
─────────────────────────────────
Queries/Second Peak: [Number]
Concurrent Users: [Number]
Data Volume: [Amount]
Response Latency Target: [p95 latency]
Availability Target: [SLA %]
Disaster Recovery: [RPO/RTO]
Geographic Deployment: [Single/Multi-region]

SECTION 4: DATA REQUIREMENTS
───────────────────────────
Data Source Systems: [List systems]
Data Types: [Structured, Unstructured, etc.]
Data Volume Growth: [% per year]
Data Residency: [Geographic constraints]
Data Classification: [Sensitivity level]
Retention Requirements: [Duration]

SECTION 5: COMPLIANCE & SECURITY
────────────────────────────────
Regulatory Requirements: [GDPR, HIPAA, FedRAMP, etc.]
Data Classification: [Public, Confidential, etc.]
Encryption Requirements: [At rest, in transit]
Authentication: [SSO, MFA requirements]
Audit Requirements: [Audit logging, compliance reporting]
Compliance Certifications: [ISO 27001, SOC 2, etc.]

SECTION 6: INTEGRATION REQUIREMENTS
───────────────────────────────────
Source Systems: [Systems providing data]
Destination Systems: [Systems consuming results]
APIs Needed: [API specifications]
Data Flows: [Frequency, volume, format]
Third-Party Integrations: [SaaS tools, etc.]

SECTION 7: OPERATIONAL REQUIREMENTS
───────────────────────────────────
Support Hours: [24/7, business hours]
On-Call Support: [Yes/No]
Incident Response: [SLA for critical issues]
Planned Maintenance: [Window constraints]
Monitoring & Alerting: [Required monitoring]
Logging & Retention: [Log retention requirements]

SECTION 8: ASSUMPTIONS & CONSTRAINTS
───────────────────────────────────
Assumptions:
- [List assumptions about environment, scope, timeline]

Constraints:
- [Budget limits, timeline, regulatory, etc.]

Out of Scope:
- [Things not included in this assessment]

SECTION 9: SUCCESS CRITERIA
──────────────────────────
Quantitative Metrics:
- Response latency: <500ms p95
- System availability: >99.9%
- Query accuracy: >95%
- Cost per query: <$0.05

Qualitative Metrics:
- User satisfaction: 4+/5
- Team capability: Can operate independently
- Support effectiveness: Timely issue resolution

SECTION 10: SIGN-OFF
────────────────────
Business Owner: _________________ Date: _______
Technical Owner: ________________ Date: _______
Project Manager: ________________ Date: _______
Solutions Architect: _____________ Date: _______
```

---

## Discovery Interview Checklist

```text
PRE-INTERVIEW PREPARATION
☐ Research customer background
☐ Review industry and competitive landscape
☐ Prepare customized questions
☐ Create interview agenda
☐ Arrange video conference setup
☐ Prepare collaboration tools
☐ Set expectations with customer

INTERVIEW EXECUTION
☐ Start with opening/agenda review
☐ Ask strategic business questions
☐ Probe for pain points and priorities
☐ Understand operational constraints
☐ Gather technical requirements
☐ Map stakeholders and decision criteria
☐ Document all responses
☐ Validate understanding (summarize)
☐ Schedule follow-up

POST-INTERVIEW FOLLOW-UP
☐ Send thank you email within 24 hours
☐ Prepare discovery summary document
☐ Fill in requirements template
☐ Identify gaps and follow-up questions
☐ Schedule technical deep-dive (if needed)
☐ Begin initial solution design
☐ Schedule executive presentation
```

---

## Common Discovery Pitfalls to Avoid

```text
❌ PITFALL 1: Talking too much
   ✓ SOLUTION: Practice active listening, ask open-ended questions

❌ PITFALL 2: Not asking follow-up questions
   ✓ SOLUTION: Prepare "Why?" and "Tell me more" prompts

❌ PITFALL 3: Skipping stakeholder mapping
   ✓ SOLUTION: Identify all decision makers early

❌ PITFALL 4: Missing compliance requirements
   ✓ SOLUTION: Always ask about regulatory and audit requirements

❌ PITFALL 5: Accepting vague answers
   ✓ SOLUTION: Get specific numbers (latency, throughput, users)

❌ PITFALL 6: Not documenting assumptions
   ✓ SOLUTION: Explicitly call out assumptions and confirm

❌ PITFALL 7: Missing data flow details
   ✓ SOLUTION: Draw diagrams and confirm data movement

❌ PITFALL 8: Underestimating integration complexity
   ✓ SOLUTION: Deep-dive on all integration points
```

---

## Related Topics

- **Main Page:** [Pre-Sales & Solution Design](./presales-solution-design.md)
- **Solution Sizing:** [Solution Sizing & Planning](./solution-sizing.md)
- **Cost Analysis:** [Cost Estimation & TCO](./cost-estimation.md)
- **Proposal Writing:** [Proposal Development](./proposal-development.md)
- **Assessment:** [Pre-Sales & Solution Design Knowledge Check](./presales-knowledge-check.md)

---

_Last Updated: October 21, 2025_
