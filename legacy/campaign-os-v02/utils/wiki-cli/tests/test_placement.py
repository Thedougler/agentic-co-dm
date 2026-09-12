"""TDD for the `placement-conformance` cluster (ADR-0042 Task 14): W5
(required-headings), W55 (template-spine-consistency), W95 (type-folder-
placement), W97 (subtype-folder-partition), W100 (core-page-aliases), W125
(monster-found-at) — plus the shared `wiki_cli.templates` reader.

W5 and W55 resolve templates against the REAL `vault/_templates/` tree
(same convention as `test_frontmatter_schema.py`'s own `FrontmatterSchemaRule`
tests) — the only way to prove either rule matches what a real template
declares today, not a stub the test invents. `templates.py`'s own reader
functions are additionally covered directly against a mini `_templates/`
fixture tree, independent of any rule. W95/W97/W100/W125 build a small
fixture vault under `tests/fixtures/placement/vault/` and a `VaultIndex`
over it, per this port wave's shared exemplar.
"""

from __future__ import annotations

from pathlib import Path

import wiki_cli.rules  # noqa: F401  side-effect: registers every rule
from wiki_cli import templates
from wiki_cli.config import load_config
from wiki_cli.contracts import Finding, Page, Severity, registry
from wiki_cli.index import VaultIndex
from wiki_cli.markdown import load_page

FIXTURES = Path(__file__).parent / "fixtures" / "placement"


def _corpus() -> VaultIndex:
    return VaultIndex.build(FIXTURES, FIXTURES / "vault", ("vault",))


def check(rule_id: str, fixture: str) -> list[Finding]:
    rule = registry()[rule_id]
    page = load_page(FIXTURES, fixture)
    return list(rule.check(page, _corpus()))


def _page(rel_path: str, frontmatter: dict[str, object], body: str) -> Page:
    return Page(
        rel_path=rel_path,
        raw="",
        frontmatter=frontmatter,
        body=body,
        body_start_line=len(frontmatter) + 2,
    )


# --- templates.py — the shared reader, tested directly -----------------

_MINI_TEMPLATES_ROOT = FIXTURES / "_templates"


def test_resolve_template_bare_type_excludes_optional_heading() -> None:
    entry = templates.resolve_template(_MINI_TEMPLATES_ROOT, "widget", None)
    assert entry is not None
    assert entry.required_headings == ("Alpha", "Beta")


def test_resolve_template_subtype_prefers_exact_stem() -> None:
    entry = templates.resolve_template(_MINI_TEMPLATES_ROOT, "widget", "gizmo")
    assert entry is not None
    assert entry.required_headings == ("Alpha", "Delta")


def test_resolve_template_unknown_type_returns_none() -> None:
    assert templates.resolve_template(_MINI_TEMPLATES_ROOT, "no-such-type", None) is None


def test_default_spine_reads_ordered_top_level_keys() -> None:
    spine = templates.default_spine(_MINI_TEMPLATES_ROOT)
    assert spine is not None
    assert spine.spine_keys == (
        "type",
        "status",
        "publish",
        "title",
        "aliases",
        "summary",
        "created",
        "updated",
        "tags",
        "tier",
        "owner_skill",
    )


def test_default_spine_missing_file_returns_none(tmp_path: Path) -> None:
    assert templates.default_spine(tmp_path / "_templates") is None


# --- W5: required-headings ----------------------------------------------
# Against the REAL `vault/_templates/_srd/_class.md`, whose "Core <Class>
# Traits" / "<Class> Class Features" required headings carry the
# `<Placeholder>` wildcard — porting w5-required-headings.test.mjs's own
# hard-won cases (a real, wildcarded template caught a false positive a
# fixture never would).


