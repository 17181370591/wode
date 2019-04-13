from threading import Thread,currentThread,Lock
from multiprocessing import Process
import os,time

a=[1]
mutex = Lock()
x=1000

def f1(a):
    for i in range(x):
        mutex.acquire()
        a[0]=a[0]+1
        print('f111-----{}'.format(a))
        mutex.release()
        time.sleep(.001)



def f2(a):
    for i in range(x):
        mutex.acquire()
        a[0]=a[0]+1
        print('f2--{}'.format(a))
        mutex.release()
        time.sleep(.001)


if __name__=='__main__':
    t1=Thread(target=f1,args=(a,))
    t1.start()

    #time.sleep(1)
    t2=Thread(target=f2,args=(a,))
    t2.start()
