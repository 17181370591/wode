from multiprocessing import Process
import time

def test(a,b):
    for i in range(3):
        print("{}---test---{}".format(a,b))
        time.sleep(0.1)

if __name__=="__main__":
    l=[]
    for i in range(5):
        p = Process(target=test,args=(i,time.clock()))
        l.append(p)
        #让这个进程开始执行test函数里的代码
    for p in l:
        p.start()
        p.join(0.15)
#join()⽅法可以等待⼦进程结束后再继续往下运⾏，
# 通常⽤于进程间的同步
#堵塞,0.15表示超时时间，也可以不加参数
    print("---main---")

