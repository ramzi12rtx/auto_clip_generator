import os
from utils.downloader import download_youtube_video
from utils.clip_maker import make_clip
from utils.audio_transcriber import extract_audio_and_transcribe
from utils.subtitle_adder import add_subtitles
from utils.uploader import upload_to_youtube

def main():
    print("🎯 بدء العملية التلقائية")

    try:
        video_path = download_youtube_video()
        print(f"✅ تم تحميل الفيديو: {video_path}")
    except Exception as e:
        print("❌ Error downloading video:", e)
        return

    try:
        clip_path = make_clip(video_path)
        print(f"✅ تم إنشاء كليب: {clip_path}")
    except Exception as e:
        print("❌ Error creating clip:", e)
        return

    try:
        srt_path = extract_audio_and_transcribe(clip_path)
        print(f"✅ تم تفريغ الصوت إلى: {srt_path}")
    except Exception as e:
        print("❌ Error transcribing audio:", e)
        return

    try:
        final_video = add_subtitles(clip_path, srt_path)
        print(f"✅ تم إضافة الترجمة: {final_video}")
    except Exception as e:
        print("❌ Error adding subtitles:", e)
        return

    try:
        upload_to_youtube(final_video, "Clip created from trending video")
    except Exception as e:
        print("❌ Error uploading video:", e)

if __name__ == "__main__":
    main()
