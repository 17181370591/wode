from threading import Thread,currentThread
import os,time

def worker(num):
    for i in range(5):
        pid=os.getpid()
        tid=currentThread().ident
        print("=={}--{}=={}".format(pid,tid,num))
        time.sleep(0.1)

if __name__=='__main__':
    l=[]
    for i in range(3):
        t=Thread(target=worker,args=(i,))
        l.append(t)
    for i in l:
        i.start()
        i.join(0.2)
        #join()⽅法可以等待⼦进程结束后再继续往下运⾏，
# 通常⽤于进程间的同步
#堵塞,0.2表示超时时间，也可以不加参数
    print(0)

