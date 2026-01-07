#!/usr/bin/env python3
"""
Complete Video Production Workflow
Automates the entire pipeline: processing, thumbnail, and metadata generation
"""

import sys
import argparse
from pathlib import Path
import yaml

# Add parent directory to path to import our modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.process_video import VideoProcessor
from thumbnails.thumbnail_generator import ThumbnailGenerator
from metadata.youtube_metadata import YouTubeMetadataGenerator


class WorkflowManager:
    def __init__(self, config_file: str = "../config.yaml"):
        self.config = self._load_config(config_file)
        self.video_processor = None
        self.thumbnail_gen = ThumbnailGenerator()
        self.metadata_gen = YouTubeMetadataGenerator(
            self.config['project']['name']
        )

    def _load_config(self, config_file: str) -> dict:
        """Load configuration from YAML file"""
        config_path = Path(__file__).parent / config_file
        if config_path.exists():
            with open(config_path, 'r') as f:
                return yaml.safe_load(f)
        else:
            print(f"Warning: Config file not found at {config_path}")
            return self._default_config()

    def _default_config(self) -> dict:
        """Return default configuration"""
        return {
            'project': {'name': 'Tutorial Series'},
            'video': {
                'compression': {'crf': 23, 'preset': 'medium'},
                'watermark': {'enabled': False}
            },
            'youtube': {
                'defaults': {'category': 'Education'},
                'default_tags': ['tutorial', 'coding']
            }
        }

    def process_video(self, input_file: str, output_dir: str = "../processed-videos") -> Path:
        """Process video with compression and optimization"""
        print(f"\n{'='*60}")
        print(f"STEP 1/3: Processing Video")
        print(f"{'='*60}\n")

        self.video_processor = VideoProcessor(input_file, output_dir)

        # Compress video
        print("Compressing video...")
        crf = self.config['video']['compression']['crf']
        preset = self.config['video']['compression']['preset']

        compressed = self.video_processor.compress_video(
            crf=crf,
            preset=preset,
            output_name=f"{Path(input_file).stem}_compressed.mp4"
        )

        # Add watermark if enabled
        if self.config['video']['watermark'].get('enabled', False):
            watermark_file = self.config['video']['watermark'].get('file')
            if watermark_file and Path(watermark_file).exists():
                print("Adding watermark...")
                processor = VideoProcessor(compressed, output_dir)
                position = self.config['video']['watermark'].get('position', 'bottom-right')
                compressed = processor.add_watermark(
                    watermark_file,
                    position=position,
                    output_name=f"{Path(input_file).stem}_final.mp4"
                )

        # Create YouTube formats
        print("Creating YouTube-optimized formats...")
        processor = VideoProcessor(compressed, output_dir)
        formats = processor.create_youtube_formats()

        print(f"\n✓ Video processing complete!")
        print(f"  1080p: {formats['1080p']}")
        print(f"  720p: {formats['720p']}")

        return formats['1080p']

    def create_thumbnail(self, video_file: str, title: str,
                        timestamp: str = "00:00:05") -> Path:
        """Generate thumbnail from video"""
        print(f"\n{'='*60}")
        print(f"STEP 2/3: Creating Thumbnail")
        print(f"{'='*60}\n")

        thumbnail = self.thumbnail_gen.create_thumbnail_from_video(
            video_file=video_file,
            title=title,
            timestamp=timestamp
        )

        print(f"\n✓ Thumbnail created: {thumbnail}")
        return thumbnail

    def generate_metadata(self, title: str, description: str,
                         tags: list = None,
                         timestamps: list = None,
                         links: list = None) -> dict:
        """Generate YouTube metadata"""
        print(f"\n{'='*60}")
        print(f"STEP 3/3: Generating Metadata")
        print(f"{'='*60}\n")

        # Merge tags with defaults
        if tags is None:
            tags = []
        default_tags = self.config['youtube'].get('default_tags', [])
        all_tags = list(set(tags + default_tags))

        # Merge links with standard links
        if links is None:
            links = []
        standard_links = self.config['youtube'].get('standard_links', [])
        all_links = standard_links + links

        metadata = self.metadata_gen.generate_metadata(
            title=title,
            description=description,
            tags=all_tags,
            category=self.config['youtube']['defaults']['category'],
            timestamps=timestamps,
            links=all_links
        )

        print(f"\n✓ Metadata generated!")
        print(f"  Title: {metadata['title']}")
        print(f"  Tags: {', '.join(metadata['tags'][:5])}...")

        return metadata

    def complete_workflow(self, video_file: str, title: str,
                         description: str,
                         tags: list = None,
                         timestamps: list = None,
                         links: list = None,
                         thumbnail_timestamp: str = "00:00:05") -> dict:
        """Run complete workflow: video processing, thumbnail, and metadata"""
        print(f"\n{'#'*60}")
        print(f"# Complete Video Production Workflow")
        print(f"# Video: {Path(video_file).name}")
        print(f"# Title: {title}")
        print(f"{'#'*60}")

        # Step 1: Process video
        processed_video = self.process_video(video_file)

        # Step 2: Create thumbnail
        thumbnail = self.create_thumbnail(video_file, title, thumbnail_timestamp)

        # Step 3: Generate metadata
        metadata = self.generate_metadata(
            title=title,
            description=description,
            tags=tags,
            timestamps=timestamps,
            links=links
        )

        # Summary
        print(f"\n{'='*60}")
        print(f"WORKFLOW COMPLETE!")
        print(f"{'='*60}")
        print(f"\n📹 Video (upload this): {processed_video}")
        print(f"🖼️  Thumbnail: {thumbnail}")
        print(f"📝 Metadata: {Path(metadata.get('_metadata_file', 'metadata'))}")
        print(f"\nReady for YouTube upload! 🚀\n")

        return {
            'video': str(processed_video),
            'thumbnail': str(thumbnail),
            'metadata': metadata
        }


