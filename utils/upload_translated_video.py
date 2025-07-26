import os
import google.auth
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

def upload_translated_video(video_path, title, description=""):
    CLIENT_ID = os.getenv("YOUTUBE_CLIENT_ID")
    CLIENT_SECRET = os.getenv("YOUTUBE_CLIENT_SECRET")
    REFRESH_TOKEN = os.getenv("YOUTUBE_REFRESH_TOKEN")

    if not (CLIENT_ID and CLIENT_SECRET and REFRESH_TOKEN):
        raise Exception("❌ YouTube OAuth credentials not set in environment variables.")

    creds = Credentials(
        token=None,
        refresh_token=REFRESH_TOKEN,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        scopes=["https://www.googleapis.com/auth/youtube.upload"]
    )
    creds.refresh(Request())

    youtube = build("youtube", "v3", credentials=creds)

    request_body = {
        "snippet": {
            "title": title[:100],
            "description": description or "Video clip with automatic subtitles",
            "tags": ["shorts", "AI", "translation", "clips"],
            "categoryId": "22"
        },
        "status": {
            "privacyStatus": "public"
        }
    }

    media = MediaFileUpload(video_path, resumable=True)

    print("📤 Uploading video...")
    request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media
    )

    response = request.execute()
    print(f"✅ Video uploaded: https://youtu.be/{response['id']}")
