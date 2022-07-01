from .parse import BS
from .getpage import GetPage
from lemuvi.helpers.helpCleanHtml import hcleanHTML

class ScraperLetters():
    def __init__(self):
        ### ### ### Datas ### ### ###
        self.Datas = {}
        self.Data = []

    def createBS(self, url):
        request = GetPage(url)
        html = request.g.text
        self.bs = BS(html)

    def getlistArtists(self, url):
        prop = ['ul','class','cnt-list-thumb-l']
        self.createBS(url)
        self.bs.getData(prop)
        cleanData = hcleanHTML(self.bs.Data, t="b")
        for a in cleanData:
            i = cleanData.index(a)+1
            self.Datas[i] = a

    def getlistMusic(self, url):
        prop = ['a','class','song-name']
        self.createBS(url)
        self.bs.getALLData(prop)
        self.Datas = self.bs.DicData

    def GetLetters(self, url):
        if not "https" in url:
            url = "https://www.letras.com"+url
        self.createBS(url)
        prop = ['div', 'class','p402_premium']
        self.bs.getData(prop)
        cleanData = hcleanHTML(self.bs.Data)
        self.letters = cleanData

