// Shared scope/walk/subprocess logic for prose-scoped lint tooling
// (Vale producers, frontmatter schema). Scope: every wiki page
// under vault/ (nested pcs/episodes/campaign material included) plus
// _templates/, minus agent-internal .claude/ dirs, vault/refs/table-*
// (generator rows, not prose), and raw/
// (retired, frozen material) and inbox/ (unprocessed intake). No other
// carve-outs: every live page gets linted, including drafts, interviews,
// transcripts, and voice scripts — a directory exemption for live content
// is exactly the kind of permanent unlinted backlog this repo doesn't want.
import { readdirSync, lstatSync, statSync, readFileSync, writeFileSync, mkdirSync, rmSync, openSync, closeSync, existsSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import os from 'node:os';
import { spawnSync } from 'node:child_process';
import { randomUUID } from 'node:crypto';
import fg from 'fast-glob';

// CAMPAIGN_ROOT wins when set (env_local.sh's documented precedence — an
// explicit override sandboxes the ratchet/findings tooling to a fixture
// root in tests), else the real repo root auto-detected from this file.
export const REPO_ROOT = process.env.CAMPAIGN_ROOT
  ? path.resolve(process.env.CAMPAIGN_ROOT)
  : path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
export const INCLUDE_ROOTS = [
  'vault',
  '_templates',
  '.claude/skills',
  '.claude/agents',
  '.claude/rules',
  '.claude/commands',
  'docs/guardrails',
  'docs/.claude/skills',
  'utils/scripts/.claude/skills',
  'utils/site/.claude/skills',
];

// raw/ is retired, frozen material kept for reference only. No producer
// lints it — not on a sweep, not when named explicitly. inbox/ is
// unprocessed intake — not yet canon, never linted either.
export function isArchived(relPath) {
  return relPath === 'raw' || relPath.startsWith('raw/');
}

export function isInbox(relPath) {
  return relPath === 'inbox' || relPath.startsWith('inbox/');
}

// withFrontmatterGuard/withLineChunking ephemeral sibling copies (see
// .gitignore's matching *.vale-fm-*.md / *.vale-chunk-*.md entries and
// withFrontmatterGuard's doc comment below) — never a real scan target. An
// orphan surviving a killed process (SIGKILL/OOM skips the `finally`
// cleanup) would otherwise get walked by the very next collectScope() /
// expandTargets() call, get treated as a genuine wiki page, and — if its
// own front matter still trips the wikilink/callout transform — spawn a
// SECOND, nested temp copy under its own already-ephemeral name. Confirmed
// in the wild: a killed batch left
// `perrin-black-jaw-stats.vale-fm-<pid>-<uuid>.md` orphaned; a later sweep
// re-scanned it as content and wrote
// `...vale-fm-<pid>-<uuid>.vale-fm-<pid2>-<uuid2>.md` beside it. Excluding
// the pattern here stops both the misclassification and the compounding.
const VALE_TEMP_RE = /\.vale-(?:fm|chunk)-\d+-/;
// A line chunk keeps the original's exact basename and carries the marker on
// its enclosing ephemeral directory instead, so the path — not the basename
// alone — is what identifies it.
const VALE_TEMP_DIR_RE = /(?:^|[\\/])\.vale-(?:fm|chunk)-\d+-[^\\/]*[\\/]/;

export function isValeTempFile(relOrAbsPath) {
  return VALE_TEMP_RE.test(path.basename(relOrAbsPath))
    || VALE_TEMP_DIR_RE.test(relOrAbsPath);
}

export function isExcluded(relPath) {
  if (isArchived(relPath)) return true;
  if (isInbox(relPath)) return true;
  if (isValeTempFile(relPath)) return true;
  if (relPath.startsWith('vault/refs/table-')) return true;
  if (relPath === 'docs/tags.md') return true;
  // vault/_templates and vault/_assets are symlinks to the repo-root
  // directories of the same name — they exist so Obsidian, whose vault root
  // is vault/, can reach templates and attachments. _templates is already
  // its own include root, so walking them here would lint every template
  // twice and fire W57 on every duplicated basename.
  if (relPath.startsWith('vault/_')) return true;
  // Obsidian's own config, inside the vault root but not wiki content.
  if (relPath.startsWith('vault/.obsidian/')) return true;
  return false;
}

function walk(dir, out) {
  let entries;
  try {
    entries = readdirSync(dir);
  } catch {
    return;
  }
  for (const entry of entries) {
    const full = path.join(dir, entry);
    // vault/_templates and vault/_assets are symlinks to the repo-root dirs of
    // the same name, so Obsidian (vault root = vault/) can reach templates and
    // attachments. Walking them would scan every template a second time.
    if (lstatSync(full).isSymbolicLink()) continue;
    const stat = statSync(full);
    if (stat.isDirectory()) {
      // node_modules: a skill's vendored scripts dir (.claude/skills/*/scripts/
      // node_modules) sits inside INCLUDE_ROOTS — its packaged .md files are
      // not this repo's prose.
      if (entry.startsWith('.') || entry === 'node_modules') continue;
      walk(full, out);
    } else if (entry.endsWith('.md')) {
      out.push(full);
    }
  }
}

export function collectScope() {
  const files = [];
  for (const root of INCLUDE_ROOTS) walk(path.join(REPO_ROOT, root), files);
  // CLAUDE.md files (root + every nested one) are agent instruction prose
  // scattered outside INCLUDE_ROOTS' own directories (repo root, .claude/,
  // docs/, utils/) — a glob, not a walkable root.
  for (const rel of fg.sync('**/CLAUDE.md', { cwd: REPO_ROOT, dot: true, ignore: ['**/node_modules/**', '**/.git/**'] })) {
    files.push(path.join(REPO_ROOT, rel));
  }
  const seen = new Set();
  const rels = [];
  for (const abs of files) {
    const rel = path.relative(REPO_ROOT, abs);
    if (seen.has(rel) || isExcluded(rel)) continue;
    seen.add(rel);
    rels.push(rel);
  }
  return rels;
}

// Line index of a YAML frontmatter block's closing `---`, or -1 when
// `lines` has none. Shared by stripFrontmatter and the wikilink-transform
// guard below — both need the same boundary, computed the same way.
function frontmatterEnd(lines) {
  if (lines[0]?.trim() !== '---') return -1;
  for (let i = 1; i < lines.length; i++) {
    if (lines[i].trim() === '---') return i;
  }
  return -1;
}

// YAML frontmatter is data syntax, not prose — e.g. `aliases: ["Perrin"]`'s
// straight quotes are legitimate YAML, not a curly-quote violation. Blank
// the region between the first two `---` delimiters, same line-number-
// preserving approach as stripFences below.
export function stripFrontmatter(content) {
  const lines = content.split('\n');
  const end = frontmatterEnd(lines);
  if (end === -1) return content;
  for (let i = 0; i <= end; i++) lines[i] = '';
  return lines.join('\n');
}

// Vale's TokenIgnores/BlockIgnores never reach YAML frontmatter values: Vale
// parses front matter through a separate code path (`lintMetadata`) that
// runs, and completes, before the Transform step TokenIgnores/BlockIgnores
// apply in (confirmed against Vale v3.13.0 source — internal/lint/md.go's
// lintMarkdown calls lintMetadata before Transform; internal/lint/
// metadata.go's lintMetadata reads each field's raw parsed-YAML string and
// lints it directly, with no Transform call in between). A second symptom
// shares this root cause: when a frontmatter field's exact wikilink text
// also appears in the body, Vale's own alert-location code (internal/core/
// file.go's assignLoc, handed blk.Context = the whole file for a metadata
// block) can misattribute a second flagged word inside that same field to
// the body line instead of the true frontmatter line — confirmed by a
// minimal repro (a two-vocab-word slug like `keth-naar` mislocates its
// second word once the same wikilink also appears in the body; a
// single-vocab-word slug like `tidefall` does not). Both symptoms disappear
// once the flagged text no longer exists in what Vale reads, so
// frontmatter values get the same slug-vs-display split TokenIgnores gives
// body prose — applied before Vale runs instead of inside it. Mirrors
// TokenIgnores' own two `.vale.ini` patterns: a piped wikilink keeps only
// its display half, an embed (never rendered as text) is dropped whole.
const FM_PIPED_WIKILINK_RE = /\[\[[^\]|]+\|([^\]]+)\]\]/g;
const FM_EMBED_RE = /!\[\[[^\]]+\]\]/g;
// An UNPIPED frontmatter wikilink is all slug and no display half, so there
// is nothing left to spell/term-check once the split above would have run —
// dropped whole, same as an embed. `within:` is the case that forces this:
// `vault/_templates/CLAUDE.md` requires it to carry the full vault-relative
// path with NO alias, so every containment key in the vault presents Vale a
// bare kebab-case path. Without this, a lowercase segment inside the path
// (`.../midchain/wibowos-provisions`) trips Vale.Terms demanding
// `Midchain`, and the only ways to satisfy it are editing the link target's
// case (breaks resolution) or adding the alias the template forbids.
//
// Substituted with a filler word, NOT deleted: an embed always sits inside
// an already-quoted scalar, but an unpiped wikilink is often a bare
// sequence item (`- [[slug]]`), and deleting it leaves `- ` — an empty node
// that fails Vale's own YAML parse of the temp copy with E201 and takes the
// whole batch's findings down with it. "link" is an ordinary dictionary
// word, so it carries no spelling, term, or vocabulary signal of its own.
const FM_UNPIPED_WIKILINK_RE = /\[\[[^\]|]+\]\]/g;
const FM_UNPIPED_WIKILINK_FILLER = "link";
// Mirrors .vale.ini's own TokenIgnores entry for the 5e rarity tier "Very
// Rare" — same root cause as the wikilink split above (Vale's frontmatter
// path never applies TokenIgnores), so the `rarity: very rare` enum value
// needs the same pre-scan neutralization. Dropped to just "rare" so
// write-good.Weasel/proselint.Very stop matching `\bvery\b` without
// introducing a Vale.Spelling hit of their own (an earlier squash to
// "veryrare" did); this only ever reaches the ephemeral lint copy, never
// the real file.
const FM_VERY_RARE_RE = /\bvery rare\b/gi;
// `owner_skill:` names the guide or skill that owns the page's quality and
// persists onto every instantiated page (ADR-0044). When it points at a skill
// rather than a GUIDE.md, its value literally contains "SKILL.md", which
// CampaignOS.ProcessLeak flags as repo-process vocabulary leaking into wiki
// prose — correct for a body sentence, wrong for the one frontmatter key
// designed to hold exactly that. The whole value is blanked for the lint copy
// (same root cause and same remedy as the keys above); a real ProcessLeak in
// the page body is untouched.
const FM_OWNER_SKILL_RE = /^(owner_skill:\s*).*$/gm;
// Any frontmatter value naming a file under _assets/ (`reference_image:`,
// and whatever asset key comes next) is an on-disk path, case-sensitive and
// not ours to reword — renaming the file is the only way to "fix" a finding
// against it, and that breaks the embed. Vale.Terms otherwise demands
// `Blight`/`Riva` for the lowercase slug inside
// `_assets/banners/blight-banner.webp`. Matched by the value's shape rather
// than by key name so a new asset key needs no change here.
const FM_ASSET_PATH_RE = /^([a-z_]+:\s*).*_assets\/.*$/gm;
// `pc: "<pc-slug>"` (pc-abilities.md/pc-combat-profile.md/pc-inventory.md/
// pc-spells.md/pc-stats.md/pc-gallery.md/pc-interview.md templates) is a
// machine identifier, not prose — Vale's frontmatter path never applies
// TokenIgnores (same root cause as the wikilink split above), so a lowercase
// slug that embeds a PC's name (e.g. "crissdalynn-khinriss") trips
// Vale.Terms wanting it capitalized. Title-case each hyphen segment for the
// ephemeral lint copy only; the real file's slug (used for lookups) never
// changes.
const FM_PC_KEY_RE = /^(pc: "?)([a-z][a-z0-9-]*)("?)$/gm;
const FM_TRANSFORM_HINT_RE =
  /\[\[[^\]]+\]\]|\bvery rare\b|^pc: "?[a-z]|^owner_skill:\s*\S|_assets\//im;

