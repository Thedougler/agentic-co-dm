---
name: spell-design
description: >-
  Write, edit, or create named spell pages for the campaign wiki. Use when a
  spell needs a persistent page, missing named spell, casting narration,
  classification, 2024 rules effect, discovery source, or spell history. Fill
  wiki/templates/spell.md.
---

# Spell Design

## Work Gate

Prep only. Follow `docs/agents/work.md`.

Show a chat proposal before writing a campaign wiki page. Write under `wiki/`
only after DM acceptance. If a needed named spell is missing, that spell page is
work to do now: propose it instead of treating the missing note as out of
scope. Ground invention in wiki pages and/or 2024 D&D spell patterns; set
`invention: true`, cite `[[pages]]`, and show contradictions.

## Spell Job

A spell page makes a named spell runnable: what the casting looks like, what
kind of magic it is, and the exact 2024 effect the DM can adjudicate. The page
is done when narration, classification, and the effect block are filled without
another format guide.

Create or edit a named spell page when the spell has a durable identity and
players can learn, cast, seek, identify, counter, fear, bargain for, research,
or return to it. Store the note under:

`wiki/<campaign>/spells/`

Keep one-off magical color in the owning beat, place, NPC, or item until it has
a name or recurring consequence.

## Procedure

### 1. Retrieve The Spell

Read the brief, `wiki/templates/spell.md`, and relevant caster, faction, place,
item, teacher, book, patron, hazard, and prior spell notes. Preserve established
names, aliases, level, school, components, limits, sources, taboos, and open
questions.

Write one identity sentence before the page:

> This is a [level/school] spell that [table effect], recognized by [casting
> signature], and it gives players [choice or pressure].

If that sentence has no table effect, source, or consequence, keep retrieving or
ask for the missing premise before drafting the page.

### 2. Start From The Template

Copy `wiki/templates/spell.md`. Keep its frontmatter and headings unless an
unused template section says it may be omitted. Fill these frontmatter fields:

```yaml
type: spell
lifecycle: proposed
reveal: unrevealed
campaign: <campaign slug>
visibility: dm
level: "<cantrip or spell level>"
school: "<abjuration|conjuration|divination|enchantment|evocation|illusion|necromancy|transmutation>"
ritual: false
summary: "<one runnable sentence>"
```

Do not add a second spell template.

### 3. Fill The Playable Page

Fill `> [!narration] Narration` through theatre of the mind. It must say what a
bystander sees, hears, and feels at the casting in complete sentences. Keep
secrets, DCs, and unearned names out of player-facing prose.

Fill the classification line:

`Level, School (Ritual when it is a ritual)`

Fill the rules block in 2024 terms:

- **Casting Time.** Action, Bonus Action, Reaction trigger, minute, hour, or
  special timing.
- **Range.** Distance, self, touch, area origin, and target count.
- **Components.** V, S, M, costly or consumed material, and focus limits.
- **Duration.** Instantaneous, fixed duration, Concentration duration, or until
  discharged.

Then write one short effect block with every table consequence needed to run it:
save or attack, ability score, DC source, damage dice and type, healing,
condition, movement, object effect, area, target limits, repeated saves,
Concentration breakpoints, end condition, and scaling when it scales.

Anchor numbers against existing 2024 spells of the same level and role. Reskin a
close spell when canon is silent; mark material changes as invention.

### 4. Fill Discovery And Lore Only When Needed

Fill `## Discovery` when the spell needs a scroll, book, teacher, patron,
ritual site, faction archive, bargain, or other source. State where it can be
found, what access costs, what clue points there, and what changes when the
party gets it.

Fill `## Lore` when the spell needs history. State the old truth, who still
cares, what evidence survives, and how that history changes a present choice.

Discovery and Lore on a spell page stay on that spell page. They are spell
sections, not separate `type: lore` notes.

## Craft Basis

Use the 2024 spell-entry shape: casting time, range, components, duration, then
effect. Use DM-facing craft only to sharpen table utility: visible magic before
rules, compare against peer spells for level pressure, and keep prep runnable at
the table instead of exhaustively simulating edge cases.

## Done

The page is done when:

- It lives in `wiki/<campaign>/spells/` with `type: spell`.
- Narration, or an explicit theatre-of-the-mind handoff, gives visible casting
  experience without secrets, DCs, or unearned names.
- Level, school, and ritual status are filled in frontmatter and body.
- Casting time, range, components, and duration are filled.
- The 2024 effect block states saves or attacks, damage, conditions, target and
  area rules, duration end, and scaling when applicable.
- Discovery is filled when the spell needs a scroll, book, teacher, or patron.
- Lore is filled when the spell needs history.
- Invention is labeled, cited, and proposed for DM acceptance.
