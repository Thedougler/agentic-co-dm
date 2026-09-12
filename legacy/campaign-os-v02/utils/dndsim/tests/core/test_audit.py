from __future__ import annotations

import json

from dndsim.core.audit import append_audit_line, build_audit_line, digest_report


def test_digest_report_is_deterministic_sha256() -> None:
    assert digest_report("hello") == digest_report("hello")
    assert digest_report("hello") != digest_report("hello world")
    assert len(digest_report("hello")) == 64


def test_build_audit_line_carries_all_fields() -> None:
    line = build_audit_line(
        engine_version="0.2.0",
        seed=42,
        argv=["sim-combat", "--seed", "42"],
        subject={"a": "Fighter", "b": "Goblin"},
        totals={"cells": 1, "universes": 1000, "wallMs": 12.3},
        cells=[{"index": 0, "winRate": 0.6}],
        report_text="# report",
    )
    payload = line.as_dict()
    assert payload["engineVersion"] == "0.2.0"
    assert payload["seed"] == 42
    assert payload["subject"] == {"a": "Fighter", "b": "Goblin"}
    assert payload["totals"]["cells"] == 1
    assert payload["cells"] == [{"index": 0, "winRate": 0.6}]
    assert payload["resultDigest"] == digest_report("# report")
    assert payload["schemaVersion"] == 1
    assert isinstance(payload["ts"], str) and payload["ts"]


def test_build_audit_line_without_report_text_has_no_digest() -> None:
    line = build_audit_line(engine_version="0.2.0", seed=1, argv=[], subject={}, totals={})
    assert line.as_dict()["resultDigest"] is None
    assert line.as_dict()["cells"] == []


def test_append_audit_line_writes_one_json_line_and_creates_file(tmp_path) -> None:  # type: ignore[no-untyped-def]
    path = tmp_path / "nested" / "dndsim-audit.jsonl"
    line = build_audit_line(engine_version="0.2.0", seed=1, argv=["x"], subject={}, totals={})
    append_audit_line(path, line)
    assert path.exists()
    lines = path.read_text().splitlines()
    assert len(lines) == 1
    assert json.loads(lines[0])["seed"] == 1


def test_append_audit_line_is_append_only() -> None:
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as d:
        path = Path(d) / "audit.jsonl"
        first = build_audit_line(engine_version="0.2.0", seed=1, argv=[], subject={}, totals={})
        second = build_audit_line(engine_version="0.2.0", seed=2, argv=[], subject={}, totals={})
        append_audit_line(path, first)
        append_audit_line(path, second)
        lines = path.read_text().splitlines()
        assert len(lines) == 2
        assert json.loads(lines[0])["seed"] == 1
        assert json.loads(lines[1])["seed"] == 2
