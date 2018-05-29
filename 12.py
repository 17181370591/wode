
import requests,json

with open('2.json') as f:
    jj=f.read()
    j=json.loads(jj)
se=requests.session()
u='http://mail.sina.com.cn/'

d={}
for i in j:
    d[i['name']]=i['value']

r=se.get(u,cookies=d)

print('17181' in r.content.decode())
