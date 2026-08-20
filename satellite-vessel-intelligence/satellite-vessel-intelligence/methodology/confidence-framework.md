# Confidence Framework

## Confidence levels

**HIGH**
Multiple independent visual indicators converge, and image quality is
sufficient to observe them clearly.

**MEDIUM**
Classification is plausible but evidence is partially obscured or
ambiguous — some expected indicators are visible, others cannot be
confirmed.

**LOW**
Evidence is insufficient, conflicting, or limited — a classification
hypothesis may still be offered, but it should be presented as
provisional.

## Classification confidence ≠ identity confidence

These are separate analytical dimensions and should never be collapsed
into a single number.

- **Classification confidence** — how confident the analysis is that the
  vessel belongs to a given broad type (tanker, gas carrier, container
  vessel, etc.), based on structural evidence visible in the imagery.
- **Identity confidence** — how confident the analysis is about *which
  specific vessel* this is (name, IMO number, owner, flag), which
  typically requires validation against independent data sources such as
  AIS, vessel particulars, or registry records.

**Example:**

```
Classification Confidence: HIGH
Identity Confidence:       LOW
```

A vessel's structural class can be assessed with high confidence directly
from imagery, while its specific identity may remain low-confidence or
unresolved without independent corroborating data. Treating these as one
combined score would overstate what the imagery alone can support.

## Applying this in practice

Every assessment in `data/vessel-assessments.csv` records
`classification_confidence` and `identity_confidence` as separate
columns, alongside `detection_confidence` and `dimension_confidence`.
`identity_confidence` is marked `N/A` where no attempt at identity
resolution was made.
