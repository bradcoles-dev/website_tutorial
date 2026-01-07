# Tutorial Production Workflow

This guide walks you through the complete workflow for creating tutorial videos from recording to publishing.

## Pre-Production

### 1. Planning

- [ ] Choose tutorial topic
- [ ] Research and outline content
- [ ] Prepare code examples
- [ ] Create script/talking points
- [ ] Set up development environment

### 2. Asset Preparation

```bash
# Ensure you have:
- Intro video (assets/intro.mp4)
- Outro video (assets/outro.mp4)
- Watermark/Logo (assets/overlays/watermark.png)
- Background music (optional: assets/music/)
```

## Production

### 3. Recording

**Recommended Settings:**
- Resolution: 1920x1080 (minimum)
- Frame rate: 30fps or 60fps
- Audio: Clear microphone, separate track if possible
- Screen recording: OBS Studio, Camtasia, or similar

**Recording Checklist:**
- [ ] Test audio levels
- [ ] Close unnecessary applications
- [ ] Hide sensitive information
- [ ] Use large, readable fonts
- [ ] Record intro/hook
- [ ] Record main content
- [ ] Record outro/call-to-action

**File Naming:**
```
YYYY-MM-DD_tutorial-topic_v01.mp4
Example: 2025-01-08_python-basics_v01.mp4
```

### 4. Save Raw Footage

```bash
# Move recording to raw-footage directory
cp ~/Downloads/recording.mp4 raw-footage/2025-01-08_python-basics_v01.mp4
```

## Post-Production

### 5. Video Editing (Optional)

Before automated processing, you may want to:
- Trim dead air at start/end
- Remove mistakes or long pauses
- Add zoom effects for important parts
- Adjust audio levels

Use tools like:
- DaVinci Resolve (free)
- Adobe Premiere Pro
- Final Cut Pro
- Kdenlive (Linux)

### 6. Automated Processing

#### Option A: Batch Processing (Recommended for standard workflow)

```bash
# Process all videos in raw-footage/
bash scripts/batch_process.sh
```

This will:
1. Compress videos
2. Add intro/outro
3. Add watermark
4. Create 1080p and 720p versions

#### Option B: Custom Processing

```python
from scripts.process_video import VideoProcessor

# Initialize
processor = VideoProcessor('raw-footage/my-tutorial.mp4')

# Step 1: Compress
processor.compress_video(crf=23, preset='medium')

# Step 2: Get info
info = processor.get_video_info()
print(f"Duration: {info['format']['duration']} seconds")

# Step 3: Create YouTube formats
processor.create_youtube_formats()
```

### 7. Create Thumbnail

#### Quick Method:

```bash
python thumbnails/thumbnail_generator.py \
  raw-footage/my-tutorial.mp4 \
  "Learn Python - Complete Beginner Guide" \
  00:00:15
```

#### Custom Method:

```python
from thumbnails.thumbnail_generator import ThumbnailGenerator

gen = ThumbnailGenerator()

# Extract frame and customize
gen.create_thumbnail_from_video(
    video_file='raw-footage/my-tutorial.mp4',
    title='Learn Python',
    timestamp='00:00:15'
)

# Or create from scratch
gen.create_custom_thumbnail(
    background_color=(25, 25, 112),  # Midnight blue
    title='Learn Python',
    subtitle='Beginner Friendly',
    output_name='custom_thumb.jpg'
)
```

**Thumbnail Best Practices:**
- Use bright, contrasting colors
- Keep text large and readable (80px+)
- Include faces if possible (increases CTR)
- Use 1-3 words max
- Test on mobile screens
- Include branding consistently

### 8. Generate Metadata

```python
from metadata.youtube_metadata import YouTubeMetadataGenerator

gen = YouTubeMetadataGenerator()

# Create timestamps from your video
timestamps = [
    {"time": "0:00", "label": "Introduction"},
    {"time": "1:15", "label": "Setting up environment"},
    {"time": "3:45", "label": "Writing first program"},
    {"time": "7:20", "label": "Understanding variables"},
    {"time": "11:30", "label": "Functions explained"},
    {"time": "15:00", "label": "Practice exercises"},
    {"time": "18:45", "label": "Conclusion & next steps"}
]

# Generate metadata
metadata = gen.generate_metadata(
    title="Learn Python Programming - Complete Beginner Guide 2025",
    description="In this comprehensive tutorial, you'll learn Python from scratch...",
    tags=["python", "programming", "tutorial", "beginner", "coding", "2025"],
    timestamps=timestamps,
    links=[
        {"label": "Source Code", "url": "https://github.com/user/repo"},
        {"label": "Exercise Solutions", "url": "https://example.com/solutions"},
        {"label": "Discord Community", "url": "https://discord.gg/example"}
    ]
)
```

**SEO Tips:**
- Include year in title (e.g., "2025")
- Use keywords naturally
- Front-load important words
- Keep title under 60 characters
- Write compelling descriptions
- Add 10-15 relevant tags

## Publishing

### 9. YouTube Upload Preparation

Your files should now include:
- `processed-videos/tutorial_1080p.mp4` - Main upload
- `thumbnails/tutorial_thumbnail.jpg` - Custom thumbnail
- `metadata/tutorial_metadata.json` - Metadata (copy description/tags)

