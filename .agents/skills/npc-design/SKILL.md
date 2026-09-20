---
name: npc-design
description: >-
  Design, revise, and run engaging NPCs and villains for D&D 5.5e (2024 rules).
  Use when creating incidental extras, scene NPCs, recurring allies, patrons,
  rivals, faction faces, villains, lieutenants, or social encounters. Covers
  wants, leverage, limits, portrayal, Influence/Attitude, villain plans, and
  monster-style combat packages. Do not use for pure monster design without a
  personal identity (use homebrew-monsters-5e) or for player-character builds.
---

# NPC design
## Boundary contract

### Input

Take a named NPC owner, the caller's objective, the relevant brief,
`wiki/templates/npc.md`, and linked canon/evidence for the person's ties,
current situation, and table role. The owner is a playable identity with
agency, not a generic monster or biography request.

### Owner-specific Work

Work only the NPC: preserve the appropriate prep scale, build want, leverage,
need, limit, contradiction, and portrayal signals, then fill the NPC template.
Keep Influence/Attitude distinct from request posture, leave PC choices open,
and route any fightable numbers to the monster-style owner.

### Capability Handoff

Hand off only a bounded seam (for example, dialogue/look to
`theatre-of-the-mind`, a place to `place-design`, pacing to `session-beats`, or
combat math to `homebrew-monsters-5e`) with the NPC owner, parent objective,
evidence, and exact section requested. Require return evidence naming the child
artifact/section and completion result; resume NPC work only after that seam
meets the NPC contract, otherwise report the missing evidence or blocker.

### Done

Use the existing `## Done` checklist below. Completion is observable when the
named NPC page path, NPC-template and agency/playability checks, combat
handoff when applicable, and any child return evidence are reported.


Prep only. Follow `docs/agents/work.md`.

## Refuse gates

- **Work gate.** Show a chat proposal before writing under `wiki/`. Write only
  after DM acceptance.
- **Invention.** Never present invention as wiki fact. Set `invention: true` (or
  mark proposed), cite `[[pages]]`, show contradictions, and propose for
  acceptance. No silent canon or rich unused biography as established fact.
- **Role enum.** Frontmatter `role` is exactly one of `rival` | `patron` |
  `contact`. Craft/job labels (gatekeeper, informant, …) go in Nature/body —
  never in YAML `role`. Do not default `role`.
- **Template lock.** Copy `wiki/templates/npc.md` only. Fill At a Glance,
  narration portrait, Running, Connections with substance — not empty headings.
- **Narration.** Spoken look is `[!narration]` `{Name}`. Theatre of the mind.
  No secrets, DCs, unearned names, or DM thesis in player-facing prose.
- **Prep scale.** Match importance: incidental = name/job, immediate want, one
  signal, exit — refuse novel biography for a one-shot stew seller.
- **No lore dump.** Situated knowledge through conversation, evidence, and
  choices — not one unbroken exposition speech.
- **Influence ≠ mind control.** Attitude (Friendly/Indifferent/Hostile) is
  separate from request posture (Willing/Unwilling/Hesitant). A check moves
  position; it does not erase oaths, limits, or agency.
- **No DMPC.** Allies stay supportive, limited, and player-directed. Give want
  and cost; do not let them choose the party's plan or solve the central problem.
- **Three clues.** Essential conclusions need ~three independent channels.
  Do not gate a villain arc behind one clue or one check.
- **No cutscene immunity.** Direct villain contact accepts interrupt, injure,
  expose, bargain, or bypass — or uses genuine remote/protected fiction. No
  post-hoc immunity after players act.
- **Betrayal rare.** Earned, foreshadowable, motivated, answerable — not the
  default for every trusted patron/ally. Prefer divided loyalties and off-ramps.
- **Active villain plan.** Interruptible steps with visible signs and player
  interference — not idle in the final room until heroes arrive.
- **Monster package, not PC sheet.** Reject full PC class sheets for ordinary
  enemies. Concise monster-style block; hand numbers/balance to
  `homebrew-monsters-5e`.
- **Multiple conclusions.** Defeat, escape, compromise, exposure, alliance, or
  conditional reform. Do not predetermine redemption as the only ending.

## Central principle

An NPC is a legible, interruptible source of **agency and consequence**, not a
biography. Spend prep in proportion to table importance.

| Importance | Prep | At the table |
| --- | --- | --- |
| Incidental extra | Name/job, immediate want, one signal | One line, reaction, exit |
| Scene NPC | Want, leverage, limit, contradiction, 2–3 signals | Ask/offer/refuse; leave a hook |
| Recurring/significant | Card plus relationships, activity log, change trigger | Pursues goals between appearances |
| Villain/faction face | Recurring card plus front, clock, contingencies | Acts off-screen and responds to players |

## Build the person

1. **Function + identity `role`.** State craft function this session (see
   `references/npc-templates.md`). Set wiki `role` to `rival` | `patron` |
   `contact` only.
2. **Immediate want.** Concrete, present-tense; can change the next scene.
3. **Leverage + need.** What they can grant/deny/expose/mobilize; what they lack
   or fear losing. Cost on leverage; playable address for need.
4. **Limit.** Line, resource, skill, oath, fear, or time that blocks easy wins.
5. **Productive contradiction.** Two truths under pressure — do not resolve in prose.
6. **Four portrayal signals.** Visual anchor, repeatable behavior, voice
   principle (not accent), sample line carrying want.
7. **PC invitation.** One optional reason to engage per PC — never a forced bond.

## File the wiki note

Copy `wiki/templates/npc.md`. Pass person jobs in `wiki/AGENTS.md` Layout.
At a Glance: Role, Nature, Home, Wants + one-sentence **DM thesis**. Spoken look
is `[!narration]` `{Name}`. Running: first move and posture-change. Relationships:
wikilink + meaning (omit only on stub with no named ties). Omit unused optional
sections. Named-ingest stubs: identity fields + complete sentences only.

Identity defaults: `location`/`faction` unknown → `unknown`/`none`; omit unused
`aliases`; supply `role`. Density exemplars in `wiki/_raw/` are not clone targets.
`specs/003-npc-page-standard/contracts/npc-page.md` is optional extra depth.

**Combat:** `# Combat` only if fightable. One-sentence encounter rule + on-page
sheet **or** exactly one `type: creature` pointer. Landmark stages: one sheet per
named condition. Else omit the heading.

## Handoffs

Narration/dialogue → `theatre-of-the-mind`; places → `place-design`; pacing →
`session-beats`; combat math → `homebrew-monsters-5e`; vault lookup →
`.agents/skills/qmd` plus
`specs/004-qmd-search-default/contracts/retrieval-precedence.md`.

Read `references/npc-craft.md` for social play, recurrence/villains, wiki fill
detail, audit, and failure modes. Also: `references/npc-templates.md`,
`references/villain-front.md`, `references/social-and-combat.md`.

## Done

- Fills `wiki/templates/npc.md`; `role` is rival|patron|contact; craft job in body.
- Want, leverage, need, limit present-tense and playable at the right prep scale.
- Narration is perceivable-only; invention labeled/cited/proposed; wiki write after accept.
- Villain (if any): active interruptible plan, no cutscene immunity, multiple conclusions.
- Combat (if any): monster package + handoff — not a PC sheet.
- DM recovers the actionable card in under 30 seconds.
