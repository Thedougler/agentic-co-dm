# Pixels

When filling `[!narration]`, a portrait, a first look, or scene-setting, **see**
related art before drafting. Filename, alt text, and embed markup are labels.
**Pixels** are the picture.

Read this file when the owning parent, run card, roster note, or user message
points at `attachments/` art, or the user attached a picture of the subject.
Skip hit lines, recaps, dialogue turns, and jobs with no related images. Missing
art is not a stop: write from parent prose.

## Collect

Take only images that depict the current subjects:

| Kind | Use as |
|---|---|
| Owner Art / portrait / identity image | Cold portrait and situated look of that owner |
| Run-card identity embed | Spoken look of that roster body |
| Session illustration of **this** moment | Situated block for that beat only |
| User-attached picture of the subject | The offered look |
| Foundry token | Color, gear, overhead silhouette when no portrait exists |
| Layout / room plate | Spatial first look of that space |
| Battlemap of **this** site | Situated place geometry |

Leave unrelated campaign portraits, other-session art, and character sheets.
One image per owner is enough when near-duplicates exist; prefer portrait over
banner over token.

Distinct things need distinct pictures. An image or battlemap of a different
owner, nearby place, earlier scene, or similar-looking subject is vibe reference
only. It can suggest palette, density, weather, or genre, but it must not become
the described identity or the embedded asset for the new thing. If no exact
depiction exists, write from parent prose and route a new visual-aid request.

## Open

Resolve `![[attachments/…]]` / `[[attachments/…]]` to the vault file. Open each
file with the host vision tool so the picture is in context (Grok: `read_file`
on the image path; Claude Code: `Read` on the image path). Reading the markdown
embed is not seeing.

If the file is missing or will not render, mark it unavailable and continue from
parent prose. Do not invent pixels from the filename.

Completion: every collected related image is seen or marked unavailable.

## Extract

Add pixel-supported facts to the fragmentary inventory in
[boundary.md](boundary.md). Provenance: `pixels:<path>`.

Take silhouette, scale vs nearby objects, color, material, wear, parts, clothes,
gear, and a sensory cue the picture supports (wet sheen, dust, blood).

Keep the mode gate. Cold portrait takes durable identity (body, clothes, marks).
A fight pose or market stall in the art is illustration, not permission to stage
that scene. Situated look may use current pose and setting when they match table
state. A painted secret, hidden item, or unearned name still needs an access
channel.

## Reconcile

Owner appearance prose is the identity source of truth (`visual-aids`). Pixels
fill missing drawable nouns.

- Parent silent, pixels show a cloak color: add the color.
- Parent and pixels agree: keep the more specific drawable noun.
- Parent and pixels conflict: keep the parent; flag the mismatch outside
  `[!narration]`.
- Illustration shows a completed attack: keep that out of a cold portrait.

Do not mint, edit, or promote art. That is `visual-aids`.

## Weave

Fold pixel facts onto the body in flowing spoken prose. The table hears the
look, not a description of a file.

**Weak:** A deer-stalker of Aruhe stands in the trees.

**Strong:** A shaggy deer taller than a man leans on pale blood-smeared arms
that end in long claws, branching antlers filling the space above its head.

Completion: a player hearing the block could sketch the same silhouette, colors,
and marks the DM sees in the related art.
