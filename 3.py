import requests,execjs,re,fake_useragent as fu
from lxml import etree

ua=fu.UserAgent()
    
u=r'http://www.goubanjia.com/'
r=requests.get(u,headers={'user-agent':ua.random})
r=etree.HTML(r.text)
s=r.xpath('//tr[@class="success"||"warning"]')
for i in s:
    print(i.xpath('string(.)'))
