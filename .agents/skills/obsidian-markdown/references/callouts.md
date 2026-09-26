# Callouts

`[!narration]` is the only callout in this vault. It means one thing: words the DM reads aloud to the players. Everything else on a page is DM-facing already, so mechanics, secrets, and procedures are plain prose under their heading (`Checks`, `Secrets`, `At the Table`, the type's core section).

```markdown
> [!narration] Title
> Player-safe spoken text: what the characters perceive, present tense.
```

A page carries one narration block per moment the players live through, at the slot its template gives it. Titles in use:

- Owner pages: the subject's name (`> [!narration] Matteo Scola`), the player-safe look, in the header row. Moment slots below it: `In action` (creature), `First meeting` (npc), `When met` (faction), `In use` (item), `On contact` (hazard), `Underway` (vehicle), `{Area}` and `Returning` (place), `On the road` (region), `Common telling` and `Found text` (lore).
- Beats, encounters, and session-prep: `Previously` (the session's first beat), `Opening`, `{Creature}` and `{NPC}` (titled with the name, as each enters), `Revelation`, `Outcomes`, `Exit`, `If the session ends here` (cliffhanger), `Closing Image` and `Stinger` (resolution).
- Recaps: `Recap`.

Rules:

- Write a narration block only when it has its spoken text; delete an empty slot.
- Keep it open (never the collapsed `-` form) and outside table cells. Spoken text for one branch goes in the table's Narration column as `_italic_`.
- Nothing the players must not hear goes inside it: no secrets, DCs, unearned names, or the DM's At a Glance read.
- Columns use the `col` / `col-md` codeblock syntax ([columns.md](columns.md)).

## Body line breaks

Callout bodies use real line breaks: continue each rendered line as its own quoted line. YAML frontmatter and fenced code or statblocks are the only places a literal backslash-`n` may appear.

```markdown
> [!narration] High air
> Dense grass waits sixty feet straight down.
> The wind shears across open sky.
```
