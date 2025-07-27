from moviepy.editor import VideoFileClip

def make_clip(video_path, start=0, duration=30):
    clip = VideoFileClip(video_path).subclip(start, start + duration)
    clip = clip.resize((1080, 1920))  # فيديو طولي
    output_path = "output/short_clip.mp4"
    clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
    return output_path
