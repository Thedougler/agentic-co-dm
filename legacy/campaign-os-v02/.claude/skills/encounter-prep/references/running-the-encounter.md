# Running the encounter

Load when writing Tactical Notes/Run Sheet/Raising the Stakes/Lowering the
Stakes for a prepped encounter, or when adjudicating a combat branch point
at the table. This is the canonical home for encounter *running* guidance —
`draft-moment`'s `.claude/skills/composing-beats/references/runtime-surface.md` loads this file for any
combat branch point instead of duplicating it (its own core
loop/DC-setting/keep-it-alive guidance stays generic across combat and
non-combat scenes). Role placement, tactical personality, difficulty
dials, running hordes, and table positioning/targeting/improvised-numbers
all live here.

---

## 1. Role placement and tactics

Justification: a role name alone doesn't tell a DM how to *run* it at the
table — where it stands, when to use it, what to avoid. `.claude/skills/draft-content/references/monster.md`
owns the seven roles' stat-priority *definitions* (§2 of
`vault/refs/vault/monster/references/cr-design.md`); this is where they're placed and played once combat starts.
Condensed from Sly Flourish's Monster Roles guide (`5e-mb-monster-
roles.md`).

- **Ambusher** — starts hidden, reveals only to attack, often re-hides.
  Use sparingly (drags fights out); good for a villain needing an escape,
  or a fight preceded by a social scene.
- **Artillery** — seeks cover/elevation, or spreads to the sides to force
  characters to split up. Characters shouldn't need more than ~1 round of
  movement to reach it — getting there should be fun, not a slog.
- **Bruiser** — front line, rarely switches targets. Use with care against
  1st-level parties (one-shot risk from a lucky crit).
- **Controller** — place out of easy reach but within its power's range;
  pairs well with a Defender guarding it. Watch for the same character
  locked down round after round — that reads as punishment, not
  challenge; rotate targets if it does.
- **Defender** — front line, or stationed near whatever it protects. Use
  sparingly — too many in one fight (or too many defender-heavy fights)
  slows combat and locks characters in place instead of letting them
  explore the encounter area.
- **Leader** — center or slightly back, near whoever it's boosting. Pair
  with 1–2 Defenders to protect it. Most interesting used sparingly, or
  varied in flavor (a healer priest reads differently from a
  buff-granting war-chanter) rather than repeated identically.
- **Skirmisher** — starts far enough out to show off darting in and
  retreating; rewards a battlefield with dividing terrain (walls, side
  chambers, multiple levels).

## 2. Tactical personality

Justification: pick one, govern all of a creature's decisions for *this*
encounter — a property of the instance, not of the reusable creature
kind (a `.claude/skills/draft-content/references/monster.md` page never bakes one in).

| Personality | Behavior |
|---|---|
| Apex predator | Targets weakest first; retreats only when cornered |
| Pack hunter | Coordinates with allies; piles on one target |
| Territorial | Attacks anything near lair; won't give chase |
| Cunning | Targets casters/healers; uses terrain; feigns weakness |
| Relentless | Fixates on one target; ignores flanking |
| Protective | Attacks whoever hit its ward; interposes itself |
| Chaotic | Rolls or chooses randomly; unsettling and unpredictable |

For a party of 5th level or higher specifically, also read
`vault/refs/vault/monster/references/lightning-rods.md`
before finalizing tactics — it reframes "how hard should this creature
counter the party" into "what should it let them show off."

## 3. Difficulty dials

Justification: published/designed stats are an average — these four
"dials," condensed from `vault/refs/vault/monster/references/difficulty-dials.md`, are the
fast, table-safe way to retune a fight without re-deriving CR mid-session.

- **Hit points.** Set anywhere within the Hit Dice's min–max, or as a
  rule of thumb, halve/double the average for a weaker/stronger
  individual. Turn down to end a dragging fight early; turn up if a fight
  is resolving too fast.
- **Number of monsters.** The most dramatic dial, and the most visible to
  players — plan in advance how creatures might flee/break (an undead
  horde collapsing once its necromancer dies) or how reinforcements might
  join a losing fight, so the change reads as diegetic, not arbitrary.
- **Damage.** Adjust within the attack's dice-expression range, or add a
  full extra damage die with an in-fiction reason (a weapon catches fire,
  a curse empowers a killing blow) — this reads as a clear threat
  increase to players, unlike a silent HP bump.
- **Number of attacks.** The highest-impact dial after monster count — a
  lone creature facing a full party often benefits from an extra attack;
  a monster on the ropes can lose one.

Mix dials together for the biggest shift (e.g., a weakened-but-frenzied
creature: HP down, attacks up) — don't turn every dial up on every fight
just to raise difficulty; an easy, fast-cutting battle is sometimes
exactly right. These four dials are the concrete mechanism behind a
Raising the Stakes or Lowering the Stakes dial that needs to trigger
mid-fight rather than being baked into the initial roster.

## 4. Running hordes

Justification: tracking individual HP/attacks for a dozen+ low-CR
creatures is the single biggest table-speed cost of a horde fight (the
"7+ (horde)" row of `combat-calibration.md`'s multi-enemy scaling table).
Condensed from `vault/refs/vault/monster/references/running-hordes.md`.

- **Pool damage.** Track one damage total for the whole horde instead of
  per-creature. Every time the pool exceeds one horde member's HP, remove
  a creature and reset the pool to zero (round HP to the nearest 5/10 to
  simplify). A single attack big enough to kill multiple members removes
  that many at once.
- **Resolve attacks/saves in bulk.** Instead of individual rolls, assume
  1/4 of the horde's attacks or saves succeed (1/2 with advantage, 1/10
  with disadvantage). Rolling anyway? Roll twice — each success means 1/4
  of the horde's rolls hit; both fail means none do.
- **Area effects vs. a packed horde** — baseline creatures caught, by
  area size: tiny (5 ft.) 2, small (10–15 ft.) 4, large (20 ft.) 16, huge
  (30+ ft.) 32, short line (60 ft.) 6, long line (120 ft.) 8. Lean toward
  more creatures caught, not fewer — that's the payoff for a party using
  AoE against a horde.
- **Keep it to one stat block per horde** — narrate physical variation,
  don't mix monster types into one horde. Once a horde thins to a
  manageable handful, switch back to tracking individuals normally.

## 5. Table positioning without a grid

Justification: this repo runs theater-of-the-mind by default. Condensed
from `vault/refs/theater-of-the-mind-extended.md`.

- Assume any creature can move within 5 ft. of any other, and every
  creature is in range of every ranged attack, unless stated otherwise
  (an enemy behind a protective line of allies, a longer distance called
  out explicitly).
- A creature within an enemy's reach that tries to move away provokes an
  opportunity attack, unless it can Disengage.
- Note up front which environmental features (a chandelier, a cracked
  pillar, a cliff edge) offer cover or a chance for a cinematic move, so
  players can use them without having to ask.

## 6. Identifying monsters and picking targets

Justification: how the table tracks "which monster is which" without a
map or minis — same source as § 5.

- Ask the player attacking a monster to describe its physical traits
  rather than naming its stat block.
- When it isn't clear which character a monster would attack, choose
  randomly and say so out loud — builds trust that the DM isn't
  targeting a favorite. If it's narratively obvious (going after a
  concentrating spellcaster), just say why.

## 7. Zone movement at the table

Justification: how a zone (`encounter-composition.md` § Zone-based
terrain definition) actually gets moved through and attacked across once
play starts. Condensed from `vault/refs/zone-based-combat.md`.

- On their turn, a character can move within a zone or move to an
  adjacent zone; extra movement allows up to two zones.
- Attacks with range ≥25 ft. reach the same zone or one zone away; ≥50
  ft. reach two or more zones away.
- A melee attack with 5-ft. reach provokes an opportunity attack against
  a target trying to move away, and imposes disadvantage on that
  target's ranged attacks while engaged.
- Areas of effect, by rough size: tiny (1–2 creatures, same zone), small
  (2–3, same zone), large (4–6, same zone), huge (12, across two zones),
  short line (2–3, same zone), large line (2–4, across two zones) — an
  area affecting a tightly packed horde can double these counts (§ 4).

## 8. Improvised numbers

Justification: for an unplanned combatant with no prepped stat block —
same source as § 5.

AC = 12 + ½ CR · attack bonus = 3 + ½ CR · save DC = 12 + ½ CR ·
single-target damage = 2d6 per CR · multi-target damage = 1d6 per CR.

## 9. Passive monster initiative and cinematic advantage

Justification: two fast table-speed tricks, condensed from
`vault/refs/quick-tricks-for-lazier-5e-games.md`.

- **Passive initiative.** For simple fights, skip individual monster
  initiative rolls — use `10 + the monster's Dex modifier` (puts most
  monsters mid-order), or for the fastest option, have every monster act
  on a fixed initiative count of 12.
- **Cinematic advantage.** Offer advantage on an attack or check if a
  player describes a high-action move (swinging from a chandelier to
  stab downward). Call for an ability check; success grants advantage on
  the next attack, failure has a real but fairly minor consequence
  (never fatal on its own) — the point is to make going for it feel
  rewarding, not risky.

## 10. Flee, surrender, and reinforcement waves

Justification: `vault/refs/vault/monster/references/lazy-tricks-for-running-monsters.md` § Other Lazy
Monster Tricks — running tricks for the actual arc of a fight, not a
creature's design. Feeds Tactical Notes' retreat/morale-break prompt
directly.

- Have foes flee or surrender when it makes narrative sense — a fight
  doesn't have to end in a pile of bodies to end.
- Constructs and summoned undead can be destroyed outright when whatever
  controls them dies or is banished — no separate morale check needed.
- Run multiple waves of monsters for a big set-piece battle instead of
  fielding everything at once (also keeps the creature-type cap
  meaningful — `encounter-composition.md` § 2).
- Reduce a monster's HP on the fly to let it drop or surrender sooner if
  the fight is dragging; raise its attack count if the party is having
  too easy a time (§ 3, Difficulty dials, is the fuller version of this).
