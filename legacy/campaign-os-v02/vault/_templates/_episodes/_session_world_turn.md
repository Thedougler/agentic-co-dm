---
type: session
subtype: world-turn
status: draft
publish: false
aliases: []
created: "{date}"              # the real date this world turn was written
updated: "{date}"              # same value as created on first write
tags: []
number:
world_date:              # the in-fiction date this turn resolves to, once its off-screen time passes, in the campaign calendar's own reckoning, e.g. "15 Eleint, 1495 DR" (see the calendar page's current_date)
owner_skill: ".claude/skills/world-update/SKILL.md"   # OPTIONAL — the guide or skill that owns this page's quality
uid: 37f04e36-f44f-44e2-abb6-6ec785801a6f
---

# World Turn — <YYYY-MM-DD>

Proposals only — `canon-review` applies these lines by hand;
`world-update` never edits `vault/` directly (its Hard Rule 2).

One line naming which session this turn follows, and a `REVIEWED-BY-HUMAN:
(pending)` marker.

## `<Faction — Front name>` (`<tier>`)

One subsection per processed Front, in the order `world-update` rolled
them. Each carries: a Context Brief (standing goal/method, current
position, this turn's evidence, off-screen move, the deep-read detail the
triage paste omitted), the Propose line, the `d20` roll and its
interpretation, then the ledger lines themselves —
`- [ ] VERB target :: change (citation)`, closed verb set `FACT` /
`APPEAR` / `NEW` / `QUEST` / `REVIEW`, full grammar in
`.claude/skills/world-update/references/ledger-mechanics.md`.

A dormant Front whose trigger didn't fire this turn still gets a
subsection — state which named trigger(s) didn't fire and why, so the
Front reads as reviewed-and-held, not silently skipped.
