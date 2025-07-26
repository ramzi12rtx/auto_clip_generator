from moviepy.editor import VideoFileClip
import os
import tempfile
import whisper

def extract_audio_and_transcribe(video_path):
    # استخراج الصوت من الفيديو
    clip = VideoFileClip(video_path)
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_audio:
        audio_path = tmp_audio.name
        clip.audio.write_audiofile(audio_path, logger=None)

    # تحميل نموذج Whisper
    model = whisper.load_model("base")

    # تفريغ الصوت إلى نص
    result = model.transcribe(audio_path)
    transcript = result["text"]

    # حذف الملف المؤقت
    os.remove(audio_path)

    return transcript.strip()
