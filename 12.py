import asyncio,time,aiohttp,requests
from lxml import etree
            
async def f(se,i):     #虎扑湿乎乎帖子列表获取帖子地址
    async with se.get(url.format(i)) as r:
        s=await r.text()
        s=etree.HTML(s)
        res=s.xpath('//a[@class="truetit"]/@href')
        for i in res:           
            l.add(i)
            
async def m():
    async with aiohttp.ClientSession() as se:
        ts=[asyncio.ensure_future(f(se,i)) for i in range(j)]
        await asyncio.wait(ts)
        
async def fetch(session, url):
    async with session.get(url) as response:
        s= await response.text()
        s=etree.HTML(s)
        res=s.xpath('//div[@class="j_u"]/@uname')
        for i in res:
            if i in b:
                b[i]+=1
            else:b[i]=1
        return

async def main():
    async with aiohttp.ClientSession() as session:
        ts=[asyncio.ensure_future(fetch(session,url1.format(i))) for i in l]
        print(len(ts))
        await asyncio.wait(ts)



l=set()
b={}
url='https://bbs.hupu.com/vote-{}'
url1='https://bbs.hupu.com{}'

t=time.clock()
j=8
loop=asyncio.get_event_loop()
loop.run_until_complete(m())
print(time.clock()-t)
print('len(l)=',len(l))

t=time.clock()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print(time.clock()-t)
print(sum(b.values()))
