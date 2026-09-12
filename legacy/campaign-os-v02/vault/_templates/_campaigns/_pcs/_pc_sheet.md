---
type: pc
subtype: character-sheet
pc: "{pc-slug}"
alias: "{OPTIONAL — short lowercase CLI shortcut, e.g. 'pbj' — lets `npm run dndsim -- sim-combat {alias} --sweep-corpus` resolve without the full slug}"
pc_level: {number: null}
class_levels: "{e.g., Bard 3 / Warlock 1}"
last_synced: "{date}"
owner_skill: ".claude/skills/combat-profiles/SKILL.md"   # OPTIONAL — the guide or skill that owns this page's quality
uid: 82f761b5-138a-4012-bb2d-4eceeef676cd
---

The machine artifact converted from a player's
character sheet (PDF or plain text). A derived-data page, like
`pc-combat-profile.md`/`party-combat-profile.md`: it carries `type:` for
frontmatter-schema validation but no governed spine (no `status:` —
`_templates/default.md` § Spine contract).

Open with a `Source:` line naming the sheet file
(`_assets/character-sheets/{pc-slug}-character-sheet.pdf`) and any `[verify]`
flags for values that appear inconsistent with other sheet data — transcribed as printed,
never silently "fixed".

## What lives here, and what does not

The human-readable transcription lives in `vault/campaigns/shattered-sea/pcs/`, one governed page
per facet, each instantiated from its own template:

| Facet | Page | Template |
|---|---|---|
| Ability scores, saves, skills, speeds, proficiencies | `vault/campaigns/shattered-sea/pcs/stats/{pc-slug}-stats.md` | `_templates/pc-stats.md` |
| Traits, features, actions, bonus actions, reactions, feats | `vault/campaigns/shattered-sea/pcs/abilities/{pc-slug}-abilities.md` | `_templates/pc-abilities.md` |
| Spellcasting, cantrips, known/prepared, slots | `vault/campaigns/shattered-sea/pcs/spells/{pc-slug}-spells.md` | `_templates/pc-spells.md` |
| Attunement, carried gear, caches, currency | `vault/campaigns/shattered-sea/pcs/inventory/{pc-slug}-inventory.md` | `_templates/pc-inventory.md` |
| AC, max HP, class levels, total level | `vault/campaigns/shattered-sea/pcs/{pc-slug}.md` frontmatter | `_templates/pc.md` |

This file carries only what those pages cannot: the source citation, the
`[verify]` flags, and the machine-parseable Combatant Block. Restating a
table that already exists on one of the pages above is a duplication
defect — link to it instead.

## Combatant Block

The sim input, everything on the pages above re-expressed as data, on the
same Fantasy Statblocks fence every NPC and creature uses:

````text
```statblock
layout: Basic 5e Layout
name:
size:
type: humanoid
ac:
hp:
stats: [STR, DEX, CON, INT, WIS, CHA]
saves: { }
actions:
sim:
  side: party
```
````

Schema and rules: `utils/dndsim/CLAUDE.md` (§ unified statblock
schema, `sim:` extension namespace). Attacks/saves go in `actions:`/
`bonus_actions:` as SRD-grammar `desc:` prose (2014 or 2024 phrasing, both
supported); anything the grammar can't express — resource pools, Hex/GWM/
Bardic-Inspiration-style capabilities, a heal, a costed/triggered reaction
— goes in the top-level or per-action `sim:` block. The top-level
`sim.abilities:` list declares every always-available capability the sim's
auto-policy may use — one left out silently floors the PC's simulated
numbers. A caster declares `sim.spellcasting:` pools (one per class) whose
`known:` spells are referenced by NAME from the spell library (README
§ Spell library) — never re-encoded per sheet; the block always states a
`speed:` (the range-band model reads it, 30 ft. RAW default when the sheet
is silent). Every value traces to a row on one of the `vault/campaigns/shattered-sea/pcs/` pages
above; `[verify]`-tagged values carry the tag alongside as a YAML comment;
a value the sheet doesn't state and no cited SRD page supplies stays OUT
of the block — a page-sourced number enters tagged
`[srd]`/`[sheet+srd]` with the path recorded (combat-profiles
`.claude/skills/combat-profiles/references/data-and-sheets.md` Rule 3); a plausible guess never does.

**Quality rules:** every number verifiable from the source. No
editorializing — this is a mechanical reference, not the profile;
"good for..." commentary belongs in the combat profile's Calibration
Notes.

**Keeping in sync:** when a player reports a level-up or a new sheet,
re-read it, update the four `vault/campaigns/shattered-sea/pcs/` pages and this Combatant Block
together, bump `last_synced` on every one of them, and flag every profile
that cites this sheet as stale.
