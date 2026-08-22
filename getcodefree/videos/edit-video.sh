#!/usr/bin/env bash
# video-editor wrapper — wraps capcut-cli for agent use
# Usage: ./edit-video.sh '{"source_urls":["..."],"template":"viral-short","aspect_ratio":"9:16","captions":true,"brand_overlay":true}'

set -euo pipefail

INPUT_JSON="${1:-}"
if [[ -z "$INPUT_JSON" ]]; then
  echo "Usage: $0 '<json-input>'"
  exit 1
fi

# Parse input
SOURCE_URLS=$(echo "$INPUT_JSON" | jq -r '.source_urls[]')
TEMPLATE=$(echo "$INPUT_JSON" | jq -r '.template // "viral-short"')
ASPECT_RATIO=$(echo "$INPUT_JSON" | jq -r '.aspect_ratio // "9:16"')
CAPTIONS=$(echo "$INPUT_JSON" | jq -r '.captions // true')
CAPTION_LANG=$(echo "$INPUT_JSON" | jq -r '.caption_lang // "en"')
MUSIC_TRACK=$(echo "$INPUT_JSON" | jq -r '.music_track // ""')
BRAND_OVERLAY=$(echo "$INPUT_JSON" | jq -r '.brand_overlay // true')
HOOKS=$(echo "$INPUT_JSON" | jq -r '.hooks // [] | @json')
CTA=$(echo "$INPUT_JSON" | jq -r '.cta // "Follow @AmitavPanda99"')

# Paths
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
RAW_DIR="$ROOT/videos/raw"
DRAFT_DIR="$ROOT/videos/drafts"
PREVIEW_DIR="$ROOT/videos/previews"
PRESET_DIR="$ROOT/videos/presets"
SPEC_DIR="$ROOT/videos/specs"

mkdir -p "$RAW_DIR" "$DRAFT_DIR" "$PREVIEW_DIR" "$PRESET_DIR" "$SPEC_DIR"

# Timestamp for unique names
TS=$(date +%s)
DRAFT_NAME="edit-$TS"
DRAFT_PATH="$DRAFT_DIR/$DRAFT_NAME"
PREVIEW_PATH="$PREVIEW_DIR/$DRAFT_NAME.mp4"

echo "🎬 Starting video edit: $DRAFT_NAME"
echo "   Template: $TEMPLATE"
echo "   Aspect: $ASPECT_RATIO"

# 1. Download source videos
LOCAL_FILES=()
i=0
for URL in $SOURCE_URLS; do
  i=$((i+1))
  EXT="${URL##*.}"
  EXT="${EXT%%\?*}"
  [[ "$EXT" == "$URL" ]] && EXT="mp4"
  OUT_FILE="$RAW_DIR/src-$TS-$i.$EXT"
  echo "⬇️  Downloading $URL → $OUT_FILE"
  curl -L -f -o "$OUT_FILE" "$URL" || { echo "❌ Download failed: $URL"; exit 1; }
  LOCAL_FILES+=("$OUT_FILE")
done

# 2. Create draft from first video
PRIMARY="${LOCAL_FILES[0]}"
echo "📝 Creating draft from $PRIMARY"
capcut quickstart "$DRAFT_NAME" --video "$PRIMARY"

# 3. Add additional videos as segments
for ((j=1; j<${#LOCAL_FILES[@]}; j++)); do
  echo "➕ Adding clip ${LOCAL_FILES[$j]}"
  capcut add-video "$DRAFT_NAME" --video "${LOCAL_FILES[$j]}"
done

# 4. Apply preset/template
PRESET_FILE="$PRESET_DIR/$TEMPLATE.json"
if [[ -f "$PRESET_FILE" ]]; then
  echo "🎨 Applying preset: $TEMPLATE"
  capcut apply "$DRAFT_NAME" --preset "$PRESET_FILE"
else
  echo "⚠️  Preset not found: $PRESET_FILE, using defaults"
fi

# 4b. Set aspect ratio
capcut compile "$DRAFT_NAME" "$(cat <<EOF
{
  "canvas": { "aspect_ratio": "$ASPECT_RATIO" }
}
EOF
)"

# 5. Auto-captions
if [[ "$CAPTIONS" == "true" ]]; then
  echo "💬 Adding captions ($CAPTION_LANG)"
  capcut caption "$DRAFT_NAME" --lang "$CAPTION_LANG"
fi

# 6. Brand overlay
if [[ "$BRAND_OVERLAY" == "true" ]]; then
  echo "🏷️  Adding brand overlay"
  LOGO="$ROOT/getcodefree/brand/assets/logo.png"
  if [[ -f "$LOGO" ]]; then
    capcut add-image "$DRAFT_NAME" --image "$LOGO" --start 0 --end 9999 --position "top-right" --scale 0.15
  fi
  capcut add-text "$DRAFT_NAME" --text "@AmitavPanda99" --start 0 --end 9999 --position "bottom-right" --font-size 24 --color "#19d3c5"
  capcut add-text "$DRAFT_NAME" --text "$CTA" --start 9990 --end 9999 --position "center" --font-size 32 --color "#ffffff" --bg-color "#0f172a"
fi

# 7. Hook texts (first 3 seconds)
HOOK_ARRAY=$(echo "$HOOKS" | jq -c '.')
if [[ "$HOOK_ARRAY" != "[]" ]]; then
  echo "$HOOK_ARRAY" | jq -r '.[]' | while IFS= read -r hook; do
    capcut add-text "$DRAFT_NAME" --text "$hook" --start 0 --end 3 --position "top-center" --font-size 28 --color "#ffffff" --bg-color "#0f172a"
  done
fi

# 8. Music track
if [[ -n "$MUSIC_TRACK" && -f "$MUSIC_TRACK" ]]; then
  echo "🎵 Adding music: $MUSIC_TRACK"
  capcut add-audio "$DRAFT_NAME" --audio "$MUSIC_TRACK" --start 0 --volume 0.3
fi

# 9. Lint & fix
echo "🔍 Linting draft"
capcut lint "$DRAFT_NAME" --fix

# 10. Preview render
echo "🎥 Rendering preview"
capcut render "$DRAFT_NAME" --out "$PREVIEW_PATH"

# 11. Output result
INFO=$(capcut info "$DRAFT_NAME" -H 2>/dev/null || true)
DURATION=$(echo "$INFO" | grep -oE 'duration[^0-9]*([0-9.]+)' | head -1 | sed 's/[^0-9.]//g' || echo "0")

cat <<EOF
{
  "agent": "video-editor",
  "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "draft_path": "$DRAFT_PATH/",
  "preview_path": "$PREVIEW_PATH",
  "source_urls": $(echo "$SOURCE_URLS" | jq -R . | jq -s .),
  "template": "$TEMPLATE",
  "aspect_ratio": "$ASPECT_RATIO",
  "duration_seconds": ${DURATION:-0},
  "status": "ready_for_review",
  "open_command": "open -a CapCut \"$DRAFT_PATH/\""
}
EOF

echo "✅ Done. Draft ready at: $DRAFT_PATH/"
echo "📺 Preview: $PREVIEW_PATH"
echo "👉 Open in CapCut: open -a CapCut \"$DRAFT_PATH/\""