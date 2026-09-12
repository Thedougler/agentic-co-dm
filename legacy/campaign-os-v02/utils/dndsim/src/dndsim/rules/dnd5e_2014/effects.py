"""Timed effects: application, scheduled expiry, and concentration-sourced
removal — a batched (per-universe) tracker, expressed through the core's own
:class:`~dndsim.core.tags.BatchTags` rather than a bespoke array-of-objects
per combatant.

An effect is applied under a `source` id, opaque to this module exactly as
:class:`~dndsim.core.entity.Modifier.source` is opaque to the core. A
concentration-sourced effect always uses :func:`concentration_source`'s id
as its `source`; when that concentration breaks,
:meth:`EffectTracker.remove_from_source` removes exactly the effects that
carry it — never effects from any other source.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

import numpy as np

from dndsim.rules.dnd5e_2014.mechanics import ConcentrationSaveMechanic

if TYPE_CHECKING:
    from dndsim.core.rng import BatchRNG
    from dndsim.core.tags import BatchTags
    from dndsim.rules.dnd5e_2014.advantage import AdvantageMode


def concentration_source(owner_id: str) -> str:
    """The effect-`source` id every effect a `owner_id`'s concentration
    applies must carry, so a broken check removes exactly those effects."""
    return f"conc:{owner_id}"


@dataclass(slots=True)
class _ActiveEffect:
    source: str
    tag: str
    duration: np.ndarray  # per-universe rounds remaining; ignored where ~active
    active: np.ndarray  # per-universe bool: currently applied in this universe
    # (ability, dc) for a save-ends rider (issue #63's save_ends interlock,
    # e.g. Hideous Laughter's incapacitated_prone) — None for an effect that
    # never re-saves, ticked by :meth:`EffectTracker.tick_saves`.
    save_ends: tuple[str, int] | None = None


@dataclass(slots=True)
class EffectTracker:
    """Batched effect application, scheduled expiry, and source-keyed
    removal for one :class:`~dndsim.core.tags.BatchTags` instance. One
    tracker covers every effect that can land on the entities sharing that
    `BatchTags` (typically one combatant)."""

    tags: BatchTags
    size: int
    _effects: list[_ActiveEffect] = field(default_factory=list)

    def apply(
        self,
        *,
        source: str,
        tag: str,
        mask: np.ndarray,
        duration_rounds: int | None = None,
        save_ends: tuple[str, int] | None = None,
    ) -> None:
        """Apply `tag`, sourced from `source`, to every universe in `mask`.
        `duration_rounds=None` means indefinite — it expires only via
        :meth:`remove_from_source` or :meth:`remove`, never by ticking (a
        concentration-sourced effect: it lasts exactly as long as the
        concentration that sourced it, not a fixed round count). `save_ends`
        (issue #63) additionally lets :meth:`tick_saves` end it early on a
        successful re-save, independent of `duration_rounds`."""
        duration = np.full(self.size, -1, dtype=np.int32)
        if duration_rounds is not None:
            duration[mask] = duration_rounds
        active = np.zeros(self.size, dtype=np.bool_)
        active[mask] = True
        effect = _ActiveEffect(
            source=source, tag=tag, duration=duration, active=active, save_ends=save_ends
        )
        self._effects.append(effect)
        self.tags.add(tag, mask)

    def tick_end_of_round(self) -> None:
        """Decrement every timed (non-indefinite) effect's duration by one
        round; any that reach zero expire and are untagged in exactly the
        universes where they were active. Indefinite effects
        (`duration_rounds=None` at apply time) never tick — this is the
        "effects expire on schedule" half of #45's acceptance criteria."""
        remaining: list[_ActiveEffect] = []
        for effect in self._effects:
            timed = effect.active & (effect.duration >= 0)
            effect.duration = np.where(timed, effect.duration - 1, effect.duration)
            expiring = timed & (effect.duration < 0)
            if expiring.any():
                self.tags.remove(effect.tag, expiring)
                effect.active = effect.active & ~expiring
            if effect.active.any():
                remaining.append(effect)
        self._effects = remaining

    def tick_saves(
        self, rng: BatchRNG, *, save_bonus: Callable[[str], int], mask: np.ndarray
    ) -> None:
        """Re-save every active `save_ends`-tagged effect (issue #63's
        save_ends interlock — 5e RAW "at the end of each of its turns"): on
        success the effect ends immediately, in exactly the universes that
        passed, instead of running out its `duration_rounds` (or, for the
        common case of no declared duration, never ending at all). Without
        this, a newly-real condition like `incapacitated_prone` (Hideous
        Laughter) applies once and locks its target out of every remaining
        round — overshooting the reference the opposite direction from the
        gap issue #63 diagnosed. `save_bonus` resolves the effect's own save
        ability to this tracker's owner's bonus, the same lookup
        :func:`~dndsim.rules.dnd5e_2014.combat._resolve_save_primitive` uses
        for the initial save.

        `mask` (rolled-initiative turn order) restricts this re-save to the
        universes where this is genuinely this owner's own end-of-turn right
        now — with per-universe rolled initiative, ``END_OF_TURN:<cid>`` can
        fire more than once per round (once per turn-order bucket this
        combatant occupies across the batch), so an unmasked re-save would
        double-roll the same round's save for whichever universes are
        dispatched in an earlier bucket."""
        remaining: list[_ActiveEffect] = []
        for effect in self._effects:
            if effect.save_ends is not None and bool((effect.active & mask).any()):
                ability, dc = effect.save_ends
                mechanic = ConcentrationSaveMechanic(con_bonus=save_bonus(ability), dc=dc)
                outcomes = mechanic.resolve(rng, size=self.size)
                passed = (outcomes >= 1.0) & effect.active & mask
                if bool(passed.any()):
                    self.tags.remove(effect.tag, passed)
                    effect.active = effect.active & ~passed
            if effect.active.any():
                remaining.append(effect)
        self._effects = remaining

    def remove_from_source(self, source: str, mask: np.ndarray) -> None:
        """Remove, in every universe selected by `mask`, every effect
        sourced from `source` — never an effect from any other source. This
        is the exact mechanism a broken concentration check uses: it never
        needs to know which tags concentration granted, only its own source
        id (:func:`concentration_source`)."""
        remaining: list[_ActiveEffect] = []
        for effect in self._effects:
            if effect.source == source:
                removed = effect.active & mask
                if removed.any():
                    self.tags.remove(effect.tag, removed)
                effect.active = effect.active & ~mask
            if effect.active.any():
                remaining.append(effect)
        self._effects = remaining

    def active_sources(self, tag: str) -> list[str]:
        """Every distinct `source` currently holding `tag` active anywhere
        in the batch — for tests and inspection, never consulted by
        resolution logic itself."""
        return [
            effect.source for effect in self._effects if effect.tag == tag and effect.active.any()
        ]


def resolve_concentration_checks(
    *,
    damage: np.ndarray,
    mask: np.ndarray,
    con_bonus: int,
    advantage_mode: AdvantageMode,
    rng: BatchRNG,
) -> np.ndarray:
    """The damage-triggered concentration check (PHB p.203): DC
    ``max(10, damage // 2)``, one roll per universe in `mask`. `damage` is
    masked-size (shape ``(mask.sum(),)``), matching
    :meth:`~dndsim.core.resources.ResourcePool.spend`'s own `amount`
    convention. DC varies per-universe with the damage just taken, so
    universes are bucketed by their unique DC and each bucket resolved
    through one scalar-`dc` :class:`~dndsim.rules.dnd5e_2014.mechanics.ConcentrationSaveMechanic`
    instance — the same bucket-by-choice shape ADR-0011 already uses for
    divergent per-universe decisions. Returns a full-size boolean pass/fail
    array (only meaningful where `mask` is True)."""
    size = mask.shape[0]
    idx = np.flatnonzero(mask)
    if idx.shape[0] != damage.shape[0]:
        raise ValueError(f"damage has {damage.shape[0]} entries but mask selects {idx.shape[0]}")
    passed = np.zeros(size, dtype=np.bool_)
    dc = np.maximum(10, damage.astype(np.int64) // 2)
    for unique_dc in np.unique(dc):
        bucket_idx = idx[dc == unique_dc]
        mechanic = ConcentrationSaveMechanic(
            con_bonus=con_bonus, dc=int(unique_dc), advantage_mode=advantage_mode
        )
        outcomes = mechanic.resolve(rng, size=bucket_idx.shape[0])
        passed[bucket_idx] = outcomes >= 1.0
    return passed


def check_concentration_and_break(
    *,
    tracker: EffectTracker,
    owner_id: str,
    damage: np.ndarray,
    concentrating_mask: np.ndarray,
    con_bonus: int,
    advantage_mode: AdvantageMode,
    rng: BatchRNG,
) -> np.ndarray:
    """Run the damage-triggered concentration check for every universe in
    `concentrating_mask`, and for every universe that fails, remove exactly
    the effects `owner_id`'s concentration sourced (via
    :meth:`EffectTracker.remove_from_source`). Returns the per-universe
    broke-concentration mask."""
    passed = resolve_concentration_checks(
        damage=damage,
        mask=concentrating_mask,
        con_bonus=con_bonus,
        advantage_mode=advantage_mode,
        rng=rng,
    )
    broke: np.ndarray = concentrating_mask & ~passed
    if broke.any():
        tracker.remove_from_source(concentration_source(owner_id), broke)
    return broke
