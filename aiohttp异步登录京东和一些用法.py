'''
#简要教程：https://blog.csdn.net/getcomputerstyle/article/details/71515331
#详细文档：http://aiohttp.readthedocs.io/en/stable/client.html


session.post('http://httpbin.org/post', data=b'data')
session.post(url, json={'test': 'object'})
post的形参是data，json
x=await r.text(encoding='utf8')     #encoding默认不用加,requests的r.text
files = {'file': open('report.xls', 'rb')}
await session.post(url, data=files)   #post文件
print(await r.read())        #相当于requests的r.content
print(await r.json())        #相当于requests的r.json()
size=1024
with open('1.jpg','wb') as f:   #保存二进制数据到图片
    f.write(await r.content.read())
    while 1:
        chunk=await r.content.read(size)
        if not chunk:
            break
        f.write(chunk)

params = {'key1': 'value1', 'key2': 'value2'}       #get传参数方法1
async with session.get('http://httpbin.org/get',
      params=params) as resp:
      assert resp.url == 'http://httpbin.org/get?key2=value2&key1=value1'
      
      
params = [('key', 'value1'), ('key', 'value2')]         #get传参数方法2，可以传key相同的参数
async with session.get('http://httpbin.org/get',
    params=params) as r:
    assert r.url == 'http://httpbin.org/get?key=value2&key=value1'
'''



#这里用一个session等两个号，估计第一个号会被登出。
#从get登录界面获取参数，访问验证码图片并保存，post登录全部用了异步，感觉比同步的方式快不少，
#但不能等账号登录，估计需要多进程+异步实现

import aiohttp,asyncio,fake_useragent as fu,time,requests
from lxml import etree

name2='171813703**'
pw2='''Ts9dwzYIDhqlyy2GGPl4lVzrkSDQqMfplLURPFpLDZwwe5/iadXJ1zpKn9dbfjTEmCpmTtz6VJjJbxX8Mv
    6NwxkpxAizji8kYJitdElklTXY/x3EWgYCyAbYUAKpm0aA9I7pHRmxnlSPQZnloVdiyfWSqoXDhuDCydH+SDl+qXM='''

u1=r'https://passport.jd.com/new/login.aspx' 
pw='''OYu8r2AQTs9zo7Zm+7xs3JM96rdA7iYN+btGefhPS2Z3al5dUyQ5zHRtn/yoh5iNpQoqZRcKs84wxJo+
Iy6dgaTw0PhLB3HMw0bdUdgfTBl+NCj4KyG48j+HX+KjWU1wNFttQD+7bupaCouVsu5ek8ubb32Ze0+OOJwxZyj6Dyk='''
ua=fu.UserAgent().random
hh={'user-agent':ua,'referer':u1}

#get方式打开登录界面，获取参数，并异步下载验证码

async def f(se,u,user,pw):
    d={'file':open('1.jpg','rb')}
    async with se.get(u,data=d,timeout=6) as f:
        t=await f.text()
        r1=etree.HTML(t)
        uuid=r1.xpath('//input[@id="uuid"]')[0].attrib['value']
        eid=r1.xpath('//input[@id="eid"]')[0].attrib['value']
        fp=r1.xpath('//input[@id="sessionId"]')[0].attrib['value']
        pubKey=r1.xpath('//input[@id="pubKey"]')[0].attrib['value']
        sa_token=r1.xpath('//input[@id="sa_token"]')[0].attrib['value']
        await yzm(se,uuid,us=user)
        cc=input('{}yzm='.format(user))
        d={'eid':eid,   'fp':fp,'_t':'_t','authcode':cc,'uuid':uuid,
                'loginType':'c','loginname':user,
                'nloginpwd':pw,'pubKey':pubKey,'sa_token':sa_token}
        print(f.headers)       
        return d,f.headers

    
    
#post方法登录

async def p(se,d,fh):
    u2=r'https://passport.jd.com/uc/loginService?uuid={}&&r=0.3738090767112452&version=2015'
                    .format(d['uuid'])
    async with se.post(u2,data=d) as r2:
        x=await r2.text()
        print(x)
        return x

    
    
#异步下载验证码

async def yzm(se,uuid,us):
    u00=r'https://authcode.jd.com/verify/image?a=1&acid={}&uid={}&yys={}'
    u0=u00.format(uuid,uuid,str(int(time.time()*1000)))
    print(u0)
    async with se.get(u0,headers=hh) as rrr:
        with open('{}.jpg'.format(us),'wb') as jp:
            jp.write(await rrr.content.read())

            
            
#把获取参数和登录放一起

async def login(se,us,pw):
    d,fh=await f(se,u1,user=us,pw=pw)
    return await p(se,d,fh)



async def main():
    async with aiohttp.ClientSession(headers=hh) as se:
        await login(se,us=name2,pw=pw2)
        await login(se,us='1339574****',pw=pw)
        return se
        
        
  

loop=asyncio.get_event_loop()
r=loop.run_until_complete(asyncio.ensure_future(main()))
