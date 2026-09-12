# Species/Race Design Reference (Tasha's model, 2021+)

Read this when `rule-prep`'s interview establishes `subtype: subsystem` for
a homebrew species/race (species has no dedicated template subtype of its
own; see `.claude/skills/rule-prep/SKILL.md` § Subtype routing). Mined from the legacy
`dnd5e-homebrew` skill's species design reference.

## Standard template

```markdown
## [Species Name]
*[Flavor sentence — what this species is, where they come from.]*

### [Species Name] Traits
**Creature Type.** You are a Humanoid. [Or: also considered [type] for any
prerequisite or effect requiring it.]
**Size.** You are Medium. [Or Small.]
**Speed.** Your walking speed is 30 feet. [Add swim/climb/fly if the
concept calls for it, budgeted per the table below.]
**[Signature Trait Name].** [The species' primary mechanical identity.]
**[Secondary Trait Name].** [One additional moderate ability.]
**[Tertiary Trait/Skill].** You gain proficiency in [skill/tool/weapon].
**Darkvision.** 60 feet, if applicable.
**Languages.** Common + one other, agreed with the DM.
```

## Feature budget system

Target total: **5–6 points**. Every trait costs from this table; sum
before finalizing, don't design past budget and rationalize afterward.

| Feature | Cost |
|---|---|
| Darkvision 60 ft | 1.0 |
| Darkvision 120 ft | 1.5 |
| Skill proficiency | 0.5 |
| Tool proficiency | 0.25 |
| Weapon proficiency (single weapon) | 0.25 |
| Weapon proficiency (martial group) | 0.75 |
| Armor proficiency (light) | 0.5 |
| Language | 0.25 |
| Resistance, common damage type (fire/cold/poison) | 1.5 |
| Resistance, uncommon type (psychic/radiant/necrotic) | 1.0 |
| Cantrip | 1.0 |
| Spell 1/day (1st–2nd level) | 1.0 |
| Spell 1/day (3rd level) | 1.5 |
| Spell 1/day (4th–5th level) | 2.0 |
| Innate spell progression (1st@1st, 2nd@3rd, 3rd@5th) | 2.5 |
| Advantage on a specific save type | 1.0 |
| Advantage on a specific skill | 0.75 |
| Flight speed (30 ft, light-armor-only) | 2.5 |
| Swim speed (30 ft) | 0.5 |
| Climb speed (30 ft) | 0.5 |
| Powerful unique passive (Dwarven Resilience-tier) | 1.0–1.5 |
| Expertise in one skill | 1.5 |
| Natural armor (AC = 13 + DEX) | 1.5 |
| Natural weapon (1d6 unarmed) | 0.5 |
| Amphibious | 0.5 |

## Worked budget examples

- **Elf-tier (~5.5 pts)**: Darkvision 60 (1.0) + Fey Ancestry-equivalent
  (1.0) + a ribbon rest-trait (0.5) + a skill proficiency (0.5) + a cantrip
  or speed+proficiency package (1.0–1.5) + a language/weapon extra
  (0.5–0.75).
- **Dwarf-tier (~5.5 pts)**: a resilience passive (poison adv+resist, 1.5),
  Darkvision 60 (1.0), a scaling HP trait (1.5), a tool proficiency (0.25),
  weapon-group training (0.5), and a knowledge-expertise trait (0.75).
- **Tiefling-tier (~5.25 pts)**: Darkvision 60 (1.0) + a damage resistance
  (1.5) + an innate-spell package (2.5) + a language (0.25).

## ASI guidelines (Tasha's model)

Standard: +2 to one ability score, +1 to a different one. Alternative: +1
to three different scores. The **player** assigns these — never hard-code
which ability a species "must" raise.

## Subraces

If the species has subraces: the base carries 3–4 points, each subrace
adds 1.5–2 more, and each subrace's features must distinguish its own
fantasy meaningfully — two subraces that feel identical mechanically have
failed the split.

## Red flags

- **Flight at level 1** (30+ ft) — very strong, restricts encounter design;
  if included, light/no-armor-only and budget the full 2.5.
- **Two damage resistances** — 3 points from resistance alone is too much
  for anything short of a Very-Rare-tier concept.
- **At-will invisibility or misty-step-tier mobility** — needs a once-per-rest
  limit at minimum.
- **Full innate spell progression + a resistance + darkvision together** —
  budget overflow; cut one.
- **Free expertise at level 1** — expertise is already a strong class
  feature (Rogue/Bard); giving it to a species costs a full 1.5.
- **True immunity** (not resistance) — reserve for Very Rare concepts with
  a real trade-off attached; almost never appropriate at the species level.
- **A nonstandard creature type with no drawback** — a Fiend or Undead
  species should interact with Turn Undead/Protection from Evil-type
  effects, not just gain the flavor with none of the cost.
