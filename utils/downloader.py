import subprocess
import uuid

def download_youtube_video(url):
    video_id = str(uuid.uuid4())[:8]
    output_path = f"assets/video_{video_id}.mp4"
    command = [
        "yt-dlp",
        "--no-playlist",
        "--no-check-certificate",
        "--match-filter", "license='Creative Commons'",
        "-f", "mp4",
        "-o", output_path,
        url
    ]
    subprocess.run(command, check=True)
    return output_path
