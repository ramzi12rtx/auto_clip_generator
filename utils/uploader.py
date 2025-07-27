utils/uploader.py

import requests import os import pickle from google.oauth2.credentials import Credentials from googleapiclient.discovery import build from googleapiclient.http import MediaFileUpload

def get_trending_creative_commons_video(): api_key = os.getenv("YOUTUBE_API_KEY") if not api_key: raise Exception("❌ YOUTUBE_API_KEY not set in environment variables.")

trending_url = (
    "https://www.googleapis.com/youtube/v3/videos?"
    "part=snippet&chart=mostPopular&maxResults=10&regionCode=US"
    "&videoCategoryId=0&key=" + api_key
)

trending_response = requests.get(trending_url)
trending_data = trending_response.json()

for item in trending_data.get("items", []):
    video_id = item["id"]
    license_url = (
        f"https://www.googleapis.com/youtube/v3/videos?part=status&id={video_id}&key={api_key}"
    )
    license_response = requests.get(license_url).json()
    license_type = license_response["items"][0]["status"].get("license")

    if license_type == "creativeCommon":
        return f"https://www.youtube.com/watch?v={video_id}"

raise Exception("❌ No Creative Commons video found in trending list.")

def upload_to_youtube(video_path, title="AI Generated Clip", description="Clip generated automatically"): if not os.path.exists("token.pickle"): raise Exception("❌ token.pickle not found. You must authenticate first.")

with open("token.pickle", "rb") as token_file:
    creds = pickle.load(token_file)

youtube = build("youtube", "v3", credentials=creds)

request_body = {
    "snippet": {
        "title": title,
        "description": description,
        "tags": ["shorts", "AI", "clip"],
        "categoryId": "22"  # People & Blogs
    },
    "status": {
        "privacyStatus": "public"
    }
}

media = MediaFileUpload(video_path)

request = youtube.videos().insert(
    part="snippet,status",
    body=request_body,
    media_body=media
)

response = request.execute()
print(f"✅ تم رفع الفيديو: https://youtu.be/{response['id']}")

