"""The command surface of ADR-0064: one command per job, one flag per
question an agent can actually answer.

- `wiki lint` is scoped, `wiki sweep` is the corpus (test_only_filter.py
  owns the scoping proof); the retired display filters are gone from
  `lint --help`
- `wiki drain` is the single debt surface: queue, `--over` triage, and the
  claim lease that `worklist`/`claims`/`release` used to spread over three
  commands
- `wiki explain RULE` prints that rule's guide page and exits 2 on an id
  no page documents
- `wiki debt accept` raises the floors and refuses without `--force`
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path

import pytest
from typer.testing import CliRunner

from wiki_cli import cli, db
from wiki_cli.cli import _guide_pages
from wiki_cli.contracts import Finding, Severity, Tier

runner = CliRunner()

_FILE_A = "vault/npcs/barnaby-rook.md"
_FILE_B = "vault/locations/the-open-midchain.md"


@dataclass(frozen=True)
class _StubConfig:
    """Only what `drain`/`explain`/`debt` read off a Config — the corpus
    pass itself is monkeypatched out, so no vault is needed."""

    repo_root: Path
    cache_path: Path


def _stub_config(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> _StubConfig:
    config = _StubConfig(repo_root=tmp_path, cache_path=tmp_path / "cache.db")
    monkeypatch.setattr(cli, "_load_config", lambda _command: config)
    monkeypatch.setattr(cli, "_git_root", lambda _repo_root: tmp_path)
    return config


def _finding(rule_id: str, *, file: str = _FILE_A) -> Finding:
    return Finding(
        rule_id=rule_id,
        file=file,
        line=1,
        message=f"{rule_id} fired",
        severity=Severity.WARNING,
        tier=Tier.CONTENT_SHAPE,
        producer="wiki",
    )


def _seed_cache(conn: sqlite3.Connection, rel_path: str, findings: list[Finding]) -> None:
    for finding in findings:
        db.set_cached(
            conn,
            rel_path=rel_path,
            content_hash="hash",
            rule_id=finding.rule_id,
            rule_version=1,
            config_fingerprint="fp",
            findings=[finding],
        )


# --- retired flags ---


def test_lint_help_names_no_retired_flag() -> None:
    result = runner.invoke(cli.app, ["lint", "--help"])
    assert result.exit_code == 0
    for retired in ("--severity", "--producer", "--ratchet-exit"):
        assert retired not in result.output


def test_retired_commands_are_gone() -> None:
    for retired in (["worklist"], ["claims"], ["release"], ["baseline", "over"]):
        assert runner.invoke(cli.app, retired).exit_code != 0


# --- drain ---


def test_drain_lists_the_queue_worst_first(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    config = _stub_config(monkeypatch, tmp_path)
    conn = db.connect(config.cache_path)
    _seed_cache(conn, _FILE_A, [_finding("W25"), _finding("W12")])
    _seed_cache(conn, _FILE_B, [_finding("W25", file=_FILE_B)])
    conn.close()

    result = runner.invoke(cli.app, ["drain"])

    assert result.exit_code == 0
    lines = result.output.splitlines()
    assert lines[0].startswith("DRAIN — cache ")
    assert lines[1].startswith(f"{_FILE_A}  2 findings")
    assert lines[2].startswith(f"{_FILE_B}  1 findings")


def test_drain_claim_release_and_claims_share_one_command(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    config = _stub_config(monkeypatch, tmp_path)
    conn = db.connect(config.cache_path)
    _seed_cache(conn, _FILE_A, [_finding("W25")])
    conn.close()

    claimed = runner.invoke(cli.app, ["drain", "--claim", "1", "--agent-id", "agent-7"])
    assert claimed.output.splitlines() == [_FILE_A]

    listed = runner.invoke(cli.app, ["drain", "--claims"])
    assert listed.output.splitlines()[0] == "CLAIMS — 1 active"
    assert _FILE_A in listed.output
    assert "agent-7" in listed.output

    released = runner.invoke(cli.app, ["drain", "--release", _FILE_A])
    assert released.output.strip() == f"released {_FILE_A}"
    assert runner.invoke(cli.app, ["drain", "--claims"]).output.strip() == "CLAIMS — none active"


def test_drain_release_all_clears_every_claim(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    config = _stub_config(monkeypatch, tmp_path)
    conn = db.connect(config.cache_path)
    _seed_cache(conn, _FILE_A, [_finding("W25")])
    _seed_cache(conn, _FILE_B, [_finding("W25", file=_FILE_B)])
    conn.close()

    runner.invoke(cli.app, ["drain", "--claim", "2"])
    result = runner.invoke(cli.app, ["drain", "--release-all"])

    assert result.output.strip() == "released 2 claim(s)"


def test_drain_rejects_two_modes_at_once(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _stub_config(monkeypatch, tmp_path)

    result = runner.invoke(cli.app, ["drain", "--over", "--claims"])

    assert result.exit_code == 2
    assert "at most one of" in result.output


def test_drain_over_is_the_triage_view(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    _stub_config(monkeypatch, tmp_path)
    monkeypatch.setattr(cli, "_full_sweep_findings", lambda _config: [_finding("W25")])

    result = runner.invoke(cli.app, ["drain", "--over"])

    assert result.exit_code == 0
    assert result.output.splitlines()[0] == "ratchet +1 over floor · 1 findings above floor"


# --- explain ---


def _write_guides(tmp_path: Path, names: list[str]) -> Path:
    guide_dir = tmp_path / "vault" / "refs" / "lint"
    guide_dir.mkdir(parents=True)
    for name in names:
        (guide_dir / name).write_text(f"# {name}\nbody\n", encoding="utf-8")
    return guide_dir


def test_guide_pages_matches_a_family_page_case_insensitively(tmp_path: Path) -> None:
    guide_dir = _write_guides(tmp_path, ["w86-vale-prose.md", "w22-w23-callouts.md", "w8.md"])

    assert [p.name for p in _guide_pages(guide_dir, "W86")] == ["w86-vale-prose.md"]
    assert [p.name for p in _guide_pages(guide_dir, "w23")] == ["w22-w23-callouts.md"]
    # A shorter id never borrows a longer one's page.
    assert [p.name for p in _guide_pages(guide_dir, "W8")] == ["w8.md"]


def test_explain_prints_the_guide_page(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    _stub_config(monkeypatch, tmp_path)
    _write_guides(tmp_path, ["w86-vale-prose.md"])

    result = runner.invoke(cli.app, ["explain", "w86"])

    assert result.exit_code == 0
    assert "# w86-vale-prose.md" in result.output


def test_explain_exits_2_listing_pages_for_an_unknown_rule(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _stub_config(monkeypatch, tmp_path)
    _write_guides(tmp_path, ["w86-vale-prose.md"])

    result = runner.invoke(cli.app, ["explain", "W999"])

    assert result.exit_code == 2
    assert "no guide page for 'W999'" in result.output
    assert "w86-vale-prose" in result.output


# --- debt ---


def test_debt_accept_refuses_without_force(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _stub_config(monkeypatch, tmp_path)
    monkeypatch.setattr(
        cli, "_full_sweep_findings", lambda _config: pytest.fail("no corpus pass without --force")
    )

    result = runner.invoke(cli.app, ["debt", "accept"])

    assert result.exit_code == 2
    assert "refusing without --force" in result.output


def test_debt_accept_raises_floors_to_live_counts(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _stub_config(monkeypatch, tmp_path)
    monkeypatch.setattr(
        cli, "_full_sweep_findings", lambda _config: [_finding("W25"), _finding("W25")]
    )

    result = runner.invoke(cli.app, ["debt", "accept", "--force"])

    assert result.exit_code == 0
    from wiki_cli.baseline import load_baseline

    assert load_baseline(tmp_path) == {_FILE_A: {"W25": 2}}
