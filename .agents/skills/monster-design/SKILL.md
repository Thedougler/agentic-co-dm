---
name: monster-design
description: >-
  Design, tune, reskin, audit, and file monsters and creatures for D&D 5.5e
  (2024 / SRD 5.2.1): beasts, swarms, troops, minions, elites, legendary and
  solo bosses, and variants of existing creatures. Use when creating or
  improving a `type: creature` page or any part of one (statblock, difficulty
  against the live party, look, ecology, signs, weaknesses), or a named NPC's
  combat forms. Player-character builds go elsewhere.
---

# Monster design

In order of importance, a monster is:

1. **A fight worth having.** Its statblock threatens this party, the party
   you actually have, not the average party the Challenge Rating assumes. It
   is fun to fight, and it is flavourful, memorable, and sometimes
   terrifying. Every feature is a choice the players must answer.
2. **A real thing in the world.** It eats, nests, hunts, and leaves signs. The
   people of the setting have names for it, rules about it, and uses for its
   body. The campaign's canon shaped it.
3. **A look the table remembers.** Form follows function. Every ability shows
   on the body as a **tell**, and theatre-of-the-mind turns those tells into
   narration a sharp player can read.

File what constitution X makes canon. Follow `docs/agents/work.md`.

## Boundary contract

- **Input:** A named creature (existing page, variant, or one to mint), the
  caller's objective and brief (intended difficulty, encounter, environment),
  the live party's PC pages, `wiki/templates/creature.md`, and the vault canon
  the creature touches.
- **Work:** The steps below, for this one creature.
- **Done:** Every item in `## Done` holds for the reported page path.
- **Capability Handoff:** Every check, save, and escape DC gets the mandatory
  `dnd5e-mechanics` pass (the chassis sets the number, that skill sets the
  test). The narration goes to `theatre-of-the-mind` with the packet from
  step 7. A creature with a name, history, and personal ties is an NPC: its
  page belongs to `npc-design`, and this skill supplies the statblocks and
  encounter rule for its Combat section. The encounter it appears in belongs
  to `encounter-prep`; its lair or habitat place to `place-design`; items made
  from its body, or the item a creature disguises itself as, to `item-design`. A named owner the creature needs
  and the vault lacks is minted first by its owner skill (AGENTS.md **HARD:
  entity-before-spoken**). Each child returns its page path or result; resume
  at the step that waited on it, or report the named gap.

## Page rules

- **Canon.** User-said facts file immediately on the live path. Invented
  additions are shown to the DM as a proposal, marked as invention and citing
  the `[[pages]]` they grow from, and filed after the DM accepts.
- **Preserve.** Improving an existing page keeps every established fact; a
  retuned number replaces the old one and the proposal names the change.
- **One callout.** `[!narration]` is the only callout. Truths, origins, and
  secrets are plain complete sentences in Biology or Behavior.
- **Explicit DM layer** (AGENTS.md **HARD: dm-facing-explicit**). What it is,
  where it came from, and what it wants are stated by name.
- **Original expression.** Borrow patterns from published monsters, never
  their names or text. Paraphrase every rule.
- **Process stays off the page.** The party read, dossier, three-round script,
  and packet are working notes.

## Steps

[references/example.md](references/example.md) takes one monster through
every step; read it before step 3.

### 1. Read the party and the canon

**Party.** Read every PC page in `wiki/entities/pc/`, especially `## Sheet`,
`## Combat Profile`, and recent `## Session Log` fights. Write the **party
read** in working notes:

| PC | Level | AC | HP | Weak saves | Round-1 damage | Signature trick | Escape and mobility |
|---|---|---|---|---|---|---|---|

Then add the party's totals: **nova** (best first-round damage, all PCs),
**sustained** damage per round, healing per round, their hard control (stuns,
banishes, grapples, walls), and what ended their recent fights too fast. When
the DM says monsters have felt soft, those fights are the evidence.

**Canon.** Retrieve before inventing (constitution XII), using QMD per
AGENTS.md § Vault retrieval. Read the creature page if it exists, every page
that links to it (`grep -rliF "[[<name>" wiki/entities` for the slug, title,
and each alias), its region, and the places it lives. Search for its prey and
predators, the factions that hunt, fear, tame, or worship it, the items made
from it, and its lore. `qmd get` every hit you will use. Write the **canon
inventory**: `[[slug]]` · kind · the fact that ties it to this creature. List
the other creatures in its region and the ecological niche each one fills.

