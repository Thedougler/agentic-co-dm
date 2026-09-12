# `[!check]` — the DM scan for every roll on this picture

**Role:** after a spoken picture of a place, person, or object, one callout
holds every skill, save, contest, and group roll the party could try.
The prep did the adjudication; the table replays it.

## Use when

A picture just landed and the party can roll: look, talk, steal, save,
push, hide, contest, or a group check.

## Never for → use instead

- A standing rule with no roll → `[!mechanic]`.
- A secret with no player path to it → plain prose.
- Passive-perception gating with no roll → plain prose stating the threshold.

## Prose contract

- **Title:** the pictured thing (`La Vasca`, `Goat at the tideline`). Skills
  live in the table, not the title.
- **Body:** one table, every line prefixed `>`.

| Check | DC | Failure | Pass |

**Check** — `Perception`, `Wisdom save`, `Athletics vs Athletics`, `Group Dexterity`.
**DC** — a number. A four-band group roll writes `bands`. A contest writes `contest`.
**Failure** / **Pass** — what the DM says or does. Wikilink the fact. A pipe
in an alias is `[[page\|Alias]]`. Group bands compress into these two cells:
Failure holds CF and F; Pass holds S and CS, each with its number range.

One callout per picture. More rolls are more rows.

Group 5d20 (cold-open Hook beat steps,
`.claude/skills/writing-cold-opens/references/cold-open-page.md` § Repo
integration): five d20s, one per
player seat, named-skill modifiers, summed. Fewer than five seated → the
DM distributes the leftover dice. State that mechanic here only — the
row writes `Group <Skill>` and `bands`.

Worldview sets an NPC's starting social DC:
`.claude/skills/composing-beats/references/runtime-surface.md`.

## Example

```markdown
> [!check] La Vasca
>
> | Check | DC | Failure | Pass |
> |---|---|---|---|
> | Perception | 13 | dock noise | the tribute basin — [[old-faas]] |
> | Insight | 14 | he is in a hurry | the sea debt before the arch — [[umberlee]] |
> | Group Dexterity | bands | CF 5-24: the ram takes him at the tideline. F 25-49: in the open. | S 50-84: party already in the water. CS 85+: he lives. |
```

## Conversion table

| Found | Fix |
|---|---|
| Bare check table under a heading | wrap it in `[!check] <picture>` |
| Tiered `**Success:**` / `**Failure:**` body | one table row |
| `[!check] Perception (DC 15) — Label` | title is the picture; skill and DC move into the row |
| A second `[!check]` for the same picture | another row |
| Untitled `[!check]` | name the picture |
| An attack roll's target labeled as a difficulty class | `AC <n>` (W70) |
| A DC table row with no skill and no failure | fill Check and Failure (W70) |

## CSS

```css
.callout[data-callout="check"] {
  --callout-color: 76, 175, 125;
  --callout-icon: lucide-dices;
}
.callout[data-callout="check"] table {
  width: 100%;
  font-size: 0.92em;
}
.callout[data-callout="check"] th,
.callout[data-callout="check"] td {
  padding: 0.2em 0.45em;
  vertical-align: top;
}
```
