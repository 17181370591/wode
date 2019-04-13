from multiprocessing import Pool,Process,Manager
import os,time

def worker(num):
    for i in range(2):
        print("===pid=%d==num=%d="%(os.getpid(), num))
        time.sleep(0.1)

if __name__=='__main__':
    q=Manager().Queue()     #进程池不能使用multiprocessing.Queue()
    po=Pool(2)
    for i in range(9):
        q.put(i)
    while not q.empty():
        a=q.get()
        po.apply_async(worker,(a,))

    po.close()
    po.join()