Done when every PC has a filled row, the party totals are written, and every
backlink and relevant search hit is in the inventory or dropped with a reason.

### 2. Choose the path

**Reskin** when only the fiction changes. **Variant** when one or two features
change. **Full design** when the role, decision loop, or chassis cannot be
reached either way. Write one line saying why the path is enough. A reskin
keeps its numbers, and the party read may still send it through step 5.

### 3. Make it this creature and no other

Read [references/concept.md](references/concept.md) for archetypes, diversity
axes, and exemplars.

1. **Stock version.** One line: "a big wolf", "a lich", "a giant jellyfish".
   Everything that line predicts is the default.
2. **Twist.** Break one rule the stock version keeps, using campaign canon.
   The lich whose phylactery is a place, not an object. The mimic grown to
   island size, wearing a paradise as bait. The hawk that lifts whales.
3. **Niche.** What it eats, where, when, and how. It fills a niche no creature
   in its region already fills, or it takes that niche differently (another
   layer of terrain, another time of day, another prey size).
4. **Form follows function.** Each signature ability comes from a body part
   or habit players can see: four wings for a rolling dive, a hum that goes
   quiet before the strike. Each striking body part does something in the
   fight.
5. **Fiction sentence.** "This is a [fantasy] [role] that [signature] to
   pursue [goal], fears [fear], and gives players [counterplay]." Then write
   Fantasy, Signature, Goal, Fear, Counterplay, and Proof, where Proof is the
   tell that makes the signature fair.
6. **Swap test.** Put a regional neighbour's name in place of this creature's
   name. Replace every line that stays true.

Done when the twist, niche, and signature all fail the swap test, meaning
each is true of this creature only.

### 4. Build the fight

Read [references/menace.md](references/menace.md). It covers what makes a
monster fun, memorable, tough, and terrifying.

1. **Difficulty target.** Standard, Hard, Deadly, or Terrifying, from the
   brief. Default to Hard for a named threat and Terrifying for a boss.
   Difficulty is set against the party read, not the CR label.
2. **Role.** One primary role; the first turn shows it.

   | Role | Function | Typical trade | Expected player response |
   |---|---|---|---|
   | Ambusher | Hides, strikes, withdraws | Burst for durability | Reveal it, deny hiding, ready actions |
   | Artillery | Ranged pressure | Offense for HP or AC | Cover, close distance, disrupt |
   | Bruiser | Dangerous melee | Damage and HP for AC, speed, or saves | Kite, control, focus fire |
   | Controller | Terrain, movement, conditions | Control for direct damage | Break setup, reposition, rescue |
   | Defender | Protects allies, holds space | Durability for damage | Bypass, shove, isolate |
   | Leader | Buffs, heals, commands | Team power for personal offense | Kill or separate it |
   | Skirmisher | Moves through the party | Mobility for durability | Pin it, deny routes |

   Rank (minion, standard, elite, solo) is separate from role.
3. **Signature move.** The feature players will talk about next session. Write
   **Tell → Threat → Responses → Payoff**: the visible windup, what happens if
   ignored, at least two viable answers, and the opening it leaves.
4. **Features.** Every feature expresses the concept and asks the players a
   question. Cut any feature with no response or payoff.
5. **Escalation.** How the fight changes when it is Bloodied, when its
   signature is answered, and when it is losing: a new form, a split, a
   retreat, a desperate move. Solos and bosses need one.
6. **Morale and ending.** When it flees, surrenders, bargains, or fights to
   the death, and why.

Done when the signature move has a written tell, at least two player answers,
and a payoff, and the escalation changes the players' choices.

### 5. Set the numbers

Run [references/reference-gate.md](references/reference-gate.md), then
[references/chassis-and-budget.md](references/chassis-and-budget.md), whose
**Tuning to the party** section sets the numbers against the party read.

- **Survive the nova.** The monster shows its signature at least once against
  the party's best first round.
