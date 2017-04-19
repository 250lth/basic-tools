import urllib.request

httpd = urllib.request.HTTPHandler(debuglevel=1)
httpsd = urllib.request.HTTPHandler(debuglevel=1)
opener = urllib.request.build_opener(httpd, httpsd)
urllib.request.install_opener(opener)
data = urllib.request.urlopen("http://edu.51cto.com")