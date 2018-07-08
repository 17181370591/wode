import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('2.jpg',0)
a,b=100,200
cv2.namedWindow('a')
def nothing(x):
    pass

cv2.createTrackbar('low','a',100,200,nothing)
cv2.createTrackbar('high','a',0,255,nothing)
for a in range(10,300,30):
    print(a)
    edges = cv2.Canny(img,a,a+150)
    cv2.imshow('a',edges)
    cv2.waitKey(0)

'''
while 1:
    cv2.imshow('a',edges)
    cv2.waitKey(0)
    a=cv2.getTrackbarPos('low','a')
    b=cv2.getTrackbarPos('high','a')
    print(a,b)
    edges = cv2.Canny(img,a,a*2)
'''
    

