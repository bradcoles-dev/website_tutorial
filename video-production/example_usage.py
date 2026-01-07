#!/usr/bin/env python3
"""
Example Usage Script
Demonstrates how to use the video production toolkit
"""

from pathlib import Path

# Example 1: Basic Video Processing
def example_video_processing():
    """Process a video with compression and optimization"""
    print("=" * 60)
    print("Example 1: Basic Video Processing")
    print("=" * 60)

    from scripts.process_video import VideoProcessor

    # Initialize processor
    processor = VideoProcessor('raw-footage/my-video.mp4')

    # Get video information
    info = processor.get_video_info()
    print(f"Video duration: {info.get('format', {}).get('duration', 'unknown')}")

    # Compress video
    compressed = processor.compress_video(crf=23, preset='medium')
    print(f"Compressed video: {compressed}")

    # Create YouTube formats
    formats = processor.create_youtube_formats()
    print(f"1080p: {formats['1080p']}")
    print(f"720p: {formats['720p']}")


# Example 2: Thumbnail Creation
def example_thumbnail_creation():
    """Create a thumbnail from video or image"""
    print("\n" + "=" * 60)
    print("Example 2: Thumbnail Creation")
    print("=" * 60)

    from thumbnails.thumbnail_generator import ThumbnailGenerator

    generator = ThumbnailGenerator()

    # From video frame
    thumbnail = generator.create_thumbnail_from_video(
        video_file='raw-footage/my-video.mp4',
        title='Learn Python Programming',
        timestamp='00:00:05'
    )
    print(f"Thumbnail created: {thumbnail}")

    # Custom thumbnail
    custom = generator.create_custom_thumbnail(
        background_color=(25, 25, 112),  # Midnight blue
        title='Tutorial Title',
        subtitle='Beginner Friendly',
        output_name='custom_example.jpg'
    )
    print(f"Custom thumbnail: {custom}")


# Example 3: Metadata Generation
def example_metadata_generation():
    """Generate YouTube metadata"""
    print("\n" + "=" * 60)
    print("Example 3: Metadata Generation")
    print("=" * 60)

    from metadata.youtube_metadata import YouTubeMetadataGenerator

    generator = YouTubeMetadataGenerator("My Tutorial Series")

    # Create metadata
    metadata = generator.generate_metadata(
        title="Learn Python - Complete Beginner Guide",
        description="In this comprehensive tutorial, you'll learn Python from scratch.",
        tags=["python", "programming", "tutorial", "beginner"],
        timestamps=[
            {"time": "0:00", "label": "Introduction"},
            {"time": "2:30", "label": "Setup"},
            {"time": "5:00", "label": "First Program"},
            {"time": "10:00", "label": "Conclusion"}
        ],
        links=[
            {"label": "Source Code", "url": "https://github.com/user/repo"},
            {"label": "Discord", "url": "https://discord.gg/community"}
        ]
    )

    print(f"Title: {metadata['title']}")
    print(f"Tags: {', '.join(metadata['tags'])}")
    print(f"Category: {metadata['category']}")


# Example 4: Tutorial Series Management
def example_series_management():
    """Manage a tutorial series"""
    print("\n" + "=" * 60)
    print("Example 4: Tutorial Series Management")
    print("=" * 60)

    from metadata.youtube_metadata import TutorialSeriesManager

    # Create series
    series = TutorialSeriesManager("Python Basics")
    series.create_series(
        description="Complete Python programming course",
        playlist_id="PLxxxxxx"
    )

    # Add episodes
    episodes = [
        ("Getting Started", "Install Python and setup environment"),
        ("Variables and Data Types", "Learn about Python variables"),
        ("Control Flow", "If statements and loops"),
    ]

    for i, (title, desc) in enumerate(episodes, 1):
        series.add_episode(
            episode_number=i,
            title=title,
            description=desc,
            tags=["python", "tutorial", f"episode-{i}"]
        )

    print(f"Created series with {len(episodes)} episodes")


# Example 5: Complete Workflow
def example_complete_workflow():
    """Run complete workflow for a video"""
    print("\n" + "=" * 60)
    print("Example 5: Complete Workflow")
    print("=" * 60)

    from scripts.complete_workflow import WorkflowManager

    workflow = WorkflowManager()

    # Process everything
    result = workflow.complete_workflow(
        video_file='raw-footage/my-video.mp4',
        title='My Tutorial Title',
        description='Learn something awesome in this tutorial',
        tags=['tutorial', 'coding', 'python'],
        timestamps=[
            {"time": "0:00", "label": "Intro"},
            {"time": "1:00", "label": "Setup"},
            {"time": "5:00", "label": "Coding"},
            {"time": "10:00", "label": "Conclusion"}
        ],
        thumbnail_timestamp='00:00:05'
    )

    print(f"Video: {result['video']}")
    print(f"Thumbnail: {result['thumbnail']}")
    print("Metadata: See metadata/ directory")


