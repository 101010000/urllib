import urllib.request
#定义一个url 访问的地址
url = "http://www.baidu.com"
#模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)
#获取响应的页面源码
#read()方法 返回的是字节型的二进制数据
#我们要将二进制数据转化为字符串 解码
#decode("编码的格式")方法解码
content = response.read().decode("UTF-8")
#打印数据
print(content)