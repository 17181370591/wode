import os,os.path,re,time
from bs4 import BeautifulSoup
from urllib.request import urlopen,urlretrieve
count=0
co=1
def xiazai(url):
    zz=time.clock()
    print(url)
    a=set()
    d={}
    global a,d
    b=qiming(url)
    bs=BeautifulSoup(urlopen(url))
    p=re.compile(r'.*')
    pp=bs.findAll('a',{'onclick':'return hs.expand(this)'})
    do=r'c:\down'
    for i in pp:
        a.add(i.attrs.get('href'))        
    #    d=dict(zip(a,c))
    #    print(d)
    for i in a:
        if i:
            global co
        #    t=i.split('/')
        #    print('di是这么多',d[i],i,co)
            urlretrieve(i,do+r'\\'+str(co)+'.jpg') 
            co=co+1
    zzz=time.clock()
    print('这一轮花了',zzz-zz,'秒')
def qiming(url):
    b=set()
    c=set()
    global b,c
    bss=BeautifulSoup(urlopen(url))
    ppp=bss.findAll('a',{'onclick':'atarget(this)'})
    cop=re.compile(r'(【.*?】)*.*?')
    for i in ppp:
        if len(i.attrs)==3 and '【' in i.get_text():
            b.add(i.get_text())     
    for i in b:
        s=cop.search(i).group()
        c.add(i.replace(s,''))
 #   print(c)
    return c


t=1

while True:
    try:
        url=r'https://bbs.zdfx.net/forum-61-%i.html' %t    
        xiazai(url)
        t=t+1
        

    except Exception as e:
        break
    
    

    
#print(len(a),a,'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')    
    
        
