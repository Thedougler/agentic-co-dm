# Callouts

## ai-co-dm house callouts

```markdown
> [!narration] Narration
> Player-facing TotM prose. Empty stub ok on pass 1.

> [!narration] Initial Narration
> Session/run beat scene-setting. Mandatory empty stub on pass 1. Fill on pass 2.

> [!mechanic]
> Table procedure, DCs, HP, conditions — owner pages. Not used on session/run cards.

> [!secret] Title
> Hidden truth / unearned lore on owner pages. Never inside narration.
```

On long-lived owner pages such as NPC, PC, or faction pages, collapse a secret when
that page benefits from progressive disclosure:

```markdown
> [!secret]- Title
> Collapsed hidden truth / unearned lore.
```

## Session/run surfaces

On run-guide, session-prep, session, and beat notes:

- The only callout is `[!narration]`.
- Title the mandatory scene-setting block **Initial Narration**.
- Place additional titled stubs after the Zones table (`{Place}`) and after the Threat clock table (`Tick {n}`) only when those tables have no Narration column; one How the Scene Resolves callout for the unconditional spoken state; and after each roster embed (`{Creature}`).
- Conditional spoken (zone, tick, most-likely How the Scene Resolves option) lives in the table cell as `==_italic_==`. Do not stack a titled callout per option.
- Empty stub bodies and empty Narration cells are required on mechanical pass 1. Pass 2 fills every body and every spoken cell.
- Procedure is a **heading**. Do not add a `DM truth` section — the whole card is DM-facing. Do not use `[!secret]` / `[!mechanic]` on session/run cards.
- Never put a callout inside a table cell. Obsidian does not render it there.
- Keep callouts open: never the collapsed `[!…]-` form.

Collapsed secrets remain allowed on long-lived owner pages such as NPC, PC, or faction
pages when progressive disclosure is useful.

## Syntax

```markdown
> [!note]
> Body.

> [!warning] Custom Title
> Body.

> [!faq]- Collapsed by default
> Body.

> [!faq]+ Expanded by default
> Body.

> [!question] Outer
> > [!note] Nested
> > Inner
```

## Body line breaks

Callout bodies use real line breaks: continue each rendered line as its own
quoted line, and keep list items on separate lines. Never serialize a line
break as a literal backslash followed by `n`. This rule is especially strict
for run-guide, session-prep, session, and beat notes. YAML frontmatter and
fenced code/statblocks are the only exemptions (including YAML string values
inside a statblock fence); elsewhere, a literal `\n` is a FAIL.

```markdown
> [!narration] High air
> Dense grass waits sixty feet straight down.
> The wind shears across open sky.
```

## Built-in types

`note` · `abstract`/`summary`/`tldr` · `info` · `todo` · `tip`/`hint`/`important` · `success`/`check`/`done` · `question`/`help`/`faq` · `warning`/`caution`/`attention` · `failure`/`fail`/`missing` · `danger`/`error` · `bug` · `example` · `quote`/`cite`

## Plugin callout types

`[!col]` · `[!col-md]` / `[!col-md-N]` — obsidian-columns layout. See [COLUMNS.md](COLUMNS.md).
