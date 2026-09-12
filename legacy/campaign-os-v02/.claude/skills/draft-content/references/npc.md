
# Draft — NPC

A named individual with relationships and a story role. Done means the DM
can improvise this NPC from the `**Wants:**` line alone.

## Template

`vault/_templates/_campaigns/_npcs/_npc.md` — one shape for every NPC
regardless of `subtype:`, copy it, never retype it from memory. It alone
owns this page's headings and their order; this guide never adds or
reorders one.

## Read first — all four, before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` — the prep craft floor.
2. `.claude/skills/composing-beats/references/audits.md` — PC agency, NPC independence.
3. `vault/refs/vault/_common/hard-rules.md` — the shared rules; they
   bind this type and are never restated below.
4. `vault/refs/vault/_common/queries.md` — run the stub check now and
   paste the output.

`DN1: <four files read, stub-check output pasted>`.

## Hard rules — this type only

- **The Wants Line.** About to finalize -> the opening `**Wants:**` line is
  mandatory and derived, never independent: one bold-led sentence
  compressing the Toy Chest's `primary_goal` + `active_problem`. Write the
  Toy Chest first, then compress it.
- **The Opening Move.** About to finalize an NPC appearing in a session ->
  the Opening move line is mandatory and its physical hook is an action,
  never an attribute: job mid-way · who speaks first · their first line.
- **Relationships Are Links.** About to write `## Relationships` -> every
  connection is a `[[wikilink]]` verified by the stub check, never prose
  naming an entity without linking it.
- **The Quote Is Theirs.** One in-character sentence -> if it could belong
  to any NPC, rewrite it.

## Interview — this type only

Ask these in the same message as
`vault/refs/vault/_common/interview.md`'s shared questions:

- Race or species.
- `subtype:` — mandatory, `major | minor | recurring`; no default, ask
  rather than guessing.
- Role or function. A `villain`/`ally`/`rival`/`recurring`/`contact` answer
  fills the template's `role:` key; anything else stays prose, `role:`
  absent.
- Recurring antagonist needing a stat block? A yes routes to
  `vault/refs/vault/npc/references/villains.md`.
- Major or recurring NPC with an agenda that advances independently of the
  party? Apply the Clock decision rule
  (`vault/refs/vault/faction/references/front.md`) and write a
  Front into `## Goals & Fronts`. A `minor` NPC skips this — no ticking
  clock means backdrop.

## Toy Chest

Five fields — `primary_goal`, `consistent_method`, `active_problem`,
`performance_hooks`, `link_of_relevance` — written once as a table in the
DM-only material, no frontmatter duplication.
Fields: `vault/refs/vault/npc/references/toy.md`.
Layout: `vault/refs/vault/npc/references/output.md`.

## Magic grounding

Whenever this NPC has an ability, innate spellcasting, or trait a player spell (Detect Magic, Identify, Counterspell, Dispel Magic) could interact with — add a `> [!mechanic]` callout. Fill only the fields that apply; omit the rest.

| Field | Required | Notes |
|---|---|---|
| **Tradition** | yes | Arcane / Divine / Primal |
| **School** | yes | One of the eight SRD schools; `unclassifiable` for effects beyond the taxonomy |
| **Spell analogue(s)** | if meaningful | Closest SRD spell(s) or a named homebrew ritual |
| **Homebrew element** | if homebrew | One line on what it adds or differs from SRD |
| **Detect Magic** | yes | School + one sensory sentence, read-aloud ready |
| **Identify** | omit | NPC abilities do not receive an Identify block |
| **Counterspell** | if non-obvious | yes / no / not applicable + one-line reason |

Tradition taxonomy: [[magic-in-the-shattered-sea]].

## Before you ship

Lifecycle `vault/refs/vault/_common/lifecycle.md` · gaps
`vault/refs/vault/_common/degrade.md` · handoffs
`vault/refs/vault/_common/handoffs.md` · boundaries
`vault/refs/vault/_common/out-of-scope.md` · then
`vault/refs/vault/_common/checklist.md` and
`vault/refs/vault/npc/references/checklist.md`.

## Reference files

| File | Read when |
|---|---|
| `vault/refs/vault/npc/references/toy.md` | Filling any Toy Chest field |
| `vault/refs/vault/npc/references/output.md` | Laying out sections, sizing the read-aloud |
| `vault/refs/vault/npc/references/villains.md` | The NPC is a recurring antagonist |
| `vault/refs/vault/faction/references/front.md` | Writing a `## Goals & Fronts` Front for a major/recurring NPC |
| `vault/refs/vault/npc/references/social-checks.md` | Picking a worldview word or a social-check DC |
| `vault/refs/vault/npc/references/example.md` | A full worked page, interview to finished |
| `vault/refs/vault/npc/references/checklist.md` | The NPC-specific checks that run after the shared checklist — the Wants line, the five Toy fields, the Opening move. |
| `vault/refs/ideas/villains-and-themes.md` | Villain interiority beyond page mechanics |
| `vault/refs/stories/prose-and-character-craft.md` | The NPC-entrance moves for the read-aloud |
