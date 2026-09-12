"""W140/W141 — eNN-overview / eNN-run-guide-<slug>, stretch coverage."""

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


def _guide(rel_path: str, body: str) -> Page:
    return _page(
        rel_path,
        {"type": "session", "subtype": "run-guide"},
        body,
    )


_WALK = """\
## Last Time

hook

## Prep

where

## 1 — Open

![[beat-01-open#Checks]]

## Exit

- [[beat-01-skip]]
"""


def test_w140_bare_run_guide_name_fails() -> None:
    page = _guide("vault/episodes/009/run-guide.md", _WALK)
    findings = list(registry()["W140"].check(page, _StubCorpus()))
    assert any("e09-run-guide-" in finding.message for finding in findings)


def test_w140_legacy_single_basename_fails() -> None:
    page = _guide("vault/episodes/009/e09-run-guide.md", _WALK)
    findings = list(registry()["W140"].check(page, _StubCorpus()))
    assert any("e09-run-guide-" in finding.message for finding in findings)


def test_w140_slug_basename_is_silent() -> None:
    page = _guide("vault/episodes/009/e09-run-guide-open.md", _WALK)
    assert list(registry()["W140"].check(page, _StubCorpus())) == []


def test_w140_overview_wrong_name_fails() -> None:
    page = _page(
        "vault/episodes/009/index.md",
        {"type": "session", "subtype": "overview", "session_shape": "crossing"},
        "## Read first\n\nhere\n",
    )
    findings = list(registry()["W140"].check(page, _StubCorpus()))
    assert any("e09-overview.md" in finding.message for finding in findings)


def test_w140_index_subtype_fails() -> None:
    page = _page(
        "vault/episodes/009/e09-index.md",
        {"type": "session", "subtype": "index"},
        "## Now\n\nhere\n",
    )
    findings = list(registry()["W140"].check(page, _StubCorpus()))
    assert any("overview" in finding.message for finding in findings)


def test_w140_missing_session_shape_fails() -> None:
    page = _page(
        "vault/episodes/009/e09-overview.md",
        {"type": "session", "subtype": "overview"},
        "## Read first\n\nx\n",
    )
    findings = list(registry()["W140"].check(page, _StubCorpus()))
    assert any("session_shape" in finding.message for finding in findings)


def test_w140_invalid_session_shape_fails() -> None:
    page = _page(
        "vault/episodes/009/e09-overview.md",
        {"type": "session", "subtype": "overview", "session_shape": "voyage"},
        "## Read first\n\nx\n",
    )
    findings = list(registry()["W140"].check(page, _StubCorpus()))
    assert any("voyage" in finding.message for finding in findings)


def test_w140_session_008_bare_name_is_silent() -> None:
    page = _guide("vault/episodes/008/run-guide.md", "## Now\n\nold brief\n")
    assert list(registry()["W140"].check(page, _StubCorpus())) == []


def test_w141_beat_missing_from_walk_and_exit_fails() -> None:
    guide = _guide("vault/episodes/009/e09-run-guide-open.md", _WALK)
    missing = _page(
        "vault/episodes/009/beat-02-other.md",
        {"type": "beat", "beat_type": "development"},
        "## Pressure\n\nx\n",
    )
    findings = list(registry()["W141"].check(guide, _StubCorpus([guide, missing])))
    assert any("beat-02-other" in finding.message for finding in findings)


def test_w141_exit_wikilink_covers_beat() -> None:
    guide = _guide("vault/episodes/009/e09-run-guide-open.md", _WALK)
    beat = _page(
        "vault/episodes/009/beat-01-skip.md",
        {"type": "beat", "beat_type": "development"},
        "## Pressure\n\nx\n",
    )
    assert list(registry()["W141"].check(guide, _StubCorpus([guide, beat]))) == []


def test_w141_exit_transclusion_fails() -> None:
    body = """\
## Prep

where

## 1 — Open

![[beat-01-open#Checks]]

## Exit

![[beat-01-skip]]
"""
    guide = _guide("vault/episodes/009/e09-run-guide-open.md", body)
    findings = list(registry()["W141"].check(guide, _StubCorpus([guide])))
    assert any("transclusion" in finding.message for finding in findings)


def test_w141_covered_beats_are_silent() -> None:
    guide = _guide("vault/episodes/009/e09-run-guide-open.md", _WALK)
    open_beat = _page(
        "vault/episodes/009/beat-01-open.md",
        {"type": "beat", "beat_type": "hook"},
        "## Pressure\n\nx\n",
    )
    skip_beat = _page(
        "vault/episodes/009/beat-01-skip.md",
        {"type": "beat", "beat_type": "development"},
        "## Pressure\n\nx\n",
    )
    assert (
        list(registry()["W141"].check(guide, _StubCorpus([guide, open_beat, skip_beat])))
        == []
    )


