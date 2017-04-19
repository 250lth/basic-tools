import urllib.request
import urllib.error

try:
    urllib.request.urlopen("http://blog.csdn.net")
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)

try:
    urllib.request.urlopen("http://blog.baidusss.com")
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)
except urllib.error.URLError as e:
    print(e.reason)