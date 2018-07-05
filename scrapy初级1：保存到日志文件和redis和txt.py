#settings.py里面要设置ROBOTSTXT_OBEY = False，不然有些网站会不爬取

scrapy抓取什么值得买信用卡前两页的标题。目录如下
test1/
    spiders/
        __init__.py
        fuck.py
    items.py
    middlewares.py
    pipelines.py
    settings.py
#cmd输入scrapy crawl smzdm运行，可以发现spider里的爬虫文件名字可以乱取
        
#================================================================================
#fuck.py
import scrapy
from ..items import Test1Item

class SMSpider(scrapy.Spider):
    name='smzdm'
    start_urls=['https://www.smzdm.com/fenlei/xinyongka/',
                'https://www.smzdm.com/fenlei/xinyongka/p2/#feed-main']

    def parse(self,response):
        zf=Test1Item()
        r=response
        r1=r.xpath('//h5//span[contains(@class,"-mark")]/text()').extract()
        r2=r.xpath('//h5//span[@class="z-highlight"]/text()').extract()
        print(len(r1),len(r2))
        x=zip(r1,r2)
        for i,j in x:
            zf['tag']=i
            zf['content'] = j
            yield zf
            
#================================================================================
#================================================================================
#items.py
# -*- coding: utf-8 -*-
# Define here the models for your scraped items
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Test1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tag = scrapy.Field()
    content= scrapy.Field()
    pass

#================================================================================
#================================================================================
#middlewares.py
#================================================================================
#================================================================================
#pipelines.py
# -*- coding: utf-8 -*-

from redis import Redis

import logging
logger = logging.getLogger(__name__)

class Test1Pipeline(object):
    def __init__(self):
        self.i = 0

    def open_spider(self,spider):
        self.r=Redis(password='asd123')

    def spider_close(self,spider):
        pass

    def process_item(self, item, spider):
        print(self.i,spider.name)
        self.i+=1
        self.r.sadd('a',item['tag']+'@@@'+item['content'])
        logger.warning(item)                                #打印日志，item默认会以debug形式打印
        return item

class Test2Pipeline(object):
    def process_item(self, item, spider):        
        with open('1.txt','a',encoding='utf8') as f:
            f.write(item['tag']+'@@@'+item['content']+'\n')
        return items   
    
#================================================================================
#================================================================================
#settings.py
ITEM_PIPELINES = {
   'test1.pipelines.Test1Pipeline': 300,
    'test1.pipelines.Test2Pipeline': 400,       #有教程说这两个值要不同，但似乎可以相同
}

ROBOTSTXT_OBEY = False

LOG_LEVEL = 'DEBUG'                 #设置日志输出的最低标准
LOG_FILE = 'new.txt'                #日志保存位置


import fake_useragent               #设置请求头
ua=fake_useragent.UserAgent()
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
    'user-agent':ua.random
}
#================================================================================
