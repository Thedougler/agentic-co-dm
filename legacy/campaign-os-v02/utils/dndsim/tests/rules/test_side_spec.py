"""Side-spec grammar for `dndsim sim-combat <X> <Y>` (issue #67)."""

from __future__ import annotations

from pathlib import Path

import pytest

from dndsim import plugins
from dndsim.rules.dnd5e_2014.side_spec import (
    SideSpecError,
    resolve_combatant_arg,
    resolve_side,
)

_FIXTURE_STATBLOCK = (
    "```statblock\nname: {name}\nac: 12\nhp: 10\nstats: [10, 10, 10, 10, 10, 10]\n"
    "actions:\n  - name: Slap\n    desc: 'Melee Weapon Attack: +2 to hit, "
    "reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage.'\n```\n"
)


@pytest.fixture(autouse=True)
def _load_rules_pack() -> None:
    plugins.load_rules_packs()
    plugins.load_policies()


def _write(dir_: Path, filename: str, *, name: str | None = None, alias: str | None = None) -> Path:
    path = dir_ / filename
    body = _FIXTURE_STATBLOCK.format(name=name or filename)
    if alias is not None:
        body = f"---\nalias: {alias}\n---\n\n{body}"
    path.write_text(body)
    return path


# --- resolve_combatant_arg (port of load.mjs's resolveCombatantArg) ----------


def test_resolve_combatant_arg_literal_path_used_as_is(tmp_path: Path) -> None:
    path = _write(tmp_path, "grung.md", name="Grung")
    assert resolve_combatant_arg(str(path), [tmp_path]) == path


def test_resolve_combatant_arg_matches_stripped_sheet_suffix(tmp_path: Path) -> None:
    path = _write(tmp_path, "perrin-sheet.md", name="Perrin")
    assert resolve_combatant_arg("perrin", [tmp_path]) == path


def test_resolve_combatant_arg_matches_stripped_statblock_suffix(tmp_path: Path) -> None:
    path = _write(tmp_path, "grung-elite-statblock.md", name="Grung Elite")
    assert resolve_combatant_arg("grung-elite", [tmp_path]) == path


def test_resolve_combatant_arg_matches_bare_basename(tmp_path: Path) -> None:
    path = _write(tmp_path, "otar.md", name="Otar")
    assert resolve_combatant_arg("otar", [tmp_path]) == path


def test_resolve_combatant_arg_matches_frontmatter_alias(tmp_path: Path) -> None:
    path = _write(tmp_path, "the-foul.md", name="Otar the Foul", alias="otar")
    assert resolve_combatant_arg("otar", [tmp_path]) == path


def test_resolve_combatant_arg_no_match_names_search_dirs(tmp_path: Path) -> None:
    with pytest.raises(SideSpecError, match=str(tmp_path)):
        resolve_combatant_arg("nobody", [tmp_path])


def test_resolve_combatant_arg_ambiguous_match_names_every_candidate(tmp_path: Path) -> None:
    a = _write(tmp_path, "grung.md", name="Grung A")
    b = _write(tmp_path, "grung-statblock.md", name="Grung B")
    with pytest.raises(SideSpecError) as excinfo:
        resolve_combatant_arg("grung", [tmp_path])
    message = str(excinfo.value)
    assert "matches multiple files" in message
    assert str(a) in message
    assert str(b) in message


def test_resolve_combatant_arg_never_fuzzy_matches(tmp_path: Path) -> None:
    _write(tmp_path, "grung-skirmisher.md", name="Grung Skirmisher")
    with pytest.raises(SideSpecError):
        resolve_combatant_arg("grung", [tmp_path])


def test_resolve_combatant_arg_case_sensitive(tmp_path: Path) -> None:
    _write(tmp_path, "grung.md", name="Grung")
    with pytest.raises(SideSpecError):
        resolve_combatant_arg("Grung", [tmp_path])


