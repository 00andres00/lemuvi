from requests import get, post

class GetPage():
    def __init__(self, url, method='Get'):
        self.URL = url
        self.getPage(method)

    def getPage(self, method):
        if method != 'Get':
            self.g = post(self.URL)
        else:
            self.g = get(self.URL)


