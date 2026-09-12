# Defuddle — fetching one URL

Use the Defuddle CLI instead of `WebFetch` whenever a research round hands
over a URL to read — documentation, an article, a blog post, any standard
web page — to strip navigation/ads/clutter and save tokens. Not for a URL
ending in `.md` — that's already markdown; use `WebFetch` directly.

If not installed: `npm install -g defuddle`.

## Usage

Always use `--md` for markdown output:

```bash
defuddle parse <url> --md
```

Save to file:

```bash
defuddle parse <url> --md -o content.md
```

Extract specific metadata:

```bash
defuddle parse <url> -p title
defuddle parse <url> -p description
defuddle parse <url> -p domain
```

## Output formats

| Flag | Format |
|------|--------|
| `--md` | Markdown (default choice) |
| `--json` | JSON with both HTML and markdown |
| (none) | HTML |
| `-p <name>` | Specific metadata property |
