"""Pydantic models for per-type frontmatter validation.

One model per content type (~30 types). Each model inherits `BaseFrontmatter`
which validates fields shared across all types (status, publish, tier, etc.).

All models use `extra='allow'` so unknown additional fields do not produce
false positives — W84 covers unknown-key detection. Optional fields default to
`None` so a page that omits them does not fail validation; only a field that IS
present with an invalid value (wrong enum member, wrong Python type) raises a
`ValidationError`.
"""

from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class _Status(StrEnum):
    DRAFT = "draft"
    PENDING = "pending"
    CANON = "canon"
    SRD = "srd"
    RETIRED = "retired"
    ACTIVE = "active"
    COMPLETE = "complete"


class _Tier(StrEnum):
    CORE = "core"
    SUPPORTING = "supporting"
    PERIPHERAL = "peripheral"


class BaseFrontmatter(BaseModel):
    """Shared governed fields present on every typed page."""

    model_config = ConfigDict(extra="allow", strict=False)

    type: str | None = None
    status: _Status | None = None
    publish: bool | None = None
    tier: _Tier | None = None
    aliases: list | None = None
    tags: list | None = None


# ---------------------------------------------------------------------------
# Campaign types
# ---------------------------------------------------------------------------


class _NpcSubtype(StrEnum):
    MAJOR = "major"
    MINOR = "minor"
    RECURRING = "recurring"


class NpcFrontmatter(BaseFrontmatter):
    subtype: _NpcSubtype | None = None


class _LocationSubtype(StrEnum):
    BUILDING = "building"
    PLANE = "plane"
    DUNGEON = "dungeon"
    SETTLEMENT = "settlement"
    REGION = "region"
    SHOP = "shop"


class LocationFrontmatter(BaseFrontmatter):
    subtype: _LocationSubtype | None = None


class _EventSubtype(StrEnum):
    GENERAL = "general"
    BATTLE = "battle"
    DISASTER = "disaster"
    ARRIVAL = "arrival"
    FESTIVAL = "festival"
    NEGOTIATION = "negotiation"
    RITUAL = "ritual"
    DISAPPEARANCE = "disappearance"
    WAR = "war"


class EventFrontmatter(BaseFrontmatter):
    subtype: _EventSubtype | None = None


class _SecretSubtype(StrEnum):
    CACHE = "cache"


class SecretFrontmatter(BaseFrontmatter):
    subtype: _SecretSubtype | None = None


class _CampaignSubtype(StrEnum):
    ONGOING = "ongoing"
    ONE_SHOT = "one-shot"


class CampaignFrontmatter(BaseFrontmatter):
    subtype: _CampaignSubtype | None = None


class _CultureSubtype(StrEnum):
    LANGUAGE = "language"


class CultureFrontmatter(BaseFrontmatter):
    subtype: _CultureSubtype | None = None


class _LoreSubtype(StrEnum):
    FACT = "fact"
    LEGEND = "legend"
    RUMOUR = "rumour"


class LoreFrontmatter(BaseFrontmatter):
    subtype: _LoreSubtype | None = None


class _ReferenceSubtype(StrEnum):
    PLAYER_GRAVITY = "player-gravity"
    PARTY_ITEMS = "party-items"
    THREADS = "threads"
    SPOILERS = "spoilers"


class ReferenceFrontmatter(BaseFrontmatter):
    subtype: _ReferenceSubtype | None = None


class _WorldSubtype(StrEnum):
    ORIGINAL = "original"
    PUBLISHED = "published"
    HYBRID = "hybrid"


class WorldFrontmatter(BaseFrontmatter):
    subtype: _WorldSubtype | None = None


# pc subtypes: optional character-sheet / combat-profile pages
class _PcSubtype(StrEnum):
    COMBAT_PROFILE = "combat-profile"
    CHARACTER_SHEET = "character-sheet"
    PARTY_COMBAT_PROFILE = "party-combat-profile"


class PcFrontmatter(BaseFrontmatter):
    subtype: _PcSubtype | None = None


