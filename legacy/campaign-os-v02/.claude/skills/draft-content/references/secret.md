
# Draft — Secret

A concealed thing attached to a place, a person, or an organisation — a
waterfall hiding a chest, a false wall behind a bookshelf, a second ledger
under the counted one — narrated exactly like ordinary texture until a
player actively looks. Done means the page's own read-aloud text gives away
nothing and the DM has a real DC to run at the table.

## Template

Two templates, one spine. Headings fixed and in order, none optional:
`## Presentation · ## Concealment · ## Discovery · ## Reveal`. This guide
never adds or reorders a heading.

| Copy | When |
|---|---|
| `vault/_templates/_campaigns/_secret_cache.md` | Something is stored here — the reveal hands the party item(s). Carries `subtype: cache` and `contains:` |
| `vault/_templates/_campaigns/_secret.md` | Everything else — a passage, a hidden room, a concealed identity, a truth screened by a habit. No `subtype:`, no `contains:` |

## Read first — all four, before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` — the prep craft floor.
2. `.claude/skills/composing-beats/references/audits.md` — PC agency, NPC independence.
3. `vault/refs/vault/_common/hard-rules.md` — the shared rules bind this
   type, never restated below (this type also states a DC, so its
   mechanical-types section binds too).
4. `vault/refs/vault/_common/queries.md` — run the stub check now, paste
   the output.

`DF1: <four files read, stub-check output pasted>`.

## Hard rules — this type only

- **Presentation Never Tells.** The Presentation read-aloud box reads
  exactly like any other background-texture description at the same site —
  no lingering camera, no tell-adjective. A DM skimming ahead shouldn't be
  able to tell this page differs from an ordinary one.
- **Never Published.** `publish: false`, always. A secret page reaching the
  player site is the one failure this type cannot recover from.
- **Reward, Never Gate.** Optional content for a curious party. If the plot
  needs what's behind this, the Three-Clue Rule binds: two further
  independent routes to the same conclusion must exist elsewhere, or it's a
  chokepoint, not a secret — route it to the location or quest page instead.
- **Two Thresholds, Not One.** State the passive Perception number a party
  moving through without searching would need to beat, distinct from the
  active `[!check]` DC a player must choose to roll.
- **Notice, Then Work Out.** Perception finds that something is there; a
  second check opens it only when defeating the concealment is a separate
  act from spotting it. Never write the second box to fill the shape.
- **Calibrate The DC.** About to invent one from vibes → read
  `vault/refs/table-random-traps.md`'s Save DC tiers or
  `vault/refs/gameplay-toolbox-traps.md` and cite the tier against the
  party's real level.
- **Item Needs Its Own Page First** (`subtype: cache`). `contains:`
  wikilinks resolve to a real item page — `.claude/skills/draft-content/references/item.md`
  builds it first if it doesn't exist yet, then hands back the wikilink; add
  the reciprocal `found_at:` there pointing here.
- **Host Already Exists.** `within:` resolves to a real page — the location,
  room, NPC, or faction this is attached to; this guide never authors that
  page itself.

## Interview — this type only

Ask with `vault/refs/vault/_common/interview.md`'s shared questions:

- What ordinary-looking feature or behaviour screens this (the Concealment
  truth)?
- What's behind it — item(s) (`subtype: cache`, wikilinked, built by
  `.claude/skills/draft-content/references/item.md` first if they don't exist), or a
  passage, room, identity, or truth?
- Passive Perception threshold, and the active check's skill + DC?
- Once noticed, does it still have to be worked out — a second check with
  its own skill and DC — or is spotting it the whole act?
- Which page is this attached to (`within:`)?
- Is this genuinely optional, or does something downstream depend on
  finding it (Reward, Never Gate)?

## Before you ship

[[vault/refs/vault/_common/lifecycle|Lifecycle]] `vault/refs/vault/_common/lifecycle.md` · gaps
`vault/refs/vault/_common/degrade.md` · handoffs
`vault/refs/vault/_common/handoffs.md` · boundaries
`vault/refs/vault/_common/out-of-scope.md` · then
`vault/refs/vault/_common/checklist.md` plus:

- [ ] `## Presentation` box read back once as if this page didn't exist — no
      word in it hints anything is there.
- [ ] `publish: false`.
- [ ] `within:` resolves to a real, already-existing page (quoted, full
      vault-relative wikilink).
- [ ] `subtype: cache` only — `contains:` wikilink(s) resolve to a real item
      page, with that page's `found_at:` pointing back here, and the Reveal
      box names every one of them.

## Out of scope

The item's own mechanics, rarity, and provenance belong to
`.claude/skills/draft-content/references/item.md`. The place or person this sits inside
belongs to that type's own guide; this guide only links to it.

Information with no physical concealment and no fixed location belongs
elsewhere. A fact to dispense wherever the party happens to be is a `quest`
page's Secrets & Clues. The same list scoped to one night is the run
guide's. A story already in circulation is `lore`'s rumour subtype. The
standing index of what players don't know yet is
`vault/campaigns/shattered-sea/spoilers.md`.

A trivial one-off DC bullet stays inline on the host page. Only a
concealment worth reusing, revisiting, or handing off on its own earns a
`secret` page.
