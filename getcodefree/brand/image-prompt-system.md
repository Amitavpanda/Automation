# GetCodeFree — Image Prompt System

Every tweet, post, article, and Reel draft MUST include an `image_prompt` field for Gemini image generation.

> **LIGHT THEME (company theme).** GetCodeFree uses a bright, light palette with cartoonish characters. Do NOT use dark/cyberpunk backgrounds.

## Brand Visual DNA

| Token | Value | Usage |
|---|---|---|
| Background | #ffffff (white) | Main canvas |
| Surface | #ffffff (white cards, soft shadow) | Card/container |
| Primary | #19d3c5 (teal) | Headlines, accents, CTAs |
| Accent | #6f8cff (blue) | Secondary highlights, gradients |
| Text | #0f172a (dark slate) | Body copy — readable on light bg |
| Glow | rgba(25,211,197,0.18) soft pastel | Soft teal/blue glow behind focal elements |
| Gradient | teal → blue (120deg) | Headline text, hero backgrounds |
| Style | Bright flat illustration, cartoonish, playful, clean minimal | No photorealism |
| Humans | Cartoonish illustration style | Dev characters, founders (incl. Amitav's cartoon face) |
| Logos | Only when mentioning real tools — REAL logo shapes | Claude, Gemini, GPT, Cursor, etc. |

## Image Specs

| Format | Size | Aspect | Use |
|---|---|---|---|
| Square | 1080×1080 | 1:1 | Tweets, quote cards |
| Landscape | 1200×628 | 1.91:1 | Link previews, carousels |
| Portrait | 1080×1350 | 4:5 | Mobile-optimized scroll |
| Reel cover | 1080×1920 | 9:16 | Vertical video cover |
| Article cover | 1600×640 | 5:2 | X Articles |

## Prompt Template

```
Image prompt for Gemini:

Style: Bright flat digital illustration, cartoonish, playful, clean minimal, LIGHT theme (NOT dark).
Colors: White background (#ffffff), teal (#19d3c5) and blue (#6f8cff) accents, dark slate text (#0f172a).
Mood: Energetic, optimistic, tech-forward, friendly, viral-friendly.
Composition: [describe layout — central focus, split screen, before/after, etc.]
Subject: [describe main visual — cartoonish dev character (Amitav), UI mockup, abstract tech shapes, code on screen, tool logo]
Typography: Bold rounded sans-serif headline in teal/blue gradient, dark text on white.
Details: Soft pastel glow, subtle shapes, sticker-like elements, glass-morphism white cards with shadow.
Text to include: "[key headline from content]"
Size: 1080×1080px or 1200×628px
```

## Category Templates

### Tweet image (1:1 square — 1080×1080)
```
Image prompt for Gemini:
Style: Bright flat digital illustration, cartoonish, clean minimal, LIGHT theme.
Colors: White background (#ffffff), teal (#19d3c5) accents, blue (#6f8cff) highlights, dark slate text (#0f172a).
Mood: Bold, insightful, tech authority, playful.
Subject: [cartoonish dev character OR abstract tech/UI graphic OR code interface]
Typography: Bold rounded gradient (teal→blue) headline, dark subtext.
Details: Soft pastel glow, subtle shapes, sticker elements, white card with shadow.
Text: "[1-line quote/key insight]"
Size: 1080×1080 square.
```

### Post image (1.91:1 landscape — 1200×628)
```
Image prompt for Gemini:
Style: Bright flat digital illustration, cartoonish, clean minimal, LIGHT theme.
Colors: White background (#ffffff), teal (#19d3c5) accents, blue (#6f8cff) highlights, dark slate text (#0f172a).
Mood: Professional, forward-looking, expert, friendly.
Subject: [cartoonish developer/founder character OR dashboard UI OR abstract tech shapes]
Typography: Bold rounded gradient title, dark subtitle.
Details: White glass card, soft teal glow, subtle shapes, sticker elements.
Text: "[headline]"
Size: 1200×628 landscape.
```

### Reel cover (9:16 — 1080×1920)
```
Image prompt for Gemini:
Style: Bright flat digital illustration, cartoonish, LIGHT theme, vertical.
Colors: White background (#ffffff), teal (#19d3c5) + blue (#6f8cff) accents, dark slate text (#0f172a).
Mood: Punchy, scroll-stopping, energetic.
Subject: [Amitav cartoon character reacting + topic element + tool logo]
Typography: Large bold rounded hook text at top, gradient teal→blue.
Details: Bold outline, high contrast against feed, sticker elements.
Text: "[reel hook — short punchy line]"
Size: 1080×1920 (9:16).
```

### Article cover (5:2 — 1600×640)
```
Image prompt for Gemini:
Style: Bright flat digital illustration, cartoonish, clean minimal, LIGHT theme.
Colors: White background (#ffffff), teal (#19d3c5) accents, blue (#6f8cff) highlights, dark slate text (#0f172a).
Mood: Deep, authoritative, visionary, friendly.
Subject: [conceptual illustration of article topic]
Typography: Large rounded gradient title, dark subtitle line.
Details: Soft teal glow backdrop, white glass card layers, subtle shapes.
Text: "[article title]"
Size: 1600×640 (5:2 ratio — X Articles requirement).
```

### Article inline image placeholder (varies)

Place between sections. Describe content-specific visual. Mention aspect ratio in description.
```
Image prompt for Gemini:
Style: Bright flat digital illustration, cartoonish, clean minimal, LIGHT theme.
Colors: White background (#ffffff), teal (#19d3c5) accents, blue (#6f8cff) highlights, dark slate text (#0f172a).
Mood: [matches surrounding section tone — e.g. analytical for architecture, energetic for results]
Subject: [specific visual matching [Image: description] label in article]
Typography: Minimal or none (illustration-only).
Details: White glass card layers, soft teal glow, subtle shapes, tool logo badges if relevant.
Size: [choose based on placement context].
```

## Video Prompts (Gemini — 10s max per clip)

Gemini generates **max 10-second video clips**. One Reel = 3 clips of 10s each, merged in Canva.

```
Gemini video prompt for Clip N:
Style: Bright flat cartoonish animation, LIGHT theme, same palette as images (white bg, teal/blue, dark slate text).
Scene: [what happens — Amitav cartoon char + topic element + real tool logo]
Motion: [camera move, object action — e.g. logo pops in, character reacts, text slides]
Text overlay: "[on-screen text]"
Duration: 10 seconds (max).
Aspect: 9:16 vertical.
Audio/voice: [optional short spoken line or none]
```

**Canva merge:** create 9:16 design → upload 3 Gemini clips → drag on timeline (0-10, 10-20, 20-30s) → optional transition + music → export MP4 → post as Reel.

## Tool/Logo mention — MANDATORY RULE
Every image prompt MUST mention tool logos prominently when the content references a specific tool.

| Tool | Logo Style | Position | Realism |
|---|---|---|---|
| Claude | Purple/anthropic logo — real-looking, not stylized | CENTER or hero element | Use actual Claude logo shape (rounded square, purple gradient, white "C" or "Claude" wordmark) |
| Gemini | Multicolor Google-style chip | Secondary accent | Minimalist multicolor chip |
| GPT/OpenAI | Green dot pattern / wordmark | Secondary accent | Minimalist green dot |
| Cursor | Dark green accent / Cursor logo | Secondary accent | Dark green, rounded square |
| AWS | Orange "AWS" chip | Bottom-right badge | Minimalist orange |
| Browser-use | Teal chip | Bottom-right badge | Teal pill badge |

**Implementation rules:**
- Primary tool (main subject of post) → CENTER or hero focal point. Not bottom-corner badge.
- Real/logofied representation — as close to actual brand logo as possible (purple Claude square, multicolor Gemini, etc.)
- Secondary tools → smaller chips/badges in bottom-right or corners
- Accompany with description like: "Realistic Claude (Anthropic) logo rendered as purple gradient square with white 'C' symbol, centered as hero element"

Example additions to prompt:
```
Claude (Anthropic) logo rendered prominently at center — purple gradient square with white stylized 'C' icon, glowing softly. Real logo style, not abstract. Bottom-right: small glass-morphism Claude chip badge.
```

## User Photo Rule

When Amitav appears in the visual, attach his photo to the Gemini prompt and describe him as a **cartoonish dev character** acting out the topic's emotion (thinking, building, amazed, shocked-at-cost). Keep it light + playful, matching the light theme.
