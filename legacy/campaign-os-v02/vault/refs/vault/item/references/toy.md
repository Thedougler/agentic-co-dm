---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "The Item Toy table's six fields, what belongs in each, and the good/bad pair that shows the difference."
created: "2026-08-03"
updated: "2026-08-03"
tags: [craft]
uid: 16ea69d6-c387-49e9-a7e9-742e73fe39f0
---

# Item Toy (the six fields)

Write these once, as a markdown table in the DM-only material, no heading of
its own. `rarity` and `attunement` themselves are governed frontmatter keys
(`vault/refs/vault/item/references/frontmatter.md`), not table rows — the table
carries their *justification*, which is prose and can't live in a YAML enum
value.

| Field | What goes here |
|---|---|
| `one_thing` | The single core mechanic, one sentence (The One-Thing Discipline). |
| `rarity_justification` | The 2 RAW items cited to justify the `rarity:` frontmatter value. |
| `attunement_reason` | Which branch of the decision tree triggered the `attunement:` frontmatter value. |
| `pc_connection` | The PC-Connection Requirement — which PC, and the specific mechanism. Required, wikilinked. |
| `current_holder` | Who or where holds this item right now — an NPC, a location, or "unclaimed, awaiting placement." Wikilinked if it resolves to a page. |
| `narrative_hook` | How the party could plausibly encounter it in the current arc. |

Field rules (the universal three are `.claude/skills/composing-beats/references/runtime-surface.md`
§3; these are the item-specific good/bad pairs):

- `one_thing` — ✓ "Grants advantage on Stealth checks made in shadow or
  darkness." ✗ "Helps you sneak around and also protects you and also looks
  cool."
- `rarity_justification` — ✓ "Uncommon — comparable to
  [Cloak of Elvenkind](vault/srd/items/uncommon/cloak-of-elvenkind.md)
  (advantage on Stealth, no attunement) and
  [Boots of Elvenkind](vault/srd/items/uncommon/boots-of-elvenkind.md)
  (advantage on Stealth-relevant terrain checks)." ✗ "Probably
  uncommon-ish."
- `pc_connection` — if you can't answer this in one sentence, the item isn't
  ready to generate (the PC-Connection Requirement).
- `current_holder` — ✓ "renn-oxby, sells it from his east-pier stall."
  ✗ "somewhere in the world."
