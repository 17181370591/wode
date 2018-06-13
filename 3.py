#http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC%2B%E5%A4%A7%E8%BF%9E&kw=python&p=1&isadv=0

import requests,re
from lxml import etree

u=r'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC%2B%E5%A4%A7%E8%BF%9E&kw=python&p=1&isadv=0'
tt=re.sub('[\t\n\r]*(  )+','',requests.get(u).text)
print(len(tt))
with open('1.txt','w',encoding='utf-8') as f:
    f.write(tt)
r=etree.HTML(tt)
s=r.xpath('//table[@class="newlist"]')


for i in s:
    j=i.xpath('.//td')
    q=[x.xpath('string(.)') for x in j]
    print('\t'.join(q))
