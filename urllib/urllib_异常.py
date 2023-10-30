import urllib.request
import urllib.error
# url = 'https://blog.csdn.net/HHX_01/article/details/1325549201' #针对浏览器无法连接到服务器而增加出来的错误提示
url = 'https://pbszcqdgb.com' #一般是主机地址和参数有问题
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46'
}
try:
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    print(content)
except urllib.error.HTTPError:
    print("HTTPerror")
except urllib.error.URLError:
    print("URLerror")