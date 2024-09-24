import cv2
import numpy as np
import random

def jiaoyan(img,percentage):
    dst=img
    per=int(img.shape[0]*img.shape[1]*percentage)
    for i in range(per):
        randx=random.randint(0,img.shape[0]-1)
        randy=random.randint(0,img.shape[1]-1)
        if random.random()<0.5:
            dst[randx,randy]=0
        else:
            dst[randx,randy]=255
    return dst

img=cv2.imread("lenna.png",0)
img1=jiaoyan(img,0.8)
img=cv2.imread("lenna.png")
img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("beforepicture",img2)
cv2.imshow("afterpicture",img1)
cv2.waitKey(0)