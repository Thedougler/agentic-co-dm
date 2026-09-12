---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "A worked homebrew creature fixture running interview through Toy Chest, Prepped Reveals, and the transcluded stat block, with the PC draw left as a placeholder slot."
created: "2026-08-03"
updated: "2026-08-10"
tags: [maritime, stealth, survival]
uid: c5abd5f4-13cc-4c1c-806f-1048feb98c03
---

# Worked example (fixture — placeholder names, not real campaign content)

User: "I need a homebrew monster the party might run into more than once —
something that ambushes ships near Harborwatch."

Standard queries come back empty for `"tideglass ripper"` (the chosen name)
across `vault/` and `vault/episodes/*/transcript.md` — clean to create.
`find-creature` turns up no freely-licensed statblock close enough to the
concept to vendor. No RAW analog fits the concept closely enough to reskin
(Reuse Before Inventing checked, genuinely new). Interview fills in: reused
across encounters (travel-events flagged it for a shipping-lane leg),
aberration, preys on vessels near reef breaks, ties to `<PC name>`'s
shipping route running through the same waters — fill that slot from the PC
sheets, never from this page.

````markdown
---
type: monster
status: pending
publish: false
title: ""
aliases: ["Tideglass Ripper"]
summary: "A reef-dwelling aberration that ambushes ships near Harborwatch's shipping lanes, striking once from below and vanishing before it's seen."
created: "2026-07-30"
updated: "2026-07-30"
tags: [maritime, aberration]
tier: supporting
source: ""
source_url: ""
license: ""
found_at: ["[[shattered-sea|The Shattered Sea]]", "[[central-strait|Central Strait]]"]
statblock: transcluded
name: ""
campaigns: []
reference_image: ""
---

# Tideglass Ripper

**Wants:** Feed before the reef's seasonal current shift forces it deeper,
striking once from below and vanishing before it can be identified.
**Morale:** Retreats permanently the first time it takes 20 or more damage
in a single hit — it never presses a fight it's losing.

> [!read-aloud]
> The water goes glass-still half a second before the hull shudders, and
> whatever hit it is already gone — just a wake, spreading toward the reef
> break.

## Description

Harborwatch sailors call reef breaks near known sightings "ripper water"
and route around them. No one's gotten a clean look at one and lived to
describe more than the wake it leaves.

## Ecology

A reef-dwelling aberration that hunts by keel-shadow, striking once from
directly below and retreating to depth to feed — it never surfaces fully
unless a hull is already breached. A recent reef collapse destroyed its
usual feeding ground, pushing it into the shipping lane.

## Toy Chest

| Verb | Unstable Condition | Consequence | Link of Relevance |
|---|---|---|---|
| Track its strike pattern across repeated hits | Three ships hit in the same reef break within a season | The party can predict its next likely target and stage an ambush | Protects the same reef-break route <PC name>'s shipping runs depend on |

## Prepped Reveals

A single hit for 20 or more damage sends it into permanent retreat — the
DM can end the threat without a second full encounter.

## Stats & Combat

![[tideglass-ripper-statblock]]
````

The Stat Block Placement Choice: this page set `statblock: transcluded`,
so the embed above resolves to its own page,
`vault/campaigns/shattered-sea/monsters/<slug>-statblock.md`.
That separate page always registers itself in the bestiary via its own
`statblock: inline` frontmatter (Bestiary wiring,
`vault/refs/vault/monster/references/statblock-format.md`) — a different key
than this creature page's own `statblock: transcluded` choice above — with
`name:` matching the codeblock's `name:` exactly.

```yaml
statblock: inline
name: "Tideglass Ripper"
```

```statblock
name: "Tideglass Ripper"
layout: Basic 5e Layout
size: Large
type: aberration
alignment: unaligned
ac: 15
hp: 84
hit_dice: "8d10 + 40"
speed: "swim 40 ft."
stats: [18, 14, 20, 6, 12, 8]
senses: "blindsight 60 ft., passive Perception 11"
languages: "—"
cr: 5
traits:
  - name: "Keel-Shadow Ambush"
    desc: "The ripper has advantage on attack rolls against any target that hasn't noticed it, which is nearly always true on its first strike."
actions:
  - name: "Breach Strike"
    desc: "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 24 (4d8 + 6) piercing damage, and the target must succeed on a DC 15 Strength save or be dragged underwater."
  - name: "Submerge"
    desc: "The ripper dives to depth, becoming unreachable by non-swimming creatures until it strikes again."
```
