import win32api,win32gui,win32con,ctypes,time,win32clipboard


#点击左键，先down在up，x，y分别表示相当当前鼠标位置的偏移量（不知道怎么取的）
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


#移动鼠标到（x,y）
ctypes.windll.user32.SetCursorPos(x,y)


#获取鼠标当前位置，返回横纵坐标的tuple
win32gui.GetCursorPos()


#获取屏幕大小（分辨率）
win32api.GetSystemMetrics(0)    #宽
win32api.GetSystemMetrics(1)    #高


#用spy++查看窗口的类名（a）或者标题名（b），可用只找一个。另一个填0或者None
a=win32gui.FindWindow(a,b)


#查看a句柄对应窗口的左上右下的坐标
left, top, right, bottom=win32gui.GetWindowRect(a)


# 获取某个句柄的类名和标题
title = win32gui.GetWindowText(a)
clsname = win32gui.GetClassName(a)


#关闭某窗口,a,b是win32gui.FindWindow的参数
win32gui.PostMessage(win32gui.FindWindow(a, b), win32con.WM_CLOSE, 0, 0)


#激活窗口，a是句柄
win32gui.SetForegroundWindow(a)


#返回当前激活窗口的句柄
win32gui.GetForegroundWindow()


#a是句柄，最大化窗口，普通显示
win32gui.ShowWindow(a,win32con.SW_MAXIMIZE)
win32gui.ShowWindow(2754548,win32con.SW_SHOWNORMAL)

hex(x)      #求x（10进制）的16进制数字


a=win32gui.FindWindow(None,'Python 3.6.3 Shell')
print(a)
l = []
#获取a的所有子窗口的句柄，保存到l里
win32gui.EnumChildWindows(a, lambda hwnd, param: param.append(hwnd),  l)


#找子窗口，先用spy++分析窗口层次和获取窗口的类名或者标题
a=win32gui.FindWindow('XLMAIN',None)        #用FW和类名找到最外层窗口，a是句柄
b=win32gui.FindWindowEx(a,None, None,'EtEditBarWidget')     #用FWE在a里找到第一层标题是'EtEditBarWidget'的子窗口，b是句柄
c=win32gui.FindWindowEx(b,None, None,'EtFmlEditBar')        #同上，找到了excel的编辑框句柄
#发送消息，SendMengage可以直接传入字符串等，但是对编辑框使用失败了，对txt文件成功，参数一是编辑框/txt光标所在窗口的句柄
a=int('004E0518',16)
win32api.SendMessage(a, win32con.WM_SETTEXT,0,'helasd大家\a\3水瀬祈りあｓだｓ」ｓ\s\t\n\w%20')


a='000503AE'
a=int(a,16)
#BOOL SetWindowPos（HWN hWnd，HWND hWndlnsertAfter,int X，int Y,int cx，int cy,UNIT．Flags）
#X和Y表示要将窗口移动到额位置的左上角的坐标，cx和cy表示窗口移动后的大小
win32gui.SetWindowPos(a,1,0,0,300,300,0)




b=(120,120)
ctypes.windll.user32.SetCursorPos(*b)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|\
                     win32con.MOUSEEVENTF_LEFTUP,0,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|\
                     win32con.MOUSEEVENTF_LEFTUP,0,0,0)
time.sleep(2)
b=(130,170)
ctypes.windll.user32.SetCursorPos(*b)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|\
                     win32con.MOUSEEVENTF_LEFTUP,0,0,0)

a=(68,65,74,73,65,72,65,79,32,13)
for i in a:
    print(i)
    time.sleep(.1)
    win32api.keybd_event(i,0,0,0)
    win32api.keybd_event(i,0,win32con.KEYEVENTF_KEYUP,0)

win32api.keybd_event(18,0,0,0)
win32api.keybd_event(115,0,0,0)
win32api.keybd_event(115,0,win32con.KEYEVENTF_KEYUP,0)
win32api.keybd_event(18,0,win32con.KEYEVENTF_KEYUP,0)
time.sleep(.5)
win32api.keybd_event(13,0,0,0)
win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)




