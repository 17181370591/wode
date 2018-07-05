#用已经登录成功的cookies伪装登录，d是cookies字典
#直接在start_requests的scrapy.Request里设置好cookies就可以登录了，
#不知道是虎扑检测不严厉还是怎么回事，在requests里cookies一定要在session访问一个网页后，
#使用session.cookies.update更新cookies才能使用。

#response.request.headers.getlist('Cookie')[0].decode()可以得到cookies的类似url链接的文本（str），
#reco接收这个文本，并进行修改，返回的cs1是长度为0的list，内容是修改后的cookies的类似url链接的文本(bytes)，
#可以直接传给response.request.headers.setlist，用来更新cookies
#然而不知道虎扑的检测机制，不知道这么做能不能有效的更改cookies，因为不用reco也会成功

import scrapy

def reco(Cookie):
        c=Cookie.split(';')
        dd={}
        for i in c:
            x=i.split('=',1)
            dd[x[0]]=x[1]
        #dd.update({'us':'你是二笔吗'})
        for i in dd:
            dd[i]='1'
        print(dd)
        cs=''
        for i in dd.keys():
            cs+=i.strip()+'='+dd[i].strip()+';'
        cs=cs[:-1].encode()
        cs1=[]
        cs1.append(cs)
        return cs1
    
class MySpider(scrapy.Spider):
    name = 'Hupu'
    start_urls = [r'https://bbs.hupu.com/topic-12',r'https://bbs.hupu.com/topic-13']
    d={'_fmdata':'kYqIQs9LTYz5oRjOMdPb5iB6bclI6hqFswD5tXPSkD%2FcaKyCqSGi5cytdTcXbHzuqikmcDIabpykxIC7e8anCwZ3DY1NSSBrF0jE1yBSfks%3D',
    'us':'9b1005328020120a3ee8a32ce9f717db590c7cf302f799bdcf9854a6985ccb916dfeac9c343894e00b5e7b01847f2fa228d42d409c2854944882bcfec3a5e1c4',
   'u':'35048460|6Zi/5Y2h6KW/MQ==|4015|a624d0ae11f14f7df55e50e48f082772|11f14f7df55e50e4|aHVwdV8yZjQxZjJiM2YwNTg1ZTQw',
   '_CLT':'00376064be821b71351c003dda774e37',
   'PHPSESSID':'1d5bb84a87b96c3bc5531567068e0fbf',
   '_HUPUSSOID':'d3e074f0-a69b-4268-9326-8ae765546e4c',
   '__guid':'13421668.1702922777230312000.1508844317035.6482',
   }
    
    def parse(self, response):
        print(len(response.text))   #response.body
        
        Cookie = response.request.headers.getlist('Cookie')[0].decode()
        response.request.headers.setlist('Cookie',reco(Cookie))  

        yield scrapy.Request(self.start_urls[1],callback=self.parse)


    def start_requests(self):
        # 带着cookie向网站服务器发请求，表明我们是一个已登录的用户
        yield scrapy.Request(self.start_urls[0],
                             callback=self.parse,
                             cookies=self.d)
