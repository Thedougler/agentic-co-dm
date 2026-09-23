# Pixels

Related art is a fact source. A filename, alt text, or embed line is a label;
the **pixels** are the picture. Run this file for every block that shows how
something looks (`SKILL.md` step 3), before drafting. Art is supporting
evidence: when none exists, write from the parent prose.

## 1. Search

List every subject the block will show: the scene or site itself, and each
named person, creature, place, item, and vehicle in it. For each one, collect
images from all three places:

1. **Linked.** Every image embedded or linked on the parent page and on each
   owner page: the image under the title, `## Art`, `## Visual reference`,
   statblock and section embeds, and any `![[…]]` or `[[…]]` that ends in an
   image extension. A transcluded section (`![[marsh-strider#Statblock]]`)
   brings its page's images with it.
2. **Related by name.** Images in `wiki/attachments/`, nested folders
   included, whose filename contains the subject's distinctive word. Many
   files break the `{slug}-{role}` grammar or carry a region prefix
   (`aruhe-marsh-strider-of-aruhe.jpg`), so search the word, not the exact
   slug: `find wiki/attachments -iname '*strider*'`. For a session beat, also
   search its number (`session-14-03-*`); those are illustrations and maps of
   that exact scene.
3. **Offered.** Images the user attached or named in the request.

Keep a match only when it depicts this subject or this moment. A name-alike of
another owner (`young-marsh-strider` when writing the adult) stays out.

Done when each subject has a search note listing the images kept, or "none
found" with the words searched.

## 2. Choose

Match each kept image to the job its role can do. Roles come from the filename
suffix (`wiki/attachments/README.md`); an image with no suffix gets its role
from what you see when you open it.

| Role | Gives the narration |
|---|---|
| `reference` sheet, `portrait` | Identity: body, face, colors, marks, clothes, gear |
| `overview`, owner art with no suffix | Identity of the subject, and for a place, its shape, ground, light, and routes |
| Session illustration (`session-<NN>-<BB>-*`) | This beat only: where things sit, poses, light, weather |
| `battlemap` | Geometry only: routes, cover, distances, compass (top is north) |
| `teaser`, `banner` | Mood, light, and palette; never identity or layout |
| `handout` | The prop exactly as the players will hold it |
| `token` | Color and gear, only when nothing better exists |

With near-duplicates, open the strongest for each job: reference sheet, then
portrait, then overview, then token.

**Distinct things need distinct pictures.** Art of a different owner, a
nearby place, an earlier scene, or another form or state of this subject (a
blight form, a juvenile, a wounded variant) describes only that thing. It may
suggest palette or weather; it never becomes this subject's look.

## 3. Open

Resolve every embed to a file. Obsidian resolves a bare name
(`![[marsh-strider-portrait.jpg]]`) anywhere in the vault:
`find wiki -name 'marsh-strider-portrait.jpg'`. A path embed
(`![[attachments/shattered-sea/…]]`) is relative to `wiki/`.

Open each file with the host vision tool so the picture is in context (Claude
Code: `Read` on the image path; Grok: `read_file`). Reading the embed line is
not seeing. A missing or unreadable file is marked unavailable; write from
prose and invent nothing from its filename.

Done when every kept image is opened or marked unavailable.

## 4. Analyze

Look at the whole picture, then region by region, and write what it shows as
fragments on the fact list, each sourced `pixels:<path>`:

- **Identity:** silhouette and body plan, size against something in frame,
  colors and patterns, materials and textures, wear and damage, marks and
  scars, clothes and gear.
- **Space:** what is near and far, left and right; ground, water, and
  growth; where each thing sits relative to the others (these become
  **handles**); the light source and its direction, time of day, weather.
- **Sense cues the picture supports:** wet sheen, steam, smoke, dust, blood,
  spray, wind in the grass.
- **The eye's first stop:** the thing the picture makes you look at first.
  It is the leading candidate for the focus (`SKILL.md` step 5).

Text lettered onto a reference sheet (labels, callouts, notes) is prose, not
pixels; treat it like the owner page.

Done when a player hearing your facts could sketch the same silhouette,
colors, marks, and layout the art shows.

## 5. Reconcile

Owner appearance prose is the identity source of truth (`visual-aids`); pixels
fill in every drawable noun it leaves out.

- Prose silent, pixels show it (a cloak color, a scar): add it.
- Prose and pixels agree: keep the more specific drawable noun.
- Prose and pixels conflict: keep the prose; flag the mismatch in the report.
- Owner art (reference, portrait, overview, token) gives **durable identity**
  only: body, face, coloring, marks, clothes, gear. Its pose, gesture,
  expression, action, and backdrop are the illustrator's moment and stay out
  of every block, portrait and situated alike; the beat decides what the
  subject is doing.
- A session illustration of this exact beat may also give poses and
  placement, when they match the table state.
- Painted secrets, hidden items, and unearned names still need a way to reach
  the players ([boundary.md](boundary.md)).

Placing, minting, or editing art belongs to `visual-aids`.

## 6. Weave

The durable facts the pixels add beyond the prose are why you opened the
art. Carry the ones that set the subject apart into the block, folded onto the
body that owns them, in spoken prose. The table hears the thing, never a
description of a picture ("in the image", "the art shows").

**Weak:** A deer-stalker of Aruhe stands in the trees.

**Strong:** A shaggy deer taller than a man leans on pale blood-smeared arms
that end in long claws, branching antlers filling the space above its head.

## 7. Report

Return one art note with the block, outside the narration and off the wiki
page:

```
Art seen: wiki/attachments/marsh-strider-reference.jpg (reference; gray oily feathers, red crest quills); wiki/attachments/session-14-03-strider-shallows.jpg (illustration; reed circles, low sun from the left)
Woven: gray oily feathers, red crest quills
Art unavailable: none
Mismatches: none
```

or `Art: none found (searched attachments for "strider")`.
