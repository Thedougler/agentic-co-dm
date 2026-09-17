"""Explicit, owned, expiring finding waivers."""
from __future__ import annotations

import datetime as dt
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

@dataclass(frozen=True, slots=True)
class Waiver:
    rule_id: str
    target: str
    reason: str
    owner: str
    granted: str
    expires: str

    @classmethod
    def from_mapping(cls, value: dict[str, Any]) -> "Waiver":
        required = ("rule_id", "target", "reason", "owner", "granted", "expires")
        missing = [key for key in required if not value.get(key)]
        if missing:
            raise ValueError(f"waiver missing required fields: {', '.join(missing)}")
        return cls(*(str(value[key]) for key in required))

    def expired(self, *, today: dt.date | None = None, session: int | None = None) -> bool:
        today = today or dt.date.today()
        expiry = self.expires.strip().lower()
        if expiry.startswith("session-"):
            try:
                return session is not None and session >= int(expiry.split("-", 1)[1])
            except ValueError:
                return False
        try:
            return today > dt.date.fromisoformat(expiry)
        except ValueError:
            return False

    def matches(self, finding: Any, *, today: dt.date | None = None, session: int | None = None) -> bool:
        if self.expired(today=today, session=session) or self.rule_id != finding.rule_id:
            return False
        target = self.target
        if target == "*":
            return True
        file_name = str((finding.location or {}).get("file", ""))
        if target.startswith("file:"):
            return file_name == target.removeprefix("file:")
        if target.startswith("npc:"):
            needle = target.removeprefix("npc:").casefold()
            return needle in file_name.casefold() or needle in str((finding.location or {}).get("text", "")).casefold()
        if target.startswith("session:"):
            needle = target.removeprefix("session:").casefold()
            return needle in file_name.casefold()
        return False

    def to_dict(self) -> dict[str, str]:
        return {"rule_id": self.rule_id, "target": self.target, "reason": self.reason,
                "owner": self.owner, "granted": self.granted, "expires": self.expires}


class WaiverRegistry:
    def __init__(self, waivers: list[Waiver]):
        self.waivers = waivers

    @classmethod
    def load(cls, path: str | Path) -> "WaiverRegistry":
        path = Path(path)
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise ValueError(f"could not load waivers {path}: {exc}") from exc
        if isinstance(raw, dict):
            raw = raw.get("waivers", [])
        if not isinstance(raw, list):
            raise ValueError("waivers must be a JSON array")
        return cls([Waiver.from_mapping(item) for item in raw])

    def match(self, finding: Any, *, today: dt.date | None = None, session: int | None = None) -> Waiver | None:
        return next((waiver for waiver in self.waivers if waiver.matches(finding, today=today, session=session)), None)

    def validate(self) -> list[str]:
        errors = []
        for index, waiver in enumerate(self.waivers):
            if not waiver.expires:
                errors.append(f"waiver {index} has no expiry")
        return errors
