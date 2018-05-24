import win32clipboard,win32con,win32api,win32gui,ctypes,time

#定位到600,600
c=(600,600)
ctypes.windll.user32.SetCursorPos(*c)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|\
                     win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
time.sleep(1)

#打开剪切板，不打开剪切板无法使用
win32clipboard.OpenClipboard()
#清空剪切板，不清空的话GetClipboardData会返回最新设置的内容，但粘贴不会
win32clipboard.EmptyClipboard()  
txt='erbda大家asd&*（{'
#设置剪切板内容，需要选择SetClipboardData，文本必须编码
win32clipboard.SetClipboardData(win32con.CF_TEXT,txt.encode('gb18030'))
#获取剪切板内容
data = win32clipboard.GetClipboardData(win32con.CF_TEXT)
print(data)
#关闭剪切板，不关闭的话粘贴会失败
win32clipboard.CloseClipboard()

#粘贴
win32api.keybd_event(17,0,0,0)
win32api.keybd_event(86,0,0,0)
win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0)
win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
time.sleep(1)
win32api.keybd_event(13,0,0,0)
win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
