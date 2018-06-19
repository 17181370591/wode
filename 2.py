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
    ts=[]
    l=mu.Lock()
    ts.append(th.Thread(target=t1,args=(3,2,'吃饭')))
    ts.append(th.Thread(target=t2,args=(5,1,'呼吸呼吸',l)))
    ts.append(th.Thread(target=t2,args=(3,2,'跳舞aaaaa',l)))
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    print(time.time()-ti)

def g():
    ti=time.time()
    p=Pool(4)
    p.starmap(t1,[(3,2,'吃饭'),(5,1,'呼吸呼吸'),(3,2,'跳舞aaaaa')])
    p.close()
    #p.join()
    print(time.time()-ti)

def ff():
    ti=time.time()
    ts=[]
    l=mu.Lock()
    ts.append(th.Thread(target=t1,args=(3,2,'吃饭')))
    ts.append(th.Thread(target=t2,args=(5,1,'呼吸呼吸',l)))
    ts.append(th.Thread(target=t2,args=(3,2,'跳舞aaaaa',l)))
    for t in ts:
        t.setDaemon(1)   #setDaemin和join冲突
        t.start()
    print(time.time()-ti)

def fff():
    ti=time.time()
    ts=[]
    l=mu.Lock()
    ts.append(th.Thread(target=t1,args=(3,2,'吃饭')))
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
