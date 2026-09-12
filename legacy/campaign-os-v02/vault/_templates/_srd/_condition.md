---
type: condition
status: draft
publish: false
title: ""                      # OPTIONAL (display title if it differs from the H1 heading; absent, the H1 is the title, llm-wiki skill)
aliases: []
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
owner_skill: ".claude/skills/draft-content/references/condition.md"   # OPTIONAL — the guide or skill that owns this page's quality
created: "{date}"
updated: "{date}"
tags: []
tier: supporting        # OPTIONAL - core | supporting | peripheral; absent, defaults to supporting (llm-wiki skill)
condition_status: active   # active | dormant | cured
campaigns: []            # OPTIONAL - this page's campaign(s), if this repo runs more than one
uid: 41d53b1b-c206-4e53-9b3d-8085c6a6cfd3
---

# <Condition Name>

*One-line description: what this affliction is and what it does to whoever carries it.*

## Nature

Name what this condition concretely is. This type covers disease, curse,
mutation, madness, poison tracked as a lasting effect instead of a
single save. This type absorbs all five categories. It never forks into
disease/curse/madness sibling templates, so state plainly which of them
this page is. Name who or what it can affect (a species, a bloodline, a
location's population, anyone exposed to a specific trigger). In-world
facts only.

## Onset & Symptoms

How the condition first manifests and how it changes the carrier over
time: the delay before symptoms appear, and whether it worsens in
observable stages or arrives all at once and holds steady. State what an
onlooker would actually notice at each stage, not just what the carrier
feels.

## Transmission & Origin

Name the mechanism that spreads or inflicts the condition: contact,
ingestion, inhalation, a curse's casting, inheritance, exposure to a
place or event. State where it came from (a plague ship, a wronged
spellcaster, a magical catastrophe, a natural mutation with no one to
blame). A condition with no origin worth naming states that plainly
instead of inventing one.

## Cure & Mechanical Effect

State whether a healer can cure this condition. Real states include: a
mundane remedy works, a specific spell works, a ritual works, or nothing
does yet, "no known cure." Name what happens to an untreated carrier
over time. Then state the
mechanical link: `[[rule-slug]]` to the `type: rule, subtype: condition`
page that carries this affliction's table mechanics (the effect on
ability checks, saves, HP, or other numbers), if one exists, or "no
mechanical effect, narrative only" when none does. This page never
states the numbers itself.
