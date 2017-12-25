from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urlretrieve
bs=BeautifulSoup(urlopen(r'http://pythonscraping.com'))
im=bs.find('img',{'alt':'Home'}).attrs['src']
urlretrieve(im,r'c:\1.jpg')
