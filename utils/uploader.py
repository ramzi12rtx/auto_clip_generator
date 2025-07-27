# utils/uploader.py

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os
import pickle

def upload_to_youtube(video_path, title="AI Generated Clip", description="Clip generated automatically"):
    # تحميل التوكن المحفوظ
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
