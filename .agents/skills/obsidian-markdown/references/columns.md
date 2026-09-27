# Columns (obsidian-columns plugin)

Plugin: [obsidian-columns](https://github.com/tnichols217/obsidian-columns). The vault uses the **codeblock** syntax only, so `[!narration]` inside a column stays a real callout.

## Syntax

Parent codeblocks need more backticks than children. Everything above `===` is settings; `flexGrow` sets relative width. Put a `##` heading inside the `col-md` that holds its body so the title stays with it in Reading view.

`````markdown
````col
```col-md
flexGrow=1
===
## Situation

- **Where.** Fact.
```

```col-md
flexGrow=1
===
## Actors

- **Name.** Fact.
```
````
`````

Other settings: `height` (CSS value; overflow scrolls), `textAlign`, and border properties (`borderColor`, `borderStyle`, `borderWidth`, `borderRadius`, `borderPadding`). Columns narrower than the plugin's minimum width wrap below each other, so the left column is what a phone reader sees first.

## The one pattern

Columns work like a published adventure's sidebar: they sit two short, same-moment DM blocks side by side.

| Pattern | Where | Left | Right |
|---|---|---|---|
| **Beat pair** | Beats, encounters, session plans | One short block (`Situation`, `Stage`, `Pressure`) | Its same-moment partner (`Actors`, `Pressure`, `Spotlight`), equal width |

Everything else stays full width: every `[!narration]` callout (owner-page looks, beat openings, first looks, closing images), statblocks, and wide tables (Checks, Handles, Outcomes, Beat Map, Gazetteer). A narration block is words the DM reads aloud, so it gets the page's full width and its own place in the reading order.

A run-card roster may pair two `![[Name#Statblock]]` embeds in one row; a third monster starts a new row.
