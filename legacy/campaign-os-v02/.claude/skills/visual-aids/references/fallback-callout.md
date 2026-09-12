# Fallback (no generation available)

If generation fails (no API key, API error, insufficient credits, `use-openrouter` not
installed), write the full prompt as a `> [!visual-aid]` callout where the image would go:

```markdown
> [!visual-aid] Scene: Kyzil Reunion
> [full prompt incorporating every art-style.md directive]
```

A capable agent or the DM replaces this callout with an embed later. Never skip the callout and
leave a blank gap — a missing image with no record of the intended prompt is unrecoverable.
(`VISUAL-AID` is registered in `.obsidian-linter.jsonc`'s callout allowList; the `callouts`
skill's type table routes the type here — this skill owns its contract.)
