# Muse Code plugin research (as of 2026-10-01)

Muse Code latest in changelog: **1.4.2**. Official Meta docs (dev.meta.ai/docs/muse-code/*) cover skills, hooks, MCP,
but I could NOT retrieve a plugin-manifest/marketplace spec from them (the fetched `extending` page was truncated before any
plugin section; the changelog only mentions plugins in passing). Everything below on manifest shape is **derived from real repos**
that pass `muse plugins validate`, not from a Meta spec.

## 1. Manifest: `.muse-plugin/plugin.json`
Skills go under `capabilities.skills` as an array of objects `{id, path, enabledDefault?}`, NOT a top-level `skills` string.
`path` points at the SKILL.md file (relative to repo root). Minimal single-skill manifest (browserbase/browse-plugin PR #5, validated on Muse 1.3.0):
```json
{
  "schemaVersion": 1,
  "name": "meme",
  "displayName": "Meme",
  "version": "0.1.0",
  "description": "...",
  "compat": { "source": "native", "manifestDir": ".muse-plugin" },
  "capabilities": {
    "skills": [
      { "id": "meme", "path": "skills/meme/SKILL.md", "enabledDefault": true }
    ],
    "commands": [],
    "hooks": [],
    "mcpServers": [],
    "reminders": []
  }
}
```
- yowcow/dude's manifest omits `enabledDefault`, `commands`, `mcpServers`, `reminders`, so those are optional. Hook shape there:
  `{"id":"session-start","event":"SessionStart","command":["sh","hooks/session-start"],"timeoutMs":5000}`.
- MCP server shape (sonilo): `{"id":"sonilo","transport":"http","url":"https://api.sonilo.com/mcp"}`.
- Installed skill id becomes `plugin:<name>:<skill-id>` (e.g. `plugin:browse:browse`); list with `muse skills list --source plugin`.
- **Icon/logo field: UNVERIFIED, no evidence one exists.** None of the three reference manifests (browse, sonilo, dude) use one. Safest: omit it from the Muse manifest; test an extra field with `muse plugins validate .` before relying on it (unknown-field behaviour unknown).
- Required vs optional fields: not formally verified. Safe set = schemaVersion, name, displayName, version, description, compat, capabilities.skills.
- Claude-style `"skills": "./skills/"` text field: I found no report of Muse's exact error; the native manifest above sidesteps it. Muse can also read Claude/Codex manifests as fallback (`manifest_family`: native|claude|codex per browse docs) but the native one wins when present.

## 2. marketplace.json and install
- Muse **accepts the existing `.agents/plugins/marketplace.json`** (browse docs, verified by Browserbase on 1.3.0). It also supports `.muse-plugin/marketplace.json`, Claude-like shape (yowcow/dude PR #478):
```json
{
  "name": "meme",
  "description": "Meme plugin marketplace",
  "owner": { "name": "Your Name", "email": "you@example.com" },
  "plugins": [
    { "name": "meme", "description": "...", "version": "0.1.0", "source": "./",
      "author": { "name": "Your Name", "email": "you@example.com" } }
  ]
}
```
  No top-level version; version lives in `plugins[].version`.
- Commands (browse docs, sonilo PR #29):
```
muse plugins validate . [--json]            # may need MUSE_EXPERIMENTAL_PLUGINS=on|1
muse plugins install . --scope user          # local checkout
muse plugins marketplace add <name> <git-url-or-abs-path>
muse plugins install <plugin>@<marketplace>
muse plugins approve <plugin>                # activates third-party MCP servers/hooks; skills are active on install
muse plugins inspect|enable|disable|update|remove <plugin>
muse plugins marketplace update <name>
muse skills list --source plugin
```
- Gating: sonilo README says plugin management is behind `MUSE_EXPERIMENTAL_PLUGINS` "as of Muse Code 1.4.0" (already-installed plugins run without the flag). Builds <=1.1.1 and at least one 1.3.0 build report plugins unavailable. Still experimental, so expect change.
- No-plugin fallback: official docs say Muse auto-discovers skills from `~/.agents/skills`, `~/.claude/skills`, `$CODEX_HOME/skills`, and project `.agents/skills/<id>/SKILL.md`, `.claude/skills`, `.codex/skills`; also `muse skills install ./skills/meme --scope user`. A plain skills repo works with zero Muse manifest (https://dev.meta.ai/docs/muse-code/extending).

## 3. Official directory / submission
- **No official Meta Muse Code plugin directory or store found.** Plugin docs aren't visibly public on dev.meta.ai. (The consumer Muse app has a separate "Connector Platform", muse.ai/platform, for connectors; different product, relevance unverified.)
- Best distribution: public GitHub repo that doubles as marketplace -> users run
  `muse plugins marketplace add meme https://github.com/<you>/<repo>` then `muse plugins install meme@meme`.
- Community: MuseDirectory (musedirectory.dev, states "Not affiliated with Meta") lists plugins/skills/marketplaces; submit via /submit.html (form generates JSON to email hello@musedirectory.dev or paste in a PR). Manual curation, no guarantees.
- Skill-only alternative: `npx skills add <owner>/<repo>` (agentskills.io spec), as Sonilo also ships.

## 4. Coexistence with a Codex manifest
Yes, in practice. yowcow/dude ships `.claude-plugin/`, `.codex-plugin/`, `.muse-plugin/`, `.agents/plugins/marketplace.json`; browserbase/browse-plugin ships root `plugin.json` (Open Plugin spec) + `.claude-plugin`, `.cursor-plugin`, `.grok-plugin`, `.muse-plugin`, `.agents/plugins/marketplace.json`, `gemini-extension.json`. Muse 1.3.0 result: `valid: true` plus two non-blocking warnings: `ignored-root-manifest` (root plugin.json ignored) and `multiple-manifests` (picks native `.muse-plugin` over Claude/Codex). Install and skill discovery unaffected. So a root `plugin.json` with `extensions.com.openai` or `.codex-plugin/plugin.json` is fine; share one `skills/meme/SKILL.md`. Keep versions in sync across manifests (browse uses scripts/sync-version.mjs). `muse skills validate` treats SKILL.md `allowed-tools` as advisory (info only).

## Sources
- https://github.com/browserbase/browse-plugin/pull/5 (+ docs/muse-code.md on main)
- https://github.com/sonilo-ai/skills/pull/29
- https://github.com/yowcow/dude/pull/478 (issues 476/479)
- https://dev.meta.ai/docs/muse-code , /extending , /changelog
- https://blog.fsck.com/2026/09/29/I-asked-muse-to-tell-me-about-updates-to-its-skills/ (only mirrors muse's built-in skills at github.com/obra/muse-skills; nothing on plugins)
- https://www.musedirectory.dev/submit.html
- Surfaced by search only, not fetched: oh-my-musecode, fulcrumaxe PR #219, muse-code-acp-plugin

## Flags (unverified)
- Icon/logo field; formal required-field list; official Meta plugin docs; Muse's exact error on a text `skills` field.
- No muse binary was run (sandbox network blocked). Recommend: `curl -fsSL https://dev.meta.ai/install.sh | sh`, then `MUSE_EXPERIMENTAL_PLUGINS=1 muse plugins validate .` on the final repo.
