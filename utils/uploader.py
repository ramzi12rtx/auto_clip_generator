import os
import pickle
import requests
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def get_trending_creative_commons_video(api_key):
    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        "part": "snippet",
        "chart": "mostPopular",
        "regionCode": "US",
        "videoCategoryId": "",  # اتركه فارغًا لجميع الفئات
        "maxResults": 10,
        "key": api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    for item in data.get("items", []):
        video_id = item["id"]
        license_type = item["snippet"].get("license", "")
        if license_type == "creativeCommon":
            return f"https://www.youtube.com/watch?v={video_id}"

    raise Exception("❌ لم يتم العثور على فيديو Creative Commons.")

def upload_to_youtube(video_path, title="AI Generated Clip", description="Clip generated automatically"):
    if not os.path.exists("token.pickle"):
        raise Exception("❌ token.pickle not found. You must authenticate first.")

    with open("token.pickle", "rb") as token_file:
        creds = pickle.load(token_file)

    youtube = build("youtube", "v3", credentials=creds)

    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": ["shorts", "AI", "clip"],
            "categoryId": "22"
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
