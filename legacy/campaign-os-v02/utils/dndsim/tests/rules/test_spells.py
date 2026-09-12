"""The spell-library Importer (issue #48): name resolution and
compile_spellcasting's Action/ActionSim/Modifier output — plus the
ADR-0009 boundary proof (no spell vocabulary outside the spell modules)."""

from __future__ import annotations

import re
from collections.abc import Iterator
from pathlib import Path

import pytest

import dndsim
import dndsim.rules.dnd5e_2014
from dndsim.core.importer import importers
from dndsim.rules.dnd5e_2014.attack_string import AttackAction, SaveAction, UnmodeledAction
from dndsim.rules.dnd5e_2014.compile import compile_statblock
from dndsim.rules.dnd5e_2014.sim_extension import SpellcastingPool
from dndsim.rules.dnd5e_2014.spells import (
    IMPORTER_ID,
    SPELL_DIRS,
    SpellCompileError,
    SpellContent,
    SpellImporter,
    clear_spell_cache,
    compile_spellcasting,
    load_spell_def,
    spell_slugify,
)
from dndsim.rules.dnd5e_2014.statblock import parse_statblock_page

REPO_ROOT = Path(__file__).resolve().parents[4]
SRD_SPELL_DIRS = SPELL_DIRS


@pytest.fixture(autouse=True)
def _clear_cache() -> Iterator[None]:
    clear_spell_cache()
    yield
    clear_spell_cache()


def test_spell_importer_is_registered() -> None:
    assert IMPORTER_ID in importers
    assert importers.get(IMPORTER_ID) is SpellImporter


# --- name resolution: exact slug -> "-spell" suffix -> alias ----------------


def test_spell_slugify_drops_apostrophes_rather_than_hyphenating() -> None:
    assert spell_slugify("Hunter's Mark") == "hunters-mark"


def test_load_spell_def_resolves_by_exact_slug(tmp_path: Path) -> None:
    target = tmp_path / "hex.md"
    target.write_text("# Hex\n\nFlavor only.", encoding="utf-8")
    with pytest.raises(SpellCompileError, match=re.escape(str(target))):
        load_spell_def("Hex", dirs=(str(tmp_path),))


def test_load_spell_def_resolves_by_spell_disambiguation_suffix(tmp_path: Path) -> None:
    target = tmp_path / "darkness-spell.md"
    target.write_text("# Darkness\n\nFlavor only.", encoding="utf-8")
    with pytest.raises(SpellCompileError, match=re.escape(str(target))):
        load_spell_def("Darkness", dirs=(str(tmp_path),))


def test_load_spell_def_resolves_by_frontmatter_alias(tmp_path: Path) -> None:
    target = tmp_path / "hideous-laughter.md"
    target.write_text(
        '---\naliases: ["Tasha\'s Hideous Laughter"]\n---\n\n# Hideous Laughter\n\nFlavor only.',
        encoding="utf-8",
    )
    with pytest.raises(SpellCompileError, match=re.escape(str(target))):
        load_spell_def("Tasha's Hideous Laughter", dirs=(str(tmp_path),))


def test_load_spell_def_unresolvable_name_names_candidates(tmp_path: Path) -> None:
    (tmp_path / "fireball.md").write_text("# Fireball\n\nFlavor only.", encoding="utf-8")
    with pytest.raises(SpellCompileError, match="no page found"):
        load_spell_def("Firewalk", dirs=(str(tmp_path),))


def test_load_spell_def_page_names_it_not_yet_modeled(tmp_path: Path) -> None:
    (tmp_path / "prestidigitation.md").write_text(
        "# Prestidigitation\n\nFlavor only.", encoding="utf-8"
    )
    with pytest.raises(SpellCompileError, match="no sim data on page"):
        load_spell_def("Prestidigitation", dirs=(str(tmp_path),))


def test_real_srd_spell_disambiguation_suffix_file_resolves_but_is_unmodeled() -> None:
    with pytest.raises(SpellCompileError, match="no sim data on page"):
        load_spell_def("Darkness", dirs=SRD_SPELL_DIRS)


# --- compile_spellcasting: attack / save / heal / self-buff -----------------


def _pool(**overrides: object) -> SpellcastingPool:
    base: dict[str, object] = {
        "ability": "cha",
        "dc": 15,
        "attack_bonus": 7,
        "known": ["Hex"],
    }
    base.update(overrides)
    return SpellcastingPool.model_validate(base)


def test_undeclared_slot_resource_is_rejected() -> None:
    pool = _pool(slots={1: "undeclared_slot"})
    with pytest.raises(SpellCompileError, match="not a declared sim.resources id"):
        compile_spellcasting(pool, resource_ids=frozenset(), source="test.md")


def test_leveled_spell_with_no_usable_slot_warns_and_skips() -> None:
    pool = _pool(known=["Hex"], slots={})
    result = compile_spellcasting(pool, resource_ids=frozenset(), source="test.md")
    assert result.actions == ()
    assert any("no declared slot" in w for w in result.warnings)


