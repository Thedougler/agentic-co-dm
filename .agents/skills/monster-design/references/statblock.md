# Statblock

Read this in step 8. Creature pages use the `statblock` fence (the Fantasy
Statblocks plugin, `Basic 5e Layout`) with SRD 5.2.1 wording inside each
`desc`. Use original names and paraphrase; delete fields that do not apply.

## 2024 phrasing

| Element | Write it as |
|---|---|
| Attack | `Melee Attack Roll: +7, reach 10 ft. Hit: 13 (2d8 + 4) Bludgeoning damage.` |
| Ranged attack | `Ranged Attack Roll: +6, range 60/240 ft. Hit: 10 (2d6 + 3) Piercing damage.` |
| Save effect | `Constitution Saving Throw: DC 15, each creature in a 30-foot Emanation originating from the fogbell. Failure: 27 (6d8) Thunder damage, and the target has the Prone condition. Success: Half damage only.` |
| Condition | Capitalised with "has the … condition": `the target has the Grappled condition (escape DC 15)` |
| Recharge and limits | `(Recharge 5–6)`, `(1/Day)`, `(3/Day, or 4/Day in Lair)` |
| Areas | `20-foot Cone`, `30-foot Emanation`, `10-foot Cube`, `60-foot-long, 5-foot-wide Line` |
| Durations | `until the end of its next turn`, `until the start of the fogbell's next turn`, `(repeat the save at the end of each of its turns)` |
| Resistances | Damage types only: `"Bludgeoning, Cold"`. There is no "nonmagical attacks" qualifier in 2024 |
| Legendary Resistance | `If the fogbell fails a saving throw, it can choose to succeed instead.` |
| Legendary actions | A first entry with an empty name holding: `Legendary Action Uses: 3. Immediately after another creature's turn, the fogbell can expend a use to take one of the following actions. It regains all expended uses at the start of each of its turns.` |

Every feature states its timing, range, targets, attack or save, effect,
duration, and how it ends. Put the tell for a signature move in its text or
in a trait, so the DM reads it at the table.

## Fence

````markdown
![[attachments/{slug}-overview.jpg|{Title} overview]]
```statblock
layout: Basic 5e Layout
name: "{Title}"
size: Huge
type: monstrosity
alignment: unaligned
ac: "14 (natural armor)"
hp: 190
hit_dice: "20d12 + 60"
speed: "10 ft., fly 20 ft. (hover)"
stats: [18, 10, 16, 3, 14, 6]
saves:
  - constitution: 6
  - wisdom: 5
skillsaves:
  - perception: 5
damage_resistances: "Bludgeoning"
damage_immunities: "Thunder"
condition_immunities: "Prone"
senses: "Blindsight 120 ft., Passive Perception 15"
languages: "—"
cr: "8"
traits:
  - name: "Legendary Resistance (2/Day)"
    desc: "..."
actions:
  - name: "Multiattack"
    desc: "..."
bonus_actions:
  - name: "..."
    desc: "..."
reactions:
  - name: "..."
    desc: "Trigger: ... Response: ..."
legendary_actions:
  - name: ""
    desc: "Legendary Action Uses: 3. ..."
  - name: "..."
    desc: "..."
```
````

Omit `bonus_actions`, `reactions`, and `legendary_actions` when unused. Put
the overview image, when one exists, on the line just before the fence; every
other image goes under `## Art` in its role subsection (`### Token`,
`### Battlemap`, and so on) using `wiki/attachments/{slug}-{role}.{ext}`.

## Forms and stages

A creature with more than one form (a split, a second stage, a phylactery
that weakens) gets one fence per form. The first fence is the full block; each
later fence names the first with `monster: "{Title} (Stage 1)"` and overrides
only what changes, using `traits-` / `traits+` (and the same pattern for
`actions`) to remove or add entries. Above the fences, state the trigger that
swaps forms in one plain sentence, keyed to the fiction.

## Named NPC with a combat form

When the creature is a named individual, its page is an NPC page owned by
`npc-design`. This skill supplies its Combat section: an encounter rule (the
fiction that decides which fence to use) followed by one fence per form, or a
single pointer to a species creature page it uses unchanged.
