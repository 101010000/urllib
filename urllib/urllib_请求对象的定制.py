import urllib.request

url = "http://www.baidu.com"
#url组成
#http/https   www.baidu.com    80/443
#协议              域名          端口     路径    参数    锚点
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46'
}
#因为urlopen()方法中不能存储字典，所以headers不能传递进去
#请求对象的定制--反爬
request = urllib.request.Request(url=url,headers=headers) #位置参数
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")
print(content)