// A `[!check]` callout title requires an em-dash by the callouts spec
// (`vault/campaigns/.claude/skills/callouts/references/check.md`): `[!check]
// <Skill or Save> — <Label>`. .vale.ini's BlockIgnores documents this exact
// em-dash as a required false positive for ai-tells.EmDashUsage, but a file
// with many `[!check]` callouts still leaks one unsuppressed error (Vale
// v3.13.0, confirmed via a standalone regexp2 reproduction: the BlockIgnores
// replace call itself wraps every match correctly in isolation, so the leak
// sits deeper in Vale's own pipeline, not in this repo's BlockIgnores
// pattern). Swap the em-dash for a comma on these lines only, one rune for
// one rune, so every other column position on the line stays aligned for
// any other finding Vale reports there.
const CHECK_CALLOUT_DASH_RE = /^(> \[!check\][^\n]*?)—([^\n]*)$/gm;

export function neutralizeCheckCalloutDashes(content) {
  return content.replace(CHECK_CALLOUT_DASH_RE, (_m, before, after) => `${before},${after}`);
}

// A ```statblock fence is the Fantasy Statblocks plugin's own YAML schema
// (vault/refs/vault/monster/references/statblock-format.md) — machine-parsed
// data, kept byte-accurate for `dndsim lint`'s parser, not prose anyone may
// reword. Vale skips fenced code on its own, so ordinary rules never reach in;
// a `scope: raw` rule reads the unprocessed source instead and does, which is
// how ai-tells.Metacommentary came to flag a lair action's `desc:` for
// explaining what the action sets up — exactly the substantive mechanical note
// a DM needs. Blanked line-for-line so every other finding in the file keeps
// its real line number.
const STATBLOCK_FENCE_RE = /^(```statblock[^\n]*\n)([\s\S]*?)(^```)/gm;

