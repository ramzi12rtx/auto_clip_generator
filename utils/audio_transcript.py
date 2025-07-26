import whisper

def transcribe_audio(audio_path):
    print("📝 تحويل الصوت إلى نص...")
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    
    return result["segments"]  # يحتوي على التوقيت والنص
