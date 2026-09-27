"""Frontmatter `type` → owner skill for lint issue lists."""
from __future__ import annotations

_EXCEPTIONS = {
    "creature": "monster-design",
    "quest": "narrative-islands",
}
_DESIGN = frozenset(
    {"place", "npc", "faction", "item", "vehicle", "spell", "lore", "region"}
)


def owner_skill(page_type: str) -> str:
    """Return the owner skill for a campaign page type, or empty."""
    key = (page_type or "").strip().strip("\"'").casefold()
    if key in _EXCEPTIONS:
        return _EXCEPTIONS[key]
    if key in _DESIGN:
        return f"{key}-design"
    return ""
