import requests
import os

def get_trending_video_url():
    api_key = os.getenv("YOUTUBE_API_KEY")
    if not api_key:
        raise Exception("❌ YOUTUBE_API_KEY not set in environment variables.")

    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&maxResults=10&regionCode=US&videoCategoryId=0&key={api_key}"

    response = requests.get(url)
    data = response.json()

    for item in data.get("items", []):
        if item["status"]["license"] == "creativeCommon":
            return f"https://www.youtube.com/watch?v={item['id']}"

    raise Exception("❌ لا يوجد فيديوهات Creative Commons في الترند.")
