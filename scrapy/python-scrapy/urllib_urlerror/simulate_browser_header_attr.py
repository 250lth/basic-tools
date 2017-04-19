import urllib.request

url = "http://blog.csdn.net/weiwei_pig/article/details/69891700"
# failed
#file = urllib.request.urlopen(url) => HTTP Error 403

# We should simulate browser

# first method
# set User-Agent
# get User-Agent from browser--f12--network
headers = ("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()
fhandle = open("../myweb/part4/3.html", "wb")
fhandle.write(data)
fhandle.close()

# second method
# use add_header() to add header
req = urllib.request.Request(url)
req.add_header("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0")
data2 = urllib.request.urlopen(req).read()
fhandle1 = open("../myweb/part4/3-1.html", "wb")
fhandle1.write(data)
fhandle1.close()
