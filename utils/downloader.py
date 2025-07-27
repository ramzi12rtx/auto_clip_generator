from pytube import YouTube
import os

def download_youtube_video():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # فيديو تجريبي (غيّره لاحقًا)
    yt = YouTube(url)
    stream = yt.streams.filter(file_extension='mp4', progressive=True).get_highest_resolution()
    path = stream.download(output_path="assets", filename="video.mp4")
    return path
