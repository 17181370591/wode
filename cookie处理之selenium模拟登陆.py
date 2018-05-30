from selenium import webdriver
import json

#可以正常登录，打开其他网页自动处理cookie
'''
预先保存登录好的cookie的方法是：
with open('2.json','w') as f:
    f.write(json.dumps(dr.get_cookies()))
'''

dr = webdriver.Firefox()
u1='https://tieba.baidu.com/'
u="http://www.baidu.com"

dr.get(u)
dr.delete_all_cookies()
      
#add_cookie里传入的键可以自己测试，新浪邮箱登录时domain是必须的（name和value所有地方都必须）
with open('2.json') as f:
    f=f.read()
    j=json.loads(f)
    for i in j:
        dr.add_cookie({'domain': i['domain'],
                       'name': i['name'],
                       'value': i['value'],
                       'path': '/',
                       'expiry': i['expiry']
                    })

dr.get(u)
dr.get(u1)


