
# Draft — Culture

A learned, shared way of life a people carries: ethnicity, customs,
traditions and rituals, dress, cuisine-as-custom, and festival-as-
institution. Done means a DM can run the culture's daily texture and its
standing institutions straight from the page.

## Template

`vault/_templates/_campaigns/_culture/_culture.md`, copy it. Headings
fixed and in order: `## The Culture · ## Customs & Traditions` (OPTIONAL,
delete outright if no recurring institution has real content yet)
`· ## Naming` (OPTIONAL, delete if this culture has no naming convention
of its own) `· ### Deliberate Silences` (OPTIONAL).

### Subtype: language

A culture's own naming conventions (personal names, place names, the
sounds that mark a name as belonging to it) stay on the culture page's
`## Naming` section.

Once a language has its own script, speaker base, dialects, or grammar
worth recording — not just how it names people and places — it routes to
its own page: `type: culture, subtype: language`,
`vault/_templates/_campaigns/_culture/_culture_language.md`.

Headings fixed and in order: `## The Language · ## Script & Speech`
(OPTIONAL, delete if genuinely nothing beyond "spoken, no script" is
known yet) `· ## Speakers & Dialects` (OPTIONAL, delete if no dialectal
spread is understood yet) `· ## Sample Phrases & Names` (OPTIONAL, delete
if no sample material exists yet) `· ### Deliberate Silences` (OPTIONAL).

A culture page links out to its language's page rather than duplicating
script or dialect detail inline.

## Read first, all four, before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md`, the prep craft floor.
2. `.claude/skills/composing-beats/references/audits.md`, PC agency, NPC independence.
3. `vault/refs/vault/_common/hard-rules.md`, shared rules, bind this type,
   never restated below.
4. `vault/refs/vault/_common/queries.md`, run the stub check now, paste the
   output.

`DF1: <four files read, stub-check output pasted>`.

## Hard rules, this type only

- **Culture Absorbs, Species Does Not.** Biology, traits, and mechanical
  ancestry stay on the `species` page. Everything a people learns and
  shares (customs, dress, cuisine, values, rites, festivals-as-
  institution) belongs here instead. A culture page that starts
  describing darkvision or a creature-type trait has drifted onto
  `species` territory. Move it.
- **Institution, Not Incident.** A one-off celebration that happened on a
  specific date is an `event` page, linked from `## Customs & Traditions`.
  The recurring institution that produces it (the festival's rules, its
  yearly rhythm, what it means to the people who run it) is written here.
  A festival with only one instance so far still gets written as the
  institution, not the incident, the moment it is understood to recur.
- **`peoples` Names Who Holds It, Or Is Deleted.** Fill `peoples` with
  every species or community that actually holds this culture. A
  culture with no fixed membership (a trade-network in-group, a
  diaspora) deletes the key rather than forcing a species onto it.
- **`within` Names A Home, Or Is Deleted.** Fill `within` only when this
  culture is rooted in one region or settlement. A culture that spans many
  ports or has no single home deletes the key instead of picking one
  arbitrarily.

## Interview, this type only

Ask with `vault/refs/vault/_common/interview.md`'s shared questions:

- Who holds this culture? One or more species, or a cross-species
  community. None yet named -> ask, never default to the nearest species
  page.
- Rooted in one place, or does it travel? Decides whether `within` is
  filled or deleted.
- Any customs or traditions active right now, a rite coming due, a custom
  under strain? None yet -> `## Customs & Traditions` is deleted, not left
  empty.
- A naming convention of its own? None yet -> `## Naming` is deleted, not
  left empty.

## Before you ship

- Lifecycle: [[vault/refs/vault/_common/lifecycle|Lifecycle]]
- Gaps: `vault/refs/vault/_common/degrade.md`
- Handoffs: [[vault/refs/vault/_common/handoffs|Handoffs]]
- Boundaries: `vault/refs/vault/_common/out-of-scope.md`
- Common checklist: `vault/refs/vault/_common/checklist.md`
- Culture checklist: `vault/refs/vault/culture/references/checklist.md`

## Reference files

| File | Read when |
|---|---|
| `vault/refs/vault/culture/references/checklist.md` | Culture-only checklist additions |
