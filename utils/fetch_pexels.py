import os
import requests
import random
import uuid

def download_free_video_from_pexels(query="technology", output_folder="assets"):
    api_key = os.getenv("PEXELS_API_KEY")
    headers = {
        "Authorization": api_key
    }

    url = f"https://api.pexels.com/videos/search?query={query}&per_page=10"
    response = requests.get(url, headers=headers)
    data = response.json()

    if "videos" not in data or len(data["videos"]) == 0:
        raise Exception("❌ No videos found on Pexels for this query.")

    video_url = random.choice(data["videos"])["video_files"][0]["link"]
    filename = f"video_{uuid.uuid4().hex[:8]}.mp4"
    output_path = os.path.join(output_folder, filename)

    print(f"🎥 Downloading video from Pexels: {video_url}")
    video_data = requests.get(video_url).content
    os.makedirs(output_folder, exist_ok=True)

    with open(output_path, "wb") as f:
        f.write(video_data)

    print(f"✅ تم تحميل الفيديو إلى: {output_path}")
    return output_path
