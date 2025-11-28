---
layout: default
title: Pre-Sales & Solution Design Knowledge Check
parent: Pre-Sales & Solution Design
nav_order: 4.3
---

# Pre-Sales & Solution Design Quiz

{: .no_toc }

Master pre-sales skills for sovereign cloud and edge AI solutions with scenario-based questions covering discovery, sizing, TCO analysis, and proposal development.

---

## Quiz Instructions

- **Total Questions:** 15
- **Passing Score:** 70% (11 of 15 correct)
- **Time Estimate:** 25-35 minutes
- **Format:** Scenario-based multiple choice (A/B/C/D)
- **Note:** Focus on practical pre-sales scenarios and real-world customer engagements.

---

## Questions

### Question 1: Discovering Compliance Requirements

**Scenario:** You're in a discovery meeting with a healthcare organization. The customer mentions they need "data sovereignty" but hasn't elaborated. You have limited time for follow-up questions.

What's the BEST follow-up question to understand their actual requirement?

A) "Do you need HIPAA compliance?"
B) "What specific data residency requirements do you have? And what regulations drive those?"
C) "Is data residency in the US sufficient, or do you need EU or other regions?"
D) "Have you looked at Azure government clouds?"

**Correct Answer:** B

**Explanation:**

- Option A is too narrow (assumes healthcare = HIPAA only; could be GDPR, PCI-DSS, state laws)
- Option B uncovers the root requirement (data residency + regulatory driver)
- Knowing the regulation tells you compliance requirements, certification path, audit frequency
- Option C makes assumptions before understanding the driver
- Option D jumps to solutions before understanding requirements
- Best practice: Ask open-ended question that uncovers root cause and business driver

---

### Question 2: Stakeholder Identification

**Scenario:** You're designing an enterprise solution for a manufacturing company with 5 facilities. The CIO says "The operations team will run this, and IT will support it."

What's the risk in this stakeholder approach?

A) The operations team doesn't need AI
B) You may miss the key decision makers and end up with misaligned solution
C) Operations teams are always unprepared for technology
D) Manufacturing doesn't typically have CISO involvement

**Correct Answer:** B

**Explanation:**

- In most enterprises, operations isn't the primary decision maker for new technology
- Key missing stakeholders likely include:
  - Plant/facility managers (business impact)
  - CISO or security team (compliance and risk)
  - Finance (budget approval)
  - Engineering (technical integration)
- Without discovering full stakeholder map, solution may not address real concerns
- Even if technically excellent, proposal may fail due to misaligned decision criteria

---

### Question 3: Workload Characterization

**Scenario:** Customer says "We want to process data faster." In sizing terms, this is ambiguous. What specific metrics do you need to size properly?

Which is the MOST critical first question?

A) "How many servers do you have today?"
B) "How many queries per second will you run, and what's your latency target?"
C) "What's your budget?"
D) "When do you need this operational?"

**Correct Answer:** B

**Explanation:**

- QPS + latency target directly drive hardware sizing decisions
- A: Server count tells you current scale but not future requirement
- C: Budget constraints matter but aren't the primary sizing driver
- D: Timeline affects project schedule but not technical sizing
- B: QPS determines GPU/CPU needs; latency determines quantization/batching strategy
- Example:
  - 100 QPS @ 500ms latency → 1 GPU sufficient
  - 10,000 QPS @ 100ms latency → 16+ GPUs needed
- This single question drives $50K-500K hardware decision

---

### Question 4: Hardware Sizing for LLM Inference

**Scenario:** Customer needs to run Llama 2 7B model for 500 QPS peak load with <200ms latency requirement. Current hardware available: 8 CPU-only nodes (no GPUs).

What's your sizing recommendation?

A) Use CPU inference with 8 nodes, optimize with quantization
B) Recommend procuring 2x T4 GPUs (16GB VRAM each)
C) Recommend procuring 4x T4 GPUs for adequate headroom and HA
D) Recommend cloud APIs instead since edge isn't viable

**Correct Answer:** C

**Explanation:**

- Llama 2 7B in INT4 quantization: ~2GB VRAM
- 500 QPS with batch size 4 = 125 batches/sec per GPU
- Per GPU throughput: 4,000 QPS capacity (8x headroom)
- With 1 GPU: 2,000 QPS capacity (4x headroom) - borderline
- Option A: CPU inference = 30-50 tokens/sec (vs. 2000/sec GPU) - insufficient
- Option B: 2 GPUs gives 4,000 QPS but zero HA capacity
- Option C: 4 GPUs gives 8,000 QPS + redundancy (if 1 GPU fails, still 6,000 QPS)
- Option D: premature - haven't tried edge solution yet
- Best practice: Size for peak + redundancy (2x minimum)

