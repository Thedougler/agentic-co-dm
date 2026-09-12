"""Re-measures ADR-0011's decision-bucket ceiling against a real legendary
statblock (issue #52's other acceptance criterion), generalizing issue #59's
own remeasurement on its synthetic 3-vs-3 "Grung Chief" fixture (167
decision points, mean 2.28, max 3 — commit 5ee221c0's own message) to the
real Otar the Foul content this harness's matchup set uses.

No source file is touched to get this telemetry: `combat.py` imports
`bucket_by_choice` by name into its own module namespace
(`from dndsim.core.universe import ... bucket_by_choice`), so monkeypatching
the name bound in `dndsim.rules.dnd5e_2014.combat` — restored in a
`finally` — counts every call and every returned bucket list's length for
the duration of one `run_combat` call, with zero permanent change to either
module.

Run as one command from the repo root::

    uv run --project utils/dndsim python utils/dndsim/scripts/measure_decision_buckets.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import numpy as np  # noqa: E402
from parity_matchups import build_matchups  # noqa: E402

from dndsim import plugins  # noqa: E402
from dndsim.core.rng import cell_seed  # noqa: E402
from dndsim.core.universe import UniverseBatch  # noqa: E402
from dndsim.rules.dnd5e_2014 import combat as combat_module  # noqa: E402
from dndsim.rules.dnd5e_2014.combat import run_combat  # noqa: E402

SEED = 1
UNIVERSES = 8_000
ROUND_CAP = 20


def measure(matchup_id: str) -> tuple[int, float, int]:
    """Returns ``(decision_points, mean_bucket_count, max_bucket_count)``
    for the named matchup — one call to `bucket_by_choice` is one decision
    point, its returned list's length is that decision's bucket count."""
    # getattr/setattr rather than direct attribute access: `combat.py`
    # (rules/dnd5e_2014/** — out of this issue's owned paths) has no
    # `__all__`, so mypy strict's implicit-reexport check would otherwise
    # flag `combat_module.bucket_by_choice` as an unexported attribute.
    bucket_counts: list[int] = []
    real_bucket_by_choice = getattr(combat_module, "bucket_by_choice")  # noqa: B009

    def counting_bucket_by_choice(codes: np.ndarray) -> list[tuple[int, np.ndarray]]:
        buckets: list[tuple[int, np.ndarray]] = real_bucket_by_choice(codes)
        bucket_counts.append(len(buckets))
        return buckets

    matchup = next(m for m in build_matchups() if m.id == matchup_id)
    setattr(combat_module, "bucket_by_choice", counting_bucket_by_choice)  # noqa: B010
    try:
        seed = cell_seed(SEED, matchup_id)
        batch = UniverseBatch(size=UNIVERSES, seed=seed)
        run_combat(list(matchup.party), list(matchup.enemies), batch, round_cap=ROUND_CAP)
    finally:
        setattr(combat_module, "bucket_by_choice", real_bucket_by_choice)  # noqa: B010

    decision_points = len(bucket_counts)
    mean_buckets = sum(bucket_counts) / decision_points if decision_points else 0.0
    max_buckets = max(bucket_counts) if bucket_counts else 0
    return decision_points, mean_buckets, max_buckets


def main() -> int:
    plugins.load_rules_packs()
    plugins.load_policies()
    print(f"seed={SEED} universes={UNIVERSES} round_cap={ROUND_CAP}\n")
    print("ADR-0011 Phase 0 (toy 2-vs-2): bucket count flat, mean 1.51-1.62, max 2")
    print(
        "Issue #59 remeasurement (synthetic 3-vs-3, legendary+lair Grung Chief fixture): "
        "167 decision points, mean 2.28, max 3\n"
    )
    for matchup_id in (
        "dnd5e_2014:combatant/perrin-black-jaw-vs-dnd5e_2014:combatant/grung-elite-warrior",
        "dnd5e_2014:combatant/party-vs-dnd5e_2014:combatant/grung-elite-warrior",
        "dnd5e_2014:combatant/party-vs-dnd5e_2014:combatant/grung-elite-warrior-x2",
        "dnd5e_2014:combatant/party-vs-dnd5e_2014:combatant/otar-the-foul",
    ):
        decision_points, mean_buckets, max_buckets = measure(matchup_id)
        print(
            f"{matchup_id}: {decision_points} decision points, "
            f"mean {mean_buckets:.2f}, max {max_buckets}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
