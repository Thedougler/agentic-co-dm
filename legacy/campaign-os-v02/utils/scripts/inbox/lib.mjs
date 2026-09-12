// Shared helpers for the inbox:check / inbox:archive / inbox:similar commands.
// Stateless by design (raw/CLAUDE.md): "what has been archived" and "which
// wiki page(s) came from it" are both derived on demand from disk — the
// former by rehashing raw/'s own files (findArchivedByHash), the latter by
// grepping vault/ for `source:` frontmatter citing the archived path
// (findWikiPagesForArchivedPath) — never from a ledger. This replaces
// llm-wiki-ingest's queue-file/INGESTED.tsv bookkeeping for inbox-sourced
// content only (migration-mode sources outside inbox/ still use that
// mechanism — see llm-wiki-ingest/SKILL.md).

import { createHash } from 'node:crypto';
import { readFileSync, existsSync, mkdirSync, renameSync, readdirSync, rmdirSync, statSync, writeFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';
// markitdown-ts is dynamically imported inside convertToMarkdownCompanion,
// not statically here — importing it eagerly costs ~2s on its own (loading
// its bundled converters) even when there is nothing under inbox/ left to
// convert, which is the common case on every SessionStart (perf: see
// sweep-to-markdown.mjs's cache-check-before-import ordering).

const __dirname = path.dirname(fileURLToPath(import.meta.url));
// INBOX_REPO_ROOT lets tests point every path here at an isolated temp
// sandbox instead of the real repo — unset in normal use.
export const REPO_ROOT = process.env.INBOX_REPO_ROOT
  ? path.resolve(process.env.INBOX_REPO_ROOT)
  : path.resolve(__dirname, '..', '..', '..');
export const INBOX_DIR = path.join(REPO_ROOT, 'inbox');
export const ARCHIVE_DIR = path.join(REPO_ROOT, 'raw');
export const VAULT_DIR = path.join(REPO_ROOT, 'vault');

const SKIP_NAMES = new Set(['.DS_Store', '.gitkeep']);

/** @param {string} absPath */
export function hashFile(absPath) {
  return createHash('sha256').update(readFileSync(absPath)).digest('hex');
}

// Recursively lists every real file under `rootDir`, skipping OS/editor
// noise. Shared walk behind listInboxFiles/listArchivedFiles.
/** @param {string} rootDir */
function walkFiles(rootDir) {
  /** @type {string[]} */
  const results = [];
  /** @param {string} dir */
  function walk(dir) {
    for (const name of readdirSync(dir)) {
      if (SKIP_NAMES.has(name)) continue;
      const abs = path.join(dir, name);
      const st = statSync(abs);
      if (st.isDirectory()) {
        walk(abs);
      } else if (st.isFile()) {
        results.push(abs);
      }
    }
  }
  if (existsSync(rootDir)) walk(rootDir);
  return results;
}

// Recursively lists every real file under inbox/, skipping OS/editor noise.
/** @returns {string[]} */
export function listInboxFiles() {
  return walkFiles(INBOX_DIR);
}

// Recursively lists every real file under raw/, skipping OS/editor noise —
// the derivation source for "what has already been archived" (no ledger;
// raw/CLAUDE.md).
/** @returns {string[]} */
export function listArchivedFiles() {
  return walkFiles(ARCHIVE_DIR);
}

// Returns the repo-relative raw/ path(s) whose content hash matches `hash` —
// the dedupe check inbox:check/inbox:archive both use, derived directly from
// raw/'s current contents on every call instead of a ledger. raw/ is small
// (a few hundred files, single-digit MB), so rehashing it each call costs
// well under a second — no cache needed.
/** @param {string} hash */
export function findArchivedByHash(hash) {
  return listArchivedFiles()
    .filter((abs) => hashFile(abs) === hash)
    .map((abs) => path.relative(REPO_ROOT, abs));
}

// Returns every vault/ page (repo-relative path, sorted) whose `source:`
// frontmatter cites `archivedRelPath` exactly — the wiki-paths mapping,
// derived from disk instead of a ledger (raw/CLAUDE.md's ingestion
// contract). Shells to grep rather than walking vault/'s ~2000+ pages in JS.
/** @param {string} archivedRelPath */
export function findWikiPagesForArchivedPath(archivedRelPath) {
  if (!existsSync(VAULT_DIR)) return [];
  const result = spawnSync(
    'grep',
    ['-rl', '-F', `source: "${archivedRelPath}"`, VAULT_DIR],
    { encoding: 'utf8' }
  );
  if (result.error) throw result.error;
  // grep exits 1 (no error) when nothing matches — only >1 is a real failure.
  if (result.status !== 0 && result.status !== 1) {
    throw new Error(`grep failed (status ${result.status}): ${result.stderr}`);
  }
  return result.stdout
    .split('\n')
    .filter(Boolean)
    .map((abs) => path.relative(REPO_ROOT, abs))
    .sort();
}

// Accepts a path with or without a leading "inbox/" and resolves it to an
// absolute path under inbox/. Throws with a clear message if it doesn't exist.
/** @param {string} inputPath */
export function resolveInboxPath(inputPath) {
  const stripped = inputPath.replace(/^inbox\//, '');
  const abs = path.join(INBOX_DIR, stripped);
  if (!existsSync(abs) || !statSync(abs).isFile()) {
    throw new Error(`No such file under inbox/: ${inputPath}`);
  }
  return abs;
}

// Given an absolute path under inbox/ or raw/, returns it if it exists,
// checking inbox/ first then raw/ (used by inbox:similar, which is
// useful both pre- and post-archiving).
/** @param {string} inputPath */
export function resolveInboxOrArchivePath(inputPath) {
  const strippedInbox = inputPath.replace(/^inbox\//, '');
  const inboxAbs = path.join(INBOX_DIR, strippedInbox);
  if (existsSync(inboxAbs) && statSync(inboxAbs).isFile()) return inboxAbs;

  const strippedArchive = inputPath.replace(/^raw\//, '');
  const archiveAbs = path.join(ARCHIVE_DIR, strippedArchive);
  if (existsSync(archiveAbs) && statSync(archiveAbs).isFile()) return archiveAbs;

  // Also accept an absolute path or a path already relative to the repo root.
  const asGiven = path.isAbsolute(inputPath) ? inputPath : path.join(REPO_ROOT, inputPath);
  if (existsSync(asGiven) && statSync(asGiven).isFile()) return asGiven;

  throw new Error(`No such file under inbox/ or raw/: ${inputPath}`);
}

export function currentYearMonth() {
  const d = new Date();
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}`;
}

// True if some vault/ page already has this stem — an archived
// file sharing a wiki page's basename makes every [[wikilink]] to that stem
// vault-wide ambiguous (markdownlint-obsidian resolves wikilinks against all
// *.md files, not just the lint-scoped ones), so raw/ must never reuse a
// live basename even though it isn't itself linted.
/**
 * @param {string} stem
 */
function collidesWithVaultBasename(stem) {
  for (const root of ['vault']) {
    const rootAbs = path.join(REPO_ROOT, root);
    if (!existsSync(rootAbs)) continue;
    const stack = [rootAbs];
    while (stack.length > 0) {
      const dir = stack.pop();
      if (dir === undefined) continue;
      for (const entry of readdirSync(dir, { withFileTypes: true })) {
        const p = path.join(dir, entry.name);
        if (entry.isDirectory()) stack.push(p);
        else if (entry.name.endsWith('.md') && path.basename(entry.name, '.md') === stem) return true;
      }
    }
  }
  return false;
}

// Moves absSrcPath (must be under inbox/) into raw/<YYYY-MM>/, suffixing
// the destination filename with the first 8 hex chars of `hash` whenever the
// plain name would collide — either with another file already in that
// archive dir, or with any live vault/ page's basename (see
// collidesWithVaultBasename). Returns the archive-relative destination path
// (e.g. "raw/2026-07/foo.md").
/**
 * @param {string} absSrcPath
 * @param {string} hash
 */
export function moveIntoArchive(absSrcPath, hash) {
  const yyyyMm = currentYearMonth();
  const destDir = path.join(ARCHIVE_DIR, yyyyMm);
  mkdirSync(destDir, { recursive: true });

  const base = path.basename(absSrcPath);
  const ext = path.extname(base);
  const stem = base.slice(0, base.length - ext.length);
  let destAbs = path.join(destDir, base);
  if (existsSync(destAbs) || collidesWithVaultBasename(stem)) {
    destAbs = path.join(destDir, `${stem}-${hash.slice(0, 8)}${ext}`);
  }

  renameSync(absSrcPath, destAbs);
  pruneEmptyDirsUpTo(path.dirname(absSrcPath), INBOX_DIR);

  return path.relative(REPO_ROOT, destAbs);
}

// Walks upward from `startDir` removing empty directories, stopping at (and
// never removing) `stopDir`.
/**
 * @param {string} startDir
 * @param {string} stopDir
 */
export function pruneEmptyDirsUpTo(startDir, stopDir) {
  let dir = startDir;
  while (dir !== stopDir && dir.startsWith(stopDir + path.sep)) {
    if (readdirSync(dir).length > 0) break;
    rmdirSync(dir);
    dir = path.dirname(dir);
  }
}

const MARKDOWN_COMPANION_SKIP_EXTENSIONS = new Set(['.md', '.markdown', '.txt']);

// PDFs get no markitdown-ts-generated companion: the underlying extraction
// only surfaces the PDF's static text layer, silently dropping filled-in
// form-field values on a fillable-form PDF (a character-sheet export is
// exactly this shape — inbox/CLAUDE.md). Callers that would auto-generate a
// companion (to-markdown.mjs, sweep-to-markdown.mjs) check this first and
// point to the `anthropic-skills:pdf` skill instead; this does NOT change
// companionMarkdownPath below, which archive.mjs still needs to locate and
// sweep up any pre-existing PDF companion when archiving the original.
/** @param {string} absPath */
export function isPdfPath(absPath) {
  return path.extname(absPath).toLowerCase() === '.pdf';
}

// Given an absolute path to any file, returns the absolute path its
// markitdown-generated sibling .md companion would have (same dir, same
// stem, .md extension) — regardless of whether that companion exists yet.
// Returns null for a file that is itself already markdown/text (it has no
// companion, it IS the terminal form).
/** @param {string} absPath */
export function companionMarkdownPath(absPath) {
  const ext = path.extname(absPath).toLowerCase();
  if (MARKDOWN_COMPANION_SKIP_EXTENSIONS.has(ext)) return null;
  return `${absPath.slice(0, absPath.length - path.extname(absPath).length)}.md`;
}

// Converts absPath to markdown via markitdown-ts and writes the result to
// its companion .md path (see companionMarkdownPath). Throws if absPath is
// already markdown/text, the companion already exists, or conversion fails
// or produces no content. Returns the absolute path written.
/** @param {string} absPath */
export async function convertToMarkdownCompanion(absPath) {
  const destAbs = companionMarkdownPath(absPath);
  if (!destAbs) throw new Error(`Already markdown/text, no companion to create: ${absPath}`);
  if (existsSync(destAbs)) throw new Error(`Refusing to overwrite existing file: ${destAbs}`);

  const { MarkItDown } = await import('markitdown-ts');
  const markitdown = new MarkItDown();
  const result = await markitdown.convert(absPath);
  if (!result || !result.markdown) throw new Error(`markitdown-ts produced no content for: ${absPath}`);

  writeFileSync(destAbs, result.markdown);
  return destAbs;
}

// --- SessionStart sweep failure cache -------------------------------------
// sweep-to-markdown.mjs (the SessionStart hook) skips re-attempting a file
// whose conversion already failed for its current content, so a file that
// can never convert here (missing system dependency like exiftool,
// genuinely unsupported format like .m4a, or a source markitdown-ts can't
// extract text from) doesn't pay a full markitdown-ts attempt on every
// single session start forever. Keyed by repo-relative path + an mtime+size
// signature, so editing/replacing the source file makes it retry. Deliberate
// on-demand conversion (`npm run inbox:to-md -- -f <path>`) never consults
// this cache — see to-markdown.mjs — it always attempts, per inbox/CLAUDE.md.
export const FAILURE_CACHE_PATH = path.join(REPO_ROOT, '.inbox-convert-failures.json');

/** @typedef {Record<string, { sig: string, message: string }>} FailureCache */

/** @returns {FailureCache} */
export function loadFailureCache() {
  try {
    return JSON.parse(readFileSync(FAILURE_CACHE_PATH, 'utf8'));
  } catch {
    return {};
  }
}

/** @param {FailureCache} cache */
export function saveFailureCache(cache) {
  try {
    writeFileSync(FAILURE_CACHE_PATH, `${JSON.stringify(cache, null, 2)}\n`);
  } catch {
    // best-effort — a write failure just means the next sweep retries
  }
}

/** @param {string} absPath */
function fileSignature(absPath) {
  const st = statSync(absPath);
  return `${st.mtimeMs}:${st.size}`;
}

/**
 * @param {string} absPath
 * @param {FailureCache} cache
 */
export function isKnownFailure(absPath, cache) {
  const entry = cache[path.relative(REPO_ROOT, absPath)];
  if (!entry) return false;
  try {
    return entry.sig === fileSignature(absPath);
  } catch {
    return false;
  }
}

/**
 * @param {string} absPath
 * @param {string} message
 * @param {FailureCache} cache
 */
export function recordFailure(absPath, message, cache) {
  try {
    cache[path.relative(REPO_ROOT, absPath)] = { sig: fileSignature(absPath), message };
  } catch {
    // ignore — if we can't stat it, we can't cache it; next sweep retries
  }
}

/**
 * @param {string} absPath
 * @param {FailureCache} cache
 * @returns {boolean} true if an entry existed and was removed
 */
export function clearFailure(absPath, cache) {
  const key = path.relative(REPO_ROOT, absPath);
  if (!(key in cache)) return false;
  delete cache[key];
  return true;
}

// Strips a leading YAML frontmatter block (--- ... ---) if present, returns
// the remaining body.
/** @param {string} content */
export function stripFrontmatter(content) {
  if (!content.startsWith('---\n') && content !== '---') return content;
  const end = content.indexOf('\n---', 4);
  if (end === -1) return content;
  const afterMarker = content.indexOf('\n', end + 1);
  return afterMarker === -1 ? '' : content.slice(afterMarker + 1);
}
