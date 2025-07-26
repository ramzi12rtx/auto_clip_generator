main.py

import os from utils.fetch_video import download_youtube_video from utils.clip_editor import extract_clip from utils.subtitles import add_subtitles from utils.video_enhancer import enhance_video from utils.uploader import upload_to_youtube from datetime import datetime

def main(): print("🚀 بدء العملية...")

# 1. تنزيل فيديو عشوائي من YouTube
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # مثال، استبدله أو اجعل جلبه تلقائي
video_path = download_youtube_video(video_url)

# 2. استخراج كليب قصير (مثلاً من الثانية 30 إلى 60)
clip_path = extract_clip(video_path, start_time=30, duration=30)

# 3. إضافة ترجمة تلقائية للكليب
subtitled_path = add_subtitles(clip_path)

# 4. تحسين جودة الفيديو (فلاتر، تعديل الأبعاد، الخ)
enhanced_path = enhance_video(subtitled_path)

# 5. إعادة نشر الكليب على YouTube
upload_to_youtube(enhanced_path)

print("✅ تم نشر الفيديو بنجاح!")

if name == "main": main()

