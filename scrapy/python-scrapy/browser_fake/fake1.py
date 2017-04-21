import urllib.request
import http.cookiejar

url = "http://news.163.com/17/0421/10/CIHRF8ON0001875N.html"
cjar = http.cookiejar.CookieJar()
proxy = urllib.request.ProxyHandler({'http': "127.0.0.1:8888"})
opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler, urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read()
fhandle = open("../myweb/part8/1.html", "wb")
fhandle.write(data)
fhandle.close()