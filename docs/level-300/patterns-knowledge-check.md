---
layout: default
title: Architecture Patterns - Knowledge Check
parent: Level 300 - Advanced
nav_order: 15
description: "Assessment covering API gateway, event-driven, and data mesh patterns for sovereign clouds"
---

# Architecture Patterns - Knowledge Check

{: .no_toc }

Test your expertise in advanced architecture patterns including API gateways, event-driven architectures, and data mesh implementations for sovereign cloud environments.

---

## Quiz Instructions

**Total Questions:** 15  
**Passing Score:** 12/15 (80%)  
**Time Estimate:** 25-35 minutes  
**Format:** Expert-level scenario-based questions

This assessment covers:

- API gateway patterns and sovereign API management
- Event-driven architectures with data sovereignty
- Data mesh principles and federated governance
- Cross-domain integration patterns

---

### Question 1: API Gateway — Sovereignty Enforcement

An organization wants to enforce data residency at the API layer. Which API gateway pattern is MOST effective?

A) Centralized global gateway with regional backends  
B) Regional gateway instances with geography-aware routing  
C) Single gateway with encryption for all requests  
D) No gateway — direct service-to-service communication

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Regional gateways ensure requests and data stay within sovereignty boundaries:

**Pattern Architecture:**

| Component | Location | Purpose |
|-----------|----------|---------|
| Regional Gateway | EU, US, APAC | Request routing, policy enforcement |
| Backend Services | Same region as gateway | Data processing |
| Traffic Manager | Global | Geographic routing to nearest gateway |

**Sovereignty Enforcement:**

- Gateway applies regional policies
- Data never crosses regional boundaries
- Audit logs remain local
- Compliance policies enforced at ingress

**Why Not Others:**

- **A:** Centralized gateway creates single point of cross-border data flow
- **C:** Encryption doesn't address data residency
- **D:** No gateway means no centralized policy enforcement

**Reference:** [API Gateway Patterns](api-gateway-patterns.md)
</details>

---

### Question 2: Event-Driven — Message Ordering

A financial services application requires strict message ordering for transaction events. Which pattern ensures correct ordering?

A) Partitioned topics with partition key = account ID  
B) Multiple parallel consumers for throughput  
C) Random distribution across partitions  
D) Batching all messages into single partition

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: A**

**Explanation:**
Partitioning by key ensures ordering within each partition:

**Ordering Guarantee:**

| Pattern | Ordering | Throughput |
|---------|----------|------------|
| **Partition by account** | Per-account ordering | High (parallel partitions) |
| Single partition | Global ordering | Low (single consumer) |
| Random | No ordering | Highest |

**Implementation:**

```text
Account 123 events → Partition 5 → Consumer 5 (in order)
Account 456 events → Partition 2 → Consumer 2 (in order)
```

**Financial Use Case:**

- All transactions for one account processed in order
- Different accounts processed in parallel
- Balance always consistent per account

**Reference:** [Event-Driven Architecture](event-driven-architecture.md)
</details>

---

### Question 3: Data Mesh — Domain Ownership

In a data mesh architecture, who is responsible for data quality?

A) Central data team  
B) Domain team that produces the data  
C) Consumers of the data  
D) External auditors

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Data mesh principle: "Domain-oriented decentralized data ownership":

**Data Mesh Ownership Model:**

| Role | Responsibility |
|------|----------------|
| **Domain Team (Producer)** | Data quality, SLAs, schema, documentation |
| Central Platform | Infrastructure, standards, governance framework |
| Consumers | Responsible use, feedback on quality issues |

**Quality at Source:**

- Domain experts understand data semantics
- Quality checks embedded in data pipelines
- SLAs defined and monitored by domain
- Consumers trust published data products

**Why Not Others:**

- **A:** Central team doesn't scale, doesn't understand domain context
- **C:** Consumers can report issues but shouldn't fix source
- **D:** Auditors verify but don't own quality

**Reference:** [Data Mesh Sovereignty](data-mesh-sovereignty.md)
</details>

---

### Question 4: API Gateway — Rate Limiting Strategy

A government API must protect against DoS while providing fair access to all agencies. Which rate limiting approach is BEST?

A) Global rate limit (1000 requests/minute total)  
B) Per-IP rate limiting  
C) Per-API-key rate limiting with agency quotas  
D) No rate limiting — trust all government users

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: C**

**Explanation:**
Per-API-key limiting with quotas provides fair allocation:

**Rate Limiting Hierarchy:**