export function neutralizeStatblockFences(content) {
  return content.replace(
    STATBLOCK_FENCE_RE,
    (_m, open, body, close) => open + body.replace(/[^\n]/g, " ") + close,
  );
}

export function transformFrontmatterWikilinks(content) {
  const lines = content.split('\n');
  const end = frontmatterEnd(lines);
  if (end === -1) return content;
  for (let i = 1; i < end; i++) {
    lines[i] = lines[i]
      .replace(FM_EMBED_RE, '')
      .replace(FM_PIPED_WIKILINK_RE, (_m, display) => display)
      .replace(FM_UNPIPED_WIKILINK_RE, FM_UNPIPED_WIKILINK_FILLER)
      .replace(FM_VERY_RARE_RE, 'rare')
      .replace(FM_OWNER_SKILL_RE, '$1""')
      .replace(FM_ASSET_PATH_RE, '$1""')
      .replace(FM_PC_KEY_RE, (_m, prefix, slug, suffix) => {
        const titled = slug.split('-').map((w) => w[0].toUpperCase() + w.slice(1)).join('-');
        return `${prefix}${titled}${suffix}`;
      });
  }
  return lines.join('\n');
}

// Scans `targets` (files or directories — anything expandTargets accepts)
// for files whose front matter needs the wikilink transform, WITHOUT adding
// any of them to Vale's own argv: the scan runs entirely in-process
// (expandTargets + readFileSync), and only the small affected subset
// (typically a handful of files, never the whole corpus) gets written out
// and appended as extra paths. Passing every expanded file to Vale as an
// individual argv entry instead — the first cut of this — hit E2BIG on a
// full-vault sweep (~12k files, well past ARG_MAX); this keeps the
// caller's original targets (however small or large, directory or file)
// untouched and only ever adds a few paths on top.
//
// A file whose front matter holds no piped wikilink/embed is left alone
// entirely (the common case — no I/O beyond the read-and-test). A file
// that does gets an ephemeral sibling copy (same directory, so the same
// .vale.ini section glob applies) written with the transform applied, and
// its ORIGINAL path is added to the returned exclude glob — Vale must skip
// the original wherever it's reached (an explicit arg or a directory walk;
// both honor `--glob`), or its still-unclean text and the ephemeral copy's
// clean one would both get linted, alerting twice. `extraExcludes` folds
// in any exclusion the caller already needed (e.g. `!**/node_modules/**`)
// — Vale takes exactly one `--glob` value, so every exclusion has to live
// in one combined pattern.
//
// A copy is added to the returned targets ONLY when no directory target
// already covers it — Vale doesn't skip dotfiles (only the `node_modules`/
// `.git` DIRECTORY names, per its own ShouldIgnoreDirectory), so a
// directory target's own walk rediscovers a sibling copy on its own; also
// listing it as an explicit arg would lint (and print) it a second time.
//
// Callers MUST call cleanup() in a finally block even on error, or an
// ephemeral copy leaks.
//
// `checkCalloutGuard: true` (advisory vale only — vale-hard never
// runs ai-tells, so it has nothing to guard against here) folds in
// neutralizeCheckCalloutDashes for the same ephemeral-copy mechanism: a
// file needing only the callout-dash swap, only the wikilink swap, or both
// still gets exactly one copy, never two.
//
// Deleting a copy the instant OUR OWN vale run finishes (the original
// design) is a real cross-process/cross-tool race, confirmed by direct
// repro: markdownlint-obsidian builds a vault-wide file index on every
// invocation (wikilink/embed resolution needs to know about every page, not
// just the files it was told to lint) regardless of the `ignores` glob in
// .obsidian-linter.jsonc (that glob only filters which files get their own
// rules run, not what the vault indexer discovers) — so it can `readdir` a
// directory, see an ephemeral copy that's still there, and by the time it
// gets around to opening it, a concurrent `withFrontmatterGuard` invocation
// has already deleted it, surfacing an unrelated file's ENOENT as an OFM901
// finding on whatever page it happened to be linting (98ab781d's
// `.obsidian-linter.jsonc` ignores entry narrows this but doesn't close it —
// confirmed: same ENOENT reproduces against this repo with generic decoy
// `.vale-fm-*.md` churn in a sibling directory, no shared content needed).
// Renaming the copy first wouldn't help — the other process is already
// blocked on opening the OLD name, so the fix isn't a better delete, it's no
// synchronous delete: `cleanup()` sweeps only copies old enough that no
// realistic concurrent reader could still be mid-open on them, and a fresh
// copy from THIS run is swept later, by whichever invocation next touches
// that directory once the grace period has passed.
const STALE_TEMP_MS = 2 * 60 * 1000;

