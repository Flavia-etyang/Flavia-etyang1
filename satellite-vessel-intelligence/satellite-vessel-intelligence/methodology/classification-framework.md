# Classification Framework

## Purpose

This document describes how a broad vessel classification hypothesis is
formed from overhead imagery. It does not describe a fixed decision tree —
vessel configurations vary, and classification is a judgment supported by
converging evidence rather than a lookup against a single rule.

## Principle

Classification is based on **converging evidence**, not a single visual
cue. A clear cargo deck alone does not establish an oil-tanker
classification. Cylindrical or spherical containment structures alone do
not establish a gas-carrier classification. A hull with rectangular stack
geometry alone does not establish a container-vessel classification.

Each broad type is instead assessed against a small set of structural
indicators that, taken together, make one classification more plausible
than the alternatives.

## Structural indicators by broad type

**Tankers (crude oil, product):**
- Longitudinal deck piping and manifold arrangement
- Predominantly clear, unobstructed cargo deck
- Aft-positioned superstructure
- Hull proportions consistent with bulk liquid carriage

**Gas carriers (LPG / LNG):**
- Distinct cargo-containment architecture on deck (cylindrical, spherical,
  or membrane-type, depending on vessel design)
- Containment structures are visually distinguishable from open deck space
- Aft-positioned superstructure

**Container vessels:**
- Repetitive rectangular cargo geometry (container stacks)
- Regular bay spacing across the deck
- Deck cranes, where fitted
- Hull proportions consistent with a higher L/B ratio than bulk carriers

## Process

1. Identify which indicators are visible.
2. Note which indicators are absent, obscured, or ambiguous.
3. Compare the observed pattern against more than one broad-type
   hypothesis.
4. Select the hypothesis best supported by the balance of evidence.
5. Record classification confidence separately from identity confidence
   (see `confidence-framework.md`).

## What this framework does not do

It does not assign vessel identity, ownership, flag, or operator. Those
require independent validation sources (AIS, vessel particulars, registry
data) and are treated as a separate analytical question. See
`evidence-vs-inference.md`.
