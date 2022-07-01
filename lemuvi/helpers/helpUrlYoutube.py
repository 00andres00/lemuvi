def hURLYoutube(url):
    if "https://" and "youtube.com" in url:
        if "watch?v=" in url:
            return url
        else:
            return url
    else:
        if "watch?v=" in url:
            if "playlist?list=" in url:
                print(url)
                return "https://youtube.com/"+url
        else:
            return None

