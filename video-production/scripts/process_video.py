#!/usr/bin/env python3
"""
FFmpeg Video Processing Script
Handles common video processing tasks for tutorial content
"""

import subprocess
import os
import sys
import json
from pathlib import Path
from typing import Optional, List, Dict

class VideoProcessor:
    def __init__(self, input_file: str, output_dir: str = "../processed-videos"):
        self.input_file = Path(input_file)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        if not self.input_file.exists():
            raise FileNotFoundError(f"Input file not found: {input_file}")

    def get_video_info(self) -> Dict:
        """Get video metadata using ffprobe"""
        cmd = [
            'ffprobe',
            '-v', 'quiet',
            '-print_format', 'json',
            '-show_format',
            '-show_streams',
            str(self.input_file)
        ]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return json.loads(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error getting video info: {e}")
            return {}

    def compress_video(self, output_name: Optional[str] = None,
                       crf: int = 23, preset: str = 'medium') -> Path:
        """
        Compress video using H.264 codec
        CRF: 18-28 (lower = better quality, 23 is default)
        Preset: ultrafast, fast, medium, slow, veryslow
        """
        if not output_name:
            output_name = f"{self.input_file.stem}_compressed.mp4"

        output_file = self.output_dir / output_name

        cmd = [
            'ffmpeg',
            '-i', str(self.input_file),
            '-c:v', 'libx264',
            '-crf', str(crf),
            '-preset', preset,
            '-c:a', 'aac',
            '-b:a', '128k',
            '-y',
            str(output_file)
        ]

        print(f"Compressing video with CRF={crf}, preset={preset}...")
        subprocess.run(cmd, check=True)
        print(f"Compressed video saved to: {output_file}")
        return output_file

    def add_intro_outro(self, intro_file: Optional[str] = None,
                        outro_file: Optional[str] = None,
                        output_name: Optional[str] = None) -> Path:
        """Concatenate intro, main video, and outro"""
        if not output_name:
            output_name = f"{self.input_file.stem}_final.mp4"

        output_file = self.output_dir / output_name

        # Create concat file list
        concat_list = self.output_dir / 'concat_list.txt'
        with open(concat_list, 'w') as f:
            if intro_file and Path(intro_file).exists():
                f.write(f"file '{Path(intro_file).absolute()}'\n")
            f.write(f"file '{self.input_file.absolute()}'\n")
            if outro_file and Path(outro_file).exists():
                f.write(f"file '{Path(outro_file).absolute()}'\n")

        cmd = [
            'ffmpeg',
            '-f', 'concat',
            '-safe', '0',
            '-i', str(concat_list),
            '-c', 'copy',
            '-y',
            str(output_file)
        ]

        print("Adding intro/outro...")
        subprocess.run(cmd, check=True)
        concat_list.unlink()  # Clean up
        print(f"Final video saved to: {output_file}")
        return output_file

    def add_watermark(self, watermark_file: str, position: str = 'bottom-right',
                      output_name: Optional[str] = None) -> Path:
        """
        Add watermark to video
        Position: top-left, top-right, bottom-left, bottom-right
        """
        if not output_name:
            output_name = f"{self.input_file.stem}_watermarked.mp4"

        output_file = self.output_dir / output_name

        # Position mapping
        positions = {
            'top-left': '10:10',
            'top-right': 'W-w-10:10',
            'bottom-left': '10:H-h-10',
            'bottom-right': 'W-w-10:H-h-10'
        }

        overlay_pos = positions.get(position, 'W-w-10:H-h-10')

        cmd = [
            'ffmpeg',
            '-i', str(self.input_file),
            '-i', watermark_file,
            '-filter_complex', f'[1:v]scale=120:-1[wm];[0:v][wm]overlay={overlay_pos}',
            '-c:a', 'copy',
            '-y',
            str(output_file)
        ]

        print(f"Adding watermark at {position}...")
        subprocess.run(cmd, check=True)
        print(f"Watermarked video saved to: {output_file}")
        return output_file

    def extract_audio(self, output_name: Optional[str] = None) -> Path:
        """Extract audio track from video"""
        if not output_name:
            output_name = f"{self.input_file.stem}_audio.mp3"

        output_file = self.output_dir / output_name

        cmd = [
            'ffmpeg',
            '-i', str(self.input_file),
            '-vn',
            '-acodec', 'libmp3lame',
            '-q:a', '2',
            '-y',
            str(output_file)
        ]

        print("Extracting audio...")
        subprocess.run(cmd, check=True)
        print(f"Audio saved to: {output_file}")
        return output_file

    def create_clips(self, timestamps: List[tuple], output_prefix: str = "clip") -> List[Path]:
        """
        Create multiple clips from timestamps
        timestamps: [(start, end), ...] in format "HH:MM:SS" or seconds
        """
        clips = []

        for i, (start, end) in enumerate(timestamps, 1):
            output_file = self.output_dir / f"{output_prefix}_{i:02d}.mp4"

            cmd = [
                'ffmpeg',
                '-i', str(self.input_file),
                '-ss', str(start),
                '-to', str(end),
                '-c', 'copy',
                '-y',
                str(output_file)
            ]

            print(f"Creating clip {i}: {start} to {end}...")
            subprocess.run(cmd, check=True)
            clips.append(output_file)

        print(f"Created {len(clips)} clips")
        return clips

    def add_subtitles(self, subtitle_file: str, output_name: Optional[str] = None) -> Path:
        """Burn subtitles into video"""
        if not output_name:
            output_name = f"{self.input_file.stem}_subtitled.mp4"

        output_file = self.output_dir / output_name

        # Escape path for FFmpeg filter
        subtitle_path = str(Path(subtitle_file).absolute()).replace('\\', '/').replace(':', '\\:')

        cmd = [
            'ffmpeg',
            '-i', str(self.input_file),
            '-vf', f"subtitles='{subtitle_path}'",
            '-c:a', 'copy',
            '-y',
            str(output_file)
        ]

        print("Adding subtitles...")
        subprocess.run(cmd, check=True)
        print(f"Subtitled video saved to: {output_file}")
        return output_file

    def resize_video(self, width: int, height: int, output_name: Optional[str] = None) -> Path:
        """Resize video to specific dimensions"""
        if not output_name:
            output_name = f"{self.input_file.stem}_{width}x{height}.mp4"

        output_file = self.output_dir / output_name

        cmd = [
            'ffmpeg',
            '-i', str(self.input_file),
            '-vf', f'scale={width}:{height}',
            '-c:a', 'copy',
            '-y',
            str(output_file)
        ]

        print(f"Resizing video to {width}x{height}...")
        subprocess.run(cmd, check=True)
        print(f"Resized video saved to: {output_file}")
        return output_file

    def create_youtube_formats(self) -> Dict[str, Path]:
        """Create optimized versions for YouTube (1080p, 720p, etc.)"""
        formats = {}

        # 1080p
        print("Creating 1080p version...")
        formats['1080p'] = self.resize_video(1920, 1080, f"{self.input_file.stem}_1080p.mp4")

        # 720p
        print("Creating 720p version...")
        formats['720p'] = self.resize_video(1280, 720, f"{self.input_file.stem}_720p.mp4")

        return formats


def main():
    if len(sys.argv) < 2:
        print("Usage: python process_video.py <input_file> [options]")
        print("\nExamples:")
        print("  python process_video.py video.mp4 --compress")
        print("  python process_video.py video.mp4 --watermark logo.png")
        print("  python process_video.py video.mp4 --info")
        sys.exit(1)

    input_file = sys.argv[1]
    processor = VideoProcessor(input_file)

    # Simple command-line interface
    if '--info' in sys.argv:
        info = processor.get_video_info()
        print(json.dumps(info, indent=2))

    elif '--compress' in sys.argv:
        processor.compress_video()

    elif '--watermark' in sys.argv:
        idx = sys.argv.index('--watermark')
        if idx + 1 < len(sys.argv):
            watermark_file = sys.argv[idx + 1]
            processor.add_watermark(watermark_file)

    elif '--extract-audio' in sys.argv:
        processor.extract_audio()

    elif '--youtube' in sys.argv:
        processor.create_youtube_formats()

    else:
        print("No valid operation specified. Use --help for options.")


if __name__ == '__main__':
    main()
