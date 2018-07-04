'''
获取虎扑足球首页的帖子里第一页随机获取一个用户的用户名和头像，但是遇到头像地址相同的用户不会重复下载
spider里设置了getLogger，同时在文件和控制台显示/保存日志
设置ITEM_PIPELINES = {
    'Hupu.pipelines.HupuPipeline': 300,
    'Hupu.pipelines.HupupicPipeline':111,
}后，可以看到HupupicPipeline先对items进行处理，但时间较长，
所以后来HupuPipeline和HupupicPipeline一起处理items。
由于HupuPipeline的处理里，不满足条件的items不会被返回，所以如果先用HupuPipeline进行处理，
会出现HupupicPipeline处理时候出现找不到items的情况。
'''

==============================================================
#hupy1.py

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import logging,random
from ..items import HupuItem
from redis import Redis

#使用redis验证收集到的用户信息是否正确，因为第一页一般有90多个用户，但下载的图片一般只有60多个，
#使用redis，发现收集到 了90+用户的id的图片地址，但图片地址set去重后，发现确实只有60多个
red=Redis(password='asd123')            
def loo():
    logger=logging.getLogger()
    handler = logging.FileHandler("1.txt")
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(console)
    return logger
lo=loo()

class MySpider(CrawlSpider):
    name = 'Hupu'
    start_urls = ['https://bbs.hupu.com/topic']

    rules = (
        Rule(LinkExtractor(
            allow=('https://bbs.hupu.com/\d+\.html',)),
             callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        ps=response.xpath(r'//img[@src and @alt]')
        if 1:                                       #这里以前使用了一个循环爬取第一页所有用户，不改回去了
            i=random.choice(ps)
            it=HupuItem()
            x=i.xpath('@alt').extract_first()
            y=i.xpath('@src').extract_first()
            red.lpush('a',x)
            red.lpush('b',y)
            lo.error(response.url+'@'*8+x+y)
            it['t']=x
            it['image_url']=y
            yield it

    
==============================================================
#settings.py

# -*- coding: utf-8 -*-
BOT_NAME = 'Hupu'

SPIDER_MODULES = ['Hupu.spiders']
NEWSPIDER_MODULE = 'Hupu.spiders'
#LOG_LEVEL='DEBUG'
#LOG_FILE='1.txt'

ROBOTSTXT_OBEY = True

DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
}

# 避免下载最近90天已经下载过的文件内容
FILES_EXPIRES = 90


# 避免下载最近90天已经下载过的图像内容
IMAGES_EXPIRES = 90

ITEM_PIPELINES = {
    'Hupu.pipelines.HupuPipeline': 300,
    'Hupu.pipelines.HupupicPipeline':111,
}

IMAGES_STORE='e:\\hupu\pic'
'''
# 设置图片缩略图
IMAGES_THUMBS = {
    'small': (50, 50),
    'big': (250, 250),
}
# 图片过滤器，最小高度和宽度，低于此尺寸不下载
IMAGES_MIN_HEIGHT = 110
IMAGES_MIN_WIDTH = 110
'''

==============================================================
#pipelines.py

import scrapy,logging,time,datetime,re,os
from redis import Redis
from scrapy.pipelines.images import ImagesPipeline

r1=re.compile("[\|\\\?\*\<\":\>\+\[\]\/\']+")                   #去掉非法字符
def safename(name):
    return re.sub(r1,'',name)

class HupuPipeline(object):
    def __init__(self):
        self.r=Redis(password='asd123')
        self.r1=self.r.smembers('hupuname')

    def process_item(self, item, spider):
        x=item['t']
        if len(x)>7 and x.encode() not in self.r1:
            self.r.sadd('hupuname',x)
            logging.error('self.r.scard(hupuname)={}'.
                          format(self.r.scard('hupuname')))
            with open('2.txt','a',encoding='utf8') as f:
                f.write(x+'\n')
            return item

class HupupicPipeline(ImagesPipeline):#继承ImagesPipeline这个类
    
    def get_media_requests(self, item, info):
        #logging.warning('报错地址：：：'+item['image_url'])
        yield scrapy.Request(item['image_url'])

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        #print("E:\\Hupu\\pic\\",'@'*33,image_paths[0])
        if not image_paths:
            print("Item contains no images")
        if item['t']:                                       #文件改名，改成用户名.jpg
            newname = item['t']+ '.'+image_paths[0].split('.')[-1]
            os.rename("E:\\Hupu\\pic\\" + image_paths[0],
                      "E:\\Hupu\\pic\\" + newname)
        return item
    

