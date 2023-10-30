#定制更高级的请求头(动态cookie和代理无法使用请求对象的定制)
#需求 使用handler来访问百度 获取网页源码
import urllib.request

url = "https://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36"
}
request = urllib.request.Request(url=url,headers=headers)
#handler build_opener open
#获取handler对象
handler = urllib.request.HTTPHandler()
#获取opener对象
opener = urllib.request.build_opener(handler)
#调用open方法
response = opener.open(request)
content = response.read().decode("utf-8")
print(content)