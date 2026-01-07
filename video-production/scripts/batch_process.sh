#!/bin/bash
# Batch FFmpeg Processing Script for Tutorial Videos

set -e  # Exit on error

# Configuration
RAW_DIR="../raw-footage"
PROCESSED_DIR="../processed-videos"
INTRO_FILE="../assets/intro.mp4"
OUTRO_FILE="../assets/outro.mp4"
WATERMARK="../assets/overlays/watermark.png"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Video Batch Processing Script ===${NC}"

# Create directories if they don't exist
mkdir -p "$PROCESSED_DIR"

# Function to process a single video
process_video() {
    local input_file="$1"
    local filename=$(basename "$input_file")
    local name="${filename%.*}"

    echo -e "\n${GREEN}Processing: $filename${NC}"

    # Step 1: Compress and optimize
    echo "Step 1/4: Compressing video..."
    ffmpeg -i "$input_file" \
        -c:v libx264 \
        -crf 23 \
        -preset medium \
        -c:a aac \
        -b:a 128k \
        -y "$PROCESSED_DIR/${name}_compressed.mp4" \
        -loglevel warning -stats

    # Step 2: Add intro/outro (if files exist)
    if [ -f "$INTRO_FILE" ] && [ -f "$OUTRO_FILE" ]; then
        echo "Step 2/4: Adding intro and outro..."

        # Create concat file
        cat > "$PROCESSED_DIR/concat_${name}.txt" << EOF
file '$(realpath "$INTRO_FILE")'
file '$(realpath "$PROCESSED_DIR/${name}_compressed.mp4")'
file '$(realpath "$OUTRO_FILE")'
EOF

        ffmpeg -f concat \
            -safe 0 \
            -i "$PROCESSED_DIR/concat_${name}.txt" \
            -c copy \
            -y "$PROCESSED_DIR/${name}_with_intro_outro.mp4" \
            -loglevel warning -stats

        rm "$PROCESSED_DIR/concat_${name}.txt"
        CURRENT_FILE="$PROCESSED_DIR/${name}_with_intro_outro.mp4"
    else
        echo "Step 2/4: Skipping intro/outro (files not found)"
        CURRENT_FILE="$PROCESSED_DIR/${name}_compressed.mp4"
    fi

    # Step 3: Add watermark (if exists)
    if [ -f "$WATERMARK" ]; then
        echo "Step 3/4: Adding watermark..."
        ffmpeg -i "$CURRENT_FILE" \
            -i "$WATERMARK" \
            -filter_complex "[1:v]scale=120:-1[wm];[0:v][wm]overlay=W-w-10:H-h-10" \
            -c:a copy \
            -y "$PROCESSED_DIR/${name}_watermarked.mp4" \
            -loglevel warning -stats
        CURRENT_FILE="$PROCESSED_DIR/${name}_watermarked.mp4"
    else
        echo "Step 3/4: Skipping watermark (file not found)"
    fi

    # Step 4: Create YouTube-optimized versions
    echo "Step 4/4: Creating YouTube formats..."

    # 1080p version
    ffmpeg -i "$CURRENT_FILE" \
        -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2" \
        -c:v libx264 \
        -crf 23 \
        -preset medium \
        -c:a copy \
        -y "$PROCESSED_DIR/${name}_1080p.mp4" \
        -loglevel warning -stats

    # 720p version
    ffmpeg -i "$CURRENT_FILE" \
        -vf "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2" \
        -c:v libx264 \
        -crf 23 \
        -preset medium \
        -c:a copy \
        -y "$PROCESSED_DIR/${name}_720p.mp4" \
        -loglevel warning -stats

    echo -e "${GREEN}✓ Completed: ${name}_1080p.mp4${NC}"
}

# Process all videos in raw-footage directory
if [ -d "$RAW_DIR" ]; then
    video_count=0
    for video in "$RAW_DIR"/*.{mp4,mov,avi,mkv}; do
        if [ -f "$video" ]; then
            process_video "$video"
            ((video_count++))
        fi
    done

    if [ $video_count -eq 0 ]; then
        echo -e "${RED}No video files found in $RAW_DIR${NC}"
    else
        echo -e "\n${GREEN}=== Processing Complete ===${NC}"
        echo -e "${GREEN}Processed $video_count video(s)${NC}"
        echo -e "${BLUE}Output directory: $PROCESSED_DIR${NC}"
    fi
else
    echo -e "${RED}Error: $RAW_DIR directory not found${NC}"
    exit 1
fi
