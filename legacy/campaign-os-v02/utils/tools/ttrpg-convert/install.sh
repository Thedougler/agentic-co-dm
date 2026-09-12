#!/usr/bin/env bash
# Downloads the ttrpg-convert-cli native binary for this platform into
# utils/tools/ttrpg-convert/bin/. Re-run to reinstall/upgrade (edit VERSION).
set -euo pipefail

VERSION="3.3.3"
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

case "$(uname -s)-$(uname -m)" in
  Darwin-arm64)  ASSET="osx-aarch_64" ;;
  Darwin-x86_64) ASSET="osx-x86_64" ;;
  Linux-x86_64)  ASSET="linux-x86_64" ;;
  *) echo "Unsupported platform: $(uname -s)-$(uname -m)" >&2; exit 1 ;;
esac

URL="https://github.com/ebullient/ttrpg-convert-cli/releases/download/${VERSION}/ttrpg-convert-cli-${VERSION}-${ASSET}.zip"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

echo "Downloading ttrpg-convert-cli ${VERSION} (${ASSET})..."
curl -sL -o "$TMP/ttrpg-convert.zip" "$URL"
unzip -o -q "$TMP/ttrpg-convert.zip" -d "$TMP/extracted"

rm -rf "$DIR/bin"
mkdir -p "$DIR/bin"
cp "$TMP/extracted/ttrpg-convert-cli-${VERSION}-${ASSET}/bin/ttrpg-convert" "$DIR/bin/ttrpg-convert"
chmod +x "$DIR/bin/ttrpg-convert"

"$DIR/bin/ttrpg-convert" --version
echo "Installed to $DIR/bin/ttrpg-convert"
