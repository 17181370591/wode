#可以对excel单元格进行输入，是模块PyUserInput的一部分
import win32clipboard,win32con,win32api,win32gui,ctypes,time
import pymouse,pykeyboard,os,sys

#定位到600,600
c=(600,600)
ctypes.windll.user32.SetCursorPos(*c)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|\
                     win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
time.sleep(1)

k = pykeyboard.PyKeyboard()

#直接传入字符串
k.type_string('Hello, World!')


k.press_key('A')    #模拟键盘按A键 
k.release_key('A')  #模拟键盘松开A键

k.press_key(k.space_key) #模拟键盘按 空格键 
k.release_key(k.space_key) #模拟键盘松开空格键 
time.sleep(1)

#tap_key是点击的意思，相当于press+release，但是除了键还必须要一个参数，
#可以是n，表示次数，可以是interval，表示间隔时间
k.tap_key('l',n=5,interval=.3)   
k.tap_key(k.backspace_key,interval=1.3)

#k.space_key表示空格键，其键码是32，所以可以直接输入32
k.press_key(k.space_key)  
k.release_key(32) 

