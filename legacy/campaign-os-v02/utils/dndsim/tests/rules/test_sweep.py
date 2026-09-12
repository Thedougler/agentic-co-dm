"""Corpus and count sweeps (issue #53)."""

from __future__ import annotations

from pathlib import Path

import pytest

from dndsim import plugins
from dndsim.core.rng import cell_seed
from dndsim.core.universe import UniverseBatch
from dndsim.profile import ProfileError
from dndsim.rules.dnd5e_2014.attack_string import DamageGroup
from dndsim.rules.dnd5e_2014.combat import run_combat
from dndsim.rules.dnd5e_2014.compile import CompiledAbility, CompiledStatblock
from dndsim.rules.dnd5e_2014.primitives import AttackPrimitive, RoutineStepPrimitive
from dndsim.rules.dnd5e_2014.statblock import StatblockParseError
from dndsim.rules.dnd5e_2014.sweep import (
    SweepLoadError,
    combatant_spec_from_statblock,
    corpus_sweep,
    count_sweep,
    enumerate_corpus,
    load_combatant_spec,
)

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures"


@pytest.fixture(autouse=True)
def _load_rules_pack() -> None:
    plugins.load_rules_packs()
    plugins.load_policies()


def _attack(id_: str, to_hit: int, damage: list[DamageGroup]) -> AttackPrimitive:
    return AttackPrimitive(id=id_, to_hit=to_hit, damage=damage)


def _statblock_with_attack(
    *,
    name: str = "Fixture Foe",
    ac: int = 14,
    hp: int = 20,
    to_hit: int = 5,
    damage: list[DamageGroup] | None = None,
    routed: bool = True,
    legendary_actions_per_round: int = 0,
) -> CompiledStatblock:
    damage = damage or [DamageGroup(dice="1d8+3", type="slashing")]
    attack_id = "dnd5e_2014:primitive/attack/fixture-attack"
    ability = CompiledAbility(
        id=attack_id, name="Fixture Attack", step=_attack(attack_id, to_hit, damage)
    )
    routine = (RoutineStepPrimitive(ref=attack_id, count=1, alternatives=[]),) if routed else ()
    return CompiledStatblock(
        id=f"dnd5e_2014:statblock/{name.lower().replace(' ', '-')}",
        name=name,
        ac=ac,
        hp=hp,
        side="enemy",
        compiled_actions=(ability,),
        routine=routine,
        legendary_actions_per_round=legendary_actions_per_round,
    )


# --- combatant_spec_from_statblock -------------------------------------------


def test_combatant_spec_from_statblock_attaches_the_compiled_statblock() -> None:
    statblock = _statblock_with_attack(name="Fixture Foe", ac=15, hp=22, to_hit=6)
    spec = combatant_spec_from_statblock(statblock, suffix="/subject")
    assert spec.entity.id == f"{statblock.id}/subject"
    assert spec.entity.name == "Fixture Foe"
    assert spec.armor_class == 15
    assert spec.hp_max == 22
    # issue #60: run_combat executes the real compiled kit through this
    # field, not the legacy attack_bonus/damage_dice_* fallback below.
    assert spec.compiled is statblock
    assert spec.attack_bonus == 6
    assert spec.damage_dice_count == 1
    assert spec.damage_dice_sides == 8
    assert spec.damage_bonus == 3


def test_combatant_spec_from_statblock_falls_back_to_first_attack_action_with_no_routine() -> None:
    statblock = _statblock_with_attack(routed=False)
    spec = combatant_spec_from_statblock(statblock, suffix="/x")
    assert spec.attack_bonus == 5


def test_combatant_spec_from_statblock_raises_with_no_compiled_action() -> None:
    statblock = CompiledStatblock(
        id="dnd5e_2014:statblock/no-attack", name="No Attack", ac=10, hp=5, side="enemy"
    )
    with pytest.raises(SweepLoadError, match="no compiled action"):
        combatant_spec_from_statblock(statblock, suffix="/x")


def test_combatant_spec_from_statblock_suffix_disambiguates_self_matchup() -> None:
    statblock = _statblock_with_attack()
    subject = combatant_spec_from_statblock(statblock, suffix="/subject")
    opponent = combatant_spec_from_statblock(statblock, suffix="/opponent")
    assert subject.entity.id != opponent.entity.id


def test_combatant_spec_from_statblock_sets_legendary_true_for_a_legendary_creature() -> None:
    statblock = _statblock_with_attack(name="Legendary Thing", legendary_actions_per_round=1)
    spec = combatant_spec_from_statblock(statblock, suffix="")
    assert spec.legendary is True


