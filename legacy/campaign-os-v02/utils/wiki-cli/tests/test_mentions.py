"""W25, W122, W77, W62 — corpus-aware "mentions and atomicity" rules ported
from the legacy JS lint engine's `utils/scripts/lint-rules/w*.mjs` modules.
See each rule module's docstring for the ported spec."""

from __future__ import annotations

from pathlib import Path

import wiki_cli.rules  # noqa: F401  import-for-side-effect: registers every rule
from wiki_cli.contracts import registry
from wiki_cli.index import VaultIndex
from wiki_cli.markdown import load_page

FIXTURES = Path(__file__).parent / "fixtures" / "mentions"


def _corpus() -> VaultIndex:
    return VaultIndex.build(FIXTURES, FIXTURES / "vault", ("vault",))


def check(rule_id: str, fixture: str):
    rule = registry()[rule_id]
    page = load_page(FIXTURES, fixture)
    return list(rule.check(page, _corpus()))


# ---- W25 — unlinked-mention ----


def test_w25_flags_unlinked_mention():
    findings = check("W25", "vault/scenes/mentions-unlinked.md")
    assert [(f.rule_id, f.line) for f in findings] == [("W25", 8)]
    assert "Barnaby Rook" in findings[0].message
    assert "vault/npcs/barnaby-rook.md" in findings[0].message


def test_w25_clean_when_already_linked():
    assert check("W25", "vault/scenes/mentions-linked.md") == []


def test_w25_clean_when_section_linked():
    assert check("W25", "vault/scenes/mentions-section-linked.md") == []


def test_w25_clean_on_stoplisted_name():
    # "ghost" is a real UNLINKED_MENTION_STOPLIST entry (wiki.toml) — the
    # candidate name is excluded from the scan index entirely, so an
    # unlinked, capitalized mention of it never fires.
    assert check("W25", "vault/scenes/mentions-stoplisted.md") == []


def test_w25_out_of_scope_on_a_story_page():
    # vault/stories/ is W25's own exclusion — W122 covers that scope instead.
    assert check("W25", "vault/stories/mentions-story.md") == []


# ---- W122 — narrative-unlinked-mention ----


def test_w122_flags_unlinked_mention_in_a_story():
    findings = check("W122", "vault/stories/mentions-story.md")
    assert [(f.rule_id, f.line) for f in findings] == [("W122", 8)]
    assert findings[0].severity.value == "warning"


def test_w122_out_of_scope_outside_stories_and_ideas():
    assert check("W122", "vault/scenes/mentions-unlinked.md") == []


def test_w122_out_of_scope_on_a_nested_skill_doc():
    # A .claude/skills/ subtree under vault/stories/ is agent-facing
    # instruction prose, not narrative content — no wikilink duty.
    assert check("W122", "vault/stories/.claude/skills/draft-story/SKILL.md") == []


def test_w122_idea_page_wikilink_resolves_to_landed_page_of_same_slug():
    # vault/campaigns/shattered-sea/npcs/sir-quackers-the-fowl.md (landed,
    # aliased "Quackers") and vault/ideas/sir-quackers-the-fowl.md (its
    # pre-canon sketch) share the exact slug "sir-quackers-the-fowl", and
    # "campaigns" sorts before "ideas" — corpus.pages() visits the idea page
    # last. The idea page's own [[sir-quackers-the-fowl|Quackers]] wikilink
    # must resolve through raw_index to the landed npc page, not to itself,
    # so the later bare "Quackers" mention is recognized as already linked.
    assert check("W122", "vault/ideas/sir-quackers-the-fowl.md") == []


def test_w25_two_landed_pages_share_an_alias_last_write_wins_unaffected():
    # vault/npcs/collision-alpha.md and vault/scenes/collision-beta.md both
    # alias "Twin Marker" — neither is a vault/ideas/ page, so the idea
    # carve-out in raw_index must not touch this case: legacy's
    # last-write-wins-in-path-order behavior (whichever sorts later,
    # collision-beta) still applies unchanged.
    findings = check("W25", "vault/scenes/mentions-collision.md")
    assert [(f.rule_id, f.line) for f in findings] == [("W25", 8)]
    assert "vault/scenes/collision-beta.md" in findings[0].message


# ---- W77 — inline-entity-description ----


def test_w77_flags_inline_npc_bio_on_a_ship_page():
    findings = check("W77", "vault/ships/inline-bio.md")
    assert [(f.rule_id, f.line) for f in findings] == [("W77", 10)]
    assert "Corven Ashgrave" in findings[0].message
    assert "no page exists for it anywhere in the vault" in findings[0].message


def test_w77_clean_on_pc_authored_pages():
    assert check("W77", "vault/campaigns/shattered-sea/pcs/inline-bio-pc.md") == []


def test_w77_clean_on_refs_reference_material():
    assert check("W77", "vault/refs/inline-bio-refs.md") == []


def test_w77_clean_on_srd_status_pages():
    assert check("W77", "vault/ships/inline-bio-srd.md") == []


# ---- W62 — inline-statblock-drift ----


def test_w62_flags_stat_block_restated_in_a_parenthetical():
    findings = check("W62", "vault/scenes/statblock-drift.md")
    assert [(f.rule_id, f.line) for f in findings] == [("W62", 8)]
    assert "vault/npcs/vashu.md" in findings[0].message


def test_w62_clean_on_a_bare_link():
    assert check("W62", "vault/scenes/statblock-clean.md") == []
