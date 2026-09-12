#!/usr/bin/env node
// count:lines — prints the raw line count (wc -l semantics) for one or
// more files, plus the prose-only count W12/W89 use for reference.
// Informational only, no lint rule gates this.
import { readFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const REPO_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');

// ============================================================================
// Inlined from utils/scripts/lint-rules/lib/fences.mjs
// ============================================================================

const FENCE_LINE = /^\s*(`{3,}|~{3,})(.*)$/;
const CLOSING_ONLY = /^\s*(`+|~+)\s*$/;

/**
 * @param {string[]} lines
 * @returns {boolean[]} same length as `lines`; true if that line is inside
 *   (or is the opening/closing delimiter of) a fenced code block.
 */
function fencedLineFlags(lines) {
  const flags = Array.from({ length: lines.length }, () => false);
  /** @type {{ char: string, len: number } | null} */
  let open = null;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    if (open === null) {
      const m = line.match(FENCE_LINE);
      if (m) {
        open = { char: m[1][0], len: m[1].length };
        flags[i] = true;
      }
      continue;
    }

    flags[i] = true;
    const close = line.match(CLOSING_ONLY);
    if (close && close[1][0] === open.char && close[1].length >= open.len) {
      open = null;
    }
  }

  return flags;
}

// ============================================================================
// Inlined from utils/scripts/lint-rules/lib/corpusStats.mjs
// ============================================================================

/**
 * Count raw physical lines in a file's full text, matching `wc -l`
 * semantics exactly (a trailing newline is not an extra empty line) —
 * unlike countProseLines below, nothing is excluded.
 * @param {string} raw
 */
function countRawLines(raw) {
  const lines = raw.split("\n");
  if (lines.length > 0 && lines[lines.length - 1] === "") lines.pop();
  return lines.length;
}

/**
 * Count PROSE lines in a span of markdown lines — the verbosity measure
 * W12/W89 compare against neighbours. Excluded as data, not prose: blank
 * lines, fence delimiters and everything inside a fence (statblocks, shell
 * blocks), table rows (`|`-led), and HTML-comment-only lines. A section
 * that is one big statblock or price table measures near zero — length
 * rules exist to trim verbosity, and data density is not verbosity.
 * @param {readonly string[]} lines
 */
function countProseLines(lines) {
  let count = 0;
  const fenced = fencedLineFlags(lines);
  for (let i = 0; i < lines.length; i++) {
    if (fenced[i]) continue;
    const trimmed = lines[i].trim();
    if (trimmed === "") continue;
    if (trimmed.startsWith("|")) continue;
    if (/^<!--.*-->$/.test(trimmed)) continue;
    count += 1;
  }
  return count;
}

const files = process.argv.slice(2);
if (files.length === 0) {
  console.error('Usage: npm run count:lines -- <file.md> [file2.md ...]');
  process.exit(1);
}

for (const file of files) {
  const abs = path.resolve(file);
  let raw;
  try {
    raw = readFileSync(abs, 'utf8');
  } catch (err) {
    console.error(`${file}: cannot read (${err.message})`);
    continue;
  }
  const rawCount = countRawLines(raw);
  const prose = countProseLines(raw.split('\n'));
  const rel = path.relative(REPO_ROOT, abs);
  console.log(`${rel}: ${rawCount} lines (${prose} prose)`);
}
