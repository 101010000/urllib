import urllib.request
import urllib.parse
# https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&
# start=0&limit=20 ----------------------------------------------第一页
# https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&
# start=20&limit=20----------------------------------------------第二页 
# https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&
# start=40&limit=20----------------------------------------------第三页
# start = (page-1)*20
def request_design(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46'
    }
    data = {
        'start': (page-1)*20,
        'limit':20,
    }
    data = urllib.parse.urlencode(data)
    url = base_url + data
    request =urllib.request.Request(url=url,headers=headers)
    return request
def response_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf—8")
    return content
def download_data(page,content):
    with open(f"./test/douban_{page}.json","w",encoding="utf-8") as fp: #with open()调用完会自动关闭文件
        fp.write(content)
        
if __name__ == '__main__':
    start_page = int(input("请输入起始页:"))
    end_page = int(input("请输入结束页:"))
    for page in range(start_page,end_page+1):
        #请求对象的定制
        request = request_design(page)
        #获取响应的内容
        content = response_content(request)
        #下载数据
        download_data(page,content)