# GetCodeFree — Image Prompt System

Every tweet, post, and article draft MUST include a `image_prompt` field for Gemini image generation.

## Brand Visual DNA

| Token | Value | Usage |
|---|---|---|
| Background | #090d11 (near-black) | Main canvas |
| Surface | #10161c (dark slate) | Card/container |
| Primary | #19d3c5 (teal) | Headlines, accents, glows |
| Accent | #6f8cff (blue) | Secondary highlights, gradients |
| Text | #edf2f7 (off-white) | Body copy |
| Glow | rgba(25,211,197,0.18) | Teal glow behind focal elements |
| Gradient | teal → blue (120deg) | Headline text, hero backgrounds |
| Style | Minimalist tech, dark cyberpunk-clean | No photorealism |
| Humans | Cartoonish illustration style | Dev characters, founders |
| Logos | Only when mentioning real tools | Claude, Gemini, GPT, etc. |

## Image Specs

| Format | Size | Aspect | Use |
|---|---|---|---|
| Square | 1080×1080 | 1:1 | Tweets, quote cards |
| Landscape | 1200×628 | 1.91:1 | Link previews, carousels |
| Portrait | 1080×1350 | 4:5 | Mobile-optimized scroll |

## Prompt Template

```
Image prompt for Gemini:

Style: Digital illustration, minimalist tech aesthetic, dark mode, cyberpunk-clean.
Colors: Dark navy/teal background (#090d11), bright teal (#19d3c5) and blue (#6f8cff) accents, glowing elements, white/off-white text.
Mood: Futuristic, professional, energetic, tech-forward.
Composition: [describe layout — central focus, split screen, etc.]
Subject: [describe main visual — cartoonish dev character, UI mockup, abstract tech shapes, code on screen, tool logo]
Typography: Bold sans-serif headline text in teal gradient on dark background.
Details: Subtle grid lines, light particles, glass-morphism card surfaces, soft teal glow.
Text to include: "[key headline from content]"
Size: 1080×1080px or 1200×628px
```

## Category Templates

### Tweet image (1:1 square — 1080×1080)
```
Image prompt for Gemini:
Style: Digital illustration, minimalist tech, dark cyberpunk-clean.
Colors: #090d11 background, #19d3c5 teal accents, #6f8cff blue highlights.
Mood: Bold, insightful, tech authority.
Subject: [cartoonish dev character OR abstract tech/UI graphic OR code interface]
Typography: Bold gradient (teal→blue) headline, white subtext.
Details: Subtle grid, teal glow behind focal point, glass surface.
Text: "[1-line quote/key insight]"
Size: 1080×1080 square.
```

### Post image (1.91:1 landscape — 1200×628)
```
Image prompt for Gemini:
Style: Digital illustration, minimalist tech, dark cyberpunk-clean.
Colors: #090d11 background, #19d3c5 teal accents, #6f8cff blue highlights.
Mood: Professional, forward-looking, expert.
Subject: [cartoonish developer/founder character OR dashboard UI OR abstract tech shapes]
Typography: Bold gradient title, white subtitle.
Details: Glass card, teal glow, subtle particle effects, grid lines.
Text: "[headline]"
Size: 1200×628 landscape.
```

### Article cover (5:2 — 1600×640)
```
Image prompt for Gemini:
Style: Digital illustration, minimalist tech, dark cyberpunk-clean.
Colors: #090d11 background, #19d3c5 teal accents, #6f8cff blue highlights.
Mood: Deep, authoritative, visionary.
Subject: [conceptual illustration of article topic]
Typography: Large gradient title, white subtitle line.
Details: Full teal glow backdrop, glass card layers, tech grid.
Text: "[article title]"
Size: 1600×640 (5:2 ratio — X Articles requirement).
```

### Article inline image placeholder (varies)

Place between sections. Describe content-specific visual. Mention aspect ratio in description.
```
Image prompt for Gemini:
Style: Digital illustration, minimalist tech, dark cyberpunk-clean.
Colors: #090d11 background, #19d3c5 teal accents, #6f8cff blue highlights.
Mood: [matches surrounding section tone — e.g. analytical for architecture, energetic for results]
Subject: [specific visual matching [Image: description] label in article]
Typography: Minimal or none (illustration-only).
Details: Glass card layers, teal glow, grid lines, tool logo badges if relevant.
Size: [choose based on placement context].
```

### Tool/Logo mention
When content mentions specific tools, include their logo/styled reference:
- Claude → Purple/anthropic-styled chip icon
- Gemini → Multicolor Google-style chip
- GPT/OpenAI → Green dot pattern
- Kimi K3 → Blue/teal chip
- Cursor → Dark green accent
- AWS → Orange chip
- Browser-use → Teal chip

Example addition to prompt:
```
Include a small stylized "[Tool]" chip/badge in the bottom-right corner.
Colors: [tool-specific colors]. Style: Glass-morphism pill badge.
```
