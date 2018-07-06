import numpy as np
import cv2

# Create a black image
img = np.ones((512,512,3), np.uint8)*166

# Draw a diagonal blue line with thickness of 5 px
cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.rectangle(img,(388,0),(510,128),(0,255,0),-3)
cv2.circle(img,(128,388),128,(0,0,255),1)
cv2.ellipse(img,(256,256),(100,50),30,0,270,(0,255,255),2)

pts = np.array([[10,5],[20,30],[50,10],[70,20]])
print(pts)
pts = pts.reshape((-1,1,2))
print(pts)
cv2.polylines(img,[pts],False,(0,255,255))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(256,499), font, 2,
            (255,255,255),2,cv2.LINE_AA)
cv2.imshow('',img)
