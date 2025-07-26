from pytube import YouTube
import os

def download_youtube_video(video_url, output_path="downloads"):
    os.makedirs(output_path, exist_ok=True)
    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        print(f"⬇️ Downloading: {yt.title}")
        downloaded_path = stream.download(output_path)
        print(f"✅ Video downloaded to {downloaded_path}")
        return downloaded_path
    except Exception as e:
        print("❌ Error downloading video:", e)
        return None
