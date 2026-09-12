"""TDD for typed frontmatter edge ingestion (issue 04) and the two anchor
lint rules derived from the typed graph.

All tests use `tmp_path` for isolation — no shared fixture directory,
so the cache never carries state between runs.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import wiki_cli.rules  # noqa: F401  side-effect: registers every rule
from wiki_cli.contracts import registry
from wiki_cli.index import VaultIndex


def _setup(root: Path, pages: dict[str, str]) -> None:
    vault = root / "vault"
    vault.mkdir(parents=True, exist_ok=True)
    for name, content in pages.items():
        target = vault / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
    (root / "wiki.toml").write_text("", encoding="utf-8")


def _conn(root: Path) -> sqlite3.Connection:
    return sqlite3.connect(str(root / ".wiki-cli" / "cache.sqlite3"))


# ---------------------------------------------------------------------------
# Typed edge ingestion
# ---------------------------------------------------------------------------


def test_location_frontmatter_produces_located_at_edge(tmp_path: Path) -> None:
    _setup(
        tmp_path,
        {
            "port-city.md": "---\ntype: location\n---\nPort City body.\n",
            "hero.md": "---\ntype: npc\nlocation: \"[[Port City]]\"\n---\nHero body.\n",
        },
    )
    VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",))

    rows = _conn(tmp_path).execute(
        "SELECT raw_target, section, link_type FROM links WHERE source = 'vault/hero.md'"
    ).fetchall()
    typed = [(r[1], r[2]) for r in rows]
    assert ("location", "LOCATED_AT") in typed


def test_within_frontmatter_produces_contains_edge(tmp_path: Path) -> None:
    _setup(
        tmp_path,
        {
            "tavern.md": "---\ntype: location\n---\nTavern body.\n",
            "item.md": "---\ntype: item\nwithin: \"[[Tavern]]\"\n---\nItem body.\n",
        },
    )
    VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",))

    rows = _conn(tmp_path).execute(
        "SELECT raw_target, section, link_type FROM links WHERE source = 'vault/item.md'"
    ).fetchall()
    typed = [(r[1], r[2]) for r in rows]
    assert ("within", "CONTAINS") in typed


def test_factions_list_produces_multiple_member_of_edges(tmp_path: Path) -> None:
    _setup(
        tmp_path,
        {
            "ravens.md": "---\ntype: faction\n---\nRavens.\n",
            "guild.md": "---\ntype: faction\n---\nGuild.\n",
            "npc.md": "---\ntype: npc\nfactions:\n  - \"[[Ravens]]\"\n  - \"[[Guild]]\"\n---\nNPC body.\n",
        },
    )
    VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",))

    rows = _conn(tmp_path).execute(
        "SELECT raw_target, section, link_type FROM links "
        "WHERE source = 'vault/npc.md' AND link_type = 'MEMBER_OF'"
    ).fetchall()
    assert len(rows) == 2


def test_owner_frontmatter_produces_owned_by_edge(tmp_path: Path) -> None:
    _setup(
        tmp_path,
        {
            "owner-npc.md": "---\ntype: npc\n---\nOwner body.\n",
            "artifact.md": "---\ntype: item\nowner: \"[[Owner NPC]]\"\n---\nArtifact body.\n",
        },
    )
    VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",))

    rows = _conn(tmp_path).execute(
        "SELECT raw_target, section, link_type FROM links WHERE source = 'vault/artifact.md'"
    ).fetchall()
    typed = [(r[1], r[2]) for r in rows]
    assert ("owner", "OWNED_BY") in typed


def test_origin_frontmatter_produces_originates_from_edge(tmp_path: Path) -> None:
    _setup(
        tmp_path,
        {
            "homeland.md": "---\ntype: location\n---\nHomeland.\n",
            "wanderer.md": "---\ntype: npc\norigin: \"[[Homeland]]\"\n---\nWanderer.\n",
        },
    )
    VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",))

    rows = _conn(tmp_path).execute(
        "SELECT raw_target, section, link_type FROM links WHERE source = 'vault/wanderer.md'"
    ).fetchall()
    typed = [(r[1], r[2]) for r in rows]
    assert ("origin", "ORIGINATES_FROM") in typed


def test_episode_frontmatter_produces_canon_in_edge(tmp_path: Path) -> None:
    _setup(
        tmp_path,
        {
            "session-01.md": "---\ntype: episode\n---\nSession 01.\n",
            "event.md": "---\ntype: npc\nepisode: \"[[Session 01]]\"\n---\nEvent.\n",
        },
    )
    VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",))

    rows = _conn(tmp_path).execute(
        "SELECT raw_target, section, link_type FROM links WHERE source = 'vault/event.md'"
    ).fetchall()
    typed = [(r[1], r[2]) for r in rows]
    assert ("episode", "CANON_IN") in typed


def test_body_wikilinks_have_null_link_type(tmp_path: Path) -> None:
    _setup(
        tmp_path,
        {
            "target.md": "---\ntype: npc\n---\nTarget body.\n",
            "source.md": "---\ntype: npc\n---\nSee [[Target]] for more.\n",
        },
    )
    VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",))

    rows = _conn(tmp_path).execute(
        "SELECT link_type FROM links WHERE source = 'vault/source.md'"
    ).fetchall()
    assert len(rows) >= 1
    assert all(r[0] is None for r in rows)


def test_page_with_typed_edge_and_body_link_to_same_target(tmp_path: Path) -> None:
    """Typed frontmatter edge and body wikilink to the same target produce
    separate rows: typed edge with link_type set, body link with NULL."""
    _setup(
        tmp_path,
        {
            "city.md": "---\ntype: location\n---\nCity body.\n",
            "merchant.md": (
                "---\ntype: npc\nlocation: \"[[City]]\"\n---\n"
                "Merchant lives in [[City]].\n"
            ),
        },
    )
    VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",))

    rows = _conn(tmp_path).execute(
        "SELECT section, link_type FROM links WHERE source = 'vault/merchant.md' "
        "AND raw_target = 'City'"
    ).fetchall()
    link_types = {r[1] for r in rows}
    assert "LOCATED_AT" in link_types
    assert None in link_types


def test_empty_typed_frontmatter_value_produces_no_edge(tmp_path: Path) -> None:
    """A key with a null or empty value must not insert a link row."""
    _setup(
        tmp_path,
        {"page.md": "---\ntype: npc\nlocation:\nwithin: \"\"\n---\nBody.\n"},
    )
    VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",))

    rows = _conn(tmp_path).execute(
        "SELECT link_type FROM links WHERE source = 'vault/page.md' AND link_type IS NOT NULL"
    ).fetchall()
    assert rows == []


def test_typed_edge_target_resolved_in_db(tmp_path: Path) -> None:
    """After build, the `target` column in a typed edge row resolves to the
    target page's rel_path (not NULL) when the target exists."""
    _setup(
        tmp_path,
        {
            "known-place.md": "---\ntype: location\n---\nKnown place.\n",
            "traveller.md": "---\ntype: npc\nlocation: \"[[known-place]]\"\n---\nTraveller.\n",
        },
    )
    VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",))

    row = _conn(tmp_path).execute(
        "SELECT target FROM links WHERE source = 'vault/traveller.md' AND link_type = 'LOCATED_AT'"
    ).fetchone()
    assert row is not None
    assert row[0] == "vault/known-place.md"


