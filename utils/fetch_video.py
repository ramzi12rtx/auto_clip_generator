import os import yt_dlp from datetime import datetime

def fetch_video(query, download_path="downloads"): os.makedirs(download_path, exist_ok=True)

ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': f'{download_path}/%(title)s.%(ext)s',
    'quiet': True,
    'noplaylist': True,
}

search_url = f"ytsearch1:{query}"

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(search_url, download=True)
    video_info = info_dict['entries'][0]
    video_path = ydl.prepare_filename(video_info)

print(f"✅ Downloaded video: {video_path}")
return video_path

