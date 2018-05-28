from selenium import webdriver
import json

dr = webdriver.Firefox()
u1='https://tieba.baidu.com/'
u="http://www.baidu.com"

dr.get(u)
dr.delete_all_cookies()
      
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


