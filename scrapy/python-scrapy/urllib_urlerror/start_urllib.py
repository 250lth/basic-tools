import urllib.request

file = urllib.request.urlopen("http://www.baidu.com")
data = file.read()
dataline = file.readline()

print(dataline)
print(data)

# storage the data as a html

# 1.open and write
fhandle = open("../myweb/part4/1.html", "wb")
fhandle.write(data)
fhandle.close()

# 2.use urlretrieve()
filename = urllib.request.urlretrieve("http://edu.51cto.com", filename = "../myweb/part4/2.html")

# clean up the cache
urllib.request.urlcleanup()

# other useful tools
print(file.info())
print(file.getcode()) #=> 200
print(file.geturl())

# code it, using quote()
code_sina = urllib.request.quote("http://www.sina.com.cn")
print(code_sina)
# decode
print(urllib.request.unquote(code_sina))