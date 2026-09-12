---
type: craft
status: canon
publish: false
aliases: []
created: 2026-08-07
updated: 2026-08-07
tags: [craft]
summary: "The generative method for inventing new D&D 5e mechanics: flavor-first, SRD-splice, iterate, edge-test, party-useful — read before any prep skill's balance-citation gate."
uid: e87f50ce-cb0d-44fa-87e5-4dbbedc60eec
---

# Homebrewing Mechanics

Read this before designing any new mechanical content — a magic item, a
feat, a spell, a subclass feature, a species trait, a monster ability, a
trap or hazard effect. `.claude/skills/draft-content/references/item.md`, `rule-prep`, and `.claude/skills/draft-content/references/monster.md` each
gate the *output* (rarity/benchmark citation, `[RAW]`/`[HB]` labeling,
prohibited-feature lists) — this file is the step before that gate: how to
get from a design goal to a candidate mechanic in the first place. Cite this
file from a skill's own hard rules instead of restating it.

---

## 1. Flavor-first check

Before touching any number, ask: does the request actually need a new
mechanic, or does re-describing an existing one solve it? A weapon that
"feels special," an NPC voice that "feels ancient," a spell that "looks
like coral instead of fire" — none of that requires new math. Re-skin the
existing mechanic (same numbers, new description) and stop.

This is free. No rarity/benchmark citation, no `[HB]` label — a flavor-only
change never touches `## Mechanics`. The tell that a request needs to
continue past this section: the ask changes what the mechanic *does* at the
table (an extra effect, a bigger number, a new use case), not just what it
looks or sounds like.

## 2. SRD-splice method

When flavor alone can't hit the design goal, don't invent freehand — find
the closest 1-3 examples already in `vault/srd/` (`vault/srd/items/<rarity>/`,
`vault/srd/feats/`, `vault/srd/spells/<school>/`, `vault/srd/classes/subclasses/`,
`vault/srd/species/`) and change the minimum needed to reach the new fantasy.

- **Exact match exists** → reskin it outright, keep the math (this is
  `.claude/skills/draft-content/references/item.md`/`rule-prep` Hard Rule 1's stub-check territory).
- **No exact match, but a close analog exists** → splice: take the bounded
  shape (range, duration, recovery, action cost) from one SRD entry and the
  effect type from another, rather than inventing a new template. Reuse the
  SRD's own phrasing for recovery/duration clauses ("once per long rest",
  "for the duration, up to 1 hour", "1d4 minutes to arrive") instead of
  writing new ones — the SRD's bounding language is already balance-tested.
- **Ceiling, not floor** — when splicing from a higher-level spell or a
  class feature, scale *down* toward the target tier: fewer questions, a
  smaller radius, a shorter duration, a narrower trigger. Reaching for the
  SRD is not license to import its full scope at a lower cost.

## 3. Iterate

Generate 2-3 candidate versions before committing to one. Reject any
candidate that's mechanically identical to its SRD source with only the
name changed — that's a reskin, not a homebrew, and belongs in § 1
instead. The versions worth keeping differ in what makes them worth
inventing at all: a different trigger, a different resource cost, a
narrower or wider scope than the source. Pick the one that's most
distinct from its source while still fitting the design goal and the
target power tier.

## 4. Edge-case pass

Before finalizing, name what the mechanic touches:

- **Concentration** — does it stack for free with an actual concentration
  spell that does something similar? If the SRD analog costs concentration
  and this doesn't, that's the gap to close, not a feature.
- **Multiclassing** (`vault/srd/rules/multiclassing.md`) — does a one-level dip into another class combine with
  this to double an effect it wasn't designed to interact with (e.g. a
  mark-and-bonus-damage rider plus Sneak Attack)?
- **Action economy** — does it grant a second bonus action, reaction, or
  free attack that stacks with what the PC's class already gives them?
- **Stacking** — does repeated or simultaneous use (multiple marks, nested
  triggers) scale the effect past what a single instance was budgeted for?

Any "yes" above means bound it further (a recharge clause, a
once-per-turn cap, an explicit "doesn't stack with itself") until the
interaction can't break the action economy or damage budget. An unbounded
power — no stated recovery, no cap on repeated use — is the single most
common failure at this step; state action cost, range, duration, and
recovery explicitly, same finding as `.claude/skills/draft-content/references/item.md`/`rule-prep`'s own Hard
Rules on labeling.

## 5. Party-utility gate

A homebrewed mechanic ships only if it's useful to the party or a named
party member — never a mechanic that exists purely for NPC/DM use, purely
decorative, or built for a hypothetical future PC. This generalizes
`.claude/skills/draft-content/references/item.md`'s PC-Connection Requirement and `rule-prep` Hard Rule 2's PC-Connection
Requirement from "who does this narratively pull on" to the mechanic
itself: if no one at the table would ever choose to use it, the design
isn't ready to ship, regardless of how well-bounded or SRD-grounded it is.
