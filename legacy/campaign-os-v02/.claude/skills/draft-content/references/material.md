
# Draft — Material

A raw substance or trade good, counted by weight, volume, or dose rather
than held as one discrete thing. Absorbs ores, metals, reagents, flora,
food and drink, and drugs or poisons sold as goods, plus any generic trade
commodity that doesn't fit those buckets. Done means the DM can name its
form, its worth, and where a party gets some, straight from frontmatter.

## Template

`vault/_templates/_srd/_material.md` — copy it. Headings fixed and in
order: `## Properties · ## Uses · ## Trade` (OPTIONAL — delete outright if
no established market exists yet).

## Read first — all four, before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` — the prep craft floor.
2. `.claude/skills/composing-beats/references/audits.md` — a material never decides, feels,
   thinks, or wants (the Player Character Boundary).
3. `vault/refs/vault/_common/hard-rules.md` — the shared and mechanical-type
   rules bind this type, never restated below.
4. `vault/refs/vault/_common/queries.md` — run the stub check now, paste the
   output.

`DM1: <four files read, stub-check output pasted>`.

## Hard rules — this type only

- **The Item-vs-Material Boundary.** A made thing a PC can hold and own
  as one discrete object — a sword, a ring, a potion already bottled and
  finished — is `item` (`vault/_templates/_srd/_item.md`,
  `.claude/skills/draft-content/references/item.md`); the substance or stuff it's made
  from or out of, counted by weight or volume and traded as a commodity,
  is `material`. The star-iron a smith forges into a sword is a
  `material`; the finished sword is an `item`. The moment a page states
  attunement, a single owner, or a fixed set of powers, it has crossed
  into `item` territory and belongs on that template instead.
- **The Poison-vs-Condition Boundary.** A poison as a tradeable good, its
  dose, its price, how someone applies it, is `material`. What that
  poison does to a victim once it lands, the actual mechanical or
  narrative affliction, is `condition`
  (`.claude/skills/draft-content/references/condition.md`). Cross-link the two; never fold
  the effect into `## Uses` here.
- **Worth Needs a Real Benchmark.** Before setting `worth:` -> name one
  comparable real trade good already on the page's stub check or in
  `vault/campaigns/shattered-sea/**`, and set the number relative to it.
  A number invented with no comparison is a guess, not a value.
- **`form` Is Descriptive, Not a Fork.** `form:` sorts a page for
  filtering; it never spawns a separate template or a separate section
  set. A food, an ore, and a poison all use the same three headings.

## Interview — this type only

Ask with `vault/refs/vault/_common/interview.md`'s shared questions:

- The concept — what concretely is this substance, and which `form`
  (ore, metal, reagent, flora, food, drink, poison, commodity, other)?
- The Item-vs-Material Boundary — is this the raw stuff, or already a
  finished, held thing? The latter -> stop, this belongs on `item`
  instead.
- What's it for (`## Uses`)? A poison -> name the good only; its effect
  goes on a `condition` page instead (the Poison-vs-Condition Boundary).
- `unit`/`worth` right now, with the real benchmark that justifies the
  number?
- Does a market for it exist yet? None -> delete `## Trade` outright
  rather than leaving it empty.

## Before you ship

- [[vault/refs/vault/_common/lifecycle|Lifecycle]]: `vault/refs/vault/_common/lifecycle.md`
- Gaps: `vault/refs/vault/_common/degrade.md`
- [[vault/refs/vault/_common/handoffs|Handoffs]]: `vault/refs/vault/_common/handoffs.md`
- Boundaries: `vault/refs/vault/_common/out-of-scope.md`
- Common checklist: `vault/refs/vault/_common/checklist.md`
- Material checklist: `vault/refs/vault/material/references/checklist.md`

## Reference files

| File | Read when |
|---|---|
| `.claude/skills/draft-content/references/item.md` | Deciding the Item-vs-Material Boundary for a specific page |
| `.claude/skills/draft-content/references/condition.md` | Writing a poison's mechanical effect (the Poison-vs-Condition Boundary) |
| `vault/refs/vault/material/references/checklist.md` | Material-only checklist additions |
