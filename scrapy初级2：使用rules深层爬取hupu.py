#这里的rules表示scrapy先请求start_urls，对response里满足allow的正则的链接（a标签的href属性，
#注意allow的值是元组，可以多写几个取并值），回调函数self.parse_item，即打印帖子html文件里的作者，
#extract_first()打印第一个，值为空时不报错，有默认值就返回默认值('没有找到'))，可以不填默认值；
#follow=False表示找完start_urls里满足正则的链接，访问链接后打印作者就完成了；
#而follow=True表示找完start_urls里满足正则的链接，还要在这些链接里找满足正则的链接，
#一直找下去，并且把所有访问过的链接的作者打印

import scrapy
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
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):    
        x=response.xpath(r'//div[@class="j_u"]/@uname').extract_first('没有找到')
        logging.error(response.url+'@'*8+x)

    

    
