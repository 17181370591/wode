import requests,json

#登录首页成功，但切换页面现实未登录，估计登录失败。
#推测原因是requests的cookie对象默认过期时间是expires，
#而百度是expiry，但不知道怎么修改

#事先将登陆好的cookie保存到2.json
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
