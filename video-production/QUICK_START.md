# Quick Start Guide

Get started with the Video Production Toolkit in 5 minutes!

## 1. Install Dependencies

```bash
# Install Python packages
pip install -r requirements.txt

# Verify FFmpeg is installed
ffmpeg -version
```

If FFmpeg is not installed:
- **Windows**: `choco install ffmpeg`
- **macOS**: `brew install ffmpeg`
- **Linux**: `sudo apt-get install ffmpeg`

## 2. Basic Configuration

Edit [config.yaml](config.yaml) and set:

```yaml
project:
  name: "Your Channel Name"
  author: "Your Name"
```

## 3. Process Your First Video

### Option A: Quick Single Video

```bash
# Place your video in raw-footage/
cp myvideo.mp4 raw-footage/

# Compress and optimize
python scripts/process_video.py raw-footage/myvideo.mp4 --compress

# Create thumbnail
python thumbnails/thumbnail_generator.py raw-footage/myvideo.mp4 "My Video Title"

# Generate metadata
python metadata/youtube_metadata.py "My Video Title" "Video description here" tutorial coding
```

### Option B: Full Automated Pipeline

```bash
# 1. Add your intro/outro/watermark (optional)
cp intro.mp4 assets/intro.mp4
cp outro.mp4 assets/outro.mp4
cp logo.png assets/overlays/watermark.png

# 2. Place videos in raw-footage/
cp *.mp4 raw-footage/

# 3. Run batch processing
bash scripts/batch_process.sh

# 4. Generate thumbnails for each video
python thumbnails/thumbnail_generator.py raw-footage/video1.mp4 "Title 1"
python thumbnails/thumbnail_generator.py raw-footage/video2.mp4 "Title 2"
```

## 4. Common Tasks

### Compress a Video
```bash
python scripts/process_video.py input.mp4 --compress
```

### Add Watermark
```bash
python scripts/process_video.py input.mp4 --watermark assets/overlays/logo.png
```

### Extract Audio
```bash
python scripts/process_video.py input.mp4 --extract-audio
```

### Create Multiple Resolutions
```bash
python scripts/process_video.py input.mp4 --youtube
# Creates 1080p and 720p versions
```

### Create Custom Thumbnail
```python
from thumbnails.thumbnail_generator import ThumbnailGenerator

gen = ThumbnailGenerator()
gen.create_custom_thumbnail(
    background_color=(30, 30, 30),
    title="My Tutorial",
    subtitle="Beginner Friendly"
)
```

### Generate Complete Metadata
```python
from metadata.youtube_metadata import YouTubeMetadataGenerator

gen = YouTubeMetadataGenerator()
gen.generate_metadata(
    title="My Tutorial Title",
    description="Learn something awesome",
    tags=["tutorial", "coding", "python"],
    timestamps=[
        {"time": "0:00", "label": "Intro"},
        {"time": "2:30", "label": "Main Content"},
        {"time": "10:00", "label": "Conclusion"}
    ]
)
```

## 5. Python API Examples

### Process Multiple Videos

```python
from scripts.process_video import VideoProcessor
from pathlib import Path

# Process all MP4 files
for video in Path('raw-footage').glob('*.mp4'):
    processor = VideoProcessor(str(video))
    processor.compress_video(crf=23)
    processor.create_youtube_formats()
```

### Batch Thumbnail Generation

```python
from thumbnails.thumbnail_generator import ThumbnailGenerator

gen = ThumbnailGenerator()

videos = [
    ('video1.mp4', 'Introduction to Python'),
    ('video2.mp4', 'Python Data Types'),
    ('video3.mp4', 'Python Functions'),
]

for video_file, title in videos:
    gen.create_thumbnail_from_video(
        f'raw-footage/{video_file}',
        title,
        timestamp='00:00:05'
    )
```

### Create Tutorial Series

```python
from metadata.youtube_metadata import TutorialSeriesManager

series = TutorialSeriesManager("Python Basics")
series.create_series(
    description="Learn Python from scratch",
    playlist_id="PLxxxxxx"
)

# Add episodes
for i in range(1, 11):
    series.add_episode(
        episode_number=i,
        title=f"Lesson {i}",
        description=f"Episode {i} of Python Basics",
        tags=["python", "tutorial", "beginner"]
    )
```

## 6. File Structure After Setup

```
video-production/
├── raw-footage/          # Your original recordings
│   └── tutorial.mp4
├── processed-videos/     # Automated output
│   ├── tutorial_compressed.mp4
│   ├── tutorial_1080p.mp4
│   └── tutorial_720p.mp4
├── thumbnails/           # Generated thumbnails
│   └── tutorial_thumbnail.jpg
├── metadata/             # Video metadata
│   └── tutorial_metadata.json
└── assets/              # Your branding assets
    ├── intro.mp4
    ├── outro.mp4
    └── overlays/
        └── watermark.png
```

## 7. Upload to YouTube

After processing:

1. **Video**: Use the `_1080p.mp4` file from `processed-videos/`
2. **Thumbnail**: Use the `.jpg` file from `thumbnails/`
3. **Metadata**: Copy title, description, and tags from `metadata/*.json`

## Next Steps

- Read the full [README.md](README.md) for advanced features
- Check [TUTORIAL_WORKFLOW.md](tutorials/TUTORIAL_WORKFLOW.md) for complete production workflow
- Customize [config.yaml](config.yaml) for your needs

## Troubleshooting

**FFmpeg errors**: Make sure FFmpeg is in your PATH
```bash
# Test FFmpeg
ffmpeg -version
```

**Python errors**: Ensure all packages are installed
```bash
pip install -r requirements.txt
```

**Permission errors** (Linux/Mac): Make scripts executable
```bash
chmod +x scripts/batch_process.sh
```

## Need Help?

- Check the [README.md](README.md) for detailed documentation
- Review example code in the scripts
- See [TUTORIAL_WORKFLOW.md](tutorials/TUTORIAL_WORKFLOW.md) for the complete workflow

Happy creating!
