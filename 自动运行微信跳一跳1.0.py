#opencv里有更好的版本，这个没用了

#一般只能跑200分，原因基本确定是get_pic抓取不准
#思路是，截图到电脑，打开图片，棋子是紫色，较容易抓取，取一定范围内同一纵坐标上数量最多的点，取中值即可，
#然后将整个图大致分为阴影部分，背景部分和目标块部分，阴影部分随着背景又有变化，不好处理，背景部分取坐标0,0的点a，
#然后rgb值各-20得到b，a和b之间的都是背景；去掉这两部分，从上向下查询可得到目标块部分，
#目标块第一个点是上顶点，上顶点向左下走，走到横坐标变大时停止，此时的点是左顶点，
#分别取两个顶点在水平和垂直方向的交点，得到目标块的中点，但经常效果不好
'''

adb控制手机

查看屏幕大小  adb shell wm size

adb shell input swipe 100 100 200 200 300
从 100 100 经历300毫秒滑动到 200 200

adb shell input tap 500 1050        点击500，1050
'''


# -*- coding: utf-8 -*-
import os,math
import time
import numpy as np,random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image


VERSION = "1.1.4"
step=1
path1=r'C:\Users\Administrator\Desktop\111'


#操作1对手机截图，保存成sdcard/autojump.png
#操作2将sdcard/autojump.png保存到电脑桌面，和操作2_1效果一样，注意2_1有个小数点表示当前路径

def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/autojump.png')            #1
    #os.system('adb pull /sdcard/autojump.png .')                       #2_1
    os.system('adb pull /sdcard/autojump.png {}'.format(os.getcwd()))            #2
    img1=Image.open('autojump.png')
    img1=img1.crop((0,300,720,1280))
    img1.save('autojump.png')
    #img1.convert('RGB').save(path1+r'\{}.jpg'.format(step))


#a,b分别是棋子到目标的横纵坐标的差值，z是长度，c是常数，将距离转换成时间

def sq(a,b,c=2.1):
    d=math.sqrt(a*a+b*b)
    z=round(d*c)
    print(z)
    return z



#获取棋子的中点

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



#获取目标块的中点

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
    

    

#画黑白图，两个中点分别扩展3个像素方便观看

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
        
        
        
        
#将get_pic和get_chess返回的res表示成图像，调试用

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









