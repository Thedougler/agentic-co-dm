---
name: lore-design
description: >-
  Write, edit, or create named lore pages for the campaign wiki. Use when a
  lore note, world truth, history, belief, rumor, legend, doctrine, custom, law,
  cosmology, prophecy, revelation, missing named lore note, Current Truth,
  discovery path, or table-facing lore handle needs a persistent page. Fill
  wiki/templates/lore.md.
---

# Lore Design

## Work Gate

Prep only. Follow `docs/agents/work.md`.

Show a chat proposal before writing a campaign wiki page. Write under `wiki/`
only after DM acceptance. If a needed named lore note is missing, that lore page
is work to do now: propose it instead of treating the missing note as out of
scope. Ground invention in wiki pages and/or D&D campaign patterns; set
`invention: true`, cite `[[pages]]`, and show contradictions. Never invent table
history or present invention as established wiki fact.

## Lore Job

A lore page answers one durable question about the world: what is true, why it
matters, how the characters can notice or use it, and what it explains or warns
about. The page is done when one question, At a Glance, Current Truth, and At
the Table are filled without another format guide.

Create or edit a named lore page when the truth has a durable identity and
players can witness, investigate, misunderstand, exploit, challenge, fear,
teach, bargain over, or return to it. Store the note under the campaign wiki
folder that owns this kind of lore.

Keep one-off color, item properties, spell history, vehicle lore, faction
history, place backstory, and quest context in the owning page until the lore
has its own durable question. Actual items stay `type: item`; ingest remapping
belongs outside this skill.

## Procedure

### 1. Retrieve The Lore

Read the brief, `wiki/templates/lore.md`, and relevant session, place, faction,
NPC, quest, item, spell, vehicle, creature, and prior lore notes. Preserve
established names, witnessed facts, party knowledge, in-world accounts,
exceptions, contradictions, sources, and open questions.

Write one question before the page:

> What does this lore let the DM answer or the players act on?

If the answer is several unrelated truths, split them into linked notes. If the
answer depends on table history, use only events the notes establish; otherwise
mark it as invention or an open canon question.

### 2. Start From The Template

Copy `wiki/templates/lore.md`. Keep its frontmatter and headings unless an
unused template section says it may be omitted. Fill these frontmatter fields:

```yaml
type: lore
lifecycle: proposed
reveal: unrevealed
campaign: <campaign slug>
visibility: dm
kind: <fact|history|belief|rumor|legend|doctrine|custom|law|cosmology|prophecy|revelation>
truth: <established|partial|contested|false|unknown>
scope: "<where, when, or for whom this is true, or blank>"
region: "<known region or blank>"
era: "<known era or blank>"
summary: "<one runnable sentence>"
```

Do not add a second lore template. Do not set lifecycle or reveal to canon-level
status before the players interact with or witness the lore.

### 3. Fill The Page

Fill `> [!abstract] At a Glance`:

- **Core truth:** the smallest useful answer to the durable question.
- **Why it matters:** the decision, danger, opportunity, relationship, or
  interpretation this truth changes.
- **Scope:** where, when, or for whom the truth applies, when bounded.

Fill `## Current Truth` with what is actually true now in complete sentences.
Separate fact from interpretation. Link important people, factions, places,
objects, events, creatures, spells, and other lore concepts that already have
their own notes. Record limits, exceptions, unknowns, and impossibilities when
they change play.

Fill `## At the Table` with the handles that make the lore usable:

- **Players notice:** an observable sign, behavior, phrase, symbol, consequence,
  or environmental detail.
- **This explains:** a linked page, event, mystery, practice, or condition the
  players may misread.
- **This enables:** a choice or course of action that becomes possible once the
  characters understand the lore.
- **This warns of:** a danger or consequence attentive characters can anticipate.

Omit unused optional sections. Use `## Who Knows`, `## Accounts`, `## Discovery`,
`## History`, `## If This Is Changing`, `## Consequences`, `## Connections`,
`## Open Canon`, and `## Sources` only when they help run play or preserve a
real source.

### 4. Handle Discovery And Canon

For hidden or contested lore, write revelations as conclusions the players can
reach, not scenes they must follow. Give structurally important revelations
multiple independent clues from plausible sources; background revelations can
stay lighter.

Lore remains changeable prep until players interact with or witness it. Omit
`## Canon Log` until that happens. After table witness, Campaign Editor /
`reconciling-session-evidence` (not `session-wrapup`) updates Current Truth and
appends Canon Log rows. `session-wrapup` only files the narrative recap.

## Craft Basis

Use lore as a table tool, not an encyclopedia entry: one portable truth, visible
signs, player choices, and consequences. Practical inputs: Justin Alexander's
revelation and clue practice, Mike Shea's secrets-and-clues prep, and
situation-based campaign prep that records current truth and pressure instead
of scripting future plot.

## Done

The page is done when:

- It fills `wiki/templates/lore.md` without adding another template.
- It has `type: lore` and is not remapped to `type: item`.
- It answers one durable question; unrelated truths are split into linked notes.
- At a Glance states the core truth and why it matters.
- Current Truth states what is actually true now.
- At the Table includes notice, explains, enables, and warns handles.
- Pre-witness lore stays proposed/unrevealed and changeable by the DM.
- Canon Log is omitted until players interact with or witness the lore.
- Table history is cited from notes or left open; it is not invented.
- Invention is labeled, cited, and proposed for DM acceptance.
