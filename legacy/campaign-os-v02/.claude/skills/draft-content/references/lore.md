
# Draft — Lore

The wiki's catch-all for reference material with no active agenda and no
place of its own — not a dumping ground. Its real external standard is a
Forgotten Realms Wiki history/legend article — prose, a
History section, and, for a genuine legend, multiple conflicting in-world
accounts of the same event (`subtype: legend`, e.g. Asgorath's competing
dragonborn-origin myths). A rumour (unverified gossip the party can hear
and investigate) is a distinct genre grounded in the GM-craft
rumour-table tradition, not this one — `vault/refs/vault/lore/references/rumour.md`.

## Template

`vault/_templates/_srd/_lore.md` — copy it, never retype it from memory.
Fixed heading: `## The Fact`. `### Deliberate Silences` OPTIONAL, only
when this lore intentionally leaves something unexplained.

## Subtype boundary (read before doing anything)

This type holds myth, legend, prophecy, dreams and visions, cosmology,
magic-system lore, and history including eras and timelines — reference
material with no active agenda, no temporal location, and no place of its
own. Lore answers "what is true about the world" and "what did the world
decide happened"; it does not answer "who rules now" or "what is about to
change."

Before creating a page, confirm it's genuinely lore and not one of these:

- A god itself → `.claude/skills/draft-content/references/deity.md`; the myths told about
  that god stay here.
- A way of life — customs, dress, cuisine, a recurring festival →
  `.claude/skills/draft-content/references/culture.md`.
- A timekeeping system, its months and cycles →
  `.claude/skills/draft-content/references/calendar.md`; the sequence of what happened
  stays here.
- A danger advancing on its own clock →
  `.claude/skills/draft-content/references/threat.md`.
- An active NPC, faction, or location's own history/secret → lives
  inline on *that* page, not a separate lore page.
- An item's mechanical or historical significance →
  `.claude/skills/draft-content/references/item.md`'s page.
- A dissolved-but-still-agenda-bearing organization →
  `.claude/skills/draft-content/references/faction.md` — "no active agenda" is the actual
  test, not "not currently on-screen."
- A recurring place the party revisits →
  `.claude/skills/draft-content/references/location.md`; a sea lane, road, or trade route →
  `.claude/skills/draft-content/references/route.md`.
- Unverified in-world gossip the party can hear and investigate →
  `vault/refs/vault/lore/references/rumour.md`, not this guide.
- Campaign overview or one-shot/module content → `.claude/skills/draft-content/references/campaign.md`.

## Read first — before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` — the prep craft floor.
2. `vault/refs/vault/_common/hard-rules.md` — the shared rules bind
   this type, never restated below.
3. `vault/refs/vault/_common/queries.md` — run the stub check now:
   `grep -ril "<lore topic/name>" vault/ vault/campaigns/shattered-sea/pcs/`
   and `grep -rl --include=transcript.md -i "<lore topic/name>" vault/episodes/`.
   A hit → expand that page in place, never duplicate. Empty output is
   informative, not conclusive — escalate through `llm-wiki-query`'s
   tiers first.

`DL1: <three files read, stub-check output pasted>`.

## Hard rules — this type only

- **PC Connection Or Explicit Foundational Call.** Writing `## The Fact`
  with no stated PC pull -> stop, name it: a specific PC's thread, or an
  explicit DM call that it's foundational world-texture with no single PC
  pull — never a silent default.
- **State Active Or Atmospheric.** Finishing a page's fact section without
  saying whether it's currently *active* (a countdown, a custom about to
  be tested, a debt coming due) or explicitly atmospheric texture with no
  hook -> stop, never leave it ambiguous.
- **Advance Independent Of Discovery.** A prophecy, custom, or historical
  clock -> let it advance whether or not the party ever learns of it
  (`.claude/skills/composing-beats/references/audits.md` §1).
- **Strongest Objection For DM-Only Synthesis.** A hidden truth
  recontextualizing a public myth is a DM-only synthesized conclusion,
  not something grepped from the wiki — name its **strongest objection**
  (the reading where the connection is coincidental, forced, or
  unsupported) and a testable, greppable search that could confirm or
  falsify it. A conclusion that can't name its own strongest objection
  hasn't earned its place on the page. Full detail:
  `vault/refs/vault/lore/references/content.md` § Strongest Objection.

## Interview — this type only

Ask with `vault/refs/vault/_common/interview.md`'s shared questions:

- What's the fact, in one sentence — cosmology, history, culture, legend,
  or prophecy?
- Confirm it's genuinely lore, not another page type's own history (§
  Subtype boundary) — does it belong to an existing NPC, faction, item,
  or place?
- Which PC or campaign thread does this pull on, or is it foundational
  world-texture with no single PC?
- Is there something currently active about this fact right now, or is
  it atmospheric texture with no hook?

Sparking a fact when the DM doesn't have one yet, or sharpening a
legend/prophecy/pantheon entry: `vault/refs/vault/lore/references/content.md`.

## Magic grounding

Whenever this page describes a supernatural effect, magic-system phenomenon, or cosmological mechanism a player spell (Detect Magic, Identify, Counterspell, Dispel Magic) could interact with — add a `> [!mechanic]` callout. Fill only the fields that apply; omit the rest.

| Field | Required | Notes |
|---|---|---|
| **Tradition** | yes | Arcane / Divine / Primal |
| **School** | yes | One of the eight SRD schools; `unclassifiable` for effects beyond the taxonomy |
| **Spell analogue(s)** | if meaningful | Closest SRD spell(s) or a named homebrew ritual |
| **Homebrew element** | if homebrew | One line on what it adds or differs from SRD |
| **Detect Magic** | yes | School + one sensory sentence, read-aloud ready |
| **Identify** | items and locations only | Full paragraph the DM reads aloud |
| **Counterspell** | if non-obvious | yes / no / not applicable + one-line reason |

Tradition taxonomy: [[magic-in-the-shattered-sea]].

## Before you ship

[[vault/refs/vault/_common/lifecycle|Lifecycle]] `vault/refs/vault/_common/lifecycle.md` · gaps
`vault/refs/vault/_common/degrade.md` · handoffs
`vault/refs/vault/_common/handoffs.md` · boundaries
`vault/refs/vault/_common/out-of-scope.md` · then
`vault/refs/vault/_common/checklist.md`.

## Out of scope

- An active entity's own history — its own page, not this guide.
- The campaign overview or a one-shot/module — `.claude/skills/draft-content/references/campaign.md`.
- Transcribing a source document — `llm-wiki-ingest`, which is
  fidelity-only: a claim with no source backing gets a stub, never an
  invented detail. This guide is the opposite, **inventing** new lore.
- Unverified gossip with a live, investigable question —
  `vault/refs/vault/lore/references/rumour.md`.

## Owned paths

`vault/campaigns/shattered-sea/lore/<slug>.md` — `status: draft` while
incomplete, `pending` once table-ready. Never writes to `vault/` directly
(`transcript-ingest`'s move, once played) and never sets `status: canon`
or `publish: true`.

## References

| File | Read when |
|---|---|
| `vault/refs/vault/lore/references/content.md` | Sparking a lore fact when the DM doesn't have one yet, or sharpening a legend/prophecy/pantheon entry |
| `vault/refs/vault/lore/references/rumour.md` | Unverified in-world gossip the party can hear, spread, and investigate, with a DM-known truth value |
| `vault/refs/vault/lore/references/rumour-content.md` | Sparking a rumour when the DM doesn't have one yet, or sharpening the field mapping |