def test_w141_whole_file_beat_embed_passes() -> None:
    body = """\
## Prep

where

## 1 — Open

![[beat-01-open]]

## Exit

- [[beat-01-skip]]
"""
    guide = _guide("vault/episodes/009/e09-run-guide-open.md", body)
    findings = list(registry()["W141"].check(guide, _StubCorpus([guide])))
    assert not any("whole-file" in finding.message for finding in findings)


def test_w141_play_wikilink_covers_beat() -> None:
    body = """\
## Prep

where

## 1 — Open

Open on [[beat-01-open|Cold Open]]. Speak [[beat-01-open-narration-open|the wreck]].

## Exit

- [[beat-01-skip]]
"""
    guide = _guide("vault/episodes/009/e09-run-guide-open.md", body)
    beat = _page(
        "vault/episodes/009/beat-01-open.md",
        {"type": "beat", "beat_type": "hook"},
        "## Pressure\n\nx\n",
    )
    findings = list(
        registry()["W141"].check(guide, _StubCorpus([guide, beat]))
    )
    assert findings == [], f"expected 0 findings; got {findings}"


def test_w141_narration_file_embed_covers_parent_beat() -> None:
    body = """\
## Prep

where

## 1 — Open

![[beat-01-open-narration-open]]

## Exit

- [[beat-01-skip]]
"""
    guide = _guide("vault/episodes/009/e09-run-guide-open.md", body)
    beat = _page(
        "vault/episodes/009/beat-01-open.md",
        {"type": "beat", "beat_type": "hook"},
        "## Pressure\n\nx\n",
    )
    findings = list(
        registry()["W141"].check(guide, _StubCorpus([guide, beat]))
    )
    assert findings == [], f"expected 0 findings; got {findings}"


def test_w141_whole_file_prefix_is_scoped_to_beat() -> None:
    # Only beat- whole-file embeds fire — a passage- slug is out of scope now
    # that passage is a retired type carrying no coverage semantics here.
    body = """\
## Prep

where

## 1 — Open

![[passage-01-south]]

## Exit

- [[beat-01-skip]]
"""
    guide = _guide("vault/episodes/009/e09-run-guide-open.md", body)
    findings = list(registry()["W141"].check(guide, _StubCorpus([guide])))
    assert not any("whole-file" in finding.message for finding in findings)


def test_w141_heading_embed_is_silent() -> None:
    body = """\
## Prep

where

## 1 — Open

![[uncertainty-refit-tour#Read-aloud]]

![[uncertainty-refit-tour#Checks]]

## Exit

- [[beat-01-skip]]
"""
    guide = _guide("vault/episodes/009/e09-run-guide-open.md", body)
    assert list(registry()["W141"].check(guide, _StubCorpus([guide]))) == []


def test_w141_union_across_guides_covers_beats() -> None:
    first = _guide(
        "vault/episodes/009/e09-run-guide-open.md",
        """\
## Prep

start

## 1 — Open

![[beat-01-open#Checks]]

## Exit

- [[e09-run-guide-harbour]]
""",
    )
    second = _guide(
        "vault/episodes/009/e09-run-guide-harbour.md",
        """\
## Prep

harbour

## 1 — Dock

![[beat-02-other#Pressure]]

## Exit

- [[beat-01-skip]]
""",
    )
    beat1 = _page(
        "vault/episodes/009/beat-01-open.md",
        {"type": "beat", "beat_type": "hook"},
        "## Pressure\n\nx\n",
    )
    beat2 = _page(
        "vault/episodes/009/beat-02-other.md",
        {"type": "beat", "beat_type": "development"},
        "## Pressure\n\nx\n",
    )
    beat3 = _page(
        "vault/episodes/009/beat-01-skip.md",
        {"type": "beat", "beat_type": "development"},
        "## Pressure\n\nx\n",
    )
    corpus = _StubCorpus([first, second, beat1, beat2, beat3])
    assert list(registry()["W141"].check(first, corpus)) == []


def test_w141_retired_type_siblings_are_ignored() -> None:
    guide = _guide("vault/episodes/009/e09-run-guide-open.md", _WALK)
    moment = _page(
        "vault/episodes/009/moment-01-open.md",
        {"type": "moment", "engagement": "required"},
        "## What Happens\n\nx\n",
    )
    beat = _page(
        "vault/episodes/009/beat-01-skip.md",
        {"type": "beat", "beat_type": "development"},
        "## Pressure\n\nx\n",
    )
    fork = _page(
        "vault/episodes/009/fork-01-leave.md",
        {"type": "fork"},
        "## Paths\n\nx\n",
    )
    assert (
        list(registry()["W141"].check(guide, _StubCorpus([guide, moment, beat, fork])))
        == []
    )


def test_w141_session_008_is_silent() -> None:
    page = _guide("vault/episodes/008/run-guide.md", "## Now\n\nold\n")
    assert list(registry()["W141"].check(page, _StubCorpus())) == []
