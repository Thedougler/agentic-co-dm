"""Additive page identity transitions for .manifest.json."""
from __future__ import annotations

import datetime as dt
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

@dataclass(frozen=True)
class ManifestTransition:
    page_path: str
    transition: str
    target: str | None = None
    reason: str | None = None
    timestamp: str | None = None

    def validate(self) -> None:
        if not self.page_path or Path(self.page_path).is_absolute():
            raise ValueError("page_path must be vault-relative")
        if self.transition not in {"merged_into", "renamed_to", "archived"}:
            raise ValueError(f"invalid identity transition: {self.transition}")
        if self.transition in {"merged_into", "renamed_to"} and not self.target:
            raise ValueError(f"{self.transition} requires target")

    def to_dict(self) -> dict[str, Any]:
        return {key: value for key, value in asdict(self).items() if value is not None}


def apply_transition(data: dict[str, Any], transition: ManifestTransition) -> dict[str, Any]:
    transition.validate()
    out = json.loads(json.dumps(data))
    rows = out.setdefault("page_identity_transitions", [])
    if not isinstance(rows, list):
        raise ValueError("manifest page_identity_transitions must be a list")
    item = transition.to_dict()
    item.setdefault("timestamp", dt.datetime.now(dt.timezone.utc).isoformat())
    if item not in rows:
        rows.append(item)
    out["last_updated"] = item["timestamp"]
    return out


def update_manifest(path: str | Path, transition: ManifestTransition) -> dict[str, Any]:
    target = Path(path)
    data = json.loads(target.read_text(encoding="utf-8"))
    out = apply_transition(data, transition)
    temporary = target.with_suffix(target.suffix + ".tmp")
    temporary.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temporary.replace(target)
    return out
