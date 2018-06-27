import requests
import re,os
import time,asyncio,aiohttp
from redis import Redis
from lxml import etree
from multiprocessing.dummy import Pool

xxx=500
headers={ 'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36' }
path=os.getcwd()+r'\test'
try:
    os.mkdir(path)
except Exception:pass
def g():        #获取图片地址u
    r=Redis(host='192.168.1.102',password='asd123')
    ll=r.scard('mz')
    print('剩余图数量：',ll)
    if ll>xxx:
        return r.spop('mz').decode()
        
def getname(u):     #从图片地址提取图片名字n
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
            
async def main():
    async with aiohttp.ClientSession(headers=headers) as se:
        a1=1
        while a1:
            a1=await down(se)

t1=time.clock()
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.ensure_future(main()))
print(time.clock()-t1)




