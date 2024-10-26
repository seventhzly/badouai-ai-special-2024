import matplotlib.pyplot as plt
import cv2

img=cv2.imread('lenna.png',flags=0)
cv2.imshow('canny',cv2.Canny(img,100,300))
cv2.waitKey(0)
cv2.destroyAllWindows()