#这里的rules表示scrapy先请求start_urls，对response里满足allow的正则的链接（a标签的href属性，
#注意allow的值是元组，可以多写几个取并值），回调函数self.parse_item，即打印帖子html文件里的作者，
#extract_first()打印第一个，值为空时不报错，有默认值就返回默认值('没有找到'))，可以不填默认值；
#follow=False表示找完start_urls里满足正则的链接，访问链接后打印作者就完成了；
#而follow=True表示找完start_urls里满足正则的链接，还要在这些链接里找满足正则的链接，
#一直找下去，并且把所有访问过的链接的作者打印

============================================================================

#hupu.py，爬虫spider文件

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import logging

class MySpider(CrawlSpider):            #这里不能写scrapy.Spider
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

    
============================================================================
#pipelines.py，用来处理spider yield的items
#打开对应的redis集合，如果username的长度大于7且没有保存过，则保存
'''
为了启用一个Item Pipeline组件，你必须将它的类添加到 ITEM_PIPELINES 配置，就像下面这个例子:
ITEM_PIPELINES = {
    'myproject.pipelines.PricePipeline': 300,
    'myproject.pipelines.JsonWriterPipeline': 800,
}
分配给每个类的整型值，确定了他们运行的顺序，item按数字从低到高的顺序，
，数字越小越优先，通过pipeline，通常将这些数字定义在0-1000范围内。
'''


import scrapy,logging,time,datetime
from redis import Redis

class HupuPipeline(object):
    def __init__(self):
        self.r=Redis(password='asd123')
        self.r1=self.r.smembers('hupuname')

    def process_item(self, items, spider):
        x=items['t']
        if len(x)>7 and x.encode() not in self.r1:
            
            self.r.sadd('hupuname',x)
            #logging.error('self.r.scard(hupuname)={}'.format(self.r.scard('hupuname')))
            
            with open('2.txt','a',encoding='utf8') as f:
                f.write(x+'\n')
                
            return items
    
