import urllib.request
import urllib.parse
import http.cookiejar

url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=edf82adf"
postdata = urllib.parse.urlencode({
    "username": "250lth",
    "password": "250lth"
}).encode('utf-8')
req = urllib.request.Request(url, postdata)
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0')
cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))

urllib.request.install_opener(opener)
file = opener.open(req)
data = file.read()
file = open("../myweb/part5/3.html", "wb")
file.write(data)
file.close()
url2 = "http://bbs.chinaunix.net"
data2 = urllib.request.urlopen(url2).read()
fhandle = open("../myweb/part5/4.html", "wb")
fhandle.write(data2)
fhandle.close()