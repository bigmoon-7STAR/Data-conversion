import yt_dlp
import sys
import os

def download(url):
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'writethumbnail': True,  # サムネイルを一時的にダウンロード
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
            },
            {
                'key': 'EmbedThumbnail', # サムネイルをファイルに埋め込む設定
            },
            {
                'key': 'FFmpegMetadata',  # タイトルなどのメタデータも追加
            }
        ],
        'outtmpl': 'output/%(title)s.%(ext)s',
    }
    
    if not os.path.exists('output'):
        os.makedirs('output')
        
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        video_url = sys.argv[1]
        download(video_url)
    else:
        print("URLを指定してください")
