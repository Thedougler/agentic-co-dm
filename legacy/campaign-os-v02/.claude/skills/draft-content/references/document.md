
# Draft — Document

An in-world text — a book, tome, letter, treaty, contract, recording, or
inscription — that exists whether or not it is ever shown at the table.
Grounded in World Anvil's Document article genre (a record of anything
containing written or recorded content: books, letters, recordings,
illustrations) and Call of Cthulhu's Mythos tome convention (a text with
real weight and, sometimes, a real effect on whoever studies it). Done
means `## Text` holds the document's actual words, or states plainly why
it doesn't yet.

Routes here: any in-world text with weight beyond a single scene —
referenced by an NPC, tied to a quest or faction, something the party
might learn *of* before ever holding it. A prop invented purely for one
scene, with no in-world history and no reason to persist past it, stays a
`handout` alone (`.claude/skills/draft-content/references/handout.md`) — the Handout
Boundary below decides which.

## Template

`vault/_templates/_campaigns/_document.md` — copy it. Headings fixed and
in order: Text, Origin, Effects Of Reading. Text is OPTIONAL only when
the words are lost, destroyed, or not yet drafted; state which, never
leave it empty. Effects Of Reading is OPTIONAL; delete it outright if
reading the document does nothing beyond what it says.

## Read first — all four, before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` — the prep craft floor.
2. `.claude/skills/composing-beats/references/audits.md` — PC agency, NPC independence.
3. `vault/refs/vault/_common/hard-rules.md` — shared rules; bind this type, never restated below.
4. `vault/refs/vault/_common/queries.md` — run the stub check now, paste the output.

`DD1: <four files read, stub-check output pasted>`.

## Hard rules — this type only

- **The Handout Boundary.** A `document` is the in-world text itself; a
  `handout` is that text staged as a physical table prop. One text, one
  home for its words: `document`'s `## Text` holds them canonically, and
  a `handout` built from an existing document transcludes that section
  (`![[<slug>#Text]]`) rather than retyping it. A text with no in-world
  existence beyond one scene — invented for the table, never referenced
  by an NPC or tied to a quest/faction — stays a `handout` alone; don't
  force a `document` page onto it. Building a handout from a document
  that already exists → transclude, never duplicate.
- **Verbatim, Never A Paraphrase.** `## Text` holds the document's own
  words. Can't yet state the concept as actual document text → it isn't
  ready to build (mirrors the handout guide's own rule).
- **Origin Is In-World, Not Meta.** `## Origin` states the document's
  in-world creation — author, date, circumstance — never a note about how
  the DM sourced it or when it was added to the wiki (git log is that
  history, `.claude/rules/docs.md`).
- **Author Is A Wikilink Or Explicit Unknown.** `author:` names a
  resolvable `[[wikilink]]` to the NPC, faction, or deity that wrote or
  issued it; genuinely anonymous or unattributed in-world → state that
  explicitly rather than leaving the field blank.
- **Effects Live On Their Own Page.** A real numeric or mechanical effect
  from reading/studying/carrying this document belongs on that effect's
  own `item` (`.claude/skills/draft-content/references/item.md`) or `rule`
  (`rule-prep` skill) page, linked from `## Effects Of Reading` — never
  duplicated as stat text here.
- **Chain-Load Draft-Story For Prose.** Drafting the document's own words
  → chain-load `draft-story` (not `dnd5e-scene-narration`, which drafts
  scene narration, not a document's own text).

## Interview — this type only

Ask with `vault/refs/vault/_common/interview.md`'s shared questions:

- The concept — what concretely is this document (the `form:` value:
  book, tome, letter, treaty, contract, recording, or inscription)? None
  yet → ask what it looks like rather than picking a genre for the DM.
- The Handout Boundary — does this text have real in-world weight beyond
  one scene, or is it purely a table prop? Purely a prop → stop, this
  belongs on a `handout` page instead, not here.
- Already exists as a `handout` page? → this document's `## Text` becomes
  the source of truth; edit the handout to transclude it
  (`![[<slug>#Text]]`) instead of carrying its own copy.
- Who wrote or issued it, and is that known in-world (`author:`)?
- What does it actually say, verbatim — or what's it close enough to now
  that the actual wording can be drafted?
- Does reading, studying, or carrying it do anything beyond what it says
  (`## Effects Of Reading`)? Nothing → delete the heading outright.

## Before you ship

- [[vault/refs/vault/_common/lifecycle|Lifecycle]]: `vault/refs/vault/_common/lifecycle.md`
- Gaps: `vault/refs/vault/_common/degrade.md`
- [[vault/refs/vault/_common/handoffs|Handoffs]]: `vault/refs/vault/_common/handoffs.md`
- Boundaries: `vault/refs/vault/_common/out-of-scope.md`
- Common checklist: `vault/refs/vault/_common/checklist.md`
- Document checklist: `vault/refs/vault/document/references/checklist.md`

## Reference files

| File | Read when |
|---|---|
| `.claude/skills/draft-content/references/handout.md` | Deciding the Handout Boundary, or building a table-prop version of this document |
| `.claude/skills/draft-content/references/item.md` | This document also carries real 5e mechanics (a cursed contract, a magic scroll) |
| `vault/refs/vault/document/references/checklist.md` | Document-only checklist additions |
