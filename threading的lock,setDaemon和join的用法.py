#lock：被lock的代码似乎会按非多线程（或者说阻塞？）的方式执行，所以f，fff里t2的被lock的代码会阻塞，
#出现了吃饭和呼吸同时进行而跳舞等待，呼吸完成后吃饭和跳舞同时运行

#setDaemon(1/True)和join（）冲突，join后setDaemon会无效

#join设置主线程阻塞，t1.join将使主线程等待t1完成后再完成，
#所以ff的运行结果是先打印时间（不到1秒），然后t1和t2继续执行完

#t1.setDaemon设置主线程完成后直接退出，不等待t1完成，
#所以fff的运行结果是打印时间（不到1秒）后程序直接结束
#如果同时设置了join，主线程会等子线程执行完再运行，所以setDaemon无效

#用pool比较简单，但似乎无法运行不同的函数，例如写p.map（t1,***）；p.map（t2,***）会按阻塞的方式运行，
#所以ff，fff里用了Thread，而f里用了apply_async
#另外Pool用map和apply_async在未设置Pool.join()的情况下效果不一样，
#用map的话依旧等待子线程，相当于子线程设置了join（）；
#而apply_async不等待且直接退出，相当于子线程不设置join（）且设置了setDaemon（1）


import threading as th,multiprocessing as mu,time
from multiprocessing.dummy import Pool

def t1(a,b,c):
    for i in range(a):
        time.sleep(b)
        print('t111111111第{}次'.format(i),c)

def t2(a,b,c,l):
    l.acquire()
    for i in range(a):
        time.sleep(b)
        print('t2222第{}次'.format(i),c)
    l.release()
    
def f():
    ti=time.time()
    p=Pool(4)
    ts=[]
    l=th.Lock()
    p.apply_async(t1,(6,2,'吃饭'))
    p.apply_async(t2,(5,1,'呼吸呼吸',l))
    p.apply_async(t2,(3,2,'跳舞aaaaa',l))
    p.close()
    p.join()
    print(time.time()-ti)

def g():
    ti=time.time()
    p=Pool(4)
    p.starmap(t1,[(6,2,'吃饭'),(5,1,'呼吸呼吸'),(3,2,'跳舞aaaaa')])
    p.close()
    #p.join()
    print(time.time()-ti)

def ff():
    ti=time.time()
    ts=[]
    l=th.Lock()
    ts.append(th.Thread(target=t1,args=(6,2,'吃饭')))
    ts.append(th.Thread(target=t2,args=(5,1,'呼吸呼吸',l)))
    ts.append(th.Thread(target=t2,args=(3,2,'跳舞aaaaa',l)))
    for t in ts:
        t.setDaemon(1)   #setDaemin和join冲突
        t.start()
    print(time.time()-ti)

def fff():
    ti=time.time()
    ts=[]
    l=th.Lock()
    ts.append(th.Thread(target=t1,args=(6,2,'吃饭')))
    ts.append(th.Thread(target=t2,args=(5,1,'呼吸呼吸',l)))
    ts.append(th.Thread(target=t2,args=(3,2,'跳舞aaaaa',l)))
    for t in ts:
        t.start()
    print(time.time()-ti)  
    
if __name__ == '__main__':
    #f()
    g()
    #ff()
    #fff()
