import numpy as np
import cv2
import random

def gauss(img,mean,variance,percentage):
    dst=img
    width,height=img.shape[0],img.shape[1]
    per=int(width*height*percentage)
    for i in range(per):
        randx=random.randint(0,width-1)
        randy=random.randint(0,height-1)
        dst[randx,randy]=img[randx,randy]+random.gauss(mean,variance)
        if dst[randx,randy]<0:
            dst[randx,randy]=0
        elif dst[randx,randy]>255:
            dst[randx.randy]=255
    return dst

img=cv2.imread("lenna.png",0)
img1=gauss(img,100,100,0.8)
img=cv2.imread("lenna.png")
img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("beforepicture",img2)
cv2.imshow("afterpicture",img1)
cv2.waitKey(0)