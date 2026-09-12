# Worked Example (fixture — placeholder name, not real campaign content)

Full interview-to-page flow, worked end to end. Read this alongside
§ Output structure in `.claude/skills/rule-prep/references/output-structure.md`.

User: "I want a Ranger subclass for my PC who's obsessed with the tides
and sea omens."

Standard queries: `grep -ril "tide.*ranger\|sea.*omen.*subclass" vault/`
→ no hits, nothing to reskin.

Interview fills in: subtype `subclass`, base class Ranger, PC connection —
this is for the player's own character; core fantasy — "reads the sea's
moods as omens, and the sea listens back." Reading
`.claude/skills/rule-prep/references/class-design.md`'s Ranger row: core kit is Favored Enemy/
Tasha's replacements + spellcasting; watch out — Rangers are already
action-economy-strained, so no feature adds a per-turn action.

Balance citation: comparable to Gloom Stalker (Dread Ambusher: bonus
damage + extra attack round 1 of combat, no ongoing action cost) rather
than Beastmaster (a full pet, which does add per-turn management).

DM Review Gate: core fantasy, balance citation, and the action-economy
trap check presented; DM approves.

tideomen-conclave.md:

```markdown
---
type: rule
status: pending
publish: false
aliases: ["Tideomen Conclave"]
created: 2026-07-30
updated: 2026-07-30
tags: []
subtype: subclass
---

# Tideomen Conclave

> [!read-aloud] The tide doesn't just rise and fall for you — it's telling
> you something, and you've learned to listen.

*Subclass · Ranger · 3rd level*

| Field | Value |
|---|---|
| core_fantasy | Reads the sea's moods as omens, and the sea listens back. |
| balance_citation | Comparable to Gloom Stalker's Dread Ambusher (round-1 bonus, no ongoing action cost) rather than Beastmaster's per-turn pet management. |
| pc_connection | Built for [[example-tide-ranger-pc]]'s own character concept. |
| subclass_trap_checked | Rangers are action-economy-strained (references/class-design.md) — no feature here adds a per-turn action; the 3rd-level feature is a passive, round-1-only trigger. |

## Mechanics

**[HB] Tide-Read (3rd level).** Once per combat, on your first turn, if
you can see or hear a body of water, you gain advantage on your first
attack roll and the first saving throw you make that combat.

**[HB] Omen Sense (3rd level).** You always know the current phase of the
tide and moon without a check, and gain advantage on Survival checks made
near open water.

## Provenance

Designed for [[example-tide-ranger-pc]]'s Ranger at session prep, approved
at the DM Review Gate on the date this page was drafted.
```
