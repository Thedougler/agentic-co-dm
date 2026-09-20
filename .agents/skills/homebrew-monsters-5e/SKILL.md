---
name: homebrew-monsters-5e
description: Research, design, reskin, balance, audit, and revise monsters for the 2024/2025 D&D rules commonly called 5.5e. Use when creating individual monsters, variants, minions, encounter groups, legendary creatures, or boss fights. Custom features communicate lore, origin, or stakes a second person can state. Substantial homebrew names the plot or character beat it manifests. Number-only or difficulty-only is incomplete. Stock unchanged and explicit stock-fight overrides are exempt. Do not use for player-character builds.
---

# Homebrew Monsters 5e

File what constitution X makes canon. Follow `docs/agents/work.md`.

## Success criteria
- The monster has a memorable **fiction signature**, a readable role, counterplay, and a reason to exist in this encounter.
- A custom combat feature communicates lore, origin, or stakes a second person can state. Number-only features are incomplete.
- A substantial homebrew names the plot or character beat it manifests. Difficulty-only is incomplete.
- Stock published opposition used unchanged does not need custom features. An explicit DM request for a stock or featureless fight overrides.
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
Write one sentence: "This is a [fantasy] [role] that [signature] to pursue [goal], fears [fear], and gives players [counterplay]." Then fill **Fantasy / Signature / Goal / Fear / Counterplay / Proof**. Proof is the observable **tell** that makes the signature fair.

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

## Numerical chassis and encounter design
Read `references/chassis-and-budget.md` for formulas, PB table, trade rules, three-round offense script, defense checklist, action-economy packages (standard / elite / solo), legendary actions, action-oriented phases, and bloodied transitions. The core principles:

- **Trade, do not stack.** One strong axis, one support axis, a meaningful weakness. Do not stack high AC, HP, broad resistances, immunities, control, damage, and mobility.
- **Three-round honesty.** Script likely first three rounds including setup, misses, recharge, reactions, legendary/off-turn actions. Compare output and control to peers.
- **Defense bypass.** Every unusual defense needs a bypass, tell, resource, or trade. Conditions should create choices or a clock — prefer slowed movement, narrow disadvantage, exposed positions, or repeat saves over turn deletion.
- **Lightning rods.** Do not solve solo play with inflated AC/HP alone. Use fragile burst targets, expendable lieutenants, terrain objectives, visible hazards — so the party's best features work somewhere. Leave immunities blank unless fiction and encounter justify them.

Integrate objective, terrain, allies, reinforcements, escape, and failure states other than TPK. Trap counterplay must not depend on one check.

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

Read `references/stat-block-template.md` for the full statblock template, 2024 notation examples, and the design-to-wiki field mapping.

Two paths depending on whether the creature has a personal identity:

### Standalone creature → `wiki/templates/creature.md`
Pass on creature jobs in `wiki/AGENTS.md` Layout: look, runnable sheet, life, hunt. Copy `wiki/templates/creature.md`. File a *linear* page: H1, `[!narration]`, `## Statblock` with at most one overview image immediately before the fence, then Visual reference when a sheet exists, Biology when anatomy matters, Behavior, Tactics, and Art subsections for remaining images. Frontmatter includes `region` alongside standard fields.

Exemplars: `wiki/entities/creature/bloodhawk.md` (aerial skirmisher, pounce-and-haul loop), `wiki/entities/creature/spiguar.md` (grass ambusher, drag-into-cover loop).

**Life** answers habitat (ground it uses and ground it refuses when that refusal is true), habits, diet, social. Shut-downs MUST be things the party can do.

**Hunt** answers signs, instincts, opening, shut-down, aftermath.

**Art** holds extra images when they exist. Omit when unused.

Design outputs map: fiction signature → narration + life; decision loop → hunt; three-round script informs hunt but stays in the design conversation; encounter integration → habitat + social + instincts; counterplay → shut-down; running notes → hunt + aftermath.

### NPC with combat form → `wiki/templates/npc.md`
When the creature has a name, history, relationships, and a personal identity, statblocks live in the NPC file's `# Combat` section — not a separate creature note. The NPC file owns identity, history, and relationships; the `# Combat` section owns the stat fences.

- State an **encounter rule** before the statblocks: the fiction condition that selects which block to use.
- One statblock per stage or form, keyed to fiction conditions (memorial damage, pact state, betrayal), not HP thresholds alone.

Exemplar: `wiki/entities/npc/Hinewai.md` (three staged statblocks keyed to Death Bloom condition).

- Behavior and Tactics fields fold into the NPC's `## Running` section instead of standalone `## Behavior` / `## Tactics` sections.

## Handoffs
- **dnd5e-mechanics**: which save or check a feature uses; chassis still owns the DC number.
- **theatre-of-the-mind**: spatial prose, tells, and runnable descriptions without a map.
- **dungeon-design**: sites, rooms, hazards, terrain, and encounter architecture.
- **session-beats**: reveal, escalation, pacing, and scene timing.
- **qmd-retrieval**: campaign-vault retrieval; do not invent missing canon.
