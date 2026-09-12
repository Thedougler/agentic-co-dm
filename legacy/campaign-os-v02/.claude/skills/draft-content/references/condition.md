
# Draft — Condition

The world-fact side of an affliction: what a disease, curse, mutation,
madness, or lasting poison-effect concretely is, how it spreads or was
inflicted, and what it does to whoever carries it — never the numbers
that resolve it at the table. This type absorbs all five categories under
one flexible template; it is never split into disease/curse/mutation/
madness sibling templates, sections and this guide's own judgment carry
the difference instead. Done means the DM can narrate the affliction —
its onset, its spread, its cure — from this page alone.

## The rule-vs-condition boundary

A mechanical `condition` subtype already exists under `type: rule` —
`vault/_templates/_srd/_rule.md`'s `subtype: condition`, owned by
`.claude/skills/rule-prep/SKILL.md`. The two never merge:

- **`type: rule, subtype: condition`** holds the mechanics: what the
  affliction does to a character sheet — the numeric ceiling (DC,
  damage dice, duration, saves-per-day), the RAW precedent it sits
  beside, labeled `[RAW]`/`[HB]`. No in-world narrative.
- **`type: condition`** (this type) holds the world-fact: what the
  affliction concretely is, how it spreads or was inflicted, who carries
  it, what it means in the setting. No numbers.

**Which page a given affliction's detail goes on:** a fact resolves at
the table with a die roll or a fixed number → the `type: rule` page. A
fact is true in the world regardless of whether it's ever rolled (this
plague started on a specific ship; this curse marks its victims with a
grey streak in their hair) → this page. An affliction that needs both
gets both pages, cross-linked: this page's `## Cure & Mechanical Effect`
closes with a `[[rule-slug]]` link to its `type: rule` counterpart, or
states "no mechanical effect — narrative only" when no table mechanics
exist yet. Never invent the numeric page's content here, and never
narrate in-world flavor on the `type: rule` page.

## Template

`vault/_templates/_srd/_condition.md` — copy it. Headings fixed and in order: Nature, Onset & Symptoms, Transmission & Origin, Cure & Mechanical Effect. None are OPTIONAL — every condition has an origin (even "unknown"), a transmission or infliction mechanism, and a cure state (even "no known cure") worth stating plainly.

## Read first — all four, before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` — the prep craft floor.
2. `.claude/skills/composing-beats/references/audits.md` — PC agency, NPC independence.
3. `vault/refs/vault/_common/hard-rules.md` — shared rules; bind this type, never restated below.
4. `vault/refs/vault/_common/queries.md` — run the stub check now, paste the output.

`DF1: <four files read, stub-check output pasted>`.

## Hard rules — this type only

- **The Rule-vs-Condition Boundary.** Run the test above before writing
  anything. A page that states a DC, a damage die, or a duration belongs
  on the `type: rule, subtype: condition` page instead — never duplicate
  those numbers here.
- **What This Type Absorbs.** Diseases, curses, mutations, madnesses, and
  poisons tracked as a lasting effect (not a single save) all route
  here. Never fork a new sibling template for one of these categories —
  `## Nature` states which this page is.
- **`condition_status` Is Its Own Key.** Track the affliction's current
  state in the world in `condition_status: active | dormant | cured`
  only; don't duplicate it in `status` or prose — same discipline as
  `threat_status`/`faction_status`. `active` means it is currently
  affecting or able to affect carriers; `dormant` means present but not
  currently manifesting or spreading; `cured` means eradicated or no
  longer capable of affecting anyone in this campaign.
- **No Mechanics Without a Rule Page.** Never write a save DC, a damage
  die, or any other number on this page, even provisionally — the
  `## Cure & Mechanical Effect` closing line either links the real
  `type: rule` page or says plainly that none exists yet.

## Interview — this type only

Ask with `vault/refs/vault/_common/interview.md`'s shared questions:

- The concept — what concretely is this affliction, and which of the
  five absorbed categories (disease, curse, mutation, madness,
  poison-effect) is it? None yet → ask what an onlooker would notice
  first, rather than picking a category for the DM.
- Does it need table mechanics (a save, a DC, a lasting numeric effect)?
  Yes and no `type: rule, subtype: condition` page exists yet → flag it
  as a gap rather than inventing numbers on this page.
- `condition_status` right now? Template default is `active`; correct if
  wrong.
- Onset timing and any staged progression — filled from what the DM
  already knows, never invented wholesale.

## Before you ship

- [[vault/refs/vault/_common/lifecycle|Lifecycle]]: `vault/refs/vault/_common/lifecycle.md`
- Gaps: `vault/refs/vault/_common/degrade.md`
- [[vault/refs/vault/_common/handoffs|Handoffs]]: `vault/refs/vault/_common/handoffs.md`
- Boundaries: `vault/refs/vault/_common/out-of-scope.md`
- Common checklist: `vault/refs/vault/_common/checklist.md`
- Condition checklist: `vault/refs/vault/condition/references/checklist.md`

## Reference files

| File | Read when |
|---|---|
| `vault/_templates/_srd/_rule.md` | Before writing anything — confirms whether this affliction's numbers belong on a separate `subtype: condition` rule page |
| `.claude/skills/rule-prep/SKILL.md` | Drafting or linking the mechanical counterpart page |
| `vault/refs/vault/condition/references/checklist.md` | Condition-only checklist additions |
