#js分析地址：https://zhuanlan.zhihu.com/p/32344678
'''
我们直接用浏览器访问，发现访问时带入了一个j_token的cookie请求，这是从哪来的，我们需要从哪找到呢？

后面破解我们能够知道，这其实是两步。第一步不带j_token请求，会跳转到js混淆代码，
计算获取j_token并写入cookie中去；第二步带j_token请求，请求到最终呈现。

f12的source里面可以创建snippet，然后粘贴js进去点右边三角形可以运行，
js代码不需要html，head，script等标签，python里的execjs也不要标签
'''


import requests,execjs,re,fake_useragent as fu
from lxml import etree

#将window.v转换成j_token，方法是从js解密出来的
def p(s):
    return s[2: 4]+'n'+s[0: 1]+'p'+s[4: 8]\
           +'e'+s[1: 2]+s[16:]+s[8: 16]

#从text打印案件标题
def get1(s):
    s=etree.HTML(s)
    s=s.xpath(r'//h3[@class="entry-title"]')
    for i in s:
        print(i.xpath('string(.)'))
    
ffu=fu.UserAgent()
se=requests.session()
#re1=re.compile(r'window.v="([_1-9A-Za-z]+)";',re.S)
#上面应该写0-9
re1=re.compile(r'window.v="(.*?)";',re.S)

u='''http://openlaw.cn/search/judgement/default?type=&typeValue=&courtId=&lawFirmId=&lawyerId=&docTy
pe=&causeId=&judgeDateYear=&lawSearch=&litigationType=&judgeId=&procedureType=&judgeResult=&courtLevel
=&procedureType=&zone=&keyword=%E5%90%83%E9%A5%AD&page={}'''

for i in range(1,5):
    print(u.format(i))
    r=se.get(u.format(i),headers={'user-agent':ffu.random})
    
    #找到真实页面的话，文本长度超过10000，这里应该用别的方法判断，懒得改了
    #进入真实页面获取信息。可以发现第一次进入js页面，之后每次都直接进入真实页面
    if len(r.text)>10000:
        print('*'*88)
        get1(r.text)
        continue
    
    #没找到真实页面，则调用f来算jtoken并进入真实页面
    res=re.search(re1,r.text)
    s=res.group(1)
    se.cookies.update({'j_token':p(s)})
    r=se.get(u.format(i),headers={'user-agent':ffu.random})
    get1(r.text)




