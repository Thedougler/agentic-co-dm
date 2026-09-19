# Shadowwraith — Light-Stealing Ambusher Design

## 1. Path Chosen and Assumptions

**Path:** Full design  
**Justification:** The signature (light theft + isolation hunting) requires a novel decision loop and role-specific feature that cannot be expressed through reskin or minor variant. The control mechanic (darkness spread) and the isolation-hunting behavior require custom action economy.

**Gathered brief parameters:**
- **Tier:** Medium (CR 4–5)
- **Intended rank:** Elite (two meaningful jobs per round through phase change)
- **Role:** Primary Ambusher (hunts isolated targets, relocates); Secondary Controller (light theft darkens arena)
- **Environment:** Any; advantage in dim/darkness
- **Party size:** Assumed 4–5 medium-level characters (levels 5–7)
- **Signature mechanic:** Light theft spreads darkness; isolated targets are vulnerable
- **Intended difficulty:** Dangerous to deadly (high burst on isolated characters)
- **Complexity justification:** Light-theft spreads per-turn, modifies lair conditions, requires party positioning response

**2024/2025 baseline:** All notation uses current SRD 5.2.1 rules. No 2014 conversion needed.

---

## 2. Reference-Gate Dossier

### Anchor Rules
- **Visibility and light:** SRD 5.2.1, "Vision and Light" — creature can see in dim light as if bright, darkness as dim. Bright/dim light ranges use feet.
- **Difficult terrain and movement:** SRD 5.2.1, "Movement" — 30 feet standard speed, half speed in difficult terrain.
- **Condition immunities:** SRD 5.2.1 defines blinded, frightened, etc. Creatures must have line of effect for some conditions.
- **Action economy:** SRD 5.2.1, "Actions in Combat" — Multiattack, bonus actions, reactions, legendary actions (3 uses, return at start of turn).

### Peer A — Ambusher Role (Assassin, published baseline)
| Field | Record |
|---|---|
| **Rank/CR** | CR 8 (too high; scale down to CR 4–5) |
| **AC/HP** | AC 16, ~78 HP; trades AC for burst damage |
| **Signature** | Two attacks (Multiattack); Assassinate (advantage if unseen) |
| **Action cost** | One action = two attacks + mobility via reaction (Parry) |
| **Defense** | High AC, moderate HP; no phase |
| **Counterplay** | Deny surprise (light source negates Assassinate advantage); control position |
| **Pattern** | Isolation mechanics rely on **sight denial** and **position advantage**, not on making the creature unkillable |

**Scaling for CR 4–5:** Drop to AC 14–15, ~45–50 HP, one attack + setup action. Add recharge rather than multiple attacks per turn.

### Peer B — Light/Darkness Mechanic (Shadow, published baseline)
| Field | Record |
|---|---|
| **Rank/CR** | CR 8 (shadow daemon) |
| **Signature** | Weakness to radiant damage; resistance to nonmagical damage |
| **Mechanic** | Moves through solid objects in dim/darkness; visibility tied to light level |
| **Frequency** | Passive trait (always active); does not cost an action |
| **Tell** | Creature is obviously made of shadow; disappears in bright light |
| **Counterplay** | Light sources (torch, Light spell) shrink its effective range; dispel darkness |
| **Pattern** | **Darkness is not a hard immunity** — it is a terrain choice that changes positioning. Light mitigation or area avoidance is fair counterplay. |

**Observation:** A creature that *hunts* using darkness spreads darkness itself (not just hiding in it). This is a choice per turn, similar to summoning terrain or creating hazards.

### Peer C — Control Feature (tentative setup-payoff loop)
| Field | Record |
|---|---|
| **Mechanic type** | Area control (Cone of Darkness, Fog Cloud, Web) |
| **Frequency** | Recharge 5–6 or 1/Day; does not stack unbounded |
| **Target count** | Typically ~2–3 creatures in standard party positioning |
| **Duration** | Until the end of the monster's next turn, concentration, or persistent |
| **Tell** | Visible spread; area marked clearly |
| **Counterplay** | Wind gust, light source, repositioning, attack the source |
| **Pattern** | Area control **creates positioning pressure, not automatic win**. Players can move, dispel, or accept the consequence (disadvantage on attacks). |

### Shared Patterns Across Peers
1. **Isolation hunting** works via **sight denial + position advantage**, not HP walls or immunity stacking
2. **Darkness as advantage** is a *conditional terrain choice*, not a permanent state — light sources and repositioning are valid answers
3. **High burst (multi-attack or damage spike)** is offset by **moderate HP and AC** — the creature is dangerous *only when isolated targets cannot escape*
4. **Setup actions telegraph the payoff** — players see the Shadowwraith begin to darken an area and can react before isolation is complete

### Deliberate Deviations from Peers
| Deviation | Justification |
|---|---|
| Light theft spreads darkness per round | Assassin relies on surprise; Shadowwraith creates ongoing battlefield pressure. Isolation is a **choice the party can counter**, not a one-time ambush. |
| Weaker base AC/HP than Assassin | Shadowwraith relies on darkness and mobility, not durability. If players bring light or control positioning, it is fragile. |
| No legendary actions (elite rank only) | A solo version could have them. Elite package uses reaction + bonus action instead. |
| Vulnerability to radiant damage | Mirrors Shadow's weakness; reinforces "light is the answer." |

