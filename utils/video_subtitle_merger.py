import subprocess
import os

def merge_subtitles_with_video(video_path, subtitle_path, output_path="output/video_with_subs.mp4"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    try:
        cmd = [
            "ffmpeg",
            "-i", video_path,
            "-vf", f"subtitles={subtitle_path}",
            "-c:a", "copy",
            output_path
        ]
        subprocess.run(cmd, check=True)
        print(f"✅ Video with subtitles saved to: {output_path}")
        return output_path
    except subprocess.CalledProcessError as e:
        print(f"❌ FFmpeg error: {e}")
        return None
