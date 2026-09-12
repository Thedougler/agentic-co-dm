"""`wiki.toml` [thresholds] accessors on `Config`."""

from __future__ import annotations

from wiki_cli.config import load_config


def test_threshold_returns_string():
    config = load_config()
    assert config.threshold("PAGE_PROSE_FLOOR") == "150"


def test_threshold_list_semicolons():
    config = load_config()
    assert "interview" in config.threshold_list("UNLINKED_MENTION_STOPLIST")


def test_threshold_list_pipes():
    config = load_config()
    assert "dm" in config.threshold_list("PLAY_CALLOUTS")


def test_threshold_missing_key_raises():
    config = load_config()
    try:
        config.threshold("NOT_A_REAL_THRESHOLD_KEY")
    except KeyError:
        return
    raise AssertionError("expected KeyError for a missing threshold key")


def test_fingerprint_includes_thresholds(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / ".git").mkdir()

    toml_a = tmp_path / "wiki.toml"
    toml_a.write_text('[thresholds]\nPAGE_PROSE_FLOOR = "150"\n', encoding="utf-8")
    fingerprint_a = load_config(tmp_path).fingerprint

    toml_a.write_text('[thresholds]\nPAGE_PROSE_FLOOR = "999"\n', encoding="utf-8")
    fingerprint_b = load_config(tmp_path).fingerprint

    assert fingerprint_a != fingerprint_b
