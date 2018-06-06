import requests,fake_useragent as fu,time,re,json
from lxml import etree
def checkip(i):
    p={'http':'http://{}:{}'.format(i[0],i[1]),\
       'https':'https://{}:{}'.format(i[0],i[1])}
    print(p)
    try:
        r=requests.get('https://httpbin.org/get',\
                       verify=True,proxies=p,timeout=5)
        if r.status_code==200:
            print(r.text)
        else:
            print('ip有问题',r.status_code)
    except Exception as e:
        print(e)

#每次get/post都要加headers，不然该次会被墙
ua=fu.UserAgent()
h=ua.random
se=requests.session()
print(h)
nn=r'http://www.xicidaili.com/nn'
r=se.get(nn,headers={'user-agent':h}).text
re1=re.compile(r'<td>(\d+.\d+.\d+.\d+)</td>[\s\t\n]+<td>(\d+)</td>',re.S)
res=re.findall(re1,r)
for i in res:
    checkip(i)