### 10. Upload to YouTube

1. Go to YouTube Studio
2. Click "Create" → "Upload videos"
3. Select your 1080p processed video
4. While uploading, fill in:
   - **Title**: Copy from metadata JSON
   - **Description**: Copy from metadata JSON
   - **Thumbnail**: Upload your generated thumbnail
   - **Playlist**: Add to relevant playlist
   - **Tags**: Copy from metadata JSON
   - **Category**: Usually "Education"

5. Add chapters:
   - YouTube auto-detects timestamps in description
   - Ensure first timestamp is 0:00

6. End screen:
   - Add subscribe button
   - Add video suggestions
   - Add playlist

7. Cards:
   - Link to previous video
   - Link to playlist
   - Link to website

### 11. Post-Publishing

- [ ] Share on social media
- [ ] Add to relevant playlists
- [ ] Pin a comment with resources
- [ ] Respond to early comments
- [ ] Monitor analytics after 24-48 hours

## Tutorial Series Workflow

For a series of tutorials:

```python
from metadata.youtube_metadata import TutorialSeriesManager

# Create series
series = TutorialSeriesManager("Python Mastery")
series.create_series(
    description="Complete Python programming course for beginners",
    playlist_id="PLxxxxxxxxxxxxxx"
)

# Add episodes
episodes = [
    ("Introduction to Python", "Get started with Python"),
    ("Variables and Data Types", "Learn about Python data types"),
    ("Control Flow", "If statements and loops"),
    # ... more episodes
]

for i, (title, desc) in enumerate(episodes, 1):
    series.add_episode(
        episode_number=i,
        title=title,
        description=desc,
        tags=["python", "tutorial", f"episode-{i}"]
    )
```

## Quality Checklist

Before uploading, verify:

### Video Quality
- [ ] Resolution: 1920x1080 minimum
- [ ] Audio: Clear, no background noise
- [ ] No dead air longer than 2-3 seconds
- [ ] Intro/outro present
- [ ] Watermark visible but not distracting
- [ ] File size reasonable (<2GB for YouTube)

### Content Quality
- [ ] Clear explanations
- [ ] Code visible and readable
- [ ] Pace appropriate for target audience
- [ ] Examples included
- [ ] Call-to-action at end

### Metadata Quality
- [ ] Title is SEO-optimized
- [ ] Description is comprehensive
- [ ] Timestamps accurate
- [ ] Tags relevant
- [ ] Links working
- [ ] Thumbnail attractive and readable

### Accessibility
- [ ] Captions/subtitles (auto-generated or custom)
- [ ] Clear audio
- [ ] Large text in code examples
- [ ] High contrast visuals

## Time Estimates

Typical timeline for a 15-minute tutorial:

- **Planning & Scripting**: 2-3 hours
- **Recording**: 1-2 hours (with retakes)
- **Editing**: 2-4 hours
- **Automated Processing**: 10-20 minutes
- **Thumbnail Creation**: 15-30 minutes
- **Metadata Generation**: 15-30 minutes
- **Upload & Publishing**: 30 minutes
- **Total**: ~6-10 hours

## Tips for Efficiency

1. **Batch Recording**: Record multiple tutorials in one session
2. **Templates**: Use consistent intro/outro/thumbnail styles
3. **Scripts**: Prepare detailed scripts to reduce retakes
4. **Automation**: Use batch processing for standard workflow
5. **Asset Library**: Build a library of reusable assets
6. **Keyboard Shortcuts**: Learn your editing software shortcuts
7. **Regular Schedule**: Establish a consistent upload schedule

## Common Issues & Solutions

### Issue: Video file too large
```bash
# Increase compression
python scripts/process_video.py input.mp4 --compress
# Then manually set higher CRF in the script (25-28)
```

### Issue: Audio quality poor
- Use noise reduction in Audacity
- Record in quiet environment
- Use a quality microphone
- Add audio normalization in post

### Issue: Text unreadable
- Increase font size (minimum 24px)
- Use high contrast colors
- Zoom in when showing code
- Use syntax highlighting

### Issue: Video too long
- Break into multiple parts
- Cut unnecessary content
- Increase playback speed of slow parts
- Add timestamps so viewers can skip

## Resources

### Recording Tools
- **OBS Studio**: Free, open-source
- **Camtasia**: Paid, beginner-friendly
- **ScreenFlow**: Mac only
- **ShareX**: Windows, free

### Editing Tools
- **DaVinci Resolve**: Free, professional
- **HitFilm Express**: Free
- **OpenShot**: Free, simple
- **Kdenlive**: Free, Linux

### Audio Tools
- **Audacity**: Free audio editing
- **Krisp**: Noise cancellation
- **Adobe Audition**: Professional

### Microphones
- **Budget**: Blue Snowball, Fifine K669
- **Mid-range**: Blue Yeti, Audio-Technica AT2020
- **Pro**: Shure SM7B, Rode PodMic

### Learning Resources
- YouTube Creator Academy
- VidIQ (SEO tool)
- TubeBuddy (Channel management)

## Next Steps

1. Review this workflow
2. Set up your production environment
3. Record your first tutorial
4. Run through the complete workflow
5. Upload and publish
6. Analyze performance
7. Iterate and improve

Happy creating!
