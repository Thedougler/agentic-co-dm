"""TDD for the queue behind `wiki drain` (ADR-0042, ADR-0064): grouping
cached findings into a dispatch queue, and the claim/lease layer on top of
it.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

from wiki_cli import db
from wiki_cli.contracts import Finding, Severity, Tier
from wiki_cli.drain import build_queue, claim_top_n

_FINGERPRINT = "fp-test"


def _finding(
    rel_path: str,
    rule_id: str,
    *,
    producer: str = "wiki",
    severity: Severity = Severity.WARNING,
) -> Finding:
    return Finding(
        rule_id=rule_id,
        file=rel_path,
        line=1,
        message=f"{rule_id} fired",
        severity=severity,
        tier=Tier.CONTENT_SHAPE,
        producer=producer,
    )


def _seed(
    conn: sqlite3.Connection,
    rel_path: str,
    rule_id: str,
    findings: list[Finding],
    *,
    content_hash: str = "hash-1",
) -> None:
    db.set_cached(
        conn,
        rel_path=rel_path,
        content_hash=content_hash,
        rule_id=rule_id,
        rule_version="1",
        config_fingerprint=_FINGERPRINT,
        findings=findings,
    )


def test_drain_groups_by_file(tmp_path: Path) -> None:
    conn = db.connect(tmp_path / "cache.sqlite3")
    _seed(conn, "vault/a.md", "W1", [_finding("vault/a.md", "W1")])
    _seed(
        conn,
        "vault/b.md",
        "W1",
        [_finding("vault/b.md", "W1"), _finding("vault/b.md", "W1")],
    )
    _seed(
        conn,
        "vault/c.md",
        "W1",
        [_finding("vault/c.md", "W1") for _ in range(3)],
    )

    entries = build_queue(conn)

    assert [e.rel_path for e in entries] == ["vault/c.md", "vault/b.md", "vault/a.md"]
    assert [e.count for e in entries] == [3, 2, 1]


def test_drain_filters_by_rule_id_case_insensitively(tmp_path: Path) -> None:
    conn = db.connect(tmp_path / "cache.sqlite3")
    _seed(
        conn,
        "vault/a.md",
        "W1",
        [_finding("vault/a.md", "W1", producer="wiki")],
    )
    _seed(
        conn,
        "vault/b.md",
        "W2",
        [_finding("vault/b.md", "W2", producer="vale")],
    )

    entries = build_queue(conn, rules=["w2"])

    assert [e.rel_path for e in entries] == ["vault/b.md"]


def test_drain_claim_excludes_claimed(tmp_path: Path) -> None:
    db_path = tmp_path / "cache.sqlite3"
    conn_a = db.connect(db_path)
    _seed(conn_a, "vault/a.md", "W1", [_finding("vault/a.md", "W1") for _ in range(3)])
    _seed(conn_a, "vault/b.md", "W1", [_finding("vault/b.md", "W1") for _ in range(2)])
    _seed(conn_a, "vault/c.md", "W1", [_finding("vault/c.md", "W1")])

    claimed_first = claim_top_n(conn_a, 1, "agent-a", 1800)
    assert claimed_first == ["vault/a.md"]

    conn_b = db.connect(db_path)
    claimed_second = claim_top_n(conn_b, 3, "agent-b", 1800)

    assert "vault/a.md" not in claimed_second
    assert set(claimed_second) == {"vault/b.md", "vault/c.md"}


def test_drain_expired_ttl_frees_file(tmp_path: Path) -> None:
    db_path = tmp_path / "cache.sqlite3"
    conn_a = db.connect(db_path)
    _seed(conn_a, "vault/a.md", "W1", [_finding("vault/a.md", "W1")])

    claimed_first = claim_top_n(conn_a, 1, "agent-a", -10)
    assert claimed_first == ["vault/a.md"]

    conn_b = db.connect(db_path)
    claimed_second = claim_top_n(conn_b, 1, "agent-b", 1800)

    assert claimed_second == ["vault/a.md"]


def test_drain_limit(tmp_path: Path) -> None:
    conn = db.connect(tmp_path / "cache.sqlite3")
    for i in range(5):
        rel_path = f"vault/file-{i}.md"
        _seed(conn, rel_path, "W1", [_finding(rel_path, "W1") for _ in range(i + 1)])

    entries = build_queue(conn, limit=2)

    assert len(entries) == 2
    assert [e.rel_path for e in entries] == ["vault/file-4.md", "vault/file-3.md"]


def test_drain_path_glob_filter(tmp_path: Path) -> None:
    conn = db.connect(tmp_path / "cache.sqlite3")
    _seed(conn, "vault/npcs/a.md", "W1", [_finding("vault/npcs/a.md", "W1")])
    _seed(conn, "vault/locations/b.md", "W1", [_finding("vault/locations/b.md", "W1")])

    entries = build_queue(conn, path_glob="vault/npcs/*")

    assert [e.rel_path for e in entries] == ["vault/npcs/a.md"]
