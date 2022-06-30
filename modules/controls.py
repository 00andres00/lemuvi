from .scraping.scraperletters import ScraperLetters


class ControlScraper():
    def __init__(self):
        self.Artists = {}
        self.Musics = {}
        self.letters = []

    def cShowmusic(self):
        name = input("> ")
        url = hURL(name)
        self.scraper = ScraperLetters()
        self.scraper.getlistMusic(url)
        self.musics = self.scraper.Datas
        for k in self.musics:
            print(str(k) +".- "+self.musics[k][0])

    def cShowArtists(self):
        letter = input("> ")
        self.scraper = ScraperLetters()
        self.scraper.getlistArtists(letter)
        for k in self.Artists:
            print(str(k) +".- "+self.Artists[k][0])

    def cgetletters(self):
        print("Insterta el numero de la canción")
        num = input("> ")
        self.scraper.GetLetters(self.musics[int(num)][1])
        print(self.scraper.letters)
        input("-Enter-")
