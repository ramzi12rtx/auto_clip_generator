import requests
import uuid
import os

def download_video_from_pexels(query="nature"):
    api_key = os.getenv("PEXELS_API_KEY")
    headers = {"Authorization": api_key}
    url = f"https://api.pexels.com/videos/search?query={query}&per_page=1"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        video_url = data["videos"][0]["video_files"][0]["link"]

        output_path = f"assets/video_{uuid.uuid4().hex[:8]}.mp4"
        os.makedirs("assets", exist_ok=True)
        video_data = requests.get(video_url)
        with open(output_path, "wb") as f:
            f.write(video_data.content)
        print(f"✅ تم تحميل فيديو من Pexels: {output_path}")
        return output_path
    except Exception as e:
        print("❌ Error downloading from Pexels:", e)
        return None
