---
type: encounter
status: draft
publish: false
title: ""
aliases: ["Velvet Noose Intercept"]
summary: "The Velvet Noose boards the Uncertainty with a sealed case, not powder — she already has the Crown's dispatch order. The question is what the party confirms, and what they trade to make her leave."
created: "2026-08-11"
updated: "2026-08-11"
owner_skill: "vault/campaigns/.claude/skills/encounter-prep/SKILL.md"
tags: [maritime, combat]
tier: supporting
campaigns: [Shattered Sea]
uid: d8e3f1a2-5b6c-4d7e-8f90-a1b2c3d4e5f6
---

# Velvet Noose Intercept

*The ship that cannot be fought arrives with a sealed case and waits. The real fight is over what the Crown's dispatch order says in clause four, and whether the party figures it out before [[mave-sorn|the Captain]] reads it aloud.*

| Field | |
|---|---|
| `primary_goal` | Proves that power in the [[central-strait\|Strait]] is informational, not military. Whoever controls what the Crown is tracking controls what happens next. |
| `consistent_method` | The Captain presents rather than threatens. She reads silence as an answer. She does not prompt; she waits through discomfort until someone speaks. |
| `active_problem` | She has the [[uncertainty\|Uncertainty]]'s name, departure port, and the Crown dispatch order before the skiff reaches the rope ladder. The party cannot win by refusing to answer — they can only choose what to confirm. |
| `performance_hooks` | Voice: bureaucratic, unhurried, slightly amused. Tic: she reads the dispatch aloud one clause at a time, pausing after each. She does not rush the pause. |
| `link_of_relevance` | [[perrin-black-jaw\|Perrin Black-Jaw]] — the Crown dispatch names a "supernatural irregularity aboard" without naming a person; the Captain's right of inspection is really an invitation to watch Perrin's face when she reads clause four. The mechanism is her attention, not her authority. |
| `terrain_shift` | Round 3 of any combat: a gun-crew on the Noose runs a long cannon across to the open port facing the Uncertainty. Until it fires or is stood down, every PC in the open on the main deck makes a [[constitution\|Constitution]] saving throw at the end of their turn or becomes [[frightened\|Frightened]] until the start of their next turn. |
| `objective` | Win condition beyond defeating every enemy: the party leaves with the Captain's letter of transit — or departs without it at a cost the story tracks. |

## Opening

**Dramatic Question:** Does the crew thread the Noose's terms without surrendering what the Crown is hunting — and do they even know what that is before the Captain does?

> [!read-aloud]
> The skiff makes the Uncertainty's rope ladder in under twelve minutes. The oarsmen ship their oars without being told.
>
> The captain who steps over the rail is wearing the kind of clean that means she had time to change since this morning. No visible blade. Her first mate's hand rests on a belaying pin and stays there. Four marines take positions at the stern rail without looking at anyone in particular.
>
> From the Noose, two decks up and ninety yards off, a gun-crew can be heard running out a long cannon — not to fire, just to let the sound cross the water.
>
> She holds the sealed case, already open, both hands flat at the corners. She does not look down at it.
>
> *The Captain*: I have your vessel name, your last port of call, and the exact language of the Crown's dispatch authorising your detention.
>
> She sets the case on the hatch cover, face up, without looking at the document.
>
> *The Captain*: My terms are inside. I will take questions after.

## Drama Suite

The parley opens with the Captain standing at the case, waiting. Her terms: one hour of conversation, a declared manifest of the forward hold, right of inspection. In exchange: safe passage, no search, a letter of transit signed by her — worth more than it should be in Midchain harbours.

**What she actually wants:** confirmation that whatever the Crown is tracking is supernatural in nature. The dispatch reads "irregularity." She wants to know whether that means contraband, a person, or something outside a clean legal category. The difference determines what she sells the intelligence for and to whom.

**What the party has to trade:** [[geoffrey-draves|Geoffrey Draves]] knows the Crown search fleet's current heading and composition — he would not have taken this route otherwise. That intelligence is worth the terms. She does not know that they know it.

**The case on the hatch cover:** it is open. Any PC can read the dispatch. Clause four: *"…supernatural irregularity manifesting as arcane attunement outside standard registry; subject may be unaware of the designation."* This is in plain sight. The Captain does not mention it until she is ready to.