class _SessionSubtype(StrEnum):
    HIGHLIGHTS = "highlights"
    INGEST_REVIEW = "ingest-review"
    INDEX = "index"
    OVERVIEW = "overview"
    RECAP = "recap"
    RUN_GUIDE = "run-guide"


class SessionFrontmatter(BaseFrontmatter):
    subtype: _SessionSubtype | None = None


# ---------------------------------------------------------------------------
# SRD types
# ---------------------------------------------------------------------------


class _SpellSubtype(StrEnum):
    ABJURATION = "abjuration"
    CONJURATION = "conjuration"
    DIVINATION = "divination"
    ENCHANTMENT = "enchantment"
    EVOCATION = "evocation"
    ILLUSION = "illusion"
    NECROMANCY = "necromancy"
    TRANSMUTATION = "transmutation"


class SpellFrontmatter(BaseFrontmatter):
    subtype: _SpellSubtype | None = None


class _RuleSubtype(StrEnum):
    CLASS = "class"
    SUBCLASS = "subclass"
    BACKGROUND = "background"
    CONDITION = "condition"
    SUBSYSTEM = "subsystem"
    SPELL = "spell"
    FEAT = "feat"
    SPECIES = "species"


class RuleFrontmatter(BaseFrontmatter):
    subtype: _RuleSubtype | None = None


class _PuzzleSubtype(StrEnum):
    PUZZLE = "puzzle"
    TRAP = "trap"
    HAZARD = "hazard"
    TRIAL = "trial"
    COMPOSITE = "composite"


class PuzzleFrontmatter(BaseFrontmatter):
    subtype: _PuzzleSubtype | None = None


class _ShipTier(StrEnum):
    """Ship tier uses integer strings 1-4, not the standard core/supporting/peripheral scale."""

    T1 = "1"
    T2 = "2"
    T3 = "3"
    T4 = "4"


class ShipFrontmatter(BaseFrontmatter):
    """Ship pages use a different `tier` scale (1–4) from every other type."""

    model_config = ConfigDict(extra="allow", strict=False)
    # Override base tier with ship-specific integer-string tier
    tier: _ShipTier | None = None  # type: ignore[assignment]


# ---------------------------------------------------------------------------
# Registry: type string -> model class
# ---------------------------------------------------------------------------

#: Types that carry no subtype constraint beyond the base model.
_BASE_ONLY_TYPES = frozenset(
    {
        "agent-guidance",
        "background",
        "beat",
        "calendar",
        "class",
        "condition",
        "craft",
        "deity",
        "dm-screen",
        "document",
        "encounter",
        "faction",
        "feat",
        "fork",
        "guide",
        "handout",
        "humanoid",
        "idea",
        "interview",
        "item",
        "material",
        "moment",
        "monster",
        "passage",
        "pc-abilities",
        "pc-gallery",
        "pc-inventory",
        "pc-spells",
        "pc-stats",
        "player",
        "profession",
        "quest",
        "route",
        "runbook",
        "season",
        "session-log",
        "species",
        "statblock",
        "story",
        "subclass",
        "table",
        "threat",
        "pc",
    }
)

_REGISTRY: dict[str, type[BaseFrontmatter]] = {
    "npc": NpcFrontmatter,
    "location": LocationFrontmatter,
    "event": EventFrontmatter,
    "secret": SecretFrontmatter,
    "campaign": CampaignFrontmatter,
    "culture": CultureFrontmatter,
    "lore": LoreFrontmatter,
    "reference": ReferenceFrontmatter,
    "world": WorldFrontmatter,
    "pc": PcFrontmatter,
    "session": SessionFrontmatter,
    "spell": SpellFrontmatter,
    "rule": RuleFrontmatter,
    "puzzle": PuzzleFrontmatter,
    "ship": ShipFrontmatter,
}

for _t in _BASE_ONLY_TYPES:
    _REGISTRY.setdefault(_t, BaseFrontmatter)


def model_for(page_type: str) -> type[BaseFrontmatter] | None:
    """Return the Pydantic model class for a content type, or None for unknown types."""
    return _REGISTRY.get(page_type)
