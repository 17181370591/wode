from gevent.pool import Pool 
from gevent import monkey 
# monkey.patch_all() 
monkey.patch_socket() 
monkey.patch_ssl()
import threading,time,requests,multiprocessing,gevent
from lxml import etree



url='https://bbs.hupu.com/topic-{}'
def p(page):
    a=0
    while True:
        r1=requests.get(url.format(page+1))
        r1=r1.text
        a+=1
        if len(r1)>1111:
            break
        if a>2:
            return
    r=etree.HTML(r1)    
    a=r.xpath('//a[@class="truetit"]')
    for i in range(5):
        print(a[i].xpath('string(.)')[:11])
    print('='*11)

if __name__=='__main__':
    b=5
    t=time.clock()
    for i in range(b):
        p(i)
    print('什么都不用',time.clock()-t)

    t=time.clock()
    ts=[] 
    for i in range(b):
        th=threading.Thread(target=p,args=(i,))
        ts.append(th)
        th.start()
        th.join()   
    print('多线程',time.clock()-t)

    '''   
    t=time.clock()
    ts=[] 
    for i in range(b):
        th=multiprocessing.Process(target=p,args=(i,))
        ts.append(th)
        th.start()
        th.join()   
    print('多进程',time.clock()-t)
    '''
    
    t=time.clock()
    ts=[] 
    for i in range(b):
        th=gevent.spawn(p(i))
        ts.append(th)
    gevent.joinall(ts)   
    print('协程',time.clock()-t)
