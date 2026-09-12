---
type: secret
status: draft           # draft | pending | canon | srd | retired
publish: false
title: ""                      # OPTIONAL — display title if it differs from the H1 heading; absent ⇒ the H1 is the title (llm-wiki skill)
aliases: []
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
created: "{date}"
updated: "{date}"
owner_skill: ".claude/skills/draft-content/references/secret.md"   # OPTIONAL — the guide or skill that owns this page's quality
tags: []
tier: supporting        # OPTIONAL — core | supporting | peripheral; absent ⇒ supporting (llm-wiki skill)
within: ""               # quoted, full vault-relative wikilink to the location, room, NPC, or faction page this secret is attached to — e.g. "[[campaigns/shattered-sea/locations/undermountain]]"
campaigns: []            # OPTIONAL — this page's campaign(s), if this repo runs more than one
uid: 8014eae0-1e12-4972-ba99-3c721b009952
---

# <Name>

*One-line description — the concealment in one sentence: the ordinary-looking feature or behaviour that screens this, and the place, person, or organisation it sits inside.*

## Presentation

![[<slug>-narration-presentation]]

## Concealment

The mechanism that keeps this ordinary at a glance — what is actually screening it from notice (a curtain of falling water, a false wall, a rubble line, a floorboard, a second set of books, a name nobody has reason to connect) and why a passing look would never register it as unusual. This is the truth the Presentation box above is built to withhold.

## Discovery

Passive Perception threshold, if any — the number a party moving through without searching would need to beat to notice something is off, distinct from the active check below.

> [!check] <Skill> (DC <N>) — <Label>
> **Success:** <what the party notices, and how the concealment gives way>.
>
> **Failure:** <nothing — the party moves on, with no visible sign they missed anything>.

A concealment that must additionally be worked out once noticed — a seam found but no catch, a ledger read but not decoded — states that as a second `[!check]` box directly below, its own skill and DC, resolving how the thing opens rather than whether it is spotted. One check is enough where noticing and defeating are the same act; never write the second box empty to keep the shape.

## Reveal

![[<slug>-narration-reveal]]
