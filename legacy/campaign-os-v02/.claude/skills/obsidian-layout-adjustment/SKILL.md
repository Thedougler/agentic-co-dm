---
name: obsidian-layout-adjustment
description: Visual styling for a Campaign OS Obsidian vault (vault/.obsidian/ present) — CSS snippets for tabs, sidebars, note surfaces, properties, backlinks, graph panes, file explorer, icons, links, graph.json colorGroups. Use when the DM asks to restyle Obsidian, a CSS change did nothing/looks wrong, or "color my graph"/"color by tag".
---

# Obsidian Layout Adjustment

Changes how Obsidian looks via CSS snippets, translating the DM's plain-language description of
what they see into the stable Obsidian layer/backend object it maps to, editing active snippets
safely, and proving the change with a screenshot. Not a general CSS workflow or a fixed-theme
generator — Obsidian is always the same kind of environment (app frame, tab headers, side docks,
view headers, pane shells, note surface, properties, file explorer, backlinks, graph, rendered
markdown, status bar); the vault, theme, snippets, and taste direction change, but the canvas
stays Obsidian.

## Normal output mode

Make live styling work faster, not turn every small request into a report:

1. Say the phrase→layer mapping only when it prevents ambiguity — one sentence is usually enough.
2. Act: inspect active snippets, checkpoint, patch, format, reload, screenshot.
3. Report concisely — changed files, checkpoint, screenshot status.

Write a long workflow report only when the DM asks for a plan/audit/review/explanation, when
running evals or building this skill, when refactoring without visual changes, or when the
request is ambiguous enough that acting first would be risky.

## Use the reference

Read `.claude/skills/obsidian-layout-adjustment/references/workflow-reference.md` when: the DM
names a visible object that could map to more than one Obsidian layer; a screenshot shows
"nothing changed," "still wrapped," "not lifted," or an unreadable icon; you're refactoring
active snippets without changing the accepted look; or you need the full surface map, change-type
map, or failure-pattern list. It is Obsidian-specific — read it before treating the UI as an
unknown web page.

## Graph view coloring

A separate procedure from CSS snippets — rewrites `vault/.obsidian/graph.json`'s
`colorGroups` directly, backing it up first, never touching CSS or page
content. Read `.claude/skills/obsidian-layout-adjustment/references/graph-colors.md`
for the mode table (by-tag/by-category/by-visibility/custom/combined), the
color palette, and the merge-without-clobbering procedure.

## Operating loop

1. Read `vault/.obsidian/appearance.json`; treat `enabledCssSnippets` as the active styling
   source of truth. Read active snippets before archives, backups, or old experiments.
2. Translate the DM's phrase into an Obsidian object and its owning layer (see reference).
3. Classify the change type: color, readability, lift, shape, structure, density,
   simplification, workflow, or refactor.
4. Save a named checkpoint before subjective edits: copy active snippets to
   `vault/.obsidian/snippet-archive/`, never into `vault/.obsidian/snippets`, so the picker stays clean.
5. Re-read the exact current block, then edit one owning layer (stage, shell, header, wrapper,
   or child) — formatting reshapes the file, so a patch from a remembered shape misses.
6. Format CSS; reload/focus Obsidian; screenshot the exact affected area.
7. Use the screenshot and the DM's correction as evidence. If it fails, inspect ownership or
   restore — don't keep piling CSS onto the same wrong target.
8. Refactor only after the DM accepts the visual state (see § Refactor rule).

Ask for explicit confirmation before: switching themes, disabling snippets/plugins,
hiding/moving properties as a workflow change, changing global typography/density substantially,
deleting archived experiments, or touching files outside `vault/.obsidian/snippets`/Obsidian settings.

## Screenshot gate

CSS validity is not visual success — the screenshot is product truth. For every meaningful pass:
checkpoint, patch, format, reload/focus, screenshot the affected area, compare to the complaint.
Verify the verifier — confirm Obsidian is actually frontmost before trusting a capture; for a
tiny issue, capture just that region (`screencapture -R<x,y,w,h> out.png`). If the screenshot
disproves the fix, keep working, restore, or say it failed — never close as if formatting proved
success.

## Refactor rule

Do not refactor during taste exploration. Once the DM likes the look: save a baseline checkpoint,
add/update a file map and section headers, preserve selector order unless changing it
intentionally, format, diff-check for accidental visual changes, screenshot, and archive
inactive iterations outside `vault/.obsidian/snippets`.

## Closing report

Keep it short: active snippet files changed, checkpoint paths saved, what phrase mapped to which
Obsidian layer, what was screenshot-verified, and anything not verified or intentionally
deferred. Don't re-explain the whole workflow after every small pass — it should already be
visible in the actions taken.
