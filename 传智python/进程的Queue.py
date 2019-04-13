from multiprocessing import Pool,Process,Queue
import os,time

def worker(num):
    for i in range(2):
        print("===pid=%d==num=%d="%(os.getpid(), num))
        time.sleep(0.1)

if __name__=='__main__':
    q=Queue()
    l=[]
    for i in range(5):
        q.put(i)
    while not q.empty():
        a=q.get()
        b = Process(target=worker, args=(a,))
        l.append(b)
    for i in l:
        i.start()
