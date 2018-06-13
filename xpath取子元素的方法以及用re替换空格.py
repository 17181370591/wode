#http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC%2B%E5%A4%A7%E8%BF%9E&kw=python&p=1&isadv=0
#对etree.HTML元素进行一次查找得到s后，继续查找s的子元素要用'.//*' ，里面的.表示在当前元素进行查找！！！
#对html文件用\s+可以替换所有空格，但是也会导致<a href='****'>成<ahref='****'>而无法抓取a，
#所以用了sub替换'[\t\n\r]*  +'成''，即连续有两个空格才会被替换，这里无法替换单独[\t\n\r]+，但是用|会出问题，好像是无法匹配空格，原因不明


import requests,re
from lxml import etree

u=r'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC%2B%E5%A4%A7%E8%BF%9E&kw=python&p=1&isadv=0'
tt=re.sub('[\t\n\r]*  +','',requests.get(u).text)
print(len(tt))
with open('1.txt','w',encoding='utf-8') as f:
    f.write(tt)
r=etree.HTML(tt)
s=r.xpath('//table[@class="newlist"]')


for i in s:
    j=i.xpath('.//td')
    q=[x.xpath('string(.)') for x in j]
    print('\t'.join(q))
