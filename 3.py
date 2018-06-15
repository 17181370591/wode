#据说密码使用了rsa加密，但不会破解

# -*- coding:utf-8 -*-
import re,execjs,os
import requests,time
import fake_useragent as fk
from lxml import etree

ua=fk.UserAgent()
se = requests.session()   
se.headers.update({'user-agent':ua.random})

u1=r'https://passport.jd.com/new/login.aspx'            #登录页面

r1=etree.HTML(se.get(u1).text)          #打开登录页面获取参数

uuid=r1.xpath('//input[@id="uuid"]')[0].attrib['value']
eid=r1.xpath('//input[@id="eid"]')[0].attrib['value']
fp=r1.xpath('//input[@id="sessionId"]')[0].attrib['value']
pubKey=r1.xpath('//input[@id="pubKey"]')[0].attrib['value']
sa_token=r1.xpath('//input[@id="sa_token"]')[0].attrib['value']

#登录部分开始
#判断有没有验证码，如果u00返回true就要验证码
u00=r'https://passport.jd.com/uc/showAuthCode'
z=se.get(u00)
cc=''
if 'rue' in z.text:
    #u0是验证码图片的地址，下载到本地后打开手动填写，要注意请求头要设置referer，否则会直接跳转京东首页
    u00=r'https://authcode.jd.com/verify/image?a=1&acid={}&uid={}&yys={}'
    u0=u00.format(uuid,uuid,str(int(time.time()*1000)))
    h=se.headers
    h['referer']=u1
    z=se.get(u0,headers=h)
    with open('1.jpg','wb') as f:
        f.write(z.content)
    os.system('1.jpg')
    cc=input('请输入验证码:')
    
pw='''OYu8r2AQTs9zo7Zm+7xs3JM96rdA7iYN+btGefhPS2Z3al5dUyQ5zHRtn/yoh5iNpQoqZRcKs84wxJo+Iy6dgaTw0PhLB3HMw0bdUdgfTBl+NCj4KyG48j+HX+KjWU1wNFttQD+7bupaCouVsu5ek8ubb32Ze0+OOJwxZyj6Dyk='''
d={'eid':eid,   'fp':fp,'_t':'_t','authcode':cc,'uuid':uuid,'loginType':'c','loginname':'13395747825',
   'nloginpwd':pw,'pubKey':pubKey,'sa_token':sa_token}
print('post提交的数据是：',d)

u2=r'https://passport.jd.com/uc/loginService?uuid={}&&r=0.3738090767112452&version=2015'.format(uuid)
r2=se.post(u2,data=d).text
print('登录结果是：',r2)
if 'emptyAuthcode' in r2:
    quit()
#登录部分结束，如果登录失败，退出程序




#ou1是订单的html源码页面，html里有商品的数量，收货人等信息；页面的js里有订单号等信息；
#商品是由json获得，获取地址是ou2，post的data就在ou1的js里
#注意这里的订单都是2016年的！！！获取近期订单要去掉对应的参数

ou1=r'https://order.jd.com/center/list.action?search=0&d=2016&s=4096&page={}'
def get_p(page):                    #获取ou1的参数，返回字典
    oh=se.headers.copy()
    or1=se.get(ou1.format(page))
    ot1=or1.text
    with open('1.txt','w',encoding='utf-8') as f:
        f.write(ot1)
    orderWareIds=re.search(re.compile(r"orderWareIds']='([0-9,]+)';"),ot1).group(1)
    orderWareTypes=re.search(re.compile(r"orderWareTypes']='([0-9,]+)';"),ot1).group(1)
    orderIds=re.search(re.compile(r"orderIds']='([0-9,]+)';"),ot1).group(1)
    orderTypes=re.search(re.compile(r"orderTypes']='([0-9,]+)';"),ot1).group(1)
    orderSiteIds=re.search(re.compile(r"orderSiteIds']='([0-9,]+)';"),ot1).group(1)
    data={'orderWareIds':orderWareIds,'orderWareTypes':orderWareTypes,
          'orderIds':orderIds,'orderTypes':orderTypes,'orderSiteIds':orderSiteIds}
    return data

#ou2是商品信息的获取页面
ou2=r'https://order.jd.com/lazy/getOrderProductInfo.action'
def get_order(ou2,page,data):
    oh2=se.headers.copy()
    oh2.update({'Referer':ou1.format(page)})
    or2=se.post(ou2,headers=oh2,data=data)
    ot2=or2.json()
    print('当前第{}也'.format(page))
    for i in ot2:
        print(i['name'])            #打印商品名称

#从第一页开始打印商品信息，打印到最后一页
page=1 
while True:
    try:
        data=get_p(page)
        get_order(ou2,page,data)
        page+=1
    except AttributeError as e:
        print(e)
        break

        
#下单。京东下单的一种流程是：先加入购物车，将被购买的商品勾选，然后post数据到u_buy购买，
#数据submitOrderParam.trackId不知道怎么获得，复制了一个，但是应该是md5加密编码，
#riskControl可以从u_bus获取，u_bus是订单确认前最后的页面，也是在购物车点提交后的页面
def buy():
    u_bus=r'https://cart.jd.com/cart.action?r=0.8322363310165506'
    def get_bus(u_bus):
        r=se.get(u_bus)
    u_b=r'https://trade.jd.com/shopping/order/getOrderInfo.action?rid=1529072906888'
    r_b=se.get(u_b)
    re_b=re.compile(r'riskControl" value="(.*?)"',re.S)
    riskControl=re.search(re_b,r_b.text).group(1)
    u_buy=r'https://trade.jd.com/shopping/order/submitOrder.action'
    bd={'overseaPurchaseCookies':'','vendorRemarks':[],'submitOrderParam.sopNotPutInvoice':'false',
        'submitOrderParam.trackID':'TestTrackId','submitOrderParam.ignorePriceChange':0,
        'submitOrderParam.btSupport':0,'submitOrderParam.jxj':1,
        'submitOrderParam.trackId':'c0cba34b9e0a42c1d15fd37903d1ca98','riskControl':riskControl}
    r_buy=se.post(u_buy,data=bd)
    pritn(len(r_buy.text)
