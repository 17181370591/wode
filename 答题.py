from PIL import ImageGrab,Image
import  base64,requests,fake_useragent as fu,json,time,sys
from urllib import parse
from io import BytesIO
import win32api,win32gui,win32con,ctypes,time,win32clipboard

wind=win32gui.FindWindow(0,'夜神模拟器')
left, top, right, bottom=win32gui.GetWindowRect(wind)
print('left,top=',left,top)


ua=fu.UserAgent()
ak='6rBvDRG1V5qIVMVw6Q9UAzNR'
sk='dNmjjhj0s8KrBDHb9GGbFgGimdkGD5et'
se=requests.session()
h={'Content-Type':'application/json;charset=UTF-8'}
se.headers.update(h)
lis,clis=[],[]
for i in range(4):
    lis.append((100,200+80*i))         #剪切后图片的相对位置
    clis.append((200+left,450+top+80*i))
#lis=((100,200),(100,280),(100,360),(100,440))       
#clis=((200,450),(200,530),(200,610),(200,690))


def get_at(ak,sk):      #获取百度access_token并返回
    host = 'https://aip.baidubce.com/oauth/2.0/token'
    d={'client_id':ak,'grant_type':'client_credentials','client_secret':sk}
    r=se.post(host,data=d)
    at=r.json()['access_token']
    return at
#下面是已经获取好的
at='24.828170f05c6638c22ca88fe37cdd69b2.2592000.1531749753.282335-11408274'


def pic2word(z):     #通过百度orc将图片转化为文字，返回json      
    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=' + at
    img = base64.b64encode(z)
    r1=se.post(url,data=parse.urlencode({"image": img})).json()
    r=r1['words_result']
    le=len(r)
    words=[i['words'] for i in r]
    q=''.join(words[:le-4])
    ans=words[le-4:]
    print('='*22,'\n',q)
    print(ans)     
    return q,ans

def gotobaidu(q,ans):           #去百度搜索word里的问题q
    u1=r'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd={}'.format(parse.quote(q))
    r1=se.get(u1)
    t1=r1.text
    p=[]
    for i in ans:
        p.append(t1.count(i))
    if p:
        return p.index(max(p)) or 0,p,r1


pica=(0+left,250+top,550+left,top+750)

def get_pic(pica):
    z=ImageGrab.grab(pica)
    #z.show()
    print('pica=',pica)
    print('lis=',lis)
    a1=z.getpixel((200,330))
    if a1[0]>200 and sum(a1)<400:
        ctypes.windll.user32.SetCursorPos(400+left,top+570)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
        return
    for i in lis:
        if z.getpixel(i)!=(255,255,255):
            return
        
    zz=BytesIO()
    z.save(zz,'jpeg')
    return zz.getvalue()       


def main():    
    while True:
        z=get_pic(pica)
        if z:
            try:
                q,ans=pic2word(z)
                a,b,r=gotobaidu(q,ans)
                print(b,'答案是：',1+a)
                ctypes.windll.user32.SetCursorPos(*clis[a])
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
            except Exception as e:
                print(sys.exc_info()[2].tb_lineno,e)
        time.sleep(4)


main()


