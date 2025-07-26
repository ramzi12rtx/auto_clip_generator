from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import pysrt
import os

def add_subtitles(video_path, srt_path):
    try:
        # Load video
        video = VideoFileClip(video_path)
        subs = pysrt.open(srt_path)
        clips = []

        for sub in subs:
            txt = sub.text.replace('\n', ' ')
            start = sub.start.ordinal / 1000.0
            end = sub.end.ordinal / 1000.0

            txt_clip = TextClip(
                txt,
                fontsize=48,
                color='white',
                font='Arial-Bold',
                stroke_color='black',
                stroke_width=2,
                method='caption',
                size=(video.w * 0.9, None),
                align='center'
            ).set_position(('center', 'bottom')).set_start(start).set_duration(end - start)

            clips.append(txt_clip)

        final = CompositeVideoClip([video, *clips])
        output_path = f"{os.path.splitext(video_path)[0]}_subtitled.mp4"
        final.write_videofile(output_path, codec='libx264', audio_codec='aac')

        return output_path

    except Exception as e:
        print("❌ Error adding subtitles:", e)
        return None
