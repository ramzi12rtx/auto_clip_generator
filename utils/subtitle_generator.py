import whisper
import os

def generate_subtitles(audio_path, output_srt_path="output/subtitles.srt"):
    os.makedirs(os.path.dirname(output_srt_path), exist_ok=True)

    try:
        model = whisper.load_model("base")  # يمكنك تغييره إلى "small" أو "medium" أو "large"
        result = model.transcribe(audio_path)

        # حفظ الترجمة بصيغة SRT
        with open(output_srt_path, "w", encoding="utf-8") as f:
            for i, segment in enumerate(result["segments"]):
                start = format_timestamp(segment["start"])
                end = format_timestamp(segment["end"])
                text = segment["text"].strip()
                f.write(f"{i+1}\n{start} --> {end}\n{text}\n\n")

        print(f"✅ Subtitles saved to {output_srt_path}")
        return output_srt_path
    except Exception as e:
        print(f"❌ Error generating subtitles: {e}")
        return None


def format_timestamp(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"