def main():
    parser = argparse.ArgumentParser(
        description='Complete video production workflow automation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage
  python complete_workflow.py video.mp4 "My Tutorial" "Learn something cool"

  # With tags
  python complete_workflow.py video.mp4 "Python Tutorial" "Learn Python" --tags python coding tutorial

  # With thumbnail timestamp
  python complete_workflow.py video.mp4 "My Tutorial" "Description" --thumbnail-time 00:00:10

  # With timestamps for chapters
  python complete_workflow.py video.mp4 "Tutorial" "Description" \\
    --timestamps "0:00,Introduction" "2:30,Setup" "5:00,Coding"
        """
    )

    parser.add_argument('video_file', help='Input video file')
    parser.add_argument('title', help='Video title')
    parser.add_argument('description', help='Video description')
    parser.add_argument('--tags', nargs='+', help='Video tags', default=[])
    parser.add_argument('--timestamps', nargs='+',
                       help='Timestamps in format "time,label" e.g. "0:00,Intro"',
                       default=[])
    parser.add_argument('--links', nargs='+',
                       help='Links in format "label,url"',
                       default=[])
    parser.add_argument('--thumbnail-time', default='00:00:05',
                       help='Timestamp for thumbnail extraction (default: 00:00:05)')
    parser.add_argument('--config', default='../config.yaml',
                       help='Config file path (default: ../config.yaml)')

    args = parser.parse_args()

    # Parse timestamps
    timestamps = []
    for ts in args.timestamps:
        if ',' in ts:
            time, label = ts.split(',', 1)
            timestamps.append({'time': time.strip(), 'label': label.strip()})

    # Parse links
    links = []
    for link in args.links:
        if ',' in link:
            label, url = link.split(',', 1)
            links.append({'label': label.strip(), 'url': url.strip()})

    # Run workflow
    workflow = WorkflowManager(args.config)
    workflow.complete_workflow(
        video_file=args.video_file,
        title=args.title,
        description=args.description,
        tags=args.tags,
        timestamps=timestamps if timestamps else None,
        links=links if links else None,
        thumbnail_timestamp=args.thumbnail_time
    )


if __name__ == '__main__':
    main()
