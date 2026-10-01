#!/bin/sh
# Validate the plugin and build the directory submission ZIP into dist/.
set -eu
root="$(cd "$(dirname "$0")/.." && pwd)"
plugin="$root/plugins/happy-memes"
version="$(python3 -c "import json,sys; print(json.load(open(sys.argv[1]))['version'])" "$plugin/.codex-plugin/plugin.json")"
zip_path="$root/dist/happy-memes-$version.zip"

mkdir -p "$root/dist"
rm -f "$zip_path"
# The OpenAI package is only the Codex manifest, skills, and assets; the Muse manifest stays in the repo.
(cd "$plugin" && zip -r -X -q "$zip_path" .codex-plugin skills assets -x '*.DS_Store')
python3 "$root/scripts/validate.py" "$plugin" "$zip_path"
echo "$zip_path"
