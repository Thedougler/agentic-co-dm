# Columns (obsidian-columns plugin)

Plugin: [obsidian-columns](https://github.com/tnichols217/obsidian-columns). The vault uses the **codeblock** syntax only, so `[!narration]` inside a column stays a real callout.

## Syntax

Parent codeblocks need more backticks than children. Everything above `===` is settings; `flexGrow` sets relative width. Put a `##` heading inside the `col-md` that holds its body so the title stays with it in Reading view.

`````markdown
````col
```col-md
flexGrow=2
===
## At a Glance

Lead sentence.

- **Label.** Fact.
```

```col-md
flexGrow=1
===
> [!narration] Name
> Player-safe look.
```
````
`````

Other settings: `height` (CSS value; overflow scrolls), `textAlign`, and border properties (`borderColor`, `borderStyle`, `borderWidth`, `borderRadius`, `borderPadding`). Columns narrower than the plugin's minimum width wrap below each other, so the left column is what a phone reader sees first.

## The two patterns

Columns work like a published adventure's sidebar: they sit two short, same-moment blocks side by side. The vault uses exactly two patterns.

| Pattern | Where | Left | Right |
|---|---|---|---|
| **Header row** | Every owner page, directly under the H1 and overview art | `## At a Glance`, `flexGrow=2` | `> [!narration] Name`, `flexGrow=1` |
| **Beat pair** | Beats, encounters, session plans | One short block (`Situation`, `Stage`, `Pressure`) | Its same-moment partner (`Actors`, `Pressure`, `Spotlight`), equal width |

Everything else stays full width: statblocks, wide tables (Checks, Handles, Outcomes, Beat Map, Gazetteer), and beat openings (`> [!narration] Opening`) the DM reads aloud.

A run-card roster may pair two `![[Name#Statblock]]` embeds in one row; a third monster starts a new row.
