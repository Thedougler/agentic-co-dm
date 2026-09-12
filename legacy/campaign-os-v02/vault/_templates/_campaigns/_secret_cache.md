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
subtype: cache           # fixed — this template IS the cache fork; a secret with nothing stored in it uses _secret.md
within: ""               # quoted, full vault-relative wikilink to the location or room this hidden spot sits inside — e.g. "[[campaigns/shattered-sea/locations/undermountain]]"
contains: []             # array of wikilinks to the item(s) hidden here — add a reciprocal found_at: entry on each item's own page pointing back here
campaigns: []            # OPTIONAL — this page's campaign(s), if this repo runs more than one
uid: 44b580f5-dce7-4c6e-a6a4-785cdf13f84b
---

# <Name>

*One-line description — the concealment in one sentence: the ordinary-looking feature that hides the cache, and the room or place it sits in.*

## Presentation

![[<slug>-narration-presentation]]

## Concealment

The physical mechanism that keeps this ordinary at a glance — what's actually screening the cache from view (the waterfall's curtain of water, a false wall, a rubble line, a floorboard) and why a passing look would never register it as unusual. This is the truth the Presentation box above is built to withhold.

## Discovery

Passive Perception threshold, if any — the number a party walking through without searching would need to beat to notice something's off, distinct from the active check below.

> [!check] <Skill> (DC <N>) — <Label>
> **Success:** <what the party notices and how the concealment gives way>.
>
> **Failure:** <nothing — the party moves on, with no visible sign they missed anything>.

A cache that must additionally be opened once found — a strongbox with a lock, a ledger in cipher — states that as a second `[!check]` box directly below, its own skill and DC, resolving how it opens rather than whether it is spotted. One check is enough where finding and opening are the same act; never write the second box empty to keep the shape.

## Reveal

![[<slug>-narration-reveal]]
