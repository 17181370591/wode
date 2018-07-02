import scrapy
from ..items import Test1Item

class GanJiSpider(scrapy.Spider):
    name='zufang'
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