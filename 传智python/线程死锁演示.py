from threading import Thread,Lock
import os,time,sys

mutexA = Lock()
mutexB = Lock()
print(mutexA,mutexB)

def f(a,b):
    name=sys._getframe().f_code.co_name
    a.acquire()
    print('{} on'.format(a))
    time.sleep(.1)
    b.acquire()
    print('{} on'.format(b))

    b.release()
    print('{} off'.format(b))
    a.release()
    print('{} off'.format(a))

if __name__=='__main__':
    t1=Thread(target=f,args=(mutexA,mutexB))
    t1.start()

    time.sleep(1)
    t2=Thread(target=f,args=(mutexB,mutexA))
    t2.start()
