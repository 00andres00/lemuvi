from bs4 import BeautifulSoup

class BS():
    def __init__(self, html):
        self.BS = BeautifulSoup(html, "html.parser")
        self.DicData = {}
        self.Data = []

    def getALLData(self, prop):
        i=1
        for d in self.BS.find_all(prop[0], {prop[1]:prop[2]}):
            listData = [d.text, d['href']]
            self.DicData[i] = listData
            i+=1

    def getData(self, prop):
        for d in self.BS.find(prop[0], {prop[1]:prop[2]}).children:
            self.Data.append(d)
