"""W143 — new passage/moment/fork/sequence/dm-screen pages outside the
frozen episodes (001-008) and the episode 09 leftover set fail."""

from __future__ import annotations

from pathlib import Path

import wiki_cli.rules  # noqa: F401
from wiki_cli.contracts import Page, registry


class _StubCorpus:
    def __init__(self) -> None:
        self.repo_root = Path(".")


def _page(rel_path: str, page_type: str) -> Page:
    return Page(
        rel_path=rel_path,
        raw=f"---\ntype: {page_type}\n---\n\n# x\n",
        frontmatter={"type": page_type},
        body="# x\n",
        body_start_line=4,
    )


def _check(rel_path: str, page_type: str) -> list:
    return list(registry()["W143"].check(_page(rel_path, page_type), _StubCorpus()))


def test_w143_legacy_e09_beat_is_silent() -> None:
    assert _check("vault/episodes/009/beat-01-crown-cutter.md", "beat") == []


def test_w143_legacy_e09_passage_is_silent() -> None:
    assert _check("vault/episodes/009/passage-01-crossing-to-fathomrush.md", "passage") == []


def test_w143_new_episode_beat_is_legal() -> None:
    assert _check("vault/episodes/010/beat-01-new.md", "beat") == []


def test_w143_new_episode_passage_fails() -> None:
    findings = _check("vault/episodes/010/passage-01-new.md", "passage")
    assert len(findings) == 1
    assert "passage" in findings[0].message


def test_w143_template_is_silent() -> None:
    assert _check("vault/_templates/_episodes/_beat_hook.md", "beat") == []


def test_w143_new_episode_moment_fails() -> None:
    findings = _check("vault/episodes/010/moment-01-peak.md", "moment")
    assert len(findings) == 1
    assert "moment" in findings[0].message


def test_w143_new_episode_fork_fails() -> None:
    findings = _check("vault/episodes/010/fork-01-peak.md", "fork")
    assert len(findings) == 1
    assert "fork" in findings[0].message


def test_w143_new_episode_sequence_fails() -> None:
    findings = _check("vault/episodes/010/sequence-01-open.md", "sequence")
    assert len(findings) == 1
    assert "sequence" in findings[0].message


def test_w143_new_episode_dm_screen_fails() -> None:
    findings = _check("vault/episodes/010/dm-screen.md", "dm-screen")
    assert len(findings) == 1
    assert "dm-screen" in findings[0].message


def test_w143_passage_basename_wrong_type_fails() -> None:
    findings = _check("vault/episodes/010/passage-99-disguised.md", "moment")
    assert len(findings) == 1


def test_w143_frozen_episode_moment_is_silent() -> None:
    # Episodes 001-008 are played history — retired-type names/types never fire there.
    assert _check("vault/episodes/008/moment-01-peak.md", "moment") == []


def test_w143_frozen_episode_dm_screen_is_silent() -> None:
    assert _check("vault/episodes/008/dm-screen.md", "dm-screen") == []


def test_w143_legacy_e09_fork_is_silent() -> None:
    assert _check("vault/episodes/009/fork-01-the-heading-choice.md", "fork") == []


def test_w143_legacy_e09_moment_is_silent() -> None:
    assert _check("vault/episodes/009/moment-02-la-vasca-departure.md", "moment") == []


def test_w143_legacy_e09_sequence_is_silent() -> None:
    assert _check("vault/episodes/009/sequence-01-cold-open-aruhe.md", "sequence") == []
