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
                
async def g(i):     #获取帖子第一页所有id
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

t=time.clock()
j=2
#运行f(),获取帖子地址
ts=[asyncio.ensure_future(f(i)) for i in range(1,j)]
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(ts))
print(time.clock()-t)

#1，获取id，页面数量过多时（1000左右）会保报错
t=time.clock()      
ts=[asyncio.ensure_future(g(i)) for i in l]    
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(ts))
print(time.clock()-t)

#2，写成回调形式，效果同1，一次只能运行1和2中的一个
t=time.clock()
ts=[]
loop=asyncio.get_event_loop()
for i in l:
    task=asyncio.ensure_future(g1(i))
    task.add_done_callback(callb)
    ts.append(task)
loop.run_until_complete(asyncio.wait(ts))
print(time.clock()-t)

