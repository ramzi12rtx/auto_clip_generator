from pytube import YouTube
import os

def download_youtube_video(video_url, output_dir="downloads"):
    os.makedirs(output_dir, exist_ok=True)
    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        output_path = stream.download(output_path=output_dir)
        print(f"✅ Downloaded video to {output_path}")
        return output_path
    except Exception as e:
        print(f"❌ Error downloading video: {e}")
        return None
