# -*- coding: utf-8 -*-
import os,math
import time
import numpy as np,random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image

cd=os.getcwd()
VERSION = "1.1.4"
step=1
path1=r'C:\Users\Administrator\Desktop\111'

def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/autojump.png')
    #os.system('adb pull /sdcard/autojump.png .')
    os.system('adb pull /sdcard/autojump.png {}'.format(cd))
    img1=Image.open('autojump.png')
    img1=img1.crop((0,300,720,1280))
    img1.save('autojump.png')
    #img1.convert('RGB').save(path1+r'\{}.jpg'.format(step))


def sq(a,b,c=2.1):
    d=math.sqrt(a*a+b*b)
    z=round(d*c)
    print(z)
    return z


def get_chess():        
    res=np.argwhere((img[:,:,0]<60)*(40<img[:,:,0])*
                    (img[:,:,1]<60)*(40<img[:,:,1])*
                    (img[:,:,2]<100)*(80<img[:,:,2]))

    #res是棋子所有点在img1里的坐标
    mini=res.argmin(axis=0)[1]         #棋子底部正中心的索引
    maxi=res.argmax(axis=0)[1]
    mx=max(min(600,res[mini][0]),min(600,res[maxi][0]))            #中点的横坐标
    mi=int(np.average(np.argwhere(res[:,0]==mx)))       #中点的index
    my=res[mi][1]               #中点的纵坐标
    return mx,my,res

def get_pic(img):
    img=img.astype(int)
    i00=img[0,0]
    i0=img[:,:,0]
    i1=i0.reshape(980,720,1)
    i2=np.concatenate((i1,i1,i1),axis=2)
    res=np.argwhere(1-((abs(img-i00)<22).all(axis=2)*(img<i00+1).all(axis=2)+
                       (abs(img-150)<20).all(axis=2)*(1-(img==i2).all(2))))
    #img.max(axis=2)-img.min(axis=2)>0不行为什么
    upp=res[0]
    
    '''
    re1=np.where(res[:,0]<upp[0]+80)
    pic_miny=res[re1][:,1].min()    
    leftp=res[np.argwhere(res[:,1]==pic_miny)[0]][0]
    '''
    temp=upp
    while True:
        try:
            newd=res[np.where(res[:,0]==temp[0]+2)][0]
            #print(temp,newd)
            if newd[1]<temp[1] and newd[1]>temp[1]-15:
                temp=newd
            else:
                break
        except Exception:
            break

    nx,ny=temp[0],upp[1]
    dr(res,nx,ny)
    return nx,ny,res
    

def dr(res,nx,ny):
    global step
    print(step,nx,ny)
    ii=np.zeros_like(img)
    ii[res[:,0],res[:,1]]=[255,255,255]
    dd=3
    ii[mx-dd:mx+dd,my-dd:my+dd]=[255,0,0]
    ii[nx-dd:nx+dd,ny-dd:ny+dd]=[255,0,0]
    pic=Image.fromarray(ii)
    #pic.save(path1+r'\{}_{}_{}.jpg'.format(step,a,b))
    pic.save('2.jpg')
        
def drr(res):
    ii=np.zeros_like(img)
    ii[res[:,0],res[:,1]]=[255,255,255]
    Image.fromarray(ii).show()
 
    
    
while True:
    time.sleep(random.random()+.5)
    pull_screenshot()
    img1=Image.open('autojump.png')
    img=np.array(img1)[:,:,:3]
    if (img[755,577]==[255,255,255]).all() and (img[755,163]==[255,255,255]).all():
        break
    mx,my,res1=get_chess()
    nx,ny,res2=get_pic(img)
    print('棋子的坐标是{},{}'.format(mx,my))
    print('目标的坐标是{},{}'.format(nx,ny))
    time.sleep(2)
    z=sq(mx-nx,my-ny)
    x1=random.randrange(200,500)
    x2=random.randrange(200,500)
    x3=x1+random.randrange(-100,100)
    x4=x2+random.randrange(-100,100)
    cmd = 'adb shell input swipe {} {} {} {} {}'.format(x1,x2,x3,x4,z)
    os.system(cmd)
    step+=1








'''
fig.canvas.mpl_connect('button_press_event', on_click)
ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)
plt.show()
'''
'''
查看屏屏幕的方法adb shell wm size

adb shell input swipe 100 100 200 200 300
从 100 100 经历300毫秒滑动到 200 200

adb shell input tap 500 1050点击500，1050，正好是重试按钮的位置
'''

