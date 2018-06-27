#原帖地址：http://python.jobbole.com/86328/
#只实现了多台电脑连接redis，读取url然后下载图片到<b>各自电脑</b>，不知道算不算分布式
#redis远程访问，可参考https://blog.csdn.net/qq_36470507/article/details/78874372
#注释掉bind 127.0.0.1，设置protected-mode no，在服务里重启redis


import requests
import re,os
import time,asyncio,aiohttp
from redis import Redis
from lxml import etree

#=====================================================================
#用aiohttp协程获取图片的url，以集合形式保存到redis

headers={ 'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) 
         Chrome/52.0.2743.116 Safari/537.36' }
         
nu=99                                   #获取99个网页的图片的url

async def push_redis_list(a,b):
    r = Redis(password='asd123')
    print (r.keys('*'))
    async with aiohttp.ClientSession(headers=headers) as se:
        for i in range(a,b):
            num = 5100+i;                   #抓取的取件仅在5100--5200之间
            url ='http://www.meizitu.com/a/'+ str(num) +'.html'
            async with se.get(url,timeout=30) as x:
                et=etree.HTML(await x.text('gb18030'))
                img_url_list=et.xpath('//div[@id="picture"]/p/img/@src')
                r.sadd('mz',*img_url_list)
                print(r.scard('mz'))
    return r

t1=time.clock()
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.ensure_future(push_redis_list(0,nu)))
print(time.clock()-t1)

#=====================================================================
#从redis的mz里pop图片地址url，分配下载
         
         
xxx=700                 #不全部下载，redis的url剩下700个时停止
headers={ 'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) 
         Chrome/52.0.2743.116 Safari/537.36' }
         
path=os.getcwd()+r'\test'
         
try:
    os.mkdir(path)
except Exception:
    pass
         
         
def g():        #从redis通过spop获取图片地址u
    r=Redis(host='192.168.1.102',password='asd123')
    ll=r.scard('mz')
    print('剩余图数量：',ll)
    if ll>xxx:
        return r.spop('mz').decode()
         
        
def getname(u):     #从图片地址u提取图片名字n，并去掉特殊字符
    x=r'http://mm.chinasareview.com/wp-content/uploads/'
    name=u.replace(x,'')
    n=re.sub(r'[\\/:*?"<>|\r\n]+','',name)
    #print(u,type(u))
    return n
         

async def down(se):     #用图片u地址下载图片
    u=g()    
    if not u:return
    n=getname(u)
    #print('u=',u,'n=',n)
    async with se.get(u) as r:              
        with open(os.path.join(path,n),'wb') as f:
            f.write(await r.content.read())
            return 1
      
         
#a1是down的返回值，下载成功返回1，否则返回None；当到达700时上面的函数都会返回None

async def main():
    async with aiohttp.ClientSession(headers=headers) as se:
        a1=1
        while a1:
            a1=await down(se)
         

t1=time.clock()
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.ensure_future(main()))
print(time.clock()-t1)




