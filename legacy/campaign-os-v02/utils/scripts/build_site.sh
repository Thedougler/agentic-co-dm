#!/usr/bin/env bash
# build_site.sh — strip -> quartz build -> leak_check
#
# Contract: sys/runbooks/publish.md
# Runbook: sys/runbooks/publish.md (Phase 7, step 3)
#
# This script implements layers 2 and 3 of the three-layer publish defense
# (layer 1, ExplicitPublish, lives in site/quartz.config.ts):
#
#   1. Page opt-in       — Quartz's ExplicitPublish filter (site/quartz.config.ts)
#   2. Section strip      — THIS SCRIPT: copies publish:true pages to a staging
#                            dir, deletes every DM-only section (any H2/H3
#                            whose heading text contains "dm only"
#                            case-insensitive, e.g. `## DM Only`, `## Arc
#                            Notes (DM Only)`, `## dm only` — stripped from
#                            the heading to the next heading of the
#                            same-or-higher level) and every `%%...%%`
#                            comment, then builds Quartz from the staging
#                            copy. The vault files under vault/ are never
#                            written to — strip happens on the copy only.
#   3. Leak check         — THIS SCRIPT invokes utils/scripts/leak_check.py (if it
#                            exists) against the built HTML and prints its
#                            PUBLISH-CHECK: PASS/FAIL block. If leak_check.py
#                            has not been implemented yet, this script prints
#                            a loud WARNING instead of faking a PASS — a build
#                            that skipped layer 3 is not deploy-safe.
#
# Usage:
#   scripts/build_site.sh                 # build from the real vault (repo root)
#   CAMPAIGN_ROOT=/path/to/fixture-vault scripts/build_site.sh
#                                          # build from a fixture vault instead,
#                                          # for acceptance testing — never point
#                                          # this at anything you don't want
#                                          # treated as the vault to publish.
#   BUILD_SITE_OUTPUT=/tmp/out scripts/build_site.sh
#                                          # override the output dir (default
#                                          # site/public)
#
# Exit codes: 0 = built (see output for whether leak_check ran and passed);
# 1 = quartz build failed; 2 = leak_check.py found a leak (PUBLISH-CHECK: FAIL).

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# SITE_DIR is always the real Quartz install — the fixture override below
# only changes where content is *read from*, never where Quartz itself lives.
SITE_DIR="$REPO_ROOT/utils/site"

# CAMPAIGN_ROOT lets acceptance tests point the content scan at a fixture
# vault (with its own vault/ sys/secrets.md) without
# ever writing fixture pages into the real vault. Defaults to the repo root.
ROOT_DIR="$(cd "${CAMPAIGN_ROOT:-$REPO_ROOT}" && pwd)"

OUTPUT_DIR="${BUILD_SITE_OUTPUT:-$SITE_DIR/public}"
STAGING_DIR="$(mktemp -d "${TMPDIR:-/tmp}/campaign-os-publish.XXXXXX")"

cleanup() { rm -rf "$STAGING_DIR"; }
trap cleanup EXIT

echo "build_site.sh: vault root   $ROOT_DIR"
echo "build_site.sh: staging dir  $STAGING_DIR"
echo "build_site.sh: output dir   $OUTPUT_DIR"

# --- Layer 2: copy publish:true pages into staging, stripping DM Only + %%...%% ---
# Vault files are read-only from this point on; every write below targets
# $STAGING_DIR, never $ROOT_DIR.
COPIED_COUNT="$(python3 - "$ROOT_DIR" "$STAGING_DIR" <<'PYEOF'
import re
import sys
from pathlib import Path

root = Path(sys.argv[1])
staging = Path(sys.argv[2])

# Everything that may legitimately carry publish: true. Structurally-secret
# trees (docs/, scripts/, .claude/, sessions ledgers/transcripts) are
# never scanned at all — enforced here, and again by Quartz's ignorePatterns.
SOURCE_DIRS = ["vault"]

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
PUBLISH_TRUE_RE = re.compile(r"^publish:\s*true\s*$", re.MULTILINE)
COMMENT_RE = re.compile(r"%%.*?%%", re.DOTALL)

# A DM-only section is any H2/H3 whose heading text contains "dm only"
# case-insensitive (covers "## DM Only", "## Arc Notes (DM Only)", and
# "## dm only" typos), stripped from the heading to the next heading of the
# same-or-higher level: an H2 DM-only section runs to the next H2 (or end of
# file), an H3 DM-only section runs to the next H3-or-H2 (or end of file) so
# it never swallows a following player-facing H3.
HEADING_RE = re.compile(r"^(#{2,3})[ \t]+([^\n]*)\r?\n", re.MULTILINE)


def strip_dm_only(body):
    headings = [
        (len(m.group(1)), m.group(2), m.start(), m.end())
        for m in HEADING_RE.finditer(body)
    ]

    ranges = []
    for idx, (level, text, start, _end) in enumerate(headings):
        if "dm only" not in text.lower():
            continue
        section_end = len(body)
        for level2, _text2, start2, _end2 in headings[idx + 1:]:
            if level2 <= level:
                section_end = start2
                break
        ranges.append((start, section_end))

    if not ranges:
        return body

    ranges.sort()
    merged = [list(ranges[0])]
    for start, end in ranges[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    out = []
    prev_end = 0
    for start, end in merged:
        out.append(body[prev_end:start])
        prev_end = end
    out.append(body[prev_end:])
    return "".join(out)

copied = []
for source_dir in SOURCE_DIRS:
    src_root = root / source_dir
    if not src_root.is_dir():
        continue
    for md_path in sorted(src_root.rglob("*.md")):
        text = md_path.read_text(encoding="utf-8")
        m = FRONTMATTER_RE.match(text)
        if not m or not PUBLISH_TRUE_RE.search(m.group(1)):
            continue

        body = text[m.end():]
        body = strip_dm_only(body)
        body = COMMENT_RE.sub("", body)
        stripped = text[:m.end()] + body

        rel = md_path.relative_to(root)
        dest = staging / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(stripped, encoding="utf-8")
        copied.append(str(rel))

for rel in copied:
    print(f"build_site.sh:   + {rel}", file=sys.stderr)
print(len(copied))
PYEOF
)"

echo "build_site.sh: staged $COPIED_COUNT publish:true page(s)"
if [ "$COPIED_COUNT" -eq 0 ]; then
  echo "build_site.sh: no publish:true pages found — building an empty site."
fi

# --- Layer 1 + build: quartz build from the staging copy ---
# ExplicitPublish (site/quartz.config.ts) re-checks publish:true on top of
# the pre-filtered staging copy — belt and suspenders, same as ignorePatterns.
( cd "$SITE_DIR" && npx quartz build -d "$STAGING_DIR" -o "$OUTPUT_DIR" )

# --- Layer 3: leak check on built output ---
LEAK_CHECK="$REPO_ROOT/utils/scripts/leak_check.py"
if [ -f "$LEAK_CHECK" ]; then
  if ! python3 "$LEAK_CHECK" "$OUTPUT_DIR" --secrets "$ROOT_DIR/sys/secrets.md"; then
    exit 2
  fi
else
  cat <<'WARN'
PUBLISH-CHECK: SKIPPED — utils/scripts/leak_check.py does not exist yet (layer 3
not implemented). This build has NOT been checked against
sys/secrets.md, `DM Only`, `%%`, `status: pending`, or
`CONTRADICTION` markers in the output. Do not treat site/public/ as
deploy-safe until leak_check.py exists and this script has been re-run.
WARN
fi

echo "build_site.sh: done. Output at $OUTPUT_DIR"
