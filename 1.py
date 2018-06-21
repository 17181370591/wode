import execjs,os,time,hashlib,requests,fake_useragent as fu,base64,re

   
t=str(round(time.time()*1000)) 
n='hello'
S='fanyideskweb'
D='ebSeFb%=XZ%T[KZ)c(sy!'
u1=r'http://fanyi.youdao.com/?keyfrom=fanyi.logo'
ua=fu.UserAgent()
se=requests.session()

se.headers.update({'User-Agent':ua.random})     #必须
se.get(u1)
def getsign(r=t,n=n,S=S,D=D):
    md5=hashlib.md5((S + n + r + D).encode())
    a=md5.hexdigest()
    print(a)
    return a
se.headers.update({'Referer':u1})


u=r'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

sign=getsign()
d={'i':n,'from':'AUTO','to':'AUTO',
   'smartresult':'dict','client':S,
   'doctype':'json','salt':t,'version':'2.1',
   'sign':sign,'typoResult':'false',
   'keyfrom':'fanyi.web','action':'FY_BY_REALTIME'}

r=se.post(u,data=d)
print(r.text)
