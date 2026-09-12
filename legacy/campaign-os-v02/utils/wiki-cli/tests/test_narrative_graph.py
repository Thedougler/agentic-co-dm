"""TDD for the narrative-model rules still live after ADR-0061 retired
moment/fork/sequence: W114 (operative-transclusion), W119
(grandfather-link), W132/W133 (beat contracts), W139 (situation contract).

Fixtures live under `tests/fixtures/narrative_graph/vault/` as a real,
interconnected mini beat/encounter web (`episodes/099/`) plus a
standalone containment chain for W119 (`locations/`), built through a real
`VaultIndex` — every case exercises actual corpus resolution, never a stub.
"""

from __future__ import annotations

from pathlib import Path

import wiki_cli.rules  # noqa: F401  import-for-side-effect: registers every rule
from wiki_cli.contracts import Severity, registry
from wiki_cli.index import VaultIndex
from wiki_cli.markdown import load_page

FIXTURES = Path(__file__).parent / "fixtures" / "narrative_graph"


def _corpus():
    return VaultIndex.build(FIXTURES, FIXTURES / "vault", ("vault",))


def check(rule_id, fixture):
    rule = registry()[rule_id]
    page = load_page(FIXTURES, fixture)
    return list(rule.check(page, _corpus()))


# --- W114: operative-transclusion -----------------------------------------


def test_w114_scene_missing_embeds_fires_once_per_missing_heading():
    findings = check("W114", "vault/episodes/099/scene-02-partial.md")

    assert [(f.rule_id, f.line) for f in findings] == [("W114", 10), ("W114", 10)]
    messages = "\n".join(f.message for f in findings)
    assert "§ Tactical Notes" in messages
    assert "§ Endings" in messages
    assert "![[test-boss-encounter#Tactical Notes]]" in messages


def test_w114_moment_embedding_every_operative_heading_stays_silent():
    # Also proves the `moment-<N>-<slug>.md` basename branch (not just `scene-`).
    assert check("W114", "vault/episodes/099/moment-1-covered.md") == []


def test_w114_encounter_page_itself_is_out_of_scope():
    assert check("W114", "vault/episodes/099/test-boss-encounter.md") == []


# --- W119: grandfather-link -------------------------------------------------


def test_w119_containment_row_linking_grandparent_fires_and_is_fixable():
    findings = check("W119", "vault/locations/gp-01-label-row.md")

    assert len(findings) == 1
    assert findings[0].fixable is True
    assert "is this page's grandparent, not its parent" in findings[0].message
    assert "[[gp-subregion|The Fixture Subregion]]" in findings[0].message


def test_w119_grandparent_named_in_prose_stays_silent():
    assert check("W119", "vault/locations/gp-02-prose.md") == []


def test_w119_address_row_linking_parent_alongside_ancestor_stays_silent():
    assert check("W119", "vault/locations/gp-03-address.md") == []


def test_w119_label_bullet_fires_with_no_fix():
    findings = check("W119", "vault/locations/gp-04-label-bullet.md")

    assert len(findings) == 1
    assert findings[0].fixable is False


def test_w119_containment_row_naming_real_parent_stays_silent():
    assert check("W119", "vault/locations/gp-05-clean.md") == []


# --- W132: beat-if-ignored ---------------------------------------------------


def test_w132_beat_with_if_ignored_stays_silent():
    assert check("W132", "vault/episodes/099/beat-clean.md") == []


def test_w132_beat_with_empty_if_ignored_fires():
    findings = check("W132", "vault/episodes/099/beat-no-if-ignored.md")

    assert len(findings) == 1
    assert "if_ignored" in findings[0].message
    assert findings[0].severity is Severity.ERROR


def test_w132_non_beat_page_stays_silent():
    assert check("W132", "vault/episodes/099/moment-with-engagement.md") == []


# --- W133: beat-narration-embed ----------------------------------------------


def test_w133_beat_with_narration_embed_stays_silent():
    assert check("W133", "vault/episodes/099/beat-clean.md") == []


def test_w133_beat_without_narration_embed_fires():
    findings = check("W133", "vault/episodes/099/beat-no-narration.md")

    assert len(findings) == 1
    assert "narration" in findings[0].message
    assert findings[0].severity is Severity.ERROR


def test_w133_non_beat_page_stays_silent():
    assert check("W133", "vault/episodes/099/moment-with-engagement.md") == []


# --- W139: situation-contract -----------------------------------------------


def test_w139_complete_situation_stays_silent():
    assert check(
        "W139", "vault/campaigns/shattered-sea/situations/active-pressure.md"
    ) == []


def _assert_w139_error(fixture: str, message_part: str) -> None:
    findings = check("W139", fixture)

    assert len(findings) == 1
    assert message_part in findings[0].message
    assert findings[0].severity is Severity.ERROR


def test_w139_missing_lifecycle_fires():
    _assert_w139_error(
        "vault/campaigns/shattered-sea/situations/no-lifecycle.md", "lifecycle"
    )


def test_w139_missing_pressure_fires():
    _assert_w139_error("vault/campaigns/shattered-sea/situations/no-pressure.md", "pressure")


def test_w139_missing_if_ignored_fires():
    _assert_w139_error(
        "vault/campaigns/shattered-sea/situations/no-if-ignored.md", "if_ignored"
    )


def test_w139_next_section_fires():
    _assert_w139_error("vault/campaigns/shattered-sea/situations/with-next.md", '"## Next"')


def test_w139_read_aloud_fires():
    _assert_w139_error(
        "vault/campaigns/shattered-sea/situations/with-read-aloud.md", "read-aloud"
    )


def test_w139_prescribed_player_action_warns():
    findings = check(
        "W139", "vault/campaigns/shattered-sea/situations/prescribed-player-action.md"
    )

    assert len(findings) == 1
    assert "Prescribed-player-action" in findings[0].message
    assert findings[0].severity is Severity.WARNING


def test_w139_non_situation_page_stays_silent():
    assert check("W139", "vault/episodes/099/moment-with-engagement.md") == []


def test_w139_missing_beat_chart_fires_all_eight_headings():
    findings = check(
        "W139", "vault/campaigns/shattered-sea/situations/no-beat-chart.md"
    )

    assert len(findings) == 8
    messages = "\n".join(f.message for f in findings)
    for heading in (
        "Dramatic Question",
        "Player Gravity",
        "Current State",
        "Active Beat",
        "Beat Spine",
        "Live Branches",
        "Climax Readiness",
        "Unused Possibilities",
    ):
        assert heading in messages, heading
    for finding in findings:
        assert finding.severity is Severity.ERROR


def test_w139_partial_beat_chart_fires_only_missing_heading():
    findings = check(
        "W139", "vault/campaigns/shattered-sea/situations/partial-beat-chart.md"
    )

    assert len(findings) == 1
    assert "Live Branches" in findings[0].message


def test_w119_descriptive_detail_cell_stays_silent():
    assert check("W119", "vault/locations/gp-06-detail-cell.md") == []


def test_w119_row_with_several_ancestor_links_fires_per_link_with_no_fix():
    findings = check("W119", "vault/locations/gp-07-multi-link-row.md")

    assert len(findings) == 2
    assert all(f.fixable is False for f in findings)


def test_w119_page_whose_parent_is_top_of_chain_has_no_grandparent():
    assert check("W119", "vault/locations/gp-region.md") == []


def test_w119_page_with_no_parent_field_stays_silent():
    assert check("W119", "vault/locations/gp-sea.md") == []