| Roll | DC | Outcome |
|---|---|---|
| Persuasion / Deception / Insight | 10 | Keep the manifest categories vague — cargo types without specifics. She accepts partial disclosure. Inspection clause suspended, deadline extended thirty minutes. She departs with the dispatch but no confirmation. |
| Persuasion / History / Investigation | 15 | Offer the Crown fleet's heading. Draves confirms it freely if the party persuades him. She counters: letter of transit plus she keeps a copy of the dispatch. The party comes out ahead. |
| Persuasion / Deception vs. her passive Insight (11) | 20 | Convince her the dispatch is keyed to a different vessel — Crown misidentification, happens in busy straits. She believes it and departs without confirmation, without the dispatch copy, without searching. No letter of transit, but nothing confirmed either. |

> [!check] Persuasion (DC 12) — Draves Confirms Fleet Routing
> **Success:** Draves confirms the heading freely; frame it as "giving her something to leave with."
>
> **Failure:** he declines to confirm it. The fleet-routing outcome is unavailable until another approach opens it.

**Shenanigans:**

- Perrin can use Cutting Words to impose disadvantage on the Captain's Insight check against any one PC's lie. She is not immune. She does not show it.
- Jean-Claude, standing behind the case, can attempt to read clause four before she does, giving him time to warn Perrin quietly.
- If Perrin reveals his pact willingly: the Captain listens without expression and asks one question. Not a win or a loss. She will use the information. Stakes has what follows.

> [!check] Sleight of Hand (DC 15) — Read the Dispatch Early
> **Setup:** the First Mate (passive Perception 13) is watching. A distraction from another PC (Performance DC 12) opens the window before Jean-Claude attempts this.
>
> **Success:** Jean-Claude reads clause four before she does; he can warn Perrin quietly.
>
> **Failure:** the First Mate catches the motion, or the case closes first.

**If a PC attacks the Captain during the parley:** she withdraws toward the skiff while combat opens. The Noose opens the long cannon port.

## Enemy Roster

**Parley escort — aboard the Uncertainty's deck:**

[[mave-sorn|Mave Sorn]] (leader/controller). CR 4; full stats on her NPC page; inline copy below.

Velvet Noose First Mate (defender/controller) × 1 — reskinned Veteran (CR 3): AC 17 (splint), HP 58. Multiattack: longsword +5 (1d8+3) and shortsword +3 (1d6+1). Parry reaction (+3 AC against one melee hit per round). Morale: never breaks while the Captain stands.

Velvet Noose Marines (bruiser/skirmisher) × 4 — reskinned Thug (CR 1/2): AC 11 (leather), HP 32 each. Multiattack: 2 mace attacks, +4 to hit, 2d6+2 bludgeoning. Morale: holds when 2 of 4 are down; retreats with the Captain when she signals.

Three creature types (Captain / Officer-tier / Marine-tier). Within the cap.

**Full boarding escalation** — only if the parley breaks down entirely and the Uncertainty does not create a stopping condition: 2 more Officers (Veteran CR 3) and 8 more Marines (Thug CR 1/2) board via grapple-lines from the Noose. The Captain does not return. Run as horde resolution (pool damage across the board, bulk-resolve saves), not individual initiative — see Lowering the Stakes for the stopping condition.

**Mave Sorn — inline stats (run-sheet copy; full statblock on NPC page):**

Variant of [[bandit-captain|Bandit Captain]].

| Stat | Value |
|---|---|
| AC | 15 (studded leather) |
| HP | 65 |
| Speed | 30 ft |
| STR / DEX / CON | +2 / +3 / +2 |
| INT / WIS / CHA | +2 / +1 / +4 |
| Saves | DEX +5, WIS +2, CHA +6 |
| Skills | Athletics +4, Deception +6, Insight +5, Intimidation +6, Persuasion +6 |
| CR | 4 |
| Multiattack | Two Cutlass attacks. Cutlass: +5 to hit, 1d6+3 slashing. [[dagger\|Dagger]]: +5 to hit, 1d4+3 piercing (ranged 20/60). |
| Bonus Action | **Command the Escort:** one Marine or the First Mate within 60 ft. uses its Reaction to make one weapon attack immediately. |
| Reaction | **Legal Counterclaim (Parry):** adds 3 to AC against one melee hit per round; must declare before the roll resolves. |

