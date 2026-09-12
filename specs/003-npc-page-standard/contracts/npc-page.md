# Contract: NPC page

The page the DM opens. Agents copy `wiki/templates/npc.md` and add optional sections from this file only when they have content.

## Identity

Required keys and defaults: [data-model.md](../data-model.md).

`role` is `rival` | `patron` | `contact`. Craft labels (informant, gatekeeper, foil) are not identity `role`.

Done when: every required key is present; unused `aliases` is absent.

Invalid: invented `type`; empty `summary`; defaulting `role`.

## Core spine

Order, always:

1. `#` title
2. `## At a Glance` — table rows Role, Nature, Home, Wants; extra rows only if they change how the DM runs the NPC; ends with `> **DM thesis:**` one sentence
3. Spoken look — `> [!narration] {Name}` with no secrets, DCs, unearned names, or thesis
4. `## Running {Name}` — first move and the change that shifts posture
5. `# Relationships` — wikilink + meaning; patron rows MAY add invitation

Done when: a DM can state role, want, first move, and fight handling (or that there is no fight) without leaving the page.

Invalid: the old `At the table` / `Wiki facts` outline; agent shorthand; spoken look that leaks.

## Optional sections

Add only with content. Relative order:

| After Running, before Relationships | After Relationships |
|---|---|
| Extra form (glance + narration) | Activity log |
| Unique lore | Appearances |
| History | Difficulty knobs |
| Current pressure | Combat |
| | Extra art |

Done when: unused sections are absent, not stubbed.

Invalid: empty `## History`, empty `# Combat`, placeholder extra forms, unused knobs.

## Combat

If the NPC can fight:

```text
# Combat
> **Encounter rule:** …
```

Then either a runnable on-page sheet or one pointer to the creature-page sheet.

If the NPC is not expected to fight: omit the heading.

Invalid: numbers on both the NPC page and a creature page; Combat with no encounter rule.

## Bands (density checks)

| Band | Must have beyond core | Must not have unless true |
|---|---|---|
| Landmark hostile (Hinewai) | Weakness or permanent end in Glance when those facts exist; extra form pairs; Combat stages keyed to a named condition | |
| Skirmish hostile (Skarn) | Running: opening, default turn, pressure, target priority, counterplay; one fight sheet | Staged sheets; patron ledger |
| Patron (Nona) | Current pressure; public vs secret when a secret exists; activity log after appearances | Combat unless they can fight |
| Contact (Thunk) | At most one Current pressure and one practical-use block | Patron ledger; extra forms; staged sheets |

## Layout source

Match heading order and density of:

- `wiki/_raw/Hinewai.md`
- `wiki/_raw/Talon Skarn.md`
- `wiki/_raw/Nona Black-Jaw.md`
- `wiki/_raw/Thunk.md`

Glance + spoken look and Running use the same two-pane column pair as those files. Creature notes stay linear.

## Write gate

Chat proposal first. Wiki write after DM accept (FR-019). Named-ingest stubs: identity + sentences; no optional scaffolding.