---

### Question 5: Vector Database Sizing for Multi-Tenant

**Scenario:** Customer has 10 tenants, each requiring 100K vector embeddings, requiring <50ms search latency, and strict data isolation.

What's your database architecture recommendation?

A) Single Weaviate cluster with namespace isolation
B) Single Qdrant with 10 collections (one per tenant)
C) Separate Milvus instance per tenant (containerized on same cluster)
D) 10 separate cloud databases (one per tenant)

**Correct Answer:** C

**Explanation:**

- Option A: Shared cluster has resource contention → exceeds 50ms latency for some tenants
- Option B: Shared collections in single cluster = same contention issue
- Option C: Separate instances per tenant → complete data isolation, predictable latency
  - Containers enable efficient resource packing (10 small instances < 1 large cluster)
  - Kubernetes StatefulSet manages persistence per tenant
  - Meets <50ms latency requirement
- Option D: Cloud databases = sovereignty violation + costs >$50K/year
- Best practice: Containerized isolation when strict SLA + data residency needed

---

### Question 6: Cost Model Comparison

**Scenario:** Customer currently uses cloud APIs at $45K/year for 30M queries. They're considering edge deployment with $365K hardware + $500K annual operating costs.

At what annual query volume does edge become cost-competitive with cloud?

A) 50M queries/year
B) 75M queries/year
C) 100M queries/year
D) 150M queries/year

**Correct Answer:** C

**Explanation:**

- Break-even analysis:
  - Cloud: $45K/year (fixed per query)
  - Edge: $365K capex + $500K opex = $500K Year 1

- For 5-year horizon:
  - Cloud: $225K (5 × $45K)
  - Edge: $2.865M (365K + 5 × $500K)
  - Not equivalent at current volume

- At 100M queries/year:
  - Cloud: $450K/year → $2.25M over 5 years
  - Edge: $2.865M over 5 years
  - Nearly break-even (within 10%)

- At 150M+ queries/year:
  - Cloud: $675K/year → $3.375M over 5 years
  - Edge: $2.865M over 5 years
  - Edge wins (15% cheaper)

---

### Question 7: Phased Deployment for Budget Constraint

**Scenario:** Customer has a $150K Year 1 budget (not $365K) but wants to start edge deployment. What's the best recommendation?

A) Postpone until they have full budget
B) Deploy to cloud temporarily until budget available
C) Deploy 3-node cluster ($100K) in Year 1, add nodes in Year 2
D) Scale down to 2 GPUs only, accept performance compromise

**Correct Answer:** C

**Explanation:**

- Option A: May lose deal, customer might go cloud/competitor
- Option B: Violates sovereignty requirement, wastes $150K on temporary solution
- Option C: 3 nodes supports proof-of-concept workload
  - Validates ROI before full commitment
  - Spreads CAPEX: $100K Y0 + $100K Y1 + $65K Y1 = $265K total (vs. $365K)
  - Lower risk if POC results negative
  - Build confidence for operations team
- Option D: 2 GPUs insufficient for stated requirements (goes back to sizing question)
- Best practice: Phased deployments better for:
  - Budget constraints
  - Risk mitigation
  - Organizational readiness
  - Proof of value

---

### Question 8: TCO Analysis - Intangible Benefits

**Scenario:** Pure financial ROI for edge solution: -47% Year 1 (benefits don't outweigh costs). Customer is still interested.

What strategic value might justify the investment despite negative ROI?

A) Lower hardware cost than competitors
B) Compliance capability enables new business, data sovereignty competitive advantage
C) Faster deployment than cloud
D) Support from Microsoft is better

**Correct Answer:** B

**Explanation:**

- Customer is buying strategic capability, not pure cost savings
- Compliance enablement value:
  - May unlock new market segments (regulated healthcare, financial, government)
  - Potential $500K+ new revenue opportunity
  - Competitive moat (competitors can't serve these customers)
- Data sovereignty:
  - GDPR compliance, EU data residency
  - Customer trust differentiator ("We keep your data safe")
  - May command 10-20% premium in regulated industries
- Option A: Irrelevant to financial case
- Option C: True but not strategically significant for this scenario
- Option D: Support quality exists in cloud too
- Best practice: Quantify intangible benefits (even conservatively) in proposals

---

### Question 9: Proposal Development - Missing Information

**Scenario:** You're preparing a proposal with these estimates:

- Hardware: $250K
- Implementation: $100K
- Year 1 Operations: $500K

Customer asks: "What if implementation goes over, or we need more capacity?"

What's missing from your proposal?

A) Nothing, costs are clearly listed
B) Contingency buffer and phased capacity expansion plan
C) Cloud fallback plan
D) Alternative pricing from competitors

