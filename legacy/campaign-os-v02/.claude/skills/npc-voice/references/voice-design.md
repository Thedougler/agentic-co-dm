# Writing voice descriptions that design well

The `design` command turns a prose description into ~3 voice previews. ElevenLabs
reads it literally — every concrete acoustic fact steers the result; vague vibes do
nothing.

## Description recipe

Cover, in one paragraph:

1. **Body & age** — "enormous middle-aged orc", "wiry old woman". Size and age move
   pitch and weight more than any adjective.
2. **Pitch & timbre** — "deep booming baritone", "thin reedy tenor", "gravelly
   whisper".
3. **Accent, by reference** — a nationality or a well-known archetype ("thick
   Austrian accent, like a 1980s bodybuilder action hero") lands far better than
   invented fantasy accents. Pick the real-world accent the table will recognize.
4. **Delivery** — pace and attitude: "speaks slowly, cheerfully, with total
   confidence", "clipped and impatient", "warm, faintly amused".

Ground every item in the NPC's canon page — their read-aloud box and quoted lines
already encode accent and cadence ("You are the new crew, ja?" ⇒ Germanic accent).

## Sample text (`--text`)

Pass a signature line from the NPC's page, 100–300 characters — the API rejects
anything under 100 ("String should have at least 100 characters"). The previews
then audition the actual table dialogue, and the GM judges the voice on words it
will really speak. A too-short signature line: pad it with a second in-voice
sentence rather than filler. No `--text` falls back to auto-generated filler.

## Settings on `say`

| Flag | Range | Effect |
|---|---|---|
| `--stability` | 0..1 | Low = more expressive/variable between takes; high = consistent, flatter. Start 0.4–0.5 for characterful NPCs. |
| `--similarity` | 0..1 | How hard to stick to the designed voice. Default is fine; raise toward 0.9 if takes drift off-voice. |

Omit both to use the voice's account defaults. One regenerate with `--force` and a
nudged stability is normal; more than two paid retries on one line → stop and ask
the GM what's wrong with the read.
