"""Check the plugin package against OpenAI's documented directory limits."""
import json, os, re, sys, zipfile
from PIL import Image

root = sys.argv[1]
m = json.load(open(os.path.join(root, ".codex-plugin/plugin.json")))
ui = m["interface"]
errors = []

def check(ok, msg):
    if not ok:
        errors.append(msg)

def luminance(color):
    channels = [int(color[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return sum(c * weight for c, weight in zip(linear, (0.2126, 0.7152, 0.0722)))

for field, background in (("brandColor", "#FFFFFF"), ("brandColorDark", "#212121")):
    if field not in ui:
        continue
    color = ui[field]
    valid = isinstance(color, str) and re.fullmatch(r"#[0-9a-fA-F]{6}", color)
    check(valid, f"{field}: six-digit hex color")
    if valid:
        light, dark = sorted((luminance(color), luminance(background)), reverse=True)
        contrast = (light + 0.05) / (dark + 0.05)
        check(contrast >= 2, f"{field}: contrast {contrast:.2f}:1 against {background}, requires >= 2:1")
        print(f"{field}={color} contrast={contrast:.2f}:1 against {background}")

check(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}", m["name"]), "package name")
check(re.fullmatch(r"\d+\.\d+\.\d+", m["version"]), "semver")
check(0 < len(ui["displayName"]) <= 30 and "\n" not in ui["displayName"], "displayName <= 30")
check(0 < len(ui["shortDescription"]) <= 30 and "\n" not in ui["shortDescription"], "shortDescription <= 30")
check(0 < len(ui["longDescription"]) <= 4000, "longDescription <= 4000")
check(0 < len(ui["developerName"]) <= 80, "developerName <= 80")
check(ui["category"] in {"Productivity", "Creativity", "Developer Tools", "Business & Operations", "Data & Analytics",
                         "Communication", "Education & Research", "Security", "Finance", "Healthcare", "Travel",
                         "Entertainment", "Other"}, "category")
prompts = ui.get("defaultPrompt", [])
check(len(prompts) <= 3 and len({" ".join(p.split()).lower() for p in prompts}) == len(prompts), "<=3 unique prompts")
check(all(0 < len(p) <= 128 and "@" not in p for p in prompts), "prompt length/@mention")
for k in ("websiteURL", "privacyPolicyURL", "termsOfServiceURL"):
    check(ui[k].startswith("https://") and len(ui[k]) <= 1024, k)

for k in ("logo", "composerIcon"):
    p = os.path.join(root, ui[k])
    im = Image.open(p)
    check(im.width == im.height and im.width >= 48 and im.width <= 4096, f"{k} square 48..4096")
    check(os.path.getsize(p) <= 5 * 1024 * 1024, f"{k} <= 5 MiB")

skills_dir = os.path.join(root, "skills")
for s in sorted(os.listdir(skills_dir)):
    if s.startswith("."):
        continue
    text = open(os.path.join(skills_dir, s, "SKILL.md"), encoding="utf-8").read()
    fm = re.match(r"---\n(.*?)\n---\n(.+)", text, re.S)
    check(fm is not None, f"{s}: front matter")
    name = re.search(r"^name:\s*(.+)$", fm.group(1), re.M).group(1).strip()
    desc = re.search(r"^description:\s*(.+)$", fm.group(1), re.M).group(1).strip()
    check(len(desc) <= 1024, f"{s}: description <= 1024")
    check(len(f"{m['name']}:{name}") <= 64, f"{s}: namespaced name <= 64")
    print(f"skill {m['name']}:{name}  desc={len(desc)} chars  body={len(fm.group(2).splitlines())} lines  words={len(text.split())}")

print(f"displayName={ui['displayName']!r} ({len(ui['displayName'])})  short={ui['shortDescription']!r} ({len(ui['shortDescription'])})  long={len(ui['longDescription'])}")
if len(sys.argv) > 2:
    z = zipfile.ZipFile(sys.argv[2])
    names = z.namelist()
    print("zip entries:", names)
    check(os.path.getsize(sys.argv[2]) <= 100 * 1024 * 1024, "zip <= 100 MB")
    check(not any(n.startswith((".muse-plugin", ".agents")) for n in names), "zip has only the OpenAI package")
print("OK" if not errors else "ERRORS: " + "; ".join(errors))
sys.exit(1 if errors else 0)
