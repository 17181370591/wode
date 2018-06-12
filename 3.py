#coding=utf8
import requests
import itchat as wx


key = '7593ddd9947346e5ba8ff8832264ba50'
def g(msg,key=key):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data={         
	"key":key,        
	"info":msg,
        "userid":"Hello"
        }
    r=requests.post(apiUrl,data=data).json()
    
    return r.get('text')

@wx.msg_register(wx.content.TEXT)
def tuling_reply(msg):
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    defaultReply = 'I received: '+msg['Text']
    # 如果图灵Key出现问题，那么reply将会是None
    reply = g(msg['Text'])
    # a or b的意思是，如果a有内容，那么返回a，否则返回b
    # 有内容一般就是指非空或者非None，你可以用`if a: print('True')`来测试
    return reply or defaultReply


# 为了让实验过程更加方便（修改程序不用多次扫码），我们使用热启动
wx.auto_login(hotReload=True)
wx.run()
