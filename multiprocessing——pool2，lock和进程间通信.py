#关于Lock和Manager().Lock()，详见https://blog.csdn.net/moxiaomomo/article/details/11470157
#multiprocessing.Manager().Lock()
#结论是：list在传入每个子进程时都传入副本，本身不受改变，
#Manager().list()传入的是本身，修改都会发生变化，
#线程池貌似传哪个都会改变自身
#即进程间通信必须使用multiprocessing.Manager()里的结构，
#线程间通信暂时不明，百度到的教程多使用queue的Queue队列，似乎说明不需要使用特殊的方法通信

#测试list和Manager().list() 的不同，进程间数据传递
import multiprocessing as mu
import time

def f(l,a):
    for i in a:
        l.append(i)
    print('f:::',l)

def g(l):
    while l:
        print(l.pop())
    print('===g===',l)

if __name__ == "__main__":
    l=mu.Manager().list()       
    #l=[]        
    l.extend(['a','b'])
    a='cd'
    p = mu.Pool(processes = 3)
    p1=[p.apply_async(f,(l,i)) for i in a]
    p2=p.apply_async(g,(l,))
    p.close()
    p.join()
    print(l)
    
'''
=====================================================================

l=[]的输出 
f:::[a,b,c]
f:::[a,b,c]
b
a
===g===[]
[a,b]

=====================================================================
'''

'''
=====================================================================

l=mu.Manager().list()
f:::[a,b,c]
f:::[a,b,c,d]
d
c
b
a
===g===[]
[]

=====================================================================
'''
