import os
from utils.downloader import download_youtube_video
from utils.clip_maker import make_clip
from utils.audio_transcriber import extract_audio_and_transcribe
from utils.subtitle_adder import add_subtitles
from utils.uploader import upload_to_youtube
from utils.trending_fetcher import fetch_trending_videos

def main():
    api_key = os.getenv("YOUTUBE_API_KEY")
    videos = fetch_trending_videos(api_key, region_code='US', max_results=3)
    if not videos:
        print("❌ لم يتم العثور على فيديوهات رائجة")
        return

    for vid in videos:
        print("🔁 معالجة:", vid['title'])
        path = download_youtube_video(vid['url'])
        if not path:
            continue
        clip = make_clip(path)
        if not clip:
            continue
        srt = extract_audio_and_transcribe(clip)
        if not srt:
            continue
        subtitled = add_subtitles(clip, srt)
        if not subtitled:
            continue
        upload_to_youtube(subtitled, title=vid['title'])
        break
