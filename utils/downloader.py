import subprocess
import os
import uuid

def download_youtube_video(url):
    filename = f"assets/video_{uuid.uuid4().hex[:8]}.mp4"
    try:
        os.makedirs("assets", exist_ok=True)
        cmd = [
            "yt-dlp",
            "-f", "mp4",
            "-o", filename,
            url
        ]
        subprocess.run(cmd, check=True)
        print(f"✅ تم تحميل الفيديو: {filename}")
        return filename
    except Exception as e:
        print("❌ Error downloading video:", e)
        return None
