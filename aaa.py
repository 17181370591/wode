from bs4 import BeautifulSoup
from urllib.request import *
import re,json
import time,random,datetime
import sqlite3
conn=sqlite3.connect(r'c:\python34\ip2.db')
curs=conn.cursor()
#query='create table ip2(ip text primary key,gj text,sheng text,city text)'
#curs.execute(query)
random.seed(datetime.datetime.now())
a=set()
url='https://en.wikipedia.org/wiki/The_Twilight_Zone_(1959_TV_series)'
def getip(url):
    hurl='https://en.wikipedia.org/w/index.php?title='+\
      url.replace('https://en.wikipedia.org/wiki/','')+\
      '&offset=&limit=500&action=history'
    bs=BeautifulSoup(urlopen(hurl))
    ipl=bs.findAll('a',{'class':'mw-userlink mw-anonuserlink'})
    global a
    for ip in ipl:
        if len(ip.get_text())<17:
            a.add(ip.get_text())
    return a    
def dizhi(b):
    for i in b:
        js=urlopen('http://freegeoip.net/json/'+i).read().decode()
        jj=json.loads(js)
        print(i+'  : '+jj.get('country_name')+','+jj.get('region_name')+',' +jj.get('city'))
        qu='insert into ip2 values(?,?,?,?)'
        qq=i,jj.get("country_name"),jj.get("region_name"),jj.get("city")
        curs.execute(qu,qq)
        conn.commit()
def dakai(url):
    dizhi(getip(url))
    bs=BeautifulSoup(urlopen(url))
    p=re.compile(r'^/wiki/((?!File).)*$')
    pp=bs.findAll('a',{'href':p})
    s=random.choice(pp).attrs['href']
    print(s)
    dakai('https://en.wikipedia.org'+s)
dakai(url)    


    

    