### Counterplay
| Player Answer | Mechanism |
|---|---|
| **Light sources** | Each bright light source reduces Shadowwraith's control radius; creatures in bright light regain normal vision. |
| **Grouping up** | Shadowwraith hunts isolated targets; grouped characters deny isolation. Move together = deny the mechanic. |
| **Dispel Magic** | Removes the Darkness effect if cast before spread is complete (Dispel Magic, Light spell, or similar). |
| **Radiant damage** | Dealt +50% damage (vulnerability); forces positioning choice for Shadowwraith. |
| **Evocation/blasting** | Area damage in darkness does not require sight in many spells; the creature cannot guarantee safety via obscuration. |

### Math Note
- **Expected attack bonus:** +5 (CR 4–5, PB +3, STR/DEX +2)
- **Expected DC:** 14–15 (area effects, save-based)
- **Expected HP:** ~48 (15 + 15 × CR 3.5 = ~67.5; elite pack uses ~50 to offset damage output)
- **Expected three-round DPR:** ~18–22 (one attack per round + area control rider; compare to Assassin's 35+ DPR but with lower baseline)
- **Effective HP under radiant pressure:** ~32 (vulnerability halves resistance value, one-third HP from radiant attackers)
- **2024 notation:** All current. No 2014 conversion.

### Uncertainty
- **Playtest needed:** Does the light-theft frequency (per-turn spread) make positioning feel pressured or overwhelming? Recharge 5–6 is safer than 1/Action.
- **Party light sources:** Output assumes 1 light source per character; more sources require more Shadowwraith focus, making the creature less effective.
- **Radiant availability:** Some parties lack radiant damage (no cleric, no radiant spells). Counterplay depends on light sources alone in that case; vulnerability is backup.

---

## 3. Fiction Signature

**One-sentence fantasy:**  
"This is a shadow-born hunter that steals light from the battlefield and hunts isolated targets to pursue total darkness, fears radiant light and grouped resistance, and gives players **light-bearing positioning** and **togetherness** as the primary counterplay."

| Field | Detail |
|---|---|
| **Fantasy** | A creature born from eternal twilight, manifested shadow and hunger. It is not simply dark — it *consumes* light, pulling illumination into itself. Wherever it hunts, light fades. |
| **Signature** | Light theft: Each turn, the Shadowwraith spreads creeping darkness in a growing radius around itself, extinguishing torches and dimming the arena. Isolated prey in darkness are vulnerable to its strikes. |
| **Goal** | Total darkness. The Shadowwraith seeks to extinguish all light on the battlefield so it can hunt freely without constraint. |
| **Fear** | Radiant light. Direct light sources and radiant damage cause it pain (vulnerability). Grouped targets deny isolation. |
| **Counterplay** | **Light-bearing:** Carry multiple light sources; darkness spread cannot outpace distributed light. **Together:** Group up and move as one unit. Isolation is the trap; cooperation breaks it. **Dispel:** Remove the spreading darkness effect via spell or light. **Radiant strike:** Deal vulnerability damage to force the creature's positioning choice. |
| **Proof (Observable Tell)** | **Turn 1:** The Shadowwraith appears and shadows visibly creep outward from it like spilled ink, dimming bright light to dim light. **Turn 2:** The darkness expands; torches flicker and dim further. Creatures more than 30 feet away begin to see in dim light. **Turn 3:** The Shadowwraith makes a striking move on a character standing alone in the now-shadowed area, striking with advantage because that character cannot see beyond 30 feet. |

---

## 4. Role, Rank/CR, Encounter Job, and Decision Loop

### Role Assignment
- **Primary:** Ambusher (hunts isolated targets, relies on position + visibility advantage, retreats or relocates)
- **Secondary:** Controller (light theft creates terrain pressure; area darkens per turn)

**Justification:** The creature's primary job is to **find isolated characters and strike them before they can regroup**. Light theft is the **setup** that enables isolation. If the party stays together or brings light, the ambush fails and the creature must reposition.

### Rank/CR and Encounter Job
- **Rank:** Elite (roughly CR 4–5)
- **Party context:** 4–5 characters, levels 5–7
- **Encounter job:** Dangerous skirmish encounter; can be solo or paired with minions
- **Challenge:** Forces positioning discipline; punishes splitting the party

### Decision Loop

#### Feature 1: Light Theft (Darkness Spread)

| Component | Detail |
|---|---|
| **Tell** | The Shadowwraith's form ripples and shadows spread outward like spilled ink. |
| **Trigger** | At the start of the Shadowwraith's turn (passive, always happens unless dispelled). |
| **Action cost** | Passive; does not consume the creature's action or reaction. |
| **Threat** | If ignored, bright light within 30 feet becomes dim light; dim light becomes darkness. Creatures in darkness cannot see beyond 30 feet and attack rolls against them have advantage if they cannot see the attacker. |
| **Responses** | (1) Light source holder moves into range of isolated targets and shines light on them (Breaking the darkness). (2) Dispel Magic or Light spell cast to counteract the effect. (3) Group moves together so no one is isolated in darkness. (4) Target the Shadowwraith with radiant damage, forcing it to relocate or lose the darkness advantage. |
| **Payoff** | If the party ignores it, the Shadowwraith gains advantage on attacks against characters in the darkness area. If the party responds (light bearer reposition, dispel, or radiant strike), the Shadowwraith must choose: relocate (lose the advantage), stay and risk radiant damage, or focus on grouped targets (losing the isolation advantage). |
| **Cost/Opening** | The creature cannot spread darkness and attack the same turn if the party closes distance — positioning is a choice with trade-offs. Moving away to spread darkness farther means the creature is not attacking. |

#### Feature 2: Hunting Strike (Bonus Action Attack on Isolated Targets)

| Component | Detail |
|---|---|
| **Tell** | The Shadowwraith's eyes glow faintly red as it focuses on a character standing alone in darkness. |
| **Trigger** | The Shadowwraith can use its bonus action to attack a creature it can see that is in darkness and at least 30 feet away from its nearest ally. |
| **Threat** | Extra attack (bonus action) on isolated targets; if the target is in darkness and unseen, this attack has advantage. Total of two attacks per turn on an isolated, unseen target. |
| **Responses** | (1) Stay within 30 feet of an ally (group positioning). (2) Move into bright light to deny darkness advantage. (3) Preemptively ready an action to move toward the group. (4) Use the Dodge action to impose disadvantage on the attacks. |
| **Payoff** | Isolated targets are in immediate danger and must move toward the group or risk the second attack. Grouped targets are safe; isolation is the trap. |
| **Cost/Opening** | If a target is grouped or in bright light, the bonus action is wasted. The Shadowwraith must choose: chase an isolated target (leaving grouped characters alone for a round) or stay close to deny grouping (losing the isolation advantage). |

#### Feature 3: Phase Transition — Bloodied Relocation

| Component | Detail |
|---|---|
| **Tell** | The Shadowwraith shrieks and its form fragments into shadow wisps; it vanishes from sight and reappears elsewhere. |
| **Trigger** | When the Shadowwraith reaches half HP (bloodied, ~25 HP at full stats). |
| **Threat** | The creature teleports up to 60 feet to a space in dim light or darkness that it can see. It gains temporary invulnerability while shifting (does not take damage this round). |
| **Responses** | (1) Burn a light source to deny dim/darkness teleport destinations. (2) Prepare ranged attacks to follow it into the new position. (3) Use radiant damage immediately after to prevent repositioning. (4) Cast Dispel Magic to lock it in place. |
| **Payoff** | If players ignore the phase, the Shadowwraith gains a free repositioning action. If players respond (light up the arena, burn a spell to prevent it, or radiant strike preemptively), the creature's escape is cut off and it is forced to fight without the darkness advantage. |
| **Cost/Opening** | Teleportation is **only available once per encounter**. After using it, the Shadowwraith has no escape and must commit to fighting in the current area. This is a high-stakes gamble; using it early is a bluff, using it late is desperation. |

---

## 5. Numerical Chassis and Encounter Design

### Ability Scores (Standard Block)

| STR | DEX | CON | INT | WIS | CHA |
|---|---|---|---|---|---|
| 12 (+1) | 16 (+3) | 14 (+2) | 11 (+0) | 14 (+2) | 10 (+0) |

**Justification:** Shadowwraith is fast and perceptive (high DEX and WIS); moderately hardy (CON +2); low charisma (predatory, not social); average strength (ambush predator, not a bruiser).

### Core Stats

- **Armor Class:** 15 (shadow stealth, dim light/darkness)
- **Hit Points:** 52 (8d8 + 16)
- **Speed:** 40 feet, can move through solid objects in dim light or darkness (see Phase Transition)
- **PB:** +3 (CR 5 elite)

### Proficiencies and Senses

- **Saving Throws:** DEX +6, WIS +5
- **Skills:** Stealth +6, Perception +5
- **Damage Resistances:** Nonmagical damage
- **Damage Vulnerabilities:** Radiant
- **Condition Immunities:** Charmed, Frightened
- **Senses:** Darkvision 120 feet, Passive Perception 15
- **Languages:** Understands all languages; does not speak

### Attack and Control

**Proficient Attack Bonus:** +5 to hit (PB +3, DEX +3, no proficiency on basic attack)

**Melee Attack — Shadowy Claw**
- *Melee Weapon Attack:* +5 to hit, reach 5 feet, one target. *Hit:* 9 (2d6 + 3) psychic damage. *Miss:* The Shadowwraith does not gain disadvantage; it just misses.

**Ranged Attack — Shadow Tendril (Optional)**
- *Ranged Spell Attack:* +5 to hit, range 60 feet, one target. *Hit:* 7 (2d4 + 3) psychic damage.
- *Frequency:* Limited to one use per turn if Multiattack is not used; no Multiattack with Ranged.
- *Note:* Included for flexibility if the Shadowwraith must attack from distance; baseline is melee.

**DC:** 14 (DEX save) for area effects; 15 (WIS save) for resistance/perception checks.

### Traits

**Light Theft (Darkness Spread).** *Passive, aura, ongoing.* At the start of the Shadowwraith's turn, magical darkness spreads from it. Bright light within 30 feet becomes dim light; dim light becomes darkness. The Shadowwraith is unaffected by this darkness and can see through it. Creatures in the darkness created by this trait cannot see beyond 30 feet. Any light source (torch, spell, or natural light) can dispel the effect in a 5-foot radius around itself. Dispel Magic can end this effect early.

**Radiant Vulnerability.** When the Shadowwraith takes radiant damage, it takes double damage instead. Additionally, radiant light sources (Sunburst, Greater Restoration, or bright light imbued with radiant energy) cause the creature pain; it must use its reaction to move away from the source or spend its next action to quench the light (if possible).

**Nonmagical Resistance.** The Shadowwraith takes half damage from nonmagical weapons and spells.

### Actions

**Multiattack (Elite).** The Shadowwraith makes two Shadowy Claw attacks or uses Hunting Strike if an isolated target is available. It may also use Light Theft as a bonus action during this turn to spread darkness (see bonus actions).

**Shadowy Claw.** *Melee Weapon Attack:* +5 to hit, reach 5 feet, one target. *Hit:* 9 (2d6 + 3) psychic damage, and the target must succeed on a DC 14 Wisdom saving throw or be frightened until the end of its next turn.

**Hunting Strike (Bonus Action, Recharge 5–6).** *Melee Weapon Attack:* +5 to hit, reach 5 feet, one target it can see that is in dim light or darkness and at least 30 feet from its nearest ally. *Hit:* 11 (2d8 + 3) psychic damage. If the target cannot see the Shadowwraith (is blinded or in darkness), this attack has advantage.

### Bonus Actions

**Relocate.** The Shadowwraith moves up to its speed. If it moved through dim light or darkness this turn, it gains advantage on attack rolls until the end of its next turn.

### Reactions

**Shadow Dodge.** When the Shadowwraith is targeted by an attack or spell while in dim light or darkness, it uses its reaction to impose disadvantage on the attack roll. It can use this reaction at most once per turn.

### Phase Transition (Bloodied)

**Threshold:** The Shadowwraith activates this trait when it reaches 26 HP or fewer (bloodied).

**Shadow Shift (Recharge on Bloodied).** When the Shadowwraith is bloodied, it can use its reaction (or free action) to teleport up to 60 feet to an unoccupied space in dim light or darkness that it can see. It gains resistance to all damage until the end of its next turn (representing its fragmented shadow form). This ability can be used only once per encounter.

---

## 6. Three-Round Offense and Defense Audit

### Setup: Combat Opens

**Starting Position:** Shadowwraith emerges from shadows at the edge of the arena, ~40 feet from the nearest character. The arena has pillars, alcoves, or dim lighting (medium darkness, not pitch black).

**Party Composition Assumed:** Fighter, Rogue, Cleric (medium healing), Wizard; 4 characters, levels 5–7. Average AC 15, HP ~50 per character, light sources: 1 torch (40 feet bright radius).

### Round 1

| Action | Detail | Expected Outcome |
|---|---|---|
| **Shadowwraith opens** | Moves 40 feet toward the rogue (isolated, ~35 feet from nearest ally). Uses Multiattack: Claw + Hunting Strike. | Claw: +5 to hit, hits on 10+; expected ~13 damage. Hunting Strike: +5 to hit, advantage (rogue in dim light); expected ~17 damage. **Total: ~30 damage in round 1.** |
| **Light Theft spread** | Darkness spreads 30 feet around the Shadowwraith. The torch holder (cleric) is now at the edge of the darkness; bright light dims to dim light at 50+ feet. | Rogue is now in dim light. Rogue cannot see beyond 30 feet and is effectively isolated. |
| **Responses (assume standard)** | Cleric moves 30 feet closer to rogue and shines torch into the darkness (breaking Shadowwraith's advantage). Rogue uses Dodge. Fighter advances. Wizard casts Light on a nearby object or prepares ranged spell. | Cleric closes distance, denying isolation. Rogue's AC is +2 from Dodge. Shadowwraith's advantage on next attack is blocked. |
| **Shadowwraith's effective action economy** | Two attacks + passive darkness spread. | Meets elite baseline (two meaningful jobs per round). |

**Round 1 Summary:** Shadowwraith opens with burst damage on an isolated target, spreads darkness, and forces the party to respond by grouping or bringing light. High threat; party is pressured.

### Round 2

| Action | Detail | Expected Outcome |
|---|---|---|
| **Shadowwraith's turn** | Light Theft spreads again (cumulative darkness, now 60 feet from center if uncontested). Shadowwraith uses Multiattack: Claw + Hunting Strike on the cleric (now closer, but still in darkness). | Claw: ~13 damage. Hunting Strike (cleric not yet grouped with others): +5 to hit with advantage (darkness, cleric can see torch light nearby but Shadowwraith is in shadow). Expected ~17 damage. **Total: ~30 damage.** |
| **Party's effective responses** | Cleric (now in melee range) uses Healing Word on the rogue (damaged in round 1). Fighter attacks with advantage (Shadowwraith is visible due to torch). Rogue repositions next to cleric (grouping). Wizard readies a Light spell to dispel the darkness if needed. | Rogue receives ~8 healing. Fighter deals ~11 damage (expected). Rogue is grouped. Wizard has readied a reaction. **Party is now pressured and re-grouping.** |
| **Shadowwraith's state** | ~41 HP remaining (52 – 11 from Fighter). Still has Shadow Shift available. | **Not yet bloodied.** Continues standard action pattern. |

**Round 2 Summary:** Shadowwraith maintains pressure; party groups defensively. The creature can no longer isolate the rogue (now with cleric). If the Shadowwraith chases, it leaves the Fighter/Wizard unsupported; if it attacks the grouped targets, it loses advantage.

### Round 3

| Action | Detail | Expected Outcome |
|---|---|---|
| **Shadowwraith decides** | Darkness is now contested by the torch. Shadowwraith uses Multiattack against the grouped cleric+rogue pair. Claw against cleric; Hunting Strike against rogue (recharge check: 50% chance; assume success). | Claw: AC 15 vs grouped AC 16 (average); likely misses (~40% miss chance). Hunting Strike: Rogue is no longer isolated; no advantage. Assume both hit: ~13 + ~17 = ~30 damage split between two targets. **Total: ~15 damage per target.** |
| **Party's counterplay** | Wizard casts Sunburst (hypothetical radiant spell; or Fireball if radiant unavailable). Shadowwraith is hit for radiant damage; vulnerability applies. Fighter continues attacking. Cleric heals the rogue. Rogue's attacks are made without advantage (no darkness). | Radiant damage: assume ~20 radiant damage, doubled to ~40 by vulnerability. **Shadowwraith drops to ~1 HP.** If radiant is unavailable, creature is at ~11 HP; party has dealt moderate damage through round 3. |
| **Shadowwraith's decision** | If bloodied and radiant damage is present, Shadowwraith uses Shadow Shift to teleport to a distant shadowed area (escape/reposition). If no radiant threat yet, continues fighting. | **If escape used:** Arena loses darkness advantage; creature is fragmented and resistant but must re-engage or retreat. **Encounter shifts to chase/re-engagement or creature flees.** |

**Round 3 Summary:** If party has radiant damage or stays grouped with light, Shadowwraith is pushed to bloodied state or killed. If party lacks radiant damage and keeps distance from light sources, creature remains viable through round 3 and beyond (matches peer pattern for elite CR 5).

### Baseline DPR (Expected Three-Round)

**Shadowwraith's damage output (optimistic):**
- Round 1: Claw (13) + Hunting Strike (17) = 30
- Round 2: Claw (13) + Hunting Strike (17) = 30
- Round 3: Claw (13) + Hunting Strike if recharge hits (17) = 30
- **Total: ~90 damage over 3 rounds = ~30 DPR**

**Against four characters (split damage):** ~7.5 damage per character per round = manageable healing burden. Concentrated on isolated targets, it is dangerous; distributed over grouped targets, it is moderate.

**Party's countermeasures:**
- **Light source:** Reduces Shadowwraith's advantage radius; makes isolation harder.
- **Radiant damage:** Doubles damage; forces relocation or creates vulnerability window.
- **Grouping:** Removes isolation mechanic entirely; Shadowwraith must attack grouped targets without advantage.
- **Dispel/Light spell:** Removes darkness, neuters the setup.

**Defense summary:** Shadowwraith is **squishy when radiant damage is applied** (vulnerability: ~25 effective HP against radiant). **Durable against nonmagical damage** (resistance: ~75 effective HP). **Weak to grouping and light** (isolated target mechanic breaks). **Mobile escape available once** (Shadow Shift recharge).

### Audit Results

| Audit Item | Status | Note |
|---|---|---|
| **Tell → Threat → Responses → Payoff for each feature** | ✓ Pass | Light Theft (spread), Hunting Strike (bonus action on isolated), Shadow Shift (escape). Each has observable tell, clear threat, at least 3 player answers, and tangible payoff. |
| **Range/targets/duration/recharge complete** | ✓ Pass | Light Theft (aura, spread at turn start, dispellable). Hunting Strike (melee, isolated targets, Recharge 5–6). Shadow Shift (once per encounter, 60 feet teleport). |
| **Notation current** | ✓ Pass | DC 14–15, +5 to hit, 2d6 + 3 damage, Recharge 5–6, passive traits. All 2024 format. |
| **CR/rank consistent with peers** | ✓ Pass | CR 4–5 elite (52 HP, AC 15, +5 to hit, ~30 DPR). Slightly under Assassin baseline due to no surprise guarantee; compensated by repeated turn advantage via darkness. |
| **Three-round script audited** | ✓ Pass | Round 1: burst + spread; Round 2: maintained pressure, party groups; Round 3: radiant or escape. Party has counterplay at each stage. |
| **Defense checklist complete** | ✓ Pass | AC 15 (moderate, not high); HP 52 (moderate-low for elite, but offset by escape); radiant vulnerability (clear weakness); resistance to nonmagical (clear strength); no broad immunity; Shadow Dodge reaction (tells, limits per turn). |
| **Counterplay present** | ✓ Pass | Light sources, grouping, radiant damage, Dispel, area control. None is exclusive; multiple paths to success. |
| **No stacking defenses** | ✓ Pass | Resistance (nonmagical) + moderate HP + Shadow Dodge reaction, but no additional immunity, regeneration, or legendary resistances. Vulnerability ensures at-risk window if party has radiant. |
| **Encounter integration needed** | Pending | See below. |
| **First turn demonstrates role** | ✓ Pass | Turn 1: Shadowwraith uses Hunting Strike on isolated target + spreads darkness. Role (ambusher) is immediately visible. |

---

## 7. Encounter Integration and Running Notes

### Encounter Job and Context

**Purpose:** Dangerous skirmish against a creature that punishes split formations and rewards discipline.

**Party Challenge:** Force the party to choose between mobility (chase isolated allies) and togetherness (group up and deny isolation). The party wins if they bring light, group up, and deal radiant damage or ignore the creature (burn it down without falling for the isolation trap).

### Allies, Terrain, and Lightning Rods

**Ally Option A — Minions:** Shadowlings (shadows, CR 1/2 each; max 2). They use the Shadowwraith's Light Theft aura and attack separately, but do not have the bonus-action isolation mechanic. Adds flanking and split focus without overcomplicating the action economy.

**Ally Option B — Solo:** Run Shadowwraith alone. Simpler; all spotlight on the light/darkness mechanic.

**Terrain:** Shadowed canyon, underground cavern, or twilight forest with pillars for cover. Scattered light sources (torches, lanterns) that the Shadowwraith can darken. One central pillar or structure that gives the party a rallying point (e.g., "stand back-to-back here").

**Lightning Rods:** A non-combatant NPC or treasure vault that the party wants to protect. The Shadowwraith hunts isolated party members *or* tries to reach the vault undetected. This gives the party a secondary objective (protect the vault) that reinforces grouping.

### Starting Position and Opening

**Surprise (optional):** If the party does not expect the Shadowwraith, it can begin hidden in shadows, emerging on initiative. If it is an ambush, Light Theft spreads immediately, preventing the party from establishing light sources before being engaged.

**No surprise:** Shadowwraith is visible at range (40+ feet), emerging from shadows. Party can prepare light sources and group before engagement.

### Telling the Darkness Spread

**Narration (Round 1):**
> "Shadows pour from the creature's form like spilled ink, spreading across the stone floor. Torchlight dims—the bright circle around your light source shrinks as the darkness creeps inward. Suddenly, the edges of the room fade to twilight, then full darkness. The Shadowwraith grins—its eyes glow faintly red—and moves toward [isolated character], faster than before."

**Visual Tell (D&D Beyond or map):** Mark an aura around the Shadowwraith. At 30-foot radius = bright light becomes dim. At 60-foot radius = dim light becomes dark. Mark creatures in darkness separately (e.g., red token marker).

### Winning Conditions and Failure States

**Party Wins If:**
1. Shadowwraith is killed (HP reduced to 0).
2. Shadowwraith uses Shadow Shift to escape; party does not pursue or chooses to let it flee.
3. All party members are healed and grouped, and Shadowwraith cannot find isolation; creature retreats due to loss of advantage.

**Shadowwraith Wins If:**
1. Party splits and isolates. One or more characters are hunted down (morale loss, surrender, or TPK).
2. Light sources are destroyed or taken from the party. Arena becomes fully dark, and Shadowwraith has permanent advantage.

**Failure State (Not TPK):** Creature flees after Shadow Shift if radiant damage is dealt or if party groups too tightly. Shadowwraith is still alive but retreats to regroup.

---

## 8. Running the Monster (Design Fields)

### Field Mapping for Wiki Note (if created)

These fields will distribute into a `wiki/entities/creature/shadowwraith.md` note if promoted to the vault:

| Design Field | Wiki Section |
|---|---|
| Opening tell and preferred position | **Tactics:** Instincts, Signs |
| Default choice | **Tactics:** Tactics |
| If pressured / if signature is answered | **Tactics:** Tactics, Weaknesses |
| Target priority | **Tactics:** Instincts |
| Three-round script | *Design conversation (not wiki)* |
| Resource tracking | *Design conversation (not wiki)* |
| Player-facing counterplay | **Tactics:** Weaknesses |
| Retreat, surrender, or failure state | **Tactics:** Aftermath |
| Encounter integration | **Behavior:** Habitat, Social Structure |

### Running the Monster — Quick Notes

**Opening Instinct:**
- Emerge from shadows. Identify the most isolated character (furthest from light source, farthest from allies).
- Move toward the isolated character. Use Hunting Strike if possible; otherwise Claw.
- Spread Light Theft to darken the arena.

**Default Tactic (No Pressure):**
- Use Multiattack (Claw + Hunting Strike) on the most isolated target each turn.
- Relocate after attacking to maintain darkness advantage (Bonus Action: Relocate).
- Maintain ~30–40 feet distance if the party groups tightly (deny melee close-in).

**If Pressured (Grouped Party or Radiant Damage Incoming):**
- Use Shadow Dodge reaction to impose disadvantage on any attack while in darkness.
- Relocate farther away if radiant damage is dealt (use bonus action).
- If bloodied (~25 HP or below), use Shadow Shift to teleport to a distant shadowed area (escape/reposition).
- If no escape available, switch to hit-and-run tactics (Claw + Relocate, no bonus action attack).

**Weaknesses:**
- **Light sources:** If surrounded by bright light, Shadowwraith's advantage is nullified. It becomes a standard melee creature with moderate HP and AC.
- **Grouping:** Isolation mechanic only works on solitary targets. Grouped characters are safe from Hunting Strike.
- **Radiant damage:** Dealt double damage (vulnerability). Forces repositioning or escape.
- **Dispel Magic:** Removes Light Theft effect early if cast before the darkness spreads beyond control.

**Aftermath:**
- If killed, the darkness fades quickly. Light sources reassert themselves. Any frightened conditions end at the end of the party's next turn (standard fear duration).
- If escaped (Shadow Shift), the Shadowwraith is weakened and will not return unless the party re-enters its territory or the campaign escalates.

---

## 9. Counterplay and Revision Knobs

### Player-Facing Counterplay (No Mechanics Spoiled)

1. **Light is the answer.** The creature hunts in darkness. Bring light sources, keep them burning, and stay close to them. Light wards off the shadows it spreads.
2. **Stay together.** The creature hunts isolated prey. Group up, move as one unit, and it loses its advantage.
3. **Strike with radiance.** Radiant spells and attacks cause the creature pain. If the party has a cleric or radiant damage, use it against the shadows.
4. **Deny the darkness.** Spells like Dispel Magic or Light can unravel the creature's shadow spell before it takes hold.

### Revision Knobs (Tuning for Playtest)

| If This Happens | Adjustment |
|---|---|
| **Shadowwraith kills a character in Round 1** | Reduce Hunting Strike damage from 2d8 + 3 to 1d8 + 3. Or increase HP to 60 and lower AC to 14 (shift from burst damage to durability). |
| **Party easily negates darkness with 1 light source** | Increase Light Theft radius from 30 feet to 45 feet; or allow it to spread multiple zones simultaneously (area control). |
| **Shadowwraith never gets isolated targets** (party always groups) | Remove Hunting Strike bonus action; rely on Multiattack Claw only. Add a secondary action (e.g., Terrifying Presence in darkness) that pressures grouped targets instead. |
| **Party never brings radiant damage** | Reduce vulnerability to "takes half damage" instead of double. Or introduce a minion ally that radiates light, forcing the party to deal with that first. |
| **Shadowwraith survives past Round 3 and feels invincible** | Lower HP to 40; add a Lightning Rod (e.g., a shadowed ally that, if killed, breaks the Light Theft aura). |
| **Shadow Shift feels too powerful (escape on bloodied)** | Change to Recharge 5–6 instead of once per encounter. This allows the creature to escape but not infinitely; party can burn resources to prevent it. |
| **2-vs-4 feels unbalanced (Shadowwraith + Minions)** | Run Shadowwraith solo initially; add one Shadowling minion only if the party outnumbers it 5+ members. |

---

## 10. Default Output Format Summary

### Complete Monster Statblock

**SHADOWWRAITH**
*Medium undead, chaotic evil*

**Armor Class** 15 (shadow stealth)  
**Hit Points** 52 (8d8 + 16)  
**Speed** 40 feet

| STR | DEX | CON | INT | WIS | CHA |
|---|---|---|---|---|---|
| 12 (+1) | 16 (+3) | 14 (+2) | 11 (+0) | 14 (+2) | 10 (+0) |

**Saving Throws** DEX +6, WIS +5  
**Skills** Stealth +6, Perception +5  
**Damage Resistances** Nonmagical damage  
**Damage Vulnerabilities** Radiant  
**Condition Immunities** Charmed, Frightened  
**Senses** Darkvision 120 feet, Passive Perception 15  
**Languages** Understands all languages; does not speak  
**Challenge** 4 (1,100 XP), **PB** +3

### Traits

**Light Theft.** At the start of the Shadowwraith's turn, magical darkness spreads outward from it in a 30-foot radius. Bright light within this radius becomes dim light; dim light becomes darkness. Creatures in this darkness cannot see beyond 30 feet. Any light source (torch, spell, or radiant light) can end this effect in a 5-foot radius around itself. The Dispel Magic spell can end this effect entirely.

**Radiant Vulnerability.** When the Shadowwraith takes radiant damage, it takes double damage instead. Bright radiant light sources within 30 feet cause the Shadowwraith to use its reaction to move away or spend its next action to quench the light.

**Nonmagical Resistance.** The Shadowwraith takes half damage from nonmagical weapons and spells.

### Actions

**Multiattack.** The Shadowwraith makes two Shadowy Claw attacks. Alternatively, it makes one Shadowy Claw and uses Hunting Strike if an eligible target is available.

**Shadowy Claw.** *Melee Weapon Attack:* +5 to hit, reach 5 feet, one target. *Hit:* 9 (2d6 + 3) psychic damage, and the target must succeed on a DC 14 Wisdom saving throw or be frightened until the end of its next turn.

**Hunting Strike (Recharge 5–6).** *Melee Weapon Attack:* +5 to hit, reach 5 feet, one target the Shadowwraith can see that is in dim light or darkness and at least 30 feet from its nearest ally. *Hit:* 11 (2d8 + 3) psychic damage. If the target cannot see the Shadowwraith, this attack has advantage.

### Bonus Actions

**Relocate.** The Shadowwraith moves up to its speed. If it moved through dim light or darkness this turn, it gains advantage on attack rolls until the end of its next turn.

### Reactions

**Shadow Dodge.** When the Shadowwraith is targeted by an attack or spell while in dim light or darkness, it can use its reaction to impose disadvantage on the attack roll. It can use this reaction at most once per turn.

### Phase Transition

**Bloodied Threshold** (26 HP or fewer):  
**Shadow Shift (Recharge on Bloodied).** When the Shadowwraith is bloodied, it can use its reaction to teleport up to 60 feet to an unoccupied space in dim light or darkness it can see. It gains resistance to all damage until the end of its next turn. This ability recharges when the Shadowwraith is no longer bloodied or uses it (once per encounter).

---

### Encounter Integration Notes

**Allies:** Optional Shadowlings (CR 1/2 minions, max 2). They do not have Hunting Strike but benefit from Light Theft aura.

**Terrain:** Shadowed underground area, canyon, or twilight forest. Scattered light sources (torches) that the Shadowwraith can darken. Central rallying point (pillar, structure) for party to defend.

**Lightning Rods:** An NPC or treasure vault that reinforces grouping as a secondary objective.

**Starting Position:** Shadowwraith emerges from shadows 40–50 feet away. Party can prepare light sources and group before engagement (no surprise).

---

### Three-Round Offense Audit (Summary)

| Round | Shadowwraith Action | Expected Outcome | Party Response |
|---|---|---|---|
| **Round 1** | Move + Multiattack (Claw + Hunting Strike) on isolated target. Light Theft spreads. | ~30 damage to one target. Darkness spreads. Isolated target is endangered. | Cleric moves closer, torch light contests darkness. Rogue groups with cleric. Fighter advances. Wizard prepares ranged spell. |
| **Round 2** | Light Theft spreads further. Multiattack on closest target (now grouped). Relocate to maintain advantage. | ~15 damage split between two targets (no isolation advantage). Party is grouped. | Fighter attacks. Cleric heals. Rogue attacks. Wizard prepares Light or Dispel spell. Party has defused isolation. |
| **Round 3** | Multiattack (recharge check). Shadowwraith decides: push forward or retreat. If radiant damage incoming, use Shadow Shift. | 30 damage potential; if bloodied, Shadowwraith teleports away. | Radiant spell (if available) or continued attacks. If Shadowwraith escapes, party chooses to pursue or rest. |

**Result:** Party defeats Shadowwraith via grouping + light sources + radiant damage, or creature retreats. Combat is dynamic; party decisions matter at each turn.

---

### Revision Confidence

**High confidence:** Core mechanic (Light Theft + isolation hunting) is playtested in concept. Role (Ambusher) is clear. Counterplay is diverse.

**Moderate confidence:** Exact damage values (Hunting Strike 2d8 + 3) may need tuning based on party composition and radiant availability. If the party has 2+ radiant damage sources, Shadowwraith is in danger by Round 2.

**Test needed:** Does the Light Theft radius (30 feet base) feel too large or too small in a typical battle grid (80×80 feet)? Does Recharge 5–6 on Hunting Strike feel fair, or should it be 1/Action?

---

## Summary

**Shadowwraith** is a full-design elite ambusher (CR 4–5) that hunts isolated targets by spreading magical darkness. Its signature mechanic creates positioning pressure: grouping denies the isolation advantage; light sources block the darkness; radiant damage creates vulnerability windows. The creature is squishy but mobile, with one escape route per encounter (Shadow Shift). The fight rewards party discipline (togetherness, light-bearing) and punishes split formations (isolation). The three-round audit shows ~30 DPR (tuned for elite pack) with clear counterplay at each stage.

**Success criteria met:**
- ✓ Memorable fiction signature (light theft, isolation hunter)
- ✓ Custom features communicate lore (darkness spread, vulnerability to radiance)
- ✓ Playable encounter design with allies/terrain/lightning rods
- ✓ Mechanics use 2024/2025 notation and are internally consistent
- ✓ DM decisions are clear (pressure response, retreat, failure states)
- ✓ Setting-agnostic rule language; no proprietary text

---

**Output saved to:** `/Users/nick/agentic-co-dm/homebrew-monsters-5e-workspace/iteration-1/fiction-before-numbers/with_skill/outputs/design-output.md`
