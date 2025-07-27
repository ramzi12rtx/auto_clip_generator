import subprocess
import uuid

def download_youtube_video(url):
    try:
        output_path = f"assets/video_{uuid.uuid4().hex[:8]}.mp4"
        command = [
            "yt-dlp", "--no-playlist",
            "-f", "mp4",
            "--no-check-certificate",  # لتجنب مشاكل SSL
            "-o", output_path,
            url
        ]
        subprocess.run(command, check=True)
        return output_path
    except Exception as e:
        print("❌ Error downloading video:", e)
        return None
