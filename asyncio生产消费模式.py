

'''
#原写法
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
'''

#换成asyncio的写法，下面添加的sleep全部是为了与单线程作比较用，不用添加

import asyncio,time

async def consumer(n):
    if not n:
       return
    print('[CONSUMER] Consuming %s...' % n)
    #await asyncio.sleep(.2)
    return '200 OK'

async def produce(i,x):
    n = 0
    while n < x:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = await consumer(n)
        await asyncio.sleep(1)
        print('[PRODUCER] Consumer return: %s' % r,'我是第{}个协程'.format(i))

def p(i,x):
    n = 0
    while n < x:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        time.sleep(1)
        r=consumer(n)
        print('[PRODUCER] Consumer return: %s' % r,'我是第{}个'.format(i))


x=5
loop=asyncio.get_event_loop()
ts=[]
for i in range(4):
    ts.append(asyncio.ensure_future(produce(i,x)))
loop.run_until_complete(asyncio.wait(ts))

for i in range(4):
    p(i,x)
