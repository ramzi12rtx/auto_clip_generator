import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

def upload_to_youtube(video_path, title, description):
    try:
        client_id = os.getenv("YOUTUBE_CLIENT_ID")
        client_secret = os.getenv("YOUTUBE_CLIENT_SECRET")
        refresh_token = os.getenv("YOUTUBE_REFRESH_TOKEN")

        if not client_id or not client_secret or not refresh_token:
            raise Exception("❌ Missing YouTube credentials in environment variables")

        credentials = Credentials(
            token=None,
            refresh_token=refresh_token,
            token_uri="https://oauth2.googleapis.com/token",
            client_id=client_id,
            client_secret=client_secret,
            scopes=["https://www.googleapis.com/auth/youtube.upload"]
        )
        credentials.refresh(Request())

        youtube = build("youtube", "v3", credentials=credentials)

        request_body = {
            "snippet": {
                "title": title[:100],
                "description": description,
                "tags": ["shorts", "viral", "motivation", "AI"],
                "categoryId": "22"  # People & Blogs
            },
            "status": {
                "privacyStatus": "public",  # or "unlisted"
                "madeForKids": False
            }
        }

        media = MediaFileUpload(video_path)

        response = youtube.videos().insert(
            part="snippet,status",
            body=request_body,
            media_body=media
        ).execute()

        print(f"✅ تم رفع الفيديو بنجاح: https://youtu.be/{response['id']}")

    except Exception as e:
        print("❌ Error uploading to YouTube:", e)
