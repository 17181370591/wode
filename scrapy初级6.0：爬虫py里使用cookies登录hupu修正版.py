#用已经登录成功的cookies伪装登录，d是cookies字典
#直接在start_requests的scrapy.Request里设置好cookies就可以登录了，


#response.request.headers.getlist('Cookie')[0].decode()可以得到cookies的类似url链接的文本（str），
#reco接收这个文本，并进行修改，返回的cs1是长度为0的list，内容是修改后的cookies的类似url链接的文本(bytes)，


#settings.py里有COOKIES_ENABLED配置，默认为True，这种情况下，
#在spider.py用cookies伪装登录后会访问其他页面scrapy会自动处理cookies，设为false会访问失败。
#但如果在settings.py设置cookies需要设置为false，详情见初级6.2


====================================================================================

#spider.py
import scrapy
class MySpider(scrapy.Spider):
    name = 'Hupu'
    start_urls = [r'https://bbs.hupu.com/topic-12']
    d={'_fmdata':'kYqIQs9LTYz5oRjOMdPb5iB6bclI6hqFswD5tXPSkD%2FcaKyCqSGi5cytdTcXbHzuqikmcDIabpykxIC7e8anCwZ3DY1NSSBrF0jE1yBSfks%3D',
    'us':'9b1005328020120a3ee8a32ce9f717db590c7cf302f799bdcf9854a6985ccb916dfeac9c343894e00b5e7b01847f2fa228d42d409c2854944882bcfec3a5e1c4',
   'u':'35048460|6Zi/5Y2h6KW/MQ==|4015|a624d0ae11f14f7df55e50e48f082772|11f14f7df55e50e4|aHVwdV8yZjQxZjJiM2YwNTg1ZTQw',
   '_CLT':'00376064be821b71351c003dda774e37',
   'PHPSESSID':'1d5bb84a87b96c3bc5531567068e0fbf',
   '_HUPUSSOID':'d3e074f0-a69b-4268-9326-8ae765546e4c',
   '__guid':'13421668.1702922777230312000.1508844317035.6482',
   }
    
    def parse(self, response):
        print(len(response.text))  
        print(response.text[:1111])
        
    def start_requests(self):
        yield scrapy.Request(self.start_urls[0],
                             callback=self.parse,
                             cookies=self.d)


====================================================================================

#settings.py
        
# -*- coding: utf-8 -*-
import fake_useragent as fu

BOT_NAME = 'Hupu'

SPIDER_MODULES = ['Hupu.spiders']
NEWSPIDER_MODULE = 'Hupu.spiders'

ua=fu.UserAgent()
ROBOTSTXT_OBEY = False

#COOKIES_ENABLED = True                         #默认为True，设置成false不会自动处理cookies
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'USER-AGENT ': ua.random ,

}
