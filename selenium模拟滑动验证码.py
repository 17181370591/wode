#滑动验证码地址：http://jiyan.c2567.com/index.php/login/index


from selenium import webdriver
import json,time,numpy as np,os,pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image


dr = webdriver.Firefox()
u='http://jiyan.c2567.com/index.php/login/index'
dr.get(u)
cd=os.getcwd()


#函数用来画图，参数x是图的xpath，s1是图将被保存的名字
#p1是验证码图，图出现后截图保存成1.jpg，将此图的rgb数组保存到d1,并返回
def getd(x,s1):
    p1=WebDriverWait(dr,10).until(EC.presence_of_element_located((By.XPATH,x)))    
    
    #下面这个方法可以保存单个元素的截图
    p1.screenshot(s1)
    time.sleep(3)
    p1=Image.open(cd+'\\'+s1)   


#保存两张验证码图，第二张图要点击“拖动按钮”后才会出现
def drawpic():
    getd('//div[@id="dx_captcha_basic_bg_1"]/canvas','1.jpg')
    s=dr.find_element_by_id('dx_captcha_basic_slider_1')
    s.click()
    time.sleep(1)
    getd('//div[@id="dx_captcha_basic_bg_1"]/canvas','2.jpg')

    

#模拟鼠标拖动，一次拖动到终点会被ban，竖直方向始终没有移动也会ban，所以分5段拖动，并加上竖直方向的移动
#q是要水平方向要移动的总距离，qe是q/5的整数部分，如果移动qe*5足底啊会产生4像素误差，所以第五次移动修正了
#qq是竖直方向的移动，3和-3交替
def dra(q):
    action = webdriver.ActionChains(dr)
    s=dr.find_element_by_id('dx_captcha_basic_slider_1')
    action.click_and_hold(s).perform()
    time.sleep(0.15)
    qe,qq=int(q/5),3
    for i in range(5):
        if i==4:
            qe=q-4*qe
        print('第{}步移动{}'.format(i,qe))
        
        #下面这个方法用来相当移动
        action.move_by_offset(qe,qq).perform()
        time.sleep(0.15)
        qq=-qq
        
        #重新创建action，否则移动距离会累加，即（qe,qe*2,qe*3,qe*4,q）
        action = webdriver.ActionChains(dr)
    time.sleep(0.15)
    
    #松开左键
    action.release().perform()

    
def main():
    drawpic()   
    
    #下面这个方法实现了图到数组的转换，数组到图的转换用p1=Image.fromarray(d1）
    #q1，q2分别是两个验证码图的数组
    #需要特别注意数组转换后的默认数据格式是uint8（查看方法是dtype），貌似只能表示0-255的整数，
    #-3会自动转成253，所以用astype转换成int
    q1=np.array(Image.open('1.jpg')).astype(int)
    q2=np.array(Image.open('2.jpg')).astype(int)
    
    #q3是两个图的差，q4是q3的绝对值，q4的shape是150*300*4,接下来需要计算每个点rgb的和的差，
    #对axis=2维度求和就可以计算该店rgb的和，q5就是rgb的和，shape是150*300
    q3=q1-q2
    q4=np.where(q3>=0,q3,-q3)
    q5=q4.sum(axis=2)
    
    #yz是q5的阈值，大于yz则标记不同，小于yz标记相同，q6是q5里满足q5>yz的点
    #这里用argwhere，直接获取q5里满足条件的数据，如果用where会返回q5形状的True和False数组
    q6=np.argwhere(q5>yz)
    
    #接下来的思路是选择竖直坐标为x的一条横向，将横坐标小于66的作为被移动图形的横坐标集合，
    #将横坐标小于66的作为被填补图形的横坐标集合，y1和y2分别是这两个集合的均值
    #q7是q6里竖直坐标为x的点在q6里的index的集合，x取q6的1/6处的点，因为验证码图1下部有汉字，
    #导致后面大部分数据无法使用
    #q6=q6[q7]是将q7作为index传给q6，更新q6成原来的q6竖直坐标为x的点的集合
    x=q6[int(q6.shape[0]/6)][0]
    q7=np.where(q6[:,0]==x)
    q6=q6[q7]
    y1=np.average(q6[q6[:,1]<66][:,1])
    y2=np.average(q6[q6[:,1]>66][:,1])
    
    #y表示要移动的横坐标
    y=int(abs(y1-y2))
    print('原图横坐标是{}'.format(y1))
    print('新图横坐标是{}'.format(y2))
    print('移动向量是{}，纵坐标是{}'.format(y,x)) 
    
    #进行移动，返回q5是为了画图验证
    dra(y)
    return q5


#将main（）返回的q5画图
def huatu(q5):
    q7=np.where(q5>yz,255,0)
    p7=Image.fromarray(q7)
    p7.show()

    
    
#count用来计算第几次进行验证操作，没实际作用；yz暂时取100；
#wind用来记录弹出了几个新验证码窗口，该网页每弹一次窗口，id会自动加1
#验证成功且不弹出窗口的话，会出现su元素，检测到su元素则退出循环

count=1
yz=100
wind=2
while True:  
    q5=main()
    time.sleep(2)
    try:
        dr.find_element_by_id('dx_captcha_clickword_tr-btn-close_{}'.format(wind)).click()
        wind+=1
    except Exception:
        pass
    try:
        su=WebDriverWait(dr,3).until(EC.visibility_of_element_located((By.CLASS_NAME ,
                                         'dx_captcha_basic_lang_verify_success')))
        break
    except Exception as e:
        print('第{}次失败了，继续抓取'.format(count))
        count+=1

huatu(q5)