**Correct Answer:** B

**Explanation:**

- Professional proposals include:
  - Contingency: 10-15% of project cost
  - Example: Implementation 10% buffer = $10K contingency
  - Clearly communicated ($100K ± $10K)
- Capacity expansion plan:
  - What triggers additional investment? (e.g., "when QPS reaches 75% of capacity")
  - Cost of phase 2, phase 3 additions
  - Timeline for expansions
- Shows customer you've thought through risks and growth
- Missing these = unprofessional proposal
- Option A: Incomplete risk planning
- Option C: Not relevant if they want sovereign solution
- Option D: Out of scope for Microsoft proposal

---

### Question 10: Objection Handling - Security Concerns

**Scenario:** Security officer says: "We can't trust hardware from external vendors. We need to vet all components and approve supply chain."

What's the BEST response that addresses underlying concern?

A) "Microsoft ensures all hardware partners meet security standards"
B) "We have other customers using this exact hardware with no issues"
C) "I understand your concern. Here's Microsoft's supply chain vetting process, partner security certifications, and hardware component transparency. We can add supply chain audit as a gate before deployment. What specific concerns do you want to validate?"
D) "Hardware security is already built-in, no need for additional vetting"

**Correct Answer:** C

**Explanation:**

- Security officer's underlying concern: Control and visibility of supply chain
- Response A: Dismisses their concern ("trust Microsoft")
- Response B: Appeals to authority but not to their concern
- Response C: Acknowledges concern + provides transparency + offers collaborative solution
  - Shows Microsoft partnerships are vetted
  - Offers audit step for their validation
  - Invites their input on specific concerns
  - Moves from objection to collaborative problem-solving
- Response D: Minimizes their legitimate concern
- Best practice: Objection = opportunity to strengthen relationship, not to overcome

---

### Question 11: Discovery Depth - When to Stop Questioning

**Scenario:** You're 90 minutes into a discovery meeting. You've covered business drivers, compliance needs, infrastructure, and current challenges. The business owner seems ready to move forward. You notice you haven't discussed disaster recovery requirements yet.

What's the best decision?

A) Push through and ask DR questions (complete the template)
B) Wrap up the meeting, send summary, schedule follow-up for technical deep-dive
C) Ask quick one-liner about DR, then close
D) Skip DR (assume standard HA is sufficient)

**Correct Answer:** B

**Explanation:**

- Discovery meeting is getting long (stakeholder attention waning)
- 90 minutes is typical limit for executive engagement
- You've captured main requirements (excellent discovery)
- DR is important but technical detail (not executive-level decision)
- Best practice:
  - Close while momentum is positive
  - Schedule follow-up with technical team for depth
  - Send detailed summary showing you listened
  - Technical team deepdives on remaining questions (DR, network, integration)
- Option A: Risks boring decision makers, may lose deal momentum
- Option C: Quick question incomplete (deserves proper discussion)
- Option D: Risk missing critical requirement

---

### Question 12: Sizing Validation - Red Flag

**Scenario:** During sizing review, you calculate:

- Required QPS: 500
- GPU capacity per T4: 2,000 QPS
- Hardware recommendation: 1 GPU sufficient

Customer's IT manager immediately says: "You must be wrong. That seems way too small. We need at least 4 GPUs."

What should you do?

A) Agree with them (customer knows their environment better)
B) Defend your sizing calculation
C) Acknowledge their concern and explore the gap
D) Compromise: recommend 2 GPUs as middle ground

**Correct Answer:** C

**Explanation:**

- Customer concern = flag that sizing assumptions may be wrong
- Possible explanations:
  - QPS estimate was too conservative (actual will be higher)
  - Burstiness/spiky traffic not accounted for (need HA replicas)
  - Multiple workloads on same cluster (shared resources)
  - They want 50% reserve capacity (not just meet requirements)
  - They tested similar workload and need more than calculated
- Best approach: "Let me validate my assumptions. Tell me more about why you think 4 GPUs is appropriate."
- Option A: Abdicates responsibility (your job is to size correctly)
- Option B: Defensive (misses opportunity to learn)
- Option C: Collaborative (finds real requirement)
- Option D: Compromise without understanding = waste of $50K hardware

