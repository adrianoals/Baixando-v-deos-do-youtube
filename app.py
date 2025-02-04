# pip install yt-dlp

import yt_dlp

# URL do vídeo
url = "https://www.youtube.com/watch?v=_Kh_AGh3Gqs"

# Opções para baixar apenas o áudio
options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',  # Nome do arquivo
}

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([url])

