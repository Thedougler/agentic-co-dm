"""TDD for W145: speaking-time band on player-facing prose."""

from __future__ import annotations

from pathlib import Path

import wiki_cli.rules  # noqa: F401
from wiki_cli.contracts import FileRule, registry
from wiki_cli.index import VaultIndex


def _check(corpus: VaultIndex) -> list:
    rule = registry()["W145"]
    assert isinstance(rule, FileRule)
    findings = []
    for page in corpus.pages():
        findings.extend(rule.check(page, corpus))
    return [f for f in findings if f.rule_id == "W145"]


def _vault(tmp_path: Path, rel: str, text: str) -> VaultIndex:
    (tmp_path / "vault" / "_templates").mkdir(parents=True)
    (tmp_path / ".wiki-cli").mkdir()
    page = tmp_path / rel
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(text, encoding="utf-8")
    return VaultIndex.build(tmp_path, tmp_path / "vault", ("vault",))


def test_short_depiction_warns(tmp_path: Path) -> None:
    corpus = _vault(
        tmp_path,
        "vault/shop-narration-appearance.md",
        "---\ntype: narration\nmode: establish\nparent: '[[shop]]'\n---\n\n"
        "> [!narration]\n> *Salt and rope.*\n",
    )
    findings = _check(corpus)
    assert len(findings) == 1
    assert "words" in findings[0].message


def test_piped_wikilink_counts_display_only(tmp_path: Path) -> None:
    from wiki_cli.rules.speaking_time_budget import _words

    spoken = _words("The *[[uncertainty|Uncertainty]]* sits off [[aruhe|Aruhe]].")
    assert spoken == 5


def test_unpiped_wikilink_counts_slug_as_spoken_name(tmp_path: Path) -> None:
    from wiki_cli.rules.speaking_time_budget import _words

    assert _words("[[locations/aruhe]] ahead.") == 2


def test_in_band_depiction_clean(tmp_path: Path) -> None:
    body = " ".join(["timber"] * 120)
    corpus = _vault(
        tmp_path,
        "vault/shop-narration-appearance.md",
        "---\ntype: narration\nmode: establish\nparent: '[[shop]]'\n---\n\n"
        f"> [!narration]\n> *{body}*\n",
    )
    assert _check(corpus) == []
