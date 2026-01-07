#!/usr/bin/env python3
"""
YouTube Metadata Generator
Creates and manages metadata for YouTube video uploads including
titles, descriptions, tags, and timestamps
"""

import json
import yaml
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime


class YouTubeMetadataGenerator:
    def __init__(self, project_name: str = "Tutorial Series"):
        self.project_name = project_name
        self.metadata_dir = Path("../metadata")
        self.metadata_dir.mkdir(parents=True, exist_ok=True)

    def generate_metadata(self,
                         title: str,
                         description: str,
                         tags: List[str],
                         category: str = "Education",
                         timestamps: Optional[List[Dict[str, str]]] = None,
                         links: Optional[List[Dict[str, str]]] = None,
                         output_file: Optional[str] = None) -> Dict:
        """Generate complete YouTube metadata"""

        # Build description with timestamps and links
        full_description = self._build_description(
            description, timestamps, links
        )

        metadata = {
            "title": title,
            "description": full_description,
            "tags": tags,
            "category": category,
            "privacyStatus": "public",  # public, unlisted, private
            "madeForKids": False,
            "embeddable": True,
            "license": "youtube",  # youtube or creativeCommon
            "publicStatsViewable": True,
            "publishAt": None,  # Schedule publish time (ISO 8601)
            "recordingDate": datetime.now().strftime("%Y-%m-%d"),
            "playlist": None,  # Playlist ID to add video to
            "language": "en",
            "defaultAudioLanguage": "en"
        }

        # Save to file
        if output_file:
            self._save_metadata(metadata, output_file)
        else:
            # Generate filename from title
            safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).rstrip()
            safe_title = safe_title.replace(' ', '_')[:50]
            output_file = f"{safe_title}_metadata.json"
            self._save_metadata(metadata, output_file)

        return metadata

    def _build_description(self,
                          base_description: str,
                          timestamps: Optional[List[Dict[str, str]]] = None,
                          links: Optional[List[Dict[str, str]]] = None) -> str:
        """Build complete description with timestamps and links"""

        parts = [base_description, ""]

        # Add timestamps
        if timestamps:
            parts.append("📌 TIMESTAMPS")
            parts.append("-" * 40)
            for ts in timestamps:
                parts.append(f"{ts['time']} - {ts['label']}")
            parts.append("")

        # Add links
        if links:
            parts.append("🔗 LINKS & RESOURCES")
            parts.append("-" * 40)
            for link in links:
                parts.append(f"{link['label']}: {link['url']}")
            parts.append("")

        # Add standard footer
        parts.extend(self._get_standard_footer())

        return "\n".join(parts)

    def _get_standard_footer(self) -> List[str]:
        """Get standard footer for all videos"""
        return [
            "━━━━━━━━━━━━━━━━━━━━━━━━",
            "📺 SUBSCRIBE for more tutorials!",
            "👍 Like this video if you found it helpful",
            "💬 Leave a comment with your questions",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━",
            "🔔 Turn on notifications to never miss a video!",
            "",
            "#tutorial #coding #programming"
        ]

    def _save_metadata(self, metadata: Dict, filename: str):
        """Save metadata to JSON file"""
        output_path = self.metadata_dir / filename

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)

        print(f"Metadata saved to: {output_path}")

        # Also save as YAML for easier editing
        yaml_path = output_path.with_suffix('.yaml')
        with open(yaml_path, 'w', encoding='utf-8') as f:
            yaml.dump(metadata, f, default_flow_style=False, allow_unicode=True)

        print(f"YAML version saved to: {yaml_path}")

    def create_from_template(self, template_name: str, **kwargs) -> Dict:
        """Create metadata from predefined template"""

        templates = {
            "tutorial": {
                "category": "Education",
                "tags": ["tutorial", "programming", "coding", "education", "learn"],
                "standard_links": [
                    {"label": "GitHub Repository", "url": "https://github.com/yourusername/repo"},
                    {"label": "Documentation", "url": "https://docs.example.com"},
                ]
            },
            "quick_tip": {
                "category": "Education",
                "tags": ["quick tip", "programming", "coding", "howto"],
                "standard_links": []
            },
            "project_showcase": {
                "category": "Science & Technology",
                "tags": ["project", "showcase", "demo", "coding"],
                "standard_links": [
                    {"label": "Live Demo", "url": "https://demo.example.com"},
                    {"label": "GitHub", "url": "https://github.com/yourusername/project"},
                ]
            }
        }

        template = templates.get(template_name, templates["tutorial"])

        # Merge template with provided kwargs
        metadata_kwargs = {
            "category": template["category"],
            "tags": template["tags"] + kwargs.get("additional_tags", []),
            "links": template.get("standard_links", []) + kwargs.get("additional_links", []),
        }

        # Required fields from kwargs
        metadata_kwargs.update({
            "title": kwargs.get("title", ""),
            "description": kwargs.get("description", ""),
            "timestamps": kwargs.get("timestamps", []),
            "output_file": kwargs.get("output_file", None)
        })

        return self.generate_metadata(**metadata_kwargs)

    def generate_seo_tags(self, base_tags: List[str], topic: str) -> List[str]:
        """Generate SEO-optimized tags"""
        # YouTube allows up to 500 characters for tags
        seo_tags = base_tags.copy()

        # Add variations
        topic_words = topic.lower().split()
        for word in topic_words:
            if len(word) > 3:  # Skip short words
                seo_tags.append(word)

        # Add common variations
        common_tags = [
            "tutorial",
            "how to",
            "learn",
            "beginner",
            "guide",
            "programming",
            "coding",
            "development",
            "software"
        ]

        for tag in common_tags:
            if tag not in seo_tags:
                seo_tags.append(tag)

        # Remove duplicates and limit to reasonable number
        seo_tags = list(dict.fromkeys(seo_tags))[:15]

        return seo_tags

    def parse_timestamps_from_text(self, text: str) -> List[Dict[str, str]]:
        """Parse timestamps from formatted text"""
        timestamps = []

        for line in text.strip().split('\n'):
            line = line.strip()
            if not line:
                continue

            # Expected format: "00:00 - Introduction"
            parts = line.split(' - ', 1)
            if len(parts) == 2:
                time_str, label = parts
                timestamps.append({
                    "time": time_str.strip(),
                    "label": label.strip()
                })

        return timestamps

    def create_batch_metadata(self, videos_info: List[Dict]) -> List[str]:
        """Create metadata for multiple videos at once"""
        created_files = []

        for video in videos_info:
            metadata = self.generate_metadata(
                title=video['title'],
                description=video['description'],
                tags=video.get('tags', []),
                category=video.get('category', 'Education'),
                timestamps=video.get('timestamps', []),
                links=video.get('links', []),
                output_file=video.get('output_file', None)
            )
            created_files.append(metadata)

        print(f"\nCreated metadata for {len(created_files)} videos")
        return created_files

    def load_metadata(self, filename: str) -> Dict:
        """Load metadata from file"""
        file_path = self.metadata_dir / filename

        if file_path.suffix == '.yaml':
            with open(file_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        else:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)

    def update_metadata(self, filename: str, updates: Dict) -> Dict:
        """Update existing metadata file"""
        metadata = self.load_metadata(filename)
        metadata.update(updates)
        self._save_metadata(metadata, filename)
        return metadata


