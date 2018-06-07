import requests,execjs,re,fake_useragent as fu
from lxml import etree

ua=fu.UserAgent()
    
u=r'http://www.goubanjia.com/'
r=requests.get(u,headers={'user-agent':ua.random})
r=etree.HTML(r.text)

#xpath取并集
s=r.xpath('//tr[@class="success"|//tr[@class="warning"]')      
for i in s:
    #xpath取文本
    print(i.xpath('string(.)'))