def test_w5_wildcarded_headings_match_a_concrete_instance() -> None:
    page = _page(
        "vault/srd/classes/test-fixture.md",
        {"type": "class"},
        "# Title\n\n"
        "## Core Wizard Traits\n\ntext\n\n"
        "## Becoming a Wizard\n\ntext\n\n"
        "## Wizard Class Features\n\ntext\n\n"
        "## Wizard Subclass: Evoker\n\ntext\n",
    )
    rule = registry()["W5"]
    assert list(rule.check(page, corpus=None)) == []


def test_w5_missing_wildcarded_heading_flagged_by_placeholder_text() -> None:
    page = _page(
        "vault/srd/classes/test-fixture.md",
        {"type": "class"},
        "# Title\n\n## Core Wizard Traits\n\ntext\n",
    )
    rule = registry()["W5"]
    findings = list(rule.check(page, corpus=None))
    assert len(findings) == 1
    assert findings[0].rule_id == "W5"
    assert 'Missing required heading "## <Class> Class Features"' in findings[0].message


def test_w5_out_of_order_headings_flagged_by_real_text() -> None:
    page = _page(
        "vault/srd/classes/test-fixture.md",
        {"type": "class"},
        "# Title\n\n## Wizard Class Features\n\ntext\n\n## Core Wizard Traits\n\ntext\n",
    )
    rule = registry()["W5"]
    findings = list(rule.check(page, corpus=None))
    assert len(findings) == 1
    assert 'Heading "## Wizard Class Features" is out of order' in findings[0].message
    assert "expected order: Core <Class> Traits -> <Class> Class Features" in findings[0].message


def test_w5_played_episode_skips_new_moment_spine() -> None:
    page = _page(
        "vault/episodes/008/moment-01-the-table.md",
        {"type": "moment"},
        "# Title\n\n## What's True\n\ntext\n\n## Next\n\ntext\n\n## Connections\n\ntext\n",
    )
    assert list(registry()["W5"].check(page, corpus=None)) == []


def test_w5_session_010_beat_requires_handoff() -> None:
    page = _page(
        "vault/episodes/010/beat-01-open.md",
        {"type": "beat"},
        "# Title\n\n## Situation\n\ntext\n\n## Player Gravity\n\ntext\n",
    )
    findings = list(registry()["W5"].check(page, corpus=None))
    assert any("Handoff" in finding.message for finding in findings)


def test_w5_bare_type_missing_required_heading() -> None:
    # Real `_campaigns/_threat.md`: required = Nature, Clock.
    page = _page(
        "vault/campaigns/shattered-sea/threats/test-fixture.md",
        {"type": "threat"},
        "# Title\n\n## Nature\n\ntext\n",
    )
    rule = registry()["W5"]
    findings = list(rule.check(page, corpus=None))
    assert len(findings) == 1
    assert 'Missing required heading "## Clock"' in findings[0].message


def test_w5_bare_type_reordered_headings() -> None:
    page = _page(
        "vault/campaigns/shattered-sea/threats/test-fixture.md",
        {"type": "threat"},
        "# Title\n\n## Clock\n\ntext\n\n## Nature\n\ntext\n",
    )
    rule = registry()["W5"]
    findings = list(rule.check(page, corpus=None))
    assert len(findings) == 1
    assert "is out of order" in findings[0].message


def test_w5_bare_type_conforming_stays_clean() -> None:
    page = _page(
        "vault/campaigns/shattered-sea/threats/test-fixture.md",
        {"type": "threat"},
        "# Title\n\n## Nature\n\ntext\n\n## Clock\n\ntext\n",
    )
    rule = registry()["W5"]
    assert list(rule.check(page, corpus=None)) == []


def test_w5_exempt_path_stays_silent_even_with_missing_heading() -> None:
    page = _page(
        "vault/stories/session-01-test.md",
        {"type": "location"},
        "# Title\n\n## Hooks\n\ntext\n",
    )
    rule = registry()["W5"]
    assert list(rule.check(page, corpus=None)) == []


