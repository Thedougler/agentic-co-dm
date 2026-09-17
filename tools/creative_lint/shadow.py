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
    def metrics(self, rule_id: str) -> dict[str, float | int]:
        """Return audit-friendly agreement and repair measurements.

        Telemetry records may be annotated by a reviewer with ``agreement``,
        ``false_positive``, and ``repair_helpful`` booleans. Missing annotations
        are excluded rather than treated as negative evidence.
        """
        records = self.load(rule_id)
        reviewed = [record for record in records if any(key in record for key in
                    ("agreement", "false_positive", "repair_helpful"))]
        if not reviewed:
            return {"samples": len(records), "reviewed": 0, "agreement": 0.0,
                    "false_positive": 0.0, "repair_helpfulness": 0.0}

        def rate(key: str, *, invert: bool = False) -> float:
            values = [bool(record[key]) for record in reviewed if key in record]
            if not values:
                return 0.0
            numerator = sum((not value) if invert else value for value in values)
            return round(numerator / len(values), 4)

        return {
            "samples": len(records),
            "reviewed": len(reviewed),
            "agreement": rate("agreement"),
            "false_positive": rate("false_positive"),
            "repair_helpfulness": rate("repair_helpful"),
        }

    def promotion_ready(self, rule_id: str) -> bool:
        """Return whether measured telemetry clears the promotion thresholds."""
        metrics = self.metrics(rule_id)
        return (metrics["reviewed"] > 0 and metrics["agreement"] > 0.90
                and metrics["false_positive"] < 0.10)
