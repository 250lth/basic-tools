# 爬取《人民的名义》评论页
import urllib.request
import http.cookiejar
import re

# set video code
vid = "1840851863"
# set comment start id
comid = "6252857842002897155"
# create the real web address of comment request
url = "http://coral.qq.com/article/" + vid + "/comment?commentid=" + comid + "&reqnum=20"

# set head to fake browser
headers = { "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
            "Connection": "keep-alive",
            "referer": "qq.com"}

# set cookie
cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
headall = []
for key, value in headers.items():
    item = (key, value)
    headall.append(item)
opener.addheaders = headall
urllib.request.install_opener(opener)

# start crawling
data = urllib.request.urlopen(url).read().decode("utf-8")
# build re for id, username, comment
idpat = '"id":"(.*?)"'
userpat = '"nick":"(.*?)",'
conpat = '"content":"(.*?)",'
# find data
idlist = re.compile(idpat, re.S).findall(data)
userlist = re.compile(userpat, re.S).findall(data)
conlist = re.compile(conpat, re.S).findall(data)
# traverse the data
for i in range(0, 20):
    print("Username is: " + eval('u"' + userlist[i] + '"'))
    print("Comment is: " + eval('u"' + conlist[i] + '"'))
    print("\n")
