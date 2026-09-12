# Input fields

```
INPUT[fieldType(arg1(v1,v2), arg2):bindTarget]
```

Type first, arguments in parens (comma-separated), bind target after `:` — see `bind-targets.md` for the addressing scheme.

## The quoting rule

Only **single** quotes support commas or spaces inside an option value; double quotes don't. Escape with `\'`/`\\`.

```
INPUT[select(option(1, 'if you value your time, don\'t watch')):bind_target]   ✓
INPUT[select(option(1, "if you value your time, don't watch")):bind_target]    ✗ splits on the comma
```

## Types, grouped by shape

**Text-like** — `text`, `textArea`, `number`, `editor`
```
INPUT[text(placeholder(Appointment Location), limit(50)):location]
INPUT[number(defaultValue(-1)):modifier]
```

**Choice** — `toggle`, `slider`, `progressBar`, `select`, `multiSelect`, `inlineSelect`, `suggester`, `listSuggester`, `inlineListSuggester`, `imageSuggester`, `imageListSuggester`
```
INPUT[toggle(onValue(done), offValue(in progress)):status]
INPUT[slider(minValue(-10), maxValue(10), stepSize(0.1), addLabels):modifier]
INPUT[select(option(1, 1 Star), option(2, 2 Stars), option(3, 3 Stars)):rating]
INPUT[suggester(optionQuery("vault/campaigns/shattered-sea/npcs")):linked_npc]
```

**Date/time** — `date`, `dateTime`, `datePicker`, `time`
```
INPUT[date:discovered_on]
```

**List** — `list`, `inlineList`
```
INPUT[list:tags_extra]
```

## Key arguments

| Argument | Applies to | Meaning |
|---|---|---|
| `option(value, name?)` | select/multiSelect/inlineSelect/suggester family | one selectable option |
| `defaultValue` | most types | shown when the bound value is `null`/invalid — **display only, never auto-written** |
| `placeholder` | text/textArea | greyed hint text |
| `minValue`/`maxValue`/`stepSize`/`addLabels` | slider/progressBar | range and label display |
| `onValue`/`offValue` | toggle | the actual values written for on/off (default `true`/`false`) |
| `class` | any | CSS class — see `button-actions.md`'s CSS note, same child-selector rule applies |
| `limit` | text/textArea/list | max length |
| `allowOther` | suggester family | free text beyond the declared options |
| `useLinks` | suggester family | `true`/`partial`/`false` — controls `[[note]]` vs bare-name storage |
| `optionQuery` | suggester family | a Dataview data-source string feeding the option list — not a full query |
| `showcase` | any | docs/demo only — wraps the field in a card showing its own declaration |

## What a fresh field does NOT do

An `INPUT` never auto-creates its bound property and never writes until a person interacts with it. `INPUT[toggle:completed]` against a note with no `completed:` frontmatter key shows a default state but writes nothing until clicked — `defaultValue`/`placeholder` are display-only, never persisted automatically.
