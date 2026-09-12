---
name: homebrew-monsters-5e
description: Research, design, reskin, balance, audit, and revise monsters for the 2024/2025 D&D rules commonly called 5.5e. Use when creating individual monsters, variants, minions, encounter groups, legendary creatures, or boss fights. Do not use for player-character builds.
---

# Homebrew Monsters 5e

## Work gate

Prep only. Follow `docs/agents/work.md`. Load `wiki/AGENTS.md`, `copy-writer`, and `obsidian-markdown` on every vault write.

Show a chat proposal; write a campaign wiki page only after DM accept (FR-019). Reject leaves no page. Invention is required when the wiki lacks the fact: set `invention: true` and ground in wiki pages and/or D&D 5e rules. Cite `[[pages]]` for wiki claims. Show the DM any contradiction with an existing page. Never present invention as a wiki fact. Never write silent canon. A craft `type` becomes `canon` only after DM accept.

Players see nothing until the DM accepts and presents.

Done when: the page is inspectable Work, `lifecycle: proposed`, invention flagged, grounding named.


## Success criteria
- The monster has a memorable fiction signature, a readable role, counterplay, and a reason to exist in this encounter.
- Mechanics use legal 2024/2025 notation, are internally consistent, calibrated against peers, and runnable without hidden arithmetic.
- Output gives the DM decisions to make, not a pile of abilities. Prefer delete and clarify.
- Setting-agnostic paraphrased rules language. Never paste WotC proprietary book text.

## Rules basis and priority order
When facts conflict use: (1) the user brief and table constraints; (2) 2024/2025 core rules and current public SRD; (3) reference-gate peer evidence; (4) numerical chassis and three-round budget; (5) stylistic flourish. State assumptions. Do not silently mix 2014 and 2024 math.

## Gather, then choose the least-complicated path
Briefly gather tier, party size, intended difficulty, environment, role, signature, and complexity. Choose **reskin** when fiction changes but behavior does not; **variant** when one or two hooks change; **full design** only when the decision loop, role, or chassis cannot be expressed by either. Say why the path is sufficient.

## Mandatory reference gate
Before a deliberate homebrew, use `references/reference-gate.md`: inspect one official numerical peer, one role peer, and one mechanic peer (one creature may cover multiple; use at least two independent designs). Summarize patterns in a dossier. Then use `references/chassis-and-budget.md` and `references/audit-and-revise.md`.

## Define the monster before numbers
Write one sentence: “This is a [fantasy] [role] that [signature] to pursue [goal], fears [fear], and gives players [counterplay].” Then fill **Fantasy / Signature / Goal / Fear / Counterplay / Proof**. Proof is the observable tell that makes the signature fair.

## Assign a combat role
Use one primary role. Add a secondary only when complexity is justified. Rank (minion / standard / elite / solo or legendary) is separate from role.

| Role | Function | Typical trade | Expected player response |
|---|---|---|---|
| Ambusher | Hides, strikes, withdraws | Higher burst; lower durability | Reveal it, deny hiding, ready actions |
| Artillery | Ranged pressure | Accuracy/damage for lower HP or AC | Cover, close distance, disrupt positions |
| Bruiser | Dangerous melee | Damage and HP for lower AC, speed, or saves | Kite, control, focus fire |
| Controller | Terrain, movement, conditions | Control for lower direct damage | Break setup, reposition, rescue |
| Defender | Protects allies, holds space | Durability for lower damage | Bypass, shove, isolate, disable |
| Leader | Buffs, heals, commands, repositions | Team power for weaker personal offense | Eliminate or separate from allies |
| Skirmisher | Moves through or around the party | Mobility for reduced durability | Pin it, deny routes, control space |

First turn and default choice must reveal the primary role.

## Decision loop
For every signature feature write **Tell → Threat → Responses → Payoff**. Tell is a visible cue; Threat is what happens if ignored; Responses are at least two viable player answers; Payoff is the benefit, with a cost or opening. Remove features with no response or payoff.

## Numerical chassis: trade, do not stack
Set rank/CR, PB, AC, HP, attack/DC, damage, speed, and saves from the peer dossier. Use formulas and benchmarks in `references/chassis-and-budget.md`; keep one strong axis, one support axis, and a meaningful weakness. Do not stack high AC, HP, broad resistances, immunities, control, damage, and mobility merely because each looks reasonable alone.

- **Three-round offense:** script likely first three rounds, including setup, misses, recharge, reactions, legendary/off-turn actions, and targets. Compare output and control to peers.
- **Defense honesty:** audit effective HP, avoidance, mitigation, saves, immunities, regeneration, healing, and escape together. Every unusual defense needs a bypass, tell, resource, or trade.
- Conditions should create choices or a clock. Prefer slowed movement, narrow disadvantage, exposed positions, resource pressure, or repeat saves over turn deletion. Never spam hard conditions without counterplay.

