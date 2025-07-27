import requests
import os

def get_trending_video_url(region_code='US'):
    api_key = os.getenv("YOUTUBE_API_KEY")
    if not api_key:
        raise Exception("❌ YOUTUBE_API_KEY not set in environment variables.")
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&maxResults=1&regionCode={region_code}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    video_id = data["items"][0]["id"]
    return f"https://www.youtube.com/watch?v={video_id}"