class TutorialSeriesManager:
    """Manage metadata for a series of tutorial videos"""

    def __init__(self, series_name: str):
        self.series_name = series_name
        self.generator = YouTubeMetadataGenerator(series_name)
        self.series_file = self.generator.metadata_dir / f"{series_name}_series.json"

    def create_series(self, description: str, playlist_id: Optional[str] = None):
        """Initialize a new tutorial series"""
        series_data = {
            "series_name": self.series_name,
            "description": description,
            "playlist_id": playlist_id,
            "videos": [],
            "created_at": datetime.now().isoformat()
        }

        with open(self.series_file, 'w') as f:
            json.dump(series_data, f, indent=2)

        print(f"Created series: {self.series_name}")

    def add_episode(self, episode_number: int, title: str, **kwargs):
        """Add episode to series with auto-numbering"""
        # Load series
        with open(self.series_file, 'r') as f:
            series_data = json.load(f)

        # Generate episode title
        full_title = f"{self.series_name} #{episode_number}: {title}"

        # Add series description to video description
        series_desc = f"Part {episode_number} of the {self.series_name} series.\n\n{kwargs.get('description', '')}"

        # Create metadata
        metadata = self.generator.generate_metadata(
            title=full_title,
            description=series_desc,
            tags=kwargs.get('tags', []) + [self.series_name.lower().replace(' ', '_')],
            category=kwargs.get('category', 'Education'),
            timestamps=kwargs.get('timestamps', []),
            links=kwargs.get('links', []),
            output_file=f"{self.series_name.replace(' ', '_')}_ep{episode_number:02d}_metadata.json"
        )

        # Update playlist if set
        if series_data.get('playlist_id'):
            metadata['playlist'] = series_data['playlist_id']

        # Add to series
        series_data['videos'].append({
            "episode": episode_number,
            "title": full_title,
            "metadata_file": f"{self.series_name.replace(' ', '_')}_ep{episode_number:02d}_metadata.json"
        })

        # Save series
        with open(self.series_file, 'w') as f:
            json.dump(series_data, f, indent=2)

        print(f"Added episode {episode_number} to series")


def main():
    import sys

    generator = YouTubeMetadataGenerator()

    if len(sys.argv) < 3:
        print("YouTube Metadata Generator")
        print("\nUsage:")
        print("  python youtube_metadata.py <title> <description> [tags...]")
        print("\nExample:")
        print("  python youtube_metadata.py 'My Tutorial' 'Learn to code' python tutorial coding")
        sys.exit(1)

    title = sys.argv[1]
    description = sys.argv[2]
    tags = sys.argv[3:] if len(sys.argv) > 3 else []

    # Example timestamps
    timestamps = [
        {"time": "0:00", "label": "Introduction"},
        {"time": "1:30", "label": "Main Content"},
        {"time": "8:45", "label": "Conclusion"}
    ]

    metadata = generator.generate_metadata(
        title=title,
        description=description,
        tags=tags,
        timestamps=timestamps
    )

    print("\nMetadata created successfully!")
    print(f"Title: {metadata['title']}")
    print(f"Tags: {', '.join(metadata['tags'])}")


if __name__ == '__main__':
    main()
