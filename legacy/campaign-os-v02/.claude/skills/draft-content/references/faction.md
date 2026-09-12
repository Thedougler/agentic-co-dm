
# Draft — Faction

An organisation with a goal, a method, and — when its agenda advances on its own timeline — a front (a clock with a trigger and a consequence). Done means the DM can run every front from `Goals & Fronts` alone.

## Template

`vault/_templates/_srd/_faction.md` — copy it. Headings fixed and in order: `## Members · ## Goals & Fronts` (OPTIONAL — delete outright if no front has real content yet).

## Read first — all four, before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` — the prep craft floor.
2. `.claude/skills/composing-beats/references/audits.md` — PC agency, NPC independence.
3. `vault/refs/vault/_common/hard-rules.md` — shared rules; bind this type, never restated below.
4. `vault/refs/vault/_common/queries.md` — run the stub check now, paste the output.

`DF1: <four files read, stub-check output pasted>`.

## Hard rules — this type only

- **Defines, Never Advances.** Agenda advancement—ticking a clock, resolving off-screen moves, or changing canonical state—belongs in `world-update` post-[[vault/refs/runbook-ingest|INGEST]], not in this guide.
- **Front Ownership.** A front with no owning faction -> instantiate a faction page for an organisational actor, or file it on the most relevant existing entity page for a lone NPC or place-bound hazard; never invent a new page type for an ownerless pressure.
- **The Clock Decision Rule.** A front only if the agenda advances independently of the party; no ticking clock means backdrop, not a front.
- **`faction_status` Is Its Own Key.** Track operational state in `faction_status: active|dormant|dissolved` only; don't duplicate it in `status` or prose.
- **Fielded Forces Carry Numbers.** A faction that fields armed forces states their strength as real numbers -> the shared Calibrate Against The Real Party rule governs them, so read `vault/campaigns/shattered-sea/pcs/*.md` frontmatter and paste party stats before finalizing any of them.
- **Families Are Factions.** A family, dynasty, or lineage is a faction: an organisation whose members share blood.
- **Religions As Institutions.** A religion or church as an institution is a faction; the god it worships is a `deity` (`.claude/skills/draft-content/references/deity.md`). A pantheon page is an index of deity pages, and belongs to whichever of the two it actually is — an organisation, or a list.

## Interview — this type only

Ask with `vault/refs/vault/_common/interview.md`'s shared questions:

- The concept — what holds them together? None yet -> offer `vault/refs/vault/faction/references/content.md` § Organization Concepts.
- A front right now (the Clock Decision Rule)? None yet -> offer `vault/refs/vault/faction/references/content.md` § Front Archetypes.
- Per front: core tension in one sentence, running now or waiting on a named trigger, what happens at fill.
- `faction_status` right now? Template default is `active`; correct if wrong.

## Faction fields

Five fields — `primary_goal`, `consistent_method`, `active_problem`, `off_screen_action`, `performance_hooks` — one table, DM-only material, no frontmatter duplication. Fields: `vault/refs/vault/faction/references/toy.md`. Front mechanics: `vault/refs/vault/faction/references/front.md`.

## Magic grounding

Whenever this page describes a faction-level supernatural mechanic, ritual, or organized magical effect a player spell (Detect Magic, Identify, Counterspell, Dispel Magic) could interact with — add a `> [!mechanic]` callout. Fill only the fields that apply; omit the rest.

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

- [[vault/refs/vault/_common/lifecycle|Lifecycle]]: `vault/refs/vault/_common/lifecycle.md`
- Gaps: `vault/refs/vault/_common/degrade.md`
- [[vault/refs/vault/_common/handoffs|Handoffs]]: `vault/refs/vault/_common/handoffs.md`
- Boundaries: `vault/refs/vault/_common/out-of-scope.md`
- Common checklist: `vault/refs/vault/_common/checklist.md`
- Faction checklist: `vault/refs/vault/faction/references/checklist.md`

## Reference files

| File | Read when |
|---|---|
| `vault/refs/vault/faction/references/toy.md` | Filling any Faction field |
| `vault/refs/vault/faction/references/front.md` | Writing a [[vault/refs/vault/faction/references/front\|front]] — full template, lifecycle, quest-link rule, `faction_status` |
| `vault/refs/vault/faction/references/content.md` | Sparking a concept or front, detailing leadership, `performance_hooks` fuel |
| `vault/refs/vault/faction/references/example.md` | A full worked fixture, stub check through a completed front |
| `vault/refs/vault/faction/references/checklist.md` | Faction-only checklist additions |
| `vault/refs/ideas/villains-and-themes.md` | Villain interiority for faction leadership |