def test_hex_compiles_to_extra_damage_modifier_with_cost_attached() -> None:
    pool = _pool(known=["Hex"], slots={1: "pact_slot_1"})
    result = compile_spellcasting(
        pool, resource_ids={"pact_slot_1"}, source="test.md", load=lambda name: _load_real(name)
    )
    assert len(result.abilities) == 1
    ability = result.abilities[0]
    assert ability.kind == "extra_damage"  # type: ignore[attr-defined]
    assert ability.cost is not None  # type: ignore[attr-defined]
    assert ability.cost.resource == "pact_slot_1"  # type: ignore[attr-defined]
    assert any("aren't modeled" in w for w in result.warnings)


def test_bless_cost_cannot_attach_to_flat_to_hit_and_warns() -> None:
    pool = _pool(known=["Bless"], slots={1: "cleric_slot_1"})
    result = compile_spellcasting(
        pool, resource_ids={"cleric_slot_1"}, source="test.md", load=lambda name: _load_real(name)
    )
    assert len(result.abilities) == 1
    ability = result.abilities[0]
    assert ability.kind == "flat_to_hit"  # type: ignore[attr-defined]
    assert not hasattr(ability, "cost")  # degraded free: this kind carries no cost field at all
    assert any("cast cost (cleric_slot_1) not attached" in w for w in result.warnings)


def test_armor_of_agathys_compiles_temp_hp_and_retaliate() -> None:
    pool = _pool(known=["Armor of Agathys"], slots={1: "pact_slot_1"})
    result = compile_spellcasting(
        pool, resource_ids={"pact_slot_1"}, source="test.md", load=lambda name: _load_real(name)
    )
    kinds = sorted(a.kind for a in result.abilities)  # type: ignore[attr-defined]
    assert kinds == ["retaliate", "temp_hp"]
    temp_hp = next(a for a in result.abilities if a.kind == "temp_hp")  # type: ignore[attr-defined]
    assert temp_hp.cost.resource == "pact_slot_1"  # type: ignore[attr-defined]


def test_eldritch_blast_cantrip_scaling_beams_warn_when_over_one() -> None:
    pool = _pool(known=["Eldritch Blast"], level=5)
    result = compile_spellcasting(
        pool, resource_ids=frozenset(), source="test.md", load=lambda name: _load_real(name)
    )
    assert len(result.actions) == 1
    assert isinstance(result.actions[0], AttackAction)
    assert any("beams/attacks not modeled" in w for w in result.warnings)


def test_eldritch_blast_single_beam_at_low_level_does_not_warn() -> None:
    pool = _pool(known=["Eldritch Blast"], level=1)
    result = compile_spellcasting(
        pool, resource_ids=frozenset(), source="test.md", load=lambda name: _load_real(name)
    )
    assert not any("beams" in w for w in result.warnings)


def test_hideous_laughter_incapacitating_effect_tag_compiles_through() -> None:
    pool = _pool(known=["Hideous Laughter"], slots={1: "bard_slot_1", 2: "bard_slot_2"})
    result = compile_spellcasting(
        pool,
        resource_ids={"bard_slot_1", "bard_slot_2"},
        source="test.md",
        load=lambda name: _load_real(name),
    )
    assert len(result.actions) == 1
    action = result.actions[0]
    assert isinstance(action, SaveAction)
    # "incapacitated_prone" is part of the condition vocabulary (the union of
    # the reference engine's five copies), so the spell's whole point — the
    # target loses its turns — survives compilation instead of degrading to an
    # empty on_fail with a warning.
    assert [e.effect for e in action.on_fail.effects] == ["incapacitated_prone"]
    assert not any("no matching condition/rider tag" in w for w in result.warnings)
    # issue #63: save_ends now compiles through onto the rider (consumed by
    # combat.py's EffectTracker.tick_saves at the target's own end-of-turn)
    # instead of degrading to a warning; the fence's own save_ends omits
    # `dc`, so it backfills to the pool's own spell save DC.
    rider = action.on_fail.effects[0]
    assert rider.save_ends is not None
    assert rider.save_ends["save"] == "wis"
    assert rider.save_ends["dc"] == pool.dc
    assert not any("save_ends" in w for w in result.warnings)
    # No scaling on Hideous Laughter -> only the lowest qualifying slot (L1) is cast.
    assert action.name == "Hideous Laughter"


