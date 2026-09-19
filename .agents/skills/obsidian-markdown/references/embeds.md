# Embeds & image wikilinks

Vault media lives under `attachments/` (see [[attachments/00 Attachments]]). Obsidian app setting: `attachmentFolderPath: attachments`.

## Images (required pattern)

Embed (shows inline — usual choice in notes):

```markdown
![[attachments/shattered-sea/map.png]]
![[attachments/shattered-sea/map.png|400]]
![[attachments/shattered-sea/map.png|640x480]]
```

Wikilink (clickable asset, no inline render):

```markdown
[[attachments/shattered-sea/map.png]]
[[attachments/shattered-sea/map.png|Campaign map]]
```

Campaign subfolders: `attachments/<campaign-slug>/…`. Shared assets may sit at `attachments/` root.

Agents: always write the `attachments/…` path (do not rely on bare filenames).

## Other embeds

```markdown
![[Note Name]]
![[Note Name#Heading]]
![[Note Name#^block-id]]
![[attachments/handout.pdf#page=3]]
![[attachments/clip.mp3]]
```

External images (rare): `![Alt|300](https://…)` — prefer vault files when the asset is campaign canon.

List embed: put `^list-id` on its own line after the list, then `![[Note#^list-id]]`.
