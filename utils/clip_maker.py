from moviepy.editor import VideoFileClip
import os

def make_clip(video_path, output_path='output/short_clip.mp4', duration=10):
    if not os.path.exists(video_path):
        print(f"❌ الفيديو غير موجود: {video_path}")
        return None

    try:
        clip = VideoFileClip(video_path)
        if clip.duration < duration:
            print(f"❌ الفيديو قصير جداً ({clip.duration:.2f} ث). نعيد المحاولة...")
            clip.close()
            return None

        start = max(0, (clip.duration - duration) / 2)
        subclip = clip.subclip(start, start + duration)
        subclip.write_videofile(output_path, codec="libx264", audio_codec="aac")
        clip.close()
        subclip.close()
        return output_path
    except Exception as e:
        print(f"❌ Error creating clip: {e}")
        return None
