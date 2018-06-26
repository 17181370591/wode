from gevent.pool import Pool 
from gevent import monkey 
# monkey.patch_all() 
monkey.patch_socket() 
monkey.patch_ssl()
import threading,time,requests,multiprocessing,gevent,aiohttp,asyncio
from lxml import etree
#多线程的join分开写后速度快很多，
#打开10个网站，单线程时间8.8s  ,   多线程0.8s ,   gevent4.5s  , aiohttp2s


url='https://bbs.hupu.com/topic-{}'
def p(page):
    r1=requests.get(url.format(page+1))
    r=etree.HTML(r1.text)    
    a=r.xpath('//a[@class="truetit"]')
    for i in range(5):
        print(a[i].xpath('string(.)')[:11])
    print('='*11)

async def pp(page):
    async with aiohttp.ClientSession() as se:        
        await fetch(se,page)

async def fetch(se,page):
    async with se.get(url.format(page+1)) as r1:
        r=etree.HTML(await r1.text())    
        a=r.xpath('//a[@class="truetit"]')
        for i in range(5):
            print(a[i].xpath('string(.)')[:11])
        print('='*11)
        
if __name__=='__main__':
    b=10
    t=time.clock()
    for i in range(b):
        p(i)
    print('什么都不用',time.clock()-t)
    #8.8

    t=time.clock()
    ts=[] 
    for i in range(b):
        th=threading.Thread(target=p,args=(i,))
        ts.append(th)
        th.start()
    for th in ts:
        th.join()   
    print('多线程',time.clock()-t)
    #0.8

    
    t=time.clock()
    ts=[] 
    for i in range(b):
        th=gevent.spawn(p(i))
        ts.append(th)
    gevent.joinall(ts)   
    print('gevent',time.clock()-t)
    #4.5

        
    t=time.clock()
    ts=[]
    loop=asyncio.get_event_loop()
    for i in range(b):
        th=asyncio.ensure_future(pp(i))
        ts.append(th)
    loop.run_until_complete(asyncio.wait(ts))
    loop.close()
    print('协程',time.clock()-t)
    #2.0
