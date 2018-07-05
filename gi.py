from scrapy import Spider, Request, FormRequest


class GithubLoginSpider(Spider):
    name = "gi"
    # post登入的必须要的头字段
    post_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36",
    }
    #https://passport.suning.com/ids/login
    #https://order.suning.com/order/orderList.do

    def start_requests(self):
        return [FormRequest("https://passport.suning.com/ids/login",
                        #meta = {'cookiejar' : 1},
                        formdata = {
                            'username': '17198869121',
                            'password2': 'jXO72fnk1zvqRYY+MXDyYm0HnkwzwJJc9TqN/0VlI1TkcaWBy5WVaEQ8edxzfvOGPKx4YMhDBzJk5EVso4svmVkxAjxgKOkCMXW+AcR88NblIqoers47Tvbiq3e32iZGwkIZvOb3LC3MnOQt9avE7TfmjXU6poeifgQYYTC6ePA=',
                            'jsonViewType':'true','password':'',
                            'loginTheme':'b2c','service':'','sceneId':'logonImg',
                            'rememberMe':'true','client':'app',
                            },  
                        callback = self.post_login)]  #添加了meta

    #FormRequeset出问题了
    def post_login(self, response):
        print('登录'*8,response.text)
        return Request('https://my.suning.com',
                       callback=self.pa,dont_filter=True)
    def pa(self, response):      
        with open('1.txt', 'w',encoding='utf8')as f:
            f.write(response.text)
