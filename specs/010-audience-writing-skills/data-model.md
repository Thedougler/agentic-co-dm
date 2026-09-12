# Data Model: Audience Writing and Visual Skills

Entities are jobs and authorities. No database.

## Writing job

One act of authoring text.

| Field | Rule |
|---|---|
| Reader | `agent` \| `DM` \| `players`. Unknown reader → `DM`. |
| Vault | `true` if the destination is a wiki vault note; else `false`. |
| Authorities | Every matching row from the stack table. Incomplete until all are applied. |

A job may have more than one reader across passages (mixed document). Classify per passage, then apply vault format to the whole note when Vault is true.

## Visual job

One act of working with pictures.

| Field | Rule |
|---|---|
| Kind | `visual-references` (gather/use existing look) \| `visual-aids` (attach, ground, generate, promote, place) |
| Depicted owner | Named wiki owner when the picture shows one. Missing look → stop; do not invent a face. |
| Moment | Named session moment when the picture is an illustration, not identity. |

Depicting a known owner is both kinds: gather first, then produce or place.

## Reader

Who the text is for.

| Value | Authority |
|---|---|
| Agent | writing-for-agents |
| DM | copy-writer |
| Players | theatre of the mind |

## Wiki vault note

A campaign page in the wiki the DM opens. Format authority: obsidian-markdown. Skill files and repository docs are not wiki vault notes.

## Authority

One of six. They stack; they do not cancel.

| Authority | Owns | Does not own |
|---|---|---|
| writing-for-agents | Prose an agent will follow | DM Work, wiki prose, player-facing text |
| copy-writer | Prose the DM will read | Agent-consumed docs, player-facing passages |
| theatre of the mind | Text that crosses the DM/player boundary | DM procedure, hidden truth, agent instruction |
| obsidian-markdown | Format of wiki vault notes | Non-vault writing |
| visual-references | Gathering and using an owner's existing look | Placing finished art; inventing a face |
| visual-aids | Attaching, grounding, generating, promoting, placing a visual aid | Gathering references in place of visual-references; maps; spoken narration |

## Visual aid

A picture for a named owner or a named session moment. Prep art is Work until the DM accepts. Players see nothing until the DM presents.

| Kind | Rule |
|---|---|
| Reference image | Durable identity for that owner. Not a moment illustration. |
| Illustration | Session-scoped moment. Not identity. |

Pictures of a different owner, site, or moment are not identity for a new thing.

## Work

Mutable prep. Chat proposal first. Wiki write after DM accept, except named ingest stubs.

## Mixed document

One artifact with more than one reader. Typical: wiki note with DM-facing bands and spoken look. Each passage follows its reader. Vault format applies to the note.

## Relationships

- Writing job → zero or more prose authorities + obsidian-markdown if vault
- Visual job → visual-references and/or visual-aids
- Known-owner depiction → visual-references then visual-aids
- Wiki note with a picture → writing authorities for text + visual-aids for placement + obsidian-markdown
- Spoken look on a page with a picture → theatre of the mind still owns the words
- Craft jobs (facts, math, procedure) → not this model
