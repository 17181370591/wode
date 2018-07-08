import cv2,os
import numpy as np,sys

nu=0
mm=6
p=os.getcwd()+'\\1\\{}.jpg'
A = cv2.imread('3.jpg')
B = cv2.imread('q2.jpg')
print(p.format(nu),A.shape,B.shape)
# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in range(mm):
    G = cv2.pyrDown(G)
    gpA.append(G)
    #print(G.shape,'11')
    cv2.imwrite(p.format(nu),G)
    nu+=1

# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in range(mm):
    G = cv2.pyrDown(G)
    gpB.append(G)
    #print(G.shape,'22')
    cv2.imwrite(p.format(nu),G)
    nu+=1

# generate Laplacian Pyramid for A
lpA = [gpA[mm-1]]
for i in range(mm-1,0,-1):
    GE = cv2.pyrUp(gpA[i])
    #print(gpA[i-1].shape,GE.shape)
    x,y,z=gpA[i-1].shape
    L = cv2.subtract(gpA[i-1],GE[:x,:y,:z])
    lpA.append(L)
    #print(L.shape,'33')
    cv2.imwrite(p.format(nu),L)
    nu+=1

# generate Laplacian Pyramid for B
lpB = [gpB[mm-1]]
for i in range(mm-1,0,-1):
    GE = cv2.pyrUp(gpB[i])
    x,y,z=gpA[i-1].shape
    L = cv2.subtract(gpB[i-1],GE[:x,:y,:z])
    lpB.append(L)
    #print(L.shape,'44')
    cv2.imwrite(p.format(nu),L)
    nu+=1

# Now add left and right halves of images in each level
LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    print(la.shape,lb.shape)
    he=int(cols/2)
    ls = np.hstack((la[:,0:he], lb[:,he:]))
    LS.append(ls)
    cv2.imwrite(p.format(nu),ls)
    nu+=1

# now reconstruct
ls_ = LS[0]
for i in range(1,mm):
    ls_ = cv2.pyrUp(ls_)
    #print(ls_.shape,LS[i].shape)
    x,y,z=LS[i].shape
    ls_ = cv2.add(ls_[:x,:y,:z], LS[i])
    cv2.imwrite(p.format(nu),ls_)
    nu+=1

# image with direct connecting each half
he=int(cols/2)
real = np.hstack((A[:,:he],B[:,he:]))

cv2.imwrite('1/Pyramid_blending2.jpg',ls_)
cv2.imwrite('1/Direct_blending.jpg',real)
