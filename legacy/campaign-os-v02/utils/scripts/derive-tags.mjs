// Proposes Domain tags for pages that carry none (W27), derived from each
// page's own content — a spell's school and effect, a monster's creature
// type and habitat, an item's category and rarity line, a guide's subject.
// Never blankets a population with one role label: the vocabulary comes
// from docs/tags.md and the mapping below is per-page evidence, not a
// per-type constant (docs/adr/0034).
//
//   node utils/scripts/derive-tags.mjs              # propose, write TSV, change nothing
//   node utils/scripts/derive-tags.mjs --apply      # apply the proposal in place
//   node utils/scripts/derive-tags.mjs --path vault/srd/spells   # scope it
//
// Review the TSV before --apply. Pages the script cannot read confidently
// are reported as UNRESOLVED and left untouched for an agent pass.
import { readdirSync, statSync, readFileSync, writeFileSync } from "node:fs";
import { join, relative } from "node:path";

// Inlined from deleted ./lint-rules/lib/tags.mjs — loads docs/tags.md taxonomy
const TAGS_FILE = "docs/tags.md";
const GROUP_NAMES = ["Domain", "Meta", "Project"];
const VISIBILITY_PREFIX = "visibility/";

const HEADING_RE = /^(#{1,6})\s+(.*?)\s*$/;
const CANONICAL_BULLET_RE = /^- ([a-z0-9-]+)\s*$/;
const ALIAS_BULLET_RE = /^- ([a-z0-9-]+)\s*->\s*([a-z0-9-]+)\s*$/;
const BULLET_RE = /^-\s/;

function leadingWord(headingText) {
  return headingText.match(/^([A-Za-z0-9]+)/)?.[1] ?? "";
}

function slugSuggestion(text) {
  return text
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

/** @param {string} raw @returns {{ canonical: Set<string>, aliases: Map<string,string>, groups: Map<string,Set<string>>, entries: Array, issues: Array }} */
function parseTagsDoc(raw) {
  const canonical = new Set();
  const aliases = new Map();
  const groups = new Map(GROUP_NAMES.map((g) => [g, new Set()]));
  const entries = [];
  const issues = [];
  // token -> first line it was defined on (canonical bullet or alias source)
  const definedAt = new Map();

  let inCanonicalSection = false;
  let inAliasesSection = false;
  let currentGroup = null;

  const lines = raw.split("\n");
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const lineNumber = i + 1;
    const heading = line.match(HEADING_RE);

    if (heading) {
      const level = heading[1].length;
      const text = heading[2];
      if (level === 2) {
        inCanonicalSection = text === "Canonical tags";
        inAliasesSection = text === "Aliases";
        currentGroup = null;
        continue;
      }
      if (inCanonicalSection) {
        const word = leadingWord(text);
        if (GROUP_NAMES.includes(word)) {
          currentGroup = word;
        } else {
          currentGroup = null;
          issues.push({
            line: lineNumber,
            code: "C1",
            message: `"${text}" parses as a fourth tag group — the previous heading wrapped across source lines; join it back into one "### <Group> (…)" heading line`,
          });
        }
      }
      continue;
    }

    if (!BULLET_RE.test(line)) continue;

    // A bullet under "## Canonical tags" with no group heading above it is
    // still canonical (a minimal taxonomy — fixture vaults, a fresh repo —
    // may not use groups at all); it just belongs to no group.
    const section = inCanonicalSection ? (currentGroup ?? "Canonical") : inAliasesSection ? "Aliases" : null;

    if (section === null) {
      const stray = line.match(CANONICAL_BULLET_RE);
      if (stray) {
        issues.push({
          line: lineNumber,
          code: "C5",
          message: `"- ${stray[1]}" outside the tag sections matches the tag-entry shape — lib/tags.mjs would accept it as a live tag; reword or move it`,
        });
      }
      continue;
    }

    const canonicalMatch = line.match(CANONICAL_BULLET_RE);
    const aliasMatch = line.match(ALIAS_BULLET_RE);

    if (canonicalMatch) {
      const token = canonicalMatch[1];
      if (definedAt.has(token)) {
        issues.push({
          line: lineNumber,
          code: "C2",
          message: `"${token}" is defined twice (line ${definedAt.get(token)}) — delete one`,
        });
      } else {
        definedAt.set(token, lineNumber);
      }
      canonical.add(token);
      if (GROUP_NAMES.includes(section)) groups.get(section).add(token);
      entries.push({ token, kind: "canonical", target: null, line: lineNumber, section });
    } else if (aliasMatch) {
      const [, aliasToken, target] = aliasMatch;
      if (definedAt.has(aliasToken)) {
        issues.push({
          line: lineNumber,
          code: "C2",
          message: `"${aliasToken}" is defined twice (line ${definedAt.get(aliasToken)}) — delete one`,
        });
      } else {
        definedAt.set(aliasToken, lineNumber);
      }
      if (!aliases.has(aliasToken)) aliases.set(aliasToken, target);
      entries.push({ token: aliasToken, kind: "alias", target, line: lineNumber, section });
      if (!canonical.has(target) && !target.startsWith(VISIBILITY_PREFIX)) {
        issues.push({
          line: lineNumber,
          code: "C3",
          message: `alias "${aliasToken} -> ${target}" points at "${target}" which is not a canonical tag — repoint it at a tag under ### Domain/Meta/Project, or add "${target}" as a canonical bullet`,
        });
      }
    } else {
      const text = line.slice(2).trim();
      const suggestion = slugSuggestion(text);
      issues.push({
        line: lineNumber,
        code: "C4",
        message: `"- ${text}" does not parse as a tag entry — lib/tags.mjs drops it silently and every page using it then fails W13; rewrite as lowercase-hyphenated ("- ${suggestion}") or as an alias line ("- <x> -> <target>")`,
      });
    }
  }

  return { canonical, aliases, groups, entries, issues };
}

let tagTaxonomyCache = null;

/** @param {string} vaultRoot */
function loadTagTaxonomy(vaultRoot) {
  if (tagTaxonomyCache) return tagTaxonomyCache;
  let raw;
  try {
    raw = readFileSync(join(vaultRoot, TAGS_FILE), "utf8");
  } catch {
    tagTaxonomyCache = {
      accepted: new Set(),
      canonical: new Set(),
      aliases: new Map(),
      groups: new Map(GROUP_NAMES.map((g) => [g, new Set()])),
      entries: [],
      issues: [],
      path: TAGS_FILE,
    };
    return tagTaxonomyCache;
  }
  const { canonical, aliases, groups, entries, issues } = parseTagsDoc(raw);
  const accepted = new Set(canonical);
  for (const alias of aliases.keys()) accepted.add(alias);
  tagTaxonomyCache = { accepted, canonical, aliases, groups, entries, issues, path: TAGS_FILE };
  return tagTaxonomyCache;
}

const REPO_ROOT = process.cwd();
const MAX_TAGS = 5;
const OUT_TSV = "utils/scripts/.derive-tags.tsv";

const args = process.argv.slice(2);
const APPLY = args.includes("--apply");
const pathIdx = args.indexOf("--path");
const SCOPE = pathIdx !== -1 ? args[pathIdx + 1] : "vault";

// --- evidence tables -------------------------------------------------------
// Each maps one observable page fact to tones that fact genuinely implies.
// A school/creature-type/category is a distinct tone, not a shared bucket.

const SPELL_SCHOOL = {
  abjuration: ["arcane"],
  conjuration: ["arcane"],
  divination: ["mystery"],
  enchantment: ["intrigue"],
  evocation: ["combat"],
  illusion: ["stealth"],
  necromancy: ["undead"],
  transmutation: ["craft"],
};

// A spell's class list is stronger tone evidence than its school: school says
// how the magic works, class says whose story it belongs to. Cleric-and-
// paladin-only `bless` is faith, not the "intrigue" its enchantment school
// would imply.
const SPELL_CLASS = {
  cleric: "faith",
  paladin: "faith",
  druid: "nature",
  ranger: "nature",
  wizard: "arcane",
  sorcerer: "arcane",
  warlock: "arcane",
  bard: "intrigue",
  rogue: "stealth",
};

const CREATURE_TYPE = {
  undead: ["undead", "horror"],
  fiend: ["horror", "faith"],
  aberration: ["horror", "mystery"],
  beast: ["nature"],
  plant: ["nature"],
  fey: ["nature", "intrigue"],
  dragon: ["combat"],
  giant: ["combat"],
  monstrosity: ["combat", "horror"],
  humanoid: ["combat", "intrigue"],
  construct: ["craft"],
  elemental: ["arcane"],
  celestial: ["faith"],
  ooze: ["horror"],
  swarm: ["nature"],
};

// Matched against the item's `_Category, Rarity._` line, longest key first.
const ITEM_CATEGORY = {
  "wondrous item": ["arcane"],
  weapon: ["combat"],
  armor: ["combat"],
  shield: ["combat"],
  ammunition: ["combat"],
  potion: ["healing"],
  scroll: ["arcane"],
  ring: ["arcane"],
  rod: ["arcane"],
  staff: ["arcane"],
  wand: ["arcane"],
  document: ["mystery"],
  consumable: ["craft"],
  tool: ["craft"],
  instrument: ["craft"],
  vehicle: ["travel"],
  mount: ["travel"],
  gear: ["survival"],
};

// Subject signals, matched ONLY against a page's headline text (slug, title,
// summary) — never its body. Body mechanics vocabulary ("attack", "damage",
// "spell", "hit points") is uniform across SRD material and discriminates
// nothing; matching on it produces exactly the blanket tag docs/tags.md
// forbids. Terms here must name a subject, not a game mechanic.
const KEYWORDS = [
  [/\b(ship|sail|harbou?r|reef|tide|shoal|nautical|seafar|shipwreck|vessel|maritime|drown|boat|anchor)/i, "maritime"],
  [/\b(salvage|wreck|scuttl|derelict|scaveng)/i, "salvage"],
  [/\b(heal|cure|restor|revivif|regenerat|remedy|medicine|antitoxin|bandage)/i, "healing"],
  [/\b(undead|zombie|skeleton|wight|lich|ghoul|vampire|necroman|wraith|spectre|specter|mummy)/i, "undead"],
  [/\b(stealth|invisib|disguise|sneak|ambush|conceal|shadow|thieves|poison)/i, "stealth"],
  [/\b(forage|survival|wilderness|starv|exposure|weather|camp|rations|tent|climb)/i, "survival"],
  [/\b(craft|forge|smith|artisan|tinker|repair|construct|tools?\b|kit\b)/i, "craft"],
  [/\b(temple|priest|god|divine|prayer|shrine|holy|cleric|paladin|worship|celestial)/i, "faith"],
  [/\b(beast|animal|forest|jungle|plant|druid|ranger|swarm|vermin|fey|elemental)/i, "nature"],
  [/\b(trap|dungeon|cavern|explor|ruin|delve|lair|tomb|crypt|chamber|mines?\b)/i, "exploration"],
  [/\b(heist|steal|thief|burglar|smuggl)/i, "heist"],
  [/\b(noble|court|council|treaty|senate|politic|guild|charter|magistrate)/i, "politics"],
  [/\b(murder|clue|riddle|puzzle|secret|myster|cipher|omen)/i, "mystery"],
  [/\b(war|army|siege|battle|soldier|militia|warband)/i, "war"],
  [/\b(travel|journey|voyage|road|route|caravan|mount\b|steed)/i, "travel"],
  [/\b(horror|terror|dread|grotesque|nightmare|corpse|rot\b|blight)/i, "horror"],
  [/\b(arcane|wizard|sorcer|warlock|rune|glyph|eldritch|enchanted)/i, "arcane"],
  [/\b(duel|brawl|gladiat|mercenary|weaponmaster|champion|minion|boss)/i, "combat"],
  [/\b(joke|farce|comic|absurd|drunk|prank|revel)/i, "comedy"],
  [/\b(romance|lover|courtship|marriage|beloved)/i, "romance"],
  [/\b(bribe|blackmail|spy|informant|scheme|betray|rumour|rumor|conspir)/i, "intrigue"],
];

// --- helpers ---------------------------------------------------------------

function* walk(dir) {
  let entries;
  try {
    entries = readdirSync(dir);
  } catch {
    return;
  }
  for (const entry of entries) {
    // _templates/ is lint-ignored and its tags propagate to every page made
    // from it — a template's tags are authored by hand, never derived.
    if (entry.startsWith(".") || entry === "_templates") continue;
    const p = join(dir, entry);
    let st;
    try {
      st = statSync(p);
    } catch {
      continue;
    }
    if (st.isDirectory()) yield* walk(p);
    else if (p.endsWith(".md")) yield p;
  }
}

function splitFrontmatter(raw) {
  const m = raw.match(/^---\n([\s\S]*?)\n---\n?/);
  if (!m) return null;
  return { fmRaw: m[1], fmBlock: m[0], body: raw.slice(m[0].length) };
}

function fmValue(fmRaw, key) {
  const line = fmRaw.split("\n").find((l) => l.startsWith(`${key}:`));
  if (line === undefined) return null;
  return line.slice(key.length + 1).trim().replace(/^["']|["']$/g, "");
}

function hasTags(fmRaw) {
  const lines = fmRaw.split("\n");
  const i = lines.findIndex((l) => l.startsWith("tags:"));
  if (i === -1) return { present: false, empty: true, line: -1 };
  const inline = lines[i].match(/^tags:\s*\[(.*)\]\s*$/);
  if (inline) {
    const vals = inline[1].split(",").map((s) => s.trim()).filter(Boolean);
    const subject = vals.filter((v) => !v.replace(/^["']|["']$/g, "").startsWith("visibility/"));
    return { present: true, empty: subject.length === 0, line: i, inline: true };
  }
  const bullets = [];
  for (let j = i + 1; j < lines.length && /^\s*-\s+\S/.test(lines[j]); j++) {
    bullets.push(lines[j].replace(/^\s*-\s+/, "").trim());
  }
  const subject = bullets.filter((v) => !v.replace(/^["']|["']$/g, "").startsWith("visibility/"));
  return { present: true, empty: subject.length === 0, line: i, inline: false, bulletCount: bullets.length };
}

/** The statblock fence's own `type:` — a monster's creature type, not the page type. */
function creatureType(body) {
  const m = body.match(/^type:\s*"?([a-z ]+?)"?\s*$/im);
  if (!m) return null;
  const raw = m[1].trim().toLowerCase();
  if (raw === "monster") return null;
  const word = Object.keys(CREATURE_TYPE).find((k) => raw.includes(k));
  return word ?? null;
}

function itemCategory(body) {
  const m = body.match(/^_([^,._]+)[,.]/m);
  if (!m) return null;
  const line = m[1].toLowerCase();
  const keys = Object.keys(ITEM_CATEGORY).sort((a, b) => b.length - a.length);
  return keys.find((k) => line.includes(k)) ?? null;
}

function keywordTones(text, limit) {
  const hits = [];
  for (const [re, tag] of KEYWORDS) {
    if (hits.length >= limit) break;
    if (re.test(text)) hits.push(tag);
  }
  return hits;
}

/** Evidence-first, keywords only to fill remaining slots. */
function derive(fmRaw, body, relPath) {
  const type = fmValue(fmRaw, "type");
  const subtype = (fmValue(fmRaw, "subtype") ?? "").toLowerCase();
  const summary = fmValue(fmRaw, "summary") ?? "";
  // Headline text only — the page's own slug, H1 and summary. The repo path
  // is deliberately excluded: every path contains "vault", which would match
  // a keyword and blanket the whole corpus.
  const slug = (relPath.split("/").pop() ?? "").replace(/\.md$/, "").replace(/-/g, " ");
  const h1 = body.match(/^#\s+(.+)$/m)?.[1] ?? "";
  const head = `${slug} ${h1} ${summary}`;

  let seed = [];
  let basis = "keyword";

  if (type === "spell" && SPELL_SCHOOL[subtype]) {
    // Classes that can cast it, deduped in declaration order, then the
    // school as the backstop for a spell every class shares.
    const levelLine = body.match(/^\*\*Level:\*\*.*$/m)?.[0] ?? "";
    const classes = Object.keys(SPELL_CLASS).filter((c) => new RegExp(`\\b${c}\\b`, "i").test(levelLine));
    const classTones = [...new Set(classes.map((c) => SPELL_CLASS[c]))];
    seed = classTones.length > 0 ? classTones.slice(0, 2) : [...SPELL_SCHOOL[subtype]];
    // These four schools name what the spell does in a way the class list
    // cannot; the rest (abjuration/conjuration/transmutation/enchantment)
    // only restate a tone the class already carries.
    if (classTones.length > 0 && ["evocation", "necromancy", "illusion", "divination"].includes(subtype)) {
      const schoolTone = SPELL_SCHOOL[subtype][0];
      if (!seed.includes(schoolTone)) seed.push(schoolTone);
    }
    basis = classTones.length > 0 ? `spell:${classes.join("+")}/${subtype}` : `school:${subtype}`;
  } else if (type === "monster" || type === "creature") {
    const ct = creatureType(body);
    if (ct) {
      seed = [...CREATURE_TYPE[ct]];
      basis = `creature:${ct}`;
    } else {
      seed = ["combat"];
      basis = "creature:unknown";
    }
  } else if (type === "item") {
    const cat = itemCategory(body);
    if (cat) {
      seed = [...ITEM_CATEGORY[cat]];
      basis = `item:${cat}`;
    }
  }

  const tags = [...seed];
  for (const t of keywordTones(head, MAX_TAGS)) {
    if (!tags.includes(t) && tags.length < MAX_TAGS) tags.push(t);
  }
  return { tags: tags.slice(0, MAX_TAGS), basis, type };
}

function applyTags(fmRaw, body, tagState, tags) {
  const lines = fmRaw.split("\n");
  const rendered = `tags: [${tags.join(", ")}]`;
  if (!tagState.present) {
    lines.push(rendered);
  } else if (tagState.inline) {
    lines[tagState.line] = rendered;
  } else {
    lines.splice(tagState.line, 1 + (tagState.bulletCount ?? 0), rendered);
  }
  return `---\n${lines.join("\n")}\n---\n${body}`;
}

// --- main ------------------------------------------------------------------

const taxonomy = loadTagTaxonomy(REPO_ROOT);
const canonical = taxonomy.canonical;

const rows = [];
const unresolved = [];
let applied = 0;

for (const abs of walk(join(REPO_ROOT, SCOPE))) {
  const relPath = relative(REPO_ROOT, abs);
  const raw = readFileSync(abs, "utf8");
  const split = splitFrontmatter(raw);
  if (!split) continue;
  const { fmRaw, body } = split;
  if (!fmValue(fmRaw, "type")) continue; // W84's job
  if (fmValue(fmRaw, "subtype") === "ingest-review") continue;

  const tagState = hasTags(fmRaw);
  if (!tagState.empty) continue;

  const { tags, basis, type } = derive(fmRaw, body, relPath);
  const bad = tags.filter((t) => !canonical.has(t));
  if (bad.length > 0) throw new Error(`derived a tag outside docs/tags.md: ${bad.join(",")} on ${relPath}`);

  if (tags.length === 0) {
    unresolved.push(`${relPath}\t${type}`);
    continue;
  }

  rows.push(`${relPath}\t${type}\t${basis}\t${tags.join(",")}`);

  if (APPLY) {
    writeFileSync(abs, applyTags(fmRaw, body, tagState, tags));
    applied += 1;
  }
}

writeFileSync(
  join(REPO_ROOT, OUT_TSV),
  `path\ttype\tbasis\ttags\n${rows.join("\n")}\n${unresolved.map((u) => `${u}\tUNRESOLVED\t`).join("\n")}\n`,
);

const dist = new Map();
for (const r of rows) {
  for (const t of r.split("\t")[3].split(",")) dist.set(t, (dist.get(t) ?? 0) + 1);
}
const sorted = [...dist.entries()].sort((a, b) => b[1] - a[1]);

console.log(`${APPLY ? "APPLIED" : "PROPOSED"}: ${rows.length} page(s); UNRESOLVED: ${unresolved.length}`);
if (APPLY) console.log(`wrote ${applied} file(s)`);
console.log(`TSV: ${OUT_TSV}`);
console.log("tag distribution over proposed pages:");
for (const [tag, n] of sorted) {
  console.log(`  ${String(n).padStart(5)} ${tag}  (${((n / rows.length) * 100).toFixed(1)}%)`);
}
