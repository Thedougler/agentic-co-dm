"""Fail-fast path-resolution check: `validate_paths` and its wiring into
`run_lint`.

`load_config()` resolves `vault_root`/`templates_root`/`scoped_roots`/
`cache_path` without checking they exist on disk — a missing `vault/` or
`vault/_templates/` would otherwise surface deep inside a producer with a
confusing error, or silently lint nothing. `validate_paths` closes that
gap; `run_lint` calls it before any producer work begins.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from wiki_cli.config import Config, ConfigError, validate_paths
from wiki_cli.orchestrator import run_lint


def _config(
    root: Path,
    *,
    vault_root: Path | None = None,
    templates_root: Path | None = None,
    cache_path: Path | None = None,
    scoped_roots: tuple[str, ...] = ("vault",),
) -> Config:
    return Config(
        repo_root=root,
        vault_root=vault_root if vault_root is not None else root / "vault",
        templates_root=(
            templates_root if templates_root is not None else root / "vault" / "_templates"
        ),
        cache_path=cache_path if cache_path is not None else root / ".wiki-cli" / "cache.sqlite3",
        scoped_roots=scoped_roots,
        report_cap=50,
        fingerprint="test-fingerprint",
        _thresholds={},
    )


def _make_valid_tree(root: Path) -> None:
    (root / "vault" / "_templates").mkdir(parents=True)
    (root / ".wiki-cli").mkdir(parents=True)


def test_validate_paths_passes_with_valid_config(tmp_path: Path):
    _make_valid_tree(tmp_path)
    validate_paths(_config(tmp_path))  # no raise


def test_missing_vault_root_raises(tmp_path: Path):
    _make_valid_tree(tmp_path)
    (tmp_path / "vault" / "_templates").rmdir()
    (tmp_path / "vault").rmdir()

    with pytest.raises(ConfigError) as excinfo:
        validate_paths(_config(tmp_path))
    assert "vault" in str(excinfo.value)
    assert "vault_root" in str(excinfo.value)


def test_missing_templates_root_raises(tmp_path: Path):
    (tmp_path / "vault").mkdir()
    (tmp_path / ".wiki-cli").mkdir()

    with pytest.raises(ConfigError) as excinfo:
        validate_paths(_config(tmp_path))
    assert "_templates" in str(excinfo.value)
    assert "templates_root" in str(excinfo.value)


def test_missing_scoped_root_raises(tmp_path: Path):
    _make_valid_tree(tmp_path)

    with pytest.raises(ConfigError) as excinfo:
        validate_paths(_config(tmp_path, scoped_roots=("vault", ".claude")))
    assert ".claude" in str(excinfo.value)
    assert "scoped_roots" in str(excinfo.value)


def test_missing_cache_parent_raises(tmp_path: Path):
    (tmp_path / "vault" / "_templates").mkdir(parents=True)

    with pytest.raises(ConfigError) as excinfo:
        validate_paths(_config(tmp_path, cache_path=tmp_path / "no-such-dir" / "cache.sqlite3"))
    assert "no-such-dir" in str(excinfo.value)
    assert "cache_path parent" in str(excinfo.value)


def test_run_lint_calls_validation_before_producers(tmp_path: Path):
    """`vault_root` is missing — `run_lint` must raise `ConfigError` before
    touching producers, corpus indexing, or the cache."""
    (tmp_path / ".wiki-cli").mkdir()
    config = _config(tmp_path)  # vault/ and vault/_templates/ never created

    with pytest.raises(ConfigError):
        run_lint(config, targets=[])
