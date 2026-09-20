---
description: Require tag-taxonomy before editing wiki frontmatter tags
condition: '(?m)^tags:\s*.*$'
scope:
  - 'tool:edit(wiki/**/*.md)'
  - 'tool:write(wiki/**/*.md)'
interruptMode: always
---

Before editing a `tags:` field in wiki Markdown frontmatter, read `skill://tag-taxonomy`. Follow that skill and consult the canonical taxonomy before continuing with the edit.
