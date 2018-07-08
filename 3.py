'''
轮廓近似
　　将轮廓形状近似到另外一种由更少点组成的轮廓形状，新轮廓的点的数目由我们设定的准确度来决定。使用的Douglas-Peucker算法，你可以到维基百科获得更多此算法的细节。
为了帮助理解，假设我们要在一幅图像中查找一个矩形，但是由于图像的种种原因，我们不能得到一个完美的矩形，而是一个“坏形状”（如下图所示）。
现在你就可以使用这个函数来近似这个形状（）了。这个函数的第二个参数叫epsilon，它是从原始轮廓到近似轮廓的最大距离。它是一个准确度参数。选择一个好的 epsilon 对于得到满意结果非常重要。
'''
import numpy as np
import cv2
import cv2
import numpy as np
def f(contours):
    x=0
    for i in range(len(contours)):
        if len(contours[i])>x:
            x=i
    return x
yz=177
img1 = cv2.imread('oo.jpg')
img = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY) 
ret,thresh = cv2.threshold(img,yz,255,0)
image,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,3)
x=f(contours)
cnt = contours[x]
M = cv2.moments(cnt)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])         #重心的坐标
area = cv2.contourArea(cnt)         #轮廓面积
perimeter = cv2.arcLength(cnt,True)         #轮廓周长
epsilon = 0.0001*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)
img3= cv2.drawContours(img1, list(approx), -1, (0,0,255),2)
cv2.imshow('',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

img2= cv2.drawContours(img1, contours, x, (0,0,255),2)
cv2.imshow('',img2)


