#Get请求方式
import urllib.request
import urllib.parse

url = "https://www.baidu.com/s?wd="
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46'
}
#将汉字转换为unicode编码格式
#需要导入urllib.parse
name = urllib.parse.quote("python爬虫")
url = url + name
#请求对象的定制
request = urllib.request.Request(url=url,headers=headers)
#模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
#获取响应内容
content = response.read().decode("utf-8")
#打印数据
print(content)