---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "The hard rules every content type shares, cited by name rather than number, plus the extra rules binding any page that states mechanics or numbers."
created: "2026-08-03"
updated: "2026-08-15"
tags: [craft]
uid: fc831ff4-eae0-4355-af4a-9577210d511f
---

# Draft — Shared Hard Rules

These bind every type. A per-type guide adds its own rules on top and never
restates one from here. **Cite these by name, never by number** -> a numeric
citation breaks silently the moment a rule is added or reordered, and no
path checker can see the break.

## The Stub Check

About to create anything -> run `vault/refs/vault/_common/queries.md`
first and paste the output; expand an existing page in place rather than
duplicating it (`.claude/skills/composing-beats/references/runtime-surface.md` § Prep-entity floor).

## The PC-Connection Requirement

About to write the entity's connection field with no named PC -> stop and
ask. Name the specific PC, the thread of theirs it pulls on, and the
**mechanism** — the pressure this entity puts on that thread, never "ties
into the group's arc"
(`.claude/skills/composing-beats/references/runtime-surface.md` § Prep-entity floor). It lands in the page body, not
just working notes, so a later session can grep for it.

Genuinely nothing connects -> that is still a DM call, not a default. Ask.

## The Toy Field Discipline

About to fill any Toy field -> write vectors, behaviors, and situations,
never traits, personalities, or feelings
(`.claude/skills/composing-beats/references/runtime-surface.md` § Prep-entity floor). Goals are what the entity moves
toward regardless of the party; methods are table-doable in five seconds;
problems are situations, not feelings about them.

## The Template Heading Lock

About to add, remove, or reorder a template heading -> stop. Headings stay
fixed and in order, exactly as `_templates/<type>.md` states them.
Player-Known and DM-Only content share the same heading — `publish:` and
`status:` are the visibility gate (`.claude/skills/composing-beats/references/runtime-surface.md` § Prep-entity floor,
lint W20/W21). A genuinely hidden fact is written inline where its content
lives.

## The Player Character Boundary

About to write any part of the page -> write the entity's goal as a vector
advancing on its own timeline regardless of the party; never what a PC
decides, feels, thinks, or wants (`.claude/skills/composing-beats/references/audits.md` § Sandbox doctrine).

## The Three-Clue Rule

About to gate a conclusion the players must reach -> seed three independent
clues across different scenes or sources, never one roll
(`.claude/skills/composing-beats/references/runtime-surface.md` § Prep-entity floor).

## The Prose Pass

About to finalize any prose the DM reads aloud -> read it back once for
voice and naming consistency before shipping it
(`.claude/skills/composing-beats/references/runtime-surface.md` § Prep-entity floor).

## Scan Structure

About to write a DM-facing body paragraph past ~80 words -> stop and break
it: bold the load-bearing fact (name, number, or consequence) as its lead,
or split into bullets. A wall of prose that buries the one fact a DM needs
mid-session fails the same way a wrong fact does
(`vault/refs/stories/register.md` DM-facing bar). A vague consequence
("the weather turns personal") is not a fact — cash it out as a concrete
mechanic or drop it.

## Degrade By Asking

About to guess at a gap the interview did not answer -> stop and ask
instead; `vault/refs/vault/_common/degrade.md` lists the recurring
cases.

## No Instructional Prose

About to write any line on the output page -> state facts, names, numbers,
and wikilinks. No "remember to", no "never do", no meta-commentary about
how to DM. The page is terse reference for an expert DM, not a teaching
document.

## The Status Gate

About to flip `status:` past `pending` or touch `publish:` -> stop; those
belong to `transcript-ingest` and the publish proposal
(`vault/refs/vault/_common/lifecycle.md`).

---

## Rules for mechanical and combat-bearing types

These bind **any page that states mechanics or numbers**, whatever its type
-> the trigger is the content, never a list of type names. An item, rule,
creature, encounter, or ship page almost always qualifies; a location with a
lair, a faction fielding armed forces, a puzzle with a save DC, or a handout
carrying a usable effect qualifies exactly the same way the moment it states
a number.

A guide whose type states no mechanics ignores this section rather than
restating it -> never add a per-type carve-out saying these rules apply to
you as well; the condition above already says so.

### Reuse Before Inventing

About to design new mechanics -> check the SRD and `vault/campaigns/shattered-sea/monsters/` for
an existing equivalent first; a reskinned published entry with the same
mechanical effect always beats a new design. Build new only when the
setting flavor or mechanical concept genuinely cannot be satisfied by
existing content.

### Bound And Label Every Effect

About to write any power or effect -> label it `**[HB]**` or `**[RAW]**`,
then state action cost, range, duration, and recovery (long rest / short
rest / X charges / at-will) explicitly, and name the edge cases that will
come up at the table. An unbounded effect is the single most common balance
mistake here.

### Calibrate Against The Real Party

About to finalize any stat block, CR range, or difficulty number -> read
party stats from `vault/campaigns/shattered-sea/pcs/*.md` frontmatter and paste them first. CR
alone is not calibration (`.claude/skills/composing-beats/references/runtime-surface.md` § Prep-entity floor) ->
check the numbers against what this party actually does at the table.

Combat-capable entity with no party stats on hand -> read
`vault/campaigns/shattered-sea/pcs/*.md` yourself, or ask; never guess a CR.

---

## Creative-domain rider

Facts, canon, structure, and visibility are bound by every rule above.
**Prose style is free.** A timid entry — "is dangerous", "feels tense", a
generic read-aloud paragraph — is a contract violation, the same as a wrong
fact -> push for the specific, table-tested detail. Where the source is
silent and the choice is flavour rather than fact, pick the vivid option and
write it down.
