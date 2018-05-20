#/usr/bin/env python
#coding=utf8
 


import requests,re,hashlib,urllib
u=r'http://fanyi.baidu.com/'
se=requests.session()
r=se.get(u)
re1=re.compile(r"window\['common.*?token: '(.*?)'",re.S)
res=re1.search(r.content.decode('unicode_escape'))
token=res.group(1)

u='https://fanyi-api.baidu.com/api/trans/vip/translate'
u1=r'http://fanyi.baidu.com/v2transapi'
z=input()
print(z)
data={'from':'en','to':'zh','q':z,'transtype':'translang'\
      ,'simple_means_flag':3,'token':token,'salt':'1435660288',\
      'appid':'20151113000005349'}
secretKey = 'osubCEzlGjzvw8qdQc41' 
sign =data['appid'] + data['q'] + data['salt'] + secretKey  
data['sign'] = hashlib.md5(sign.encode(encoding='gb2312')).hexdigest()
        
print(data)
 
h = se.post(u,data=data)
r = h.content.decode('unicode_escape')
print(r)


