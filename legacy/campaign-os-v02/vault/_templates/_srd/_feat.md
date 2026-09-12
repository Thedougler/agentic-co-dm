---
type: feat
status: srd              # draft | pending | canon | srd | retired — sourced feat (SRD) start at srd; homebrew starts at draft or canon
publish: false
title: ""                      # OPTIONAL — display title if it differs from the H1 heading; absent ⇒ the H1 is the title (llm-wiki skill)
aliases: []
summary: "5e feat text for <Feat Name>."
owner_skill: ".claude/skills/draft-content/references/feat.md"   # OPTIONAL — the guide or skill that owns this page's quality
created: "{date}"
updated: "{date}"
tags: []
tier: supporting        # OPTIONAL — core | supporting | peripheral; absent ⇒ supporting (llm-wiki skill)
source: ""       # OPTIONAL — only for a page migrated from an raw/ source (srd) or its earlier draft (homebrew)
source_url: ""           # OPTIONAL — canonical/licensed source reference (SRD document, sourcebook + page citation)
campaigns: []            # OPTIONAL — this page's campaign(s), if this repo runs more than one
uid: 55c5e527-6939-497c-a324-bd07b0ac846b
---

# <Feat Name>

*<Origin | General | Fighting Style | Epic Boon> Feat<, Prerequisite: <prerequisite>, if any>*

<Either a single unlabeled benefit paragraph for a one-effect feat, or one
or more bolded benefit blocks for a multi-effect feat:>

**<Benefit Name>.** <Benefit text, transcribed verbatim from the SRD
source. Any named condition, skill, spell, class, or other page gets an
inline `[[slug|Display Name]]` wikilink at first mention.>

**Repeatable.** OPTIONAL — only when the SRD source marks this feat
repeatable; delete this line otherwise.
