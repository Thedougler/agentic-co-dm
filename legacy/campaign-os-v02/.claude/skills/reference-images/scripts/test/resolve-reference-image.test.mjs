import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { mkdtempSync, mkdirSync, writeFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { fileURLToPath } from "node:url";
import { after, before, test } from "node:test";

const SCRIPT = fileURLToPath(new URL("../resolve-reference-image.mjs", import.meta.url));

let root;

function run(args) {
  try {
    const stdout = execFileSync("node", [SCRIPT, ...args], { encoding: "utf8" });
    return { code: 0, stdout: stdout.trim() };
  } catch (err) {
    return { code: err.status, stdout: (err.stdout ?? "").trim(), stderr: (err.stderr ?? "").trim() };
  }
}

function page(name, frontmatter) {
  const p = join(root, name);
  writeFileSync(p, `---\ntype: npc\n${frontmatter}\n---\n\n# Test\n`);
  return p;
}

before(() => {
  root = mkdtempSync(join(tmpdir(), "refimg-"));
  mkdirSync(join(root, "_assets", "reference"), { recursive: true });
  writeFileSync(join(root, "_assets", "reference", "branca-reference.jpg"), "not-a-real-jpeg");
});

after(() => rmSync(root, { recursive: true, force: true }));

test("resolves a set field to an absolute existing path", () => {
  const p = page("set.md", 'reference_image: _assets/reference/branca-reference.jpg');
  const r = run([p, "--vault-root", root]);
  assert.equal(r.code, 0);
  assert.equal(r.stdout, join(root, "_assets", "reference", "branca-reference.jpg"));
});

test("strips a quoted value and a trailing comment (template default line)", () => {
  const p = page("commented.md", 'reference_image: "_assets/reference/branca-reference.jpg"   # OPTIONAL — note');
  const r = run([p, "--vault-root", root]);
  assert.equal(r.code, 0);
  assert.equal(r.stdout, join(root, "_assets", "reference", "branca-reference.jpg"));
});

test("empty template field exits 3 (nothing to resolve)", () => {
  const p = page("empty.md", 'reference_image: ""     # OPTIONAL — vault-relative path');
  assert.equal(run([p, "--vault-root", root]).code, 3);
});

test("absent field exits 3", () => {
  const p = page("absent.md", "tags: []");
  assert.equal(run([p, "--vault-root", root]).code, 3);
});

test("missing target file exits 4", () => {
  const p = page("missing.md", "reference_image: _assets/reference/nope.png");
  assert.equal(run([p, "--vault-root", root]).code, 4);
});

test("unsupported extension exits 6", () => {
  const p = page("svg.md", "reference_image: _assets/reference/branca-reference.svg");
  assert.equal(run([p, "--vault-root", root]).code, 6);
});

test("bad usage (no page arg) exits 2", () => {
  assert.equal(run([]).code, 2);
});
