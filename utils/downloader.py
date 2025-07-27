from pytube import YouTube

def download_youtube_video(url):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    output_path = f"assets/{yt.video_id}.mp4"
    stream.download(filename=output_path)
    return output_path
