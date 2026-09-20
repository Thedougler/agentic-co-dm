---
name: spell-design
description: >-
  Write, edit, or create named spell pages for the campaign wiki. Use when a
  spell needs a persistent page, missing named spell, casting narration,
  classification, 2024 rules effect, discovery source, or spell history. Fill
  wiki/templates/spell.md.
---

# Spell Design
## Boundary contract

### Input

Take a named spell owner, the caller's objective, the relevant brief,
`wiki/templates/spell.md`, and linked caster, source, and 2024 peer evidence.
The owner is a durable spell identity with a runnable effect, not a scroll item
or a prose-only magical flourish.

### Owner-specific Work

Work only the spell: establish the identity sentence, preserve canon, write
perceivable narration, and fill concrete casting fields plus the peer-anchored
2024 effect. Keep Discovery/Lore on this page when needed; label invention and
route checks, saves, and adjudication to the mechanics owner.

### Capability Handoff

Hand off only a bounded seam (for example, casting checks to
`dnd5e-mechanics`, a scroll/item to `dnd-5e-magic-item-design`, a place to
`place-design`, or spoken delivery to `theatre-of-the-mind`) with the spell
owner, parent objective, evidence, and exact section requested. Require return
evidence naming the child artifact/section and completion result; resume spell
work only after that seam satisfies the spell contract, otherwise report the
missing evidence or blocker.

### Done

Use the existing `## Done` checklist below. Completion is observable when the
named spell page path, spell-template and runnable-effect checks, narration and
mechanics routing, and any child return evidence are reported.


Prep only. Follow `docs/agents/work.md`.

## Refuse gates

- **Work gate.** Show a chat proposal before writing under `wiki/`. Write only
  after DM acceptance. Workspace outputs allowed before acceptance. A missing
  named spell is work to propose now — not out of scope.
- **Invention.** Never present invention as wiki fact. Set `invention: true` (or
  mark proposed), cite `[[pages]]`, show contradictions, propose for acceptance.
  No silent canon — including invented provenance, ancient-druid origin myths, or
  undeclared doctrine tied to established lore.
- **Template lock.** Copy `wiki/templates/spell.md` only. Fill narration,
  classification, casting fields, and runnable effect with substance — not empty
  headings or blank Casting Time/Range/Components/Duration labels.
- **Narration.** `> [!narration] Narration` is theatre of the mind: what a
  bystander sees, hears, and feels. No secrets, DCs, unearned names, or DM
  plumbing in player-facing prose — move those to DM-facing sections.
- **Identity first.** Before the page draft:

  > This is a [level/school] spell that [table effect], recognized by
  > [casting signature], and it gives players [choice or pressure].

  If that lacks table effect, source, or consequence, keep retrieving or ask.
- **Peer anchor.** Anchor level, damage, control, and range against 2024 peers of
  the same level and role. Reskin a close spell when canon is silent; mark
  material changes as invention. Refuse packing nova into a cantrip — raise level
  or redesign.
- **No auto-win.** Refuse no-roll, no-choice, no-cost spells that skip climax or
  confrontation. Effects need failure modes, costs, limits, or contested
  resolution.
- **No proprietary paste.** Never paste WotC Player's Handbook (or equivalent)
  spell text verbatim. Use SRD-safe paraphrase, reference-by-name, or original
  homebrew marked invention.
- **Scroll ≠ spell page.** Do not cite or treat `spell-scroll-*.md` item pages as
  `type: spell` exemplars.
- **Discovery/Lore stay here.** When filled, they remain on the spell page — not
  separate `type: lore` notes. Label invented history.

## Spell job

A named spell page is runnable casting look + classification + exact 2024 effect.
Use when the spell has durable identity players can learn, cast, seek, identify,
counter, fear, bargain for, research, or return to. Store under
`wiki/<campaign>/spells/`. Keep one-off magical color on the owning beat, place,
NPC, or item until it has a name or recurring consequence.

## Build the spell

1. **Retrieve.** Brief, `wiki/templates/spell.md`, and relevant caster/faction/
   place/item/teacher/book/patron/hazard/prior-spell notes. Preserve established
   names, level, school, components, limits, sources, open questions. Do not
   contradict established wiki facts.
2. **Identity sentence** before drafting (see refuse gate).
3. **Scaffold.** Copy `wiki/templates/spell.md`. Frontmatter: `type: spell`,
   lifecycle/reveal/campaign/visibility, `level`, `school`, `ritual`, `summary`.
4. **Runnable fill.** Narration (perceivable); Level/School/(Ritual); Casting
   Time, Range, Components, Duration with concrete 2024 values; one short effect
   block (save/attack, DC, damage, conditions, targets/area, Concentration
   breakpoints, end, scaling when it scales).
5. **Discovery / Lore only when needed.** Source, access cost, clue, and change
   on obtain — or history that changes a present choice. Omit unused.

Read `references/spell-craft.md` for craft basis, section fill detail, audit
questions, and failure modes.

## Handoffs

Narration → `theatre-of-the-mind`; items/scrolls → `dnd-5e-magic-item-design`;
places → `place-design`; lore pages → `lore-design` (spell Discovery/Lore stay on
the spell page); vault lookup → `.agents/skills/qmd`.

## Done

- Fills `wiki/templates/spell.md` under `wiki/<campaign>/spells/` with
  `type: spell`; no second template.
- Identity sentence before draft; narration perceivable-only.
- Level/school/ritual filled; casting fields concrete; effect peer-anchored and
  runnable — no cantrip-nova, auto-win, or proprietary paste.
- Discovery/Lore on-page only when needed; invention labeled/cited/proposed;
  wiki write only after accept.
- DM can cast/adjudicate tonight without a format guide.
