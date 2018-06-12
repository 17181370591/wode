# -*- coding:utf-8 -*-
import re,execjs,os
import requests,time
import fake_useragent as fk
from lxml import etree

ua=fk.UserAgent()
se = requests.session()   
se.headers.update({'user-agent':ua.random})

#先打开登录页面，获取参数s1，这个参数用来获取二维码
u1=r'https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=
                        https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&
                                un=new&lang=zh_CN&_=1528792097402'
print('u1=',u1)
r1=se.get(u1,verify=True)
re1=re.compile('"(.*?)"')
s1=re.search(re1,r1.text).group(1)


#获取二维码，保存到本地并打开
u2=r'https://login.weixin.qq.com/qrcode/{}'.format(s1)
print('u2=',u2)
with open('1.jpg','wb') as f:
    f.write(se.get(u2,verify=True).content)
os.system('1.jpg')

#这里sleep4s等待扫码，扫码成功后访问u3，获取参数ticket和s3
time.sleep(4)
u3=r'https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid={}
                            &tip=0&r=216254570&_=1528792097404'.format(s1)
print('u3=',u3)
hh=se.headers.update({'Referer':'https://wx.qq.com/'})
r3=se.get(u3,headers=hh,verify=True)
print(r3.text)
s3=re.search(re1,r3.text).group(1)
re3_1=re.compile('ticket=(.*?)&')
ticket=re.search(re3_1,s3).group(1)


#这一步应该可以不要
r4=se.get(s3,verify=True)


#用第3部分的参数获取参数s5和s5_1
u5=r'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage?ticket={}&uuid={}&
                            lang=zh_CN&scan=1528793075&fun=new&version=v2'
u5=u5.format(ticket,s1)
r5=se.get(u5,verify=True)
print(r5.text)
re5=re.compile('<pass_ticket>(.*?)</pass_ticket>')
s5=re.search(re5,r5.text).group(1)
re5_1=re.compile('<skey>(.*?)</skey>')
s5_1=re.search(re5_1,r5.text).group(1)



'''
#下面这些代码返回数据有问题，原因不明，所以用另一个链接，见第七部分
u6=r'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=215308659&pass_ticket={}'.format(s5)
d6={'r':'215308659','pass_ticket':s5}
hh=se.headers.update({'Referer':'https://wx.qq.com/'})
r6=se.post(u6,data=d6,headers=hh)
print('3603' in r6.text)
'''


#返回登录成功界面
u7=r'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?pass_ticket=&
                                        =1528793089109&seq=0&skey={}'.format(s5,s5_1)
hh=se.headers.update({'Referer':'https://wx.qq.com/'})
r7=se.post(u7,headers=hh,verify=True)
print("微信团队" in r7.content.decode('utf-8'))
