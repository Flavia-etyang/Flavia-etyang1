"""
measurement.py

Foundational analytical utilities for converting pixel-based observations
from overhead imagery into vessel dimension estimates.

These functions intentionally stay simple. The purpose of this module is
not to demonstrate advanced machine learning — it is to demonstrate that
maritime domain knowledge (Ground Sampling Distance, L/B ratio, and
measurement uncertainty) can be translated into a small, correct,
well-documented analytical tool.

All returned measurements should be treated as estimates. Overhead
imagery measurement is subject to error introduced by vessel orientation,
image resolution, georeferencing accuracy, and partial occlusion. See
methodology/dimension-estimation.md for the full discussion.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Measurement:
    """A single dimension estimate with an explicit uncertainty margin.

    Attributes:
        value_m: Central estimate of the measured dimension, in metres.
        uncertainty_m: Plus/minus uncertainty margin, in metres.
    """

    value_m: float
    uncertainty_m: float

    def __str__(self) -> str:
        return f"{self.value_m:.1f} ± {self.uncertainty_m:.1f} m"


def pixels_to_metres(pixel_distance: float, ground_sampling_distance_m: float) -> float:
    """Convert a pixel distance to a physical distance using known GSD.

    Physical distance = pixel distance x Ground Sampling Distance (GSD).

    Args:
        pixel_distance: Distance measured in the image, in pixels.
        ground_sampling_distance_m: Ground Sampling Distance of the
            source image, in metres per pixel.

    Returns:
        The estimated physical distance in metres.

    Raises:
        ValueError: If either input is negative.
    """
    if pixel_distance < 0:
        raise ValueError("pixel_distance must be non-negative")
    if ground_sampling_distance_m < 0:
        raise ValueError("ground_sampling_distance_m must be non-negative")

    return pixel_distance * ground_sampling_distance_m


def length_to_beam_ratio(length_m: float, beam_m: float) -> float:
    """Calculate the length-to-beam (L/B) ratio for a vessel.

    L/B ratio is one input among several used to support (never to
    single-handedly determine) a vessel classification hypothesis.

    Args:
        length_m: Estimated length overall (LOA), in metres.
        beam_m: Estimated maximum beam, in metres.

    Returns:
        The L/B ratio, unitless.

    Raises:
        ValueError: If beam_m is zero or either input is negative.
    """
    if length_m < 0 or beam_m < 0:
        raise ValueError("length_m and beam_m must be non-negative")
    if beam_m == 0:
        raise ValueError("beam_m must be greater than zero")

    return length_m / beam_m


def measurement_with_uncertainty(
    pixel_distance: float,
    ground_sampling_distance_m: float,
    uncertainty_pixels: float = 3.0,
) -> Measurement:
    """Estimate a physical dimension and its uncertainty from pixel data.

    Uncertainty is modelled as a fixed pixel-count margin (default: 3 px)
    propagated through the same GSD used for the central estimate. This is
    a deliberately simple model — it does not account for vessel
    orientation error, wake/shadow contamination, or georeferencing error,
    which should be assessed separately and noted qualitatively in the
    intelligence assessment.

    Args:
        pixel_distance: Distance measured in the image, in pixels.
        ground_sampling_distance_m: Ground Sampling Distance of the
            source image, in metres per pixel.
        uncertainty_pixels: Assumed pixel-level measurement uncertainty.
            Defaults to 3 pixels, a conservative starting margin for
            medium-resolution overhead imagery.

    Returns:
        A Measurement with a central estimate and an uncertainty margin,
        both in metres.
    """
    value_m = pixels_to_metres(pixel_distance, ground_sampling_distance_m)
    uncertainty_m = pixels_to_metres(uncertainty_pixels, ground_sampling_distance_m)

    return Measurement(value_m=round(value_m, 1), uncertainty_m=round(uncertainty_m, 1))


if __name__ == "__main__":
    # Minimal, illustrative usage — not a substitute for the notebook.
    gsd = 0.5  # metres per pixel, illustrative value
    loa = measurement_with_uncertainty(pixel_distance=364, ground_sampling_distance_m=gsd)
    beam = measurement_with_uncertainty(pixel_distance=58, ground_sampling_distance_m=gsd)

    print(f"Estimated LOA:  {loa}")
    print(f"Estimated beam: {beam}")
    print(f"L/B ratio:      {length_to_beam_ratio(loa.value_m, beam.value_m):.2f}")
