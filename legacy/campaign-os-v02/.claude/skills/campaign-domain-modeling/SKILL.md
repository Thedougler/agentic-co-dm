---
name: campaign-domain-modeling
description: >-
  Maintain the campaign's ubiquitous language and record DM rulings in a Campaign OS repo
  (vault/ present). Use when naming a campaign concept, place, faction, or term of art; two
  pages use different words for the same thing; a DM ruling ("per DM ruling", "DM decided")
  binds more than one page; or an undefined term surfaces. Owns the glossary and docs/rulings/ —
  never campaign facts.
---

# campaign-domain-modeling

Actively sharpen the *campaign's* ubiquitous language — the words the table uses and the rulings the
DM makes — the moment they crystallise, so a term of art or a house ruling never evaporates into
a lint config or a scattered `[!mechanic]` box. This is the campaign counterpart of
the global `domain-modeling` skill; that one owns the *system/process* vocabulary (`CONTEXT.md`,
`docs/adr/` — read `vault/refs/domain.md`), this one owns the *fiction's* vocabulary.

## Two owned artifacts, created lazily

Both live under `docs/` — deliberately not wiki content, so template law L4 and `status:`
tiers do not apply, and neither is ever published. Create each only when the first real entry exists.

### The campaign glossary — the campaign's ubiquitous language

One entry per contested word. Format:

```md
**Rattkin**:
The rat-descended folk of the undercity — the campaign's canonical name for the species.
_Avoid_: ratfolk, rat-folk, rat people
[[Rattkin]]
```

- `**Term**:` + a 1–2 sentence definition of what it IS, + `_Avoid_: <synonyms parked as losers>`,
  + a `[[wikilink]]` to the owning wiki page where one exists (omit the link when no page owns it).
- The glossary owns the *word*, never the *fact* — each fact lives on exactly one wiki page (CLAUDE.md
  project rule 6); a glossary entry that restates page content gets cut to a definition + wikilink.
- Terms of art, mechanics vocabulary, naming choices, and table shorthand only. An entity that
  deserves a page gets a page (via its prep skill / `content-type-scaffold`) — then a glossary line
  only if its *name* is contested, never as a second home for the entity's facts.

### `docs/rulings/NNNN-slug.md` — DM rulings as campaign-ADRs

One file per ruling that binds more than one page or the table itself. Format:

```md
# Trolls and the regeneration house rule

The DM ruled that fire or acid damage suppresses any creature's regeneration for one round,
not only trolls'. Chosen over a troll-only carve-out so the table has one rule to remember.
Reverses cleanly mid-campaign, but every regenerating stat block already tuned to it would need re-checking.

_Applies to_: [[Regeneration]] (the rule page)
```

- Sequential numbering: scan `docs/rulings/` for the highest `NNNN`, increment by one.
- 1–3 sentences is a complete ruling. Add optional `Status` / `Considered options` / `Consequences`
  only when they earn it.
- Offer a ruling file sparingly — write one only when all three hold: hard to reverse, surprising
  without context, and the result of a real trade-off. Any one missing → no file.
- A ruling that binds a **single page's** mechanics goes in a `[!mechanic]` callout on that page
  (the `callouts`-skill convention), not here — a rulings file records only rulings that bind more
  than one page or the table itself: tone doctrine, house mechanics, taxonomy decisions.
- The file records the *decision* — that it was ruled, why, what was rejected, the reversal cost — and
  wikilinks to the page carrying the mechanic; it never restates the mechanic (same split as code vs ADR).

## During the session

- **Challenge against the glossary, grounded in L1.** Before challenging a term, grep the
  campaign glossary for `<term>` and paste the hit: "The glossary defines X as …, you seem to mean Y —
  which?" No paste, no challenge (a memory-based challenge invents a definition that was never agreed).
- **Sharpen fuzzy or overloaded terms.** When one word carries two concepts, propose one canonical
  term and park the losers under `_Avoid_` — "you're saying 'the Detonation' for both the event and
  the weapon; pick one word per concept."
- **Stress-test with at-the-table scenarios.** Probe a proposed ruling with a concrete table case:
  "a player asks whether trolls also lose regeneration under this — what does the ruling say?" Force
  the boundary to be stated, not assumed.
- **Cross-reference with the wiki, not code.** `grep -rni "<term>" vault/ --include='*.md'`;
  a page contradicting the stated definition/ruling is surfaced. A *word* conflict resolves here; a
  *fact* conflict is routed to `canon-review` — this skill never adjudicates facts.
- **Update GLOSSARY.md inline the moment a term resolves; never batch** (a batched term is a lost
  term). GLOSSARY.md is a glossary and nothing else — no mechanics text, no campaign facts, no scratch
  notes; a line that is not a definition + `_Avoid_` + wikilink does not belong in it.

## Standard queries

```
grep -n "<term>" <campaign glossary file>
ls docs/rulings/
grep -rni "<term>" vault/ --include='*.md' -l
```

A lookup that comes back empty or noisy escalates to `llm-wiki-query` rather than concluding "not
defined" or "no page for this."

## Owned write scope

Writes only the campaign glossary file and `docs/rulings/NNNN-*.md` — nothing else. For a
single-page ruling it advises placing a `[!mechanic]` box, but the box itself is written by whoever
owns that page edit, under WIKI.md rules. Never edits `vault/` or `vault/campaigns/shattered-sea/pcs/` directly, never flips
`publish:` or `status:` on any page (those verbs belong to PUBLISH and to
`transcript-ingest`/world-update/canon-review).

## Boundaries — where each thing belongs

- System/process vocabulary (pipeline, wiki mechanics, skills) → global `domain-modeling`
  (`CONTEXT.md` / `docs/adr/`), not the campaign glossary.
- A *fact* contradiction between pages → `canon-review`; this skill resolves the word, never the fact.
- Tag vocabulary (`docs/tags.md`) → `tag-taxonomy`, not the glossary.
- Page structure and frontmatter → the type template / `content-type-scaffold`.
- The mechanic's own content → the owning wiki page: `rule-prep` for a table-wide house rule, the
  entity page's `[!mechanic]` box for a page-scoped one. A ruling file records the decision and
  wikilinks to that page; it never carries the mechanic's text.
