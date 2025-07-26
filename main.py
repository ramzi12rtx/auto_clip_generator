import os
from utils.downloader import download_youtube_video
from utils.clip_maker import make_clip
from utils.audio_transcriber import extract_audio_and_transcribe
from utils.video_subtitle_merger import merge_subtitles_with_video
from utils.upload_translated_video import upload_translated_video

def main():
    print("🎯 بدء العملية التلقائية")

    # 1. تحميل فيديو يوتيوب
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # ✅ عدله لرابط الفيديو الأصلي
    video_path = download_youtube_video(url)
    print(f"✅ تم تحميل الفيديو: {video_path}")

    # 2. تقطيع الفيديو إلى كليب قصير
    clip_path = make_clip(video_path, start_time=30, duration=30)
    print(f"✅ تم إنشاء كليب: {clip_path}")

    # 3. استخراج الصوت وإنشاء الترجمة
    srt_path = extract_audio_and_transcribe(clip_path)
    print(f"✅ تم استخراج الترجمة: {srt_path}")

    # 4. دمج الترجمة مع الفيديو
    final_video_path = merge_subtitles_with_video(clip_path, srt_path)
    print(f"✅ تم إنشاء الفيديو النهائي: {final_video_path}")

    # 5. رفع الفيديو إلى يوتيوب
    upload_translated_video(
        video_path=final_video_path,
        title="📌 معلومة سريعة مترجمة!",
        description="كليب مترجم تلقائيًا باستخدام الذكاء الاصطناعي"
    )

if __name__ == "__main__":
    main()
