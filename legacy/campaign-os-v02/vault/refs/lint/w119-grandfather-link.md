---
type: agent-guidance
status: pending
publish: false
aliases: []
created: "2026-08-04"
updated: "2026-08-04"
tags: [craft]
summary: "W119 grandfather links: a label slot naming an ancestor above the page's own parent, and how to retarget it."
uid: 1f424d7b-879f-451e-abcc-f867ec53dd19
---

# W119 — Grandfather links

Protects: the containment chain. A page connects to its own `parent:`;
a label slot naming an ancestor further up leaves the parent unlinked
everywhere it matters, so an island reads as sitting in the whole
archipelago rather than in the sub-region that holds it.

## What fires

- A containment row of an At-a-Glance table — the labels in the
  `CONTAINMENT_ROW_LABELS` constant (`Region`, `Parent Region`,
  `Location`, `Part Of`, `Parent`, `Found In`, `Sits In`) — whose cell
  links an ancestor
  above `parent:`.
- Any other table cell or list bullet that is a link with at most
  `LABEL_SLOT_MAX_RESIDUAL_WORDS` words around it, linking such an
  ancestor.

## Fix — W119

A cell holding that link and nothing else auto-fixes: `npm run lint --
<path>` retargets it to the page's own `parent:`, display text included.

Everything else is a judgment call. Retarget the slot to the parent when
the slot's job is naming what contains this page; unlink the ancestor
where a nearer place already carries the meaning. Never delete a link
that a sentence around it depends on — move the sentence instead.

## Edge cases — why an ancestor link might be correct

- Prose is exempt outright. A sentence that genuinely names an ancestor
  ("it looks like any other island of the [[midchain|Midchain]]") is the mention W25
  requires a link for; removing it trades one finding for another.
- A slot that links the parent alongside the ancestor is an address, not
  a skipped rung, and stays silent — `| Location | [[calveno|Calveno]],
  [[le-paludi|Le Paludi]] |` reads down the chain on purpose.
- A descriptive Detail cell in a `## Locations Within` table is prose
  that happens to sit in a table, and is not checked.
- A page whose parent sits at the top of the chain has no ancestor above
  it, and never fires.
