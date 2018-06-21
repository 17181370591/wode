#方法1：必须先用session访问主页u1获取headers和cookies，然后访问u进行翻译，
#referer，ua（注意请求头里是user-agent）都必须设置，post提交的关键参数是i，salt和sign，i和salt很明显，
#sign的获取方式是：分析发现sign每次都会变，两次post间找不到相应的数据，说明没有从服务端获取，
#，是从本地获取的，然后用addrule禁用js（将所有js替换成不存在的文件即可），发现无法翻译，
#然后一一测试发现是fanyi.min.js获取的，搜索sign发现有删除，根据vesion=2.1发现是最后一个，
#打印r,n,S,D,u,o等参数即可得出sign的生成函数是下面的getsign。

#方法2：将u的“_o”去掉，原因估计是不去掉的页面做了反爬虫处理，去掉的没有

import execjs,os,time,hashlib,requests,fake_useragent as fu,base64,re

   
t=str(round(time.time()*1000)) 
n='hello'
S='fanyideskweb'
D='ebSeFb%=XZ%T[KZ)c(sy!'
u1=r'http://fanyi.youdao.com/?keyfrom=fanyi.logo'
ua=fu.UserAgent()
se=requests.session()

se.headers.update({'User-Agent':ua.random})     #必须
se.get(u1)                                      #必须
se.headers.update({'Referer':u1})                #必须


def getsign(r=t,n=n,S=S,D=D):
    md5=hashlib.md5((S + n + r + D).encode())
    a=md5.hexdigest()
    print(a)
    return a


u=r'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

sign=getsign()
d={'i':n,'from':'AUTO','to':'AUTO','smartresult':'dict','client':S,
   'doctype':'json','salt':t,'version':'2.1', 'sign':sign,'typoResult':'false',
   'keyfrom':'fanyi.web','action':'FY_BY_REALTIME'}

r=se.post(u,data=d)
print(r.text)
