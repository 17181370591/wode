#python C:\Users\Administrator\Desktop\1\1.py
import asyncio,time,multiprocessing as mu,threading as th
from multiprocessing.dummy import Pool 

#进程池消耗最大，不能开的太多，不然内存和cpu飙升容易会卡死，这次开了默认值4（4核），貌似开16个进程更快也更卡
#99:28,33:9.7（表示99个任务用28s）

#线程池：比进程轻量很多，如果和进程开一样大速度差不多，但比进程能开得大很多
#9999：6.3,33333：29.3,99999_内存不够用卡死

#协程：比线程轻量很多，也快很多
#9999：2.2,33333：5.2,99999：16s，cpu50%内存1G

#多进程+协程:比单独协程更快，也更卡
#99999：10.3s,cpu90%内存1G，999999：106s,cpu100%内存3.3g

#貌似协程可以完全取代线程，追求更快就用进程+协程

z=99999                 #任务数
num=int(z/4)            #在多进程+协程中用来切割分配任务

async def f1(i):        #协程测试用
    print('wait',i)
    await asyncio.sleep(1)
    return i**2

def f2(i):              #普通测试用
    print('wait',i)
    time.sleep(1)
    return i**2

def xc(x):              #进程+协程测试用
    loop=asyncio.get_event_loop()
    ts=[]
    for i in range(x,x+num):
        ts.append(asyncio.ensure_future(f1(i)))
    loop.run_until_complete(asyncio.wait(ts))
    
if __name__=='__main__':
    t1=time.clock()
    
    '''
    #进程池和线程池
    #p=mu.Pool(4)
    p=Pool(z)
    l=[]
    p.map(f2,range(z))
    p.close()
    p.join()
    '''
    
    #'''
    #协程
    loop=asyncio.get_event_loop()
    ts=[]
    for i in range(z):
        ts.append(asyncio.ensure_future(f1(i)))
    loop.run_until_complete(asyncio.wait(ts))
    #'''

    '''
    #多进程+协程
    p=mu.Pool(4)
    p.map(xc,[0,num,num*2,num*3])
    p.close()
    p.join()    
    '''    
    print(time.clock()-t1)
    