// Best-effort: removes every `*<marker>*.md` sibling in `dir` older than
// STALE_TEMP_MS, EXCEPT the ones this process itself wrote. Called both
// before writing a new copy (reclaims orphans left by a crashed/killed
// prior invocation) and from cleanup().
// Shared by withFrontmatterGuard's `.vale-fm-` copies and withLineChunking's
// `.vale-chunk-` copies below — same orphan-reclaim mechanism, two markers.
// A `.vale-fm-` copy carries the original file's stem as a PREFIX
// (`transcript.vale-fm-<pid>-...md`), so the marker is matched anywhere in
// the name, not at the start. A `.vale-chunk-` copy instead keeps the
// original basename untouched and puts the marker on its own enclosing
// directory, so an exact-name .vale.ini section glob (`[**/CLAUDE.md]`)
// keeps matching it; a `<stem>.vale-chunk-*.md` name silently dropped every
// such section and re-linted the copy under the broad [vault/**/*.md]
// styles, which is why a file over the chunk threshold used to get a
// different rule set than the same file under it.
//
// The age threshold alone is not a safe test for "orphan": a full-corpus
// run stages temps for every batch up front and then lints for minutes, so
// its own earliest copies age past STALE_TEMP_MS while their `vale` process
// still needs them. A later batch's sweep then deletes a live sibling and
// that batch dies with `E100 [doLint] Runtime error: argument
// '<dir>/.vale-fm-*.md' does not exist` — losing every finding for those
// files. Both temp names embed the writing process's pid, so skipping our
// own pid keeps orphan reclaim working without ever deleting a live copy.
// A SECOND concurrent lint process's temps (SessionStart's backgrounded
// sweep racing an agent's own `npm run lint`) are protected by a liveness
// probe: an aged temp is deleted only when its embedded pid is no longer
// running, so a live sibling run keeps its copies however long it takes.
// ponytail: a recycled pid can shield another run's orphan until that pid
// exits — age+liveness, not a lockfile, is deliberate; the orphan is still
// reclaimed by the next sweep after the recycled pid dies.
function pidIsAlive(pid) {
  if (!Number.isInteger(pid) || pid <= 0) return false;
  try {
    process.kill(pid, 0);
    return true;
  } catch (e) {
    return e.code === 'EPERM'; // exists but not ours — still alive
  }
}

function sweepStaleTemps(dir, marker = '.vale-fm-') {
  let entries;
  try {
    entries = readdirSync(dir);
  } catch {
    return;
  }
  const now = Date.now();
  const ownMarker = `${marker}${process.pid}-`;
  for (const entry of entries) {
    const at = entry.indexOf(marker);
    if (at === -1) continue;
    if (entry.includes(ownMarker)) continue; // this run's own live copy
    const full = path.join(dir, entry);
    let stat;
    try {
      stat = statSync(full);
    } catch {
      continue;
    }
    // A marked entry is either an ephemeral `.md` copy (withFrontmatterGuard)
    // or an ephemeral directory holding one (withLineChunking, which keeps the
    // original basename inside it so per-file config globs still match).
    if (!stat.isDirectory() && !entry.endsWith('.md')) continue;
    const writerPid = Number.parseInt(entry.slice(at + marker.length), 10);
    if (pidIsAlive(writerPid)) continue; // a live sibling run's copy
    if (now - stat.mtimeMs > STALE_TEMP_MS) rmSync(full, { force: true, recursive: true });
  }
}

