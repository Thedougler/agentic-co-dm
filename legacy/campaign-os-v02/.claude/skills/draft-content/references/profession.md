
# Draft — Profession

A trade, occupation, rank, office, or honorific that exists in the setting
independent of any one character — a blacksmith, a harbor pilot, a
Chancellor of the Exchequer, a knighthood. Absorbs every trade, job title,
rank, office, and honorific this vault needs a page for; none of those get
their own type. Done means a reader can tell what someone in this
profession does, how they got there, and what it costs or earns them.

## Template

`vault/_templates/_srd/_profession.md` — copy it. Headings fixed and in
order: `## Nature · ## Entry & Advancement · ## Standing · ## Marks &
Removal` (OPTIONAL — delete outright if no real insignia/removal content
fills it yet).

## Read first — all four, before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` — the prep craft floor.
2. `.claude/skills/composing-beats/references/audits.md` — PC agency, NPC independence.
3. `vault/refs/vault/_common/hard-rules.md` — shared rules; bind this type, never restated below.
4. `vault/refs/vault/_common/queries.md` — run the stub check now, paste the output.

`DP1: <four files read, stub-check output pasted>`.

## Hard rules — this type only

- **Job, Not Package.** [[vault/refs/vault/background/GUIDE|background]]
  (`vault/_templates/_srd/_background.md`) is the mechanical
  character-creation package a PC picks at creation — ability scores, a
  feat, proficiencies, starting equipment. A `profession` is the in-world
  job itself: any number of [[vault/refs/vault/location/references/npcs|NPCs]]
  hold it, it exists whether or not a PC
  can take it as a background, and it never carries character-creation
  mechanics. A profession that also has a matching background package
  links to it inline; the mechanics stay on the background page.
- **Setting-Wide, Not Guild-Internal.** [[vault/refs/vault/faction/GUIDE|faction]]
  holds the organisation; a rank that only means something inside one
  faction's own membership stays on that faction's `## Members` or
  `## Goals & Fronts` instead of forking a `profession` page. A
  `profession` page exists only
  for a trade practiced across the setting, or a rank/office/honorific
  recognised beyond a single organisation's own membership (a knighthood
  the crown grants, a title multiple noble houses can hold, a guild
  mastership several chapters recognise).
- **One Shape, Every Kind.** Trade, rank, office, and honorific share one
  template — never fork a narrower sibling template for any of them.
  `## Nature` carries the distinction (day-to-day activity for a trade,
  function and authority for a title) in prose, not in a new heading or
  frontmatter key.
- **Earnings Stay Setting-Native.** `## Standing`'s Typical earnings line
  is stated in this setting's own currency unit, never a D&D-mechanical
  wage table — a profession page carries no game-mechanical stat block.

## Interview — this type only

Ask with `vault/refs/vault/_common/interview.md`'s shared questions:

- The concept — what concretely does someone in this profession do, or
  what does this title grant its holder? None yet -> ask what it looks
  like in practice rather than picking a default.
- Trade or title (the Job, Not Package rule and the Setting-Wide rule) —
  does this belong here at all, or on a background page (mechanical
  package) or a faction's own membership (guild-internal rank)?
- Entry: how is it obtained, and is there a recognised path upward?
- Standing: what does it pay or cost, and how is someone in it actually
  treated?
- Marks & Removal: is there real insignia or a real way to lose it, or is
  the heading better deleted for this page?

## Before you ship

- [[vault/refs/vault/_common/lifecycle|Lifecycle]]: `vault/refs/vault/_common/lifecycle.md`
- Gaps: `vault/refs/vault/_common/degrade.md`
- [[vault/refs/vault/_common/handoffs|Handoffs]]: `vault/refs/vault/_common/handoffs.md`
- Boundaries: `vault/refs/vault/_common/out-of-scope.md`
- Common checklist: `vault/refs/vault/_common/checklist.md`
- Profession checklist: `vault/refs/vault/profession/references/checklist.md`

## Reference files

| File | Read when |
|---|---|
| `.claude/skills/draft-content/references/background.md` | Deciding whether a job also needs a character-creation background package |
| `.claude/skills/draft-content/references/faction.md` | Deciding whether a rank is guild-internal (stays on the faction page) or setting-wide (belongs here) |
| `vault/refs/vault/profession/references/checklist.md` | Profession-only checklist additions |
