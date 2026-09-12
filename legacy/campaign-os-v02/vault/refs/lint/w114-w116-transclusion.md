---
type: agent-guidance
status: pending
publish: false
aliases: []
created: "2026-08-03"
updated: "2026-08-10"
tags: [combat]
summary: "W114 operative-transclusion coverage, W115 naming-substitute, W116 broken embed heading — what each protects and how to clear it on a session moment or scene page."
uid: fe2107fb-6da8-4655-9c27-18592af75612
---

# W114–W116 — Operative transclusion coverage & embed integrity

All three are scoped to session moment and scene files
(`vault/episodes/NNN/moment-N-*.md`, `vault/episodes/NNN/scene-N-*.md`)
except W116, which applies
to any `vault/**`, `pcs/**`, `sessions/**` page.

## W114 — operative-transclusion coverage

Protects: a moment or scene that references a sibling `type: encounter`
page (same episode directory) must `![[page#Heading]]`-embed every *operative*
heading that encounter page carries — Run Sheet, Tactical Notes, Raising
the Stakes, Lowering the Stakes, Endings (the full list is the
`OPERATIVE_HEADINGS` constant) — so the page runs cold at the table with
no mid-round lookup hop to a different file.

### Fix — W114

Add `![[<encounter-page>#<Heading>]]` for each missing operative heading,
placed where the beat actually spends those numbers — placement is a
judgment call (`draft-moment` Hard Rule 7), not mechanical; only headings
the target page actually carries are required.

## W115 — naming-substitute

Protects: a naming-discipline note telling the DM never to say a name
aloud at the table ("naming discipline", "never say X aloud") must carry
a quoted table-safe substitute within the next few lines — otherwise the
DM has to invent one live, mid-scene.

### Fix — W115

Add a quoted substitute plus a marker word beside the tell, e.g.:

> Table-safe substitute: "the Foul One"

The line needs both a marker (substitute/call it/instead/table-safe) and
a quoted phrase within the lookahead window to clear.

## W116 — embed heading resolves

Protects: a `![[page#Heading]]` transclusion whose heading doesn't exist
on the target page renders as a broken embed in Obsidian, exactly where
the runner expected real content mid-play.

### Fix — W116

Open the target page, find its actual current heading text, and repoint
the embed to match exactly (case-insensitive). This fires most often after
a heading rename on the target page that the embedding page's `#Heading`
fragment never followed.

### Edge cases

- Block refs (`#^block`) and non-`.md` embeds (images, audio) are out of
  scope for W116.
- An embed pointing at a page that doesn't resolve at all is W85/W18's
  finding, not W116's — W116 only fires once the target page itself
  resolves but the heading on it doesn't.
