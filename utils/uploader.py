def get_trending_video_url():
    query = "motivational speeches"
    api_key = os.getenv("YOUTUBE_API_KEY")
    if not api_key:
        raise Exception("❌ YOUTUBE_API_KEY not set in environment variables.")

    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&type=video&q={query}&videoLicense=creativeCommon&key={api_key}"

    response = requests.get(url)
    data = response.json()

    for item in data.get("items", []):
        video_id = item["id"]["videoId"]
        return f"https://www.youtube.com/watch?v={video_id}"

    raise Exception("❌ لم يتم العثور على فيديوهات Creative Commons.")
