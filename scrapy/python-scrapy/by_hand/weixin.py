import re
import urllib.request
import time
import urllib.error


# simulate browser
headers = ("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]

# install opener
urllib.request.install_opener(opener)

# a list to store urls
listurl = []

# use proxy
def use_proxy(proxy_addr, url):
    try:
        import urllib.request
        proxy = urllib.request.ProxyHandler({'http':proxy_addr})
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().decode('utf-8')
        return data
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
        time.sleep(10)
    except Exception as e:
        print("exception:" + str(e))
        time.sleep(1)

# get all the links of articles
def getlisturl(key, pagestart, pageend, proxy):
    try:
        page = pagestart
        keycode = urllib.request.quote(key)
        pagecode = urllib.request.quote("&page")

        for page in range(pagestart, pageend + 1):
            url = "http://weixin.sogou.com/weixin?type=2&query=" + keycode + pagecode + str(page)
            data1 = use_proxy(proxy, url)
            listurlpat = '<div class="txt-box">.*?(http://.*?)"'
            listurl.append(re.compile(listurlpat, re.S).findall(data1))
        print("共获取到文章" + str(len(listurl)) + "页")
        return listurl
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
        time.sleep(10)
    except Exception as e:
        print("exception:" + str(e))
        time.sleep(1)

# get content from article urls
def getcontent(listurl, proxy):
    i = 0
    html1 = '''
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://
    www.w3.org/TR/xhtml/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>微信文章页面</title>
    </head>
    <body>
    '''
    fh = open("../myweb/part6/1.html", "wb")
    fh.write(html1.encode("utf-8"))
    fh.close()
    fh.open("../myweb/part6/1.html", "ab")

    for i in range(0, len(listurl)):
        for j in range(0, len(listurl[i])):
            try:
                url = listurl[i][j]
                url = url.replace("amp;", "")
                data = use_proxy(proxy, url)
                titlepat = "<title>(.*?)</title>"
                contentpat = 'id="js_content">(.*?)id="js_sg_bar"'
                title = re.compile(titlepat).findall(data)
                content = re.compile(titlepat).findall(data)
                thistitle = "此次没有获取到。。。"
                thiscontent = "此次没有获取到。。。"
                if(title != []):
                    thistitle = title[0]
                if(content != []):
                    thiscontent = content[0]

                dataall = "<p>标题为:" + thistitle + "</p><p>内容为：" + thiscontent + "</p><br>"
                fh.write(dataall.encode("utf-8"))
                print("第" + str(i) + "个网页第" + str(j) + "次处理")
            except urllib.error.URLError as e:
                if hasattr(e, "code"):
                    print(e.code)
                if hasattr(e, "reason"):
                    print(e.reason)
                time.sleep(10)
            except Exception as e:
                print("Exception: " + str(e))
                time.sleep(1)
    fh.close()

    html2 = '''
    </body>
    </html>
    '''
    fh = open("../myweb/part6/1.html", "ab")
    fh.write(html2.encode("utf-8"))
    fh.close()

if __name__ == "__main__":
    key = "物联网"
    proxy = "183.153.52.108:80"
    proxy2 = ""
    pagestart = 1
    pageend = 2
    listurl = getlisturl(key, pagestart, pageend, proxy)
    getcontent(listurl, proxy)