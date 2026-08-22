<div align="center">

# VESSEL OWNERSHIP INTELLIGENCE

### Trace · Resolve · Correlate · Validate · Assess

**Transforming fragmented maritime ownership records into structured vessel intelligence through entity resolution, relationship mapping, temporal analysis and independent source validation.**

</div>

---

## Intelligence Question

> **Who owns, controls, manages and operates a vessel — and what evidence supports that assessment?**

A vessel's identity extends beyond its IMO number, name, flag or registered owner.

Maritime ownership structures can involve multiple entities performing different legal, corporate, management and operational functions across the vessel's lifecycle.

The objective of this case study is to reconstruct those relationships from fragmented maritime records, distinguish between ownership and operational roles, identify changes over time, resolve conflicting records and assess the reliability of the resulting ownership picture.

> **The objective is not simply to find an owner.  
> The objective is to understand the ownership and control structure surrounding the vessel.**

---

# 01 — OWNERSHIP INTELLIGENCE MODEL

Vessel ownership intelligence is treated as a **relationship-analysis problem** rather than a single database lookup.

A vessel may be associated with multiple entities, each performing a different function.

```text
                              VESSEL
                                │
                ┌───────────────┼────────────────┐
                │               │                │
                ▼               ▼                ▼
         LEGAL OWNERSHIP   MANAGEMENT       OPERATIONS
                │               │                │
                ▼               ▼                ▼
       Registered Owner   Technical Manager   Operator
                │               │                │
                ▼               ▼                ▼
       Beneficial Owner  Commercial Manager  Vessel Activity
                │
                ▼
        Parent / Group
                │
                ▼
      Corporate Control
```

The analytical task is to determine:

```text
WHO
 ↓
WHAT ROLE
 ↓
FROM WHEN
 ↓
BASED ON WHICH SOURCE
 ↓
WITH WHAT CONFIDENCE
```

### Core analytical dimensions

| Dimension | Intelligence Question |
|---|---|
| **Identity** | Which vessel are we assessing? |
| **Entity** | Which company or organization is associated with it? |
| **Role** | What function does that entity perform? |
| **Relationship** | How is the entity connected to the vessel? |
| **Time** | During what period did the relationship apply? |
| **Evidence** | Which source supports the relationship? |
| **Confidence** | How reliable is the assessment? |

---

# 02 — OWNERSHIP / CONTROL / MANAGEMENT ROLES

A critical part of vessel ownership intelligence is separating entities by function.

| Role | Intelligence Meaning |
|---|---|
| **Registered Owner** | Legal entity recorded as owning the vessel |
| **Beneficial Owner** | Entity or person ultimately benefiting from or controlling the ownership interest, where established |
| **Parent / Corporate Group** | Higher-level corporate entity associated with or controlling the relevant company |
| **Technical Manager** | Entity responsible for technical management, maintenance and related vessel management functions |
| **Commercial Manager** | Entity responsible for commercial employment, chartering or related commercial functions where applicable |
| **Operator** | Entity responsible for the vessel's operational deployment |
| **Flag / Registry** | Jurisdiction under which the vessel is registered |

> **Ownership is not synonymous with management or operation.**

A company appearing in a vessel record should not automatically be interpreted as the legal owner, beneficial owner or controlling entity.

The role attached to each entity must be established independently.

---

# 03 — ANALYTICAL WORKFLOW

```mermaid
flowchart LR
A[Target Vessel] --> B[Identity Resolution]
B --> C[Collect Ownership Records]
C --> D[Entity Resolution]
D --> E[Map Ownership & Management Roles]
E --> F[Cross-Source Validation]
F --> G[Temporal Reconstruction]
G --> H[Conflict Resolution]
H --> I[Ownership Assessment]
I --> J[Confidence Assessment]
J --> K[Structured Intelligence Output]
```

### 01 — IDENTIFY

Establish the vessel's identity using stable identifiers such as:

- IMO number
- MMSI
- Vessel name
- Call sign
- Flag
- Vessel type

### 02 — COLLECT

