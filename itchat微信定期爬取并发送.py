#https://www.cnblogs.com/ouyangping/p/8453920.html
#已经会使用登录登出，发文字文件图片信息，群发，获取朋友列表，公众号列表

import itchat as wx, time,requests,fake_useragent as fu
from itchat.content import *
from lxml import etree

#不登出的话，重复auto_login会被无视
wx.auto_login(True)
#wx.login()

ua=fu.UserAgent()
f=wx.search_friends(name='17077440160')[0]
while True:
    try:
        h={'user-agent':ua.random}
        r=requests.get('https://www.smzdm.com/',headers=h)
        r=etree.HTML(r.text).xpath('//h5')
        s=r[0].xpath('string(.)')               
    except Exception as e:
        s=e
    print(time.strftime('%Y-%m-%d,%H:%M:%S'))
    print(s,'\n','='*11)
    f.send_msg(s)  
    time.sleep(600)
