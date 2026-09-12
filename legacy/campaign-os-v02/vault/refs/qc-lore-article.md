---
type: agent-guidance
status: pending
publish: false
aliases: []
created: "2026-08-03"
updated: "2026-08-03"
tags: [craft]
summary: "QC profile for a vault/ page with type: lore."
uid: 13fc4285-f3bc-4cbe-b525-a7d36ee8a858
---

# QC profile: lore-article

For `type: lore` pages — everything the wiki-page profile checks, plus the two contracts that make lore worth having.

Template: `vault/_templates/_srd/_lore.md`. Base checks: all categories in `vault/refs/qc-wiki-page.md` (TEMPLATE, ONE-FACT-ONE-PAGE, WIKILINK, AGENT-COMMENT, STATUS, META, SLOP) apply unchanged — run them first, then the two below.

| CATEGORY | Contract | How to check |
|---|---|---|
| DEPTH | The article teaches or reveals something usable at the table — a fact the DM can play, a lever, a countdown, a secret with consequences — or explicitly declares itself atmospheric texture with no draw; never ambiguous between the two. Lore that only restates what other pages already establish, or that decorates without adding anything runnable, fails. | Ask: what could a DM do at the table with this page that they couldn't before? Quote the usable fact, or the explicit no-draw declaration, or fail. |
| DRAW | The article connects to at least one active entity — a PC's thread, a live faction, an in-motion quest — in the spirit of `.claude/skills/composing-beats/references/runtime-surface.md`'s PC-connection standard, or carries the DM's explicit call that it's foundational world-texture with none; never a silent default. | Name the connected entity and quote the connecting line, or quote the explicit no-connection call, or fail. |