Gather ownership, management and corporate records from relevant maritime and open-source sources.

### 03 — RESOLVE

Determine whether apparently different company records refer to the same underlying entity.

### 04 — MAP

Separate legal ownership, beneficial ownership, management and operational relationships.

### 05 — CORRELATE

Compare information across independent sources to identify consistency, discrepancies and missing relationships.

### 06 — RECONSTRUCT

Establish how ownership and management relationships changed over time.

### 07 — RESOLVE CONFLICTS

Investigate contradictory records rather than automatically selecting one record.

### 08 — ASSESS

Produce a structured ownership assessment supported by evidence provenance and confidence.

---

# 04 — SOURCE INTELLIGENCE

Ownership intelligence is dependent on the quality, relevance and temporal context of the underlying sources.

The objective is not to collect the largest number of sources.

The objective is to determine:

> **Which source supports which relationship, for which period, and with what evidentiary strength?**

| Source Category | Primary Intelligence Value |
|---|---|
| **Ship Registries** | Registered ownership and flag information |
| **IMO / Maritime Records** | Vessel identity and particulars |
| **GISIS** | IMO-related vessel and company information |
| **Equasis** | Vessel, ownership and management records |
| **Corporate Registries** | Legal entity information and corporate relationships |
| **Company Filings** | Corporate ownership and structural information |
| **LexisNexis** | Corporate and entity research |
| **Commercial Vessel Databases** | Vessel ownership and management records |
| **Maritime Intelligence Platforms** | Cross-source vessel intelligence |
| **Historical Records** | Ownership and management changes |
| **Company Websites / Reports** | Supporting corporate evidence |
| **Open-Source Reporting** | Contextual and event-based validation |

### Source assessment

Each source should be evaluated according to:

**Authority · Recency · Specificity · Independence · Consistency · Temporal relevance**

A source is not automatically authoritative simply because it contains an ownership field.

---

# 05 — ENTITY RESOLUTION

One of the central challenges in ownership intelligence is determining whether apparently different company records refer to the same underlying entity.

For example:

```text
ABC SHIPPING LTD
        │
        ├── ABC Shipping Limited
        │
        ├── ABC Shipping Ltd.
        │
        └── ABC Shipping (Cyprus) Ltd
```

Similar names do not automatically establish corporate identity.

Entity resolution may require comparison of:

- Legal name
- Company number
- Jurisdiction
- Registered address
- Directors
- Parent company
- Corporate group
- Historical company names
- Vessel associations
- Registration dates
- Corporate filings

### Entity Resolution Principle

> **Name similarity is an indicator — not proof of entity identity.**

The assessment should distinguish between:

**Same name**

and

**Same legal / corporate entity**

where evidence permits.

---

# 06 — OWNERSHIP STRUCTURE

The ownership assessment separates four analytical layers.

### LEGAL OWNERSHIP

**Who is recorded as legally owning the vessel?**

### BENEFICIAL OWNERSHIP

**Who ultimately benefits from or controls the ownership interest, where this can be established?**

### MANAGEMENT

**Who is responsible for technical or commercial management?**

### OPERATION

**Who operates or commercially deploys the vessel?**

These relationships may converge on one entity or involve several independent entities.

```text
LEGAL OWNERSHIP
       │
       ▼
REGISTERED OWNER
       │
       ▼
BENEFICIAL INTEREST
       │
       ▼
CORPORATE CONTROL
       │
       ├───────────────┐
       ▼               ▼
TECHNICAL          COMMERCIAL
MANAGEMENT         MANAGEMENT
       │               │
       └───────┬───────┘
               ▼
            OPERATOR
               │
               ▼
        VESSEL ACTIVITY
```

> **The entity operating a vessel is not necessarily the entity legally owning it, and the registered owner is not necessarily the ultimate beneficial controller.**

---

# 07 — OWNERSHIP INTELLIGENCE SIDEBAR

The ownership assessment can be represented as a structured intelligence panel.

<table>
<tr>
<td width="50%">

<img src="assets/ownership-sidebar.svg" width="100%"/>

</td>

