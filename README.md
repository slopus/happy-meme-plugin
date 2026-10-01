# Happy Memes

A skills-only plugin for ChatGPT, Codex and Muse Code that turns a news story, launch, trend or everyday moment into an image meme you can post.

The skill (`plugins/happy-memes/skills/meme/SKILL.md`) checks the facts, writes the jokes before drawing anything, picks a format whose logic fits the joke, and prompts the host's built-in image model with short, exactly quoted captions. Each meme comes with post copy, alt text, the moment it references, and when the joke goes stale.

See [`examples/`](examples/README.md) for 20 memes from the first test run (Oct 1, 2026).

## Install

Codex / ChatGPT desktop:

```sh
codex plugin marketplace add slopus/happy-meme-plugin
codex plugin add happy-memes@happy-meme-plugin
```

Muse Code (plugins are still experimental):

```sh
MUSE_EXPERIMENTAL_PLUGINS=1 muse plugins marketplace add happy-meme-plugin https://github.com/slopus/happy-meme-plugin
MUSE_EXPERIMENTAL_PLUGINS=1 muse plugins install happy-memes@happy-meme-plugin
```

Then ask for a meme, or invoke the `meme` skill directly.

## Layout

```
.agents/plugins/marketplace.json   marketplace entry (Codex and Muse)
plugins/happy-memes/
  .codex-plugin/plugin.json        ChatGPT + Codex manifest and directory listing
  .muse-plugin/plugin.json         Muse Code manifest
  skills/meme/SKILL.md             the skill
  assets/                          logo and composer icon (Happy brutalist avatar)
scripts/build.sh                   validate and build dist/happy-memes-<version>.zip
scripts/validate.py                checks OpenAI's documented listing limits
scripts/render_icon.py             renders the icon from Happy's avatar tiles
examples/                          test-run memes
```

## Release

Bump `version` in both manifests, then run `scripts/build.sh` and follow [SUBMISSION.md](SUBMISSION.md).