def test_combatant_spec_from_statblock_sets_legendary_false_for_a_non_legendary_creature() -> None:
    statblock = _statblock_with_attack(name="Mundane Thing", legendary_actions_per_round=0)
    spec = combatant_spec_from_statblock(statblock, suffix="")
    assert spec.legendary is False


# --- loading real pages -------------------------------------------------------


def test_load_combatant_spec_against_a_real_fixture_page() -> None:
    spec = load_combatant_spec(FIXTURES_DIR / "dravosi-deckhand-statblock.md", suffix="/x")
    assert spec.entity.name == "Dravosi Deckhand"
    assert spec.hp_max == 11
    assert spec.armor_class == 13


def test_load_combatant_spec_raises_statblock_parse_error_on_broken_fence(tmp_path: Path) -> None:
    bad = tmp_path / "broken.md"
    bad.write_text("```statblock\nname: Broken\n```\n")  # missing required ac/hp/stats
    with pytest.raises(StatblockParseError):
        load_combatant_spec(bad, suffix="/x")


def test_load_combatant_spec_raises_profile_error_on_empty_fence(tmp_path: Path) -> None:
    stub = tmp_path / "stub.md"
    stub.write_text("# Stub page\n\nNo fence here.\n")
    with pytest.raises(ProfileError):
        load_combatant_spec(stub, suffix="/x")


# --- enumerate_corpus ---------------------------------------------------------


def test_enumerate_corpus_sorted_and_ignores_missing_dirs(tmp_path: Path) -> None:
    (tmp_path / "b.md").write_text("b")
    (tmp_path / "a.md").write_text("a")
    (tmp_path / "not-markdown.txt").write_text("x")
    result = enumerate_corpus([tmp_path / "does-not-exist", tmp_path])
    assert result == [tmp_path / "a.md", tmp_path / "b.md"]


# --- corpus_sweep --------------------------------------------------------------


def _write_corpus(tmp_path: Path) -> Path:
    corpus_dir = tmp_path / "corpus"
    corpus_dir.mkdir()
    (corpus_dir / "weak.md").write_text(
        "```statblock\nname: Weak Foe\nac: 10\nhp: 4\nstats: [8, 8, 8, 8, 8, 8]\n"
        "actions:\n  - name: Slap\n    desc: 'Melee Weapon Attack: +2 to hit, "
        "reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage.'\n```\n"
    )
    (corpus_dir / "strong.md").write_text(
        "```statblock\nname: Strong Foe\nac: 18\nhp: 60\nstats: [18, 12, 16, 8, 10, 8]\n"
        "actions:\n  - name: Maul\n    desc: 'Melee Weapon Attack: +8 to hit, "
        "reach 5 ft., one target. Hit: 14 (2d8+5) bludgeoning damage.'\n```\n"
    )
    (corpus_dir / "medium.md").write_text(
        "```statblock\nname: Medium Foe\nac: 13\nhp: 24\nstats: [14, 12, 14, 8, 10, 8]\n"
        "actions:\n  - name: Axe\n    desc: 'Melee Weapon Attack: +4 to hit, "
        "reach 5 ft., one target. Hit: 6 (1d8+2) slashing damage.'\n```\n"
    )
    (corpus_dir / "stub.md").write_text("# Index page\n\nNo statblock fence.\n")
    (corpus_dir / "broken.md").write_text("```statblock\nname: Broken\n```\n")
    return corpus_dir


def _write_subject(tmp_path: Path) -> Path:
    subject = tmp_path / "subject.md"
    subject.write_text(
        "```statblock\nname: Subject Fighter\nac: 16\nhp: 40\nstats: [16, 14, 14, 10, 10, 10]\n"
        "actions:\n  - name: Longsword\n    desc: 'Melee Weapon Attack: +6 to hit, "
        "reach 5 ft., one target. Hit: 8 (1d8+4) slashing damage.'\n```\n"
    )
    return subject


def test_corpus_sweep_skips_bad_pages_with_warnings(tmp_path: Path) -> None:
    corpus_dir = _write_corpus(tmp_path)
    subject = _write_subject(tmp_path)
    result = corpus_sweep(subject, corpus_dirs=[corpus_dir], seed=1, universes=200)
    assert result.corpus_count == 5
    assert result.cell_count == 3
    assert len(result.warnings) == 2
    assert any("stub.md" in w for w in result.warnings)
    assert any("broken.md" in w for w in result.warnings)
    opponents = {c.opponent for c in result.cells}
    assert opponents == {"Weak Foe", "Strong Foe", "Medium Foe"}
    # sorted ascending by the subject's own win rate
    assert result.cells[0].result.party_win_rate <= result.cells[-1].result.party_win_rate