<td width="50%" valign="top">

| Field | What it captures | Example |
|---|---|---|
| **Vessel** | Target maritime asset | `MV Example` |
| **IMO** | Stable vessel identifier | `IMO XXXXXXX` |
| **Registered Owner** | Legally recorded owner | `Example Shipping Ltd` |
| **Beneficial Owner** | Ultimate ownership / control where established | `Example Group` |
| **Technical Manager** | Technical management entity | `Example Management Ltd` |
| **Commercial Manager** | Commercial management entity | `Example Maritime Ltd` |
| **Operator** | Operational entity | `Example Shipping` |
| **Flag** | Registration jurisdiction | `Liberia` |
| **Effective Date** | Date relationship became applicable | `YYYY-MM-DD` |
| **Confidence** | Strength of ownership assessment | `HIGH` |

</td>
</tr>
</table>

The sidebar represents the **assessed ownership picture for a defined point in time**.

It should not imply that every entity associated with the vessel performs an ownership function.

---

# 08 — CASE STUDY 01 — OWNERSHIP STRUCTURE RECONSTRUCTION

## Intelligence Objective

Determine the ownership, management and operational structure associated with a target vessel.

### Analytical Path

```text
VESSEL IDENTIFICATION
        ↓
IMO / NAME / MMSI
        ↓
REGISTERED OWNER
        ↓
MANAGEMENT ENTITIES
        ↓
CORPORATE RELATIONSHIPS
        ↓
BENEFICIAL OWNERSHIP
        ↓
OPERATOR
        ↓
CROSS-SOURCE VALIDATION
        ↓
FINAL ASSESSMENT
```

### Ownership Assessment

| Role | Entity | Evidence | Confidence |
|---|---|---|---|
| Registered Owner | `[Entity]` | `[Source]` | `HIGH` |
| Beneficial Owner | `[Entity / Unknown]` | `[Source]` | `MEDIUM` |
| Technical Manager | `[Entity]` | `[Source]` | `HIGH` |
| Commercial Manager | `[Entity / N/A]` | `[Source]` | `MEDIUM` |
| Operator | `[Entity]` | `[Source]` | `HIGH` |
| Flag | `[Flag]` | `[Source]` | `HIGH` |

### Intelligence Assessment

> The available records indicate that **[Entity]** is the registered owner of the vessel, while management and operational responsibilities are associated with **[Entity / Entities]**.
>
> The ownership structure is assessed with **[HIGH / MEDIUM / LOW] confidence**, based on source consistency, record recency and independent corroboration.

---

# 09 — OWNERSHIP CHANGE DETECTION

Ownership intelligence is inherently temporal.

A vessel's ownership record at one point in time may not represent its current or historical ownership structure.

Ownership relationships should therefore be treated as **time-bound events**.

```text
2021
│
├── Registered Owner A
│
2022
│
├── Registered Owner B
│
2023
│
├── Registered Owner B
├── Technical Manager C
│
2024
│
├── Registered Owner D
├── Operator E
│
2025
│
└── Current Assessed Structure
```

### Change Detection Questions

- When did the ownership change?
- Which entity replaced the previous owner?
- Was the vessel renamed?
- Did the flag change?
- Did management change simultaneously?
- Did the operator change?
- Did the corporate group change?
- Which source first recorded the change?
- Is the change independently corroborated?
- Is there a gap between the reported transaction and its appearance in maritime records?

---

# 10 — OWNERSHIP CHANGE EVENTS

Ownership changes should be treated as **events**, not simply overwritten database fields.

| Date | Event | Previous | New | Evidence | Confidence |
|---|---|---|---|---|---|
| `YYYY-MM-DD` | Owner Change | Entity A | Entity B | Registry | HIGH |
| `YYYY-MM-DD` | Manager Change | Entity C | Entity D | Maritime Record | MEDIUM |
| `YYYY-MM-DD` | Flag Change | Flag A | Flag B | Registry | HIGH |
| `YYYY-MM-DD` | Name Change | Vessel A | Vessel B | Vessel Record | HIGH |

### Intelligence Principle

