import scrapy
from ..items import HupuItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import logging

class MySpider(CrawlSpider):
    name = 'Hupu'
    allowed_domains = []
    start_urls = ['https://bbs.hupu.com/topic']

    rules = (
        Rule(LinkExtractor(
            allow=('https://bbs.hupu.com/\d+\.html',)),
             callback='parse_item', follow=1),
    )

    def parse_item(self, response):    
        x=response.xpath(r'//div[@class="j_u"]/@uname').extract_first()
        logging.error(response.url+'@'*8+x)

    

    

'''
class MySpider(CrawlSpider):
    name = 'Hupu'
    allowed_domains = []
    start_urls = ['https://www.cnblogs.com']

    rules = (
        Rule(LinkExtractor(
            allow=('https://www.cnblogs.com/\w+/p/\d+.html',
                   'https://www.cnblogs.com/.*?-.*?.html')),
             callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        
        print(response.url)
        #yield response.url

'''
