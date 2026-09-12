# DRY Content Patterns

When writing or editing wiki pages, choose the most dynamic content pattern to avoid
duplication. See CLAUDE.md § DRY & dynamic content for the full governance rules.

### When to use each pattern

| Pattern | Syntax | Use when |
|---|---|---|
| **Base embed** | `![[tracker.base]]` or `![[tracker.base#View]]` | Displaying a list, roster, or table of entities. Bases query frontmatter live — the view updates automatically when entity pages change. |
| **Section embed** | `![[Entity-Name#Section]]` | Displaying a specific section from another page inline. Avoids copy-pasting content that should live in one place. |
| **Full-page embed** | `![[Entity-Name]]` | Embedding an entire page inline (rare — usually a section embed is more precise). |
| **Wikilink** | `[[Entity-Name]]` | Cross-referencing where the reader clicks through to the full page. |
| **Canvas embed** | `![[diagram.canvas]]` | Embedding a visual layout — mind map, flowchart, or relationship diagram. Use for synthesis pages where spatial relationships add meaning. See `obsidian-json-canvas` skill. |
| **Static text** | Plain markdown | Content unique to this page that is not derivable from any entity's frontmatter or existing sections. |

### Anti-patterns to avoid

- **Static tables listing entity status/active problems** — replace with base embeds
- **Paragraph-length descriptions of Entity B on Entity A's page** — use a section embed or compress to one sentence + wikilink
- **Hand-maintained rosters or inventories** — replace with base embeds that query the entity directory
- **"Last Updated" dates on overview pages** — file metadata handles this; remove manual dates
