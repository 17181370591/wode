import scrapy


class MySpider(scrapy.Spider):
    name = 'Hupu'
    start_urls = ['http://httpbin.org/get',]
    cookie={'fuck':'uuu'}
    def parse(self, response):
        print('*'*33,response.url,response.body)

    

    def start_requests(self):
        # 带着cookie向网站服务器发请求，表明我们是一个已登录的用户
        yield scrapy.Request(self.start_urls[0],
                             callback=self.parse,
                             cookies=self.cookie)
