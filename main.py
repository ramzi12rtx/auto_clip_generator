from utils.fetch_pexels import download_free_video_from_pexels
from utils.clip_maker import make_clip
from utils.uploader import upload_to_youtube

def main():
    print("🎯 بدء العملية التلقائية")

    clip_path = None
    attempt = 0
    max_attempts = 5

    while clip_path is None and attempt < max_attempts:
        video_path = download_free_video_from_pexels()
        clip_path = make_clip(video_path, duration=10)
        attempt += 1

    if clip_path:
        print(f"✅ تم إنشاء الكليب: {clip_path}")
        try:
            upload_to_youtube(clip_path)
        except Exception as e:
            print(f"❌ Error uploading to YouTube: {e}")
    else:
        print("❌ لم نتمكن من العثور على فيديو مناسب بعد عدة محاولات.")

if __name__ == "__main__":
    main()
