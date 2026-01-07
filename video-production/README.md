# Video Production Toolkit

A comprehensive video production toolkit for creating tutorial content with automated FFmpeg processing, thumbnail generation, and YouTube metadata management.

## Project Structure

```
video-production/
├── scripts/              # Video processing scripts
│   ├── process_video.py  # Main video processor
│   └── batch_process.sh  # Batch processing script
├── thumbnails/           # Thumbnail generation
│   └── thumbnail_generator.py
├── metadata/             # YouTube metadata
│   └── youtube_metadata.py
├── raw-footage/          # Place raw video files here
├── processed-videos/     # Output processed videos
├── assets/               # Production assets
│   ├── fonts/           # Custom fonts
│   ├── overlays/        # Watermarks, logos
│   └── music/           # Background music
├── tutorials/            # Tutorial-specific content
└── config.yaml          # Configuration file
```

## Features

### 1. Video Processing (`scripts/process_video.py`)

Comprehensive FFmpeg-based video processing with:

- **Video Compression**: Optimize videos for web delivery
- **Intro/Outro Addition**: Add branded intros and outros
- **Watermarking**: Apply watermarks to protect content
- **Audio Extraction**: Extract audio tracks
- **Video Clipping**: Create clips from timestamps
- **Subtitle Burning**: Add hardcoded subtitles
- **Format Conversion**: Create multiple resolutions (1080p, 720p)
- **Video Information**: Extract metadata with ffprobe

#### Usage Examples

```bash
# Get video information
python scripts/process_video.py myvideo.mp4 --info

# Compress video
python scripts/process_video.py myvideo.mp4 --compress

# Add watermark
python scripts/process_video.py myvideo.mp4 --watermark assets/overlays/logo.png

# Extract audio
python scripts/process_video.py myvideo.mp4 --extract-audio

# Create YouTube formats (1080p, 720p)
python scripts/process_video.py myvideo.mp4 --youtube
```

#### Python API

```python
from scripts.process_video import VideoProcessor

# Initialize processor
processor = VideoProcessor('input.mp4', output_dir='./output')

# Compress video
processor.compress_video(crf=23, preset='medium')

# Add watermark
processor.add_watermark('logo.png', position='bottom-right')

# Create clips
timestamps = [
    ('00:00:00', '00:02:30'),
    ('00:02:30', '00:05:00')
]
processor.create_clips(timestamps, output_prefix='clip')

# Add intro and outro
processor.add_intro_outro(
    intro_file='intro.mp4',
    outro_file='outro.mp4'
)
```

### 2. Batch Processing (`scripts/batch_process.sh`)

Automated batch processing for multiple videos:

- Automatically processes all videos in `raw-footage/`
- Applies compression, intro/outro, watermark
- Creates multiple resolutions
- Preserves original files

#### Usage

```bash
# Process all videos in raw-footage directory
bash scripts/batch_process.sh
```

### 3. Thumbnail Generation (`thumbnails/thumbnail_generator.py`)

Create professional YouTube thumbnails:

- **Extract from Video**: Use a frame from your video
- **Custom Overlays**: Add text, branding, effects
- **Batch Generation**: Create thumbnails for multiple videos
- **Template-based**: Use predefined styles

#### Usage Examples

```bash
# Create thumbnail from video
python thumbnails/thumbnail_generator.py video.mp4 "Tutorial Title"

# Specify timestamp
python thumbnails/thumbnail_generator.py video.mp4 "Tutorial Title" 00:00:10

# Create thumbnail from image
python thumbnails/thumbnail_generator.py image.jpg "Tutorial Title"
```

#### Python API

```python
from thumbnails.thumbnail_generator import ThumbnailGenerator

generator = ThumbnailGenerator()

# From video frame
generator.create_thumbnail_from_video(
    video_file='tutorial.mp4',
    title='Learn Python in 10 Minutes',
    timestamp='00:00:05'
)

# From image
generator.create_thumbnail_from_image(
    image_file='background.jpg',
    title='Advanced JavaScript'
)

# Custom thumbnail
generator.create_custom_thumbnail(
    background_color=(30, 30, 30),
    title='Tutorial Title',
    subtitle='Beginner Friendly'
)
```

### 4. YouTube Metadata Generator (`metadata/youtube_metadata.py`)

Generate complete YouTube metadata:

- **Titles & Descriptions**: SEO-optimized
- **Tags**: Auto-generated tags
- **Timestamps**: Chapter markers
- **Links**: Resource links
- **Series Management**: Organize tutorial series

#### Usage Examples

```bash
# Generate metadata
python metadata/youtube_metadata.py "Tutorial Title" "Learn how to code" python tutorial coding
```

#### Python API

```python
from metadata.youtube_metadata import YouTubeMetadataGenerator, TutorialSeriesManager

# Single video
generator = YouTubeMetadataGenerator()

metadata = generator.generate_metadata(
    title="Learn Python - Complete Tutorial",
    description="A comprehensive guide to Python programming",
    tags=["python", "tutorial", "programming"],
    timestamps=[
        {"time": "0:00", "label": "Introduction"},
        {"time": "2:15", "label": "Setup"},
        {"time": "5:30", "label": "First Program"}
    ],
    links=[
        {"label": "GitHub", "url": "https://github.com/user/repo"},
        {"label": "Docs", "url": "https://docs.example.com"}
    ]
)

# Tutorial series
series = TutorialSeriesManager("Python Basics")
series.create_series("Learn Python from scratch", playlist_id="PLxxxx")

series.add_episode(
    episode_number=1,
    title="Getting Started",
    description="Install Python and set up your environment",
    tags=["python", "setup", "beginner"]
)
```