def test_cure_wounds_upcast_emits_one_action_per_castable_slot_level() -> None:
    pool = _pool(known=["Cure Wounds"], slots={1: "bard_slot_1", 2: "bard_slot_2"}, ability_mod=5)
    result = compile_spellcasting(
        pool,
        resource_ids={"bard_slot_1", "bard_slot_2"},
        source="test.md",
        load=lambda name: _load_real(name),
    )
    names = sorted(a.name for a in result.actions)
    assert names == ["Cure Wounds (L1)", "Cure Wounds (L2)"]
    for action in result.actions:
        assert isinstance(action, UnmodeledAction)
    l1_sim = result.action_sim["Cure Wounds (L1)"]
    l2_sim = result.action_sim["Cure Wounds (L2)"]
    assert l1_sim.heal is not None and l1_sim.heal.dice == "2d8+5"
    # scaled first term, +ability_mod
    assert l2_sim.heal is not None and l2_sim.heal.dice == "4d8+5"
    assert l1_sim.cost is not None and l1_sim.cost.resource == "bard_slot_1"
    assert l2_sim.cost is not None and l2_sim.cost.resource == "bard_slot_2"


def _load_real(name: str) -> SpellContent:
    return load_spell_def(name, dirs=SRD_SPELL_DIRS)


# --- end-to-end: real SRD content + a real multiclass caster ---------------

PERRIN_FIXTURE_STATBLOCK = """\
```statblock
name: Perrin Black-Jaw
ac: 18
hp: 49
stats: [6, 18, 15, 11, 11, 20]
sim:
  side: party
  resources:
    - { id: bard_slot_1, max: 4, recharge: long_rest }
    - { id: bard_slot_2, max: 2, recharge: long_rest }
    - { id: pact_slot_1, max: 2, recharge: long_rest }
  spellcasting:
    - { ability: cha, dc: 16, attack_bonus: 8, level: 5, ability_mod: 5,
        slots: { 1: bard_slot_1, 2: bard_slot_2 },
        known: ["Hideous Laughter"] }
    - { ability: cha, dc: 16, attack_bonus: 8, level: 5,
        slots: { 1: pact_slot_1 },
        known: ["Eldritch Blast", "Hex", "Armor of Agathys"] }
```
"""


def test_perrin_two_independent_pools_resolve_and_compile(monkeypatch: pytest.MonkeyPatch) -> None:
    # compile_statblock's default spell loader resolves SPELL_DIRS from
    # __file__, not cwd, so this chdir is belt-and-suspenders rather than
    # load-bearing — kept so the test still proves invocation-order
    # independence rather than relying on that anchoring alone.
    monkeypatch.chdir(REPO_ROOT)

    content = parse_statblock_page(PERRIN_FIXTURE_STATBLOCK, "fixture-perrin.md")
    assert content is not None

    import yaml

    from dndsim.rules.dnd5e_2014.statblock import extract_statblock_fence

    fence = extract_statblock_fence(PERRIN_FIXTURE_STATBLOCK)
    assert fence is not None
    block = yaml.safe_load(fence)

    compiled = compile_statblock(content, actions=[], sim_data=block.get("sim"))

    action_ids = {c.id for c in compiled.compiled_actions}
    # Eldritch Blast (bard/warlock cantrip, no slot cost) compiled as an attack.
    assert "eldritch-blast" in action_ids
    # Bard pool's Hideous Laughter (save) compiled independently of the
    # warlock pool's Hex/Armor of Agathys/Eldritch Blast — two pools never mix.
    ability_kinds = sorted(p.kind for p in compiled.ability_primitives)  # type: ignore[attr-defined]
    assert "extra_damage" in ability_kinds  # Hex
    assert "temp_hp" in ability_kinds  # Armor of Agathys
    assert "retaliate" in ability_kinds  # Armor of Agathys
    # Hideous Laughter's incapacitating rider survives compilation, and Armor
    # of Agathys's own sim.notes documents its un-scaled upcast.
    laughter = next(c for c in compiled.compiled_actions if c.id == "hideous-laughter")
    assert [e.effect for e in laughter.step.on_fail.effects] == [  # type: ignore[attr-defined]
        "incapacitated_prone"
    ]
    assert not any("no matching condition/rider tag" in w for w in compiled.warnings)
    assert any("upcast" in w for w in compiled.warnings)


# --- ADR-0009 boundary: no spell vocabulary outside the spell modules ------


def test_no_spell_vocabulary_in_simulator_or_policy_modules() -> None:
    """The simulator and any Policy must stay unaware spells exist as a
    content category (issue #48's acceptance criterion) — spells compile to
    ordinary Action/Modifier primitives before anything downstream runs."""
    rules_dir = Path(dndsim.rules.dnd5e_2014.__file__).parent
    ai_dir = Path(dndsim.__file__).parent / "ai"
    checked = [
        *sorted(ai_dir.rglob("*.py")),
        rules_dir / "combat.py",
        rules_dir / "mechanics.py",
        rules_dir / "primitives.py",
        rules_dir / "conditions.py",
        rules_dir / "reactions.py",
        rules_dir / "effects.py",
        rules_dir / "advantage.py",
        rules_dir / "encounter_timeline.py",
    ]
    for path in checked:
        if not path.is_file():
            continue
        text = path.read_text().lower()
        assert not re.search(r"\bspell\b", text), f"{path} names spell vocabulary"
