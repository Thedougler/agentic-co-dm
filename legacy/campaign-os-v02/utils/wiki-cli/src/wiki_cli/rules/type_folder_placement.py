"""A `vault/**` page whose `type:` has a mapped home folder, that home
folder exists on disk, but the page sits outside every allowed prefix for
that type — ported from `utils/scripts/lint-rules/w95-type-folder-
placement.mjs` (rule id `W95`).

`vault/campaigns/**` is excluded, except `type: situation` and `type:
beat`: campaign-scoped mirrors of most types (a season-local NPC roster)
are a deliberate duplication, not drift, while Situation and Beat are
current campaign-prep homes with their own folders.
`vault/_templates/**` is excluded too (not in the legacy rule's own scope
check, but npm's `.obsidian-linter.jsonc` unconditionally ignores that
tree ahead of every custom rule — see `template_spine.py`'s LEGACY-BUG
note for the confirmed, empirical reason — so a real template such as
`_srd/_monster.md`, whose own `type: monster` sits outside
`vault/srd/monsters/`, never reaches npm's W95 either; this port adds the
same exclusion directly since wiki-cli has no equivalent ignore layer).
Unmapped types (no TYPE_HOME entry) never fire.

`TYPE_HOME` is not in `utils/scripts/lint-rules/config/thresholds.json`
(confirmed: no `TYPE_HOME` key there) — the legacy module's own
`DEFAULT_TYPE_HOME` constant is what actually governs on the real vault,
so it is reproduced here as a plain module constant rather than routed
through `config.threshold(...)`.
"""

from __future__ import annotations

from collections.abc import Iterable

from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_TYPE_HOME: dict[str, tuple[str, ...]] = {
    "npc": ("vault/campaigns/shattered-sea/npcs",),
    "location": ("vault/campaigns/shattered-sea/locations",),
    "item": ("vault/srd/items",),
    "spell": ("vault/srd/spells",),
    "monster": ("vault/srd/monsters",),
    "faction": ("vault/campaigns/shattered-sea/factions",),
    "quest": ("vault/campaigns/shattered-sea/quests",),
    "situation": ("vault/campaigns/shattered-sea/situations",),
    "beat": (
        "vault/campaigns/shattered-sea/beats",
        "vault/campaigns/shattered-sea/situations",
        "vault/episodes",
    ),
    "lore": ("vault/srd/lore",),
    "world": ("vault/worlds",),
    "species": ("vault/srd/species",),
    "class": ("vault/srd/classes",),
    "background": ("vault/srd/backgrounds",),
    "feat": ("vault/srd/feats",),
    "encounter": ("vault/campaigns/shattered-sea/encounters",),
    "deity": ("vault/campaigns/shattered-sea/deities",),
    "culture": ("vault/campaigns/shattered-sea/cultures",),
    "calendar": ("vault/campaigns/shattered-sea/lore",),
    "threat": ("vault/campaigns/shattered-sea/threats",),
    "condition": ("vault/srd/conditions",),
    "material": ("vault/srd/materials",),
    "profession": ("vault/srd/professions",),
    "document": ("vault/campaigns/shattered-sea/documents",),
    "route": ("vault/campaigns/shattered-sea/locations",),
    "secret": ("vault/campaigns/shattered-sea/secrets",),
    "ship": ("vault/campaigns/shattered-sea/vehicles",),
    "agent-guidance": ("vault/refs",),
}


@register
class TypeFolderPlacementRule(FileRule):
    """Ported from npm's W95 (`utils/scripts/lint-rules/w95-type-folder-placement.mjs`)."""

    id = "W95"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = (
        "Move this page under its type's home folder (named in the finding "
        "message), or correct type: if it's a typo."
    )
    producer = "wiki"
    pure = False
    """Depends on which home folders exist on disk, not just this file's own bytes."""
    version = "2"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        rel = page.rel_path
        if not rel.endswith(".md") or not rel.startswith("vault/"):
            return
        if rel.startswith("vault/_templates/"):
            return

        page_type = page.type
        if page_type is None:
            return
        if rel.startswith("vault/campaigns/") and page_type not in (
            "situation",
            "beat",
        ):
            return
        homes = _TYPE_HOME.get(page_type)
        if not homes:
            return

        existing_homes = [home for home in homes if (corpus.repo_root / home).is_dir()]
        if not existing_homes:
            return

        if any(rel.startswith(f"{home}/") for home in existing_homes):
            return

        yield self.finding(
            file=rel,
            line=page.body_start_line,
            message=(
                f"type: {page_type} lives outside its home — move this page under "
                f"{existing_homes[0]}/ (every inbound wikilink then needs "
                "cross-linker's sweep), or correct type: to what this folder holds; a "
                f"bare [[slug]] resolves by basename but an agent walking "
                f"{existing_homes[0]}/ never sees this page"
            ),
        )