def test_corpus_sweep_output_identical_across_worker_counts(tmp_path: Path) -> None:
    corpus_dir = _write_corpus(tmp_path)
    subject = _write_subject(tmp_path)
    results = {}
    for workers in (1, 4):
        r = corpus_sweep(
            subject, corpus_dirs=[corpus_dir], seed=7, universes=300, max_workers=workers
        )
        results[workers] = [(c.opponent, c.seed, c.result.party_win_rate) for c in r.cells]
    assert results[1] == results[4]


def test_corpus_sweep_cell_reproduces_in_isolation(tmp_path: Path) -> None:
    corpus_dir = _write_corpus(tmp_path)
    subject = _write_subject(tmp_path)
    result = corpus_sweep(subject, corpus_dirs=[corpus_dir], seed=11, universes=300)
    cell = result.cells[0]

    # Re-derive the same cell seed from the cell's own stable identity,
    # independent of the sweep's internals, and re-run it standalone.
    key = f"x:{result.subject}|opp:{cell.path}"
    assert cell_seed(11, key) == cell.seed

    subject_spec = load_combatant_spec(subject, suffix="/subject")
    opponent_spec = load_combatant_spec(Path(cell.path), suffix="/opponent")
    batch = UniverseBatch(size=300, seed=cell.seed)
    standalone = run_combat([subject_spec], [opponent_spec], batch, round_cap=20)
    assert standalone.party_win_rate == cell.result.party_win_rate


def test_corpus_sweep_raises_on_unloadable_subject(tmp_path: Path) -> None:
    corpus_dir = _write_corpus(tmp_path)
    bad_subject = tmp_path / "bad-subject.md"
    bad_subject.write_text("# no fence\n")
    with pytest.raises(ProfileError):
        corpus_sweep(bad_subject, corpus_dirs=[corpus_dir], seed=1, universes=100)


# --- count_sweep ---------------------------------------------------------------


def test_count_sweep_validates_range() -> None:
    subject = FIXTURES_DIR / "dravosi-deckhand-statblock.md"
    with pytest.raises(ValueError, match="min_count"):
        count_sweep([subject], subject, seed=1, universes=100, min_count=0)
    with pytest.raises(ValueError, match="max_count"):
        count_sweep([subject], subject, seed=1, universes=100, min_count=5, max_count=2)


def test_count_sweep_recommended_counts_use_smallest_reaching_band(tmp_path: Path) -> None:
    corpus_dir = _write_corpus(tmp_path)
    party = _write_subject(tmp_path)
    weak_monster = corpus_dir / "weak.md"
    result = count_sweep([party], weak_monster, seed=3, universes=300, min_count=1, max_count=4)
    assert result.monster == "Weak Foe"
    assert len(result.cells) >= 4
    seen_counts = [c.count for c in result.cells]
    assert seen_counts == sorted(seen_counts)
    # Every band recorded actually is the smallest count reaching it.
    for band, count in result.recommended_count_by_band.items():
        if count is None:
            continue
        matching = [c for c in result.cells if c.count == count and c.rating.band == band]
        assert matching, f"band {band} recommended count {count} not found among cells"


def test_count_sweep_extends_past_max_count_until_break_even(tmp_path: Path) -> None:
    corpus_dir = _write_corpus(tmp_path)
    party = _write_subject(tmp_path)
    medium_monster = corpus_dir / "medium.md"
    result = count_sweep([party], medium_monster, seed=5, universes=500, min_count=1, max_count=1)
    # A lone Medium Foe is a near-certain win for the fighter — the sweep
    # must keep adding counts past max_count=1 until win rate drops below
    # 50% (or the hard ceiling), never silently stopping at 1.
    assert len(result.cells) > 1
    counts = [c.count for c in result.cells]
    assert counts == list(range(1, counts[-1] + 1))
    assert result.cells[0].result.party_win_rate >= 0.5
    assert result.cells[-1].result.party_win_rate < 0.5


def test_count_sweep_output_identical_across_worker_counts(tmp_path: Path) -> None:
    corpus_dir = _write_corpus(tmp_path)
    party = _write_subject(tmp_path)
    monster = corpus_dir / "weak.md"
    results = {}
    for workers in (1, 4):
        r = count_sweep(
            [party], monster, seed=9, universes=300, min_count=1, max_count=4, max_workers=workers
        )
        results[workers] = [(c.count, c.seed, c.result.party_win_rate) for c in r.cells]
    assert results[1] == results[4]