# --- W55: template-spine-consistency ------------------------------------
# Detection tested directly (bare `_templates/...` rel_path — the port's
# own bug-compatible file-scope gate, see the rule module's LEGACY-BUG
# note); the gate itself is proven separately below against a
# real-shaped `vault/_templates/...` path.

_REQUIRED_SPINE_ORDER = (
    "type",
    "status",
    "publish",
    "aliases",
    "created",
    "updated",
    "tags",
    "phase",
    "source",
    "source_url",
    "owner_skill",
    "uid",
)


def _conforming_spine_frontmatter() -> dict[str, object]:
    return {
        key: (False if key == "publish" else "draft" if key == "status" else "")
        for key in _REQUIRED_SPINE_ORDER
    }


def test_w55_conforming_spine_stays_clean() -> None:
    page = _page("_templates/_widget.md", _conforming_spine_frontmatter(), "# <Name>\n")
    rule = registry()["W55"]
    assert list(rule.check(page, corpus=None)) == []


def test_w55_missing_spine_key_fires() -> None:
    frontmatter = _conforming_spine_frontmatter()
    del frontmatter["uid"]
    page = _page("_templates/_widget.md", frontmatter, "# <Name>\n")
    rule = registry()["W55"]
    findings = list(rule.check(page, corpus=None))
    assert any('missing spine key "uid"' in f.message for f in findings)


def test_w55_out_of_order_key_fires() -> None:
    frontmatter = _conforming_spine_frontmatter()
    aliases = frontmatter.pop("aliases")
    frontmatter["aliases"] = aliases  # re-inserted at the end -> out of order
    page = _page("_templates/_widget.md", frontmatter, "# <Name>\n")
    rule = registry()["W55"]
    findings = list(rule.check(page, corpus=None))
    assert any("is out of order" in f.message for f in findings)


def test_w55_publish_not_false_fires() -> None:
    frontmatter = _conforming_spine_frontmatter()
    frontmatter["publish"] = True
    page = _page("_templates/_widget.md", frontmatter, "# <Name>\n")
    rule = registry()["W55"]
    findings = list(rule.check(page, corpus=None))
    assert any("publish: false" in f.message for f in findings)


def test_w55_invalid_status_enum_fires() -> None:
    frontmatter = _conforming_spine_frontmatter()
    frontmatter["status"] = "not-a-real-status"
    page = _page("_templates/_widget.md", frontmatter, "# <Name>\n")
    rule = registry()["W55"]
    findings = list(rule.check(page, corpus=None))
    assert any("STATUS_ENUM" in f.message for f in findings)


def test_w55_no_status_key_stays_silent() -> None:
    page = _page("_templates/_widget.md", {"type": "widget"}, "# <Name>\n")
    rule = registry()["W55"]
    assert list(rule.check(page, corpus=None)) == []


def test_w55_real_shaped_template_path_never_fires() -> None:
    """LEGACY-BUG gate: npm's `.obsidian-linter.jsonc` unconditionally
    ignores `vault/_templates/**`, even via an explicit file argument
    (confirmed empirically) — so a real repo-root-relative template path
    must stay silent regardless of how drifted its spine is."""
    frontmatter = _conforming_spine_frontmatter()
    del frontmatter["uid"]  # would otherwise fire
    page = _page("vault/_templates/_widget.md", frontmatter, "# <Name>\n")
    rule = registry()["W55"]
    assert list(rule.check(page, corpus=None)) == []


# --- W95: type-folder-placement -----------------------------------------


def test_w95_page_outside_its_mapped_home_fires() -> None:
    findings = check("W95", "vault/stray-monster.md")
    assert len(findings) == 1
    assert findings[0].rule_id == "W95"
    assert "move this page under vault/srd/monsters/" in findings[0].message


def test_w95_page_inside_its_mapped_home_stays_silent() -> None:
    assert check("W95", "vault/srd/monsters/homed-monster.md") == []


