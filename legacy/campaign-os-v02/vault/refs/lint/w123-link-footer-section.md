---
type: agent-guidance
status: pending
publish: false
aliases: []
created: "2026-08-04"
updated: "2026-08-04"
tags: [craft]
summary: "W123 link-footer sections: a See Also/Related/Further Reading heading whose body is nothing but a list of wikilinks, and where each link belongs instead."
uid: ce40d10f-e552-444c-b2b8-319052e4ca57
---

# W123 — Link-footer sections

Fires on a trailing "See Also"/"Related"/"Sources"/"Further
Reading"-shaped heading (full list: `LINK_FOOTER_HEADINGS`,
`wiki.toml` `[thresholds]`). Every link earns a
place in the page's own body prose, or it doesn't merit being linked at
all; a footer is neither (DM directive 2026-08-04).

The heading is the violation, whatever sits under it. Rewriting the list
as a citation sentence ("This page draws on X, Y, and Z") keeps the same
links in the same place and does not resolve the finding (DM directive
2026-08-09). No template scaffolds one of these headings.

## Fix — W123

No autofix — which links move into prose and which get dropped is
judgment. For each linked page in the footer:

- Find (or write) the sentence in the page's body that already talks
  about that thing, and put the link there.
- If no sentence needs it, drop the link — it didn't merit linking.
- Delete the footer heading once every link is moved or dropped.