# --- resolve_side (port of runner.mjs's resolveSide) --------------------------


def test_resolve_side_bare_slug(tmp_path: Path) -> None:
    _write(tmp_path, "grung.md", name="Grung")
    side = resolve_side("grung", role="enemy", candidate_dirs=[tmp_path])
    assert [c.entity.name for c in side.combatants] == ["Grung"]


def test_resolve_side_literal_path(tmp_path: Path) -> None:
    path = _write(tmp_path, "grung.md", name="Grung")
    side = resolve_side(str(path), role="enemy", candidate_dirs=[tmp_path])
    assert [c.entity.name for c in side.combatants] == ["Grung"]


def test_resolve_side_count_suffix_repeats_and_disambiguates_ids(tmp_path: Path) -> None:
    _write(tmp_path, "grung.md", name="Grung")
    side = resolve_side("grung:3", role="enemy", candidate_dirs=[tmp_path])
    assert [c.entity.name for c in side.combatants] == ["Grung", "Grung", "Grung"]
    ids = [c.entity.id for c in side.combatants]
    assert len(set(ids)) == 3  # run_combat keys per-combatant state by entity.id


def test_resolve_side_comma_list_builds_heterogeneous_roster(tmp_path: Path) -> None:
    _write(tmp_path, "grung.md", name="Grung")
    _write(tmp_path, "otar.md", name="Otar")
    side = resolve_side("grung,otar:2", role="enemy", candidate_dirs=[tmp_path])
    assert [c.entity.name for c in side.combatants] == ["Grung", "Otar", "Otar"]


def test_resolve_side_party_keyword_expands_glob_sorted(tmp_path: Path) -> None:
    party_dir = tmp_path / "party"
    party_dir.mkdir()
    _write(party_dir, "b-sheet.md", name="Bravo")
    _write(party_dir, "a-sheet.md", name="Alpha")
    side = resolve_side("party", role="party", party_glob=str(party_dir / "*-sheet.md"))
    assert [c.entity.name for c in side.combatants] == ["Alpha", "Bravo"]


def test_resolve_side_party_keyword_no_match_is_an_error(tmp_path: Path) -> None:
    with pytest.raises(SideSpecError, match="matched no files"):
        resolve_side("party", role="party", party_glob=str(tmp_path / "nothing-*.md"))


def test_resolve_side_empty_spec_is_an_error() -> None:
    with pytest.raises(SideSpecError, match="empty combatant spec"):
        resolve_side("  ,  ", role="enemy", candidate_dirs=[])


def test_resolve_side_zero_count_is_an_error(tmp_path: Path) -> None:
    _write(tmp_path, "grung.md", name="Grung")
    with pytest.raises(SideSpecError, match="count must be >= 1"):
        resolve_side("grung:0", role="enemy", candidate_dirs=[tmp_path])


def test_resolve_side_ambiguous_token_names_candidates(tmp_path: Path) -> None:
    _write(tmp_path, "grung.md", name="Grung A")
    _write(tmp_path, "grung-statblock.md", name="Grung B")
    with pytest.raises(SideSpecError, match="matches multiple files"):
        resolve_side("grung", role="enemy", candidate_dirs=[tmp_path])


def test_resolve_side_unresolvable_token_is_an_error(tmp_path: Path) -> None:
    with pytest.raises(SideSpecError, match="no file matching"):
        resolve_side("nobody", role="enemy", candidate_dirs=[tmp_path])


def test_resolve_side_non_digit_after_colon_is_treated_as_part_of_the_ref(tmp_path: Path) -> None:
    # ":latest" isn't a base-10 count (the reference's /^\d+$/ test), so the
    # whole token is the ref — and no file named "grung:latest" exists.
    _write(tmp_path, "grung.md", name="Grung")
    with pytest.raises(SideSpecError, match="no file matching"):
        resolve_side("grung:latest", role="enemy", candidate_dirs=[tmp_path])
