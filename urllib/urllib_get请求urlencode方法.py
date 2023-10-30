#Get请求方式
#应用场景：多个参数时，可以用urllib.parse.urlencode()方法，将参数组合成一个字符串
import urllib.request
import urllib.parse

url = "https://www.baidu.com/s?"

data = {
    'wd':'python爬虫',
    'rsv_spt':'1',
    'rsv_iqid':'0x0128a7054000270b',
}
#将字典转换为url编码格式
name = urllib.parse.urlencode(data)
url = url + name
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46'
}
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")
print(content)