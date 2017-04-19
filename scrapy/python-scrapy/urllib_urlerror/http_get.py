import urllib.request

keyword = "clojure"
url = "http://www.baidu.com/s?wd="
url1 = url + keyword
req = urllib.request.Request(url1)
data = urllib.request.urlopen(req).read()
fhandle = open("../myweb/part4/4.html", "wb")
fhandle.write(data)
fhandle.close()

# 中文出现编码错误
# quote
keyword2 = "苍井空老师"
key_code = urllib.request.quote(keyword2)
url_all = url + key_code
req2 = urllib.request.Request(url_all)
data2 = urllib.request.urlopen(req2).read()
fh = open("../myweb/part4/5.html", "wb")
fh.write(data2)
fh.close()