from youtube_dl import YoutubeDL
from lemuvi.configs import formats

class DownloadYoutube:
    def __init__(self, url, Music=True):
        self.formats(Music)
        self._id = self.URL.strip()
        self.download()

    def formats(self, f):
        if f:
            self.format = formats['Music']
        else:
            self.format = formats['Video']

    def download(self):
        ydl_opts = {
                'format': self.format,
                'outtmpl': '%(title)s.%(ext)s'
                }
        meta = YoutubeDL(ydl_opts).extract_info(self._id)
