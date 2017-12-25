import sqlite3,re
from bs4 import BeautifulSoup
from urllib.request import urlopen
con=sqlite3.connect('sb.db')
cur=con.cursor()
p='select * from lixi'
cur.execute(p)
for i in cur.fetchall():
    print(i)
cur.close()
con.close()
#cur.execute('create table liji (id integer primary key,url text)')
#cur.execute('create table lixi (id integer primary key,fromu text,tou text)')
#con.commit()
pages=set()
def youljma(urly):
    ppy='select * from liji where url="%s"' %urly
    cur.execute(ppy)
    rey=cur.fetchall()
    if rey==[]:
        cur.execute('insert into liji (url) values("%s")' %urly)
        con.commit()
        print(cur.lastrowid,'上')
        return cur.lastrowid 
    else:
        print(rey[0][0],'下')
        return rey[0][0]
    pages.add(urly)
def lianjie(fid,gid):
    ppy='select * from lixi where fromu="%i" and tou="%i"' %(fid,gid)
    cur.execute(ppy)
    rel=cur.fetchall()    
    if rel==[]:
        cur.execute('insert into lixi (fromu,tou) values("%i","%i")' %(fid,gid))
    else:print('rel:',rel)
def getl(url,cti):
    global pages
    if cti>2:return
    bs=BeautifulSoup(urlopen(r'http://en.wikipedia.org'+url))
    p=re.compile(r'^/wiki/((?!:).)*$')
    zz=bs.findAll('a',{'href':p})
    for i in zz:
        ii=i.attrs['href']
        lianjie(youljma(url),youljma(ii))
        if ii not in pages:
            pages.add(ii)
            getl(ii,cti+1)



    