| Level | Purpose | Example |
|-------|---------|---------|
| **Per API Key** | Agency-specific quotas | Agency A: 10,000/hr |
| Per endpoint | Protect expensive operations | /reports: 100/hr |
| Global | DDoS protection | 1M total requests/hr |

**Benefits:**

- Each agency gets guaranteed capacity
- No agency can monopolize API
- Quota management enables chargeback
- Audit trail per agency

**Why Not Others:**

- **A:** Global limit lets one agency consume all capacity
- **B:** IP limiting breaks for agencies behind NAT
- **D:** No limiting enables accidental or intentional DoS

**Reference:** [API Gateway Patterns](api-gateway-patterns.md)
</details>

---

### Question 5: Event-Driven — Saga Pattern

A cross-domain transaction must update Inventory, Payments, and Shipping services. If Payments fails, what should happen?

A) Retry Payments indefinitely  
B) Compensating transactions to rollback Inventory  
C) Ignore the failure and continue  
D) Manual intervention required

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Saga pattern uses compensating transactions for rollback:

**Saga Flow:**

```text
1. Reserve Inventory ✓
2. Process Payment ✗ (fails)
3. Compensate: Release Inventory ✓
4. Saga complete (rolled back)
```

**Saga Types:**

| Type | Coordination | Use Case |
|------|--------------|----------|
| Choreography | Event-based | Simple sagas, loose coupling |
| Orchestration | Central coordinator | Complex flows, visibility |

**Why Compensating Transactions:**

- Distributed systems can't use traditional ACID transactions
- Each service manages its own data
- Compensating actions reverse previous steps
- Eventually consistent, not immediately consistent

**Reference:** [Event-Driven Architecture](event-driven-architecture.md)
</details>

---

### Question 6: Data Mesh — Cross-Domain Sovereignty

A multinational organization has EU and US data domains. How should cross-domain data sharing be handled?

A) Central data lake replicates all data globally  
B) Data contracts with sovereignty metadata, federated access  
C) No cross-domain sharing allowed  
D) Only aggregated data can cross domains

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Data contracts enable controlled cross-domain sharing:

**Data Contract Components:**

| Element | Purpose |
|---------|---------|
| **Sovereignty metadata** | Data residency requirements, transfer restrictions |
| Schema | Structure and data types |
| SLA | Quality, freshness, availability |
| Access policy | Who can access, from where |
| Lineage | Origin and transformation history |

**Cross-Border Handling:**

- EU domain publishes data product with "EU only" sovereignty tag
- US consumers see data product in catalog but cannot access
- Cross-border versions created with appropriate SCCs/BCRs
- Audit trail for all access attempts

**Why Not Others:**

- **A:** Global replication violates data residency
- **C:** Too restrictive for business needs
- **D:** Aggregation alone doesn't guarantee compliance

**Reference:** [Data Mesh Sovereignty](data-mesh-sovereignty.md)
</details>

---

### Question 7: API Gateway — mTLS Implementation

For sovereign API authentication, when should mutual TLS (mTLS) be used?

A) Only for external public APIs  
B) For all service-to-service communication within sovereign boundary  
C) Only when username/password is not available  
D) mTLS is deprecated and should not be used

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
mTLS provides cryptographic identity for both client and server:

**mTLS Benefits:**

| Benefit | Description |
|---------|-------------|
| Mutual authentication | Both parties prove identity |
| Encryption in transit | TLS channel encryption |
| Certificate-based | No passwords to manage |
| Non-repudiation | Cryptographic proof of communication |

**Sovereign Use Cases:**

- API-to-API calls within secure zone
- Zero Trust service mesh
- Cross-domain API federation
- Partner API integration

**Implementation:**

- Certificate authority per domain
- Short-lived certificates (auto-rotation)
- Certificate revocation for compromised identities

**Reference:** [API Gateway Patterns](api-gateway-patterns.md)
</details>

---

### Question 8: Event-Driven — Dead Letter Handling

Messages that fail processing after multiple retries are sent to a dead letter queue. What is the CORRECT handling approach for sovereign environments?

A) Delete dead letters immediately to save storage  
B) Forward dead letters to central global queue for analysis  
C) Keep dead letters in regional queue with alerting and manual review  
D) Automatically retry dead letters indefinitely

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: C**

**Explanation:**
Regional dead letter handling maintains sovereignty:

**Dead Letter Process:**

