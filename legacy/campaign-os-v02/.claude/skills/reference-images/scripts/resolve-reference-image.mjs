#!/usr/bin/env node
// reference-images — resolve a content page's `reference_image` frontmatter
// field to a validated absolute filesystem path, ready to hand to
// `openrouter.sh image ... --reference <path>` as generation context.
//
// Usage:
//   node resolve-reference-image.mjs <page.md> [--vault-root <dir>]
//
// On success: prints the absolute path to stdout, exits 0.
// Field unset/empty ................. exit 3 (nothing to resolve — the field is optional)
// File missing at the resolved path . exit 4
// vault root undetectable ........... exit 5
// unsupported extension ............. exit 6 (openrouter.sh --reference takes png|jpg|jpeg|webp|gif)
// bad usage / unreadable page ....... exit 2
//
// vault-relative means "from the vault (git repo) root". Root is `--vault-root`
// when given, else the nearest ancestor of the page that contains `.git`.
// No dependencies — Node built-ins only, so no node_modules to install.
import { existsSync, readFileSync } from "node:fs";
import { dirname, extname, isAbsolute, resolve } from "node:path";

// openrouter.sh's own accepted set for --reference (svg is deliberately excluded —
// the image API rejects it). Keep in sync with that script's extension guard.
const SUPPORTED_EXTS = new Set(["png", "jpg", "jpeg", "webp", "gif"]);

function fail(code, message) {
  process.stderr.write(`${message}\n`);
  process.exit(code);
}

function parseArgs(argv) {
  let page;
  let vaultRoot;
  for (let i = 0; i < argv.length; i += 1) {
    const a = argv[i];
    if (a === "--vault-root") {
      vaultRoot = argv[i + 1];
      i += 1;
    } else if (a.startsWith("--vault-root=")) {
      vaultRoot = a.slice("--vault-root=".length);
    } else if (!page) {
      page = a;
    }
  }
  return { page, vaultRoot };
}

// Pull the `reference_image` scalar out of a page's leading YAML frontmatter.
// Returns the raw string value, or null when the block or field is absent/empty.
function readReferenceImageField(pageText) {
  if (!pageText.startsWith("---")) return null;
  const end = pageText.indexOf("\n---", 3);
  if (end === -1) return null;
  const block = pageText.slice(0, end);
  for (const line of block.split("\n")) {
    const m = /^reference_image:\s*(.*)$/.exec(line);
    if (!m) continue;
    return unwrapScalar(m[1]);
  }
  return null;
}

// Strip a trailing `# comment`, then surrounding quotes, then whitespace.
// Templates ship `reference_image: ""     # OPTIONAL — ...`; a set page ships a bare path.
function unwrapScalar(raw) {
  let v = raw.trim();
  if (v.startsWith('"') || v.startsWith("'")) {
    const q = v[0];
    const close = v.indexOf(q, 1);
    v = close === -1 ? v.slice(1) : v.slice(1, close);
  } else {
    const hash = v.indexOf("#");
    if (hash !== -1) v = v.slice(0, hash);
  }
  v = v.trim();
  return v.length === 0 ? null : v;
}

function findVaultRoot(startDir) {
  let dir = startDir;
  for (;;) {
    if (existsSync(resolve(dir, ".git"))) return dir;
    const parent = dirname(dir);
    if (parent === dir) return null;
    dir = parent;
  }
}

const { page, vaultRoot: vaultRootArg } = parseArgs(process.argv.slice(2));
if (!page) {
  fail(2, "usage: resolve-reference-image.mjs <page.md> [--vault-root <dir>]");
}

const pagePath = isAbsolute(page) ? page : resolve(process.cwd(), page);
if (!existsSync(pagePath)) fail(2, `page not found: ${pagePath}`);

let pageText;
try {
  pageText = readFileSync(pagePath, "utf8");
} catch (err) {
  fail(2, `cannot read page: ${err instanceof Error ? err.message : String(err)}`);
}

const field = readReferenceImageField(pageText);
if (field === null) fail(3, `no reference_image set on ${pagePath}`);

const vaultRoot = vaultRootArg
  ? resolve(process.cwd(), vaultRootArg)
  : findVaultRoot(dirname(pagePath));
if (!vaultRoot) {
  fail(5, `cannot locate vault root (no .git ancestor of ${pagePath}); pass --vault-root`);
}

const ext = extname(field).slice(1).toLowerCase();
if (!SUPPORTED_EXTS.has(ext)) {
  fail(
    6,
    `reference_image has unsupported extension .${ext || "(none)"} — openrouter.sh --reference takes ${[...SUPPORTED_EXTS].join(", ")}`,
  );
}

const abs = isAbsolute(field) ? field : resolve(vaultRoot, field);
if (!existsSync(abs)) fail(4, `reference_image points to missing file: ${abs}`);

process.stdout.write(`${abs}\n`);
