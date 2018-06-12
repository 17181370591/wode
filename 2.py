# -*- coding:utf-8 -*-
import re,execjs,os
import requests,time
import fake_useragent as fk
from lxml import etree

ua=fk.UserAgent()
se = requests.session()   
se.headers.update({'user-agent':ua.random})
#se.proxies={'http': 'http://221.224.49.237:3128', 'https': 'https://221.224.49.237:3128'}
u1=r'https://passport.jd.com/new/login.aspx'


r1=etree.HTML(se.get(u1).text)
uuid=r1.xpath('//input[@id="uuid"]')[0].attrib['value']
eid=r1.xpath('//input[@id="eid"]')[0].attrib['value']
fp=r1.xpath('//input[@id="sessionId"]')[0].attrib['value']
pubKey=r1.xpath('//input[@id="pubKey"]')[0].attrib['value']
sa_token=r1.xpath('//input[@id="sa_token"]')[0].attrib['value']
u00=r'https://passport.jd.com/uc/showAuthCode'
z=se.get(u00)
cc=''
if 'rue' in z.text:
    u00=r'https://authcode.jd.com/verify/image?a=1&acid={}&uid={}&yys={}'
    u0=u00.format(uuid,uuid,str(int(time.time()*1000)))
    h=se.headers
    h['referer']=u1
    z=se.get(u0,headers=h)
    with open('1.jpg','wb') as f:
        f.write(z.content)
    os.system('1.jpg')
    cc=input('请输入验证码:')
pw='OYu8r2AQTs9zo7Zm+7xs3JM96rdA7iYN+btGefhPS2Z3al5dUyQ5zHRtn/yoh5iNpQoqZRcKs84wxJo+Iy6dgaTw0PhLB3HMw0bdUdgfTBl+NCj4KyG48j+HX+KjWU1wNFttQD+7bupaCouVsu5ek8ubb32Ze0+OOJwxZyj6Dyk='

d={'eid':eid,   'fp':fp,'_t':'_t','authcode':cc,
    'uuid':uuid,'loginType':'c','loginname':'13395747825',
   'nloginpwd':pw,'pubKey':pubKey,'sa_token':sa_token}
print(d)
u2=r'https://passport.jd.com/uc/loginService?uuid=\
{}&&r=0.3738090767112452&version=2015'.format(uuid)
r2=se.post(u2,data=d).text
print('r2=',r2)
