from threading import Thread,currentThread
from multiprocessing import Process
import os,time

a = 100

def f1():
    global a
    for i in range(3):
        a=a+1
    print("f1 a=",a)

def f2():
    global a
    print("f2 a=",a)

if __name__=='__main__':
    p1=Process(target=f1)
    p1.start()
    p2=Process(target=f2)
    p2.start()

    print('=' * 22)
    time.sleep(1)

    t1=Thread(target=f1)
    t1.start()
    t2=Thread(target=f2)
    t2.start()


'''输出如下：
f1 a= 103
f2 a= 100
f1 a= 103
f2 a= 103
主进程和两个子进程的a都是100,p1进程修改a成103,p2和主进程的a不变，
然后t1和t2是主进程的子线程，会修改主进程的a，
说明进程的变量都不共享(有各自的内存空间)，线程的全局变量共享
'''
