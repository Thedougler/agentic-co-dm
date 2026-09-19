---
name: faction-design
description: >-
  Write, edit, or create named faction pages for the campaign wiki. Use when a
  faction, organization, order, guild, cult, polity, crew, movement, or cell
  needs a persistent page — public face, DM thesis, active agenda, faction turn,
  assets, people, territory, or relationships. Also use when a missing named
  faction blocks a beat, scene, or session prep. Covers fronts, faction turns,
  and off-screen motion for sandbox play.
---

# Faction Design

File what constitution X makes canon. Follow `docs/agents/work.md`.

## Central principle

A faction is a source of **off-screen motion and campaign pressure**, not an
org chart. Spend prep in proportion to table importance. Every useful faction
should pursue a want, exert pressure through a method, and collide with the
party or another faction. Keep the economy of attention: a want, a method, and
one visible portent often beat a page of lore.

| Importance | Prep | At the table |
| --- | --- | --- |
| Named background group | Name, public purpose, one portent | Mentioned in rumor or seen in passing |
| Scene faction | Want, method, pressure, one signal | Ask/offer/threaten; leave a hook |
| Recurring/significant | Full page plus relationships, faction turn | Acts off-screen; players can notice or interfere |
| Campaign-shaping | Full page plus milestones, hidden agenda, collision map | Drives arcs; changes the world whether helped or opposed |

## Build the faction

1. **Want.** Write a concrete, present-tense want that can change the campaign:
   "control the southern shipping lanes," not "be powerful." A faction without a
   concrete want is decoration.
2. **Method.** Name the signature way it acts — force, trade, infiltration,
   ritual, diplomacy, sabotage, law. Method makes the faction recognizable and
   constrains what it can attempt.
3. **Pressure.** Why it must act now. A comfortable faction generates no play.
   Pressure comes from scarcity, deadline, rival, exposure, opportunity, or
   internal fracture.
4. **Portent.** The visible sign of off-screen motion — a change the party can
   observe, hear rumored, suffer, or discover. Portents are the faction's table
   presence between direct encounters. Without them the faction exists only when
   the DM remembers to mention it.
5. **Collision.** Where the faction's want intersects another faction, NPC, place,
   or the party. Collision creates decisions; isolation creates backstory.
6. **Player opening.** What the party can influence, protect, expose, steal,
   negotiate, sabotage, support, or refuse. A faction the party cannot affect is
   a cutscene.

If you cannot fill want, method, and one collision, the group is not yet a
faction — keep it as a mention in its owning beat, place, or NPC note until it
earns a page.

## File the wiki note

Copy `wiki/templates/faction.md` as scaffold. The co-located
`wiki/templates/contracts/faction.yml` owns required, optional, and
lifecycle-gated section semantics — consult it for what to include or omit.
Faction pages use only the `[!narration]` callout; keep DM-facing material as
ordinary prose.

Store the note under `wiki/<campaign>/factions/` with `type: faction`.

### Identity sentence

Write one sentence before drafting the page:

> This is a [kind/scope] faction that [wants concrete change], acts through
> [signature method], and gives players [choice or pressure].

If the sentence has no concrete change, method, or player opening, keep
retrieving or ask for the missing premise.

### What the skill adds beyond the template

The template carries section structure and fill prompts. The skill adds:

- **DM thesis** is one sentence of campaign pressure — what this faction is
  about and why it matters now. Not a summary; a thesis drives prep decisions.
- **Public face** narration goes through theatre of the mind. No secrets, DCs,
  hidden leaders, or unearned names.
- **Active agenda** — keep one whenever possible. A second only when the faction
  genuinely sustains an independent project. Each agenda needs: goal, why, next
  move, needs, opposition, next signal, player opening, and if-completed state.
- **Current Turn** — name the turn state at creation; do not roll it.
  `world-tick` resolves turns later and appends Turn Log rows.
- **Assets, people, territory, relationships** — include only entries that
  currently change play. A kingdom may own thousands of soldiers; link the
  regiment or spy ring that matters this session.
- **Invention** is labeled, cited `[[pages]]`, and proposed for DM acceptance.
  Never present invention as wiki fact.

Read `references/faction-craft.md` for front design, faction turns, failure
modes, and audit questions.

## Handoffs

Hand off narration/dialogue to `theatre-of-the-mind`, named NPCs to
`npc-design`, places to `place-design`, off-screen resolution to `world-tick`,
pacing to `session-beats`, and vault lookup to `.agents/skills/qmd` plus
`specs/004-qmd-search-default/contracts/retrieval-precedence.md`.

## Done

The page is done when:

- It lives in `wiki/<campaign>/factions/` with `type: faction`.
- It fills `wiki/templates/faction.md` per the template contract.
- The identity sentence holds: concrete want, method, player opening.
- DM thesis is one sentence of campaign pressure.
- Invention is labeled, cited, and proposed.
- The DM can answer: What do they want? What can they do? What will they do
  next? What changes if they succeed? How can the party notice or interfere?
