"""Wilson score confidence interval for a proportion.

Used by adaptive stopping (:mod:`dndsim.core.adaptive`) to decide whether a
run's success-rate estimate has tightened enough to halt, and by any report
that needs to attach an interval to a reported rate.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ConfidenceInterval:
    """A proportion's point estimate and interval bounds.

    ``p``/``lo``/``hi`` are all ``None`` together exactly when ``trials``
    was 0 — never read a lone ``None`` as zero.
    """

    p: float | None
    lo: float | None
    hi: float | None

    @property
    def half_width(self) -> float | None:
        """``(hi - lo) / 2``, or ``None`` when the interval is undefined."""
        if self.lo is None or self.hi is None:
            return None
        return (self.hi - self.lo) / 2


def wilson_interval(successes: int, trials: int, z: float = 1.96) -> ConfidenceInterval:
    """The Wilson score interval for ``successes`` out of ``trials``.

    ``z=1.96`` is the 95% interval, the default used throughout dndsim's
    adaptive stopping and reporting.
    """
    if trials == 0:
        return ConfidenceInterval(p=None, lo=None, hi=None)
    if successes < 0 or successes > trials:
        raise ValueError(f"successes ({successes}) must be within [0, trials={trials}]")
    p = successes / trials
    z2 = z * z
    denom = 1 + z2 / trials
    center = (p + z2 / (2 * trials)) / denom
    half = (z * ((p * (1 - p) / trials + z2 / (4 * trials * trials)) ** 0.5)) / denom
    return ConfidenceInterval(p=p, lo=max(0.0, center - half), hi=min(1.0, center + half))
