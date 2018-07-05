#post_login访问'https://my.suning.com'时，抓包可以发现回访问两次（直接访问一次，重定向一次），
#由于第二次才会抓取数据，第一次访问后第二次访问会被过滤，所以抓取不到数据，设置dont_filter=True即可

#可以发现start_requests也能直接用FormRequest（post）请求
#重定向有可能会遇到类似问题，所以最好都加dont_filter=True？？
#登陆成功后，访问我的订单，我的设置都会自己附上cookies，所以不知道meta设置cookiejar有什么用


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
                            'username': '1719886****',
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
                       #meta={'cookiejar': response.meta['cookiejar']},
                       callback=self.pa,dont_filter=True)       #不设置dont_filter=True抓不到数据
    def pa(self, response):      
        with open('1.txt', 'w',encoding='utf8')as f:
            f.write(response.text)
