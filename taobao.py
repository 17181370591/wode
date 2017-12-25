from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
p=urlopen('https://buyertrade.taobao.com/trade/itemlist/list_bought_items.htm?spm=a3204.7139825.a2226mz.9.I5133L&t=20110530')
print(p.read())
