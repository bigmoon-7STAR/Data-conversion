import yt_dlp
import sys
import os

def download(url):
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }],
        'outtmpl': 'output/%(title)s.%(ext)s', # outputフォルダに保存
    }
    if not os.path.exists('output'):
        os.makedirs('output')
        
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = sys.argv[1]
    download(video_url)
