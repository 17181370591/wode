#这里设置ua只是用了settings，也可以直接在spider里设置，实际情况可以用fake_useragent
#设置proxy比较麻烦

===========================================================================    

#hupu.py
import scrapy

class MySpider(scrapy.Spider):
    name = 'Hupu'
    start_urls = ['http://httpbin.org/get',]
    
    def parse(self, response):
        print('*'*33,response.url,response.body)
    
    def start_requests(self):
        # 带着cookie向网站服务器发请求，表明我们是一个已登录的用户
        yield scrapy.Request(self.start_urls[0],callback=self.parse)

===========================================================================     

#settings.py
# -*- coding: utf-8 -*-
BOT_NAME = 'Hupu'

SPIDER_MODULES = ['Hupu.spiders']
NEWSPIDER_MODULE = 'Hupu.spiders'

ROBOTSTXT_OBEY = False

DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
   'USER-AGENT ': 'fuck u 3 times'
}
  
IPS=["118.190.95.26:9001","183.48.91.107:8118",]

DOWNLOADER_MIDDLEWARES = {
    #'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None, 
    'Hupu.middlewares.MyproxiesMiddleware': 400,
}

=========================================================================== 

#middlewares.py

from scrapy import signals
import random
from .settings import IPS
 
class MyproxiesMiddleware(object):
 
      def __init__(self,ip=''):
          self.ip=ip
       
      def process_request(self, request, spider):
          thisip=random.choice(IPS)
          print("this is ip:"+thisip)
          request.meta["proxy"]="http://"+thisip


