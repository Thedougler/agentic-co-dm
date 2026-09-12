"""TDD for W137: inline play callout on a page whose template expects
callout-fragment transclusion (ADR-0053, issue #04).

The rule is advisory: it flags inline play callouts on pages whose type
template has been migrated to ``![[slug-c0N]]`` transclusion placeholders.

Fixture layout: each test creates a minimal repo in ``tmp_path`` with:
- ``wiki.toml`` supplying ``PLAY_CALLOUTS``
- ``vault/_templates/`` with per-type template files
- vault pages under ``vault/``

The rule is invoked directly against the VaultIndex so each test controls
exactly which files exist and which template each type resolves to.
"""

from __future__ import annotations

from pathlib import Path

import wiki_cli.rules  # noqa: F401  side-effect: registers every rule
from wiki_cli.contracts import FileRule, Severity, registry
from wiki_cli.index import VaultIndex

_PLAY_CALLOUTS_VALUE = "read-aloud | narration | dm | mechanic | check | dialogue | spoiler"

_WIKI_TOML = f"""\
[vault]
root = "vault"

[thresholds]
PLAY_CALLOUTS = "{_PLAY_CALLOUTS_VALUE}"
"""

_TRANSCLUSION_TEMPLATE = """\
---
type: npc
status: stub
publish: false
---

![[npc-c01]]
"""

_INLINE_TEMPLATE = """\
---
type: location
status: stub
publish: false
---

> [!read-aloud]
> OPTIONAL
"""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _build_vault(tmp_path: Path) -> None:
    """Create the minimal repo scaffold every fixture needs."""
    (tmp_path / "vault" / "_templates").mkdir(parents=True)
    (tmp_path / ".wiki-cli").mkdir(parents=True)
    (tmp_path / "wiki.toml").write_text(_WIKI_TOML, encoding="utf-8")


def _check_w137(corpus: VaultIndex) -> list:
    rule = registry()["W137"]
    assert isinstance(rule, FileRule)
    findings = []
    for page in corpus.pages():
        findings.extend(rule.check(page, corpus))
    return [f for f in findings if f.rule_id == "W137"]


# ---------------------------------------------------------------------------
# Test 1: inline play callout + template expects transclusion → finding
# ---------------------------------------------------------------------------


def test_inline_callout_on_transclusion_template_yields_finding(tmp_path: Path) -> None:
    """Inline [!read-aloud] on an npc page whose template has ![[npc-c01]] → 1 advisory finding."""
    _build_vault(tmp_path)
    (tmp_path / "vault" / "_templates" / "_npc.md").write_text(
        _TRANSCLUSION_TEMPLATE, encoding="utf-8"
    )

    page = tmp_path / "vault" / "campaigns" / "shattered-sea" / "npcs" / "grimtooth.md"
    page.parent.mkdir(parents=True)
    page.write_text(
        "---\ntype: npc\nstatus: stub\npublish: false\n---\n\n"
        "> [!read-aloud]\n> The troll grins.\n",
        encoding="utf-8",
    )

    corpus = VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",))
    findings = _check_w137(corpus)

    assert len(findings) == 1, f"expected 1 finding; got {findings}"
    assert "read-aloud" in findings[0].message
    assert findings[0].file == "vault/campaigns/shattered-sea/npcs/grimtooth.md"


# ---------------------------------------------------------------------------
# Test 2: transclusion on page whose template expects transclusion → no finding
# ---------------------------------------------------------------------------


def test_transclusion_embed_on_transclusion_template_no_finding(tmp_path: Path) -> None:
    """![[grimtooth-c01]] embed (already migrated) → 0 findings."""
    _build_vault(tmp_path)
    (tmp_path / "vault" / "_templates" / "_npc.md").write_text(
        _TRANSCLUSION_TEMPLATE, encoding="utf-8"
    )

    frag = tmp_path / "vault" / "campaigns" / "shattered-sea" / "npcs" / "grimtooth-c01.md"
    frag.parent.mkdir(parents=True)
    frag.write_text("> [!read-aloud]\n> The troll grins.\n", encoding="utf-8")

    page = tmp_path / "vault" / "campaigns" / "shattered-sea" / "npcs" / "grimtooth.md"
    page.write_text(
        "---\ntype: npc\nstatus: stub\npublish: false\n---\n\n![[grimtooth-c01]]\n",
        encoding="utf-8",
    )

    corpus = VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",))
    findings = _check_w137(corpus)
    assert findings == [], f"expected 0 findings for migrated page; got {findings}"


# ---------------------------------------------------------------------------
# Test 3: inline play callout + template still uses inline placeholder → no finding
# ---------------------------------------------------------------------------


