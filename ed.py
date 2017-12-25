from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
def ed(url):
    hh=BeautifulSoup(urlopen(url))
    p=re.compile(r'^http.((?![eE]).)*$')
    hhh=hh.findAll([],{'href':p})   
    return hhh

pp=ed('https://en.wikipedia.org/wiki/Kevin_Bacon')

for i in pp:
    print(i.attrs['href'])
print(len(pp))    
