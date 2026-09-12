"""Append-only audit log — one JSON line per invocation (issue #50).

Every invocation that produces a reportable figure appends exactly one line
here recording the engine version, seed, arguments, subject, totals,
per-cell results, and a digest of the rendered report, so that any number
cited anywhere traces back to the run that produced it.
:func:`append_audit_line` is the sole I/O in this module; everything else is
a pure function so callers can unit-test line construction without touching
the filesystem.

dndsim keeps its own log at a single well-known path (issue #50).
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

SCHEMA_VERSION = 1


def digest_report(report_text: str) -> str:
    """SHA-256 hex digest of a rendered report's text."""
    return hashlib.sha256(report_text.encode("utf-8")).hexdigest()


@dataclass(frozen=True, slots=True)
class AuditLine:
    """One append-only audit record; :meth:`as_dict` is what gets serialized."""

    engine_version: str
    seed: int
    argv: list[str]
    subject: dict[str, Any]
    totals: dict[str, Any]
    cells: list[dict[str, Any]] = field(default_factory=list)
    result_digest: str | None = None
    ts: str = field(default_factory=lambda: datetime.now(UTC).isoformat())
    schema_version: int = SCHEMA_VERSION

    def as_dict(self) -> dict[str, Any]:
        return {
            "schemaVersion": self.schema_version,
            "ts": self.ts,
            "engineVersion": self.engine_version,
            "argv": self.argv,
            "seed": self.seed,
            "subject": self.subject,
            "totals": self.totals,
            "cells": self.cells,
            "resultDigest": self.result_digest,
        }


def build_audit_line(
    *,
    engine_version: str,
    seed: int,
    argv: list[str],
    subject: dict[str, Any],
    totals: dict[str, Any],
    cells: list[dict[str, Any]] | None = None,
    report_text: str | None = None,
) -> AuditLine:
    """Pure builder for one audit line.

    ``report_text``, if given, is digested (SHA-256) and never stored raw —
    the log stays compact regardless of report size.
    """
    return AuditLine(
        engine_version=engine_version,
        seed=seed,
        argv=argv,
        subject=subject,
        totals=totals,
        cells=cells if cells is not None else [],
        result_digest=None if report_text is None else digest_report(report_text),
    )


def append_audit_line(path: Path, line: AuditLine) -> None:
    """Append ``line`` as one JSON line to ``path``, creating it if absent.

    O(1) per call — never reads the existing file, so appending never
    becomes O(file size) as the log grows.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(line.as_dict()) + "\n")
