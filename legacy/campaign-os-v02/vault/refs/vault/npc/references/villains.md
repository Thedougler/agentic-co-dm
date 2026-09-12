---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "Recurring-antagonist additions — the Three Villain Questions, stat-block build paths, and escape mechanics."
created: "2026-08-03"
updated: "2026-08-03"
tags: [intrigue]
uid: df9557eb-3b1b-4919-ba18-de0a2849814e
---

# Villain NPC additions

For a recurring antagonist, add after the standard DM-only material,
before `## Stats & Combat`:

**Three Villain Questions:**

1. What do they want? (Specific and concrete — not "power.")
2. What do they fear? (The crack in the armor — emotional and mechanical.)
3. What is their tell? (One physical habit or speech pattern.)

**Villain design checklist** — a good villain, beyond the three questions
above, condensed from `.claude/skills/composing-beats/references/composition.md`. This is the canonical
copy; `vault/refs/vault/faction/references/content.md` § Villain & Antagonist
Design cites it rather than restating it.

- Believes what they're doing is right — the conviction principle itself
  (why this matters more than a villain who just knows they're evil) is
  `vault/refs/ideas/villains-and-themes.md` § The five-axis villain's
  territory; this checklist just names the requirement.
- Expect them to die. Design for that outcome, not around avoiding it.
- Memorable — something that makes a player do a double-take.
- Their progress is visible in the world, not just stated — the party
  should be able to see what the villain has been doing between sessions.
- Responds to character interference — if the party disrupts a scheme,
  the villain reacts, adapts, or retaliates on their own timeline
  (`.claude/skills/composing-beats/references/audits.md` § Independent NPC Agency).
- Interacts with the party both directly and indirectly (through
  subordinates, environment, rumor) — not always face-to-face.

**Antagonists** (subordinates, lieutenants, or recurring foes who aren't
the campaign's top-tier villain) get a lighter version of the same
discipline — from the same source:

- Represents the villain's agenda, not a generic obstacle — contributes to
  it rather than running a parallel plot of their own.
- Often interfaces with the party *instead of* the villain — this is what
  makes a top-tier villain feel protected/insulated rather than always
  on-screen.
- Use a variety of antagonists that represent the villain's themes
  differently, not palette-swapped copies of one type.
- Has their own motivation, distinct from just "following orders."
- Reacts to the story as it unfolds, same as a full villain.

**Stat block approach** (`## Stats & Combat`, after the Calibrate Against The Real Party rule's
calibration pass): three paths, picked by build, never re-derived from
scratch across more than one.

- **Effective class level** (the default) — spellcasters get 5–7 prepared
  spells with clear tactical intent; martial villains get one signature
  technique; hybrids get one martial feature plus up to 3 spells.
- **CR-built** (a villain statted as a monster rather than a class-leveled
  humanoid — legendary actions, a full traits/actions suite, a CR number
  on the block) — the CR math is `.claude/skills/draft-content/references/monster.md`'s, not this
  skill's to duplicate (DRY): read `vault/refs/vault/monster/references/cr-design.md`
  for the CR calculation method and the solo-boss/legendary-action CR
  adjustment (+1 per 3 legendary actions, +1 for lair actions — easy to
  blow past a target CR by forgetting this), and
  `vault/refs/vault/monster/references/cr-tables.md` for the HP/DPR-by-CR
  and ability-score-to-modifier lookup tables.
  This skill still owns everything the monster guide doesn't: the Toy Chest,
  the Three Villain Questions, the escape mechanic, and keeping the page
  under `## Relationships`-bearing npc page structure rather than a
  bestiary entry.
- **Improvised** — for a minor NPC (a one-scene antagonist, a random
  brawl) who needs table-ready combat numbers with no full build. Pick a
  single CR-equivalent number (roughly the average party level, adjusted
  for how tough the NPC should feel) and derive: AC = 12 + ½ CR, DC = 12 +
  ½ CR, attack bonus = 3 + ½ CR, HP = 20 × CR, single-target damage =
  7 × CR (or 2d6 per CR), multi-target damage = 3 × CR (or 1d6 per CR).
  Lighter-weight than both paths above — use it only when there's no time
  or need for a real build, not as a shortcut for a recurring antagonist
  who'll return.

**Villain mechanics:**

- **Escape mechanic** — a recurring villain needs a way out (misty step, a
  lackey who sacrifices themselves, a legendary-action dash). Killing them
  too early ends the thread that connects to their PC (the PC-Connection Requirement).
- **Personal shield** — something that reads as invulnerability until the
  players figure it out (magic resistance, a *Shield* spell, an amulet to
  destroy first).
- **Monologue trait** *(optional flavor)* — once per combat, they can speak
  without spending their action. Include a suggested line.

Tag block, appended after the stat block:

```text
> **Personality.** [Two sentences: affect/manner, then one specific tell.]
> **Motivation.** [One sentence: exactly what they want right now, this encounter.]
> **Escape Condition.** [What triggers the retreat, and how.]
```
