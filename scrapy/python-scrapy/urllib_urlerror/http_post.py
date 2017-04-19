import urllib.request
import urllib.parse

url = "http://www.iqianyue.com/mypost/"
postdata = urllib.parse.urlencode({
    "name":"ceo@iqianyue.com",
    "pass":"aA123456"
}).encode('utf-8')
req = urllib.request.Request(url, postdata)
req.add_header("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0")
data = urllib.request.urlopen(req).read()
fhandle = open("../myweb/part4/6.html", "wb")
fhandle.write(data)
fhandle.close()