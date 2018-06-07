import requests,execjs,re,fake_useragent as fu
from lxml import etree

def p(s):
    return s[2: 4]+'n'+s[0: 1]+'p'+s[4: 8]\
           +'e'+s[1: 2]+s[16:]+s[8: 16]

def get1(s):
    s=etree.HTML(s)
    s=s.xpath(r'//h3[@class="entry-title"]')
    for i in s:
        print(i.xpath('string(.)'))
    
ffu=fu.UserAgent()
se=requests.session()
re1=re.compile(r'window.v="([_1-9A-Za-z]+)";',re.S)
re1=re.compile(r'window.v="(.*?)";',re.S)
u='http://openlaw.cn/search/judgement/default?typ\
e=&typeValue=&courtId=&lawFirmId=&lawyerId=&docTy\
pe=&causeId=&judgeDateYear=&lawSearch=&litigationTy\
pe=&judgeId=&procedureType=&judgeResult=&courtLevel\
=&procedureType=&zone=&keyword=%E5%90%83%E9%A5%AD&page={}'
for i in range(1,5):
    print(u.format(i))
    r=se.get(u.format(i),headers={'user-agent':ffu.random})
    if len(r.text)>10000:
        print('*'*88)
        get1(r.text)
        continue
    res=re.search(re1,r.text)
    s=res.group(1)
    se.cookies.update({'j_token':p(s)})
    r=se.get(u.format(i),headers={'user-agent':ffu.random})
    get1(r.text)




