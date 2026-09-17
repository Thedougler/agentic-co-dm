"""Append-only telemetry for rules in SHADOW lifecycle."""
from __future__ import annotations

import datetime as dt
import json
from pathlib import Path
from typing import Iterable, Any

from .finding import Finding


class ShadowRecorder:
    def __init__(self, directory: str | Path):
        self.directory = Path(directory)

    def record(self, findings: Iterable[Finding], *, run_id: str | None = None) -> list[Path]:
        self.directory.mkdir(parents=True, exist_ok=True)
        written: list[Path] = []
        timestamp = dt.datetime.now(dt.timezone.utc).isoformat()
        for finding in findings:
            path = self.directory / f"{finding.rule_id}.jsonl"
            payload = {"timestamp": timestamp, "run_id": run_id, **finding.to_dict()}
            with path.open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(payload, sort_keys=True) + "\n")
            written.append(path)
        return written

    def load(self, rule_id: str) -> list[dict[str, Any]]:
        path = self.directory / f"{rule_id}.jsonl"
        if not path.is_file():
            return []
        records = []
        for line in path.read_text(encoding="utf-8").splitlines():
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                continue
        return records
