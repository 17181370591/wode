from bs4 import BeautifulSoup
import re,os
from urllib.request import urlopen,urlretrieve
i=0
for i in range(919,961,20):
    print('http://hgamecg.com/index/category/2032-_ensemble_sweet_koi_suru_ojou_sama_wa_ecchi_na_hanayome/start-%i' %i)
    html=urlopen('http://hgamecg.com/index/category/2032-_ensemble_sweet_koi_suru_ojou_sama_wa_ecchi_na_hanayome/start-%i' %i) 
    bs=BeautifulSoup(html)
    ppp=re.compile(r'.*')
    pp=bs.findAll('a',{'class':'col-thumbnail'})
    rr=r'c:\down'
    if not os.path.exists(rr):
        os.makedirs(rr)
    for i in pp:
        sr=i.attrs['href']
        a=sr.split('/')
        
        cdz=i.attrs['href']
        while '../' in cdz:
            cdz=cdz.replace('../','')
        dz='http://hgamecg.com/'+cdz
        print(sr,len(pp),dz)
        
        urlretrieve(dz,rr+'\\'+a[len(a)-3]+'.jpg')
#print(len(pp))