> **A change in ownership, management, flag or vessel name can materially alter the interpretation of historical vessel activity.**

Temporal ownership analysis is therefore necessary when evaluating historical vessel behaviour, corporate relationships or risk exposure.

---

# 11 — CONFLICT RESOLUTION

Different maritime sources may contain different ownership information.

### Example

```text
SOURCE A
Registered Owner → Company A

SOURCE B
Registered Owner → Company B

SOURCE C
Operator → Company B

SOURCE D
Historical Owner → Company A
```

The analyst should not simply select the most convenient record.

The discrepancy must be investigated.

### 01 — IDENTIFY THE CONFLICT

Determine which ownership or management fields disagree.

### 02 — ESTABLISH TEMPORAL CONTEXT

Determine whether the records refer to different dates or ownership periods.

### 03 — ASSESS SOURCE AUTHORITY

Determine which source has the strongest evidentiary value for the specific relationship.

### 04 — CHECK SOURCE INDEPENDENCE

Determine whether apparently independent sources are actually reproducing the same underlying record.

### 05 — CHECK ENTITY IDENTITY

Determine whether different company names represent different entities or naming variations of the same entity.

### 06 — RESOLVE OR PRESERVE UNCERTAINTY

Where the evidence does not support a definitive conclusion, the uncertainty remains part of the assessment.

> **Unresolved uncertainty is an analytical result — not an analytical failure.**

---

# 12 — EVIDENCE VS INFERENCE

Ownership intelligence requires a clear separation between what a source states and what the analyst concludes from it.

| Stage | Question |
|---|---|
| **Observation** | What does the source explicitly state? |
| **Inference** | What does the information suggest? |
| **Validation** | What independent evidence supports it? |
| **Assessment** | What ownership relationship can reasonably be established? |
| **Confidence** | How strong is the evidence? |

### Worked Example

**Observation**

A maritime database lists Company A as the registered owner.

**Inference**

Company A is the legal owner recorded for the vessel during the relevant period.

**Validation**

A separate maritime or registry source reports the same ownership relationship during the same period.

**Assessment**

Company A is assessed as the registered owner for that period.

**Confidence**

Confidence increases where the records are consistent, sufficiently current and independently corroborated.

> **A company association is not automatically evidence of ownership or control.**

---

# 13 — CONFIDENCE FRAMEWORK

Confidence represents the strength of the **evidence supporting a specific ownership relationship**, not simply the analyst's subjective certainty.

### HIGH

Multiple reliable and sufficiently current sources support the same ownership relationship, with no material unresolved contradiction.

### MEDIUM

The relationship is plausible and supported by available evidence, but one or more elements are incomplete, dated, indirect or insufficiently corroborated.

### LOW

Evidence is limited, conflicting, outdated or insufficient to establish the relationship reliably.

---

## Confidence Factors

Ownership confidence is determined through the convergence of:

**Source authority · Source recency · Independent corroboration · Entity resolution · Temporal consistency · Corporate relationship evidence · Record completeness · Contradictions · Historical continuity**

Additional considerations include:

- Whether the source directly identifies the entity
- Whether the relationship is current or historical
- Whether multiple sources agree
- Whether the sources are genuinely independent
- Whether corporate restructuring may explain discrepancies
- Whether the entity's legal identity has been resolved
- Whether the ownership relationship is direct or inferred
- Whether material information is missing

### Critical distinction

> **Confidence in an ownership relationship ≠ confidence in vessel identity.**

A vessel may be confidently identified while its beneficial ownership remains uncertain.

---

# 14 — OWNERSHIP vs CONTROL

Ownership intelligence should avoid treating every corporate association as equivalent.

```text
REGISTERED OWNER
       │
       ▼
LEGAL OWNERSHIP
       │
       ▼
BENEFICIAL INTEREST
       │
       ▼
CORPORATE CONTROL
       │
       ├───────────────┐
       ▼               ▼
TECHNICAL          COMMERCIAL
MANAGEMENT         MANAGEMENT
       │               │
       └───────┬───────┘
               ▼
            OPERATOR
```

