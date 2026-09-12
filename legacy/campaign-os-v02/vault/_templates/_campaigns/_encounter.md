---
type: encounter
status: draft
publish: false
title: ""                      # OPTIONAL — display title if it differs from the H1 heading; absent ⇒ the H1 is the title (llm-wiki skill)
aliases: []
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
created: "{date}"
updated: "{date}"
owner_skill: ".claude/skills/encounter-prep/SKILL.md"   # OPTIONAL — the guide or skill that owns this page's quality; not yet migrated to a draft guide (ADR-0031 candidate, deferred — see ADR-0040 Consequences)
tags: []
tier: supporting        # OPTIONAL — core | supporting | peripheral; absent ⇒ supporting (llm-wiki skill)
campaigns: []            # OPTIONAL — this page's campaign(s), if this repo runs more than one
uid: 87e389ef-0000-4e43-9a2f-975ca9b8db0c
---

# <Name>

*One-line description — the core tactical problem this encounter poses.*

## Opening

**Dramatic Question:** <The one question this encounter exists to answer — once play answers it, summarize the outcome and move to ## Transition, even mid-fight.>

![[<slug>-narration-open]]

## Enemy Roster

Who/what the party faces — role (ambusher/artillery/bruiser/controller/defender/leader/skirmisher), stat block links, and how they're grouped (solo, matched group, boss+minions).

## Challenge Calibration

Expected difficulty and how it was calibrated (action economy, party level).

## Terrain

Notable terrain features and how they affect the fight — cover, elevation, hazards, interactive objects, zone-wide effects.

## Tactical Notes

How the enemies actually fight — opening move, priorities, morale breaks, retreat conditions.

## Run Sheet

The one section a DM runs the whole fight from — no mid-round question
sends them back to Tactical Notes prose.

### Foe Roster

| Foe | Init | AC | HP | Flees/breaks at | Action script |
|---|---|---|---|---|---|
| <Name/group> | <mod> | <n> | <n>/<max> | <≤n HP or stated condition> | <one line: opening move, priority target, retreat trigger> |

### Round Script

- **R1:** <opening action — who acts first, what they do>
- **R2+:** <default pattern each round until a trigger fires>
- **Trigger — <round N / HP ≤X>:** <phase, lair, or legendary-action change, stated concretely>

Statblocks: <wikilink or `![[statblock#Heading]]` per foe, at point of use>

## Raising the Stakes

A live difficulty dial, paired with Lowering the Stakes below — targets
the party's read weakness (from Challenge Calibration), tension without
unfairness. Each line pairs a trigger condition with a concrete delta
carrying exact numbers.

- **Trigger:** <condition> → **Delta:** <exact numeric change — e.g. "add 2 more Smugglers from the alley">

## Lowering the Stakes

A live difficulty dial, paired with Raising the Stakes above — plays to
the party's strength, lets them feel powerful if they find it. Same
trigger-plus-numeric-delta shape, opposite direction.

- **Trigger:** <condition> → **Delta:** <exact numeric change — e.g. "remaining Smugglers flee once 3 are down">

## If They're Stuck

OPTIONAL — only for an encounter gated on an objective or puzzle solve.

1. **Free tell:** <environmental repetition of the clue>
2. **Costed nudge:** <a check or resource spend that buys the next step>
3. **Bail-out:** <NPC/event that moves things forward at a stated fiction cost>

## Endings

Every branch this page states odds for gets written text: a win condition
per phase (if Challenge Calibration or Run Sheet names phases), the
defeat/TPK aftermath, and the disengage/flee outcome.

**Win:** <what winning this fight/phase looks like, and what changes as a result>

**Defeat:** <what happens if the party goes down — never "the DM decides"; state the actual aftermath>

**Disengage/flee:** <what happens if the party breaks off — cost, consequence, what the enemy does next>

## Stakes

What's actually on the line if the party loses or walks away.

## If Ignored

What happens if the party never engages this encounter.

## Transition

Condition → explicit goto wikilink with elapsed in-fiction time, every
written branch skip on its own line. This page never closes on prose alone.

- <condition> → [[<next-scene-or-section>]], <elapsed in-fiction time>
- <branch skip, if any> → [[<target>]]

---

*How to read this page: [[runbook-reading-conventions]].*
