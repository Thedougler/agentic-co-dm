---
type: lore
subtype: rumour         # fixed — this template IS the rumour fork; other subtypes use _templates/lore.md
status: draft
publish: false
title: ""                      # OPTIONAL — display title if it differs from the H1 heading; absent ⇒ the H1 is the title (llm-wiki skill)
aliases: []
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
created: "{date}"
updated: "{date}"
owner_skill: "vault/refs/vault/lore/references/rumour.md"   # OPTIONAL — the guide or skill that owns this page's quality
tags: []
tier: supporting        # OPTIONAL — core | supporting | peripheral; absent ⇒ supporting (llm-wiki skill)
edit_pass: 0            # OPTIONAL — last completed line pass (0–3); the draft-story skill is this key's sole writer
campaigns: []            # OPTIONAL — this page's campaign(s), if this repo runs more than one
uid: 6065aa88-1739-4ccf-8361-d691f4f432b8
---

# <Name>

*One-line description — the rumour as it's actually heard in-world, in one sentence.*

## The Rumour

The rumour verbatim, as the party would actually hear it repeated on the
street — a `type: dialogue` sibling when it's delivered as a spoken line
at the table, otherwise plain prose. States plainly what it claims.

## Truth Value

How much of the rumour is actually true: `**True**`, `**False**`, or
`**Partially true:**` followed by exactly what's real and what's distorted
or invented in the retelling. The DM-only ground truth, its own line,
never left ambiguous — mirrors `_templates/lore.md`'s active/atmospheric
split: a rumour with no stated truth value can't be adjudicated when a PC
investigates it.

## Spread

Where and from whom the party can actually hear this — which NPCs repeat
it, which locations or social class it circulates in, and whether it
grows or changes with each retelling (state how, if it mutates).

## Investigating It

What a check that presses further on this rumour reveals, tiered — a
`[!check] <Skill> — <Label>` callout (named ability/skill, DC, tiered
Success/Failure; `callouts` skill, references/check.md), never a bare DC
in prose. Success moves the party toward the Truth Value above; failure
costs something — time, a wrong lead, the source clams up — rather than
nothing happening.

> [!check] <Skill> (DC <N>) — <Label>
> **Success:** <what's confirmed, refined, or revealed>.
>
> **Failure:** <what's missed or what it costs>.