| Step | Action |
|------|--------|
| 1 | Message fails after N retries |
| 2 | Move to regional dead letter queue |
| 3 | Alert operations team |
| 4 | Manual investigation (may contain sensitive data) |
| 5 | Fix and reprocess or archive |

**Sovereignty Considerations:**

- Dead letters may contain PII/regulated data
- Cannot forward to global queue without sovereignty review
- Retention policies must comply with regulations
- Access to dead letters requires appropriate authorization

**Why Not Others:**

- **A:** Deletes evidence, loses data
- **B:** Cross-border transfer may violate residency
- **D:** Infinite retry wastes resources, doesn't fix root cause

**Reference:** [Event-Driven Architecture](event-driven-architecture.md)
</details>

---

### Question 9: Data Mesh — Self-Service Infrastructure

What is the role of the "self-service data platform" in data mesh?

A) Replace domain teams with automation  
B) Provide common infrastructure for domains to build data products  
C) Centralize all data processing  
D) Eliminate the need for data governance

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Self-service platform enables domains without central bottleneck:

**Platform Capabilities:**

| Capability | Description |
|------------|-------------|
| Data storage | Object storage, data lake, databases |
| Compute | Processing engines, orchestration |
| Catalog | Data product discovery |
| Governance | Automated policy enforcement |
| Observability | Monitoring, alerting, lineage |

**Domain Autonomy:**

- Domains use platform capabilities
- Domains own their data products
- Platform team provides, doesn't operate domain products
- Reduces time-to-market for new data products

**Why Not Others:**

- **A:** Domains still own and operate their products
- **C:** Decentralization is core data mesh principle
- **D:** Federated governance is essential

**Reference:** [Data Mesh Sovereignty](data-mesh-sovereignty.md)
</details>

---

### Question 10: API Gateway — OAuth2 Scope Enforcement

An API gateway must enforce fine-grained permissions. Which OAuth2 mechanism is MOST appropriate?

A) Client credentials only  
B) Authorization code flow with scopes  
C) Implicit flow  
D) API keys without OAuth

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Scopes enable granular permission control:

**OAuth2 Scopes:**

| Scope | Permission |
|-------|------------|
| `read:customers` | View customer data |
| `write:customers` | Modify customer data |
| `admin:customers` | Delete, manage customers |
| `gdpr:export` | Export personal data |

**Authorization Flow:**

1. User authenticates
2. Consent screen shows requested scopes
3. Token issued with approved scopes
4. API gateway validates token scopes against endpoint requirements
5. Access granted or denied per scope

**Why Not Others:**

- **A:** Client credentials = service identity, no user context
- **C:** Implicit flow is deprecated (security concerns)
- **D:** API keys don't support granular permissions

**Reference:** [API Gateway Patterns](api-gateway-patterns.md)
</details>

---

### Question 11: Event-Driven — Event Sourcing Compliance

Event sourcing stores all state changes as immutable events. How does this impact GDPR right-to-erasure requests?

A) Event sourcing is incompatible with GDPR  
B) Use crypto-shredding: encrypt PII with per-user keys, delete key on erasure  
C) Delete all events containing user data  
D) GDPR doesn't apply to event logs

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Crypto-shredding provides GDPR-compliant erasure for immutable stores:

**Crypto-Shredding Process:**

| Step | Action |
|------|--------|
| 1 | Encrypt PII in events with per-user key |
| 2 | Store encryption key in secure key vault |
| 3 | On erasure request, delete user's key |
| 4 | Encrypted data becomes unreadable |

**Benefits:**

- Event log remains intact (audit trail preserved)
- PII is cryptographically erased
- No need to modify immutable events
- Complies with right-to-erasure

**Why Not Others:**

- **A:** Crypto-shredding makes it compatible
- **C:** Deleting events breaks event sourcing integrity
- **D:** GDPR applies to all personal data processing

**Reference:** [Event-Driven Architecture](event-driven-architecture.md)
</details>

---

### Question 12: Data Mesh — Federated Governance

How should data classification policies be enforced in a federated data mesh?

A) Each domain defines its own classification scheme  
B) Central team manually reviews all data products  
C) Federated governance: central standards, automated enforcement, domain implementation  
D) No classification needed in data mesh

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: C**

**Explanation:**
Federated governance balances autonomy with standards:

**Governance Model:**

| Layer | Responsibility |
|-------|----------------|
| **Global** | Classification scheme, compliance requirements |
| **Platform** | Automated policy enforcement, tooling |
| **Domain** | Apply classifications, implement controls |

**Classification Enforcement:**

