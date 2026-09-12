"""W147 — duplicate uid: detection.

Covers both cases: (a) two pages sharing a uid, (b) a page carrying a
template's uid. Uses in-memory Page objects and a minimal Corpus stub.
"""

from __future__ import annotations

from pathlib import Path
from typing import Sequence

import wiki_cli.rules  # noqa: F401  side-effect: registers every rule
from wiki_cli.contracts import Finding, Page, Severity, registry


class _StubCorpus:
    """Minimal Corpus implementation for VaultRule tests."""

    def __init__(self, pages: list[Page]) -> None:
        self._pages = pages
        self.repo_root = Path(".")

    def pages(self) -> Sequence[Page]:
        return self._pages

    def resolve(self, name: str) -> Page | None:
        return None

    def by_type(self, page_type: str) -> Sequence[Page]:
        return [p for p in self._pages if p.type == page_type]

    def links_from(self, rel_path: str) -> Sequence[str]:
        return []

    def links_to(self, rel_path: str) -> Sequence[str]:
        return []


def _page(rel_path: str, uid: str | None) -> Page:
    fm: dict[str, object] = {"type": "location", "status": "draft"}
    fm_lines: dict[str, int] = {"type": 1, "status": 2}
    if uid is not None:
        fm["uid"] = uid
        fm_lines["uid"] = 3
    return Page(
        rel_path=rel_path,
        raw="",
        frontmatter=fm,
        body="# Title\n",
        body_start_line=len(fm) + 2,
        frontmatter_lines=fm_lines,
    )


def _run(pages: list[Page]) -> list[Finding]:
    rule = registry()["W147"]
    corpus = _StubCorpus(pages)
    return list(rule.check(corpus))


# --- Case (a): two pages share the same uid --------------------------------


def test_duplicate_uid_fires() -> None:
    findings = _run([
        _page("vault/places/alpha.md", "aaaa-1111"),
        _page("vault/places/beta.md", "aaaa-1111"),
    ])
    assert len(findings) == 2
    assert all(f.rule_id == "W147" for f in findings)
    assert all(f.severity is Severity.ERROR for f in findings)
    assert "is shared with" in findings[0].message


def test_unique_uids_stay_silent() -> None:
    findings = _run([
        _page("vault/places/alpha.md", "aaaa-1111"),
        _page("vault/places/beta.md", "bbbb-2222"),
    ])
    assert findings == []


def test_missing_uid_stays_silent() -> None:
    findings = _run([
        _page("vault/places/alpha.md", None),
        _page("vault/places/beta.md", None),
    ])
    assert findings == []


# --- Case (b): page uid matches a template uid -----------------------------


def test_template_uid_match_fires() -> None:
    findings = _run([
        _page("vault/_templates/_location.md", "tmpl-uid-1"),
        _page("vault/places/gamma.md", "tmpl-uid-1"),
    ])
    # The page should fire; the template itself should not.
    page_findings = [f for f in findings if f.file == "vault/places/gamma.md"]
    template_findings = [f for f in findings if f.file.startswith("vault/_templates/")]
    assert len(page_findings) == 1
    assert "matches template" in page_findings[0].message
    assert template_findings == []


def test_template_uid_no_match_stays_silent() -> None:
    findings = _run([
        _page("vault/_templates/_location.md", "tmpl-uid-1"),
        _page("vault/places/gamma.md", "different-uid"),
    ])
    assert findings == []


# --- Both cases at once ----------------------------------------------------


def test_duplicate_and_template_match_both_fire() -> None:
    """Two pages share a uid AND that uid is also a template uid."""
    findings = _run([
        _page("vault/_templates/_location.md", "shared-tmpl"),
        _page("vault/places/alpha.md", "shared-tmpl"),
        _page("vault/places/beta.md", "shared-tmpl"),
    ])
    alpha = [f for f in findings if f.file == "vault/places/alpha.md"]
    beta = [f for f in findings if f.file == "vault/places/beta.md"]
    # Each page gets a duplicate finding AND a template-match finding.
    assert len(alpha) == 2
    assert len(beta) == 2
    messages = {f.message.split(" — ")[1] for f in alpha}
    assert "each page must have a globally unique uid" in messages
    assert any("copied from the template" in m for m in messages)
