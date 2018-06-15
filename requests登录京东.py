#据说密码使用了rsa加密，但不会破解

# -*- coding:utf-8 -*-
import re,execjs,os
import requests,time
import fake_useragent as fk
from lxml import etree

ua=fk.UserAgent()
se = requests.session()   
se.headers.update({'user-agent':ua.random})

u1=r'https://passport.jd.com/new/login.aspx'            #登录页面

r1=etree.HTML(se.get(u1).text)          #打开登录页面获取参数

uuid=r1.xpath('//input[@id="uuid"]')[0].attrib['value']
eid=r1.xpath('//input[@id="eid"]')[0].attrib['value']
fp=r1.xpath('//input[@id="sessionId"]')[0].attrib['value']
pubKey=r1.xpath('//input[@id="pubKey"]')[0].attrib['value']
sa_token=r1.xpath('//input[@id="sa_token"]')[0].attrib['value']

#判断有没有验证码，如果u00返回true就要验证码
u00=r'https://passport.jd.com/uc/showAuthCode'
z=se.get(u00)
cc=''
if 'rue' in z.text:
    #u0是验证码图片的地址，下载到本地后打开手动填写，要注意请求头要设置referer，否则会直接跳转京东首页
    u00=r'https://authcode.jd.com/verify/image?a=1&acid={}&uid={}&yys={}'
    u0=u00.format(uuid,uuid,str(int(time.time()*1000)))
    h=se.headers
    h['referer']=u1
    z=se.get(u0,headers=h)
    with open('1.jpg','wb') as f:
        f.write(z.content)
    os.system('1.jpg')
    cc=input('请输入验证码:')
    
pw='''OYu8r2AQTs9zo7Zm+7xs3JM96rdA7iYN+btGefhPS2Z3al5dUyQ5zHRtn/yoh5iNpQoqZRcKs84wxJo+
Iy6dgaTw0PhLB3HMw0bdUdgfTBl+NCj4KyG48j+HX+KjWU1wNFttQD+7bupaCouVsu5ek8ubb32Ze0+OOJwxZyj6Dyk='''
d={'eid':eid,   'fp':fp,'_t':'_t','authcode':cc,'uuid':uuid,
   'loginType':'c','loginname':'1339574****',
   'nloginpwd':pw,'pubKey':pubKey,'sa_token':sa_token}
print('post提交的数据是：',d)

u2=r'https://passport.jd.com/uc/loginService?uuid={}&&r=0.3738090767112452&version=2015'.format(uuid)
r2=se.post(u2,data=d).text
print('登录结果是：',r2)