# Example 6: Batch Processing
def example_batch_processing():
    """Process multiple videos"""
    print("\n" + "=" * 60)
    print("Example 6: Batch Processing")
    print("=" * 60)

    from scripts.process_video import VideoProcessor
    from pathlib import Path

    # Get all videos
    raw_footage = Path('raw-footage')
    videos = list(raw_footage.glob('*.mp4'))

    print(f"Found {len(videos)} videos to process")

    for video in videos:
        print(f"\nProcessing: {video.name}")

        processor = VideoProcessor(str(video))

        # Compress
        compressed = processor.compress_video(crf=23)
        print(f"  ✓ Compressed: {compressed}")

        # Create formats
        processor_2 = VideoProcessor(compressed)
        formats = processor_2.create_youtube_formats()
        print(f"  ✓ 1080p: {formats['1080p']}")
        print(f"  ✓ 720p: {formats['720p']}")


# Example 7: Advanced Video Editing
def example_advanced_editing():
    """Advanced video editing features"""
    print("\n" + "=" * 60)
    print("Example 7: Advanced Video Editing")
    print("=" * 60)

    from scripts.process_video import VideoProcessor

    processor = VideoProcessor('raw-footage/my-video.mp4')

    # Create clips from timestamps
    clips = processor.create_clips([
        ('00:00:00', '00:02:30'),  # Intro segment
        ('00:02:30', '00:05:00'),  # Main content
        ('00:05:00', '00:06:00'),  # Outro
    ], output_prefix='segment')

    print(f"Created {len(clips)} clips")

    # Add intro and outro
    final = processor.add_intro_outro(
        intro_file='assets/intro.mp4',
        outro_file='assets/outro.mp4'
    )
    print(f"Final video with intro/outro: {final}")

    # Add watermark
    processor_2 = VideoProcessor(final)
    watermarked = processor_2.add_watermark(
        'assets/overlays/watermark.png',
        position='bottom-right'
    )
    print(f"Watermarked video: {watermarked}")


# Example 8: Custom Thumbnail Styling
def example_custom_thumbnails():
    """Create custom styled thumbnails"""
    print("\n" + "=" * 60)
    print("Example 8: Custom Thumbnail Styling")
    print("=" * 60)

    from thumbnails.thumbnail_generator import ThumbnailGenerator
    from PIL import Image

    generator = ThumbnailGenerator()

    # Create thumbnail with custom styling
    thumbnail = generator.create_thumbnail_from_video(
        video_file='raw-footage/my-video.mp4',
        title='Advanced Tutorial',
        timestamp='00:00:10'
    )

    # Load and apply effects
    image = Image.open(thumbnail)
    image_with_effects = generator.apply_effects(
        image,
        brightness=1.1,
        contrast=1.2,
        saturation=1.3
    )

    # Add branding
    if Path('assets/overlays/logo.png').exists():
        final_image = generator.add_branding(
            image_with_effects,
            'assets/overlays/logo.png',
            position='bottom-right',
            scale=0.15
        )
        final_image.save('thumbnails/branded_thumbnail.jpg', quality=95)
        print("Created branded thumbnail with effects")


# Main function to run examples
def main():
    """Run all examples"""
    print("\n" + "#" * 60)
    print("# Video Production Toolkit - Example Usage")
    print("#" * 60)

    examples = [
        ("Video Processing", example_video_processing),
        ("Thumbnail Creation", example_thumbnail_creation),
        ("Metadata Generation", example_metadata_generation),
        ("Series Management", example_series_management),
        ("Complete Workflow", example_complete_workflow),
        ("Batch Processing", example_batch_processing),
        ("Advanced Editing", example_advanced_editing),
        ("Custom Thumbnails", example_custom_thumbnails),
    ]

    print("\nAvailable Examples:")
    for i, (name, _) in enumerate(examples, 1):
        print(f"  {i}. {name}")

    print("\nNote: These are code examples showing how to use the tools.")
    print("To run them, you need actual video files in raw-footage/")
    print("\nRecommended: Start with the complete workflow:")
    print("  python scripts/complete_workflow.py video.mp4 'Title' 'Description'")

    # Uncomment to run specific examples:
    # example_metadata_generation()
    # example_series_management()


if __name__ == '__main__':
    main()
