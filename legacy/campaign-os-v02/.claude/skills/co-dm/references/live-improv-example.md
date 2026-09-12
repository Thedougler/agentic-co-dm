# Live improv — worked example

Read for a full worked trace of the stub-check → improvise → capture cycle
(SKILL.md Workflow steps 2-5, Hard Rules 1-2) end to end.

## Worked example (fixture — placeholder names, not real campaign content)

> **Player:** "What's the vendor's name, and how much for that dagger?"

1. Stub check: `grep -ril "dockside market\|enchanted dagger" vault/` — no hits.
2. Miss → improvise: "Toma runs the stall — she wants 40 gold for the
   dagger, or 30 if you can name a ship that's been through Tidefall in
   the last month." (Ties the price to something the party can actually
   engage with, not a flat number.)
3. Append to `vault/episodes/<NNN>/table-notes.md`:

```markdown
## IMPROV: Toma, dockside dagger vendor
- **Said:** "Toma wants 40 gold for the dagger, or 30 for the name of a
  ship through Tidefall this month."
- **Type:** npc
- **Context:** Dockside market stall, early in the session, unplanned.
```

4. Answer given, scene continues. `Toma` and the dagger are now durable —
   INGEST will pick up the block whether or not the audio caught the aside.

## Staying reactive once the NPC is live

An improvised NPC dies the moment they stop tracking the room. Three moves
keep one alive, all free of prep
(`vault/refs/stories/prose-and-character-craft.md` § NPC entrance,
move 6):

- **React to the line the PC just said**, not to the topic. A player who
  invents something to bluff you gets it caught: name it, price it, or
  laugh at it, but never let it pass unnoticed.
- **Call back something from a minute ago.** Quoting a PC's own earlier
  line back at them costs nothing and reads as a mind behind the voice.
- **Let the NPC be undignified.** Spitting while talking, laughing at their
  own joke, being wrong in public. Dignity is what makes an improvised NPC
  interchangeable.
