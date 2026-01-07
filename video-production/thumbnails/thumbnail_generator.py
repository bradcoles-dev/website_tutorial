#!/usr/bin/env python3
"""
Automated Thumbnail Generator for YouTube Videos
Creates eye-catching thumbnails with text overlays and styling
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import subprocess
import os
from pathlib import Path
from typing import Optional, Tuple
import json


class ThumbnailGenerator:
    def __init__(self, output_dir: str = "../thumbnails"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # YouTube thumbnail dimensions
        self.width = 1280
        self.height = 720

    def extract_frame_from_video(self, video_file: str, timestamp: str = "00:00:05") -> Image.Image:
        """Extract a frame from video at specified timestamp"""
        temp_frame = self.output_dir / "temp_frame.jpg"

        cmd = [
            'ffmpeg',
            '-ss', timestamp,
            '-i', video_file,
            '-vframes', '1',
            '-q:v', '2',
            '-y',
            str(temp_frame)
        ]

        subprocess.run(cmd, check=True, capture_output=True)
        image = Image.open(temp_frame)
        temp_frame.unlink()  # Clean up temp file

        return image

    def create_thumbnail_from_video(self, video_file: str, title: str,
                                    timestamp: str = "00:00:05",
                                    output_name: Optional[str] = None) -> Path:
        """Create thumbnail from video frame with title overlay"""
        # Extract frame
        image = self.extract_frame_from_video(video_file, timestamp)

        # Resize to thumbnail dimensions
        image = image.resize((self.width, self.height), Image.Resampling.LANCZOS)

        # Add title overlay
        image = self.add_title_overlay(image, title)

        # Save
        if not output_name:
            video_name = Path(video_file).stem
            output_name = f"{video_name}_thumbnail.jpg"

        output_path = self.output_dir / output_name
        image.save(output_path, quality=95, optimize=True)

        print(f"Thumbnail saved to: {output_path}")
        return output_path

    def create_thumbnail_from_image(self, image_file: str, title: str,
                                    output_name: Optional[str] = None) -> Path:
        """Create thumbnail from static image with title overlay"""
        image = Image.open(image_file)

        # Resize to thumbnail dimensions
        image = image.resize((self.width, self.height), Image.Resampling.LANCZOS)

        # Add title overlay
        image = self.add_title_overlay(image, title)

        # Save
        if not output_name:
            output_name = f"{Path(image_file).stem}_thumbnail.jpg"

        output_path = self.output_dir / output_name
        image.save(output_path, quality=95, optimize=True)

        print(f"Thumbnail saved to: {output_path}")
        return output_path

    def add_title_overlay(self, image: Image.Image, title: str,
                         font_size: int = 80,
                         position: str = 'bottom',
                         bg_color: Tuple[int, int, int, int] = (0, 0, 0, 180),
                         text_color: Tuple[int, int, int] = (255, 255, 255)) -> Image.Image:
        """Add text overlay to image"""
        # Create drawing context
        draw = ImageDraw.Draw(image, 'RGBA')

        # Try to load a bold font, fallback to default
        try:
            # Try common font paths
            font_paths = [
                "C:/Windows/Fonts/arialbd.ttf",  # Windows
                "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",  # Linux
                "/System/Library/Fonts/Helvetica.ttc",  # macOS
            ]

            font = None
            for font_path in font_paths:
                if os.path.exists(font_path):
                    font = ImageFont.truetype(font_path, font_size)
                    break

            if font is None:
                font = ImageFont.load_default()
        except:
            font = ImageFont.load_default()

        # Calculate text size and position
        bbox = draw.textbbox((0, 0), title, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Add padding
        padding = 40
        box_height = text_height + padding * 2

        # Position the overlay
        if position == 'bottom':
            y_pos = self.height - box_height
        elif position == 'top':
            y_pos = 0
        else:  # center
            y_pos = (self.height - box_height) // 2

        # Draw semi-transparent background rectangle
        draw.rectangle(
            [(0, y_pos), (self.width, y_pos + box_height)],
            fill=bg_color
        )

        # Calculate centered text position
        x_pos = (self.width - text_width) // 2
        text_y = y_pos + padding

        # Add text shadow for better readability
        shadow_offset = 3
        draw.text((x_pos + shadow_offset, text_y + shadow_offset), title,
                 font=font, fill=(0, 0, 0, 200))

        # Draw main text
        draw.text((x_pos, text_y), title, font=font, fill=text_color)

        return image

    def add_branding(self, image: Image.Image, logo_file: str,
                    position: str = 'bottom-right',
                    scale: float = 0.15) -> Image.Image:
        """Add logo/branding to thumbnail"""
        if not os.path.exists(logo_file):
            print(f"Warning: Logo file not found: {logo_file}")
            return image

        logo = Image.open(logo_file)

        # Resize logo
        logo_width = int(self.width * scale)
        aspect_ratio = logo.height / logo.width
        logo_height = int(logo_width * aspect_ratio)
        logo = logo.resize((logo_width, logo_height), Image.Resampling.LANCZOS)

        # Calculate position
        padding = 20
        positions = {
            'top-left': (padding, padding),
            'top-right': (self.width - logo_width - padding, padding),
            'bottom-left': (padding, self.height - logo_height - padding),
            'bottom-right': (self.width - logo_width - padding,
                           self.height - logo_height - padding)
        }

        pos = positions.get(position, positions['bottom-right'])

        # Paste logo (handle transparency)
        if logo.mode == 'RGBA':
            image.paste(logo, pos, logo)
        else:
            image.paste(logo, pos)

        return image

    def apply_effects(self, image: Image.Image,
                     brightness: float = 1.0,
                     contrast: float = 1.0,
                     saturation: float = 1.0,
                     blur: bool = False) -> Image.Image:
        """Apply visual effects to enhance thumbnail"""
        # Brightness
        if brightness != 1.0:
            enhancer = ImageEnhance.Brightness(image)
            image = enhancer.enhance(brightness)

        # Contrast
        if contrast != 1.0:
            enhancer = ImageEnhance.Contrast(image)
            image = enhancer.enhance(contrast)

        # Saturation
        if saturation != 1.0:
            enhancer = ImageEnhance.Color(image)
            image = enhancer.enhance(saturation)

        # Slight blur for artistic effect
        if blur:
            image = image.filter(ImageFilter.GaussianBlur(radius=2))

        return image

    def create_custom_thumbnail(self, background_color: Tuple[int, int, int] = (30, 30, 30),
                               title: str = "Tutorial Title",
                               subtitle: str = "",
                               output_name: str = "custom_thumbnail.jpg") -> Path:
        """Create thumbnail from scratch with custom design"""
        # Create blank image
        image = Image.new('RGB', (self.width, self.height), background_color)
        draw = ImageDraw.Draw(image)

        # Load fonts
        try:
            font_paths = [
                "C:/Windows/Fonts/arialbd.ttf",
                "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            ]

            title_font = None
            for font_path in font_paths:
                if os.path.exists(font_path):
                    title_font = ImageFont.truetype(font_path, 90)
                    subtitle_font = ImageFont.truetype(font_path, 50)
                    break

            if title_font is None:
                title_font = ImageFont.load_default()
                subtitle_font = ImageFont.load_default()
        except:
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()

        # Draw title
        bbox = draw.textbbox((0, 0), title, font=title_font)
        text_width = bbox[2] - bbox[0]
        x_pos = (self.width - text_width) // 2
        y_pos = self.height // 3

        # Shadow
        draw.text((x_pos + 4, y_pos + 4), title, font=title_font, fill=(0, 0, 0))
        # Main text
        draw.text((x_pos, y_pos), title, font=title_font, fill=(255, 255, 255))

        # Draw subtitle if provided
        if subtitle:
            bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
            text_width = bbox[2] - bbox[0]
            x_pos = (self.width - text_width) // 2
            y_pos = self.height // 2 + 50

            draw.text((x_pos + 3, y_pos + 3), subtitle, font=subtitle_font, fill=(0, 0, 0))
            draw.text((x_pos, y_pos), subtitle, font=subtitle_font, fill=(200, 200, 200))

        # Save
        output_path = self.output_dir / output_name
        image.save(output_path, quality=95, optimize=True)

        print(f"Custom thumbnail saved to: {output_path}")
        return output_path


def main():
    import sys

    if len(sys.argv) < 3:
        print("Usage: python thumbnail_generator.py <video/image_file> <title> [timestamp]")
        print("\nExamples:")
        print("  python thumbnail_generator.py video.mp4 'Tutorial Title'")
        print("  python thumbnail_generator.py video.mp4 'Tutorial Title' 00:00:10")
        print("  python thumbnail_generator.py image.jpg 'Tutorial Title'")
        sys.exit(1)

    generator = ThumbnailGenerator()

    input_file = sys.argv[1]
    title = sys.argv[2]
    timestamp = sys.argv[3] if len(sys.argv) > 3 else "00:00:05"

    # Determine if input is video or image
    video_extensions = ['.mp4', '.mov', '.avi', '.mkv', '.webm']
    file_ext = Path(input_file).suffix.lower()

    if file_ext in video_extensions:
        generator.create_thumbnail_from_video(input_file, title, timestamp)
    else:
        generator.create_thumbnail_from_image(input_file, title)


if __name__ == '__main__':
    main()
