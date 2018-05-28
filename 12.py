import requests,json

with open('2.json') as f:
    jj=f.read()
    #jj.replace("'",'"')
    j=json.loads(jj)

u='http://www.baidu.com'
u1='https://tieba.baidu.com/'
se=requests.session()
jar = requests.cookies.RequestsCookieJar()

for i in j:
    jar.set(i['name'],i['value'],domain=i['domain'], path='/')
'''
for i  in j:
    requests.utils.add_dict_to_cookiejar(se.cookies,i)
'''   
se.cookies.update(jar)
r=se.get(u)
with open('1.txt','w',encoding='utf8') as f:
    f.write(r.text)
#r=se.get(u1)
print('赤' in r.text)
