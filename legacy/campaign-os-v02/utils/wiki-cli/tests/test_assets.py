"""TDD for the five asset rules ported from the npm engine (ADR-0042):
w-art-assets-organized, w-audio-assets-organized, w-orphan-art-assets
(all `VaultRule`, judging the whole corpus/filesystem at once) and
w-art-asset-linked, w-audio-asset-linked (`FileRule`, judging one page's
sibling assets). None carry a W-number — they keep their legacy slug ids
(Global Constraints, "Rule IDs").

Every fixture asset is a real placeholder file on disk under
`tests/fixtures/assets/vault/` — the two "organized"/orphan rules walk the
real filesystem directly (`corpus.repo_root`), not the page index, so a
fixture with no real file on disk would silently pass for the wrong reason.
"""

from __future__ import annotations

from pathlib import Path

import wiki_cli.rules  # noqa: F401  import-for-side-effect: registers every rule
from wiki_cli.contracts import registry
from wiki_cli.index import VaultIndex

FIXTURES = Path(__file__).parent / "fixtures" / "assets"

_CORPUS = None


def _corpus():
    global _CORPUS
    if _CORPUS is None:
        _CORPUS = VaultIndex.build(FIXTURES, FIXTURES / "vault", ("vault",))
    return _CORPUS


def check_vault(rule_id: str):
    rule = registry()[rule_id]
    return list(rule.check(_corpus()))


def check_file(rule_id: str, rel_path: str):
    rule = registry()[rule_id]
    corpus = _corpus()
    page = next(p for p in corpus.pages() if p.rel_path == rel_path)
    return list(rule.check(page, corpus))


# --- w-art-assets-organized -----------------------------------------------


def test_loose_image_outside_assets_fires():
    findings = check_vault("w-art-assets-organized")
    files = {f.file for f in findings}

    assert "vault/loose-image.png" in files
    assert all(f.rule_id == "w-art-assets-organized" for f in findings)


def test_organized_images_never_flagged():
    findings = check_vault("w-art-assets-organized")
    files = {f.file for f in findings}

    assert not any(f.startswith("vault/_assets/") for f in files)


def test_hidden_dir_images_never_flagged():
    findings = check_vault("w-art-assets-organized")
    files = {f.file for f in findings}

    assert "vault/.claude/skills/foo/icon.png" not in files


def test_audio_pipeline_subtree_images_never_flagged():
    findings = check_vault("w-art-assets-organized")
    files = {f.file for f in findings}

    assert "vault/episodes/01/audio/raw-photo.png" not in files


# --- w-audio-assets-organized ----------------------------------------------


def test_loose_audio_outside_assets_fires():
    findings = check_vault("w-audio-assets-organized")
    files = {f.file for f in findings}

    assert "vault/loose-clip.mp3" in files
    assert all(f.rule_id == "w-audio-assets-organized" for f in findings)


def test_organized_audio_never_flagged():
    findings = check_vault("w-audio-assets-organized")
    files = {f.file for f in findings}

    assert not any(f.startswith("vault/_assets/") for f in files)


# --- w-orphan-art-assets ----------------------------------------------------


def test_orphan_banner_fires():
    findings = check_vault("w-orphan-art-assets")
    files = {f.file for f in findings}

    assert "vault/_assets/banners/orphan-banner.png" in files


def test_orphan_portrait_fires():
    findings = check_vault("w-orphan-art-assets")
    files = {f.file for f in findings}

    assert "vault/_assets/portraits/orphan-portrait.jpg" in files


def test_owned_banner_not_orphaned():
    findings = check_vault("w-orphan-art-assets")
    files = {f.file for f in findings}

    assert "vault/_assets/banners/hero-banner.png" not in files
    assert "vault/_assets/banners/villain-banner.png" not in files


# --- w-art-asset-linked ------------------------------------------------


def test_embedded_banner_stays_silent():
    assert check_file("w-art-asset-linked", "vault/pages/hero.md") == []


def test_unembedded_sibling_banner_fires():
    findings = check_file("w-art-asset-linked", "vault/pages/villain.md")

    assert len(findings) == 1
    assert findings[0].rule_id == "w-art-asset-linked"
    assert findings[0].file == "vault/pages/villain.md"


def test_leaflet_image_param_counts_as_embedded():
    assert check_file("w-art-asset-linked", "vault/pages/mapper.md") == []


def test_more_specific_owner_excludes_shorter_slug():
    # "villain-quarters-map.png" prefix-matches both "villain" and
    # "villain-quarters" — only the longer (more specific) slug owns it.
    assert check_file("w-art-asset-linked", "vault/pages/villain-quarters.md") != []
    villain_findings = check_file("w-art-asset-linked", "vault/pages/villain.md")
    assert all("villain-quarters-map" not in f.message for f in villain_findings)


# --- w-audio-asset-linked ----------------------------------------------


def test_unembedded_sibling_audio_fires():
    findings = check_file("w-audio-asset-linked", "vault/pages/singer.md")

    assert len(findings) == 1
    assert findings[0].rule_id == "w-audio-asset-linked"


def test_embedded_sibling_audio_stays_silent():
    assert check_file("w-audio-asset-linked", "vault/pages/singer-ok.md") == []
