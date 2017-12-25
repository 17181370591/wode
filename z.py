from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def gett(url):
    try:
        h=urlopen(url)
    except HTTPError as e1:
        return e1
    try:
        hh=BeautifulSoup(h.read())
        t=hh.head
    except AttributeError as e2:
        return e2
    return t
print(gett('http://www.pythonscraping.com/pages/warandpeace.html'))
