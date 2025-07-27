from utils.fetch_trending import get_trending_video_url
from utils.downloader import download_youtube_video
from utils.clip_maker import make_clip
from utils.audio_transcriber import extract_audio_and_transcribe
from utils.subtitle_adder import add_subtitles
from utils.uploader import upload_to_youtube
import os

def main():
    print("🎯 بدء العملية التلقائية")

    # 1. جلب رابط فيديو رائج
    try:
        video_url = get_trending_video_url()
        print("✅ رابط الفيديو الرائج:", video_url)
    except Exception as e:
        print("❌ Error getting trending video:", e)
        return

    # 2. تحميل الفيديو
    try:
        video_path = download_youtube_video(video_url)
        print("✅ تم تحميل الفيديو:", video_path)
    except Exception as e:
        print("❌ Error downloading video:", e)
        return

    # 3. إنشاء كليب قصير
    try:
        clip_path = make_clip(video_path)
        print("✅ تم إنشاء كليب:", clip_path)
    except Exception as e:
        print("❌ Error creating clip:", e)
        return

    # 4. تفريغ الصوت وترجمة
    try:
        srt_path = extract_audio_and_transcribe(clip_path)
        print("✅ تم تفريغ الصوت:", srt_path)
    except Exception as e:
        print("❌ Error transcribing:", e)
        return

    # 5. إضافة الترجمة
    try:
        subtitled_path = add_subtitles(clip_path, srt_path)
        print("✅ تم إنتاج فيديو بالترجمة:", subtitled_path)
    except Exception as e:
        print("❌ Error adding subtitles:", e)
        return

    # 6. رفع الفيديو
    try:
        upload_to_youtube(subtitled_path)
    except Exception as e:
        print("❌ Error uploading video:", e)

if __name__ == "__main__":
    main()