- Central team defines: Public, Internal, Confidential, Restricted
- Platform provides classification tools and validation
- Domains apply appropriate labels to their data products
- Automated checks prevent non-compliant publishing

**Why Not Others:**

- **A:** Inconsistent classification breaks cross-domain sharing
- **B:** Central bottleneck doesn't scale
- **D:** Classification essential for sovereignty

**Reference:** [Data Mesh Sovereignty](data-mesh-sovereignty.md)
</details>

---

### Question 13: API Gateway — API Versioning

A sovereign API needs to maintain backward compatibility while evolving. What is the RECOMMENDED versioning strategy?

A) No versioning — clients must always use latest  
B) URI versioning (/v1/, /v2/) with sunset policies  
C) Header versioning only  
D) Query parameter versioning (?version=1)

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
URI versioning with sunset policies provides clarity and governance:

**Versioning Strategy:**

| Aspect | Approach |
|--------|----------|
| Location | URI path (`/api/v1/customers`) |
| Discovery | Versions visible in documentation |
| Sunset | Published deprecation timeline |
| Support | N-1 version supported |

**Sunset Policy:**

1. Announce new version with migration guide
2. N-1 version enters maintenance mode
3. 6-12 month deprecation window
4. N-1 version sunset, clients must migrate

**Why URI Versioning:**

- Easy to understand and implement
- Clear in logs and monitoring
- Cacheable per version
- Supported by all HTTP clients

**Reference:** [API Gateway Patterns](api-gateway-patterns.md)
</details>

---

### Question 14: Event-Driven — Event Schema Evolution

A domain needs to add a new required field to their event schema. What is the SAFEST approach?

A) Add required field immediately, update all consumers  
B) Add as optional field first, make required after all consumers updated  
C) Create entirely new event type  
D) Send both old and new event formats simultaneously

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Backward-compatible evolution protects consumers:

**Schema Evolution Pattern:**

| Phase | Action |
|-------|--------|
| 1 | Add new field as optional (with default value) |
| 2 | Update producers to populate new field |
| 3 | Update consumers to use new field |
| 4 | Make field required in schema validation |

**Compatibility Rules:**

- Adding optional fields is backward compatible
- Removing fields breaks consumers
- Changing field types breaks compatibility
- Required → optional is safe; optional → required is not

**Schema Registry:**

Use schema registry to track versions and enforce compatibility.

**Reference:** [Event-Driven Architecture](event-driven-architecture.md)
</details>

---

### Question 15: Data Mesh — Data Product SLAs

What SLA dimensions should a data product define for sovereignty compliance?

A) Only availability (99.9% uptime)  
B) Availability, freshness, quality, and data residency guarantees  
C) Only data quality metrics  
D) SLAs are not applicable to data products

<details>
<summary>Click to reveal answer</summary>

**Correct Answer: B**

**Explanation:**
Comprehensive SLAs enable trust and compliance:

**Data Product SLA Dimensions:**

| Dimension | Example | Sovereignty Relevance |
|-----------|---------|----------------------|
| **Availability** | 99.9% uptime | Business continuity |
| **Freshness** | Data < 1 hour old | Real-time compliance reporting |
| **Quality** | < 0.1% error rate | Regulatory accuracy requirements |
| **Residency** | EU-only storage | GDPR, data sovereignty |
| **Lineage** | Full transformation history | Audit trail |

**Contract Example:**

```yaml
sla:
  availability: 99.9%
  freshness: PT1H  # 1 hour
  quality:
    completeness: 99.5%
    accuracy: 99.9%
  residency: EU
  retention: 7 years
```

**Why Comprehensive SLAs:**

- Consumers need predictability
- Regulators require specific guarantees
- Enables data product marketplace

**Reference:** [Data Mesh Sovereignty](data-mesh-sovereignty.md)
</details>

---

## Assessment Complete

**Scoring Guide:**

| Score | Result |
|-------|--------|
| 15/15 | Expert — Ready for complex pattern implementations |
| 12-14/15 | Proficient — Minor review recommended |
| 9-11/15 | Developing — Review highlighted patterns |
| < 9/15 | Needs Improvement — Complete module review |

---

## Next Steps

- **Review:** [API Gateway Patterns](api-gateway-patterns.md)
- **Review:** [Event-Driven Architecture](event-driven-architecture.md)
- **Review:** [Data Mesh Sovereignty](data-mesh-sovereignty.md)
- **Next Assessment:** [Operations Knowledge Check](operations-knowledge-check.md)
