from multiprocessing import Pool
import time
import os

def test():
    print("---进程池中的进程---pid=%d,ppid=%d--"%(os.getpid(),os.getppid()))
    for i in range(3):
        print("----{}---{}".format(i,os.getpid()))
        time.sleep(1)
    return "hahah"

def test2(args):
    print("---callback func--pid=%d"%os.getpid())
    print("---callback func--args=%s"%args)

if __name__=='__main__':
    pool = Pool(3)
    pool.apply_async(func=test,callback=test2)

    #异步的理解：主进程正在做某件事情，突然来了一件需要立刻去做的事情，
    #那么这种在父进程去做某件事情时并不知道是什么时候去做的模式就称为异步
    while True:
        time.sleep(1)
        print("----主进程-pid=%d----"%os.getpid())

''' 可以看到调用 回调函数test2 的进程是主进程
---进程池中的进程---pid=44796,ppid=24640--
----0---44796
----主进程-pid=24640----
----1---44796
----主进程-pid=24640----
----2---44796
----主进程-pid=24640----
---callback func--pid=24640
---callback func--args=hahah
----主进程-pid=24640----
----主进程-pid=24640----
----主进程-pid=24640----
...................
'''
