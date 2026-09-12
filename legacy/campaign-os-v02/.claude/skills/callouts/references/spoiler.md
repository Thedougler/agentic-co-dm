# `[!spoiler]` — canon the party hasn't reached yet

**Role:** the future-hiding block. Content that, if a player reads it, spoils plot or story —
but only the part still *ahead* of the table: a canon fact or event the party has not yet
interacted with. Distinct from a plain-prose handling note (a moment's own DM instructions,
not wrapped in any callout — `[!dm]` is retired): `[!spoiler]` is the spoiler payload itself,
isolated so a CSS toggle can hide/show it without touching anything else on the page.

**Not a spoiler, ever:** anything that already happened in a session (played out at the
table, even if a given PC wasn't present or doesn't know it — the *players* do), and any PC's
own backstory (a player already knows their own character's history). Both go in plain prose,
never in `[!spoiler]`.

## Use when

- A canon fact or future event still ahead of the party in play, and that plain
  prose would otherwise state outright: an unsolved mystery's answer, a hidden identity, a
  secret motive behind something not yet uncovered.
- A fact a player could read on this page (an NPC bio, a location page, a faction page) ahead
  of the table reaching it in a session.

## Never for → use instead

- Anything that already happened at the table, in any session → plain prose (it's not ahead
  of the party, so it can't spoil anything).
- A PC's own backstory → plain prose (the player already knows it).
- A DM-only handling note for a moment in play (secret cache location, stage direction) →
  plain prose.
- A roll-gated discovery → `[!check]`.
- A rule or number the DM applies → `[!mechanic]`.
- Background lore with no spoiler risk → plain prose.

## Isolation contract — the hard rule

A `[!spoiler]` callout must be self-contained in both directions:

- **Nothing outside the callout may depend on or reference what's inside it.** The rest of the
  page must read completely, and make sense, with the callout deleted. Never write "as
  explained below" or "(see spoiler)" pointing into it, and never state a fact in plain prose
  that only makes sense *because* of what the spoiler reveals.
- **Nothing inside the callout may be information players already know.** Only the not-yet-known
  payload goes in the box — known facts stay in plain prose outside it.

This isolation is what lets a future CSS rule hide every `[!spoiler]` block and leave a
fully coherent, spoiler-free page behind.

## Prose contract

- Lead with the concrete fact, plainly stated — no coy hedging, no "it turns out that...".
- One revelation per callout. A second spoiler fact is a second `[!spoiler]`.
- No title needed; add one only when a page carries several `[!spoiler]` blocks and they need
  to be told apart.

## Example

```markdown
<NPC name> runs <the faction>'s dockside operation and has never been seen
without her signature red coat.

> [!spoiler]
> <NPC name> is <the rival's> estranged sister, working the docks under a false
> name to keep watch on <what she is really tracking> without his knowledge.
```

## Conversion table — misuses found in this vault

| Found | Fix |
|---|---|
| An unencountered twist stated in plain prose on an NPC/location/faction page | wrap it in `[!spoiler]` |
| Plain prose that only makes sense given the spoiler ("that's why she avoids him") | fold the dependent sentence into the `[!spoiler]` itself, or cut it |
| A plain-prose handling note holding a plot twist rather than a table handling note | `[!spoiler]` |
| Two unrelated twists in one block | split into two `[!spoiler]` callouts |
| Something already revealed in a session, or a PC's own backstory, wrapped in `[!spoiler]` | unwrap it — plain prose, it's not ahead of the party |

## CSS

```css
.callout[data-callout="spoiler"]    { --callout-color: 191, 54, 54;   --callout-icon: lucide-eye-off; }
```
