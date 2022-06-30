
def hURL(word):
    return "https://www.letras.com/{}/mais_acessadas.html".format(word.replace(" ", "-"))

def hURLYoutube(url):
    if "https://" and "youtube.com" in url:
        if "watch?v=" in url:
            return url
        else:
            return url
    else:
        if "watch?v=" or "playlist?list=" in url:
            return "https://youtube.com/"+url
        else:
            return None

def hcleanHTML(l, t=None):
    cleanData = []
    if t != None:
        for d in l:
            if d != ' ':
                print(d)
                data = d.find(t)
                cleanData.append(data.text)
        return cleanData
    else:
        for d in l:
            cleanData.append(d.text)
        return cleanData


