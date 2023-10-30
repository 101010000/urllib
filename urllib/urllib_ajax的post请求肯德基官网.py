# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# post
# cname: 武汉
# pid: 
# pageIndex: 1
# pageSize: 10
import urllib.parse
import urllib.request
def request_design(page):
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data = {
        'cname':'武汉',
        'pid': '',
        'pageIndex': page,
        'pageSize': 10
    }
    data =urllib.parse.urlencode(data).encode('utf-8')
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46'
    }
    request = urllib.request.Request(url=url,data=data,headers=headers)
    return request
def response_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content
def download_data(page,content):
    with open(f"./test/kendeji_{page}.json","w",encoding="utf-8") as fp:
        fp.write(content)
if __name__ == '__main__':
    start_page = int(input("请输入起始页码:"))
    end_page = int(input("请输入结束页码:"))
    for page in range(start_page, end_page + 1):
        request = request_design(page)
        content = response_content(request)
        download_data(page,content)