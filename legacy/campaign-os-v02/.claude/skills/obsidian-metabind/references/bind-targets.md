# Bind targets

Every `INPUT`'s `:bindTarget` and every `VIEW`'s `{...}`/`:writeTarget` addresses a value with the same scheme:

```
storageType^storagePath#property
```

All three parts are optional and default to `frontmatter` / the containing file — so `property`, `frontmatter^ThisNote#property`, and (written from inside "Test Note") `frontmatter^Test Note#property` all address the same value.

## Storage types

| Type | Meaning | `storagePath` |
|---|---|---|
| `frontmatter` (default) | A YAML frontmatter field | optional, defaults to current file |
| `memory` | In-memory, ephemeral, scoped per file path — lost when unused a while or on Obsidian restart | optional |
| `globalMemory` | In-memory, ephemeral, shared across **all** notes — lost on restart | not allowed |
| `scope` | Extends another (local) bind target rather than opening a new storage path | — |

Use `memory`/`globalMemory` for UI-only state that shouldn't pollute frontmatter — a per-session combat toggle, a dashboard filter — and `frontmatter` for anything that should persist and show up in git history.

## Cross-note targets

```
INPUT[toggle:Task A#completed]
```

If the short name is ambiguous across the vault, use the full vault-relative path:

```
INPUT[toggle:path/to/Task A#completed]
```

## The spaces-in-property gotcha

A property name with spaces or special characters must use the JS bracket form — the bare dotted form silently fails to parse, with no error:

```
INPUT[toggle:["is completed"]]     ✓ works
INPUT[toggle:is completed]         ✗ silently fails
```

Nested properties: `this.is.nested` ≡ `this["is"].nested`.

## Static-only constraint

Bind targets are static strings. You cannot make "which property this points to" itself data-driven from plain Meta Bind syntax — that requires the JS Engine plugin's dynamic-bind-target feature, which is **not installed in this vault** (`enableJs: false`). Write the literal target; if a dynamic target is genuinely needed, flag the JS Engine install to the user before proposing a workaround.

## Worked examples, one per storage type

```
INPUT[number:hp_current]                    ← frontmatter (default), current file
INPUT[toggle:memory^combat-ui#dm-visible]    ← memory, ephemeral per file
VIEW[{globalMemory^#active-encounter}][text] ← globalMemory, vault-wide, no storagePath
INPUT[toggle:scope^#stunned]                 ← scope, extends a local target
```
