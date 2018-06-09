from selenium import webdriver
import json,time,numpy as np,os,pandas as pd
from lxml  import etree
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from PIL import Image

dr = webdriver.Firefox()
u='http://jiyan.c2567.com/index.php/login/index'
dr.get(u)

cd=os.getcwd()
def getd(x,s1):
    p1=WebDriverWait(dr,10).until(EC.presence_of_element_located\
                             ((By.XPATH,x)))
    p1.screenshot(s1)
    time.sleep(3)
    p1=Image.open(cd+'\\'+s1)
    d1=np.array(p1)
    return d1

def drawpic():
    getd('//div[@id="dx_captcha_basic_bg_1"]/canvas','1.jpg')
    s=dr.find_element_by_id('dx_captcha_basic_slider_1')
    s.click()
    time.sleep(1)
    getd('//div[@id="dx_captcha_basic_bg_1"]/canvas','2.jpg')

def f(x):
    x=np.array(Image.open(x))
    return pd.DataFrame(x.flatten().reshape(150*300,4))
    
def g(x):
    return np.array(Image.open(x))

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
        action.move_by_offset(qe,qq).perform()
        time.sleep(0.15)
        qq=-qq
        action = webdriver.ActionChains(dr)
    time.sleep(0.15)
    action.release().perform()

def main():
    #global yz
    drawpic()   
    q1=g('1.jpg').astype(int)
    q2=g('2.jpg').astype(int)
    q3=q1-q2
    q4=np.where(q3>=0,q3,-q3)
    q5=q4.sum(axis=2)
    q6=np.argwhere(q5>yz)
    x=q6[int(q6.shape[0]/6)][0]
    q7=np.where(q6[:,0]==x)
    q6=q6[q7]
    y1=max(np.average(q6[q6[:,1]<66][:,1]),34)
    y2=np.average(q6[q6[:,1]>66][:,1])
    y=int(abs(y1-y2))
    print('原图横坐标是{}'.format(y1))
    print('新图横坐标是{}'.format(y2))
    print('移动向量是{}，纵坐标是{}'.format(y,x)) 
    dra(y)
    return q5

def huatu(q5):
    q7=np.where(q5>yz,255,0)
    p7=Image.fromarray(q7)
    p7.show()
    
count=1
yz=120
while True:  
    q5=main()
    time.sleep(2)
    try:
        z=dr.find_element_by_xpath('//div[contains(@id,"dx_captcha_clickword_tr-btn-close")]/img')
        print('找到新页面，将关闭')
        z.click()
        z.send_keys(13)
    except Exception:
        pass
    try:
        su=WebDriverWait(dr,3).until(EC.visibility_of_element_located\
            ((By.CLASS_NAME ,'dx_captcha_basic_lang_verify_success')))
        break
    except Exception as e:
        print('第{}次失败了，继续抓取'.format(count))
        count+=1

huatu(q5)
