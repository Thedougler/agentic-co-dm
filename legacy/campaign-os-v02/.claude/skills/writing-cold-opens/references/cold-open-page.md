# Cold Open Page

The written artifact: the page skeleton, this repo's beat-page integration, and
wiki conventions. The workflow lives in `../SKILL.md`.

## Repo integration

A cold open is one Hook beat page, instantiated from the beat template in
`vault/_templates/` at `status: pending`, and composed against its session's
Beat Chart by `composing-beats`.

- Each step is **a picture, then one `[!check]`** whose table holds the group
  row (`.claude/skills/callouts/references/check.md` § Group check). The DM
  ruling at `docs/rulings/0001-cold-open-group-check.md` binds the mechanic: a
  cold-open step resolves on one combined group check — five d20s, one per
  player seat, named-skill modifiers, summed — never five individual checks.
- **Pass** and **Fail** read `if the party does X` / `if they do not`. The
  borrowed POV is the subject of the pictures, never a named-PC choreography.
- Address the borrowed NPCs by their established names, not "you all".
- **Next** carries two labeled landings. A mid-chain Fail that ends the open
  links its Fail landing on that step.
- The cold open's own short story, when it has one, is
  `vault/stories/session-NN-scene-N-<slug>.md` in second person, present tense
  (`draft-story`).

## Page skeleton

Where the beat template leaves discretion, fill this shape:

```markdown
# Cold Open — <Title>

> **Runtime:** 20–30 minutes
> **POV:** [[Character]]
> **Hook mode:** <type>
> **Handoff:** <one line>

## Purpose

- **Why now:** ...
- **Main-session connection:** ...
- **Player takeaway:** ...
- **PC knowledge afterward:** ...

## POV Brief

- **Character:** [[Character]]
- **Immediate goal:** ...
- **Situation:** ...
- **What the players need to know:** ...
- **Relevant capabilities:** ...

## Opening Frame

<player-facing narration>

## 1. Orientation — <check/save>

**Situation:** ...
**Prompt:** ...
**Success:** ...
**Failure:** ...
**Advance:** ...

## 2. Pressure — <check/save>

## 3. Complication — <check/save>

## 4. Crisis — <check/save>

## 5. Payoff — <check/save>

## Final Image

<player-facing narration>

**Hard cut:** <first image or situation of the main-PC scene>

## Carry Forward

- **Fixed facts established:** ...
- **Variable state to resolve during play:** ...
- **Player knowledge:** ...
- **PC knowledge:** ...
- **Future payoff / open question:** ...
```

Steps 2 through 5 repeat step 1's five fields.

## Wiki conventions

Keep DM-facing notes short enough to run straight from the page at the table.

Use `[[wikilinks]]` for established entities instead of repeating their lore.
Pull detail from the entity's own page when a step needs it, rather than
copying a second authoritative description into the cold open.
