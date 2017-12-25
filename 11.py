from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime
global page
page=[]
global page,inn,outt
random.seed(datetime.datetime.now())
def getin(hhhh,urlin):
    inn=[]
     
    p=re.compile(urlin) 
    for hin in hhhh.findAll('a',{'href':p}) :

        if hin.attrs['href'] not in inn:
            inn.append(hin.attrs['href'])
            page.append(hin.attrs['href'])
     #     inn.append(hin)
#    print('内链列表：')
 #   print(inn)
    return inn
def getout(hhhh,urlout):
    outt=[]
    for hout in hhhh.findAll('a',{'href':re.compile('^(http|www)((?!'+urlout+').)*$')}):
 #   for hout in hhhh.findAll('a'):    
        if hout.attrs['href'] not in outt:
            outt.append(hout.attrs['href'])
            page.append(hout.attrs['href'])
          
 #   print('外链列表：')
 #   print(outt)
    return outt
def qieduan(url):
  #  print(url.replace('https://','').replace('http://','').replace('www.','').split('/')[0])
    return url.replace('https://','').replace('http://','').replace('www.','').split('/')[0]
def wailian(url):
    try:
        
        h=urlopen(url)
        hhhh=BeautifulSoup(h)
        url=qieduan(url)
        goo=getout(hhhh,url)
        getin(hhhh,url)
        getout(hhhh,url)
     #   print(goo)
        if len(goo)>0:
            return goo[random.randint(0,len(goo)-1)]
        else:
            return getin[random.randint(0,len(getin(hhhh,url))-1)]
    except Exception as e:
        dk(page[random.randint(0,len(page)-1)]) 
def dk(url):
    print(url)
    nurl=wailian(url)
    dk(nurl)
    
dk('http://www.baidu.com/')    
t=input('qsr:')
if t==a:
    exit
    
