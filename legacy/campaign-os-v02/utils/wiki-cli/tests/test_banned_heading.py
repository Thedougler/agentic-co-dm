"""W142 — ## What's True banned on session ≥ 9."""

from __future__ import annotations

from pathlib import Path

import wiki_cli.rules  # noqa: F401
from wiki_cli.contracts import Page, registry


class _StubCorpus:
    repo_root = Path(".")

    def pages(self) -> list[Page]:
        return []

    def resolve(self, name: str) -> Page | None:
        del name
        return None

    def by_type(self, page_type: str) -> list[Page]:
        del page_type
        return []

    def links_from(self, rel_path: str) -> list[str]:
        del rel_path
        return []

    def links_to(self, rel_path: str) -> list[str]:
        del rel_path
        return []


def _page(rel_path: str, body: str) -> Page:
    return Page(
        rel_path=rel_path,
        raw=body,
        frontmatter={"type": "moment"},
        body=body,
        body_start_line=10,
    )


def test_w142_whats_true_on_009_fails() -> None:
    page = _page(
        "vault/episodes/009/moment-01-open.md",
        "## What Happens\n\nok\n\n## What's True\n\nleftover\n",
    )
    findings = list(registry()["W142"].check(page, _StubCorpus()))
    assert len(findings) == 1
    assert findings[0].rule_id == "W142"
    assert "What's True" in findings[0].message


def test_w142_what_happens_only_is_silent() -> None:
    page = _page(
        "vault/episodes/009/moment-01-open.md",
        "## What Happens\n\nok\n",
    )
    assert list(registry()["W142"].check(page, _StubCorpus())) == []


def test_w142_session_008_whats_true_is_silent() -> None:
    page = _page(
        "vault/episodes/008/moment-01-the-table.md",
        "## What's True\n\nold dump\n",
    )
    assert list(registry()["W142"].check(page, _StubCorpus())) == []
