# Quickstart: NPC Page Standard

Proves a DM can run an NPC from one page, and that new pages inherit the core spine without empty optional headings.

## Prerequisites

- Branch `003-npc-page-standard`
- Host agent with `.agents/skills/` loaded
- Layout source in `wiki/_raw/` (Hinewai, Talon Skarn, Nona Black-Jaw, Thunk)

## Story 1 — Four baselines scan

Open each baseline. Expect the core spine in order: title, At a Glance (Role/Nature/Home/Wants + DM thesis), spoken look, Running, Relationships.

| Page | Band check |
|---|---|
| Hinewai | Extra form pair; Combat stages keyed to Death Bloom, not body HP |
| Talon Skarn | Running has opening / default turn / pressure / counterplay; one sheet |
| Nona Black-Jaw | Current pressure; public vs secret; no Combat heading |
| Thunk | Practical use; Combat is a pointer, not a second sheet |

Spoken look on all four: no secrets, DCs, or unearned names.

## Story 2 — Minimal contact from the template

1. In prep, ask for a new contact the wiki lacks. Expect a chat proposal, not a wiki write.
2. Accept. File from `wiki/templates/npc.md` with only name, `role: contact`, want, spoken look, first meeting, and one relationship.
3. Expect identity defaults from [data-model.md](./data-model.md). Expect no History, extra form, activity log, knobs, or Combat headings.
4. A second reader can run first meeting from the page alone.

## Story 3 — Skirmish hostile Combat

1. Propose a `role: rival` skirmish hostile with a fight.
2. After accept, expect `# Combat` with an encounter rule and one on-page sheet (or one pointer, not both).
3. Running includes opening and counterplay.

## Pass

SC-001: role, want, first move, fight handling in under 30 seconds on each baseline. SC-002–003: core order holds; zero empty optional headings on the four baselines plus the new contact. SC-004: spoken look is player-safe. SC-007: fightable pages carry the encounter rule on the page. Accept-gate still holds.
