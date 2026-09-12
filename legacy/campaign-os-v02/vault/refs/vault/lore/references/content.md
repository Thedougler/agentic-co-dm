# Lore Content Reference

Fuel for a lore page's central fact and its active draw — sibling
reference to `vault/refs/vault/quest/references/content.md`'s and
`vault/refs/vault/faction/references/content.md`'s shape. Read this
during the interview when the DM doesn't have a fact yet, or when a
legend/prophecy/pantheon entry needs sharpening. Every section here
cites its external source; use as a spark, not a script — a lore
page still needs its own PC-connection and active-draw line named, per
`.claude/skills/draft-content/references/lore.md`'s own rules.

## Historical & Legendary Fact Fuel

`vault/refs/vault/quest/references/content.md` § Secrets & Clues Fuel
already mines `vault/refs/ideas/creating-secrets-and-clues.md` in
full — read its **Historical secrets** category there rather than
duplicating the list here. Same core discipline applies here as
there: **write the fact
abstract from its place of discovery** — a sentence the DM can drop in
wherever play goes, not gated to one scene or NPC in advance.

## Narrative Curses, Taboos, and Prophecies

`vault/refs/gameplay-toolbox.md` § Curses and Magical Contagions →
**Narrative Curses** — unclaimed elsewhere in this repo (`encounter-prep`
and `.claude/skills/draft-content/references/location.md` only cite this file's
mechanical/environmental sections). Use when a lore page's fact is a
curse, a broken taboo, or a prophecy nearing its hour:

- A narrative curse manifests when a creature violates a taboo (breaking
  a vow, defiling a tomb, murdering an innocent) and receives a
  supernatural punishment — DM-designed, or a customized mechanical
  curse type.
- The affected creature should know *why* it's punished and be able to
  learn *how* to end it — typically by symbolically righting the wrong.
- **Should feel rare, potent, and rooted in campaign lore** — this is
  the test for whether a curse belongs on a lore page at all: a one-off
  spell effect isn't lore; a taboo the whole culture organizes around
  is.
- Whether *Remove Curse* (or similar) fully lifts it, only suppresses
  it, or does nothing is the DM's call per curse — state it explicitly
  on the page rather than leaving it to be improvised cold.

This is the narrative/cultural framing only — a curse's actual save DCs
and mechanical effect (if it needs one at the table) are `rule-prep`'s
or `encounter-prep`'s craft; cross-reference rather than duplicating a
mechanical write-up here.

## Cosmology, Pantheon, and Culture Fuel

No dedicated external source covers pantheon/cosmology design directly —
build from `.claude/skills/draft-content/references/lore.md`'s Hard Rules instead of a
prompt table: name what's currently active about a deity's portfolio or
a culture's custom before writing flavor text. A pantheon entry with no
living worshipper, no active tension, and no way for a PC to have heard
of it is the anti-pattern this guide exists to prevent.

## Legend Subtype Detail

A `subtype: legend` fact carries more than one in-world account of the
same event (the FR Wiki's Asgorath article: three separate origin myths
for dragonborn creation) — state each account as it's actually told,
naming who tells which version and why, then name the DM's own ground
truth (or explicit call that none is settled) separately from the
in-world accounts. Never silently pick one telling as "the truth" without
flagging that the others are, in-world, believed just as sincerely.

## Strongest Objection for DM-Only Synthesis

Mirrors `vault/refs/vault/quest/references/output.md`'s register — read
that one too if unsure of the tone. A lore page's hidden truth — a secret
behind a public myth, an inferred historical connection no source states
outright — is a DM-only synthesized conclusion, not something grepped
from the wiki. Every one of these names its **strongest objection**: the
reading where the connection is coincidental, forced, or unsupported by
what's actually established. Follow it with a testable, greppable search
(`npm run search:content -- search "<terms>"` or `grep -ril "<terms>"
vault/ vault/campaigns/shattered-sea/pcs/`) that could confirm or
falsify it — never an invented citation. A synthesized conclusion that
can't name its own strongest objection hasn't earned its place on the
page.

## Worked Example (fixture — placeholder names, not real campaign content)

User: "I need the lore behind why Harborwatch sailors won't say the word
'anchor' on a launching ship."

Standard queries come back empty for `"The Unspoken Anchor"` (the chosen
name) across `vault/ vault/campaigns/shattered-sea/pcs/` and
`vault/episodes/*/transcript.md` — clean to create. Confirmed genuine
lore, not tied to an existing NPC/faction/place. Interview: no single PC
connects yet — DM call that it's foundational Harborwatch
culture-texture; there IS something active (a ship that broke the custom
sank in living memory, which is why it's taken seriously now, not just
superstition).

```markdown
---
type: lore
status: pending
publish: false
aliases: ["The Unspoken Anchor"]
created: 2026-07-30
updated: 2026-07-30
tags: []
---

# The Unspoken Anchor

## The Fact

Harborwatch sailors never say "anchor" while a ship is still tied to
dock — they say "the iron" instead, and a newcomer who says the wrong word
gets more nervous looks than laughs. The custom actually dates to the
wreck of the *Second Tern*, a ship whose captain mocked the superstition
publicly the morning she launched — she sank within sight of the harbor an
hour later. Sailors don't believe the word itself is cursed; they believe
mocking the custom in front of the crew is what invites bad luck, because
it means the captain isn't taking the crew's fear seriously.

**What's active:** a captain planning to break the custom publicly (to
prove a point, or out of arrogance) is a live social draw — the crew's
reaction is the actual content, not the superstition itself.

**PC connection:** foundational Harborwatch dockworker/sailor culture
texture — no single PC thread yet; flag if one develops.
```