## Challenge Calibration

**Social phase:** no CR. Difficulty is set by the DC table and the party's CHA spread: Jean-Claude −1, Crissdalynn +0, [[catarina-davirelli|Catarina]] +0, Delmar +2, Perrin +9. Only Perrin reaches the highest tier reliably unaided. The fleet-routing trade requires Draves to confirm it, which requires a persuasion check from the party.

**Parley escort combat** (Captain + First Mate + 4 Marines): total CR ≈ 4 + 3 + 2 = 9. Lazy Benchmark: ½ × 25 (five level-5 PCs) = 12.5. Roster sits below deadly. **Hard [theoretical, low confidence]** — empirical band says this party punches 1–2 CR above standard (S06: [[vashu-the-weeping-veil|Vashu]] + [[ozzeth-the-twiceborn|Ozzeth]]; S07: CR-12 [[otar-the-foul|Otar]]); actual difficulty is likely Medium. Watch concentration: the Captain's Command the Escort means the First Mate lands an extra attack through a Reaction every round, and Perrin (AC 18, STR −1) is the natural concentration-pressure target if Hex or [[faerie-fire|Faerie Fire]] is up.

**Full boarding escalation:** do not run as standard combat. 10+ opponents on a pitching deck is a resource drain, not a fight the party wins by action economy. Apply horde resolution; treat each round as costing 1d4 HP per PC from incidental fire, escalating until a stopping condition appears (see Lowering the Stakes).

## Terrain

**Zone 1 — Main Deck (50 × 30 ft):** primary zone. Barrels lashed to the mainmast (half cover), a capstan amidships (full cover, difficult terrain to reach). Coiled rope everywhere. Three grapple-lines on the port rail: a PC can cut one with a slashing weapon (one action each, AC 12) — removing a Marine from the full boarding wave per line cut.

> [!check] Coiled Rope — DEX Save (DC 10)
> Triggered when a PC moves more than 20 ft in a single action.
>
> **Success:** the PC moves without fouling the lines.
>
> **Failure:** the PC falls prone.

**Zone 2 — Quarterdeck / Stern Rail (raised, 20 × 20 ft):** 5 ft elevation. Ranged attacks from Zone 2 against Zone 1 targets have advantage; melee attacks down from the rail have disadvantage. The Captain positions here the instant combat starts. Moving from Zone 1 to Zone 2 costs 10 ft of additional movement (the stairs).

**Zone 3 — Rigging and First Yardarm (vertical):** Jean-Claude's lane. Fifteen feet up via shrouds. From the yardarm: clear firing lines to Zone 2, 60 ft reach across the deck. A Marine ordered up by the First Mate has Athletics +1 — two actions to reach him.

> [!check] Zone 3 Climb — Athletics (DC 12)
> **Success:** the PC reaches the first yardarm in one action.
>
> **Failure:** no upward progress this action.

**Zone-wide trigger at Round 3:** the Noose's long cannon port swings open. Until the cannon fires or is stood down, every PC in the open on Zone 1 makes a saving throw at the end of their turn. Full cover removes the effect. The cannon fires only if: the Captain is downed without a stopping condition, a PC attempts to damage the Noose's hull, or no stopping condition appears by Round 6.

> [!check] Open Cannon Port — CON Save (DC 13)
> **Success:** the PC holds their nerve.
>
> **Failure:** the PC becomes Frightened until the start of their next turn. Full cover (capstan, etc.) negates this entirely.

## Tactical Notes

**The Captain:** opens on Zone 2, stays there. Priority targets: whoever downed the First Mate first (she needs an escort for the skiff withdrawal), then the PC she assessed as highest threat during the parley. She uses Command the Escort as a Bonus Action every round without exception — it is free damage from a Reaction she is not spending. At ≤25 HP she calls the withdrawal aloud and begins moving toward the rope ladder. She does not sacrifice herself; she is calm and methodical on both counts.

**The First Mate:** holds Zone 1 between the stairs and any PC trying to reach Zone 2. He is a wall, not a duelist. He does not disengage while the Captain is standing.

**The Marines:** pair on a single target each — one melee, one circling for a flank. They do not know the party's specific weaknesses; they go for the softest-looking target in the open (Catarina first if visible, Crissdalynn if Catarina has cover). When 2 of 4 are down they hold position rather than close further.

