#注意rules的回调函数和类函数的名字不能用parse，不然抓不到数据，原因不明

from scrapy import Spider, Request, FormRequest
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import logging
from redis import Redis

red=Redis(password='asd123')
logger = logging.getLogger(__name__)

class LJSpider(CrawlSpider):
    i=0
    name = "Hupu"
    start_urls = ["https://nj.lianjia.com/chengjiao/"]

    rules = (
        Rule(LinkExtractor(
            allow=(r'/chengjiao/[a-z]{4,}\d{0,2}/$',)),
            # https://nj.lianjia.com/chengjiao/jianye/
             callback='parse1', follow=1),
    )


    def parse1(self, response):       
        a=response.xpath('//ul[@class="listContent"]/li')[0]
        b=a.xpath('string(div/div[@class="title"])').extract()[0]
        red.lpush('x',response.url)
        red.lpush('y',b)
        self.i+=1
        logger.error(response.url+b+str(self.i)+'zzzzz')

