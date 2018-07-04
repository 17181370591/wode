import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import logging
from ..items import HupuItem

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
        if 1:
            i=ps[-1]
            it=HupuItem()
            x=i.xpath('@alt').extract_first()
            y=i.xpath('@src').extract_first()
            lo.error(response.url+'@'*8+x+y)
            it['t']=x
            it['image_url']=y
            yield it

    
#https://bbs.hupu.com/22807587.html
