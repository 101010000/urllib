import urllib.request

#定义一个url 访问的地址
#下载网页
# url_page = "http://www.baidu.com"
# urllib.request.urlretrieve(url_page, "baidu.html")
#下载图片
# url_img = "https://www.gpbctv.com/uploads/20211117/1637140326XLIzNv.jpg"
# urllib.request.urlretrieve(url_img, "baidu_img.jpg")
#下载视频
url_video = "https://vd3.bdstatic.com/mda-pjgn1c7gkrx2g1hb/sc/cae_h264/1697585710712084972/mda-pjgn1c7gkrx2g1hb.mp4?v_from_s=hkapp-haokan-hbe&auth_key=1697690660-0-0-d937f9d939612fa5204fbca83513dfc8&bcevod_channel=searchbox_feed&pd=1&cr=2&cd=0&pt=3&logid=2660498315&vid=2312569481942164014&klogid=2660498315&abtest=112751_4-112345_2-113704_1"
urllib.request.urlretrieve(url_video, "baidu_video.mp4")