export function withFrontmatterGuard(targets, { extraExcludes = [], checkCalloutGuard = false } = {}) {
  const tempToOriginal = new Map();
  const excludeOriginals = [];
  const tempTargets = [];
  const touchedDirs = new Set();

  const dirTargets = targets
    .filter((t) => {
      try {
        return statSync(path.join(REPO_ROOT, t)).isDirectory();
      } catch {
        return false;
      }
    })
    .map((t) => path.join(REPO_ROOT, t) + path.sep);

  for (const rel of expandTargets(targets)) {
    const abs = path.join(REPO_ROOT, rel);
    let content;
    try {
      content = readFileSync(abs, 'utf8');
    } catch {
      continue;
    }
    const lines = content.split('\n');
    const end = frontmatterEnd(lines);
    const fm = end === -1 ? '' : lines.slice(0, end + 1).join('\n');
    const needsFmTransform = end !== -1 && FM_TRANSFORM_HINT_RE.test(fm);
    const needsCalloutTransform = checkCalloutGuard && CHECK_CALLOUT_DASH_RE.test(content);
    CHECK_CALLOUT_DASH_RE.lastIndex = 0; // stateful /g regex — reset after .test()
    const needsStatblockTransform = content.includes('```statblock');
    if (!needsFmTransform && !needsCalloutTransform && !needsStatblockTransform) continue;

    let transformed = needsFmTransform ? transformFrontmatterWikilinks(content) : content;
    if (needsCalloutTransform) transformed = neutralizeCheckCalloutDashes(transformed);
    if (needsStatblockTransform) transformed = neutralizeStatblockFences(transformed);
    const dir = path.dirname(abs);
    if (!touchedDirs.has(dir)) {
      touchedDirs.add(dir);
      sweepStaleTemps(dir); // reclaim orphans from a crashed/killed prior run
    }
    // pid + a crypto-random UUID (not Math.random(), whose ~52 bits of
    // entropy is fine for uniqueness but isn't the standard for a name that
    // has to be genuinely unpredictable across concurrently-spawned
    // processes) — the pid stays for a human skimming `ls` mid-run, the
    // UUID is what actually guarantees no two invocations ever pick the
    // same path.
    const tempAbs = path.join(dir, `${path.basename(abs, '.md')}.vale-fm-${process.pid}-${randomUUID()}.md`);
    writeFileSync(tempAbs, transformed);
    const tempRel = path.relative(REPO_ROOT, tempAbs);
    tempToOriginal.set(tempRel, rel);
    excludeOriginals.push(rel);
    if (!dirTargets.some((d) => tempAbs.startsWith(d))) tempTargets.push(tempRel);
  }

  const excludePatterns = [...extraExcludes, ...excludeOriginals];

  return {
    targets: [...targets, ...tempTargets],
    glob: excludePatterns.length > 0 ? `!{${excludePatterns.join(',')}}` : undefined,
    tempToOriginal,
    // Deletes this run's own copies by name, then sweeps each touched
    // directory for FOREIGN orphans (a crashed prior invocation). Callers
    // run cleanup() from a finally block after every `vale` process has
    // exited, so an eager delete-by-name is safe here — and it is the only
    // thing that reclaims our copies now that sweepStaleTemps deliberately
    // skips our own pid (see its comment: age alone cannot tell a live copy
    // from an orphan on a run that outlasts STALE_TEMP_MS).
    cleanup() {
      for (const tempRel of tempToOriginal.keys()) {
        rmSync(path.join(REPO_ROOT, tempRel), { force: true });
      }
      for (const dir of touchedDirs) sweepStaleTemps(dir);
    },
  };
}

// A single large file handed to `vale` in one piece costs far more than its
// share of a full sweep: measured on this repo's own worst offenders
// (2026-08-01), `vale`'s own per-alert cost scales with (matches × file
// size), not matches alone — a file whose match count grows with its size
// (any high-match-density file, e.g. a dialogue transcript where nearly
// every line trips at least one existence-style rule) costs O(size^2)
// wall-clock, not O(size). Confirmed empirically, not just reasoned about:
// a synthetic file built from one repeating always-matching line went
// 0.6s/500 lines -> 2.1s/1k -> 8.1s/2k -> 32.5s/4k (each doubling ~4x, the
// signature of quadratic growth); the SAME token rewritten to never match
// stayed flat at 0.25s regardless of file size; a real 2,267-line
// dialogue-transcript page timed out entirely under the full ruleset but
// completed in 46s once split into 500-line pieces vs. never completing
// whole. The two worst files in this repo (transcript.raw.md at ~28.8k and
// ~11.9k lines) are exactly this shape. This is `vale`'s own internal
// bookkeeping cost (confirmed: even a trivial, lookaround-free token
// reproduces the curve), not any one rule's regex — no rule authored in
// this repo can fix it, and no rule needs to: splitting the INPUT restores
// linear-ish total cost while every line still gets scanned by every rule
// that would have scanned it whole (full coverage, nothing disabled).
export const VALE_LINE_CHUNK = 500;

// Splits any target file whose line count exceeds `maxLines` into
// sequential ephemeral copies at `<dir>/.vale-chunk-<pid>-<uuid>-<n>/<basename>`
// — same parent directory AND the original's exact basename, so
// directory-scoped and basename-anchored .vale.ini section globs both keep
// applying. A file at or under the threshold passes through untouched
// (the common case — no I/O beyond the read-and-count). `chunkToOriginal`
// maps each chunk's rel path to `{ original, lineOffset }` so a caller can
// remap a chunk's own alert `Line` (1-based, relative to the chunk) back to
// the real file's line number by adding lineOffset. `excludeOriginals` is
// returned raw (not pre-joined into a glob) so a caller composing this with
// withFrontmatterGuard's own `extraExcludes` can merge both exclusion lists
// into that single `--glob` value Vale accepts.
//
// Callers MUST call cleanup() in a finally block even on error, or an
// ephemeral chunk leaks (same contract as withFrontmatterGuard).
export function withLineChunking(targets, { maxLines = VALE_LINE_CHUNK } = {}) {
  const chunkToOriginal = new Map();
  const excludeOriginals = [];
  const outTargets = [];
  const touchedDirs = new Set();

  const dirTargets = targets
    .filter((t) => {
      try {
        return statSync(path.join(REPO_ROOT, t)).isDirectory();
      } catch {
        return false;
      }
    })
    .map((t) => path.join(REPO_ROOT, t) + path.sep);

  for (const rel of expandTargets(targets)) {
    const abs = path.join(REPO_ROOT, rel);
    let content;
    try {
      content = readFileSync(abs, 'utf8');
    } catch {
      continue;
    }
    const lines = content.split('\n');
    if (lines.length <= maxLines) {
      outTargets.push(rel);
      continue;
    }

    const dir = path.dirname(abs);
    if (!touchedDirs.has(dir)) {
      touchedDirs.add(dir);
      sweepStaleTemps(dir, 'vale-chunk-'); // reclaim orphans from a crashed/killed prior run
    }
    excludeOriginals.push(rel);

    for (let start = 0, chunkIndex = 0; start < lines.length; start += maxLines, chunkIndex += 1) {
      const slice = lines.slice(start, start + maxLines).join('\n');
      // One ephemeral directory per chunk, holding the chunk under the
      // original's OWN basename. A chunk named `<stem>.vale-chunk-*.md`
      // instead stops matching every basename-anchored config section the
      // real file matches (`[**/CLAUDE.md]`, `[vault/_templates/CLAUDE.md]`,
      // `[docs/guardrails/_FORMAT.md]`, …), so a file over the threshold
      // silently gets a different rule set than the same file under it.
      const chunkDirAbs = path.join(dir, `.vale-chunk-${process.pid}-${randomUUID()}-${chunkIndex}`);
      mkdirSync(chunkDirAbs, { recursive: true });
      const chunkAbs = path.join(chunkDirAbs, path.basename(abs));
      writeFileSync(chunkAbs, slice);
      const chunkRel = path.relative(REPO_ROOT, chunkAbs);
      chunkToOriginal.set(chunkRel, { original: rel, lineOffset: start });
      if (!dirTargets.some((d) => chunkAbs.startsWith(d))) outTargets.push(chunkRel);
    }
  }

  return {
    targets: outTargets,
    excludeOriginals,
    chunkToOriginal,
    // Same contract as withFrontmatterGuard's cleanup above: delete this
    // run's own chunks by name, then age-sweep only foreign orphans.
    cleanup() {
      for (const chunkRel of chunkToOriginal.keys()) {
        // The chunk owns its enclosing ephemeral directory — remove that, not
        // just the file, or the empty dir leaks into the vault tree.
        rmSync(path.dirname(path.join(REPO_ROOT, chunkRel)), { force: true, recursive: true });
      }
      for (const dir of touchedDirs) sweepStaleTemps(dir, 'vale-chunk-');
    },
  };
}

