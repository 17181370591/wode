import asyncio,time,aiohttp
from lxml import etree

async def f(i):     #虎扑湿乎乎帖子列表获取帖子地址
    async with aiohttp.ClientSession() as se:
        async with se.get(url.format(i)) as r:
            s=await r.text()
            s=etree.HTML(s)
            res=s.xpath('//a[@class="truetit"]/@href')
            for i in res:
                l.add(i)
                
async def g(i):     #帖子里获取lz的id
    async with aiohttp.ClientSession() as se:
        async with se.get(url1.format(i)) as r:
            s=await r.text()
            s=etree.HTML(s)
            res=s.xpath('//div[@class="j_u"]/@uname')
            for i in res:
                if i in b:
                    b[i]+=1
                else:b[i]=1

async def g1(i):    #返回帖子的text
    async with aiohttp.ClientSession() as se:
        async with se.get(url1.format(i)) as r:
            s=await r.text()
            s=etree.HTML(s)
            res=s.xpath('//div[@class="j_u"]/@uname')
            return res

def callb(v):       #记录id和次数，作为g1的回调函数
    for i in v.result():
        if i in b:
            b[i]+=1
        else:b[i]=1
        
l=set()
b={}
url='https://bbs.hupu.com/vote-{}'
url1='https://bbs.hupu.com{}'
ts=[]
t=time.clock()
j=2
for i in range(1,j):    #运行f(),获取帖子地址
    task=asyncio.ensure_future(f(i))
    ts.append(task)
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(ts))
print(time.clock()-t)

t=time.clock()      
ts=[]
for i in l:     #获取id，页面数量过多时会保报错
    task=asyncio.ensure_future(g(i))
    ts.append(task)
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(ts))
print(time.clock()-t)

t=time.clock()
ts=[]
for i in l: #网上说用回调不会报错，但运行速度太慢，没有测试会不会报错
    task=asyncio.ensure_future(g(i))
    task.add_done_callback(callb)
    ts.append(task)
    loop.run_until_complete(task)
print(time.clock()-t)