def test_w95_situation_outside_its_mapped_home_fires() -> None:
    findings = check("W95", "vault/stray-situation.md")
    assert len(findings) == 1
    assert findings[0].rule_id == "W95"
    assert "move this page under vault/campaigns/shattered-sea/situations/" in findings[0].message


def test_w95_situation_inside_its_mapped_home_stays_silent() -> None:
    assert check("W95", "vault/campaigns/shattered-sea/situations/homed-situation.md") == []


def test_w95_situation_inside_campaign_but_outside_home_fires() -> None:
    findings = check("W95", "vault/campaigns/shattered-sea/quests/wrong-situation.md")
    assert len(findings) == 1
    assert findings[0].rule_id == "W95"
    assert "move this page under vault/campaigns/shattered-sea/situations/" in findings[0].message


# --- W97: subtype-folder-partition (VaultRule) --------------------------


def _w97_findings() -> list[Finding]:
    rule = registry()["W97"]
    return list(rule.check(_corpus()))


def test_w97_outlier_in_consensus_directory_fires() -> None:
    findings = [
        f
        for f in _w97_findings()
        if f.file == "vault/campaigns/shattered-sea/npcs/recurring/drifted-page.md"
    ]
    assert len(findings) == 1
    assert "carries subtype: recurring" in findings[0].message


def test_w97_conforming_sibling_stays_silent() -> None:
    findings = [
        f
        for f in _w97_findings()
        if f.file == "vault/campaigns/shattered-sea/npcs/recurring/page-01.md"
    ]
    assert findings == []


def test_w97_directory_below_min_pages_stays_silent() -> None:
    findings = [
        f for f in _w97_findings() if f.file.startswith("vault/campaigns/shattered-sea/npcs/mixed/")
    ]
    assert findings == []


# --- W100: core-page-aliases ---------------------------------------------


def test_w100_core_page_with_no_aliases_fires() -> None:
    findings = check("W100", "vault/core-no-aliases.md")
    assert len(findings) == 1
    assert findings[0].rule_id == "W100"
    assert "tier: core with no aliases" in findings[0].message


def test_w100_core_page_with_aliases_stays_silent() -> None:
    assert check("W100", "vault/core-with-aliases.md") == []


def test_w100_ship_tier_core_is_exempt() -> None:
    assert check("W100", "vault/core-ship.md") == []


# --- W125: monster-found-at ----------------------------------------------


def test_w125_two_resolving_locations_stays_silent() -> None:
    assert check("W125", "vault/srd/monsters/found-at-clean.md") == []


def test_w125_absent_found_at_stays_silent() -> None:
    assert check("W125", "vault/srd/monsters/found-at-absent.md") == []


def test_w125_non_monster_page_stays_silent() -> None:
    assert check("W125", "vault/routes/found-at-non-monster.md") == []


def test_w125_too_few_entries_fires_count_finding() -> None:
    findings = check("W125", "vault/srd/monsters/found-at-too-few.md")
    assert len(findings) == 1
    assert "names 1 location(s)" in findings[0].message


def test_w125_entry_naming_an_unwritten_page_warns() -> None:
    findings = check("W125", "vault/srd/monsters/found-at-dead-link.md")
    assert len(findings) == 1
    assert "does not exist yet" in findings[0].message
    assert findings[0].severity is Severity.WARNING


def test_w125_route_target_is_legal() -> None:
    findings = check("W125", "vault/srd/monsters/found-at-route.md")
    assert findings == []


def test_w125_wrong_type_entry_fires() -> None:
    findings = check("W125", "vault/srd/monsters/found-at-wrong-type.md")
    assert len(findings) == 1
    assert "type: npc page, not a location or route" in findings[0].message
    assert findings[0].severity is Severity.ERROR


def test_w125_threshold_reads_from_wiki_toml() -> None:
    assert load_config().threshold("MONSTER_FOUND_AT_MIN") == "2"
