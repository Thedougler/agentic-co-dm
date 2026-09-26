# Callouts

`[!narration]` is the only callout in this vault. It means one thing: words the DM reads aloud to the players. Everything else on a page is DM-facing already, so mechanics, secrets, and procedures are plain prose under their heading (`Checks`, `Secrets`, `At the Table`, the type's core section).

```markdown
> [!narration] Title
> Player-safe spoken text: what the characters perceive, present tense.
```

Titles in use:

- Owner pages: the subject's name (`> [!narration] Matteo Scola`), the player-safe look.
- Beats, encounters, and session-prep: `Opening`; Resolution uses `Closing Image`.
- Recaps: `Recap`.
- Lore: `Common telling`, when the lore has an in-world telling.

Rules:

- Write a narration block only when it has its spoken text; a page without a look yet has no narration block.
- Keep it open (never the collapsed `-` form) and outside table cells. Conditional spoken text in a table cell is `_italic_`.
- Nothing the players must not hear goes inside it: no secrets, DCs, unearned names, or DM thesis.
- Columns use the `col` / `col-md` codeblock syntax ([columns.md](columns.md)).

## Body line breaks

Callout bodies use real line breaks: continue each rendered line as its own quoted line. YAML frontmatter and fenced code or statblocks are the only places a literal backslash-`n` may appear.

```markdown
> [!narration] High air
> Dense grass waits sixty feet straight down.
> The wind shears across open sky.
```