**The Noose herself:** never fires into an active boarding engagement without the Captain's order. The gun-crew's presence is psychological until the Round 3 trigger. She fires only on the conditions listed under Terrain.

**The party's structural exposure:** CHA and INT saves are nearly unprotected across four of five PCs. The parley actively surfaces this: Perrin is the only one who can anchor the highest-tier social roll, and the Captain will spend the parley's first ten minutes establishing who speaks with authority. During the combat escalation, Perrin's concentration (Hex, Bardic Inspiration timing) is the First Mate's obvious target — one longsword hit against AC 18 forces a CON concentration check.

## Run Sheet

### Foe Roster

| Foe | Init | AC | HP | Flees/breaks at | Action script |
|---|---|---|---|---|---|
| The Captain | +3 | 15 | 65 / 65 | Retreats to skiff at ≤25 HP or when First Mate falls | Zone 2; Multiattack 2× Cutlass +5; Bonus Action Command the Escort every round; Reaction Counterclaim on the highest-hit-chance attack |
| First Mate | +1 | 17 | 58 / 58 | Never retreats while Captain stands | Zone 1 at the stairs; Multiattack longsword +5 + shortsword +3; Parry reaction; targets whoever is moving toward Zone 2 |
| Marine × 4 | +0 | 11 | 32 / 32 each | Holds when 2 of 4 down; retreats with Captain on her signal | Zone 1; Multiattack 2× mace +4; pair on same PC; target Catarina first |

### Round Script

- **R1:** Captain rolls initiative from Zone 2. First Mate takes position at the stairs. Four Marines advance on the nearest open PC. Captain uses Command the Escort as Bonus Action — First Mate attacks with his Reaction.
- **R2+:** Captain Multiattack + Command every round. Marines pair and press. First Mate contests Zone 2 access.
- **Trigger — Round 3:** gun-crew sound on the Noose's port. Zone-wide CON save begins (see Terrain). Announce it openly — this is information the party can act on.
- **Trigger — Captain at ≤25 HP or First Mate down:** Captain calls withdrawal aloud and moves toward the rope ladder. Marines follow on her next turn. First Mate covers; he fights until 0 HP or the rope ladder.
- **Trigger — Captain downed without stopping condition, OR any attempt to damage the Noose's hull:** the Noose fires. The cannon delivers 3d10+5 force damage to the Uncertainty's hull (ship combat consequence; not PC HP). Resolve per [[siege-rules|Siege Rules]]. The encounter becomes a ship fight the party cannot win at Tier 2.

Statblocks: [[mave-sorn|Mave Sorn]] (NPC page + inline above) · First Mate: Veteran (SRD) · Marines: [[velvet-noose-marine|Velvet Noose Marine]]

## Raising the Stakes

- **Trigger:** Perrin uses Cutting Words during a social roll AND the roll still fails → **Delta:** the Captain notes his Bardic Inspiration and names him in her ledger. Her next clause is read directly to Perrin. Difficulty of that exchange rises by 2 for the rest of the parley.
- **Trigger:** Catarina deploys her Eldritch Cannon visibly during the parley → **Delta:** the Noose opens a second cannon port. The Zone-wide CON save threshold rises from 13 to 15 and the Frightened condition extends to the end of the PC's next turn instead of the start.
- **Trigger:** party attempts Vehicles (Water) to run and fails → **Delta:** the Noose deploys Fog Battery. A fog bank closes within one round. Running is not escape — it is stalling while she closes at 55 miles/day. The Fog is a 10-minute delay, not an out. Boarding begins at the end of it.

## Lowering the Stakes

- **Trigger:** party offers the fleet routing and Draves confirms it → **Delta:** the Captain signals the Noose by pennant. The gun-crew stands the long cannon down. The Frightened effect ends. She takes the terms without inspection and leaves the letter of transit on the hatch cover when she goes over the rail.
- **Trigger:** a PC introduces an intelligence the Captain clearly does not already have — a Crown signal, a named fleet officer, a route correction (History or Investigation, delivered plausibly) → **Delta:** she pauses. Actually pauses, for the first time. Tone shifts from presenting to negotiating. All subsequent social rolls gain +2 for the encounter.
- **Trigger:** during full boarding escalation, a PC cuts two or more grapple-lines in a single turn → **Delta:** the boarding rate stops. Marines already aboard remain; no new ones come over. This is the stopping condition the Captain will accept a ceasefire around.

