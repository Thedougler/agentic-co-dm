#!/usr/bin/env node
// Splice this repo's canonical qmd collections (utils/qmd-collections.yml) into the
// machine-local ~/.config/qmd/index.yml, leaving its `models:` block alone.
// ponytail: text splice on the two top-level blocks — no YAML dep for a 2-key file.
import { readFileSync, writeFileSync, existsSync } from "node:fs";
import { homedir } from "node:os";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const repo = join(dirname(fileURLToPath(import.meta.url)), "..", "..");
const target = join(homedir(), ".config", "qmd", "index.yml");

const canonical = readFileSync(join(repo, "utils", "qmd-collections.yml"), "utf8")
  .replace(/\{\{REPO\}\}/g, repo)
  .split("\n")
  .filter((l) => !l.startsWith("#"))
  .join("\n")
  .trim();

if (!existsSync(target)) {
  console.error(`no qmd config at ${target} — run 'qmd init' first`);
  process.exit(1);
}
const current = readFileSync(target, "utf8");
// keep everything from the first top-level key that isn't `collections:`
const tail = current.replace(/^collections:\n(?:[ \t].*\n|\n)*/m, "");
writeFileSync(target, `${canonical}\n${tail.trimStart()}`);
console.log(`synced ${target}`);
