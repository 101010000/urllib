# 适用场景：数据采集时绕过登录，然后进入到页面
#个人信息页面是utf-8 但是还是报编码错误 因为并没有进入到个人信息页面 而是跳转到了登录页面
#那么登录页面不是utf-8 故报错
import urllib.request
url = "https://my.sina.com.cn/"

headers = {
    #没有cookie会跳转到登录页面，有登录之后的cookie则可以携带着cookie进入到任何页面
    'Cookie':'SUB=_2A25INWXMDeRhGeFJ61EU9SzNyT2IHXVrQ9AErDV_PUNbm9ANLRDfkW9NfKLcfXqRYLj-qvAW_ZFBQ9WoRmBEQfDn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5ZJqPuRTGpc8eaGGVd1n5r5JpX5KzhUgL.FoMNehefSKzpeo22dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNS050SK-EeKzp; ALF=1700307612; U_TRS1=000000aa.4f20c6eb.6531159e.217ea557; U_TRS2=000000aa.4f2bc6eb.6531159e.31f4cd73; UOR=,my.sina.com.cn,; SINAGLOBAL=27.17.178.170_1697715636.199235; Apache=27.17.178.170_1697715636.199236; ULV=1697715638241:1:1:1:27.17.178.170_1697715636.199236',
    #防盗链，判断当前路径是不是上一个路径进入的  一般情况下是做图片的防盗链
    'referr':'https://login.sina.com.cn/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46'
}
#请求对象的定制
request = urllib.request.Request(url=url,headers=headers)
#模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
#获取响应的内容
content = response.read().decode("utf-8")

with open("./test/weibo.html","w",encoding="utf-8") as fp:
    fp.write(content)