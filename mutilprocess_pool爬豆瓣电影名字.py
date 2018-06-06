import requests,re,fake_useragent
from lxml import etree
import execjs
se=requests.session()
ua=fake_useragent.UserAgent()
u=r'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E5%BD%B1&start={}&genres={}'
def getip(i):
    p={'http':'http://{}'.format(i)}
    print(p)
    r=requests.get(u,proxies=p,timeout=5)
    if r.status_code =='200':
        print(etree.HTML(r.text).xpath('string(//h1[@id="ipd"])'))

h={'user-agent':ua.random}
ip='171.38.37.153:8123'
p={'http':'http://{}'.format(ip)}

def f(x,u=u):
    i=0
    u=u.format('{}',x)
    while True:
        #u='http://www.baidu.com'
        r=se.get(u.format(str(i)),headers=h,proxies=p,verify=True)
        for j in r.json()['data']:
            print(x,j['title'])
        #r=se.get(u,erify=True)
        i+=10
from multiprocessing import Pool

if __name__=='__main__':
    pool = Pool(4)
    us=['悬疑','犯罪','同性','音乐']
    resultList =pool.map(f, us)
    pool.close()
    pool.join()

j1=r'C:\Users\Administrator\Desktop\2.js'
'''
with open(j1,'r',encoding='utf-8-sig') as f:
    j1=f.read()
    ctx = execjs.compile(j1)
    print(ctx.call('p','abcd256fef51a340ce26b4bb8608505b'))
    

h={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
se=requests.session()
u=r'http://openlaw.cn/search/judgement/default?type=&typeValue=&courtId=\
&lawFirmId=&lawyerId=&docType=&causeId=&judgeDateYear=\
&lawSearch=&litigationType=&judgeId=&procedureType=\
&judgeResult=&courtLevel=&procedureType=&zone=\
&keyword=%E5%90%83%E9%A5%AD'
rr=se.get(u,headers=h)
se.cookies.update({'j_token':'93n_pe67fefb16d2dae91b0e993a07c707f1'})
se.cookies.update({'session':'YTJkODRmZjUtNGFjOC00YmYwLThlOTctNzI5Y2FlZTQ4NWRj'})
r1=se.get(u,headers=h).text
with open('1.txt','w') as f:
    f.write(r1)
r2=etree.HTML(r1)
r3=r2.xpath('//article')
print(len(r3))
for i in len(r3):
    s1=i.xpath('//h3').text
    print(s1)
''' 
