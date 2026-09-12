"""``dndsim sweep-corpus`` / ``dndsim sweep-count`` — issue #53."""

from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

from dndsim.cli import app

runner = CliRunner()

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures"
NO_AUDIT = ["--no-audit-log"]


def _write_corpus(tmp_path: Path) -> Path:
    corpus_dir = tmp_path / "corpus"
    corpus_dir.mkdir()
    (corpus_dir / "weak.md").write_text(
        "```statblock\nname: Weak Foe\nac: 10\nhp: 4\nstats: [8, 8, 8, 8, 8, 8]\n"
        "actions:\n  - name: Slap\n    desc: 'Melee Weapon Attack: +2 to hit, "
        "reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage.'\n```\n"
    )
    (corpus_dir / "medium.md").write_text(
        "```statblock\nname: Medium Foe\nac: 13\nhp: 24\nstats: [14, 12, 14, 8, 10, 8]\n"
        "actions:\n  - name: Axe\n    desc: 'Melee Weapon Attack: +4 to hit, "
        "reach 5 ft., one target. Hit: 6 (1d8+2) slashing damage.'\n```\n"
    )
    return corpus_dir


def _write_subject(tmp_path: Path, name: str = "subject.md") -> Path:
    subject = tmp_path / name
    subject.write_text(
        "```statblock\nname: Subject Fighter\nac: 16\nhp: 40\nstats: [16, 14, 14, 10, 10, 10]\n"
        "actions:\n  - name: Longsword\n    desc: 'Melee Weapon Attack: +6 to hit, "
        "reach 5 ft., one target. Hit: 8 (1d8+4) slashing damage.'\n```\n"
    )
    return subject


def test_sweep_corpus_prints_markdown_table(tmp_path: Path) -> None:
    corpus_dir = _write_corpus(tmp_path)
    subject = _write_subject(tmp_path)
    result = runner.invoke(
        app,
        [
            "sweep-corpus",
            str(subject),
            "--corpus-dir",
            str(corpus_dir),
            "--seed",
            "1",
            "--universes",
            "200",
            *NO_AUDIT,
        ],
    )
    assert result.exit_code == 0, result.stdout
    assert "# Corpus sweep — Subject Fighter" in result.stdout
    assert "Weak Foe" in result.stdout
    assert "Medium Foe" in result.stdout


def test_sweep_corpus_out_option_writes_file(tmp_path: Path) -> None:
    corpus_dir = _write_corpus(tmp_path)
    subject = _write_subject(tmp_path)
    out_path = tmp_path / "report.md"
    result = runner.invoke(
        app,
        [
            "sweep-corpus",
            str(subject),
            "--corpus-dir",
            str(corpus_dir),
            "--seed",
            "1",
            "--universes",
            "200",
            "--out",
            str(out_path),
            *NO_AUDIT,
        ],
    )
    assert result.exit_code == 0, result.stdout
    assert out_path.exists()
    assert "# Corpus sweep" in out_path.read_text()


def test_sweep_corpus_party_keyword_chains_one_sweep_per_pc(tmp_path: Path) -> None:
    corpus_dir = _write_corpus(tmp_path)
    party_dir = tmp_path / "party"
    party_dir.mkdir()
    _write_subject(party_dir, "pc1-sheet.md")
    result = runner.invoke(
        app,
        [
            "sweep-corpus",
            "party",
            "--party-glob",
            str(party_dir / "*-sheet.md"),
            "--corpus-dir",
            str(corpus_dir),
            "--seed",
            "1",
            "--universes",
            "200",
            *NO_AUDIT,
        ],
    )
    assert result.exit_code == 0, result.stdout
    assert result.stdout.count("# Corpus sweep") == 1


def test_sweep_corpus_party_keyword_no_match_is_an_error(tmp_path: Path) -> None:
    result = runner.invoke(
        app,
        [
            "sweep-corpus",
            "party",
            "--party-glob",
            str(tmp_path / "nothing-matches-*.md"),
            *NO_AUDIT,
        ],
    )
    assert result.exit_code != 0


def test_sweep_corpus_writes_one_audit_line_by_default(tmp_path: Path) -> None:
    corpus_dir = _write_corpus(tmp_path)
    subject = _write_subject(tmp_path)
    log_path = tmp_path / "audit.jsonl"
    result = runner.invoke(
        app,
        [
            "sweep-corpus",
            str(subject),
            "--corpus-dir",
            str(corpus_dir),
            "--seed",
            "1",
            "--universes",
            "200",
            "--audit-log",
            str(log_path),
        ],
    )
    assert result.exit_code == 0, result.stdout
    lines = log_path.read_text().splitlines()
    assert len(lines) == 1
    payload = json.loads(lines[0])
    assert payload["seed"] == 1
    assert payload["totals"]["cells"] == 2


def test_sweep_count_prints_recommended_counts(tmp_path: Path) -> None:
    corpus_dir = _write_corpus(tmp_path)
    party = _write_subject(tmp_path)
    result = runner.invoke(
        app,
        [
            "sweep-count",
            str(party),
            str(corpus_dir / "weak.md"),
            "--seed",
            "1",
            "--universes",
            "200",
            "--min-count",
            "1",
            "--max-count",
            "3",
            *NO_AUDIT,
        ],
    )
    assert result.exit_code == 0, result.stdout
    assert "# Count sweep — Weak Foe" in result.stdout
    assert "Recommended count per band" in result.stdout
    assert "Count matrix" in result.stdout


def test_sweep_count_rejects_bad_range(tmp_path: Path) -> None:
    corpus_dir = _write_corpus(tmp_path)
    party = _write_subject(tmp_path)
    result = runner.invoke(
        app,
        [
            "sweep-count",
            str(party),
            str(corpus_dir / "weak.md"),
            "--min-count",
            "5",
            "--max-count",
            "2",
            *NO_AUDIT,
        ],
    )
    assert result.exit_code != 0


def test_sweep_count_writes_one_audit_line_by_default(tmp_path: Path) -> None:
    corpus_dir = _write_corpus(tmp_path)
    party = _write_subject(tmp_path)
    log_path = tmp_path / "audit.jsonl"
    result = runner.invoke(
        app,
        [
            "sweep-count",
            str(party),
            str(corpus_dir / "weak.md"),
            "--seed",
            "1",
            "--universes",
            "200",
            "--min-count",
            "1",
            "--max-count",
            "2",
            "--audit-log",
            str(log_path),
        ],
    )
    assert result.exit_code == 0, result.stdout
    lines = log_path.read_text().splitlines()
    assert len(lines) == 1
    payload = json.loads(lines[0])
    assert payload["seed"] == 1


def test_sim_combat_no_longer_accepts_cells_or_workers() -> None:
    result = runner.invoke(app, ["sim-combat", "--cells", "2", *NO_AUDIT])
    assert result.exit_code != 0
    result = runner.invoke(app, ["sim-combat", "--workers", "2", *NO_AUDIT])
    assert result.exit_code != 0
