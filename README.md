# Happy Memes

A skills-only plugin for ChatGPT, Codex and Muse Code that turns a news story, launch, trend or everyday moment into an image meme you can post.

The skill (`plugins/happy-memes/skills/meme/SKILL.md`) checks the facts, writes the jokes before drawing anything, picks a format whose logic fits the joke, and prompts the host's built-in image model with short, exactly quoted captions. Each meme comes with post copy, alt text, the moment it references, and when the joke goes stale.

See [`examples/`](examples/README.md) for 20 memes from the first test run (Oct 1, 2026).

## Install

ChatGPT: find **Happy Memes** in the plugin directory (submission pending).

Codex, or ChatGPT desktop from this repo:

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
  assets/                          logo and composer icon (a Happy bot face)
scripts/build.sh                   validate and build dist/happy-memes-<version>.zip
scripts/validate.py                checks OpenAI's documented listing limits
scripts/render_icon.mjs            renders the icon as a Happy bot face (DiceBear, seed "happy-memes")
examples/                          test-run memes
```

## Release

Bump `version` in both manifests, then run `scripts/build.sh` and follow [SUBMISSION.md](SUBMISSION.md).

## Credits

The icon is a Happy bot face: [Adventurer Neutral](https://www.figma.com/community/file/1184595184137881796) by [Lisa Wischofsky](https://www.instagram.com/lischi_art/), remixed by [DiceBear](https://www.dicebear.com), licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Regenerate it with `scripts/render_icon.mjs` after `npm i --no-save @dicebear/core @dicebear/styles sharp`.