## Installation

### Requirements

1. **Python 3.7+**
2. **FFmpeg** (must be in PATH)
3. **Python packages**:

```bash
pip install Pillow PyYAML
```

### FFmpeg Installation

**Windows:**
```bash
# Using Chocolatey
choco install ffmpeg

# Or download from https://ffmpeg.org/download.html
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

## Quick Start

### 1. Setup

```bash
# Navigate to video-production directory
cd video-production

# Install Python dependencies
pip install Pillow PyYAML

# Verify FFmpeg installation
ffmpeg -version
```

### 2. Configure

Edit [config.yaml](config.yaml) with your settings:

```yaml
project:
  name: "My Tutorial Series"
  author: "Your Name"

youtube:
  default_tags:
    - "tutorial"
    - "coding"

  standard_links:
    - label: "GitHub"
      url: "https://github.com/yourusername"
```

### 3. Add Assets

```bash
# Add intro/outro videos
cp intro.mp4 assets/intro.mp4
cp outro.mp4 assets/outro.mp4

# Add watermark/logo
cp logo.png assets/overlays/watermark.png
```

### 4. Process Videos

```bash
# Place raw videos in raw-footage/
cp myvideo.mp4 raw-footage/

# Run batch processing
bash scripts/batch_process.sh

# Or process individually
python scripts/process_video.py raw-footage/myvideo.mp4 --youtube
```

### 5. Create Thumbnails

```bash
python thumbnails/thumbnail_generator.py raw-footage/myvideo.mp4 "My Tutorial Title"
```

### 6. Generate Metadata

```python
python metadata/youtube_metadata.py "My Tutorial Title" "Learn something awesome" tutorial coding
```

## Workflow Example

Complete workflow for a new tutorial:

```bash
# 1. Place raw footage
cp tutorial_recording.mp4 raw-footage/

# 2. Process video
python scripts/process_video.py raw-footage/tutorial_recording.mp4 --compress
python scripts/process_video.py processed-videos/tutorial_recording_compressed.mp4 --watermark assets/overlays/watermark.png

# 3. Generate thumbnail
python thumbnails/thumbnail_generator.py raw-footage/tutorial_recording.mp4 "Learn Python Basics"

# 4. Create metadata
python -c "
from metadata.youtube_metadata import YouTubeMetadataGenerator

gen = YouTubeMetadataGenerator()
gen.generate_metadata(
    title='Learn Python Basics - Complete Tutorial',
    description='A beginner-friendly guide to Python',
    tags=['python', 'tutorial', 'beginner', 'programming'],
    timestamps=[
        {'time': '0:00', 'label': 'Introduction'},
        {'time': '2:30', 'label': 'Variables'},
        {'time': '5:15', 'label': 'Functions'}
    ]
)
"
```

## Advanced Usage

### Custom Video Processing Pipeline

```python
from scripts.process_video import VideoProcessor

processor = VideoProcessor('input.mp4')

# Step 1: Compress
compressed = processor.compress_video(crf=20, preset='slow')

# Step 2: Add watermark (use compressed video)
processor_2 = VideoProcessor(compressed)
watermarked = processor_2.add_watermark('logo.png')

# Step 3: Add intro/outro
processor_3 = VideoProcessor(watermarked)
final = processor_3.add_intro_outro(
    intro_file='intro.mp4',
    outro_file='outro.mp4'
)
```

### Batch Thumbnail Generation

```python
from thumbnails.thumbnail_generator import ThumbnailGenerator
from pathlib import Path

generator = ThumbnailGenerator()

videos = Path('raw-footage').glob('*.mp4')
titles = [
    "Episode 1: Introduction",
    "Episode 2: Advanced Topics",
    "Episode 3: Conclusion"
]

for video, title in zip(videos, titles):
    generator.create_thumbnail_from_video(str(video), title)
```

### Series Management

```python
from metadata.youtube_metadata import TutorialSeriesManager

# Create series
series = TutorialSeriesManager("Web Development Bootcamp")
series.create_series(
    description="Learn web development from scratch",
    playlist_id="PLxxxxxx"
)

# Add episodes
for i, (title, desc) in enumerate(episodes, 1):
    series.add_episode(
        episode_number=i,
        title=title,
        description=desc,
        tags=["webdev", "tutorial"]
    )
```

## Configuration Reference

See [config.yaml](config.yaml) for all available options:

- **Video settings**: Compression, formats, watermarks
- **Thumbnail settings**: Dimensions, fonts, colors, effects
- **YouTube settings**: Categories, tags, links, playlists
- **Batch processing**: Parallel processing, automation

## Tips & Best Practices

1. **Video Quality**: Use CRF 20-23 for high quality, 23-28 for smaller files
2. **Thumbnails**: Use bright colors and large text for better click-through rates
3. **Metadata**: Include timestamps for better viewer retention
4. **Watermarks**: Keep them subtle but visible
5. **File Organization**: Use descriptive names for raw footage
6. **Backups**: Always keep original raw footage

## Troubleshooting

### FFmpeg not found
```bash
# Verify FFmpeg is installed
ffmpeg -version

# Add to PATH if needed (Windows)
setx PATH "%PATH%;C:\path\to\ffmpeg\bin"
```

### Font errors in thumbnails
```bash
# The script will fall back to default font if custom fonts aren't found
# To use custom fonts, place .ttf files in assets/fonts/
```

### Permission errors (Linux/Mac)
```bash
# Make scripts executable
chmod +x scripts/batch_process.sh
```

## Contributing

Feel free to extend and customize these scripts for your needs!

## License

MIT License - Feel free to use for personal or commercial projects.
