import numpy as np
import cv2

def function(img):
    height,width,channel = img.shape
    emptyImage = np.zeros((800,800,channel),np.uint8)
    sh = 800/height
    sw = 800/width
    for x in range(800):
        for y in range(800):
            x0 = int(x/sw + 0.5)
            y0 = int(y/sh + 0.5)
            emptyImage[x,y] = img[x0,y0]
    return emptyImage
image = cv2.imread("lenna.png")
picture = function(image)
print(picture)
print(picture.shape)
cv2.imshow("after picture",picture)
cv2.imshow("origin picture",image)
cv2.waitKey(0)