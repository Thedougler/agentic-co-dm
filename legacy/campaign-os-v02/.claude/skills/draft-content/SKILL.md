---
name: draft-content
description: >-
  Route a wiki page to its drafting guide in a Campaign OS repo. Use the moment you're about
  to create or expand any page under vault/ — a world, campaign, season, NPC, location,
  faction, item, quest, situation, creature, encounter, ship, lore, rule, table, handout,
  species, deity, culture, calendar, threat, condition, document, material, profession,
  route, secret, class, or spell page. Not a status: canon page (canon-review) or a transcript
  (transcript-ingest).
---

# Draft Content

Pure dispatch. Writes nothing itself, and never substitutes for the guide it
routes to -> authoring a page from this file alone is a `vault/CLAUDE.md`
rule 4 violation (freeform page).

## Workflow

1. **Match the page's path** to one row below.
   `DC1: <path matched, or none>`.
2. **Chain-load the guide** — your next tool call is Read on the row's
   target (the Read tool itself, no acting tool call beside it) — then
   follow it, including every file its own "Read first" step names.
   `DC2: <guide read, its Read-first files read>`.
3. **No row matches** — a genuinely new content type -> chain-load
   `content-type-scaffold` instead; it creates the `_templates/<type>.md`
   and `.claude/skills/draft-content/references/<type>.md` pair, then this table gains a
   row. `DC3: <matched, or scaffold chain-loaded>`.

The page lives (or will live) at one path shape below. A type whose folder
does not exist yet is still routed here -> the folder is born with its first
page.

| Page path | Guide |
|---|---|
| `vault/campaigns/shattered-sea/npcs/<slug>.md` | `.claude/skills/draft-content/references/npc.md` |
| `vault/campaigns/shattered-sea/vehicles/<slug>.md` | `.claude/skills/draft-content/references/ship.md` |
| `vault/campaigns/shattered-sea/locations/<slug>.md` | `.claude/skills/draft-content/references/location.md` |
| `vault/campaigns/shattered-sea/factions/<slug>.md` | `.claude/skills/draft-content/references/faction.md` |
| `vault/campaigns/shattered-sea/items/<slug>.md` | `.claude/skills/draft-content/references/item.md` |
| `vault/campaigns/shattered-sea/monsters/<slug>.md` | `.claude/skills/draft-content/references/monster.md` |
| `vault/campaigns/shattered-sea/quests/<slug>.md` | `.claude/skills/draft-content/references/quest.md` |
| `vault/campaigns/*/situations/<slug>.md` | `.claude/skills/draft-content/references/situation.md` |
| `vault/campaigns/shattered-sea/encounters/<slug>.md` | `.claude/skills/encounter-prep/SKILL.md` |
| `vault/campaigns/shattered-sea/lore/<slug>.md` (subtype: fact/legend) | `.claude/skills/draft-content/references/lore.md` |
| `vault/campaigns/shattered-sea/lore/<slug>.md` (subtype: rumour) | `vault/refs/vault/lore/references/rumour.md` |
| `vault/srd/rules/<slug>.md` | `.claude/skills/rule-prep/SKILL.md` |
| `vault/worlds/<slug>.md` | `.claude/skills/draft-content/references/world.md` |
| `vault/campaigns/<slug>.md` | `.claude/skills/draft-content/references/campaign.md` |
| `vault/campaigns/shattered-sea/seasons/<slug>.md` | `.claude/skills/draft-content/references/season.md` |
| `vault/refs/tables/<slug>.md` | `.claude/skills/draft-content/references/table.md` |
| `vault/campaigns/shattered-sea/handouts/<slug>.md` | `.claude/skills/draft-content/references/handout.md` |
| `vault/campaigns/shattered-sea/puzzles/<slug>.md` | `.claude/skills/draft-content/references/puzzle.md` |
| `vault/campaigns/shattered-sea/secrets/<slug>.md` | `.claude/skills/draft-content/references/secret.md` |
| `vault/srd/classes/<slug>.md` | `.claude/skills/draft-content/references/class.md` |
| `vault/srd/spells/<slug>.md` | `.claude/skills/draft-content/references/spell.md` |
| `vault/srd/backgrounds/<slug>.md` | `.claude/skills/draft-content/references/background.md` |
| `vault/srd/feats/<slug>.md` | `.claude/skills/draft-content/references/feat.md` |
| `vault/campaigns/shattered-sea/species/<slug>.md` | `.claude/skills/draft-content/references/species.md` |
| `vault/campaigns/shattered-sea/events/<slug>.md` | `.claude/skills/draft-content/references/event.md` |
| `vault/campaigns/shattered-sea/deities/<slug>.md` | `.claude/skills/draft-content/references/deity.md` |
| `vault/campaigns/shattered-sea/cultures/<slug>.md` | `.claude/skills/draft-content/references/culture.md` |
| `vault/campaigns/shattered-sea/lore/<slug>.md` (type: calendar) | `.claude/skills/draft-content/references/calendar.md` |
| `vault/campaigns/shattered-sea/threats/<slug>.md` | `.claude/skills/draft-content/references/threat.md` |
| `vault/campaigns/shattered-sea/documents/<slug>.md` | `.claude/skills/draft-content/references/document.md` |
| `vault/campaigns/shattered-sea/locations/<slug>.md` (type: route) | `.claude/skills/draft-content/references/route.md` |
| `vault/srd/conditions/<slug>.md` | `.claude/skills/draft-content/references/condition.md` |
| `vault/srd/materials/<slug>.md` | `.claude/skills/draft-content/references/material.md` |
| `vault/srd/professions/<slug>.md` | `.claude/skills/draft-content/references/profession.md` |
| `vault/campaigns/shattered-sea/pcs/<slug>.md` — a new PC sheet | `.claude/skills/dnd5e-character-interview/SKILL.md` |
| `vault/campaigns/shattered-sea/pcs/combat-profile/<slug>.md` | `.claude/skills/combat-profiles/SKILL.md` |
| `vault/campaigns/shattered-sea/pcs/session-logs/<slug>.md` | `.claude/skills/session-history-prep/SKILL.md` |
| any path, `type: narration` | `.claude/skills/writing-player-prose/SKILL.md` |
| any path, `type: dialogue` | `.claude/skills/writing-player-prose/SKILL.md` |

