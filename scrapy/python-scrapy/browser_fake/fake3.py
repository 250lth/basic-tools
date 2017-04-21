# deleted proxy
# it can be used in action
import urllib.request
import http.cookiejar

url = "http://www.baidu.com"

# Set headers
headers = { "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
            "Connection": "keep-alive",
            "referer": "baidu.com"}
# Set cookie
cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPHandler, urllib.request.HTTPCookieProcessor(cjar))

headall = []

for key, value in headers.items():
    item = (key, value)
    headall.append(item)

opener.addheaders = headall

urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read()
fhandle = open("../myweb/part8/3.html", "wb")
fhandle.write(data)
fhandle.close()