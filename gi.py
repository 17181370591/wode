import scrapy
class MySpider(scrapy.Spider):
    name = 'Hupu'
    start_urls = [r'https://bbs.hupu.com/topic-12']

    def parse(self, response):
        le=len(response.text)
        print(le)
        print(response.text[:1111])
        


