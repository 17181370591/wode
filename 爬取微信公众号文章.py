#注意爬取速度，据说是2s一个页面，有个账号由于没有设置延时被封号了
#公众号文章主页里，向下拖动会动态用json文件加载新数据，第一页似乎没用json，
#但也可以设置offset=0获取


import requests,re,json,time
from lxml import etree

#u是公众号文章主页面，用来获取一些参数
u=r'https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzI1ODEyODk4Mw==
&scene=124&devicetype=android-19&version=26060736&lang=zh_CN&nettype=WIFI&a8scene=3
&pass_ticket=8ABVy%2F7jXEsD6Ndrj4BHWu1o44vTki%2FUW%2BEprM5yaRlepATaKex6bs4R2r4x2J2Q&wx_header=1'

#u1是文章页面的json数据
u1=r'https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzI1ODEyODk4Mw==
&f=json&offset=10&count=10&is_ok=1&scene=124&uin=777&key=777
&pass_ticket=s9kH4nD42PVpqLTQkbBJSUxYZrgDGOd2sKWaR5%2BP3qjDtXN1KP242HaBwLZdMM0M
&wxtoken=&appmsg_token=961_xvETD32kjAwHctUFazFkDCGM-zycpQw5cKCLKw~~&x5=0&f=json'



#需要添加headers模拟微信环境才能打开页面，x-wechat-key几分钟刷新一次，暂时不知道怎么获取，
#x-wechat-uin不变，由微信号决定
#似乎用不同账号会遇到相同的x-wechat-key，以后研究

h={'x-wechat-uin': 'NDAxNjAwNjkzNQ%3D%3D', 
   'user-agent':'User-Agent: Mozilla/5.0 (Linux; Android 4.4.2; SM-G955F Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 MicroMessenger/6.6.7.1321(0x26060736) NetType/WIFI Language/zh_CN'}
h['x-wechat-key']='51877e3298b8f3f69c597319cc2abe6c550ca07fbfae09b9e367a91539c2dcec6f3c26bf8833f216cfcee7e0f8b0e4db133d05e9a1fef3de3ef679c7594a1e9dede20298b068f977859f02efbd414985'



se=requests.session()
se.headers.update(h)
r1=se.get(u)


#很容易验证失败， 失败的话返回文本长度为2204，所以设定失败的话退出程序
lr1=len(r1.text)
print(lr1)
if lr1<11111:
        quit()
 

#aa用来保存文章的链接   
aa=set()
j1=se.get(u1).json()
j2=json.loads(j1['general_msg_list'])['list']
for i in j2:
        j3=i['app_msg_ext_info']
        url=j3['content_url']
        aa.add(url)


#对集合进行常规操作，这个xpath会抓取到无用信息甚至js，不修改了
while aa:
        time.sleep(3)       
        b=aa.pop()
        te=se.get(b).text
        r=etree.HTML(te)
        s=r.xpath('string(//div[@id="page-content"])')
        print(re.sub(r'[\r\t\n]+','',s))
        