---

### Question 13: Proposal Win Strategy - What's Missing?

**Scenario:** You've prepared excellent proposal with:

- Clear cost breakdown
- ROI analysis
- Technical architecture
- Implementation timeline

It's been 2 weeks since submission. Customer hasn't responded. What's most likely missing?

A) The cost is too high
B) You didn't align the solution to their strategic priorities
C) They need more technical details
D) The timeline is too aggressive

**Correct Answer:** B

**Explanation:**

- Silence after proposal = typically not about technical or timeline issues
- Most common silence reason: proposal doesn't connect to THEIR success metrics
- What's likely missing:
  - Executive summary that speaks to business value
  - Explicit ROI vs. THEIR strategic priorities
  - Testimonial or case study from similar company
  - Clear statement of how this solves THEIR stated business problem
- Option A: If cost were problem, they'd have said so
- Option C: Technical details present, wouldn't cause 2-week silence
- Option D: If timeline issue, they'd request different timeline
- Best practice:
  - Add executive summary that explicitly ties to their business drivers
  - One-page ROI summary (ROI speaks universally)
  - Reach out: "Checking in, any questions I can clarify?"

---

### Question 14: Competitive Positioning

**Scenario:** Customer asks: "Why should we go with Azure edge instead of [Competitor's] solution?"

Which response is MOST effective?

A) "Azure is better supported and has more features"
B) "Microsoft Sovereign Cloud integrates with your existing Azure investments, providing consistent governance and easier operations"
C) "Azure is cheaper"
D) "The competitors' solution doesn't support your compliance requirements"

**Correct Answer:** B

**Explanation:**

- Option A: Vague, unsubstantiated, doesn't resonate
- Option B: Speaks to customer value (existing Azure investment, operational simplicity, governance consistency)
  - Leverages stickiness (if they use Azure already)
  - Reduces complexity vs. multi-vendor solution
  - Ownership benefits (Microsoft support for entire stack)
- Option C: Rarely true for edge solutions; price wars are losable
- Option D: May be factual but defensive positioning
  - Better: "Azure is the only platform that meets your compliance AND sovereignty requirements"
- Best practice: Position on VALUE (integrated, simpler, better operations) not on feature parity

---

### Question 15: Post-Sale Value Delivery

**Scenario:** You've won the deal. Implementation begins in 2 months. What's your best strategy for ensuring high customer success and reference-ability?

A) Let the implementation team handle everything until go-live
B) Stay engaged: establish success metrics, weekly check-ins, early adoption incentives
C) Focus on managing costs during implementation to keep customer happy
D) Plan the reference call for 6 months post-go-live

**Correct Answer:** B

**Explanation:**

- Post-sale engagement directly impacts:
  - Actual vs. expected outcome (risk of disappointment)
  - Customer satisfaction and willingness to be reference
  - Adoption and time-to-value realization
- Best practice during implementation:
  - Define success metrics early (latency, availability, cost per query)
  - Weekly check-ins with customer to catch issues early
  - Celebrate milestones (hardware delivery, first cluster node up, etc.)
  - Support early adoption (proof of value before full go-live)
  - Identify reference opportunities early
- Option A: Hands-off = risk of misalignment surfacing too late
- Option C: Cost management important but not primary success driver
- Option D: Too late to course-correct (reference call should be 3 months post-go-live)
- Result: Engaged post-sale = 80%+ customer satisfaction vs. 40% hands-off approach

---

## Answer Key

| Q | Answer | Topic |
|----|--------|-------|
| 1 | B | Discovery Questioning |
| 2 | B | Stakeholder Mapping |
| 3 | B | Workload Characterization |
| 4 | C | Hardware Sizing |
| 5 | C | Database Sizing |
| 6 | C | TCO Break-Even |
| 7 | C | Phased Deployment |
| 8 | B | Strategic Value |
| 9 | B | Proposal Completeness |
| 10 | C | Objection Handling |
| 11 | B | Discovery Depth |
| 12 | C | Sizing Validation |
| 13 | B | Proposal Win Strategy |
| 14 | B | Competitive Positioning |
| 15 | B | Post-Sale Success |

---

## Scoring Guide

**Calculate your score:**

- Count the number of correct answers
- Divide by 15 and multiply by 100 for percentage

**Score Interpretation:**

**15 correct (100%):** 🏆 **Master Pre-Sales Architect**