## If They're Stuck

1. **Free tell:** the case is open on the hatch cover. Clause four reads: *"…supernatural irregularity manifesting as arcane attunement outside standard registry; subject may be unaware of the designation."* It is in plain sight, unguarded. Any PC who reads it knows what the Crown is tracking, and can plan accordingly.
2. **Costed nudge:** [[geoffrey-draves|Geoffrey Draves]] will confirm the fleet routing for free, without a Persuasion check, if the party frames it as "giving her something to leave with." He does not offer it unprompted — he will only confirm it, not volunteer it. The cost: Draves has revealed that he knew the Noose's position all along, and did not say so.
3. **Bail-out:** [[old-faas|Old Faas]] speaks up. He knows the name of a Midchain faction the Captain is already in active conflict with — he does not explain how, and the party should not push it. That name, offered as intelligence barter, moves the Captain's tone without requiring the party to reveal anything about themselves. The fiction cost: Old Faas now owes something he has not explained, and the Captain has his face.

## Endings

**Win — parley (full terms):** the Captain departs with fleet routing intelligence, the party holds the letter of transit and the dispatch order's original. [[geoffrey-draves|Geoffrey Draves]] is quiet on the way back to the helm. [[thunk|Thunk]] watches the Noose until she is out of sight.

**Win — parley (partial terms, contested):** the Captain departs with a partial manifest and no confirmed identity. She has everything she arrived with, plus the manifest. The dispatch stays with her. No letter of transit.

**Win — boarding (parley collapses, Captain retreats):** the Captain withdraws at ≤25 HP or with the First Mate down. The Noose does not fire if the Captain is ambulatory — she chose withdrawal over force, which is information. No letter of transit. The dispatch stays with her. What she does with it is Stakes.

**Defeat:** Captain downed without a stopping condition, or the party declines to cut grapples in a full boarding, or the Noose fires. The Uncertainty is brought alongside and boarded at full strength. The party is held and searched — she does not run a prison ship, she runs an information network — and released at [[midchain|Midchain]] minus the forward hold's contents. See Stakes.

**Disengage/flee:** Vehicles (Water) contest, per the beat. On success: a 40-second window to the northwest; the Noose closes it within three rounds at half sail. If the party refuses negotiation after the ranging shot and cannot escape: boarding begins, treat as full escalation. The Noose does not chase past the Midchain approaches — she has other work.

## Stakes

If the Captain departs with the dispatch and a confirmation of what the Crown is tracking, she sells the intelligence within 48 hours. The Crown learns within a week that she had the Uncertainty and let it go — and left richer. The search fleet tightens: heading changes appear on the next session's hex map.

If the party holds the letter of transit (full terms): Midchain harbour entries cost half the standard time and pass without a search. The Captain's name on the letter opens one door the party does not expect — stated the first time they show it to a harbour authority.

If the Uncertainty is boarded and searched: whatever is in the forward hold is Crown intelligence from this point forward, and the party's forward manifest is on record.

If Perrin's pact was confirmed or named during the parley: it is in her ledger. The Captain does not act on it immediately — she files it. What she files it under, and who she eventually sells it to, is a thread the DM runs forward.

## If Ignored

If the terms expire after the ranging shot without answer: the skiff returns with the same terms and a fifteen-minute deadline (per the beat). If that deadline expires: the Noose moves to full boarding. The Captain does not come aboard — she manages it from her quarterdeck by signal. No parley, no DC table, no letter of transit. The dispatch is confirmed by the search itself.

## Transition

- Parley accepted, full terms met → [[run-guide|Session 09 Run Guide]], Central Strait crossing continues, 2–3 hours elapsed
- Parley accepted, partial terms met → [[run-guide|Session 09 Run Guide]], crossing continues under changed intelligence conditions, 2 hours elapsed
- Parley collapsed, Captain withdrew → [[run-guide|Session 09 Run Guide]], crossing resumes, 4–6 hours elapsed; the mood aboard the Uncertainty is its own scene
- Noose fires, hull damage sustained → [[siege-rules|Siege Rules]] overlay, elapsed time suspended until resolved

---

*How to read this page: [[runbook-reading-conventions]].*
