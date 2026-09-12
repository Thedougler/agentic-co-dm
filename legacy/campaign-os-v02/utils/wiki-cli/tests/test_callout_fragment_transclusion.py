"""TDD for W136: callout-fragment transclusion resolution (ADR-0053, issue #03).

Two checks are exercised:

Forward — ``![[slug-c0N]]`` in a parent page must resolve to an existing file.
Orphan — a file matching ``-c\\d{2,}\\.md$`` must be transcluded by at least
one parent page.

Fixture layout uses ``tmp_path`` + ``VaultIndex.build()`` so each test
controls exactly which files exist on disk.
"""

from __future__ import annotations

from pathlib import Path

import wiki_cli.rules  # noqa: F401  side-effect: registers every rule
from wiki_cli.contracts import VaultRule, registry
from wiki_cli.index import VaultIndex

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _check_w136(corpus: VaultIndex) -> list:
    rule = registry()["W136"]
    assert isinstance(rule, VaultRule)
    return list(rule.check(corpus))


# ---------------------------------------------------------------------------
# Forward check: parent transcludes a fragment that exists → no finding
# ---------------------------------------------------------------------------


def test_forward_resolves_existing_fragment(tmp_path: Path) -> None:
    """``![[foo-c01]]`` in a parent page, ``foo-c01.md`` present → 0 findings."""
    (tmp_path / "vault" / "_templates").mkdir(parents=True)
    (tmp_path / ".wiki-cli").mkdir()

    parent = tmp_path / "vault" / "foo.md"
    parent.write_text("---\ntype: npc\n---\n\n![[foo-c01]]\n", encoding="utf-8")

    fragment = tmp_path / "vault" / "foo-c01.md"
    fragment.write_text("> [!mechanic]\n> Some mechanic text.\n", encoding="utf-8")

    corpus = VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",))
    findings = [f for f in _check_w136(corpus) if f.rule_id == "W136"]
    assert findings == [], f"expected 0 findings; got {findings}"


# ---------------------------------------------------------------------------
# Forward check: parent transcludes a missing fragment → finding on parent
# ---------------------------------------------------------------------------


def test_forward_missing_fragment_yields_finding(tmp_path: Path) -> None:
    """``![[foo-c01]]`` in a parent page, ``foo-c01.md`` absent → 1 finding."""
    (tmp_path / "vault" / "_templates").mkdir(parents=True)
    (tmp_path / ".wiki-cli").mkdir()

    parent = tmp_path / "vault" / "foo.md"
    parent.write_text("---\ntype: npc\n---\n\n![[foo-c01]]\n", encoding="utf-8")
    # foo-c01.md deliberately NOT created

    corpus = VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",))
    findings = [f for f in _check_w136(corpus) if f.rule_id == "W136"]

    assert len(findings) == 1, f"expected 1 finding; got {findings}"
    assert findings[0].file == "vault/foo.md"
    assert "foo-c01" in findings[0].message


# ---------------------------------------------------------------------------
# Orphan check: fragment with no parent transclusion → orphan finding
# ---------------------------------------------------------------------------


def test_orphan_fragment_yields_finding(tmp_path: Path) -> None:
    """``foo-c01.md`` exists, no parent transcludes it → 1 orphan finding."""
    (tmp_path / "vault" / "_templates").mkdir(parents=True)
    (tmp_path / ".wiki-cli").mkdir()

    fragment = tmp_path / "vault" / "foo-c01.md"
    fragment.write_text("> [!mechanic]\n> Some mechanic text.\n", encoding="utf-8")
    # No parent page

    corpus = VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",))
    findings = [f for f in _check_w136(corpus) if f.rule_id == "W136"]

    assert len(findings) == 1, f"expected 1 orphan finding; got {findings}"
    assert findings[0].file == "vault/foo-c01.md"
    assert "orphaned" in findings[0].message


# ---------------------------------------------------------------------------
# Non-fragment transclusion: ![[bar]] → no finding from W136
# ---------------------------------------------------------------------------