# ---------------------------------------------------------------------------
# ANCHOR_MISSING lint rule
# ---------------------------------------------------------------------------


def _anchor_missing_findings(root: Path) -> list[object]:
    corpus = VaultIndex.build(root, root / "vault", ("vault",))
    rule = registry()["wiki/anchor-missing"]
    return list(rule.check(corpus.get_page("vault/subject.md"), corpus))  # type: ignore[arg-type]


def test_anchor_missing_fires_when_location_key_has_null_value(tmp_path: Path) -> None:
    _setup(
        tmp_path,
        {"subject.md": "---\ntype: npc\nlocation:\n---\nBody.\n"},
    )
    findings = _anchor_missing_findings(tmp_path)

    assert len(findings) == 1
    assert findings[0].rule_id == "wiki/anchor-missing"  # type: ignore[attr-defined]
    assert "location:" in findings[0].message  # type: ignore[attr-defined]


def test_anchor_missing_fires_when_within_key_has_empty_string(tmp_path: Path) -> None:
    _setup(
        tmp_path,
        {"subject.md": "---\ntype: npc\nwithin: \"\"\n---\nBody.\n"},
    )
    findings = _anchor_missing_findings(tmp_path)

    assert len(findings) == 1
    assert "within:" in findings[0].message  # type: ignore[attr-defined]


def test_anchor_missing_fires_once_per_empty_key(tmp_path: Path) -> None:
    _setup(
        tmp_path,
        {"subject.md": "---\ntype: npc\nlocation:\nwithin:\n---\nBody.\n"},
    )
    findings = _anchor_missing_findings(tmp_path)
    assert len(findings) == 2


