from threading import Thread,Lock
import os,time
from queue import Queue

mutex = Lock()
produceCount=0
queue=Queue()

def produce(name):
    global produceCount
    while 1:
        if queue.qsize()<200:
            for i in range(3):
                mutex.acquire()
                produceCount=produceCount+1
                x='telephone {} produced by 工人{}号'
                print(x.format(produceCount,name))
                queue.put(produceCount)
                mutex.release()


def use(name):
    while 1:
        if queue.qsize() >0:
            time.sleep(.001)
            x='消费者{}购买了{}号手机,当前库存{}'
            a,b=queue.get(),queue.qsize()
            print(x.format(name,a,b))

if __name__=='__main__':
    for i in range(5):
        t1 = Thread(target=produce, args=(i,))
        t1.start()
    for i in range(20):
        t1 = Thread(target=use, args=(i,))
        t1.start()