// Fenced code blocks (```statblock, ```meta-bind-button, etc.) hold
// structured/data syntax, not prose — a straight quote required by e.g. the
// Obsidian statblock plugin's parser is not a curly-quote violation. Blank
// fenced lines (delimiters included) before linting; line numbers stay
// aligned for accurate findings.
export function stripFences(content) {
  const fenceRe = /^\s*(`{3,}|~{3,})/;
  let inFence = false;
  return content
    .split('\n')
    .map((line) => {
      if (fenceRe.test(line)) {
        inFence = !inFence;
        return '';
      }
      return inFence ? '' : line;
    })
    .join('\n');
}

// HTML comments (<!-- AGENT: ... -->) are authoring/editor notes — invisible
// in any markdown renderer, never part of what a player or DM reads, and in
// _templates/ specifically they're deleted by the instantiating agent before
// the page ships. Blank character-by-character (not whole lines) since a
// comment can start/end mid-line; preserves line AND column numbers for
// anything else sharing those lines.
export function stripHtmlComments(content) {
  return content.replace(/<!--[\s\S]*?-->/g, (m) => m.replace(/[^\n]/g, ' '));
}

// Both linters write their JSON to a real temp file rather than a captured
// pipe: markdownlint-obsidian-cli truncates at 64KB on a piped stdout (a
// partial-write bug — confirmed: piping gives exactly 65536 bytes of a
// 332867-byte real report; writing to a file descriptor doesn't).
// Expands a directory target to every file under it a lint producer might
// care about (.md/.mjs/.js); a file target passes through unchanged. Shared
// by wiki-cli producers (or any future
// path-scoped mode) so a target resolves identically everywhere — "no path
// = full repo, a file/folder = just that" is the one convention every
// producer in this file already follows.
export function expandTargets(targets) {
  return targets.flatMap((target) => {
    const abs = path.resolve(REPO_ROOT, target);
    const rel = path.relative(REPO_ROOT, abs);
    if (isArchived(rel)) return [];
    let stat;
    try {
      stat = statSync(abs);
    } catch {
      return [rel];
    }
    if (!stat.isDirectory()) return [rel];
    // node_modules under an expanded dir (a skill's vendored scripts) is a
    // package's own files, not this repo's lintable content — same exclusion
    // collectScope's walk applies. A vale-fm/vale-chunk orphan gets the same
    // exclusion isExcluded() gives collectScope() — see isValeTempFile's doc
    // comment above.
    return fg.sync(['**/*.md', '**/*.mjs', '**/*.js'], { cwd: abs, ignore: ['**/node_modules/**'] })
      .filter((f) => !isValeTempFile(f))
      .map((f) => `${rel}/${f}`);
  });
}

function runCaptured(cmd, args, cwd) {
  const outPath = path.join(os.tmpdir(), `lint-run-${process.pid}-${Math.random().toString(36).slice(2)}.json`);
  const fd = openSync(outPath, 'w');
  let result;
  try {
    result = spawnSync(cmd, args, { cwd, stdio: ['ignore', fd, 'ignore'] });
  } finally {
    closeSync(fd);
  }
  const raw = readFileSync(outPath, 'utf8');
  rmSync(outPath, { force: true });
  return { raw, result };
}

export function runToFile(cmd, args, cwd) {
  return runCaptured(cmd, args, cwd).raw;
}

// Same capture-to-file mechanism as runToFile (avoids the piped-stdout
// truncation bug documented above), for a caller that also needs the
// subprocess's own exit status/spawn error — e.g. a CLI wrapper that must
// propagate Vale's exit code as its own.
export function runToFileWithStatus(cmd, args, cwd) {
  const { raw, result } = runCaptured(cmd, args, cwd);
  return { raw, status: result.status, error: result.error };
}

// Files per `vale` subprocess invocation, counted AFTER withLineChunking
// expands any oversized file into its pieces (never the raw target count —
// a batch of exactly 200 raw targets that happens to include a few huge
// files can expand well past 200 real files handed to `vale`, and 200 was
// already the confirmed OOM edge for ordinary files alone: this repo's own
// measurement, 2026-08-01, had 50 files at 261MB peak RSS and 200 files
// OOMing (exit 137, empty stdout) with NO chunking involved at all). Kept
// at the smaller, empirically-safe figure now that batches also run
// concurrently (VALE_CONCURRENCY below) — concurrent batches multiply peak
// memory, so the safe per-batch figure matters more here than it did when
// batches ran strictly one at a time.
export const VALE_FILE_BATCH = 50;

// The one place every `vale`-invoking script in this repo should call
// through — wiki-cli's Vale producers' direct
// invocations both route through this single entry point.
// Batches `targets` by VALE_FILE_BATCH (OOM avoidance) and, within each
// batch, runs every file through withLineChunking first (the O(size^2)
// per-file fix documented above withLineChunking) and withFrontmatterGuard
// second (frontmatter-wikilink transform + `[!check]` callout-dash
// neutralization) before invoking `vale --output=JSON` once per batch.
// Every alert is remapped back to the real file and the real (chunk-
// offset-corrected) line number before being handed back, so a caller never
// sees a `.vale-fm-*`/`.vale-chunk-*` temp path or an in-chunk line number.
// Returns `{ byFile: Map<rel, alert[]>, status }` — `status` is the highest
// (most-failing) exit code seen across all batches, mirroring `vale`'s own
// single-invocation exit-code contract (0 clean, 1 alerts found, >1 error).
// Measured on this repo 2026-08-01: a single `vale` process pins only
// ~1-1.5 CPU cores even over hundreds of files (proselint/write-good/
// ai-tells/Readability/the Vocab lookup all cost real per-file time `vale`
// doesn't itself parallelize away — 186 ordinary files took 67s wall at
// ~110% CPU on a 10-core box). Running batches one at a time therefore
// leaves most of the box idle; this many run concurrently instead.
// Empirically tuned, not assumed: 6 and 12 both measured SLOWER full-corpus
// wall time than 8 (180s and 193s vs 139s) — past this level, concurrent
// `vale` processes contend for the same handful of cores/memory bandwidth
// instead of adding throughput, so higher isn't better past this point.
export const VALE_CONCURRENCY = 8;

// Single-quotes `s` for a POSIX shell, escaping any embedded single quote
// the standard `'\''` way (close the quote, an escaped literal quote, reopen
// the quote) — every argv token `runValeScoped` hands to a generated batch
// script goes through this, so a config/target path never needs to be
// "probably safe because this repo's paths are kebab-case" to stay correct.
export function shQuote(s) {
  return `'${String(s).replace(/'/g, `'\\''`)}'`;
}

