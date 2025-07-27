import os
from utils.fetch_pexels import download_free_video_from_pexels
from utils.clip_maker import make_clip
from utils.uploader import upload_to_youtube

def main():
    print("🎯 بدء العملية التلقائية")

    try:
        video_path = download_free_video_from_pexels()
    except Exception as e:
        print("❌ Error fetching video:", e)
        return

    try:
        clip_path = make_clip(video_path)
        print("✅ تم إنشاء الكليب:", clip_path)
    except Exception as e:
        print("❌ Error creating clip:", e)
        return

    try:
        upload_to_youtube(clip_path)
    except Exception as e:
        print("❌ Error uploading to YouTube:", e)

if __name__ == "__main__":
    main()
