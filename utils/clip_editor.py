import moviepy.editor as mp
from moviepy.video.fx import resize

def style_clip(path):
    print(f"✨ منتجة الفيديو: {path}")
    clip = mp.VideoFileClip(path)
    
    # تحويل إلى حجم طولي 9:16
    vertical_clip = resize.resize(clip, height=1080).crop(x_center=clip.w/2, width=607)
    
    output_path = path.replace(".mp4", "_styled.mp4")
    vertical_clip.write_videofile(output_path, fps=30)
    return output_path
