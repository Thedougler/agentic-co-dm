---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "How the quest's Secrets & Clues, Beats, and Outcome sections map onto the template, plus the Strongest Objection rule for DM-only conclusions."
created: "2026-08-03"
updated: "2026-08-15"
tags: [mystery]
uid: d87e61ba-d645-4510-bde8-04094f2d503e
---

# Quest Output Structure Reference

How `## Secrets & Clues` maps onto `vault/_templates/_srd/_quest.md`'s fixed headings.
Read this while filling it for the first time.

**`## Secrets & Clues`** — everything that drives the quest, written
abstract from its place of discovery (LGMRD's Creating Secrets and
Clues — a line the DM can drop in wherever play goes, not gated to one
Beat). Content-functional, not a visibility split: `publish:`/`status:`
frontmatter already gates player-visibility at the page level, so this
section carries both what the table currently knows and what hasn't
surfaced yet, together.

- **Hook** — one paragraph, or a `[!read-aloud]` callout if it's delivered
  as a scene (hand the actual paragraph to `dnd5e-scene-narration`).
- **Stated objective** — what the party believes they need to do, in their
  own terms (this may differ from the true stakes below).
- **Structural pattern** — which one (The Structural Pattern Choice), and
  the specific notes that pattern's reference entry asks for (a Thread Map
  for Convergence, a seed list for Slow Burn, an Escalation Ladder rung,
  etc.).
- **True stakes / opposition** — what's really driving this, and who or
  what opposes the party, wikilinked to their own pages.
- **`link_of_relevance`** — the PC-Connection Requirement, one line each,
  wikilinked.
- **Prepped reveals** — anything the DM plans to surface as the quest
  progresses (a twist, a hidden backer, a Reversal condition). Any hidden
  conclusion needs the Three-Clue Rule (`.claude/skills/composing-beats/references/audits.md` §3) —
  `vault/refs/vault/quest/references/content.md` § Secrets & Clues Fuel has prompt categories if the
  DM needs clue material.

**Strongest Objection.** True stakes/opposition and Prepped reveals are
DM-only synthesized conclusions, not something grepped from the wiki —
name the strongest objection to each: the reading where the connection is
coincidental, forced, or unsupported by what's actually established. Follow
it with a testable search (`npm run search:content -- search "<terms>"` or
`grep -ril "<terms>" vault/`) that could confirm or falsify it, never
an invented citation. A synthesized conclusion that can't name its own
strongest objection hasn't earned its place on the page.

**`## Beats`** — starts with only the seed: the hook and the chosen
pattern's opening move (The Beats Handoff). Everything past the seed is
`draft-story`'s DS4 territory — don't pre-write a full
beat sequence here.

**`## Outcome`** — starts empty. Filled in only when `quest_status`
actually advances past `active` (The Quest Status Ladder), by
`transcript-ingest`, per session evidence — same discipline as `## Session
Log` elsewhere: don't pre-fill it, and a later contradiction gets a
`CONTRADICTION:` block, never a silent rewrite. When it is filled in, it
names what the party walks away with, not just whether they won —
`vault/refs/vault/quest/references/content.md` § Rewards has the prompt
categories (an item's own story, a situational-use item, a social reward)
if the DM needs fuel.