- **Real threat.** At Hard and above, its three-round output can drop the
  party's most exposed PC, with a telegraph they can answer.
- **Trade, do not stack.** Get toughness from action economy, phases, allies,
  and position. Stacked AC, resistances, and immunities make a dull fight.
- **Honest answers to their tricks.** Their signature tricks still work, with
  a cost or a limit that has a reason in the fiction.

Write the three-round script and run
[references/audit-and-revise.md](references/audit-and-revise.md). Send every
check, save, and escape to `dnd5e-mechanics`.

Done when the three-round script against this party meets the difficulty
target and every audit item passes.

### 6. Make it real in the world

Fill the wiki knowledge in working notes. Each ability leaves a trace in the
world.

- **Habitat:** where it lives, which places it avoids, and why; wikilink those
  places.
- **Behaviour:** its daily habits, as a DM would play them.
- **Diet:** what it eats and what feeding leaves behind.
- **Social structure:** alone, in a pair, as a pack, colony, or court; young
  and life cycle when they matter.
- **In the world:** what locals call it, how they guard against it, what they
  trade its body parts for, and which factions hunt, use, or worship it. Link
  every owner page from the inventory.
- **Signs:** for each signature ability, the trace it leaves before anyone
  meets it (tracks, kills, sheds, sounds, damage). Players can read the fight
  ahead in the signs.
- **Instincts, Tactics, Weaknesses, Aftermath:** from steps 4 and 5.
  Weaknesses are things the party can do.
- **Truth:** its origin and any secret it carries, stated plainly.

Done when every canon inventory entry is placed, and every signature ability
has a sign.

### 7. Hand the look to theatre-of-the-mind

Build the **narration packet** as fragments, each with its source:

- **Body:** body plan and size against something familiar.
- **Focus:** the feature that makes people stare, usually the twist.
- **Surface:** colour, texture, and markings, each tied to the body part that
  carries it.
- **Senses:** one sound or smell that comes off it, with its source.
- **At rest:** what it does when nothing is bothering it; its habitat in one
  clause.
- **Tells:** the visible body part or habit behind each signature ability,
  written as plain appearance ("four wings, the lower pair broad and slow,
  the upper pair narrow"), never its function.
- **Leave out:** attacks, tactics, numbers, truths, and names the players have
  not earned.

Load `.agents/skills/theatre-of-the-mind`, portrait mode, creature recipe, and
give it the packet.

Done when the returned narration passes theatre-of-the-mind's final check and
contains every tell.

### 8. File the page

Copy `wiki/templates/creature.md`: a wiki article, statblock first, then what
the world knows about the creature. Statblock format:
[references/statblock.md](references/statblock.md).

| Section | Carries |
|---|---|
| Narration | The prose from step 7 |
| Statblock | At most one overview image just before the fence, then the `statblock` fence in 2024 phrasing |
| Visual reference | Facts from a supplied reference sheet, when one exists |
| Biology | Anatomy and how each body part works in play; origin and truth |
| Behavior | Habitat, Behavior, Diet, Social Structure, with "in the world" facts folded in |
| Tactics | Signs, Instincts, Tactics (opening, signature move, escalation, morale), Weaknesses, Aftermath |
| Art | Remaining images, each under its role subsection |

Omit empty sections, write complete sentences, and wikilink every owner page.
Run `wiki lint <path>`, then `wiki lint fix <path>`, and rerun until green.

## Done

- The party read and canon inventory are complete.
- The twist, niche, and signature fail the swap test.
- Against this party, the three-round script meets the difficulty target. The
  monster survives the nova long enough to use its signature, threatens a PC at
  Hard and above, and has an escalation if it is a solo or boss.
- The signature move has a tell, at least two answers, and a payoff; every
  feature expresses the concept.
- Every check and save passed `dnd5e-mechanics`; the statblock uses 2024
  phrasing with no hidden arithmetic.
- Every signature ability has a sign in the world and a tell in the narration.
- The narration came from theatre-of-the-mind and passes its final check.
- `[!narration]` is the only callout; the DM layer states the truth by name.
- Invention was proposed and accepted before filing; user-said canon is filed.
- `wiki lint <path>` is green, and one done-summary names the page and what
  changed.
