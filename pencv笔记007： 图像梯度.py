import cv2
import numpy as np
from matplotlib import pyplot as plt


'''
#http://www.cnblogs.com/Undo-self-blog/p/8436389.html
这一部分完全不看不懂，但看效果似乎是用来提取文本的
目标
　　• 图像梯度，图像边界等
　　• 使用到的函数有：cv2.Sobel()，cv2.Schar()，cv2.Laplacian() 等

原理
　　梯度简单来说就是求导。
　　OpenCV 提供了三种不同的梯度滤波器，或者说高通滤波器：Sobel，Scharr 和 Laplacian。我们会一一介绍他们。
　　Sobel，Scharr 其实就是求一阶或二阶导数。Scharr 是对 Sobel（使用小的卷积核求解求解梯度角度时）的优化。
  Laplacian 是求二阶导数。
  '''


img = cv2.imread('wz.jpg',0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()
