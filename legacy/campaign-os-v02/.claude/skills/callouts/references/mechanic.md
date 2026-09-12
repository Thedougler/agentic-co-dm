# `[!mechanic]` — a rule the DM applies

**Role:** the crunch the DM must apply correctly mid-scene — hazard, trap effect,
environmental rule, phase trigger, condition, access requirement — packaged so it can be read
in three seconds with dice in hand.

## Use when

- A hazard or trap: what triggers it, what it does, in numbers.
- An environmental or lair rule: the rising water, the aura, the unstable floor.
- A fight-phase trigger: "at 85 HP or below, Unstable Form activates."
- A one-off stat note inline in a scene (a named foe's key numbers for *this* fight).

## Never for → use instead

- A roll-gated branch with success/failure outcomes → `[!check]`.
- Flavor or description → prose or `[!read-aloud]`.
- A recurring creature or NPC's full stat block → its own page; wikilink it.
- A whole page of mechanics (a `rule` page) → plain sections; a page that is all mechanics
  needs no mechanic callouts.

## Prose contract

- **Bold lead term** naming the mechanic, then trigger → effect, in that order.
- Explicit numbers always: DCs, damage dice, durations, ranges. Never "appropriate damage"
  or "a hard save".
- Three or more parallel cases → a table, not prose.
- One mechanic per callout. The poison and the alarm it triggers are two callouts.

## Example

```markdown
> [!mechanic]
> **Blue bottles — contact poison.** Bare-skin contact: DC 13 CON save. Fail: 2d6 poison
> damage and poisoned 1 hour. Success: no effect. Closed bottles give no smell and no
> residue — nothing marks them as dangerous.
```

## Conversion table — misuses found in this vault

| Found | Fix |
|---|---|
| `[!CAUTION]` / `[!WARNING]` wrapping a hazard | `[!mechanic]`, trigger-first |
| A `## Hazards` prose/bullet section with no callout | one `[!mechanic]` per hazard |
| `[!IMPORTANT]` wrapping an inline stat line | `[!mechanic]` |
| Success/failure outcomes stated inside | move the roll to a `[!check]`; keep only the standing rule here |
| Two mechanics in one block | split |
| A DC (in prose or a table) with no named ability/skill or no stated failure consequence | name the ability/skill and what a failed roll does, or move a genuine roll-gated branch to its own `[!check]` (W70 warns) |

## CSS

```css
.callout[data-callout="mechanic"]   { --callout-color: 94, 129, 172;  --callout-icon: lucide-cog; }
```
