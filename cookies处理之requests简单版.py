'''
用tomcat测试发现，只要cookies里JSESSIONID一样，就会被服务器认为是同一个session。
（session的地址一样，且对一个session设置attri，另一个id一样的session能访问该值。

保存好的cookie有两种类型，
第一种是列表，如
[{'name':'a','value':'aaaa','path':'\','domain':'****','expiry':'***'},
  {'name':'b','value':'bbb','path':'\','domain':'****','expiry':'***'},
   *******************],
第二种是字典，如
{'a':'aaaa','b':'bbb',***************},
这两种可以互相转换
'''   

import requests,json

with open('2.json') as f:
    jj=f.read()
    j=json.loads(jj)
se=requests.session()
u='http://mail.sina.com.cn/'

d={}
for i in j:
    d[i['name']]=i['value']
    
#下面两行合并写成r=se.get(u,cookies=d)会失败！！
se.cookies.update(d)    
r=se.get(u)

print('17181' in r.content.decode())
