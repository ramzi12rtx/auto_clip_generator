from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os, pickle

def upload_to_youtube(video_path, title, description):
    creds = None
    if os.path.exists('token.pickle'):
        creds = pickle.load(open('token.pickle', 'rb'))
    else:
        raise Exception("❌ لا يوجد token.pickle — قم بتنفيذ OAuth flow أولًا.")

    youtube = build("youtube", "v3", credentials=creds)
    req = youtube.videos().insert(
        part="snippet,status",
        body={"snippet": {"title": title, "description": description, "categoryId": "22"},
              "status": {"privacyStatus": "public"}},
        media_body=MediaFileUpload(video_path)
    )
    resp = req.execute()
    print(f"✅ Uploaded: https://youtu.be/{resp['id']}")
