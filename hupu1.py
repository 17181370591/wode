import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import logging
from ..items import HupuItem

class MySpider(CrawlSpider):
    name = 'Hupu'
    start_urls = ['https://bbs.hupu.com/topic']

    rules = (
        Rule(LinkExtractor(
            allow=('https://bbs.hupu.com/\d+\.html',)),
             callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        it=HupuItem()
        x=response.xpath(r'//div[@class="j_u"]/@uname').extract_first('没有找到')
        logging.error(response.url+'@'*8+x)
        it['t']=x
        yield it

    
