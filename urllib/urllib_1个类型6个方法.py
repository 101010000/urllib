import urllib.request
#定义一个url 访问的地址
url = "http://www.baidu.com"
#模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

#1个类型和6个方法
#response是HTTPResponse的类型
# print(type(response)) #<class 'http.client.HTTPResponse'>

#（1）read()方法 按照一个字节一个字节去读
# content = response.read()
# print(content)

#（2）readline()方法 只能读取一行
# content = response.readline()
# print(content)

#（3）readlines()方法 读取所有行
# content = response.readlines()
# print(content)

#（4）getcode()方法 返回状态码 200
# print(response.getcode())

#（5）geturl()方法 返回url地址
# print(response.geturl())

#（6）getheaders()方法 返回响应头
# print(response.getheaders())