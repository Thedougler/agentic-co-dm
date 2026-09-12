---
type: monster
status: draft
publish: false
title: ""                 # OPTIONAL — display title if it differs from the H1
aliases: []
summary: ""                 # one sentence, ≤200 chars — cheap page preview, never empty
created: "{date}"
updated: "{date}"
tags: []
tier: supporting           # core | supporting | peripheral
source: ""                  # required for a transcribed or vendored creature — the sourcebook or document this creature comes from; OPTIONAL for an original homebrew creature
source_url: ""               # OPTIONAL — a live external source link, when one exists
found_at: []                # ≥2 wikilinks to region-scale locations where this creature is thematically found, picked per vault/refs/vault/monster/references/ecology.md
habitat: []                  # Arctic | Coastal | Desert | Forest | Grassland | Hill | Mountain | Swamp | Underdark | Underwater | Urban — one or more, per the 2024 Monster Manual's habitat categories
statblock: inline             # fixed — registers this page's codeblock into the Fantasy Statblocks bestiary (.claude/skills/obsidian-fantasy-statblocks/references/bestiary-and-recall.md)
name: ""                      # must match the inline statblock codeblock's own name: field
# cr/ac/hp/str/dex/con/int/wis/cha below all mirror the statblock codeblock's
# own fields (str-cha from its stats: [STR, DEX, CON, INT, WIS, CHA] array, in
# order) so Bases can sort/filter numerically — keep both copies in sync.
cr: 0                          # fractions as decimals: 1/8 = 0.125, 1/4 = 0.25, 1/2 = 0.5
ac: 10                         # strip any parenthetical, e.g. "15 (natural armor)" -> 15
hp: 1
str: 10
dex: 10
con: 10
int: 10
wis: 10
cha: 10
campaigns: []                 # OPTIONAL
reference_image: ""           # OPTIONAL
owner_skill: ".claude/skills/draft-content/references/monster.md"   # OPTIONAL — the guide or skill that owns this page's quality
uid: 9bee0980-49bf-4212-a545-4a8033cc7874
---

# <Name>

## Stats & Combat

Write the fenced `statblock` codeblock directly below, `name:` matching
this page's frontmatter `name:` — field schema and WotC wording in
`vault/refs/vault/monster/references/statblock-format.md`.

**Behavior states** — OPTIONAL, only for a creature with distinct tactical
phases (a hunting/digesting cycle, an enrage threshold); one row per
state. Delete this line and the table below for a creature that doesn't
need it.

| State | Trigger | Behavior |
|---|---|---|
| <State> | <What flips it into this state> | <What it does while in this state> |

**Wants:** <One bold-led line compressing what this creature is trying to do and what's currently disrupting it, drawn from the Toy Chest table below.>
**Morale:** <The pre-decided break/flee condition that ends the fight — an HP threshold, a round count, or a trigger, never a restatement of the stat block's HP.>

Wants, Morale, behavior states, and the narration-appearance sibling are
OPTIONAL for mindless or Blight-maddened fauna with no rational behavior
to model. Delete them for such creatures. For a creature with agency or
tactical intent, all are mandatory — write the Toy Chest table first,
then compress it into Wants.

![[<slug>-narration-appearance]]

```meta-bind
VIEW[{reference_image}][image(class(reference-image-view))]
```

## Description

What's commonly known or immediately visible about this creature — the
public-facing entry, what a character with no special knowledge could
already say.

## Ecology

Where it lives, what it eats, how it behaves around its own kind and
other creatures. Grounded in the terrain and culture of its `found_at:`
locations, never a generic taxonomy entry.

## Toy Chest

OPTIONAL — delete for mindless or Blight-maddened fauna with no rational
behavior to model. Required for a creature with agency, tactical intent,
or interactive hooks a DM can exploit mid-encounter. For an SRD or
third-party creature, keep only what this campaign adds. A table:
`| Verb | Unstable Condition | Consequence | Link of Relevance |`, one
row per interactive hook — never a vague "is dangerous" line.

| Verb | Unstable Condition | Consequence | Link of Relevance |
|---|---|---|---|
| <What a PC can do to/with it> | <What state makes that possible> | <What happens as a result> | <A page this ties to, if any> |

## Prepped Reveals

OPTIONAL — one or two facts a DM can drop mid-fight to reward a Nature/
Arcana/Investigation check or clever play; delete if none exist.

## Notable Individuals

OPTIONAL — named, recurring members of this creature kind; delete
otherwise.
