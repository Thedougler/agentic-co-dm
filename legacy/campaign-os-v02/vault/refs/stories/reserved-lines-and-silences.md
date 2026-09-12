---
type: guide
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: "2026-08-08"
tags: [craft]
summary: "Reserved lines (_Lines.md) for placing dialogue later in the draft, and the Deliberate Silences marking convention that exempts intentionally-unresolved content from continuity/QC findings and the InventedMystery lint rule."
tier: supporting
source: "raw/2026-07/stories-playbook-source.md"
source_url: "https://github.com/gsarig/ai-playbooks/tree/main/playbooks/stories"
campaigns: [Shattered Sea]
uid: 43b8800e-6069-4744-a21f-469822ce97b6
---

# Stories Playbook: Reserved Lines and Deliberate Silences

## Reserved lines (_Lines.md)

Lines you'll use at some point in the draft. Speaker and approximate placement noted where known. Lines are not forced into the draft. The workflow finds where they land naturally.

Frontmatter:

```yaml
title: Reserved Lines — {{story title}}
tags: [lines]
```

Structure: one section per character or thematic group (`## {{Character Name}}`), with each line block as:

```text
**"The line goes here."**
Context note: when this line might land, what it signals, why it matters. Leave blank if unknown.
```

To add a new line, duplicate the block. To mark a line as used, add `~~` strikethrough or move it to a Used section.

## Lore (_Lore.md)

Detailed worldbuilding reference, populated over time as the story develops. _Index.md holds a summary of world rules. The rich detail lives here. Claude reads this file in full when the author references the story by name.

Frontmatter:

```yaml
title: Lore — {{story title}}
tags: [lore, worldbuilding]
```

Sections: **world rules** (established, non-negotiable facts about how the world works. Claude will not contradict them); **cosmology / premise** (the central conceit, mechanism, or speculative premise, including what is deliberately left unexplained and why); **factions / institutions** (groups, organisations, power structures shaping the world); **history & mythology** (background events the reader may never see but that shape character and world); **objects & technology** (key objects, technologies, or systems with their own rules); **deliberate silences** — the `## Deliberate Silences` marking convention below.

## Marking a deliberate silence

Any page — not only `/_Lore.md` — can mark something as intentionally unresolved. Two separate mechanisms read the mark, one per checker type, and both are needed together: the heading exempts the passage from the two LLM checkers below; the comment pair exempts it from the deterministic Vale rule. Neither substitutes for the other.

### `## Deliberate Silences` heading — exempts `content-quality-checker` and `continuity-checker`

Add a level-2 `## Deliberate Silences` heading to the page, with each intentionally-unresolved item as its own bullet naming the specific unresolved thing:

```markdown
## Deliberate Silences

- Why the tide gate refuses to open at the new moon: left open on purpose, a draw for a later arc.
- What the Voice in the cistern actually is: never confirmed in-text.
```

`content-quality-checker` treats an item listed here as intentionally unexplained, never a finding; `continuity-checker` treats it as intentional ambiguity, never a `CONFLICT:` block (both agents cite this file for that rule). The boundary is exact: **only a claim named as its own bullet under this heading is exempt.** A heading with no matching bullet, an unrelated bullet, or the heading's mere presence elsewhere on the page does not blanket-exempt the rest of the document — an unresolved claim not individually listed here is a real gap or conflict, and both checkers must still report it.

### Comment pair — exempts the `CampaignOS.InventedMystery` Vale rule

`CampaignOS.InventedMystery` (`docs/vale-styles/CampaignOS/InventedMystery.yml`) flags invented-mystery phrasing ("for reasons unknown", "remains a mystery", "no one knows why", …) wherever it appears in prose. Vale's `existence` check has no whole-document conditional, so it cannot read the `## Deliberate Silences` heading above — a page adopting that heading still needs the passage itself wrapped in this exact comment pair:

```markdown
<!-- vale CampaignOS.InventedMystery = NO -->
... the passage that intentionally reads as unresolved ...
<!-- vale CampaignOS.InventedMystery = YES -->
```

`= NO` turns the rule off from that line forward; `= YES` turns it back on. Both markers must be present — an unclosed `= NO` silently exempts the rest of the file.

See also: [[story-templates]], [[global-rules]].
