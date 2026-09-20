"""Command timing and efficiency trace helpers."""
from __future__ import annotations

import datetime as dt
import json
import sys
import threading
import time
from collections.abc import Callable
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]

HEARTBEAT_INTERVAL_S = 10.0


class ProgressHeartbeat:
    """Stderr liveness line at least every `interval` seconds."""

    def __init__(
        self,
        command: str,
        interval: float = HEARTBEAT_INTERVAL_S,
        *,
        emit: Callable[[str], None] | None = None,
    ) -> None:
        self.command = command
        self.interval = interval
        self._emit = emit or (lambda line: print(line, file=sys.stderr, flush=True))
        self._stop = threading.Event()
        self._thread: threading.Thread | None = None
        self._start = 0.0

    def __enter__(self) -> ProgressHeartbeat:
        self._start = time.monotonic()
        if self.interval > 0:
            self._thread = threading.Thread(
                target=self._run,
                name=f"wiki-heartbeat-{self.command}",
                daemon=True,
            )
            self._thread.start()
        return self

    def _run(self) -> None:
        while not self._stop.wait(self.interval):
            elapsed_s = int(time.monotonic() - self._start)
            self._emit(f"wiki {self.command}: elapsed_s={elapsed_s} still=1")

    def __exit__(self, *exc: object) -> None:
        self._stop.set()
        if self._thread is not None:
            self._thread.join(timeout=1.0)


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
    extra: dict[str, Any] | None = None,
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
        if extra:
            record.update(extra)
        path = Path(trace_path) if trace_path is not None else ROOT / ".local/efficiency/traces.jsonl"
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(record, sort_keys=True) + "\n")
    except Exception:
        return
