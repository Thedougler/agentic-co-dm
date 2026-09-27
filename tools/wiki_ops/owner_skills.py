"""Frontmatter `type`/`kind` → owner skill and template path for lint issue lists."""
from __future__ import annotations

import re
from pathlib import Path

SKILLS = {
    "place": "place-design",
    "npc": "npc-design",
    "faction": "faction-design",
    "item": "item-design",
    "vehicle": "vehicle-design",
    "spell": "spell-design",
    "lore": "lore-design",
    "region": "region-design",
    "creature": "monster-design",
    "quest": "narrative-islands",
    "recap": "session-recap",
    "session-prep": "session-beats",
}
KIND_SKILLS = {
    "city": "city-design",
    "hook": "hook-beats",
    "development": "development-beats",
    "cliffhanger": "cliffhanger-beats",
    "climax": "climax-beats",
    "resolution": "resolution-beats",
    "session-plan": "session-beats",
    "encounter": "encounter-prep",
}

_TEMPLATE_FROM = re.compile(r"\s+from wiki/templates/[^\s;]+")


def _key(value: str) -> str:
    return (value or "").strip().strip("\"'").casefold()


def owner_skill(page_type: str, kind: str = "") -> str:
    """Return the owner skill for a campaign page type and kind, or empty."""
    return KIND_SKILLS.get(_key(kind), "") or SKILLS.get(_key(page_type), "")


def template_ref(filename: str) -> str:
    """Return wiki/templates/<file>.md for a resolved template filename."""
    name = Path(filename).name
    return f"wiki/templates/{name}" if name and name != "." else ""


def strip_template_ref(text: str) -> str:
    """Drop 'from wiki/templates/...' once the page-level template line owns it."""
    cleaned = _TEMPLATE_FROM.sub("", text)
    return re.sub(r"\s+\.", ".", cleaned).strip()


def prereq_lines(*, page_type: str = "", kind: str = "", skill: str = "", template: str = "") -> list[str]:
    """Read-before-edit lines printed before a dirty page's findings."""
    skill = skill or owner_skill(page_type, kind)
    lines: list[str] = []
    if skill:
        lines.append(f"Read the '{skill}' skill prior to editing.")
    if template:
        lines.append(f"Read {template} prior to editing.")
    return lines