def test_inline_callout_on_inline_template_no_finding(tmp_path: Path) -> None:
    """Inline [!read-aloud] on a location page whose template still has inline
    placeholders (no ![[...-c0N]]) → 0 findings."""
    _build_vault(tmp_path)
    (tmp_path / "vault" / "_templates" / "_location.md").write_text(
        _INLINE_TEMPLATE, encoding="utf-8"
    )

    page = tmp_path / "vault" / "world" / "location.md"
    page.parent.mkdir(parents=True)
    page.write_text(
        "---\ntype: location\nstatus: stub\npublish: false\n---\n\n"
        "> [!read-aloud]\n> The forest hums.\n",
        encoding="utf-8",
    )

    corpus = VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",))
    findings = _check_w137(corpus)
    assert findings == [], f"expected 0 findings when template uses inline placeholders; got {findings}"


# ---------------------------------------------------------------------------
# Test 4: docs/meta page with inline [!note] → no finding
# ---------------------------------------------------------------------------


def test_generic_callout_on_transclusion_template_no_finding(tmp_path: Path) -> None:
    """[!note] on a play page with a transclusion template → 0 findings.

    Generic callouts (not in PLAY_CALLOUTS) are excluded even when the template
    has migrated to transclusion — only play callout types are candidates for
    extraction into -c0N fragment files.
    """
    _build_vault(tmp_path)
    (tmp_path / "vault" / "_templates" / "_npc.md").write_text(
        _TRANSCLUSION_TEMPLATE, encoding="utf-8"
    )

    page = tmp_path / "vault" / "campaigns" / "shattered-sea" / "npcs" / "lore-npc.md"
    page.parent.mkdir(parents=True)
    page.write_text(
        "---\ntype: npc\nstatus: stub\npublish: false\n---\n\n"
        "> [!note]\n> A generic doc note.\n",
        encoding="utf-8",
    )

    corpus = VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",))
    findings = _check_w137(corpus)
    assert findings == [], f"expected 0 findings for generic [!note] callout; got {findings}"


# ---------------------------------------------------------------------------
# Test 5: W137 severity is advisory
# ---------------------------------------------------------------------------


def test_inline_read_aloud_on_narration_embed_template_yields_finding(
    tmp_path: Path,
) -> None:
    """Inline [!read-aloud] on a page whose template has ![[…-narration-…]] → finding."""
    _build_vault(tmp_path)
    (tmp_path / "vault" / "_templates" / "_npc.md").write_text(
        "---\ntype: npc\nstatus: stub\npublish: false\n---\n\n"
        "![[<slug>-narration-appearance]]\n",
        encoding="utf-8",
    )
    page = tmp_path / "vault" / "campaigns" / "shattered-sea" / "npcs" / "nona.md"
    page.parent.mkdir(parents=True)
    page.write_text(
        "---\ntype: npc\nstatus: stub\npublish: false\n---\n\n"
        "> [!read-aloud]\n> Salt in her fur.\n",
        encoding="utf-8",
    )
    findings = _check_w137(VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",)))
    assert len(findings) == 1, f"expected 1 finding; got {findings}"
    assert "read-aloud" in findings[0].message


def test_inline_mechanic_on_narration_embed_template_no_finding(tmp_path: Path) -> None:
    """[!mechanic] stays inline — W137 extracts only performative callouts."""
    _build_vault(tmp_path)
    (tmp_path / "vault" / "_templates" / "_npc.md").write_text(
        "---\ntype: npc\nstatus: stub\npublish: false\n---\n\n"
        "![[<slug>-narration-appearance]]\n",
        encoding="utf-8",
    )
    page = tmp_path / "vault" / "campaigns" / "shattered-sea" / "npcs" / "brute.md"
    page.parent.mkdir(parents=True)
    page.write_text(
        "---\ntype: npc\nstatus: stub\npublish: false\n---\n\n"
        "> [!mechanic]\n> AC 14, HP 45.\n",
        encoding="utf-8",
    )
    findings = _check_w137(VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",)))
    assert findings == [], f"expected 0 findings for inline mechanic; got {findings}"


def test_w137_severity_is_advisory(tmp_path: Path) -> None:
    """W137 findings carry advisory severity — must not gate commits."""
    _build_vault(tmp_path)
    (tmp_path / "vault" / "_templates" / "_npc.md").write_text(
        _TRANSCLUSION_TEMPLATE, encoding="utf-8"
    )

    page = tmp_path / "vault" / "campaigns" / "shattered-sea" / "npcs" / "brute.md"
    page.parent.mkdir(parents=True)
    page.write_text(
        "---\ntype: npc\nstatus: stub\npublish: false\n---\n\n"
        "> [!read-aloud]\n> The troll grins.\n",
        encoding="utf-8",
    )

    corpus = VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",))
    findings = _check_w137(corpus)

    assert findings, "expected at least one finding to check severity on"
    assert all(f.severity == Severity.WARNING for f in findings), (
        f"all W137 findings must be warnings; got {[f.severity for f in findings]}"
    )
