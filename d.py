

# -*- coding:utf-8 -*-
import re,os
import requests,time
import fake_useragent as fk
from lxml import etree

def dl(name,pw):
    #ua=fk.UserAgent(use_cache_server=False)
    ua='Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.1.6) Gecko/20070914 Firefox/2.0.0.7'
    se = requests.session()   
    se.headers.update({'user-agent':ua})

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
        pic=r'C:\Users\Administrator\Desktop\{}.jpg'.format(name)
        print(pic)
        with open(pic,'wb') as f:
            f.write(z.content)
        #os.system(pic)

        cc=input('请输入验证码{}:'.format(name))
        
    #time.sleep(3)
    d={'eid':eid,   'fp':fp,'_t':'_t','authcode':cc,'uuid':uuid,
       'loginType':'c','loginname':name,
       'nloginpwd':pw,'pubKey':pubKey,'sa_token':sa_token}
    print('post提交的数据是：',d)

    u2=r'https://passport.jd.com/uc/loginService?uuid={}&&r=0.3738090767112452&version=2015'.format(uuid)
    r2=se.post(u2,data=d).text
    print('{}登录结果是：'.format(name),r2)
    return se

