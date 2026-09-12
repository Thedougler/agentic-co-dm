---
name: dnd-5e-magic-item-design
description: Design, revise, or audit engaging and mechanically sound homebrew magic items for D&D 2024/5.5e. Use when creating magic weapons, armor, wondrous items, consumables, artifacts, curses, sentient items, or evolving items. Every design must be grounded in comparable official content or reputable published homebrew found through current web research.
---

# D&D 5e magic-item design

## Work gate

Prep only. Follow `docs/agents/work.md`.

Show a chat proposal; write a campaign wiki page only after DM accept (FR-019). Reject leaves no page. Invention is required when the wiki lacks the fact: set `invention: true` and ground in wiki pages and/or D&D 5e rules. Cite `[[pages]]` for wiki claims. Show the DM any contradiction with an existing page. Never present invention as a wiki fact. Never write silent canon. A craft `type` becomes `canon` only after DM accept.

Players see nothing until the DM accepts and presents.

Done when: the page is inspectable Work, `lifecycle: proposed`, invention flagged, grounding named.


## Success criteria
- The item promises a specific experience, has a readable decision loop, and earns its place in the campaign.
- Mechanics are legal 2024/5.5e rules language, internally consistent, and calibrated against comparable published designs.
- Power is traded, not stacked: the item has a useful ceiling, costs, limits, counterplay, and an honest party role.
- Output is runnable at the table. Prefer delete and clarify; never paste WotC proprietary book text. Paraphrase and link public rules or benchmarks.
- State assumptions, uncertainty, and tuning knobs. Keep designs setting-agnostic unless the brief supplies canon.

## Required context
Ask or state what is known about: character level and class mix; item tier, rarity, and intended owner; campaign tone and setting constraints; encounter and exploration cadence; attunement availability; desired fantasy; action economy; existing party items; and whether the item is temporary, evolving, cursed, sentient, or plot-critical. Do not invent missing campaign canon.

## Mandatory web grounding
Every deliberate design needs current web research before final numbers. Use the public 2024/5.5e rules or SRD as the rules anchor, then inspect at least three comparators: one chassis peer, one effect/role peer, and one higher- or lower-tier boundary peer. A reputable published homebrew comparator may fill one slot, but label it as such. Record actionable observations and working links in the comparator matrix; do not append a bibliography or credit page.

Use this priority order when evidence conflicts: (1) user brief and table limits; (2) current 2024/5.5e public rules; (3) official published item peers; (4) reputable published homebrew; (5) numerical audit and playtest evidence; (6) theme and flourish. Do not silently use a 2014 chassis as a 2024 benchmark: label it legacy and recalibrate it.

## Minimum research packet
Before designing, capture for each comparator: rarity/tier, attunement, item type and weapon/armor chassis, action cost, range/targets, damage or defense delta, save/DC or attack bonus, frequency/recharge, duration, concentration interaction, stacking interactions, exploration utility, and the player choice it creates. Copy none of the protected prose. Use `references/research-and-comparators.md`.

## Workflow: five passes
1. **Pitch.** Write a one-sentence promise: “This is a [item] for a [role] that lets its bearer [choice/experience] by paying [cost or risk].” Name intended experience, fantasy, owner, tier, and counterplay. If the pitch is generic, reskin or delete.
2. **Chassis.** Prefer the least speculative method: (1) reskin an existing item; (2) change form, damage type, or a narrow capability; (3) exchange one property for another of similar value; (4) combine compatible published properties, then reassess rarity; (5) create a new mechanic only when existing ones cannot express the concept. Combining two same-rarity items is stronger than either — it does not stay that rarity by default. Choose rarity and attunement after the effect is understood.
3. **Power envelope.** Build a table for reliable offense, burst offense, defense, action economy, spell access, exploration, and social utility. Compare each axis to the matrix. Trade one strong axis for a weakness, cost, narrowness, or frequency limit. Audit the whole party, not just the intended owner.
4. **Engagement loop.** Write Tell → Choice → Cost → Payoff → Counterplay. Include a normal turn, a tempting but costly use, and what happens when the item is ignored. The item should create decisions, not replace them. Prefer once-per-turn or per-rest limits over unbounded “every hit” riders.
5. **Limits and handoff.** Run `references/mechanical-audit.md` and `references/narrative-and-wording.md`. State attunement, charges, recharge, duration, target limits, concentration, stacking, failure, curse consent/exit, and tuning knobs. Give the final player-facing text only after the audit.

## Power by rarity: a ceiling, not a shopping list
Use the 2024 Magic Item Power by Rarity ceilings as maxima, not a budget to fill repeatedly. An item at its maximum spell level should not also take its maximum bonus plus strong passives and several extras.

| Rarity | Maximum limited spell effect | Maximum static bonus |
|---|---:|---:|
| Common | Level 1 | None |
| Uncommon | Level 3 | +1 |
| Rare | Level 5 | +2 |
| Very Rare | Level 8 | +3 |
| Legendary | Level 9 | +4 |

