#在settings.py里设置cookies访问，这里的cookies一定要是key=value;的一串字符串格式
'''
原文地址：http://www.cnblogs.com/cnkai/p/7418330.html
注意：     
请把settings.py里COOKIES_ENABLED设置为 False，你可能觉得奇怪，为什么我们使用了cookie却需要把它设置为False，
原因在于，我们直接把cookie放在了请求头里面，但是scrapy默认自己拥有一套处理cookie的中间件，
当你把它设置为True的时候，两者会产生影响，从而请求失败，你可以自己尝试一下。
那如果我执意要把他设置为True呢，难道就不能解决了么？
当然是可以的，但是我们今天就不在深入的讨论这个问题，以后可以单独解释。
'''

================================================================================

#spider.py
import scrapy
class MySpider(scrapy.Spider):
    name = 'Hupu'
    start_urls = [r'https://bbs.hupu.com/topic-12']

    def parse(self, response):
        print(response.text)
        print(response.text[:1111])
        
================================================================================

#settings.py

# -*- coding: utf-8 -*-
import fake_useragent as fu

BOT_NAME = 'Hupu'

SPIDER_MODULES = ['Hupu.spiders']
NEWSPIDER_MODULE = 'Hupu.spiders'

ua=fu.UserAgent()
ROBOTSTXT_OBEY = False
dd={'_fmdata':'kYqIQs9LTYz5oRjOMdPb5iB6bclI6hqFswD5tXPSkD%2FcaKyCqSGi5cytdTcXbHzuqikmcDIabpykxIC7e8anCwZ3DY1NSSBrF0jE1yBSfks%3D',
    'us':'9b1005328020120a3ee8a32ce9f717db590c7cf302f799bdcf9854a6985ccb916dfeac9c343894e00b5e7b01847f2fa228d42d409c2854944882bcfec3a5e1c4',
   'u':'35048460|6Zi/5Y2h6KW/MQ==|4015|a624d0ae11f14f7df55e50e48f082772|11f14f7df55e50e4|aHVwdV8yZjQxZjJiM2YwNTg1ZTQw',
   '_CLT':'00376064be821b71351c003dda774e37',
   'PHPSESSID':'1d5bb84a87b96c3bc5531567068e0fbf',
   '_HUPUSSOID':'d3e074f0-a69b-4268-9326-8ae765546e4c',
   '__guid':'13421668.1702922777230312000.1508844317035.6482',
   }
cc=''
for i in dd.keys():
    cc+=i+'='+dd[i]+';'
cc=cc[:-1]

COOKIES_ENABLED = False                         #重要
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'USER-AGENT ': ua.random ,
   'Cookie':cc
}
