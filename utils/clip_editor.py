import os from moviepy.editor import VideoFileClip

def split_video_to_clips(input_path, output_folder, clip_duration=30): os.makedirs(output_folder, exist_ok=True)

video = VideoFileClip(input_path)
video_duration = int(video.duration)

clip_paths = []
for i in range(0, video_duration, clip_duration):
    start = i
    end = min(i + clip_duration, video_duration)
    output_path = os.path.join(output_folder, f"clip_{start}_{end}.mp4")
    clip = video.subclip(start, end)
    clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
    clip_paths.append(output_path)

video.close()
return clip_paths

