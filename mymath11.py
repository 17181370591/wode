import sqlite3,re
from bs4 import BeautifulSoup
from urllib.request import urlopen
con=sqlite3.connect('sb.db')
cur=con.cursor()
def jl():
    ppy='create table lijiiiii (id integer primary key,url text)'
    cur.execute(ppy)
    con.commit()
def youljma(urly):
    ppy='select * from lijiiiii where url="%s"' %urly
    print(ppy)
    cur.execute(ppy)
    rey=cur.fetchall()
    print(cur.rowcount)
    if rey!=[]:
        print(rey[0][0],'shang')
    else:    
        cur.execute('insert into lijiiiii (url) values("%s")' %urly)
        con.commit()
        print(cur.rowcount,cur.lastrowid,'xia')
    

#jl()        
youljma('e')        