- Perfect score! You have mastery-level pre-sales expertise
- Ready to lead complex sovereign cloud engagements
- Qualified for senior pre-sales architect or principal consultant roles
- Consider mentoring other pre-sales professionals

**13-14 correct (87-93%):** ⭐ **Senior Pre-Sales Expert**

- Excellent pre-sales skills and judgment
- Ready for complex customer engagements
- Minor review recommended on missed topics
- Consider pursuing advanced sales certifications

**11-12 correct (73-80%):** ✅ **Experienced Professional - Ready**

- **PASSING** - Ready for customer engagements
- Solid understanding of pre-sales process
- Review areas where you missed questions
- Focus on discovery techniques and sizing validation

**9-10 correct (60-67%):** ⚠️ **Review Recommended**

- Foundational understanding but gaps exist
- Review recommended before customer presentations
- Focus on discovery questioning and TCO analysis
- Practice with scenario-based exercises
- Retake quiz after review

**Below 9 correct (<60%):** ❌ **Strong Review Needed**

- Significant gaps in pre-sales knowledge
- Strong review needed before customer-facing work
- Study all module content thoroughly
- Focus on fundamentals: discovery, sizing, TCO, proposals
- Consider shadowing experienced pre-sales professionals
- Retake quiz only after comprehensive study

---

## Study Recommendations by Topic

**If you missed questions on Discovery (Q1, Q2, Q11):**

- Review [Customer Discovery](customer-discovery)
- Study effective discovery questioning techniques
- Focus on stakeholder mapping and identification
- Practice uncovering root requirements vs stated needs

**If you missed questions on Sizing (Q3, Q4, Q5, Q12):**

- Review [Pre-Sales & Solution Design](presales-solution-design)
- Study workload characterization methods
- Focus on hardware and database sizing calculations
- Review sizing validation techniques

**If you missed questions on TCO/Financial (Q6, Q8):**

- Review [Cost Estimation](cost-estimation)
- Study TCO break-even analysis
- Focus on strategic value articulation
- Review ROI calculation methods

**If you missed questions on Proposals (Q7, Q9, Q13):**

- Review proposal development best practices
- Study phased deployment strategies
- Focus on proposal completeness and win strategies
- Review competitive differentiation

**If you missed questions on Sales Strategy (Q10, Q14, Q15):**

- Review objection handling techniques
- Study competitive positioning strategies
- Focus on post-sale success planning
- Review customer engagement best practices

---

## Next Steps

**After completing this assessment:**

1. **✅ Congratulations!** You're ready for customer-facing pre-sales engagements.

2. **📚 Apply your knowledge:**
   - Practice discovery calls with colleagues
   - Create sample proposals
   - Develop sizing calculators
   - Build TCO models

3. **🔗 Review related content:**
   - [Pre-Sales & Solution Design](presales-solution-design)
   - [Customer Discovery](customer-discovery)
   - [Cost Estimation](cost-estimation)

4. **🌐 Explore external resources:**
   - [Azure Pricing Calculator](https://azure.microsoft.com/pricing/calculator/)
   - [Azure TCO Calculator](https://azure.microsoft.com/pricing/tco/)
   - [Microsoft Sales Resources](https://partner.microsoft.com/en-us/training/)

5. **💡 Consider hands-on practice:**
   - Shadow experienced pre-sales calls
   - Create customer discovery templates
   - Build sizing and TCO calculators
   - Develop proposal frameworks
   - Practice objection handling

---

## Key Pre-Sales Skills Summary

**Discovery Excellence:**

- Ask open-ended questions to uncover root requirements
- Map all stakeholders (technical, business, executive)
- Understand regulatory drivers and compliance needs
- Validate stated requirements with deeper questioning

**Sizing Precision:**

- Characterize workloads with specific metrics (QPS, latency)
- Size hardware based on peak load + growth
- Validate sizing with benchmarks and references
- Build in capacity for redundancy and growth

**Financial Acumen:**

- Calculate accurate TCO (hardware, software, operations)
- Identify break-even points and ROI timelines
- Articulate strategic value beyond cost savings
- Present clear financial justification

**Proposal Mastery:**

- Include all required sections (technical, financial, timeline)
- Propose phased deployments to reduce risk
- Differentiate from competitors with unique value
- Set clear success metrics and milestones

---

**Quiz Version:** 1.0  
**Last Updated:** October 2025  
**Questions:** 15  
**Passing Score:** 70% (11 of 15 correct)

---

**[← Back to Pre-Sales & Solution Design](presales-solution-design)**
