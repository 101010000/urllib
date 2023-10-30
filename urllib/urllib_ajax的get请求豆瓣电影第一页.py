#get请求
import urllib.request
import urllib.parse

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20"

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46'
}
#请求对象的定制
request = urllib.request.Request(url=url,headers=headers)
#模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
#获取响应的内容
content = response.read().decode("utf-8")
#打印数据
# print(content)
#下载数据
# fp = open("./test/douban.json","w",encoding="utf-8")
# fp.write(content)
with open("./test/douban.json","w",encoding="utf-8") as fp:
    fp.write(content)
    fp.close()