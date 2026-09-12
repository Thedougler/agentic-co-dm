
# Draft — Handout

The prop itself — an in-world document's verbatim text, ready to read
aloud or hand across the table — plus what the DM does because of it.
The test: could a player hold this and read every word on it? No formal
TTRPG handout standard exists; ground the shape in the real document's
own genre convention — a letter's salutation/body/closing, a
case file's summary/statement/evidence. That variation is prose craft
owned by `draft-story`, not page-schema — the template's `form:` enum
absorbs it without a per-genre substructure.

## Template

`vault/_templates/_handouts/_handout.md` — copy it, never retype it from
memory, and owns this page's layout; this guide never adds or reorders a
heading or block. No Player-Known/DM Only split: `publish:`/`status:` on
the page itself is the visibility gate, not a heading name; handling
notes flow in plain prose below the document text, never a separate
heading (`.claude/skills/composing-beats/references/runtime-surface.md` §8).

## Read first — before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` — the prep craft floor.
2. `vault/refs/vault/_common/hard-rules.md` — the shared rules bind
   this type, never restated below.
3. `vault/refs/vault/_common/queries.md` — run the stub check now:
   `grep -ril "<document name/concept>" vault/ vault/campaigns/shattered-sea/pcs/`
   and `grep -rl --include=transcript.md -i "<document name/concept>" vault/episodes/`.
   A hit → expand that page in place, never duplicate. Empty output is
   informative, not conclusive — escalate through `llm-wiki-query`'s
   tiers first (the entity may live under an alias).

`DH1: <three files read, stub-check output pasted>`.

## Hard rules — this type only

- **Verbatim, Never A Paraphrase.** The `[!read-aloud]` box holds the
  document's own words, verbatim. Can't yet state the concept as actual
  document text → it isn't ready to build.
- **Chain-Load Draft-Story For Prose.** Drafting the document's own
  words → chain-load `draft-story` (not `dnd5e-scene-narration`, which
  drafts scene narration, not a document's own text). Load `callouts`
  (`.claude/skills/callouts/references/read-aloud.md`) for the container.
- **The At-Table Verb Test.** Writing the handling note → name the verb
  the DM performs because of it (reveal, withhold, say). No verb →
  delete the note rather than fill it with background trivia. Plain
  prose, no callout — the dm-box format is retired (`.claude/skills/callouts/SKILL.md`).
- **State Facts Plainly, No Provenance.** Canon lives in frontmatter only
  (`vault/CLAUDE.md` rule 2) — never add a Sources/Provenance section or
  narrate where the document came from.
- **Forgery Gets Real Wording.** A forged letter still gets the forger's
  actual wording in the `[!read-aloud]` box; the forgery and its tell go
  in the handling note below, never folded into the "real" text as a
  hedge.

## Interview — this type only

Ask with `vault/refs/vault/_common/interview.md`'s shared questions:

- What does the document say, verbatim — or what's it close enough to
  now that the actual wording can be drafted?
- Who's it from, and is it genuine or forged?
- What's the document's `form:` (letter, contract, wanted poster, ship's
  papers, map key, prophecy, menu, broadsheet)?
- What must the DM reveal, withhold, or say because of it — the at-table
  verb, or explicitly none?

## Before you ship

- Lifecycle — `vault/refs/vault/_common/lifecycle.md`
- Gaps — `vault/refs/vault/_common/degrade.md`
- [[handoffs|Handoffs]] — `vault/refs/vault/_common/handoffs.md`
- Boundaries — `vault/refs/vault/_common/out-of-scope.md`
- Then — `vault/refs/vault/_common/checklist.md`

## Cross-skill coordination

- **The document also carries 5e mechanics** (a cursed contract, a map
  key that's a magic item) → `.claude/skills/draft-content/references/item.md` owns that
  page; this page wikilinks to it rather than duplicating the
  mechanics.
- **The document's content is background/reference knowledge with no
  physical prop a player holds** → that's
  `.claude/skills/draft-content/references/lore.md`'s page, not a handout.
- **Tied to a named NPC (author, forger, sender) or location** → confirm
  that page exists (`.claude/skills/draft-content/references/npc.md`/
  `.claude/skills/draft-content/references/location.md`) and wikilink both directions;
  this guide never authors the NPC or location page itself.
- **Requested as a session prop** → `draft-run-guide` may quote this
  handout once it exists; the page still starts `status: draft`/
  `pending` until `transcript-ingest` confirms it was actually given.

## Out of scope

- An item's own mechanics or balance — `.claude/skills/draft-content/references/item.md`.
- NPCs, locations, factions, quests — their own drafting guides.
- Anything already `status: canon` — `canon-review`'s territory.
- Writing `given_to:`, `given_in_session:`, `status: canon`, or
  `publish: true` — `transcript-ingest`'s and PUBLISH's move
  exclusively.

## Owned paths

`vault/campaigns/shattered-sea/handouts/<name>.md` — `status: draft`
while incomplete, `status: pending` once the document text and its
handling note are finished. Never sets `status: canon`, `given_to:`,
`given_in_session:`, or `publish: true` — those flip only once the
document is actually handed to players at the table,
`transcript-ingest`'s move alone (`vault/refs/runbook-wiki.md` § Who
writes what).
