from import youtube-dl

def DownloadMusic(url):
    youtube-dl -f bestaudio -x --no-warnings --audio-quality 0 --audio-format aac -o './Music/%(title)s.%(ext)s' url

