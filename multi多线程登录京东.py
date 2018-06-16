#使用前切记修改账号名


=========================================================================================================
#这一部分是d.py的代码，作用是登陆京东，并返回session

# -*- coding:utf-8 -*-
import re,os
import requests,time
import fake_useragent as fk
from lxml import etree



#不知道为什么新电脑无法使用fk，所以ua这里手动填写了
def dl(name,pw):            #登录，返回session，参数是账号密码
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

=========================================================================================================
#这一部分是12.py的代码，使用多线程登录京东

#方法1使用了multiprocessing.dummy的Pool，据说这是个线程池
#方法2是常规的线程
#使用常规进程multiprocessing.Process和进程池multiprocessing.Pool都不会等待输入验证码而报错，原因不明

import d,multiprocessing as mu,threading as th
from multiprocessing.dummy import Pool as ThreadPool
#python C:\Users\Administrator\Desktop\12.py

name1='1339574****'
pw1='OYu8r2AQTs9zo7Zm+7xs3JM96rdA7iYN+btGefhPS2Z3al5dUyQ5zHRtn/yoh5iNpQoqZRcKs84wxJo+Iy6dgaTw0PhLB3HMw0bdUdgfTBl+NCj4KyG48j+HX+KjWU1wNFttQD+7bupaCouVsu5ek8ubb32Ze0+OOJwxZyj6Dyk='
name2='1718137****'
pw2='Ts9dwzYIDhqlyy2GGPl4lVzrkSDQqMfplLURPFpLDZwwe5/iadXJ1zpKn9dbfjTEmCpmTtz6VJjJbxX8Mv6NwxkpxAizji8kYJitdElklTXY/x3EWgYCyAbYUAKpm0aA9I7pHRmxnlSPQZnloVdiyfWSqoXDhuDCydH+SDl+qXM='
lpool=((name1,pw1),(name2,pw2))

#方法1。这种方法更好，results是两个登录函数返回的session数据的列表，可以当列表使用来进行各种操作，详情见京东下单购物车

if __name__=='__main__':
        P=ThreadPool(2)
        #P=mu.Pool(2)
        results=P.starmap(d.dl,lpool)
        P.close()
        P.join()

'''
#方法2
if __name__=='__main__':
        ps=[]
        for i in range(2):
                print(lpool[i])
                t=th.Thread(target=d.dl,args=(*lpool[i],))
                ps.append(t)
        print(ps)        
        for t in ps:
                t.start()
                t.join()

'''