// The one place every `vale`-invoking script in this repo should call
// through — wiki-cli's Vale producers' direct
// invocations both route through this single entry point.
// Batches `targets` by VALE_FILE_BATCH (OOM avoidance) and, within each
// batch, runs every file through withLineChunking first (the O(size^2)
// per-file fix documented above withLineChunking) and withFrontmatterGuard
// second (frontmatter-wikilink transform + `[!check]` callout-dash
// neutralization) before invoking `vale --output=JSON` — every batch's own
// invocation runs as its own generated shell script, and every script
// launches concurrently (capped at VALE_CONCURRENCY) through one `xargs -P`
// call, so this stays a single synchronous subprocess from the caller's
// perspective (no async cascade through collectFindings' many synchronous
// call sites) while still getting real OS-level parallelism across batches.
// Every alert is remapped back to the real file and the real (chunk-
// offset-corrected) line number before being handed back, so a caller never
// sees a `.vale-fm-*`/`.vale-chunk-*` temp path, a batch script path, or an
// in-chunk line number. Returns `{ byFile: Map<rel, alert[]>, status }` —
// `status` is the highest (most-failing) exit code any batch's own `vale`
// process reported, mirroring `vale`'s own single-invocation exit-code
// contract (0 clean, 1 alerts found, >1 execution error).
export function runValeScoped(targets, {
  configPath,
  checkCalloutGuard = false,
  extraExcludes = [],
  lineChunkMax = VALE_LINE_CHUNK,
  concurrency = VALE_CONCURRENCY,
} = {}) {
  const byFile = new Map();
  let status = 0;
  const batches = [];
  const batchErrors = [];
  let lineChunks;

  try {
    // Phase 1: line-chunk the WHOLE target list up front, once — not
    // per-sub-batch. VALE_FILE_BATCH counts real files handed to `vale`
    // (the OOM-relevant number); chunking per-sub-batch instead would let a
    // batch that happens to contain a huge file balloon well past
    // VALE_FILE_BATCH real files (confirmed: a 200-raw-target batch holding
    // 3 huge files expanded to 286 real files and OOM-killed at exactly the
    // batch size this repo had already confirmed OOMs plain files at).
    // Doing it once over everything keeps every batch below at (or under)
    // VALE_FILE_BATCH real files, chunked or not.
    lineChunks = withLineChunking(targets, { maxLines: lineChunkMax });
    const expanded = lineChunks.targets;

    // Phase 2: slice the (post-chunking) expanded list into VALE_FILE_BATCH
    // batches, and prepare each one (frontmatter-guard expansion, a script
    // file with its own output/exit-code paths). Pure file I/O — cheap, and
    // it must all finish before any `vale` process starts so no batch's
    // cleanup() can race a sibling batch's still-running process.
    // A target deleted between collection and here (a concurrent session
    // renaming/deleting pages mid-sweep) makes `vale` abort its whole batch
    // with `lstat <file>: no such file` — a vanished file has no findings to
    // lose, so drop it now; the retry in Phase 3 catches one that vanishes
    // even later, mid-run.
    const present = expanded.filter((t) => existsSync(path.join(REPO_ROOT, t)) || existsSync(t));
    for (let i = 0; i < present.length; i += VALE_FILE_BATCH) {
      const batchTargets = present.slice(i, i + VALE_FILE_BATCH);
      const guard = withFrontmatterGuard(batchTargets, {
        extraExcludes: [...extraExcludes, ...lineChunks.excludeOriginals],
        checkCalloutGuard,
      });
      const tag = `vale-batch-${process.pid}-${randomUUID()}`;
      const outPath = path.join(os.tmpdir(), `${tag}.json`);
      const errPath = path.join(os.tmpdir(), `${tag}.err`);
      const exitPath = path.join(os.tmpdir(), `${tag}.exit`);
      const scriptPath = path.join(os.tmpdir(), `${tag}.sh`);
      const valeArgs = [
        'vale',
        '--config', configPath,
        '--output=JSON',
        ...(guard.glob ? [`--glob=${guard.glob}`] : []),
        ...guard.targets,
      ].map(shQuote).join(' ');
      writeFileSync(
        scriptPath,
        `#!/bin/sh\n${valeArgs} >${shQuote(outPath)} 2>${shQuote(errPath)}\necho $? >${shQuote(exitPath)}\n`,
        { mode: 0o755 },
      );
      batches.push({ guard, outPath, errPath, exitPath, scriptPath });
    }

    // Phase 2: run every batch script concurrently. `xargs -P` (BSD and GNU
    // both support it) reads one script path per NUL-terminated line from
    // stdin and runs up to `concurrency` of them at once; each script
    // redirects its OWN stdout/stderr/exit-code to its own files, so
    // nothing about parallel execution order needs to reach this process's
    // own stdout — the parent call just blocks until every job is done.
    if (batches.length > 0) {
      const manifest = batches.map((b) => b.scriptPath).join('\0');
      const driver = spawnSync(
        'xargs',
        ['-0', '-P', String(concurrency), '-I{}', 'sh', '{}'],
        { cwd: REPO_ROOT, input: manifest, stdio: ['pipe', 'ignore', 'pipe'] },
      );
      if (driver.error) throw new Error(`vale batch driver failed to spawn: ${driver.error.message}`);
    }

    // Phase 3: read every batch's own output back and remap.
    for (const { guard, outPath, errPath, exitPath } of batches) {
      let raw = '';
      try {
        raw = readFileSync(outPath, 'utf8');
      } catch {
        // Empty/missing output — batch found nothing or crashed before
        // writing anything; the exit-code read below still surfaces a crash.
      }
      let batchStatus = 0;
      try {
        batchStatus = Number.parseInt(readFileSync(exitPath, 'utf8').trim(), 10) || 0;
      } catch {
        batchStatus = 1; // script never finished (e.g. killed) — treat as non-clean, not silently clean
      }
      status = Math.max(status, batchStatus);
      // A batch that exited >1 hit a `vale` EXECUTION error (0 clean, 1
      // alerts found), so its files were never inspected and their alerts
      // are simply missing from the result. Silence here reads to a caller
      // as "those files are clean" — an under-report that makes the gate
      // look greener than the vault is. Record what the batch actually said
      // so a caller can refuse to trust (or cache) a lossy run.
      if (batchStatus > 1) {
        let errRaw = '';
        try {
          errRaw = readFileSync(errPath, 'utf8');
        } catch {
          errRaw = '(no stderr captured)';
        }
        // Vanished-file abort: a concurrent session deleted/renamed a target
        // after this batch's script was written, and vale exits >1 at the
        // first missing file. A file that no longer exists has no findings
        // to report — retry the batch synchronously with only the survivors
        // (looped, since vale stops at the FIRST missing file). Any other
        // execution error still records a batchError below.
        // Vale reports a vanished file two ways: `lstat <p>: no such file or
        // directory` and `argument '<p>' does not exist` — match both.
        const missing = [
          ...[...errRaw.matchAll(/lstat ([^:]+): no such file or directory/g)].map((m) => m[1]),
          ...[...errRaw.matchAll(/argument '([^']+)' does not exist/g)].map((m) => m[1]),
        ].filter((p) => !existsSync(path.join(REPO_ROOT, p)) && !existsSync(p));
        if (missing.length > 0) {
          let survivors = guard.targets.filter((t) => existsSync(path.join(REPO_ROOT, t)) || existsSync(t));
          let retried = null;
          for (let attempt = 0; attempt < 3 && retried == null; attempt++) {
            const r = spawnSync('vale', [
              '--config', configPath, '--output=JSON',
              ...(guard.glob ? [`--glob=${guard.glob}`] : []),
              ...survivors,
            ], { cwd: REPO_ROOT, encoding: 'utf8', maxBuffer: 256 * 1024 * 1024 });
            const rStatus = r.status ?? 1;
            if (rStatus <= 1) {
              retried = { raw: r.stdout ?? '', status: rStatus };
            } else {
              const rErr = r.stderr ?? '';
              const again = [
                ...[...rErr.matchAll(/lstat ([^:]+): no such file or directory/g)].map((m) => m[1]),
                ...[...rErr.matchAll(/argument '([^']+)' does not exist/g)].map((m) => m[1]),
              ];
              if (again.length === 0) break; // a real error — fall through to batchErrors
              survivors = survivors.filter((t) => existsSync(path.join(REPO_ROOT, t)) || existsSync(t));
            }
          }
          if (retried != null) {
            raw = retried.raw;
            batchStatus = retried.status;
            status = Math.max(status, batchStatus);
          }
        }
        if (batchStatus > 1) {
          batchErrors.push(`exit ${batchStatus} over ${guard.targets.length} file(s): ${errRaw.trim().slice(0, 300)}`);
        }
      }
      let data = {};
      if (raw.trim().length > 0) {
        try {
          data = JSON.parse(raw);
        } catch (e) {
          const errRaw = (() => {
            try {
              return readFileSync(errPath, 'utf8');
            } catch {
              return '';
            }
          })();
          throw new Error(`vale output unparseable (${e.message}); first 300 bytes: ${raw.slice(0, 300)}; stderr: ${errRaw.slice(0, 300)}`);
        }
      }
      for (const [file, alerts] of Object.entries(data)) {
        const rel = path.isAbsolute(file) ? path.relative(REPO_ROOT, file) : file;
        const afterGuard = guard.tempToOriginal.get(rel) ?? rel;
        const chunkInfo = lineChunks.chunkToOriginal.get(afterGuard);
        const originalRel = chunkInfo ? chunkInfo.original : afterGuard;
        if (!alerts || alerts.length === 0) continue;
        const list = byFile.get(originalRel) ?? [];
        for (const a of alerts) {
          list.push(chunkInfo ? { ...a, Line: a.Line + chunkInfo.lineOffset } : a);
        }
        byFile.set(originalRel, list);
      }
    }
  } finally {
    for (const { guard, outPath, errPath, exitPath, scriptPath } of batches) {
      guard.cleanup();
      for (const p of [outPath, errPath, exitPath, scriptPath]) rmSync(p, { force: true });
    }
    lineChunks?.cleanup();
  }

  return { byFile, status, batchErrors };
}
