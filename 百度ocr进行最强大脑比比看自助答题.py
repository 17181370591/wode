#获取坐标，截图，根据某个点的颜色判断现在在答题界面还是休息界面，在休息界面则点击继续挑战，
#根据四个答案的框边缘的颜色判断当前是否已经提交答案并等待对方回答，等待中则continue，
#否则截图到内存（注意代码，重要!!）百度orc识别，百度搜索问题，在html里找最多的答案项目，根据索引判断答案的位置并点击
#缺点是类似于不属于四大发明的选项是？这样的题必定答错
#以防万一参数后四位加了****


from PIL import ImageGrab,Image
import  base64,requests,fake_useragent as fu,json,time,sys
from urllib import parse
from io import BytesIO
import win32api,win32gui,win32con,ctypes,time,win32clipboard




#先找到夜神模拟器答题的窗口句柄，然后获取窗口位置，left和top分别是偏移坐标
wind=win32gui.FindWindow(0,'夜神模拟器')
left, top, right, bottom=win32gui.GetWindowRect(wind)
print('left,top=',left,top)




#各种参数，其实不需要，因为百度不封爬虫
ua=fu.UserAgent()
ak='6rBvDRG1V5qIVMVw6Q9U****'
sk='dNmjjhj0s8KrBDHb9GGbFgGimdkG****'
se=requests.session()
h={'Content-Type':'application/json;charset=UTF-8'}
se.headers.update(h)


#lis是四个选项在剪切后生成的图片上的相对左上角的坐标（但不是选项左上角的坐标）
#clis是四个选项在屏幕里的坐标（但不是选项左上角的坐标）
lis,clis=[],[]
for i in range(4):
    lis.append((100,200+80*i))         
    clis.append((200+left,450+top+80*i))


def get_at(ak,sk):      #获取百度access_token并返回
    host = 'https://aip.baidubce.com/oauth/2.0/token'
    d={'client_id':ak,'grant_type':'client_credentials','client_secret':sk}
    r=se.post(host,data=d)
    at=r.json()['access_token']
    return at
#下面是已经获取好的
at='24.828170f05c6638c22ca88fe37cdd69b2.2592000.1531749753.282335-1140****'


#通过百度orc将图片转化为文字，返回json，参数z是剪切的图片在内存里的 二进制数据，
#百度ocr要求将图片的二进制数据进行base64编码并url编码后上传，
#pic2word返回的q和ans分别是问题和答案，
#两个￥￥之间的操作是因为百度可能将问题识别成两个部分（可能更多？），这样会导致选项位置错误，
#所以将后四项以前的项合并当做问题q，后四项为答案ans

def pic2word(z):          
    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=' + at
    img = base64.b64encode(z)
    r1=se.post(url,data=parse.urlencode({"image": img})).json()
    r=r1['words_result']
    le=len(r)                                       #￥￥
    words=[i['words'] for i in r]
    q=''.join(words[:le-4])
    ans=words[le-4:]                                   #￥￥
    print('='*22,'\n',q)
    print(ans)     
    return q,ans



#去百度搜索word里的问题q，p是ans在搜索结果中每个答案的出现次数，回p.index(max(p)) or 0是答案的索引，
#返防止报错加了if p，这样没有ans会返回None，加了or 0，没有答案就选第一项，返回p和r1为了方便调试

def gotobaidu(q,ans):           
    u1=r'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd={}'.format(parse.quote(q))
    r1=se.get(u1)
    t1=r1.text
    p=[]
    for i in ans:
        p.append(t1.count(i))
    if p:
        return p.index(max(p)) or 0,p,r1


#pica是需要剪切的图片在屏幕中的位置
pica=(0+left,250+top,550+left,top+750)

#传入pica，截图，返回图片在内存里的二进制数据
def get_pic(pica):
    z=ImageGrab.grab(pica)          #ImageGrab.grab（pica）截取pica位置的图片，返回PIL.Image对象
    print('pica=',pica)
    print('lis=',lis)
    a1=z.getpixel((200,330))
    if a1[0]>200 and sum(a1)<400:           #图片坐标（200，330）满足一定条件说明处于休息状态，点击继续挑战答题
        ctypes.windll.user32.SetCursorPos(400+left,top+570)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
        return
    for i in lis:
        if z.getpixel(i)!=(255,255,255):        #四个选项有一个颜色不是纯白说明已经选择，等待对方操作
            return        
    zz=BytesIO()                        #这一句相当于zz=open('**.jpg','wb')
    z.save(zz,'jpeg')                   #这一句相当于z.save(zz)
    return zz.getvalue()                #相当于zz.read()(?)，注意用了getvalue方法


#无限循环答题。
def main():    
    while True:
        z=get_pic(pica)
        if z:                               #只有get_pic里确认处于自己可答题状态才会返回数据，否则不会进入try
            try:
                q,ans=pic2word(z)
                a,b,r=gotobaidu(q,ans)
                print(b,'答案是第{}项'.format(1+a))
                ctypes.windll.user32.SetCursorPos(*clis[a])         #根据索引a得出答案在屏幕上的坐标
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
            except Exception as e:
                print(sys.exc_info()[2].tb_lineno,e)            #返回错误信息和行号
        time.sleep(1)


main()

============================================================================================

显示Python异常抛出所在行

try:  
    code;  
except Exception as e:  
    exc_type, exc_obj, exc_tb = sys.exc_info();  
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]  
    print(exc_type, fname, exc_tb.tb_lineno)
