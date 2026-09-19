# Columns (obsidian-columns plugin)

Plugin: [obsidian-columns](https://github.com/tnichols217/obsidian-columns). Three syntaxes. **Session/run cards use codeblock syntax** so `[!narration]` stays a real callout. Owner pages may use callout syntax when the row has no spoken callout.

## Callout syntax (preferred)

Works in live preview. Cannot limit column height.

`[!col]` makes each top-level item a column. `[!col-md]` nested inside groups items into one column.

### Two columns

```markdown
> [!col]
> First column content.
>
> Second column content.
```

### Grouped items in one column

```markdown
> [!col]
> First column content.
>
>> [!col-md]
>> Line one of second column.
>>
>> Line two of second column.
```

### Width adjustment

Append a multiplier to `col-md`: `[!col-md-2]` makes that column twice as wide.

```markdown
> [!col]
> Narrow sidebar content.
>
>> [!col-md-3]
>> This column is three times the width of the first.
>>
>> More content here.
```

Valid multipliers: `0.5`, `1`, `1.5`, `2`, `2.5`, `3`, `3.5`, `4`, `4.5`, `5`, `5.5`, `6`, `6.5`, `7`, `7.5`, `8`, `8.5`, `9`, `9.5`, `10`.

### Nested columns

Nest a new `[!col]` inside a `[!col-md]`:

```markdown
> [!col]
> Left column.
>
>> [!col-md]
>>
>>> [!col]
>>> Nested left.
>>>
>>> Nested right.
```

### Callout title

The `[!col]` title is hidden by CSS. Any text after `[!col]` is not rendered.

## Codeblock syntax

All settings available. Works in live preview. Parent codeblocks **must have more backticks** than children.

### Basic

`````markdown
````col
```col-md
Column A
```

```col-md
Column B
```
````
`````

### Settings block

Everything above `===` is settings. Both `col` and `col-md` accept a settings header.

**`col` settings:**

| Setting | Values | Effect |
|---|---|---|
| `height` | CSS value or `shortest` | Max height; overflow scrolls. `shortest` matches shortest column. |
| `textAlign` | `start` `end` `center` `justify` `left` `right` | Default alignment for all columns. |

**`col-md` settings:**

| Setting | Values | Effect |
|---|---|---|
| `height` | CSS value | Max height for this column. |
| `flexGrow` | Any positive number | Relative width (no 0.5-step limit). |
| `textAlign` | `start` `end` `center` `justify` `left` `right` | Alignment for this column (overrides group). |

**Example with settings:**

`````markdown
````col
height=shortest
textAlign=center
===
```col-md
flexGrow=1
===
Narrow column.
```

```col-md
flexGrow=2
===
Wide column, twice the width.
```
````
`````

### Rows

Use `===` within a `col` codeblock to start a new row. Forces a settings block — put `===` at the top if no settings needed.

### Border properties

Available on both `col` and `col-md`. Specifying any border property creates a border with defaults for the rest.

| Property | Default | Notes |
|---|---|---|
| `borderColor` | `white` | CSS color |
| `borderStyle` | `solid` | CSS border-style |
| `borderWidth` | `1px` | Bare number → `px` |
| `borderRadius` | `0` | Bare number → `px` |
| `borderPadding` | `0` | Bare number → `px` |

## List syntax

**Not supported in live preview.** Use callout or codeblock syntax instead.

```markdown
- !!!col
  - 1
    # Column 1
    Content here.
  - 2
    # Column 2
    This column is twice as wide (flex-grow 2).
```

Nesting works by putting another `- !!!col` inside a column.

## Plugin CSS variables

```css
--obsidian-columns-gap: 20px;
--obsidian-columns-padding: 0 20px;
--obsidian-columns-min-width: 100px;
--obsidian-columns-def-span: 1;
```

## Plugin settings

| Setting | Effect |
|---|---|
| Minimum width of column | Sets CSS `flex-basis`; columns that can't fit wrap below. |
| Default span | Default flex-grow when not specified. |

## When to use columns

- **Session/run cockpits** — pair same-moment DM jobs so the card scans as a dashboard. Use **codeblock** syntax only, so `[!narration]` keeps callout styling.
- **Side-by-side comparison** (stat blocks, NPC pairs, before/after).
- **Sidebar layout** (main content + quick-reference panel).
- **Dense reference tables** where vertical space matters.
- **Image + text** pairing on owner pages.

### Session/run pairing (codeblock only)

Put the `##` heading inside the `col-md` that holds its body. Reading view is the live surface; source outline may not list fenced headings.

**Pair (same glance):**

| Row | Left | Right | Width |
|---|---|---|---|
| Overview art | First identity/overview image | Second image | equal |
| Dashboard | `## Scene ends when` | `## At a Glance` | Glance `flexGrow=2` |
| Place + rolls | `## Now` | `## Action cards` | Action cards `flexGrow=2` |
| Procedure | `## Procedure` | `## Secondary objective` when both exist | Procedure `flexGrow=3` |
| Clock | `## Threat clock` table | Bloodied / cover-reached / scene dials | Clock `flexGrow=3` |
| Roster | Monster `![[Name#Statblock]]` (two columns max; extra wrap) | Second monster, or omit | equal |

Monster roster rows never exceed two `![[Name#Statblock]]` columns. A third monster starts a new row; a leftover odd monster sits full width. The two-column cap is for monster statblocks only.

**Keep full width:**

- `> [!narration] Initial Narration` and `> [!narration] How the Scene Resolves`
- `## Zones` and `## Be ready for` (wide ruling tables)
- `## How the Scene Resolves` body + options table
- `## Backup` and `## Battlemap`

Do not wrap a session card in `[!col]` callouts. A narration callout inside `col-md` codeblock fences does render, but spoken blocks stay full width so the DM can read them aloud.

Owner pages may use callout `[!col]` when the row has no spoken callout. Session/run surfaces always use codeblock syntax.
