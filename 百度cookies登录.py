import requests,lxml,sys
from lxml import etree
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
headers={'user-agent':'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/\
535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11'}

url='https://www.baidu.com'

r=requests.get(url,headers=headers)
cookies={'BAIDUID':'AFEA99561C8F69945E0F4B36949C3DBD:FG=1','\
BDUSS':'''VPMTdOeDJUSmo3Njkzb0stZzY4WTRHWDh6Zn45b0NHTUJ-MXo3U3\
ZQLVNod2xhTVFBQUFBJCQAAAAAAAAAAAEAAACOE6sDcXF5ejIzNjE5OAAAAAAAAAAAAA\
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJL64VmS-uFZd0'''}
p=r.cookies
p['BAIDUID']='AFEA99561C8F69945E0F4B36949C3DBD:FG=1'
p['BDUSS']='FJleE9xNEhVYUxJa0hOZzJpMFlXWWg3aXNJdUNUdXdjekV2Z2ZKY0VsQUlvd2xhTVFBQUFBJCQAAAAAAAAAAAEAAACOE6sDcXF5ejIzNjE5OAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgW4lkIFuJZW'

r2=requests.get('https://zhidao.baidu.com',cookies=p,headers=headers)

#print('qqyz' in r2.content.decode('gb2312'))
try:
    with open(r'g://1.txt','w',encoding='utf-8') as f:
        f.write(r2.text)

finally:
    f.close()
