from moviepy.editor import VideoFileClip
import os
from datetime import datetime

def make_clip(input_path, start_time=0, duration=30, output_dir="clips"):
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        clip = VideoFileClip(input_path).subclip(start_time, start_time + duration)

        # اسم الملف بناء على التاريخ
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        output_path = os.path.join(output_dir, f"clip_{timestamp}.mp4")
        clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

        print(f"✅ Clip saved to {output_path}")
        return output_path

    except Exception as e:
        print(f"❌ Error creating clip: {e}")
        return None
