#Post请求方式
import urllib.request
import urllib.parse
url = "https://fanyi.baidu.com/sug"

headers = {
    'Cookie':'ewlogin=1; BIDUPSID=96A829FEC1E945E26B80F419125966FA; PSTM=1697088103; BAIDUID=0B95F954D8142D2E44FABDFD98F3EB93:FG=1; MCITY=-218%3A; BDUSS=l-RUJSYUFHejJuSGRpc0NIaGVzV29Rd3EzeXA1MTZ4ak9CLVEza3d0NURlVTlsSVFBQUFBJCQAAAAAAQAAAAEAAAB~00YrAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEPsJ2VD7CdlME; BDUSS_BFESS=l-RUJSYUFHejJuSGRpc0NIaGVzV29Rd3EzeXA1MTZ4ak9CLVEza3d0NURlVTlsSVFBQUFBJCQAAAAAAQAAAAEAAAB~00YrAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEPsJ2VD7CdlME; BA_HECTOR=0k802ha4052l8k2h2ka581091iivpgp1o; ZFY=MJFIwNiB7tul6dBrZX8K5ZPOmO:AhPAov:AT9v201zTtw:C; BAIDUID_BFESS=0B95F954D8142D2E44FABDFD98F3EB93:FG=1; BDRCVFR[Zh1eoDf3ZW3]=mk3SLVN4HKm; delPer=0; PSINO=6; H_PS_PSSID=26350; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BCLID=8251711274092435139; BCLID_BFESS=8251711274092435139; BDSFRCVID=I-FOJexroG3O1Hvq-WXcomeQp_weG7bTDYrEQrJFTAA-JQ_VFdWiEG0Pts1-dEu-S2OOogKKLgOTHULF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=I-FOJexroG3O1Hvq-WXcomeQp_weG7bTDYrEQrJFTAA-JQ_VFdWiEG0Pts1-dEu-S2OOogKKLgOTHULF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRAOoC_-tDvtHJrwMDTD-tFO5eT22-usW4jl2hcHMPoosIOODf7-KDuiWMby24QI-NOf0l05KfbUotoH0J5kQl0FLecZQlRp3DnUBl5TtUJMqIDzbMohqqJXXPnyKMniBIv9-pnGBpQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKu-n5jHjjBjGKe3H; H_BDCLCKID_SF_BFESS=tRAOoC_-tDvtHJrwMDTD-tFO5eT22-usW4jl2hcHMPoosIOODf7-KDuiWMby24QI-NOf0l05KfbUotoH0J5kQl0FLecZQlRp3DnUBl5TtUJMqIDzbMohqqJXXPnyKMniBIv9-pnGBpQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKu-n5jHjjBjGKe3H; RT="z=1&dm=baidu.com&si=358f8c45-fe18-43c6-a2a1-7ff826af0137&ss=lnwnhexs&sl=3&tt=2o2&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=jfx"; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1697688042; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1697688042; APPGUIDE_10_6_6=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; ab_sr=1.0.1_MjZlZjQ5YTljMDhlNDI0MWQ2MDk2OGRlZjM1MGY1ZjAyNTJlNGE0ZmU1M2M0MGUwN2NhNDcyYjg1NGU2OTllODJhYjgzMTQ0MGEwMGU5OWVlY2I3NDc5MDBjOTc2N2MzNWVlY2M2YTUyMzBjMGNhYWRmZmY1ZmMwNTg2NDU1NzliMDhlMDY4MDkwYWFjZjRlYmQyYjMxMTUzMGJjNDg4Yzg5ZmM3MTYwMWQyOTAzYTBlNmRmNTc0MmMyMjUxMjc2',
    # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46'
}
data = {
    'kw':'spider'
}
#Post请求参数，必须进行编码
data = urllib.parse.urlencode(data).encode("utf-8")
#Post请求参数，是不会拼接到url后面 而是需要放在请求对象定制的参数中
#Post请求参数，必须要进行编码
request = urllib.request.Request(url=url,data=data,headers=headers)
#模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
#获取响应内容
content = response.read().decode("utf-8")
print(content)
#Post请求方式的参数 必须编码 data = urllib.parse.urlencode(data)
#编码之后 必须调用encode()方法  data = data.encode("utf-8")
#参数是放在请求对象定制的方法中 request = urllib.request.Request(url=url,data=data,headers=headers)
print(type(content))
#str->Json loads()方法
import json
content = json.loads(content)
print(content)