These relationships may overlap, but each should be independently established.

### Analytical Principle

> **A registered owner, beneficial owner, manager and operator should not be treated as interchangeable entities simply because they appear together in a vessel record.**

This distinction becomes particularly important when analysing:

- Corporate structures
- Sanctions exposure
- Vessel risk
- Ownership changes
- Fleet relationships
- Historical vessel activity

---

# 15 — OWNERSHIP INTELLIGENCE IN MARITIME RISK

Ownership becomes more valuable when correlated with other maritime intelligence layers.

```text
                         OWNERSHIP
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
          ▼                  ▼                  ▼
      AIS Behaviour      Vessel History      Flag Changes
          │                  │                  │
          ▼                  ▼                  ▼
      STS Activity       Name Changes       Ownership Changes
          │                  │                  │
          └──────────────────┼──────────────────┘
                             ▼
                     CORPORATE NETWORK
                             │
                             ▼
                       RISK ASSESSMENT
```

Ownership intelligence can provide context for:

- Vessel risk assessment
- Corporate network analysis
- Compliance screening
- Historical vessel behaviour
- Fleet relationships
- Ownership changes
- Potentially significant corporate events

> **Ownership should be treated as a relationship layer within the wider vessel intelligence picture, rather than as a standalone database field.**

---

# 16 — INTELLIGENCE OUTPUT

A final ownership assessment should be concise, traceable and reproducible.

## Vessel

`[Vessel Name]`

## IMO

`[IMO Number]`

### Current Assessed Structure

**Registered Owner:**  
`[Entity]`

**Beneficial Owner:**  
`[Entity / Unknown / Not Established]`

**Technical Manager:**  
`[Entity / Unknown]`

**Commercial Manager:**  
`[Entity / N/A / Unknown]`

**Operator:**  
`[Entity / Unknown]`

**Flag:**  
`[Flag]`

**Ownership Effective Date:**  
`[Date / Date Range]`

**Assessment Confidence:**  
`HIGH / MEDIUM / LOW`

### Key Evidence

1. `[Source / ownership record]`
2. `[Independent corroborating source]`
3. `[Historical / corporate evidence]`

### Intelligence Assessment

> `[Concise evidence-based conclusion describing the assessed ownership structure, relevant changes, source consistency and remaining uncertainty.]`

---

# 17 — ANALYTICAL PRINCIPLES

This case study follows five core principles.

### 01 — IDENTIFIERS BEFORE RELATIONSHIPS

Establish the vessel identity before attributing ownership.

### 02 — ROLE SEPARATION

Do not treat owner, manager, beneficial owner and operator as interchangeable.

### 03 — TEMPORAL AWARENESS

Ownership information must be interpreted within its relevant time period.

### 04 — SOURCE CORROBORATION

Important relationships should be supported by independent evidence where possible.

### 05 — EXPLICIT UNCERTAINTY

Where ownership cannot be established confidently, uncertainty is retained rather than concealed.

---

# 18 — TECHNICAL WORKFLOW

The analytical process can be represented as structured data.

```text
VESSEL
   ↓
IDENTIFIER RESOLUTION
   ↓
ENTITY EXTRACTION
   ↓
RELATIONSHIP MAPPING
   ↓
SOURCE NORMALIZATION
   ↓
TEMPORAL COMPARISON
   ↓
CONFLICT DETECTION
   ↓
CONFIDENCE ASSESSMENT
   ↓
STRUCTURED OWNERSHIP RECORD
```

### Example Structured Output

```json
{
  "vessel_id": "IMO XXXXXXX",
  "vessel_name": "Example Vessel",
  "registered_owner": "Example Shipping Ltd",
  "beneficial_owner": "Example Group",
  "technical_manager": "Example Management Ltd",
  "commercial_manager": "Example Maritime Ltd",
  "operator": "Example Shipping",
  "flag": "Example Flag",
  "ownership_effective_date": "YYYY-MM-DD",
  "ownership_confidence": "HIGH"
}
```

The purpose of the technical layer is not to replace maritime judgement.

