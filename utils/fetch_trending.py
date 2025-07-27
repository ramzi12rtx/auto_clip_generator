import os
import requests

def get_trending_video_url():
    api_key = os.getenv("YOUTUBE_API_KEY")
    if not api_key:
        raise Exception("❌ YOUTUBE_API_KEY not set in environment variables.")

    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&regionCode=US&maxResults=5&videoCategoryId=0&key={api_key}"
    response = requests.get(url).json()

    for video in response.get("items", []):
        license_info = video["snippet"].get("license", "youtube")
        if license_info.lower() == "creative commons":
            return f"https://www.youtube.com/watch?v={video['id']}"

    # fallback to first if no creative commons found
    return f"https://www.youtube.com/watch?v={response['items'][0]['id']}"
