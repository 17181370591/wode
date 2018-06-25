import threading
import asyncio

async def hello():
    print('Hello world!')
    await asyncio.sleep(1)
    print('Hello again!')

async def hello222():
    print('Hello world!222')
    result = await somework()
    print('Hello again!222,result: ',result)
    return result

async def somework():
    print('start doing job...')
    await asyncio.sleep(2)
    print("hi, I've done the job")
    return("hi, I've done the job............")

loop = asyncio.get_event_loop()
tasks = [hello(), hello222()]
a=loop.run_until_complete(asyncio.wait(tasks))
loop.close()
for i in list(a[0]):
    print(i,i.result())
