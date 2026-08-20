# Dimension Estimation

## Definitions

**Length Overall (LOA)** — the distance from the vessel's forward-most
point to its aft-most point, measured along the hull's long axis.

**Beam** — the vessel's maximum breadth, measured perpendicular to the
long axis at its widest point.

**L/B ratio** — `LOA ÷ Beam`. Used as one supporting input to a
classification hypothesis, not as a standalone determinant.

## Pixel-based measurement

Where Ground Sampling Distance (GSD) is known:

```
Physical distance = Pixel distance x Ground Sampling Distance (GSD)
```

This is implemented in `src/measurement.py::pixels_to_metres()`.

## Uncertainty

Estimates are reported with an explicit uncertainty margin, e.g.:

```
182 ± 5 m
```

rather than false precision such as `182.000 m`.

Uncertainty should widen when any of the following apply:

- **Image resolution** is coarse relative to the vessel's size
- **Vessel orientation** is not fully perpendicular to the measurement
  axis, introducing foreshortening
- **Georeferencing accuracy** of the source image is unknown or poor
- **Partial occlusion** (cloud, wake, adjacent vessels, imagery edge)
  obscures the bow, stern, or beam extent

`src/measurement.py::measurement_with_uncertainty()` models a simple,
fixed pixel-level uncertainty margin as a starting point. In practice,
the qualitative factors above should also be recorded alongside the
numeric estimate — see `confidence-framework.md` for how this feeds into
`dimension_confidence`.

## Bounding box caveat

The bounding rectangle used during measurement is an **annotation and
measurement aid** — it should not automatically be interpreted as the
vessel's exact physical footprint. See the "Bounding Box Explanation"
section of the top-level README for the full discussion of wake,
shadow, rotation, and resolution effects on bounding-box accuracy.