def test_non_fragment_embed_ignored(tmp_path: Path) -> None:
    """``![[bar]]`` transclusion (no ``-c0N`` pattern) → 0 findings from W136."""
    (tmp_path / "vault" / "_templates").mkdir(parents=True)
    (tmp_path / ".wiki-cli").mkdir()

    parent = tmp_path / "vault" / "foo.md"
    parent.write_text("---\ntype: npc\n---\n\n![[bar]]\n", encoding="utf-8")

    bar = tmp_path / "vault" / "bar.md"
    bar.write_text("---\ntype: location\n---\n\n# Bar\n", encoding="utf-8")

    corpus = VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",))
    findings = [f for f in _check_w136(corpus) if f.rule_id == "W136"]
    assert findings == [], f"expected 0 findings for non-fragment embed; got {findings}"


# ---------------------------------------------------------------------------
# Severity: W136 findings are baselineable warnings
# ---------------------------------------------------------------------------


def test_forward_resolves_existing_narration_sibling(tmp_path: Path) -> None:
    """``![[foo-narration-appearance]]`` with the sibling present → 0 findings."""
    (tmp_path / "vault" / "_templates").mkdir(parents=True)
    (tmp_path / ".wiki-cli").mkdir()
    (tmp_path / "vault" / "foo.md").write_text(
        "---\ntype: npc\n---\n\n![[foo-narration-appearance]]\n",
        encoding="utf-8",
    )
    (tmp_path / "vault" / "foo-narration-appearance.md").write_text(
        "---\ntype: narration\nparent: '[[foo]]'\n---\n\n*Salt and wet rope.*\n",
        encoding="utf-8",
    )
    findings = [f for f in _check_w136(VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",))) if f.rule_id == "W136"]
    assert findings == [], f"expected 0 findings; got {findings}"


def test_forward_missing_narration_sibling_yields_finding(tmp_path: Path) -> None:
    """``![[foo-narration-appearance]]`` with no sibling file → 1 finding."""
    (tmp_path / "vault" / "_templates").mkdir(parents=True)
    (tmp_path / ".wiki-cli").mkdir()
    (tmp_path / "vault" / "foo.md").write_text(
        "---\ntype: npc\n---\n\n![[foo-narration-appearance]]\n",
        encoding="utf-8",
    )
    findings = [f for f in _check_w136(VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",))) if f.rule_id == "W136"]
    assert len(findings) == 1, f"expected 1 finding; got {findings}"
    assert "foo-narration-appearance" in findings[0].message


def test_orphan_narration_file_yields_finding(tmp_path: Path) -> None:
    """``type: narration`` file with no parent embed → orphan finding."""
    (tmp_path / "vault" / "_templates").mkdir(parents=True)
    (tmp_path / ".wiki-cli").mkdir()
    (tmp_path / "vault" / "foo-narration-appearance.md").write_text(
        "---\ntype: narration\nparent: '[[foo]]'\n---\n\n*Salt.*\n",
        encoding="utf-8",
    )
    findings = [f for f in _check_w136(VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",))) if f.rule_id == "W136"]
    assert len(findings) == 1, f"expected 1 orphan finding; got {findings}"
    assert findings[0].file == "vault/foo-narration-appearance.md"
    assert "orphan" in findings[0].message.lower()


def test_w136_severity_is_a_baselineable_warning(tmp_path: Path) -> None:
    """W136 findings carry warning severity, so old hits baseline as debt."""
    (tmp_path / "vault" / "_templates").mkdir(parents=True)
    (tmp_path / ".wiki-cli").mkdir()

    fragment = tmp_path / "vault" / "foo-c01.md"
    fragment.write_text("> [!mechanic]\n> text.\n", encoding="utf-8")

    corpus = VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",))
    findings = [f for f in _check_w136(corpus) if f.rule_id == "W136"]

    assert findings, "expected at least one finding to check severity on"
    from wiki_cli.contracts import Severity

    assert all(f.severity == Severity.WARNING for f in findings), (
        f"all W136 findings must be warnings; got {[f.severity for f in findings]}"
    )
