import requests,re,fake_useragent,pandas as pd,time
from lxml import etree
import execjs
from multiprocessing import Pool,Manager

se=requests.session()
ua=fake_useragent.UserAgent()
u=r'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E5%BD%B1&start={}&genres={}'
h={'user-agent':ua.random}
ip='171.38.37.153:8123'
p={'http':'http://{}'.format(ip)}
a=[]

def f(x,a=a):
    i=0
    u=r'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E5%BD%B1&start={}&genres={}'

    u=u.format('{}',x)
    
    while True:
        aa=set()
        r=se.get(u.format(str(i)),headers=h,proxies=p,verify=True)
        data=r.json()['data']
        l=len(data)
        print('本业数量',l)
        for j in data:
            b=(x,j['title'])
            if b not in a:
                a.append(b)
                aa.add(b)
        c=pd.DataFrame(list(aa))
        c.to_csv(r'C:\Users\Administrator\Desktop\1\1.csv',\
                 mode='a',encoding='gb18030')
        if l<20:
            break
        i+=10
        print('已经收集',len(a))
        



if __name__=='__main__':
    try:
        man = Manager()
        a=man.list()       
        pool = Pool(4)
        us=['悬疑','同性','音乐']
        z=pool.starmap(f, zip(us,(a,a,a)))
        pool.close()
        pool.join()
    finally:
        pass
