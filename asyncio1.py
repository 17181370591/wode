import asyncio,time
#不加await会不等待主线程（？）
async def f(i):
    print('wait',i)
    await asyncio.sleep(i)
    return i**2

async def f1(i):
    print('wait',i)
    asyncio.sleep(i)
    return i**2

t=time.clock()
z=3
l=[]
for i in range(z):
    l.append(asyncio.ensure_future(f(i)))
loop=asyncio.get_event_loop()

loop.run_until_complete(asyncio.wait(l))
print(time.clock()-t)
for i in range(z):
    print(l[i].result())

t=time.clock()
l=[]
for i in range(z):
    l.append(asyncio.ensure_future(f1(i)))
loop=asyncio.get_event_loop()

loop.run_until_complete(asyncio.wait(l))
print(time.clock()-t)
for i in range(z):
    print(l[i].result())
