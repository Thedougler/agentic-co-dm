"""Town and crossing run-guides: ADR-0059 format passes W140/W141."""

from __future__ import annotations

from pathlib import Path

import wiki_cli.rules  # noqa: F401
from wiki_cli.contracts import Page, registry


class _StubCorpus:
    def __init__(self, pages: list[Page] | None = None) -> None:
        self.repo_root = Path(".")
        self._pages = pages or []

    def pages(self) -> list[Page]:
        return self._pages

    def resolve(self, name: str) -> Page | None:
        del name
        return None

    def by_type(self, page_type: str) -> list[Page]:
        return [page for page in self._pages if page.type == page_type]

    def links_from(self, rel_path: str) -> list[str]:
        del rel_path
        return []

    def links_to(self, rel_path: str) -> list[str]:
        del rel_path
        return []


def _page(rel_path: str, frontmatter: dict[str, object], body: str) -> Page:
    return Page(
        rel_path=rel_path,
        raw=body,
        frontmatter=frontmatter,
        body=body,
        body_start_line=8,
    )


_TOWN = """\
## Last Time

The harbour was quiet.

## Prep

Calveno docks.

## 1 — Claims

![[harbour-claims#Checks]]

## Exit

- [[velvet-noose-takes-the-lane-run-guide]]
"""

_CROSSING = """\
## Last Time

They named a bearing.

## Prep

Open water.

## 1 — Heading

![[central-strait-crossing#Premise]]

## Exit

- [[high-eyries-storm-door-run-guide]]
- [[sparholds-burning-challenge-run-guide]]
"""


def test_town_run_guide_passes_w140_and_w141() -> None:
    guide = _page(
        "vault/episodes/010/e10-run-guide-harbour.md",
        {"type": "session", "subtype": "run-guide"},
        _TOWN,
    )
    corpus = _StubCorpus([guide])
    assert list(registry()["W140"].check(guide, corpus)) == []
    assert list(registry()["W141"].check(guide, corpus)) == []


def test_crossing_run_guide_passes_w140_and_w141() -> None:
    guide = _page(
        "vault/episodes/011/e11-run-guide-strait.md",
        {"type": "session", "subtype": "run-guide"},
        _CROSSING,
    )
    corpus = _StubCorpus([guide])
    assert list(registry()["W140"].check(guide, corpus)) == []
    assert list(registry()["W141"].check(guide, corpus)) == []


def test_crossing_menu_needs_no_destination_fork() -> None:
    assert "![[fork-" not in _CROSSING
    assert "fork-01" not in _CROSSING
