// Render the plugin icon as a Happy bot face: DiceBear Adventurer Neutral drawn
// from a seed, the same way happy-desktop's BotFace gives a new bot its face.
// The pack is Lisa Wischofsky's "Adventurer Neutral" (CC BY 4.0), remixed by DiceBear.
//
// Usage: node scripts/render_icon.mjs [seed]
// Needs @dicebear/core, @dicebear/styles and sharp: npm i --no-save @dicebear/core @dicebear/styles sharp
import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";
import path from "node:path";

const require = createRequire(import.meta.url);
const { Avatar, Style } = await import("@dicebear/core");
const adventurerNeutral = require("@dicebear/styles/adventurer-neutral.json");
const sharp = require("sharp");

const seed = process.argv[2] ?? "memes-face-04";
const assets = path.join(path.dirname(fileURLToPath(import.meta.url)), "../plugins/happy-memes/assets");
const style = new Style(adventurerNeutral);

for (const [file, size] of [["logo.png", 1024], ["composer-icon.png", 256]]) {
    const svg = new Avatar(style, { seed, size }).toString();
    await sharp(Buffer.from(svg)).resize(size, size).png().toFile(path.join(assets, file));
}
console.log(`rendered seed "${seed}"`);