A crossing is a `type: route` (locations row above). Skippable texture is
drip on a Situation, Route, location, NPC, or rumour. Beat creation
(`beat-*.md`) routes through `composing-beats`, which
delegates to type-specific beat skills. Do not add `passage-*.md`,
`moment-*.md`, `fork-*.md`, `sequence-*.md` — route: `composing-beats` +
`_beat_*` templates.

A rumour page lives under `vault/campaigns/shattered-sea/lore/` and instantiates
`vault/_templates/_campaigns/_lore/_lore_rumour.md` -> the lore row's guide
routes it on from there.

Before drafting a new monster page from scratch, check `find-creature` for an
existing third-party statblock to vendor instead — the monsters row's guide
covers that check.

Before drafting a new item page from scratch, check `find-item` for an
existing third-party magic item to vendor instead — the items row's guide
covers that check.

Once the routed guide's interview/research has decided every fact the page
needs, the mechanical draft itself defaults to the `content-drafter` agent
(one file, one already-decided brief — `vault/refs/runbook-agents.md`'s
roster); the guide's own steps govern when that dispatch is worth it.

## Not routed here

Episode pipeline artifacts under `vault/episodes/NNN/` — the
run guide, DM screen, recap, highlights, and transcript — are phase
artifacts, not page types: `draft-run-guide`, `recap-writer`,
`transcript-label`, `transcript-ingest`, and `transcript-correct` own them
directly.

Vendored SRD and craft reference material (`vault/refs/stories/`,
`vault/refs/ideas/`, `vault/srd/monsters/`, `vault/srd/spells/`, and the
other SRD-marked trees) is not draft-owned -> route to `find-guidelines` or
`llm-wiki-ingest`.

## Owned paths

None. This skill never writes `vault/` — it identifies the guide that
does.
