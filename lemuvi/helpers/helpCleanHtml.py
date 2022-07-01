def hcleanHTML(l, t=None):
    cleanData = []
    if t != None:
        for d in l:
            if d != ' ':
                data = d.find(t)
                cleanData.append(data.text)
        return cleanData
    else:
        for d in l:
            cleanData.append(d.text)
        return cleanData


