from googleapiclient.discovery import build

def fetch_trending_videos(api_key, region_code='US', max_results=5):
    youtube = build('youtube', 'v3', developerKey=api_key)
    resp = youtube.videos().list(
        part='snippet,statistics',
        chart='mostPopular',
        regionCode=region_code,
        maxResults=max_results
    ).execute()
    vids = []
    for item in resp.get('items', []):
        vids.append({
            'video_id': item['id'],
            'title': item['snippet']['title'],
            'channel': item['snippet']['channelTitle'],
            'url': f'https://www.youtube.com/watch?v={item["id"]}'
        })
    return vids