A lower-level spell may appear more often than the table's maximum, but compare daily output to published items. Also weigh owner level/build, party items, magic density, permanent vs consumable, how often the ideal situation occurs, multiplier interactions, and how easily the item can be traded. Artifact and evolving items add story weight and removal/escalation conditions; they are not merely higher DPR.

## Audit pointers and design habits
- **Attunement:** use it when the item is broadly or repeatedly powerful; waive it for narrow, consumable, or mostly-fictional utility only with evidence.
- **Spell from item:** specify spellcasting ability, save DC/attack bonus, components, target, casting time, duration, concentration, charges, and whether the spell is cast from the item. Do not grant a hidden free slot or bypass concentration.
- **Action economy:** price bonus actions, reactions, concentration, setup turns, opportunity cost, and off-turn triggers. “On every hit” needs a once-per-turn limit unless the whole item is deliberately calibrated around it.
- **Class and party fit:** do not invalidate a class's signature resource, another character's niche, or the campaign's travel challenge forever. Narrow the scope or add a trade.
- **Evolving/cursed/sentient items:** make change visible and playable; never use a curse as secret plot punishment. Include consent, tells, choices, escape, and consequences.

Use `references/mechanical-audit.md` for the offense, defense, action economy, spell access, stacking, roles, and challenge-preservation audits. Use `references/narrative-and-wording.md` for the player-facing template, design notes, playtest procedure, and final checklist.

## Default output
1. Pitch, assumptions, intended experience, owner, tier, and chassis choice.
2. Comparator matrix with working links and concise research observations.
3. Power-envelope table and tradeoffs.
4. Player-facing item text in 2024/5.5e language.
5. Engagement loop: Tell → Choice → Cost → Payoff → Counterplay.
6. Mechanical audit summary, limits, stacking, and party-role effects.
7. Required design notes: Intended Experience, Published Benchmarks, Balance Assessment, and Tuning Knobs.
8. Playtest plan, revision triggers, and relevant handoff.

## Handoffs
- **theatre-of-the-mind:** item tells, sensory manifestations, cursed/sentient voice, and player-facing fiction without map assumptions.
- **dungeon-design:** item placement, vault/quest, hazards, factions, gates, and consequences around acquiring or losing it.
- **session-beats:** reveal, first-use scene, escalation, evolution, curse pressure, and payoff timing.
- **homebrew-monsters-5e:** an item that creates, commands, transforms into, or is balanced around a monster; keep creature math in that skill.
- **qmd-retrieval:** campaign-vault facts and canon; do not invent setting details when retrieval is silent.

## Campaign item workflow
Copy `wiki/templates/item.md` for consumables. Copy `wiki/templates/hazard.md` for flora hazards. `wiki/_raw/Ghost Plum.md` and `wiki/_raw/Razer-Grass.md` illustrate. Pass is jobs in `wiki/AGENTS.md` Layout, not a frozen outline.
Single item-design authority in ai-co-dm. Stackable gear remains PC/inventory data; mint a type: item note only when play, a query, or another note needs to cite the object.

Before design, retrieve the target PC, campaign hot page, relevant front/quest/session, existing signature gear, and three same-tier comparators. State tier, intended wielder, acquisition mode, campaign constraints, attunement, cadence, and strongest party synergy. Write one Signature sentence: object + distinctive verb + why it belongs here.

Make every property runnable: trigger, action type, prerequisite, target/range, roll or DC, effect, duration, uses/charges/recharge, concentration, stacking, and likely edge case. For consumable, cursed, sentient, evolving, artifact, or set-piece items, add visible tells, player choices, consent/exit where relevant, and administrable change states.

Separate reveal into first sight, handling, known mechanics, earned lore, and DM truth. Invoke theatre-of-the-mind for player-facing appearance prose; flesh-out-content may supply missing lived-in facts and visual-aids may ground an identity image.

### Note format

Copy those templates as scaffolds. Numbers live on one owner page.

1. **Frontmatter** — `type: item`, plus `campaign`, `region`, `kind`, `rarity`, `attunement`, `tags` (include region and kind in tags), and `wiki/AGENTS.md` required fields. Omit unused keys including `owner`.
2. **Spoken look** — `[!narration]` cold portrait. No secrets, DCs, unearned names.
3. **Classification** — kind and rarity (consumable) or hazard start/notice.
4. **One runnable effect** — terse 2024/5.5e text; at-table grammar from `obsidian-markdown`. Then stop on a consumable. Flora hazards also answer contact cost, careful passage, and counterplay.

Complex items (magic weapons, relics, artifacts, sentient/cursed/evolving) add sections below only when they change the table. Do not add sections a simple item does not need.

Run obsidian-markdown and applicable checks. Finish with `./scripts/after-write "design or revise item"`.
