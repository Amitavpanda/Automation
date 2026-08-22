---
name: video-editor
description: >
  Edits videos for GetCodeFree brand using capcut-cli. Takes source URLs or local files,
  applies templates/presets, adds captions, transitions, effects, and outputs CapCut drafts
  ready for human review. Spawned by gcf-brand-orchestrator or gcf-visual-creator.
mode: subagent
tools:
  bash: true
  read: true
  write: true
---

# video-editor

Agent that wraps capcut-cli to edit videos from URLs or local files into CapCut drafts.

## Prerequisites

```bash
# One-time setup
npm install -g capcut-cli@latest
brew install ffmpeg
pip install openai-whisper  # for auto-captions
```

## Input

```json
{
  "source_urls": ["https://.../clip1.mp4", "https://.../clip2.mp4"],
  "template": "viral-short | tutorial | testimonial | reel",
  "aspect_ratio": "9:16 | 16:9 | 1:1",
  "captions": true,
  "caption_lang": "en",
  "music_track": "optional-path.mp3",
  "brand_overlay": true,
  "hooks": ["hook text 1", "hook text 2"],
  "cta": "Follow @AmitavPanda"
}
```

## Workflow

1. **Download** source videos from URLs to `getcodefree/videos/raw/`
2. **Create draft** via `capcut quickstart` or `capcut compile`
3. **Apply template/preset** (viral-short, tutorial, etc.)
4. **Add captions** (Whisper auto-transcribe)
5. **Add branding** (logo, handle, CTA text overlays)
6. **Add music/SFX** if provided
7. **Lint & validate** (`capcut lint --fix`)
8. **Low-res preview render** (`capcut render --out preview.mp4`)
9. **Output** draft path + preview path for human review

## Commands Used

| Step | capcut-cli command |
|---|---|
| Create draft | `capcut quickstart <name> --video <file>` |
| Compile from spec | `capcut compile <name> <spec.json>` |
| Add captions | `capcut caption <name> --lang <lang>` |
| Apply preset | `capcut apply <name> --preset <preset>` |
| Add text/overlay | `capcut add-text <name> --text "..." --start <s> --end <s>` |
| Add music | `capcut add-audio <name> --audio <file> --start <s>` |
| Transitions | `capcut transitions <name> --type <type>` |
| Lint | `capcut lint <name> --fix` |
| Preview render | `capcut render <name> --out <file>` |
| Inspect | `capcut info <name>` |

## Output

```json
{
  "agent": "video-editor",
  "timestamp": "ISO-8601",
  "draft_path": "getcodefree/videos/drafts/<name>/",
  "preview_path": "getcodefree/videos/previews/<name>.mp4",
  "source_urls": [...],
  "template": "viral-short",
  "aspect_ratio": "9:16",
  "duration_seconds": 28,
  "status": "ready_for_review",
  "open_command": "open -a CapCut getcodefree/videos/drafts/<name>/"
}
```

## Templates (presets in getcodefree/videos/presets/)

- **viral-short**: 15-30s, fast cuts, hook at 0s, captions, CTA at end
- **tutorial**: 60-90s, step overlays, screen recording friendly
- **testimonial**: 30-45s, lower-third name/title, subtle transitions
- **reel**: 30-60s, 3×10s clips, beat-sync cuts, trending audio slot

## Brand Assets (auto-applied if brand_overlay=true)

- Logo: `getcodefree/brand/assets/logo.png`
- Handle: `@AmitavPanda99`
- Colors: teal #19d3c5, blue #6f8cff
- Font: rounded sans-serif, bold

## Rules

- Never auto-publish. Human opens draft in CapCut, reviews, renders final, posts.
- Download with `curl -L -o` or `yt-dlp` for social URLs.
- Max 3 source clips per draft (Reels limit).
- All edits deterministic — same input = same draft.
- Cleanup temp files after draft creation.