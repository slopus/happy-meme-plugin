---
name: meme
description: Make funny, postable image memes about a news story, product launch, trend, cultural moment, or the user's own situation. Use when the user asks for a meme, a reaction image, a joke picture to post, or "make this funny" visually.
---

# Meme

The user's explicit instructions (topic, format, tone, wording, count) override everything below.

## What makes a meme work

- **Familiar format + new content.** The reader should recognize the format at a glance; the joke lives in what you swap in.
- **Find the tension, not the headline.** Use the gap between the announcement and real life, hypocrisy, escalation, or the "that's me" feeling. A caption that just restates the news isn't a joke.
- **Be specific.** Use the exact price, model name, slide or detail that insiders noticed. Broad jokes are weaker.
- **Short and deadpan.** At most 12 words on the image, one setup and one payoff. Never explain the joke. Low-fi beats glossy.
- **Fresh.** A trend joke is worth making within about 72 hours. After that, take a new angle or skip it.
- **Punch up or sideways.** Aim at companies, hype, ourselves and shared pain, never at victims. Skip tragedies, deaths and active crises.

## Workflow

1. **Get the facts.** If the topic is current and you can browse, check what actually happened and the jokes people are already posting. Don't invent facts, quotes or numbers.
2. **Write jokes before images.** Draft 5 or more captions per topic that use different mechanisms. For a batch, use one joke sheet across topics. Deliberately include a sharper version of the best existing joke (credit its @handle when you deliver) and an angle nobody has posted yet. Cut any caption that restates the news or needs explaining. Keep the best 1-3.
3. **Pick a format whose logic matches the joke:**
   - Absurd literalism (the most reliable for image models): put the joke on a real object, like a product box, report card, marquee, warning sign, poster, coffee-cup names, calendar invite or pricing page.
   - Reject vs. prefer: a two-panel "no / yes".
   - Escalation: an expanding-brain stack, a chart that goes vertical, or a before / after / after-that strip.
   - Temptation: the distracted-glance shot.
   - Dilemma: two buttons and a sweating hand.
   - Denial: "this is fine" in a burning room.
   - Contrast: "what they announced / what I got", "expectation / reality".
   - Deadpan: an ordinary photo with one caption, a group-chat screenshot, or a "nobody: / me:" post.
   Recreate the layout with original characters or objects. Don't copy template photos or depict real people.
4. **Write the image prompt in this order:**
   - The medium: "cheap phone photo", "slightly blurry screenshot of a social post", "classic two-panel meme", "MS Paint comic".
   - The layout and aspect ratio. Use 1:1 or 4:5 for feeds and 16:9 for fake slides.
   - Each piece of text in quotes, with its position and font, e.g. `top, bold white Impact with black outline: "..."`.
   - Close with: `Render all text exactly as quoted. No other text, logos, or watermarks.`
   - Add imperfections where they help the joke (JPEG grain, a bad crop, clutter). Avoid "cinematic", "4k" and "ultra-detailed".
   - Use labels and generic stand-ins instead of real logos or real people's faces.
5. **Generate** with the host's built-in image tool. Make one call per meme. In a batch, save each image as soon as it passes the check.
6. **Check every image.** Is every word spelled right? Does the layout read in 2 seconds? Does the joke land without context? Fix problems with one targeted edit. If the text is still wrong after two tries, generate without text and typeset the captions yourself if you can run code. Otherwise, hand over the clean image plus the exact captions.
7. **Deliver** each meme with:
   - the image, or its saved path
   - post copy of 100 characters or fewer that adds to the joke instead of repeating the image text, or "(no copy)"
   - alt text, saying "illustration" when it depicts a real animal, place or product
   - a one-line note on the moment it refers to, and any existing joke it builds on
   - how to post: standalone or as a quote of a specific post, and the date after which the joke is stale

If image generation is unavailable, deliver the finished prompt and captions so the user can run them elsewhere.

## Limits

- Don't make realistic fake quotes, posts or screenshots attributed to real people. Parody of brands and products must read as parody.
- Don't depict real people's likeness, copyrighted characters or recognizable brand mascots (no Clippy), or build on hateful meme formats.
- Keep it suitable for a general audience.
