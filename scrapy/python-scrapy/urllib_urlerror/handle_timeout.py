import urllib.request

for i in range(1, 100):
    try:
        file = urllib.request.urlopen("http://yum.iqianyue.com", timeout=1)
        data = file.read()
        print(len(data))
    except Exception as e:
        print("出现了异常 --> " + str(e))

# Sometimes it occurs exception
# We can set the timeout bigger