## Action economy and encounter use
- **Standard:** reliable action or Multiattack; one signature or situational action; zero or one Bonus Action or Reaction.
- **Elite:** more durability or one defensive resource; reliable action plus signature; a Reaction, Bonus Action, or limited off-turn presence; allies or environmental support. Do not simply double every statistic.
- **Solo/legendary:** participate between character turns via Legendary Actions (3 uses/round; each expends one use; options return at start of turn — SRD 5.2.1), Legendary Resistance, Reaction/Bonus Action, lair/terrain, minions, or action-oriented villain phases (Position → Pressure → Desperation). Rate-limit the strongest Legendary Action. Bloodied (≤ half HP) should change decisions, not only add damage.
Do not solve solo play with inflated AC/HP alone. Use lightning rods — groups of weak creatures, fragile burst targets, reachable artillery, expendable lieutenants, visible hazards — so the party's best features work somewhere. Leave immunities blank unless fiction and encounter justify them.

Integrate objective, terrain, allies (usually two or three complementary types), reinforcements, escape, and failure states other than TPK. Trap counterplay must not depend on one check.

## 2024 notation
Use `DC 15`; `+7 to hit`; `Hit: 11 (2d8 + 2) damage`; `Recharge 5–6`; `1/Day`; `Speed 30 feet`; `PB +3`; explicit save/repeat timing; and clear shapes, ranges, targets, durations, and triggers. Label any 2014 recalibration. Statblock YAML keeps that 5e fence phrasing. Wiki-body checks and saves outside the fence use the at-table grammar in `obsidian-markdown`.

## Default output
1. Path chosen and assumptions.
2. Reference-gate dossier and peer patterns (inline, concise).
3. Fiction signature: Fantasy, Signature, Goal, Fear, Counterplay, Proof.
4. Role, rank/CR target, encounter job, and decision loop.
5. Monster stat block or reskin/variant delta.
6. Three-round offense and defense audit summary.
7. Encounter integration: allies, terrain, lightning rods, tells, escape/failure state.
8. Running notes, counterplay, and revision knobs.

## Wiki note structure

Two paths depending on whether the creature has a personal identity:

### Standalone creature → `wiki/templates/creature.md`
H1 title → `[!narration]` → `## Statblock` (image then fence) → `## Visual reference` when a sheet exists → `## Behavior` → `## Tactics` → `## Art`. Linear layout — no column wrappers. Frontmatter includes `region` and `source` alongside standard fields. Exemplar: `wiki/_raw/Bloodhawk.md`.

**Behavior** uses list items with bold labels (`- **Label.** text`): **Habitat** (terrain, territory, where it lives), **Behavior** (observable habits, body language, movement patterns), **Diet** (what it eats, feeding signs, hunger drivers), **Social Structure** (solitary/pack/herd, interactions with other creatures).

**Tactics** uses list items with bold labels (`- **Label.** text`): **Signs** (what trackers find — tracks, marks, smells, sounds), **Instincts** (what triggers aggression, what ends a hunt), **Tactics** (how it fights — opening, follow-up, preferred conditions), **Weaknesses** (exploitable flaws — terrain it hates, movement it cannot make, formations that shut it down), **Aftermath** (what the scene looks like after an encounter, salvageable remains).

**Art** holds additional images: tokens, alternate views, reference art. One embed per line.

Design outputs map: fiction signature → narration + Behavior; decision loop → Tactics; three-round script informs Tactics but stays in the design conversation; encounter integration → Habitat + Social Structure + Instincts; counterplay → Weaknesses; running notes → Tactics + Aftermath.
### NPC with combat form → `wiki/templates/npc.md`
When the creature has a name, history, relationships, and a personal identity, statblocks live in the NPC file's `# Combat` section — not a separate creature note. The NPC file owns identity, history, and relationships; the `# Combat` section owns the stat fences.

- State an **encounter rule** before the statblocks: the fiction condition that selects which block to use.
- One statblock per stage or form, keyed to fiction conditions (memorial damage, pact state, betrayal), not HP thresholds alone.
Exemplar: `wiki/shattered-sea/npcs/Aruhe - Hinewai` (three staged statblocks keyed to Death Bloom condition).
- Behavior and Tactics fields fold into the NPC's `## Running` section instead of standalone `## Behavior` / `## Tactics` sections.

Exemplar: `wiki/shattered-sea/npcs/Aruhe - Hinewai` (three staged statblocks keyed to Death Bloom condition).

## Handoffs
- **dnd5e-mechanics**: which save or check a feature uses; chassis still owns the DC number.
- **theatre-of-the-mind**: spatial prose, tells, and runnable descriptions without a map.
- **dungeon-design**: sites, rooms, hazards, terrain, and encounter architecture.
- **session-beats**: reveal, escalation, pacing, and scene timing.
- **qmd-retrieval**: campaign-vault retrieval; do not invent missing canon.

