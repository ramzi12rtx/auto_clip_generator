import os
from moviepy.editor import VideoFileClip

def split_video(input_path, clip_duration=30, output_dir="clips"):
    os.makedirs(output_dir, exist_ok=True)

    try:
        video = VideoFileClip(input_path)
        total_duration = int(video.duration)
        clips = []

        for i in range(0, total_duration, clip_duration):
            start = i
            end = min(i + clip_duration, total_duration)
            subclip = video.subclip(start, end)

            clip_path = os.path.join(output_dir, f"clip_{start}_{end}.mp4")
            subclip.write_videofile(clip_path, codec="libx264", audio_codec="aac")
            clips.append(clip_path)
            print(f"✅ Saved clip: {clip_path}")

        video.close()
        return clips

    except Exception as e:
        print(f"❌ Error splitting video: {e}")
        return []
