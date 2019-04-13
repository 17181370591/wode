from threading import Thread,currentThread
from multiprocessing import Process
import os,time



def f1(a):
    for i in range(3):
        a.append(1)
    print("f1 a=",a)

def f2(a):
    print("f2 a=",a)

if __name__=='__main__':
    a = []
    p1=Process(target=f1,args=(a,))
    p1.start()
    p2=Process(target=f2,args=(a,))
    p2.start()

    print('=' * 22)
    time.sleep(1)

    t1=Thread(target=f2,args=(a,))
    t1.start()
    t2=Thread(target=f1,args=(a,))
    t2.start()
    t3=Thread(target=f2,args=(a,))
    t3.start()

'''输出如下：
f1 a= [1, 1, 1]
f2 a= []
f2 a= []
f1 a= [1, 1, 1]
f2 a= [1, 1, 1]
主进程和p1，p2的a都是[]，p1修改a成[1,1,1]不影响令两个进程，
t1,t2,t3会修改主进程的a,所以t3输出的a也是[1,1,1]，
如果a不是引用而是不同变量，则明显不会修改a
'''
