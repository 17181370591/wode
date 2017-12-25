import requests,re,time,os,json
u0=r'https://wx.qq.com/'
u1=r'https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=853271642'
u2=r'https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&fun=new&lang=zh_CN&_='+str(int(time.time()))
u3=r'https://login.weixin.qq.com/qrcode/{}'
#u4=r'https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid={}&tip=0&r=850929860&_=1510977547593'
u4=r'https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?uuid={}&tip=0&_={}'
se=requests.Session()
se.headers['User-Agent']='Mozilla/5.0'     #修改ua的正确方式？
se.headers['ContentType']: r'application/json; charset=UTF-8'
uuid=re.compile(r'uuid = "(.*?)"').search(se.get(u2).text).group(1)
        #u2是个固定的地址，get u2得到uuid
with open('1.jpg','wb') as f:    
    f.write(se.get(u3.format(uuid)).content)     #将uuid写入u3（验证码地址），并保存成1.jpg
u4=u4.format(uuid,int(time.time()*100000))        #uuid写入u4  
#print(u3.format(uuid),chr(11)*33,u4)
os.startfile('1.jpg')                               #打开1.jpg     
time.sleep(6)                           #等待扫码确认登陆
#r4=se.get(u4.format(uuid,u4))
r4=se.get(u4)                       #得到（取得wuxin等参数的网址）所在的网址
u5=re.search(r'uri="(.*?)"',r4.text).group(1)+r'&fun=new'    #取出该网址，添加一个参数（不知道为什么要加，不加就访问不到）
r6=se.get(u5)                                   #访问多参数网址
t6=r6.text
skey=re.search(r'skey>(.*?)</skey',t6).group(1)
wxsid=re.search(r'wxsid>(.*?)</wxsid',t6).group(1)
wxuin=re.search(r'wxuin>(.*?)</wxuin',t6).group(1)
devideid='e000000000000000'
pass_ticket=re.search(r'pass_ticket>(.*?)</pass_ticket',t6).group(1)
BaseRequest={'Uin':wxuin,'Sid':wxsid,'Skey':skey,'DeviceID':devideid}   #提取参数，做成post u7的提交字典
#print(BaseRequest,'pass_ticket=',pass_ticket)
u7=r'https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxinit?pass_ticket={}&skey={}&r={}'
data={"BaseRequest":BaseRequest}                
data1=json.dumps(data)              #字典改成json格式，必须改
se.headers['ContentType']='application/json; charset=UTF-8'
r7=se.post(u7.format(pass_ticket,skey,int(time.time())),data=data1)              #访问初始化界面
##print(len(r7.text),'qsiti' in r7.text)                          #确认qsiti这个nickname是否存在
##with open('123.txt','w',encoding='utf-8') as f:
##    f.write(r7.content.decode('utf-8'))
r7j=json.loads(r7.content.decode('utf-8'))
print('r7j["User"]:',r7j["User"])
wo=r7j["User"]['UserName']
synckey=r7j['SyncKey']
synckeyu='%7C'.join((str(i['Key'])+'_'+str(i['Val']) for i in synckey['List']))
##my_f={}289/6259 6041 7640 6100
##for i in r7j["ContactList"]:
##    my_f[i["NickName"]]=i["UserName"]
def get_f():
    url_friend =r'https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?seq=0&skey={}&r={}'.format(skey, int(time.time()))
    r_friend=se.get(url_friend).content.decode('utf-8')
    r_j=json.loads(r_friend)
    my_f={}
    for i in r_j["MemberList"]:
        my_f[i["NickName"]]=i["UserName"]
    with open('123.txt','w',encoding='utf-8') as f:
        f.write(str(my_f))
    return my_f
                                #ToUserName必须填写nickname
def sendMsg(MyUserName=wo, ToUserName='岛学家22016', msg='现在时间{}'.format(time.strftime('%Y-%m-%d %H:%M:%S'))):
    usend_message = r'https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxsendmsg?lang=zh_CN&fun=new&pass_ticket={}'.format(pass_ticket)
    #print('usend_message =',usend_message)
    d_msg={"Type": 1, "Content": msg, "FromUserName": MyUserName, "ToUserName": my_f[ToUserName]}
    params = {"BaseRequest": BaseRequest}
    params['Msg']=d_msg
    json_obj = json.dumps(params,ensure_ascii=False).encode('utf-8')
    #print('json_obj:',json_obj)
    req = se.post(usend_message, data=json_obj)
    print(req.text)
my_f=get_f()
my_f1=dict(zip(my_f.values(),my_f.keys())) 
def kaiqitz():          #未完成开通消息通知
    u=r'https://webpush.weixin.qq.com/cgi-bin/mmwebwx-bin/synccheck?skey={}&sid={}&uid={}&deviceid={}&synckey={}'
    uu=u.format(skey,wxsid,wxuin,devideid,synckeyu)
    print(uu)
    return se.get(uu)
def xinxx():                #查询新消息
    u=r'https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxsync?sid={}&skey={}&pass_ticket={}'.format(wxsid,skey,pass_ticket)
    data={'Code': 3, 'FromUserName':  wo,'ToUserName': my_f['岛学家22016'],'BaseRequest':BaseRequest}
    data={'BaseRequest':BaseRequest,'SyncKey':r7j['SyncKey']}
    xin1=se.post(u,data=json.dumps(data))
    xinj=json.loads(xin1.content.decode('utf-8'))
    print(xinj['BaseResponse'])
    for i in xinj['AddMsgList']:
        if  i['Content']:
            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(i['CreateTime'])),my_f1[i['FromUserName']],i['Content'])
    return xin1
##while True:
##    sendMsg(ToUserName='京东支付')
##    time.sleep(600)
