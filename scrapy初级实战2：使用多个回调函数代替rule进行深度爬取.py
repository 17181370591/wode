#hupu.py，爬虫spider文件
#学到两个东西，一个是不断地用回调函数进行深度爬取，一个是可以完全不使用return，只用yield

import scrapy

class MySpider(scrapy.Spider):          
    name = 'Hupu'
    u=r'https://bbs.hupu.com{}'
    u1=r'https://bbs.hupu.com/topic'
    i=0
    
    def start_requests(self):
        yield scrapy.Request('https://bbs.hupu.com/topic',callback=self.f1)
    
    def f1(self, response):

        x=response.xpath('//a[@class="truetit"]/@href').extract()
        for i in x:
            print(self.u.format(i))
            yield scrapy.Request(self.u.format(i),callback=self.f2)

    def f2(self,response):
        self.i+=1
        print('f2'*8,response.url,self.i)
        x=response.xpath('string(//div[@class="quote-content"])').extract()[0]
        y=x.strip()[:55]
        
        print('y'*44,y)
        
        
    

    