It is to make the analytical process:

**Structured · Repeatable · Traceable · Auditable**

---

# 19 — TECHNICAL STACK

### Maritime Intelligence

AIS · Vessel Particulars · Ship Registries · GISIS · Equasis · Ownership Databases

### OSINT

Entity Resolution · Corporate Research · Source Correlation · Historical Research · Evidence Validation

### Analytical

Excel · Airtable · Structured Data · Python · SQL

### Intelligence Output

Ownership Mapping · Relationship Graphs · Timeline Reconstruction · Confidence Assessment

---

# 20 — DATA GOVERNANCE

Ownership intelligence can involve commercially sensitive and legally significant information.

This portfolio does not reproduce:

- Confidential employer records
- Proprietary databases
- Restricted corporate intelligence
- Client information
- Internal investigation material
- Non-public ownership records
- Proprietary screenshots or workflows

Where examples are used, entities should be anonymized or based on appropriately licensed/public information.

For each real source, record where appropriate:

- Source name
- Record type
- Publication / update date
- Access date
- Jurisdiction
- Evidence supported
- License / attribution requirements

> **The portfolio demonstrates the analytical methodology, not confidential source material.**

---

# 21 — LIMITATIONS

Ownership intelligence is subject to several limitations.

- Public records may be incomplete.
- Corporate structures may span multiple jurisdictions.
- Ownership records may lag real-world transactions.
- Beneficial ownership may not be publicly disclosed.
- Different databases may use different entity definitions.
- Historical records may be overwritten or unavailable.
- Company name similarity can create false entity matches.
- Multiple sources may derive from the same underlying record.
- Management and ownership relationships may change independently.
- Some corporate relationships may only be inferable rather than directly documented.

Therefore:

> **Absence of public evidence should not automatically be interpreted as absence of ownership or control.**

---

# FINAL INTELLIGENCE ASSESSMENT

Vessel ownership intelligence is fundamentally an **entity-resolution, relationship-mapping and temporal-analysis problem**.

The analyst's task is to connect:

```text
VESSEL
   ↓
IDENTIFIER
   ↓
ENTITY
   ↓
ROLE
   ↓
RELATIONSHIP
   ↓
TIME
   ↓
EVIDENCE
   ↓
CONFIDENCE
```

The strongest ownership assessment is not necessarily the one with the most fields populated.

It is the one where each material relationship can be traced to evidence, interpreted within its correct temporal and corporate context, and clearly distinguished from inference.

---

## Analyst's Note

> **Ownership is a relationship, not a single database field.**

Reliable maritime intelligence depends on understanding:

**who is connected to a vessel,**

**in what capacity,**

**during which period,**

**through what corporate relationship,**

**and how confidently that relationship can be established.**

The objective is not to force certainty where the evidence is incomplete.

**The objective is to produce a defensible ownership picture that can be verified, challenged and updated as new intelligence becomes available.**

---

## Portfolio Context

This case study forms part of a broader maritime intelligence portfolio covering:

| Case Study | Intelligence Question |
|---|---|
| **Satellite Vessel Intelligence** | What can vessel structure reveal from overhead imagery? |
| **Vessel Ownership Intelligence** | Who owns, controls, manages and operates the vessel? |
| **AIS Behavioural Intelligence** | What does the vessel's movement behaviour indicate? |
| **Maritime Risk & Compliance** | What risk indicators surround the vessel or entity? |
| **STS Intelligence** | What evidence supports a potential ship-to-ship transfer? |

Together, the case studies demonstrate an end-to-end maritime intelligence workflow:

```text
OBSERVE
   ↓
IDENTIFY
   ↓
RESOLVE
   ↓
CORRELATE
   ↓
VALIDATE
   ↓
ASSESS
   ↓
INTELLIGENCE
```

---

### Related Case Studies

[← Satellite Vessel Intelligence](../satellite-vessel-intelligence/README.md)

[AIS Behavioural Intelligence →](../ais-behavioural-intelligence/README.md)

[Back to Maritime Intelligence Portfolio →](../README.md)
