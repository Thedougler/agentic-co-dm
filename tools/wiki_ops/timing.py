"""Command timing and efficiency trace helpers."""
from __future__ import annotations

import datetime as dt
import json
import time
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]


def now_ms() -> float:
    return time.monotonic() * 1000


def elapsed_ms(start: float) -> int:
    return int(time.monotonic() * 1000 - start)


def timing_payload(command: str, duration_ms: int, cache: dict[str, Any] | None = None) -> dict[str, Any]:
    payload: dict[str, Any] = {"command": command, "duration_ms": duration_ms}
    if cache is not None:
        payload["cache"] = {
            "hits": int(cache.get("hits", 0)),
            "misses": int(cache.get("misses", 0)),
            "vale_skipped": int(cache.get("vale_skipped", 0)),
        }
    return payload


def append_command_record(
    command: str,
    duration_ms: int,
    exit_code: int,
    cache: dict[str, Any] | None = None,
    trace_path: str | Path | None = None,
) -> None:
    try:
        cache = cache or {}
        record = {
            "record_kind": "command",
            "schema_version": 1,
            "command": command,
            "duration_ms": duration_ms,
            "cache_hits": int(cache.get("hits", 0)),
            "cache_misses": int(cache.get("misses", 0)),
            "vale_skipped": int(cache.get("vale_skipped", 0)),
            "exit": exit_code,
            "timestamp": dt.datetime.now(dt.timezone.utc).isoformat(),
        }
        path = Path(trace_path) if trace_path is not None else ROOT / ".local/efficiency/traces.jsonl"
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(record, sort_keys=True) + "\n")
    except Exception:
        return
