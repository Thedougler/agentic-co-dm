
# Draft — Deity

A god, demigod, patron, great spirit, or mythos entity **as it is
worshipped** — what it holds dominion over, how mortals experience it, and
how it is served. Every worshipped power belongs here, never on `type: lore`
— a myth or prophecy with no active-worship dimension is the only part that
stays `lore`, and an index listing several deities stays `lore` too
(`vault/campaigns/shattered-sea/lore/shattered-sea-pantheon.md`). Done means
the DM can run this deity's presence at the
table — its presence, its worship, and any active Front — from this page
alone.

## Template

`vault/_templates/_campaigns/_deity.md` — copy it. Headings fixed and in
order: `## Portfolio & Presence · ## Worship · ## Relationships`
(OPTIONAL — delete outright if no other deity has a stated relationship
yet) `· ## Goals & Fronts` (OPTIONAL — delete outright if no front has
real content yet).

## Read first — all four, before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` — the prep craft floor.
2. `.claude/skills/composing-beats/references/audits.md` — PC agency, NPC/deity independence.
3. `vault/refs/vault/_common/hard-rules.md` — shared rules; bind this type,
   never restated below.
4. `vault/refs/vault/_common/queries.md` — run the stub check now, paste
   the output.

`DF1: <four files read, stub-check output pasted>`.

## Hard rules — this type only

- **Worshipped, Not Just Mythic.** This type is for a power **as
  worshipped** — a live domain, a manifestation stance, worship practice a
  party can encounter. A myth, prophecy, or origin story about the entity
  with no active worship dimension is `type: lore` instead; a deity page
  that has drifted into pure myth-retelling belongs there, not here.
- **Institution Boundary.** The god itself is this type. A church, cult,
  or clergy organized enough to have its own leadership, membership, and
  goals is a separate `type: faction` page, linked from `## Worship` by
  `[[wikilink]]` — never described as though the deity and its institution
  were one page.
- **Commit To One Presence Stance.** `## Portfolio & Presence` states
  exactly one working stance for how directly this deity acts in the
  world (never seen, felt only through omen or weather, speaks through
  clergy, walks among mortals) — never hedges across several at once
  (the Clock Decision Rule's sibling for deities: pick the real answer,
  don't leave it soft).
- **`worship_status` Is Its Own Key.** Track whether this deity currently
  has real worship in play in `worship_status:
  active|dormant|forgotten|usurped` only; don't duplicate it in `status`
  or prose.
- **Every Deity Has A Portfolio.** `domains:` is never empty — a page with
  nothing to put there is not yet a deity page; it's still a lore fact
  about a name.

## Interview — this type only

Ask with `vault/refs/vault/_common/interview.md`'s shared questions:

- The domains — what does this deity actually hold, in this setting's own
  vocabulary (never a borrowed D&D domain list)?
- The presence stance — how directly does this deity act, right now, in
  this campaign?
- Does this setting use an alignment axis at all? If not, delete the
  `alignment:` key rather than leaving it blank.
- Any other deity this one is ranked against, allied with, or opposed to
  (the Relationships section)?
- A [[vault/refs/vault/faction/references/front|front]] right now (the
  Clock Decision Rule, `.claude/skills/draft-content/references/faction.md`)? None yet ->
  delete `## Goals & Fronts` outright.
- `worship_status` right now? Template default is `active`; correct if
  wrong.

## Before you ship

- [[vault/refs/vault/_common/lifecycle|Lifecycle]]: `vault/refs/vault/_common/lifecycle.md`
- Gaps: `vault/refs/vault/_common/degrade.md`
- [[vault/refs/vault/_common/handoffs|Handoffs]]: `vault/refs/vault/_common/handoffs.md`
- Boundaries: `vault/refs/vault/_common/out-of-scope.md`
- Common checklist: `vault/refs/vault/_common/checklist.md`
- Deity checklist: `vault/refs/vault/deity/references/checklist.md`

## Reference files

| File | Read when |
|---|---|
| `vault/refs/vault/faction/references/front.md` | Writing a front — full template, lifecycle, quest-link rule |
| `.claude/skills/draft-content/references/faction.md` | Deciding whether this deity's church needs its own `faction` page |
| `.claude/skills/draft-content/references/lore.md` | Deciding whether content belongs here or as a myth/prophecy `lore` page |
| `vault/refs/vault/deity/references/checklist.md` | Deity-only checklist additions |
