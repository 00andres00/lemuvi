from .scraping.scraperletters import ScraperLetters
from ..helpers import (
        hURLYoutube,
        hurlArtist,
        hurLetter,
        hwrite,
        hread)


class Controls:

    def __init__(self):
        self.e = False
        self.Artists = {}
        self.Musics = {}
        self.letters = []

    def cShowmusic(self):
        name = input("> ")
        url = hurlArtist(name)
        self.scraper = ScraperLetters()
        self.scraper.getlistMusic(url)
        self.musics = self.scraper.Datas
        for k in self.musics:
            print(str(k) +".- "+self.musics[k][0])

    def cShowArtists(self):
        letter = input("> ")
        l = hurLetter(letter)
        if l != None:
            self.scraper = ScraperLetters()
            self.scraper.getlistArtists(url)
            self.Artists = self.scraper.Datas
            for k in self.Artists:
                print(str(k) +".- "+self.Artists[k])
        else:
            self.e = True

    def cShowMoreArtists(self, l):
        url = "https://www.letras.com/letra/{}/artists.html".format(l.upper())
        self.scraper.createBS(url)
        prop = ['ul','class','cnt-list']
        self.scraper.bs.getData(prop)
        cshowData()

    def cShowLetters(self, l):
        url = "https://www.letras.com/letra/{}/artists.html".format(l.upper())
        self.scraper.createBS(url)
        prop = ['ul','class','cnt-list']
        self.scraper.bs.getData(prop)
        cshowData()

    def cgetletters(self):
        print("Insterta el numero de la canción")
        num = input("> ")
        self.scraper.GetLetters(self.musics[int(num)][1])
        print(self.scraper.letters)
        input("-Enter-")

    def cshowData(self):
        cleanData = hcleanHTML(self.scraper.bs.Data)
        for a in cleanData:
            i = cleanData.index(a)+1
            self.Datas[i] = a

    def cdownloads(self, url, Music=True):
        url = hURLYoutube(url)
        if url != None:
            DownloadYoutube(url, Music)
        else:
            self.e = True


