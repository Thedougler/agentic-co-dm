# Stat-block template

Use original names and concise paraphrase. Replace bracketed fields; delete fields that do not matter. Every feature must state timing, range, targets, save/attack, effect, duration, and counterplay where relevant.

## 2024 notation examples
- `Armor Class 16 (natural armor)`
- `Hit Points 68 (8d8 + 32)`
- `Speed 30 feet, climb 20 feet`
- `+6 to hit`, `DC 14 Dexterity saving throw`, `Hit: 13 (2d8 + 4) slashing damage`
- `Recharge 5–6`; `1/Day`; `at the end of its turns`; `until the end of its next turn`
- `60-foot Cone`; `15-foot Cube`; `one target it can see`; `each creature in the area`

## Full template
**[NAME]**
*[size] [type], [alignment/setting-neutral descriptor if needed]*

**Armor Class** [number] ([reason])  
**Hit Points** [number] ([formula])  
**Speed** [movement modes]

| STR | DEX | CON | INT | WIS | CHA |
|---|---|---|---|---|---|
| [ ] ([ ]) | [ ] ([ ]) | [ ] ([ ]) | [ ] ([ ]) | [ ] ([ ]) | [ ] ([ ]) |

**Saving Throws** [only if relevant]  
**Skills** [only if relevant]  
**Damage Resistances** [specific list and scope]  
**Damage Immunities** [specific, justified list]  
**Condition Immunities** [specific, justified list]  
**Senses** [senses], **Passive Perception** [number]  
**Languages** [languages or communicate how]  
**Challenge** [rank/CR], **PB** [bonus]

### Traits
**[Signature trait].** [Tell, trigger, effect, duration, answer.]  
**[Support trait].** [Effect and cost.]  
**[Weakness or lightning rod].** [How players can exploit it.]

### Actions
**Multiattack if needed.** [Number and choice; do not print attacks that are not used.]  
**[Basic attack].** *Melee/Ranged Weapon Attack:* [bonus] to hit, [reach/range], one target. *Hit:* [average] ([dice + modifier]) [damage], plus [limited rider].  
**[Signature action] (Recharge [range] or [frequency]).** [Area, tell, save/attack, effect, duration, counterplay.]  
**[Utility/action].** [Movement, summon, setup, or retreat choice.]

### Bonus Actions
**[Name].** [Only if it competes meaningfully with the action loop.]

### Reactions
**[Name].** [Trigger] and [effect]; [cost, limit, or tell].

### Off-turn/legendary actions if elite or solo
**[Action, cost].** [Timing, range, target, modest movement/attack/setup.]  
**[Action, higher cost].** [Stronger effect with explicit limit and counterplay.]

### Phases and bloodied if used
**Phase trigger.** [Observable condition.] **Change.** [New choice, terrain, or exposed weakness.] **Exit.** [What ends it.]  
**Bloodied.** [Threshold and response; do not hide a full reset.]

## Running the Monster
Design-time fields — work through these during creation, then distribute into the wiki note.

### Standalone creature → `wiki/templates/creature.md`

Linear layout: H1 → `[!narration]` → `## Statblock` (at most one overview image immediately before the fence) → Visual reference when present → Biology when present → Behavior (list items `- **Label.**`) → Tactics (list items `- **Label.**`) → Art subsections for remaining images. Exemplars: `wiki/entities/creature/bloodhawk.md`, `wiki/entities/creature/spiguar.md`.

- **Opening tell and preferred position:** [ ] → Tactics: **Signs**, **Instincts**
- **Default choice:** [ ] → Tactics: **Tactics**
- **If pressured / if signature is answered:** [ ] → Tactics: **Tactics**, **Weaknesses**
- **Target priority:** [ ] → Tactics: **Instincts**
- **Three-round script:** [round 1 / round 2 / round 3] → stays in design conversation
- **Resource tracking:** [recharge, pool, reaction, phase] → stays in design conversation
- **Player-facing counterplay:** [at least two answers] → Tactics: **Weaknesses**
- **Retreat, surrender, or failure state:** [ ] → Tactics: **Aftermath**
- **Encounter integration:** [allies, terrain, lightning rods, reinforcements] → Behavior: **Habitat**, **Social Structure**

### NPC with combat form → `wiki/templates/npc.md`

When statblocks embed in an NPC file, the same design fields distribute differently:

- **Opening tell and preferred position:** [ ] → `## Running [Name]`
- **Default choice, pressure response:** [ ] → `## Running [Name]` subsections
- **Target priority, counterplay:** [ ] → `## Running [Name]`
- **Encounter rule (which statblock to use):** [ ] → `# Combat` preamble
- **Stage/form conditions:** [ ] → one statblock fence per condition under `# Combat`
- **Retreat, surrender, failure state:** [ ] → `## Running [Name]`
- **Encounter integration:** [ ] → Relationships table + Running section
- **Three-round script, resource tracking:** → stays in design conversation
