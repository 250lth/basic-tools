import re
import urllib.request

def getlink(url):
    # fake as browser
    headers = ("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    # install opener
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = str(file.read())
    # link re
    pat = '(https?://[^\s";]+\.(\w|/)*)'
    link = re.compile(pat).findall(data)
    # remove dumps
    link = list(set(link))
    return link

url = "http://blog.csdn.net/"
linklist = getlink(url)
for link in linklist:
    print(link[0])