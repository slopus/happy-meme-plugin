# Memes: submission runbook

Nothing has been submitted. Everything below is ready to run by hand.

## Package

```
.agents/plugins/marketplace.json   lets `codex plugin marketplace add` / Muse install from the repo
plugins/happy-memes/               plugin root
├── .codex-plugin/plugin.json      ChatGPT + Codex manifest (the format the portal normalizes to)
├── .muse-plugin/plugin.json       Muse Code manifest (native shape; Muse ignores the Codex one)
├── skills/meme/SKILL.md           the skill (≈50 lines)
└── assets/logo.png (1024²), composer-icon.png (256²)   Happy bot face: DiceBear Adventurer Neutral, seed "memes-face-04"
dist/happy-memes-<version>.zip     submission ZIP (not committed): only .codex-plugin, skills, assets
```

Rebuild and validate the ZIP after edits. Bump `version` in both manifests first, since re-uploading an unchanged version is flagged:

```sh
scripts/build.sh
```

Verified locally with Codex CLI 0.159.2 using an isolated `CODEX_HOME`: `codex plugin marketplace add <repo>` and `codex plugin add happy-memes@happy-meme-plugin` both work, and the skill shows up to the model as `happy-memes:meme`. All documented listing limits pass (`scripts/validate.py`).

## OpenAI (ChatGPT + Codex directory)

Docs: https://developers.openai.com/plugins/deploy/submission · limits: https://developers.openai.com/plugins/deploy/submission-errors · policy: https://developers.openai.com/plugins/plugin-guidelines

1. **Identity.** In platform.openai.com → Settings → Organization → General, finish individual or business verification. The listing's developer name comes from this identity, whatever the ZIP says. You need to be an org owner or have the Apps Management Write role.
2. **Upload.** Go to https://platform.openai.com/plugins → **Upload new or existing plugin** → pick the verified identity → choose **Skills only** → upload `dist/happy-memes-0.1.0.zip`.
3. **Checks.** Under **Metadata & Skills**, wait for the metadata checks and the skill safety scan (the scan can take up to 2 hours). Use **Copy issues** → fix → re-upload.
4. **Submit for review** and complete the policy attestations. Skills-only plugins don't need MCP test cases, a demo video or screenshots.
5. **After approval, select Publish plugin.** Approval alone doesn't publish anything.

Decisions to make before uploading:
- **Name.** The display name is **Memes**, as chosen by the user. The package identifier is `happy-memes`; the skill is `meme`.
- **Listing URLs.** The manifest points at https://happy.engineering/plugins/memes/, /plugins/privacy/ and /plugins/terms/. Confirm they load before uploading.
- **Copyright.** The guidelines say to use only IP you own or have permission to use. The skill tells the model to recreate meme *layouts* with original characters rather than copy template photos or real people, so the plugin stays clear of that.

## Muse Code (Meta)

There is **no official Meta directory or submission process** for Muse plugins yet. Plugin commands are still behind `MUSE_EXPERIMENTAL_PLUGINS=1` as of Muse Code 1.4.x. Distribution today:

1. Push `happy-memes/` as a public GitHub repo. It already contains `.muse-plugin/plugin.json` and `.agents/plugins/marketplace.json`.
2. Validate: `MUSE_EXPERIMENTAL_PLUGINS=1 muse plugins validate .` (not run here because Muse isn't installed; install it with `curl -fsSL https://dev.meta.ai/install.sh | sh`). Expect the non-blocking warnings `multiple-manifests` / `ignored-root-manifest`.
3. Users install with: `muse plugins marketplace add happy-memes https://github.com/<org>/happy-memes` → `muse plugins install happy-memes@happy-memes`. Without the plugin flag, Muse still auto-discovers `.agents/skills/` and `~/.agents/skills/`, so `npx skills add <org>/happy-memes` also works.
4. Optional listing: https://www.musedirectory.dev/submit.html (community-run, not affiliated with Meta, manually curated).

Details and sources are in [`docs/muse-research.md`](docs/muse-research.md).