def test_anchor_missing_silent_for_nonempty_location(tmp_path: Path) -> None:
    _setup(
        tmp_path,
        {
            "city.md": "---\ntype: location\n---\nCity.\n",
            "subject.md": "---\ntype: npc\nlocation: \"[[City]]\"\n---\nBody.\n",
        },
    )
    findings = _anchor_missing_findings(tmp_path)
    assert findings == []


def test_anchor_missing_silent_when_no_spatial_keys(tmp_path: Path) -> None:
    _setup(
        tmp_path,
        {"subject.md": "---\ntype: npc\n---\nBody.\n"},
    )
    findings = _anchor_missing_findings(tmp_path)
    assert findings == []


# ---------------------------------------------------------------------------
# ANCHOR_AMBIGUOUS lint rule
# ---------------------------------------------------------------------------


def _ambiguous_findings(root: Path) -> list[object]:
    corpus = VaultIndex.build(root, root / "vault", ("vault",))
    rule = registry()["wiki/anchor-ambiguous"]
    return list(rule.check(corpus))  # type: ignore[arg-type]


def test_anchor_ambiguous_fires_when_location_and_within_resolve_to_different_pages(
    tmp_path: Path,
) -> None:
    _setup(
        tmp_path,
        {
            "city.md": "---\ntype: location\n---\nCity.\n",
            "tavern.md": "---\ntype: location\n---\nTavern.\n",
            "vault/subject.md".replace("vault/", ""): (
                "---\ntype: npc\nlocation: \"[[City]]\"\nwithin: \"[[Tavern]]\"\n---\nBody.\n"
            ),
        },
    )
    findings = _ambiguous_findings(tmp_path)
    subject_findings = [f for f in findings if "subject" in f.file]  # type: ignore[attr-defined]

    assert len(subject_findings) == 1
    f = subject_findings[0]
    assert f.rule_id == "wiki/anchor-ambiguous"  # type: ignore[attr-defined]
    assert f.severity == "warning"  # type: ignore[attr-defined]
    assert "anchor" in f.message.lower()  # type: ignore[attr-defined]


def test_anchor_ambiguous_silent_when_anchor_key_present(tmp_path: Path) -> None:
    _setup(
        tmp_path,
        {
            "city.md": "---\ntype: location\n---\nCity.\n",
            "tavern.md": "---\ntype: location\n---\nTavern.\n",
            "subject.md": (
                "---\ntype: npc\nlocation: \"[[City]]\"\nwithin: \"[[Tavern]]\"\n"
                "anchor: city\n---\nBody.\n"
            ),
        },
    )
    findings = _ambiguous_findings(tmp_path)
    assert not any("subject" in f.file for f in findings)  # type: ignore[attr-defined]


def test_anchor_ambiguous_silent_when_only_one_anchor_resolves(tmp_path: Path) -> None:
    _setup(
        tmp_path,
        {
            "city.md": "---\ntype: location\n---\nCity.\n",
            "subject.md": (
                "---\ntype: npc\nlocation: \"[[City]]\"\nwithin: \"[[NoSuchPlace]]\"\n---\nBody.\n"
            ),
        },
    )
    findings = _ambiguous_findings(tmp_path)
    assert not any("subject" in f.file for f in findings)  # type: ignore[attr-defined]


def test_anchor_ambiguous_silent_when_both_resolve_to_same_page(tmp_path: Path) -> None:
    _setup(
        tmp_path,
        {
            "city.md": "---\ntype: location\naliases: [The City]\n---\nCity.\n",
            "subject.md": (
                "---\ntype: npc\nlocation: \"[[City]]\"\nwithin: \"[[The City]]\"\n---\nBody.\n"
            ),
        },
    )
    findings = _ambiguous_findings(tmp_path)
    assert not any("subject" in f.file for f in findings)  # type: ignore[attr-defined]


def test_anchor_missing_rule_is_registered_structural_warning() -> None:
    rule = registry()["wiki/anchor-missing"]
    assert rule.tier == "structural"
    assert rule.severity == "warning"
    assert rule.pure is True


def test_anchor_ambiguous_rule_is_registered_content_shape_warning() -> None:
    rule = registry()["wiki/anchor-ambiguous"]
    assert rule.tier == "content-shape"
    assert rule.severity == "warning"
    assert rule.pure is False
