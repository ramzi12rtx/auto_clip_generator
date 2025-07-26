import os
from utils.audio_transcript import transcribe_audio
from utils.clip_selector import select_important_clips
from utils.video_tools import extract_audio, cut_clips
from utils.clip_editor import style_clip

INPUT_VIDEO = "input_video.mp4"
OUTPUT_DIR = "output"

def main():
    print("🎬 بدء استخراج المقاطع القصيرة...")

    # 1. استخراج الصوت
    audio_path = extract_audio(INPUT_VIDEO)

    # 2. تحويل الصوت إلى نص
    transcript_segments = transcribe_audio(audio_path)

    # 3. اختيار أهم المقاطع من النص
    clips = select_important_clips(transcript_segments)

    # 4. تقطيع الفيديو
    clip_paths = cut_clips(INPUT_VIDEO, clips, OUTPUT_DIR)

    # 5. منتجة المقاطع وإضافة مؤثرات
    final_clips = [style_clip(path) for path in clip_paths]

    print("✅ تم إنشاء المقاطع:")
    for clip in final_clips:
        print("▶", clip)

if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    main()
