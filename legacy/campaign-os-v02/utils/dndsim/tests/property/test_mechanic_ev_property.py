"""ADR-0008's binding property test: registry-wide, not per-Mechanic.

For every Mechanic registered anywhere in :data:`dndsim.core.mechanic.mechanics`,
its Monte-Carlo mean over N universes must converge to its own declared
``expected_value()`` within tolerance. This file adds no Mechanic-specific
logic — it stays correct as the registry grows past today's one member.
"""

from __future__ import annotations

from hypothesis import given, settings
from hypothesis import strategies as st

from dndsim import plugins
from dndsim.core.mechanic import mechanics
from dndsim.core.rng import BatchRNG

plugins.load_rules_packs()

N_UNIVERSES = 20_000
# Monte-Carlo standard error at N=20,000 for a bounded-per-hit outcome is
# small; this tolerance is generous enough to avoid flaking while still
# catching a genuinely wrong expected_value().
ABS_TOLERANCE = 0.75
REL_TOLERANCE = 0.05


@settings(deadline=None, max_examples=25)
@given(mechanic_id=st.sampled_from(sorted(mechanics)), data=st.data())
def test_mc_mean_converges_to_declared_expected_value(
    mechanic_id: str, data: st.DataObject
) -> None:
    mechanic_cls = mechanics.get(mechanic_id)
    instance = data.draw(mechanic_cls.hypothesis_strategy())
    seed = data.draw(st.integers(min_value=0, max_value=2**31 - 1))

    outcomes = instance.resolve(BatchRNG(seed=seed), size=N_UNIVERSES)
    mc_mean = float(outcomes.mean())
    ev = instance.expected_value()

    tolerance = ABS_TOLERANCE + REL_TOLERANCE * abs(ev)
    message = f"{mechanic_id}: MC mean {mc_mean} vs declared EV {ev} (tolerance {tolerance})"
    assert abs(mc_mean - ev) <= tolerance, message
