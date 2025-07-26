import moviepy.editor as mp

def extract_audio(video_path):
    print("🔊 استخراج الصوت من الفيديو...")
    video = mp.VideoFileClip(video_path)
    audio_path = "temp_audio.mp3"
    video.audio.write_audiofile(audio_path)
    return audio_path

def cut_clips(video_path, clip_times, output_dir):
    video = mp.VideoFileClip(video_path)
    paths = []
    for i, (start, end) in enumerate(clip_times):
        clip = video.subclip(start, end)
        path = f"{output_dir}/clip_{i+1}.mp4"
        clip.write_videofile(path, fps=30)
        paths.append(path)
    return paths
